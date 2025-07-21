import turtle
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image
import os
import time
import webbrowser

# === Funções ===

paleta_atual = []
simples = False
simetria = False
quantidade = 10
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")


def escolher_paleta():
    opcoes = {
        "1": ["red", "orange", "yellow", "green", "blue", "purple", "white"],
        "2": ["#f72585", "#7209b7", "#3a0ca3", "#4361ee", "#4cc9f0"],
        "3": ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
    }
    return opcoes["1"]  # Valor inicial

def desenhar_forma(forma, cor, tamanho):
    t.color(cor)
    t.begin_fill()

    if forma == "circulo":
        t.circle(tamanho)
    elif forma == "poligono":
        lados = random.randint(3, 8)
        for _ in range(lados):
            t.forward(tamanho)
            t.right(360 / lados)
    elif forma == "estrela":
        for _ in range(5):
            t.forward(tamanho)
            t.right(144)
    elif forma == "espiral":
        t.pensize(2)
        for i in range(50):
            t.forward(i * 2)
            t.right(45)

    t.end_fill()

def gerar_arte():
    t.clear()
    angulo = 360 / quantidade if simetria else 0

    for i in range(quantidade):
        t.penup()
        if simetria:
            t.goto(0, 0)
            t.setheading(i * angulo)
            t.forward(200)
        else:
            t.goto(random.randint(-300, 300), random.randint(-300, 300))
            t.setheading(random.randint(0, 360))
        t.pendown()

        cor = random.choice(paleta_atual)
        tamanho = random.randint(20, 100)
        forma = "circulo" if simples else random.choice(["circulo", "poligono", "estrela", "espiral"])

        desenhar_forma(forma, cor, tamanho)

def guardar_imagem():
    canvas = turtle.getcanvas()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pasta = "galeria"
    os.makedirs(pasta, exist_ok=True)
    eps_file = os.path.join(pasta, f"arte_{timestamp}.eps")
    png_file = os.path.join(pasta, f"arte_{timestamp}.png")
    canvas.postscript(file=eps_file)

    try:
        img = Image.open(eps_file)
        img.load(scale=10)
        img.save(png_file, "PNG")
        os.remove(eps_file)
        messagebox.showinfo("Concluído", f"Imagem guardada como {png_file}")
        webbrowser.open(png_file)
    except Exception as e:
        print("Erro ao converter EPS para PNG:", e)
        messagebox.showwarning("Erro", f"Só foi possível guardar como EPS: {eps_file}")

def definir_parametros():
    global simples, simetria, quantidade, paleta_atual

    modo = simpledialog.askstring("Modo", "Queres modo simples ou complexo?")
    simples = modo and modo.lower().startswith("s")

    quantidade = simpledialog.askinteger("Quantidade", "Quantas formas queres desenhar?") or 10

    simetria_input = simpledialog.askstring("Simetria", "Queres modo simétrico? (s/n)")
    simetria = simetria_input and simetria_input.lower().startswith("s")

    paleta = simpledialog.askstring("Paleta", "Escolhe a paleta:\n1 - Clássica\n2 - Neon\n3 - Cores quentes")
    paletas = {
        "1": ["red", "orange", "yellow", "green", "blue", "purple", "white"],
        "2": ["#f72585", "#7209b7", "#3a0ca3", "#4361ee", "#4cc9f0"],
        "3": ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
    }
    paleta_atual = paletas.get(paleta, paletas["1"])

    gerar_arte()

def mover_cima(event):
    t.setheading(90)
    t.forward(20)

def mover_baixo(event):
    t.setheading(270)
    t.forward(20)

def mover_esquerda(event):
    t.setheading(180)
    t.forward(20)

def mover_direita(event):
    t.setheading(0)
    t.forward(20)

def clique_rato(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    cor = random.choice(paleta_atual)
    tamanho = random.randint(20, 60)
    forma = random.choice(["circulo", "poligono", "estrela"])
    desenhar_forma(forma, cor, tamanho)

# === GUI ===
root = tk.Tk()
root.title("🎨 Gerador de Arte Abstrata")
root.geometry("300x250")

btn_definir = tk.Button(root, text="Definir Parâmetros", command=definir_parametros)
btn_gerar = tk.Button(root, text="Gerar Arte", command=gerar_arte)
btn_guardar = tk.Button(root, text="Guardar Imagem", command=guardar_imagem)
btn_sair = tk.Button(root, text="Sair", command=lambda: (turtle.bye(), root.destroy()))

btn_definir.pack(pady=10)
btn_gerar.pack(pady=10)
btn_guardar.pack(pady=10)
btn_sair.pack(pady=10)

# === Controlo com Teclado ===
screen = turtle.Screen()
screen.listen()
screen.onkey(mover_cima, "Up")
screen.onkey(mover_baixo, "Down")
screen.onkey(mover_esquerda, "Left")
screen.onkey(mover_direita, "Right")

# === Controlo com Rato ===
screen.onclick(clique_rato)

paleta_atual = escolher_paleta()
root.mainloop()
