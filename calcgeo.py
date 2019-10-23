import turtle
import time
import math
while True:
    medtotal=0
    angulos = list()
    lados = list()
    totalmedlados = 0
    hipotenusa = bool
    numangulos = int(input("Digite quantos angulos tem a forma: "))
    simetrico = input("A forma é simétrica?: ").lower()[0]
    while simetrico not in "sn":
        print("Dado inválido, repita!")
        simetrico = input("A forma é simétrica?: ").lower()[0]

    if simetrico == "n":
        
        for c in range(1,numangulos + 1):
            angulos.append(int(input(f"Digite o valor do {c} angulo: ")))
            lados.append(int(input(f"Digite a medida do lado {c}: ")))
        for c in range(0,numangulos):
            medtotal += angulos[c]
        for c in range(0,numangulos):
            totalmedlados += lados[c]
    if simetrico == "s":
        medtotal = (numangulos -2) * 180
        medidaangulo = medtotal/numangulos

    if medtotal != (numangulos -2)*180 and simetrico=="n":
        print("REPITA, FORMA INVÁLIDA!")
        continue
    else:
        break
form = turtle.Turtle()
form.color("black")
form.pensize(5)
form.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=0.1)
if simetrico == "s":
    for c in range (0,numangulos):
        form.speed(1)
        form.forward(100)
        form.left(180 - medidaangulo)
if simetrico == "n":
    if numangulos == 3:
        form.forward(lados[0])
        form.left(180 - angulos[0])
        form.forward(math.hypot(lados[0], lados[2]))
        form.left(180 - angulos[1])
        form.forward(lados[2])
        hipotenusa == True
    if hipotenusa == False: 
        for c in range (0,numangulos):
            form.speed(1)
            form.forward(lados[c])
            form.left(180 - angulos[c])
time.sleep(100)
