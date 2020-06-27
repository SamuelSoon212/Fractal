while True:
    angle = input("Enter angle(10-170): ")
    try:
        angle = float(angle)
        if angle < 10 or angle >170:
            raise ValueError
        break
    except ValueError:
        print("Invalid")

left(90)
penup()
backward(300)
pendown()
speed(9999999)

def draw(length, depth):
    if depth == 11:
        return
    forward(length)
    left(angle)
    draw(0.707*length,depth+1)
    right(2*angle)
    draw(0.707*length,depth+1)
    left(angle)
    backward(length)

draw(140,0)
mainloop()
