import turtle as t
t.speed(0)
def draw_cross(size,cross):
    if cross == 0:
        t.dot(5)
    else:
        for _ in range(4):
            t.forward(size)
            draw_cross(size/2,cross-1)
            if cross ==1:
                t.dot(5)
            t.backward(size)
            t.right(90)
draw_cross(100,4)
t.exitonclick()
