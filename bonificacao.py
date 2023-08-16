"""salario = float(input("Digite o seu salario: "))
r1 = salario + (salario * 20/100)
r2 = salario + (salario * 15/100)
r3 = salario + (salario * 10/100)
r4 = salario + (salario * 5/100)

if salario <= 280:
    print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",r1)
elif salario > 280 and salario <= 700:
       print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",r2)
elif salario > 700 and salario <= 1500:
       print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",r3)
elif salario > 1500:
       print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",r4)"""
       
salario = float(input("Digite o seu salário: "))

if salario <= 280:
    convertido = salario + (salario * 20/100)
    print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",convertido)
    
elif salario > 280 and salario <= 700:
    convertido = salario + (salario * 15/100)
    print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",convertido)
    
elif salario > 700 and salario <= 1500:
    convertido = salario + (salario * 10/100)
    print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",convertido) 
       
elif salario > 1500:
    convertido = salario + (salario * 5/100)
    print("Seu salario antes do reajuste era de R$", salario, ". Agora é de R$",convertido)
