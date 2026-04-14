casa = float(input('Qual o valor da casa?'))
salario = float(input('Qual o seu salario?'))
anos = int(input('Em qnts anos você deseja pagar a casa?'))
prestacao = casa / (anos*12)
if prestacao > salario*0.30:
    print(f'A casa no valor de {casa} com o salario de {salario}sendo pago durante {anos} anos tera o empristimo \033[31m recusado \033[m')
elif prestacao < salario*0.30:
     print(f'A casa no valor de {casa} com o salario de {salario}sendo pago durante {anos} anos tera o empristimo \033[32m aprovado \033[m')