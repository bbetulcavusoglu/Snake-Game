import random
from tkinter import X
import turtle
import time

hiz=0.15

pencere= turtle.Screen()
pencere.title("Snake Game")
pencere.bgcolor("green")
pencere.setup(width=600, height=600)
pencere.tracer(0)#Pencerremizin güncellenmesine engel oluyoruz çünkü update komutuyla penceremizi güncelleyeceğiz

#Yılanın kafasını oluşturalım
#Turtle dan bir nesne oluşturuyoruz
kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape("square")
kafa.color("black")
kafa.penup()#kafa hareket ederken herhangi bir yazı yazmaması için
kafa.goto(0, 100)
kafa.direction ='stop'

#yemek ekliyoruz
yemek = turtle.Turtle()
yemek.speed(0)
yemek.shape("circle")
yemek.color("red")
yemek.penup()#kafa hareket ederken herhangi bir yazı yazmaması için
yemek.goto(0, 0)
yemek.shapesize(0.80, 0.80)

#Kuyruk ekleme yemek yiyince
kuyruklar=[]

#Puan sistemi
puan=0
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape("square")
yaz.color("white")
yaz.penup()
yaz.goto(0, 260)
yaz.hideturtle()#herhangi bir şekli olmaması için, şekil kapandı
yaz.write("PUAN: {}".format(puan), align="center", font=("Courier", 24, "normal"))

def move():
    if kafa.direction == "up":
        y=kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction == "down":
        y=kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction == "right":
        x=kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction == "left":
        x=kafa.xcor()
        kafa.setx(x-20)

def goUp():
    if kafa.direction != "down":
        kafa.direction = "up"
def goDown():
    if kafa.direction != "up":
        kafa.direction = "down"
def goRight():
    if kafa.direction != "left":
        kafa.direction ="right"
def goLeft():
    if kafa.direction != "right":
        kafa.direction = "left"


#kalvye kontrolü
pencere.listen()
pencere.onkey(goUp, "Up")
pencere.onkey(goDown, "Down")
pencere.onkey(goRight, "Right")
pencere.onkey(goLeft, "Left")


while True:
    pencere.update()
    #Pencereye çarpınca oyunu sıfırlama
    if kafa.xcor()>300 or kafa.ycor()>300 or kafa.ycor()<-300 or kafa.xcor()<-300 :
        time.sleep(1)
        kafa.goto(0,0)
        kafa.direction= "stop"

        for kuyruk in kuyruklar:
            kuyruk.goto(1000, 1000)
        
        kuyruklar=[]
        puan= 0
        yaz.clear()
        yaz.write("PUAN: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        hiz=0.15

    #Rasgele olarak yemğin değişmesi
    if kafa.distance(yemek)< 20:
        x=random.randint(-250, 250)
        y=random.randint(-250, 250)
        yemek.goto(x, y)

        puan +=10
        yaz.clear()
        yaz.write("PUAN: {}".format(puan), align="center", font=("Courier", 24, "normal"))
        #her yemek yediğimizde hızımızı düşürüyoruz
        hiz= hiz-0.001

        yeniKuyruk= turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape("square")
        yeniKuyruk.color("black")
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range (len(kuyruklar) -1, 0, -1):
            x=kuyruklar[i-1].xcor()
            y=kuyruklar[i-1].ycor()
            kuyruklar[i].goto(x,y)


    if len(kuyruklar)>0:
            x=kafa.xcor()
            y=kafa.ycor()
            kuyruklar[0].goto(x, y)

    move()
    time.sleep(hiz)
        

