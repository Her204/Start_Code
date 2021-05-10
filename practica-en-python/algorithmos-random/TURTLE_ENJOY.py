import turtle


hr = turtle.Turtle()
hr.speed(1000)

def tree(i,f):
    if i<10:
        return 
    else:
        hr.color("orange")
        hr.forward(i)
        hr.left(f)
        tree(3*i/4,f=3/4*f)
        hr.right(2*f)
        tree(3*i/4,f=3*f/4)
        hr.left(f)
        hr.backward(i)

def linear(val,angle,val2):
    if val < 10:
        return
    else:
        hr.forward(val)
        hr.left(angle)
        hr.forward(val2)
        hr.right(angle*2)
        hr.forward(val2)
        hr.left(angle*3)
        hr.forward(val)
        linear(3/4*val,angle=angle,val2=3/4*val2)

def circle_practice(val):
    if val < 10:
        return
    else:
        hr.color("green")
        hr.circle(val)
        circle_practice((8/13)*val)

def geometry_general(val,side):
    angle = 360/side
    hr.speed(2000)
    hr.color("brown")
    for a in range(1,side+1):
         hr.forward(val)
         hr.left(angle)
   

def geometry_loop(val,side,one):
    if val < 10:
        return
    else:
        geometry_general(val,side)
        geometry_loop(3*val/4,side=side+one,one=one)


for a in range(1,3):
    hr.left(180)
    geometry_loop(100,12,-1)


turtle.done()