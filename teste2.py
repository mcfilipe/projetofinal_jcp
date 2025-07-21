import turtle
import random

# Configuração da janela
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # Velocidade máxima

# Paleta de cores
cores = ["red", "yellow", "blue"]

# Função para desenhar formas aleatórias
def desenhar_forma():
    t.penup()
    t.goto(random.randint(-300, 300), random.randint(-300, 300))
    t.pendown()
    t.color(random.choice(cores))
    t.begin_fill()
    lados = random.randint(3, 8)
    tamanho = random.randint(20, 100)
    for _ in range(lados):
        t.forward(tamanho)
        t.right(360 / lados)
    t.end_fill()

# Gerar várias formas
for _ in range(50):
    desenhar_forma()

turtle.hideturtle()
turtle.done()
