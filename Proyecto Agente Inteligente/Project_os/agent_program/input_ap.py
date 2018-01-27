import re
from commands import commands
from text_ops import flattenDicts, flattenTexts, separators
from pattern.text.es import *
from pattern.text.es import conjugate
from pattern.text.es import PRESENT, PAST, FUTURE, INFINITIVE, SG, PL
from pattern.text.es import INDICATIVE, IMPERATIVE, CONDITIONAL, SUBJUNCTIVE
from pattern.text.es import IMPERFECTIVE, PERFECTIVE, PROGRESSIVE
import speech_recognition as  sr

DISTANCE_THRESHOLD = 50
# http://www.clips.ua.ac.be/pages/pattern-es

# Verb tenses
TENSES = [INFINITIVE, PRESENT, PAST, FUTURE]

# Verb persons
PERSONS = [1, 2, 3]

# Verb numerals
NUMBERS = [SG, PL]

# Verb moods
MOODS = [INDICATIVE, IMPERATIVE, CONDITIONAL, SUBJUNCTIVE]

# Verb aspects
ASPECTS = [IMPERFECTIVE, PERFECTIVE, PROGRESSIVE]

# Expands a 'lemma' form, whose root is 'root' and is function is 'function'
# It returns a list of all lemma derived 
def expandARoot(function, root):

    expanded = {}

    if function == "V":
        for tense in TENSES:
            for mood in MOODS:
                for aspect in ASPECTS:
                    for person in PERSONS:
                        for number in NUMBERS:
                            lexeme = conjugate(root,
                                               tense=tense,
                                               person=person,
                                               number=number,
                                               mood=mood,
                                               aspect=aspect,
                                               negated=False)
                            if lexeme is not None:
                                expanded[lexeme] = True
    if function == "N":
        # Singular
        expanded[root] = True
        # Plural
        expanded[pluralize(root)] = True

    if function == "A":
        expanded[root] = True
        expanded[attributive(root, PLURAL)] = True
        expanded[attributive(root, FEMALE)] = True
        expanded[attributive(root, FEMALE + PLURAL)] = True

    return expanded.keys()


# Expands a whole expression ('text' argument), searching for 'lemma' tokens and expanding them accordingly
# # It returns a list
def expandText(text, lang):

    # TODO: Implement other languages here
    if lang == "es":
        return expandTextTwo([text])
    else:
        return [text]


# Expands a whole expression ('text' argument), searching for 'lemma' tokens and expanding them accordingly
# It returns a list
def expandTextTwo(textList):

    toExpand = textList

    expansion = []

    someExpanded = False

    for text in toExpand:

        matchObj = re.search(r'(.*)(\w\(.*?\))(.*)', text)

        if matchObj:

            someExpanded = True

            if len(matchObj.group(1)) > 0:
                head = matchObj.group(1)
            else:
                head = ""

            if matchObj.group(3) is not None:
                tail = matchObj.group(3)
            else:
                tail = " "

            toExpand = matchObj.group(2)
            function = toExpand[0]
            root = toExpand[2:-1]

            # print "Head %s Tail %s" % (head,tail)
            # print "Function %s Root %s" % (function,root)
            expandedList = expandARoot(function, root)

            # pprint.pprint(expandedList)

            for form in expandedList:
                expansion.append("".join([head, form, tail]))
        else:
            expansion.append(text)

    if someExpanded:
        return(expandTextTwo(expansion))
    else:
        return(expansion)

def load_commands(type_commands):

    dicts = {}
    expressions = {}

    for i, c in enumerate(commands[type_commands]):
        c = c.rstrip().decode("utf8")
        my_expr = c.split(",")
        expressions[i] = my_expr

    dicts[type_commands] = expressions

    return dicts

def prepare_commands(dicts):

    my_struct = {}

    for key, value in dicts.items():
        tag = key

        my_struct[tag] = {}

        for (index,entry) in value.items():
            pos_key = 0
            expanded_dict = {}
            for expression in entry:
                expanded = expandText(expression, "es")
                expanded_dict[pos_key] = expanded
                pos_key += 1

            # pprint.pprint(expanded_dict)

            final_exp = []
            if 1 in expanded_dict:
                for i in range(0, len(expanded_dict[0])):
                    for j in range(0, len(expanded_dict[1])):
                        final_exp.append(
                            [flattenDicts['es'](expanded_dict[0][i]).lower(),
                                flattenDicts['es'](expanded_dict[1][j]).lower()])
            else:
                for i in range(0, len(expanded_dict[0])):
                    final_exp.append([flattenDicts['es'](expanded_dict[0][i]).lower()])

            my_struct[tag][index] = final_exp

    return my_struct

def get_match(text, type_commands):

    text = text.lower()
    text = text.split()
    dicts = load_commands(type_commands)
    my_dicts = prepare_commands(dicts)
    rules = {}
    for my_dict in my_dicts.values():
        for index,expr in my_dict.items():
            for element in expr:
                element_index = 0
                matches = {}
                for e in element:
                    element_index += 1
                    if str(e) in text:
                        matches[element_index] = 1    
                    else:
                        matches[element_index] = 0
                if len(matches) == 2:        
                    if matches[1] and matches[2]: #hace match a las dos palabras del comando
                        return (True, index)
                if len(matches) == 1: #match con la unica palabra del comando
                    if matches[1]:
                        return (True, index)


def machine_recognition():
    #r.adjust_for_ambient_noise(source, duration = 1)
    global text
    text =""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text = str(r.recognize_google(audio, language='es-PE'))
        print("J-bot thinks you said << " + text + " >>")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return text