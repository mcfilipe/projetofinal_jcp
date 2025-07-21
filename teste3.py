import turtle
import random

# === Funções ===

def escolher_paleta():
    print("Escolhe uma paleta de cores:")
    print("1. Quente (vermelho, laranja, amarelo)")
    print("2. Fria (azul, verde, roxo)")
    print("3. Aleatória")
    escolha = input("Opção (1/2/3): ")
    if escolha == "1":
        return ["red", "orange", "yellow"]
    elif escolha == "2":
        return ["blue", "green", "purple"]
    else:
        return ["red", "orange", "yellow", "green", "blue", "purple", "white"]

def desenhar_poligono(t, cor):
    t.color(cor)
    t.begin_fill()
    lados = random.randint(3, 8)
    tamanho = random.randint(20, 100)
    for _ in range(lados):
        t.forward(tamanho)
        t.right(360 / lados)
    t.end_fill()

def desenhar_circulo(t, cor):
    t.color(cor)
    t.begin_fill()
    raio = random.randint(10, 80)
    t.circle(raio)
    t.end_fill()

def gerar_arte(numero, paleta, forma):
    turtle.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    for _ in range(numero):
        t.penup()
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.setheading(random.randint(0, 360))
        t.pendown()
        cor = random.choice(paleta)
        if forma == "1":
            desenhar_circulo(t, cor)
        else:
            desenhar_poligono(t, cor)

    turtle.done()

# === Programa Principal ===

print("🖌️ Gerador de Arte Abstrata 🖌️")
formas = input("Queres desenhar (1) círculos ou (2) polígonos aleatórios? ")
quantidade = int(input("Quantas formas queres desenhar? "))
paleta = escolher_paleta()

gerar_arte(quantidade, paleta, formas)
