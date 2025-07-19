from random import randint

rnumbers = []
count = 0

while count < 5:
    num = randint(1,100)
    if num not in rnumbers:
        rnumbers.append(num)
    else:
        continue
    count += 1

numbers = [str(n) for n in rnumbers]
stringa = "/n".join(numbers)

with open("numeri.txt","w") as file:
     file.write(str(num)+"\n")

with open("numeri.txt","r") as file:
    contenuto = file.read().splitlines()

print(contenuto)


#try:
for j in range(2):
        num1 = input("Inserisci un numero: ")
        num2 = input("Inserisci un numero: ")
        
        if not num1.isdecimal() or not num2.isdecimal():
            print("Valore inserito non valido!")
            continue

        elif num1 in contenuto and num2 in contenuto:
            print("Hai indovinato!")
            break
        elif (num1 in contenuto or num2 in contenuto): 
            print("Hai indovinato solo un numero, mi dispiace!")
        else:
            print("Hai perso! Ritenta!")

#except ValueError:
    #print("Valore inserito non valido!")
#except:
    #print("Errore di sistema!")