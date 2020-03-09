import turtle


def main():
    window = turtle.Screen()
    daniel = turtle.Turtle()

    make_square(daniel)
    
    turtle.mainloop()


def make_square(daniel):
    length = int(input('Tamaño cuadrado: '))
    for i in range(4):
        make_line_and_turn(daniel, length)


def make_line_and_turn(daniel, length):
    daniel.forward(length)
    daniel.left(90)


if __name__ == '__main__':
    main()
