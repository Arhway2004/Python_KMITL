import turtle as a

def asa(number):
    a.penup()
    a.left(90)
    a.forward(number/2)
    a.right(90)
    a.backward(number/2)
    a.pendown()
    for x in range(4):
        a.forward(number)
        a.right(90)
    a.penup()
    a.forward(number/2)
    a.right(90)
    a.forward(number/2)
    a.left(90)

def asaa(number):
    while number>=5:
        asa(number)
        # a.right(10)
        number-=10
        
asaa(200)
a.done()
