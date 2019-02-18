simpson= int(input("Introduzca un número: "))

def juego(simpson):
    simpsons = ['Bart', 'Homer', 'Lisa', 'Ralph']
    for i in range(len(simpsons)):
        if i == simpson:
            return (simpsons[i])
print(juego(simpson))
