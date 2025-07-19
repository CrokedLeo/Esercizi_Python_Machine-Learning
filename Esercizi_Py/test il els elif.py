num1 = (input("primo numero: "))
num2 = (input("secondo numero: "))
num3 = (input("terzo numero: "))

if num1 == num2 == num3:
    print("Tutti e tre i numeri sono uguali")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Ci sono due numeri uguali")
elif num1 > num2 and num1 > num3:
        print("Il numero più grande è:", num1)
elif num2 > num1 and num2 > num3:
        print("Il numero più grande è:", num2)
else:
        print("Il nimero più grande è:", num3)
