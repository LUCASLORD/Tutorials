print('''2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha 
igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações''')

cond = True

while cond:
	usuario = str(input('Informe seu usuário: '))
	senha = str(input('Informe sua senha: '))
	if senha == usuario:
		print('Senha não pode ser igual usuario, informe novamente')
		cond = True
	else:
		print('Login Válido')
		cond = False
