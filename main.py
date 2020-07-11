from turtle import *

anglelist = [10,30,60,90,135]

print("\
1) 10 degrees\n\
2) 30 degrees\n\
3) 60 degrees\n\
4) 90 degrees\n\
5) 135 degrees")
while True:
  choice = input("Enter choice: ")
  try:
    choice = int(choice)
    if choice not in range(1, 6):
      raise ValueError
    break
  except ValueError:
    print("Error")

angle = anglelist[choice-1]

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
