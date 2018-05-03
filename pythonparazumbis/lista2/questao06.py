print('''6 - Faça Um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o imposto de 
Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário líquido. Calcule 
os descontoes e o salário líquido, conforme tabela abaixo:
		a. + Sálario Bruto: R$
		b. - IR(11%): R$
		c. - INSS(8%): R$
		d. - Sindicato(5%): R$
		e. = Salário Líquido: R$''')

valorhora = float(input('Informe o Valor por Hora Trabalhada: '))
qtdhora = int(input('Informe a quantidade de Horas Trabalhadas: '))

salariobruto = valorhora * qtdhora
ir = salariobruto * 11 / 100
inss = salariobruto * 8 / 100
sindicato = salariobruto * 5 /100
salarioliquido = salariobruto - (ir + inss + sindicato)

print('''Tabela de Valores
	a. + Sálario Bruto: R$ {}
	b. - IR(11%): R$ {}
	c. - INSS(8%): R$ {}
	d. - Sindicato(5%): R$ {}
	e. = Salário Líquido: R$ {}'''.format(salariobruto,ir,inss,sindicato,salarioliquido))
