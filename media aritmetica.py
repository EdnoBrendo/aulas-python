n1 = float(input("Digite qual foi sua primeira nota: "))
n2 = float(input("Digite qual foi sua segunda nota: "))
media = (n1 + n2) / 2

if media < 4:
    print("Sua nota tem conceito E ")
    
elif media >= 4 and media < 6:
    print("Sua nota tem conceito D ")
    
elif media >= 6 and media < 7.5: 
    print ("Sua nota tem conceito C")
    
elif media >= 7.5 and media < 9:
    print("Sua nota tem conceito B")
    
elif media >= 9 and media <= 10:
    print("Sua nota tem conceito A")
    
else:
    print("Suas notas são inválidas")
