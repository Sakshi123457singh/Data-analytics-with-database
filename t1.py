from turtle import *
speed ('slowest')
pencolor('red')
for i in range(6,40,2 ): #range(stop), range(start,stop) , range(start , stop, step)
    fd(120)
    lt(360/6)
    dot(10,'green')
    write(i,font=('calibari',20, 'bold'))
#reverse
goto(100,100)
for i in range(10,0,-1):
    fd(60)
    lt(360/10)
    dot(10, 'yellow')
    write(i, font=('calibari',20, 'bold'))
mainloop()
