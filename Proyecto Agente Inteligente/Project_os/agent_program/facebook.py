from pattern.web import Facebook, NEWS, COMMENTS, LIKES

fb = Facebook(license='CAACEdEose0cBAD0FqhYX26Tg9h7062f5KxELjcZC6mt91UeyRYNeUJb8WZA\
	eJZCELWSCqqeTL7SkwbVkgyV3PxVXCnNoa0o6ywdNtSa0AmW8n7oifV5l5ImQZBBXSWD9lEE8o4pggBz\
	p9NLV5x4vqcwdyW2xZB9CcHCylZBqURoQqrwZBcpTdZATZCs5BkX0WP964JdWoO7quMg40HImUv6WA')

me = fb.profile(id='10203550007847585') 

def get_posts():
	for post in fb.search(me[0], type=NEWS, count=10):
		print 'post :'+ repr(post.text) +' likes :'+ repr(post.likes)

#Navegue, acceda al chat, mire videos, revise sus correos y redes sociales desde su celular. 
#Recargue el saldo de su telefono y adquiera el Paquete de Internet en cualquier momento y lugar. Solo tiene que enviar un mensaje de texto al 779 con la palabra clave indicada en el siguiente recuadro:
#200 MB	5D
#700 MB	10D