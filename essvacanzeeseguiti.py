
#Esercizio 1: Lista dei numeri primi

#Definire una funzione per determinare se un numero è primo.
#Un numero primo è un numero maggiore di 1 che non ha divisori tranne 1 e se stesso.

def e_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#Creare una funzione che restituisca una lista dei primi n numeri primi.
#Utilizzare un ciclo while per continuare a cercare numeri primi fino a quando la lunghezza della lista non raggiunge n.

def primi_n_numeri(n):
    numeri_primi = []
    numero = 2
    while len(numeri_primi) < n:
        if e_primo(numero):
            numeri_primi.append(numero)
        numero += 1
    return numeri_primi

#Raccogliere l'input dall'utente e stampare i risultati.

n = int(input("Inserire un numero n: "))
print(f"I primi {n} numeri primi sono: {primi_n_numeri(n)}")


#--------------------------------------------------------------------------------------------------



#Esercizio 2: Fibonacci con Selezione

#Definire una funzione per calcolare l'n-esimo numero della sequenza di Fibonacci.
#Per questo, possiamo utilizzare un approccio iterativo.

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

#Raccogliere l'input dall'utente e stampare i risultati.

n = int(input("Inserire un numero n: "))
print(f"Il {n}-esimo numero nella sequenza di Fibonacci è: {fibonacci(n)}")

# Nota: La funzione e_primo utilizza un approccio ottimizzato per determinare se un numero è primo. Invece di controllare ogni divisore possibile fino a num, controlla solo fino alla radice quadrata di num. Questo è sufficiente perché se num ha un divisore maggiore della sua radice quadrata, allora deve anche avere un divisore più piccolo di essa. Ad esempio, se 29 avesse un divisore maggiore di 5 (la sua radice quadrata approssimata), allora dovrebbe anche avere un divisore minore di 5, ma non ne ha, quindi 29 è primo.