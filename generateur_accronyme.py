import turtle
text = str(input('donner une chaine de caractère: '))


def accro_gen(chaine):

    mots = chaine.split()
    accro = ''
    for i in mots:
        accro = accro+str(i[0]).upper()
    return accro


resultat = accro_gen(text)
print(f"Voici l'accronyme : {resultat}")

pen = turtle.Turtle()


def curve():
    for i in range(200):

        pen.right(1)
        pen.forward(1)


def heart():

    pen.fillcolor('red')

    pen.begin_fill()

    pen.left(140)
    pen.forward(113)

    curve()
    pen.left(120)

    curve()

    pen.forward(112)

    pen.end_fill()


def txt():

    pen.up()

    pen.setpos(-68, 95)

    pen.down()

    pen.color('lightgreen')

    pen.write(f"         {resultat}", font=(
        "Verdana", 12, "bold"))
    turtle.exitonclick()


heart()

txt()

pen.ht()
