from pattern.web import Mail, GMAIL, SUBJECT

def check_spam():
	gmail = Mail(username='...', password='...', service=GMAIL)
	i = gmail.spam.search('oferta', field=SUBJECT)[0] 
	m = gmail.spam.read(i)
	print '   From:', m.author
	print 'Subject:', m.subject
	print 'Message:'
	print m.body
 