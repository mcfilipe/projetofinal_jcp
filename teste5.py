import turtle
import random
import tkinter as tk
from tkinter import simpledialog
from PIL import Image
import os

# === Funções ===

def escolher_paleta():
    return ["red", "orange", "yellow", "green", "blue", "purple", "white"]

def desenhar_poligono(t, cor, tamanho):
    t.color(cor)
    t.begin_fill()
    lados = random.randint(3, 8)
    for _ in range(lados):
        t.forward(tamanho)
        t.right(360 / lados)
    t.end_fill()

def desenhar_circulo(t, cor, tamanho):
    t.color(cor)
    t.begin_fill()
    t.circle(tamanho)
    t.end_fill()

def desenhar_estrela(t, cor, tamanho):
    t.color(cor)
    t.begin_fill()
    for _ in range(5):
        t.forward(tamanho)
        t.right(144)
    t.end_fill()

def desenhar_espiral(t, cor):
    t.color(cor)
    t.pensize(2)
    t.begin_fill()
    for i in range(50):
        t.forward(i * 2)
        t.right(45)
    t.end_fill()

def gerar_arte(numero, paleta, simetria=False, simples=False):
    turtle.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    angulo = 360 / numero if simetria else 0

    for i in range(numero):
        t.penup()
        if simetria:
            t.goto(0, 0)
            t.setheading(i * angulo)
            t.forward(200)
        else:
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.setheading(random.randint(0, 360))
        t.pendown()

        cor = random.choice(paleta)
        tamanho = random.randint(20, 100)

        if simples:
            desenhar_circulo(t, cor, tamanho)
        else:
            forma = random.choice(["circulo", "poligono", "estrela", "espiral"])
            if forma == "circulo":
                desenhar_circulo(t, cor, tamanho)
            elif forma == "poligono":
                desenhar_poligono(t, cor, tamanho)
            elif forma == "estrela":
                desenhar_estrela(t, cor, tamanho)
            else:
                desenhar_espiral(t, cor)

    # Guardar imagem como .eps
    canvas = turtle.getcanvas()
    eps_file = "arte_abstrata.eps"
    canvas.postscript(file=eps_file)
    turtle.done()

    # Converter para PNG
    img = Image.open(eps_file)
    png_file = "arte_abstrata.png"
    img.save(png_file, "png")
    os.remove(eps_file)

# === Interface Gráfica ===
root = tk.Tk()
root.withdraw()

print("🖌️ Gerador de Arte Abstrata - Versão Avançada 🖌️")
modo = simpledialog.askstring("Modo", "Queres modo simples ou complexo?").lower()
simples = modo.startswith("s")
quantidade = simpledialog.askinteger("Quantidade", "Quantas formas queres desenhar?")
simetria = simpledialog.askstring("Simetria", "Queres modo simétrico? (s/n)").lower().startswith("s")

paleta = escolher_paleta()
gerar_arte(quantidade, paleta, simetria, simples)
