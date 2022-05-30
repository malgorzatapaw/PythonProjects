num = 0
operation = None
reset = True
result = None
calcOperations = ["+", "-", "*", "/", "**"]

while True:
    if reset == True:
        num = int(input("Podaj liczbe startowa:"))
        reset = False

    operation = input("Podaj operacje arytmetyczna jak np."
        + str(calcOperations) + " lub exit jesli koniec lub reset: ")
    if operation == "exit" : break
    if operation == "reset":
        reset = True
        continue

    if not operation in calcOperations:
        print("wprowadzona zostala bledna operacja")
        continue
    secondNum = input("podaj druga liczbe: ")

    if operation == "+":
        result = int(num) + int(secondNum)

    if operation == "-":
        result = int(num) - int(secondNum)

    if operation == "*":
        result = int(num) * int(secondNum)

    if operation == "/":
        result = int(num) / int(secondNum)

    if operation == "**":
        result = int(num) ** int(secondNum)

    print("wynik operacji" + str(num) + " " + operation + " " + str(secondNum) + " = " + str(result))

    num = result
    result = None