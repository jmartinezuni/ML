# -*- coding: utf-8 -*-
'''
__author__ = '@oscarmarinmiro'
'''


# Makes a flattened version of text coming from a dictionary or a text
def flattenDict(text):
    text = text.encode('utf-8')
    text = text.lower()
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    text = text.replace('à', 'a')
    text = text.replace('è', 'e')
    text = text.replace('ì', 'i')
    text = text.replace('ò', 'o')
    text = text.replace('ù', 'u')
    text = text.replace('ü', 'u')
    text = text.replace('ï', 'i')
    text = text.replace('l·l', 'll')
    text = text.replace('l•l', 'll')
    text = text.replace('l.l', 'll')
    text = text.replace('l·l', 'll')
    text = text.replace('\t', ' ')
    text = text.replace('\n', ' ')
    text = text.replace("\\", ' ')
    text = text.replace('á', 'a')
    text = text.replace('é', 'e')
    text = text.replace('í', 'i')
    text = text.replace('ó', 'o')
    text = text.replace('ú', 'u')
    text = text.replace('"', ' ')
    # text = text.replace('#', '')
    text = text.decode('utf-8')
    
    return text

flattenDicts = {'es': flattenDict}
flattenTexts = {'es': flattenDict}

# Ojo con la comillas-family. Lista de expresiones que pueden usarse como 'separadores'
# en las expresiones regulares
separators = {'es': [" ", "!", "¡", "¿", "?", ",", ".", ";", "(", ")", r'"', r"'", r'‘', r'“', r'“', r":", "-", "]", "[",
                     r'«', r'»', r'“', r'”', r"’", "#", "%"
                     "\t", "\n", "\r"]}
