from turtle import*
speed('fastest')
colors=['orange','skyblue','red','green']
pensize(5)
for i in range(100):
    #print(i%4,colors[i%4])
    pencolor(colors[i%4])
    fd(i*3)
    #fd(i+140)
    lt(60)
    circle(i*2,67)
mainloop()