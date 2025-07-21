import turtle
import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image
import os
import time
import webbrowser

# === Funções ===

def escolher_paleta():
    opcoes = {
        "1": ["red", "orange", "yellow", "green", "blue", "purple", "white"],
        "2": ["#f72585", "#7209b7", "#3a0ca3", "#4361ee", "#4cc9f0"],
        "3": ["#ffbe0b", "#fb5607", "#ff006e", "#8338ec", "#3a86ff"]
    }
    escolha = simpledialog.askstring("Paleta", "Escolhe a paleta:\n1 - Clássica\n2 - Neon\n3 - Cores quentes")
    return opcoes.get(escolha, opcoes["1"])

def desenhar_forma(t, forma, cor, tamanho):
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
        forma = "circulo" if simples else random.choice(["circulo", "poligono", "estrela", "espiral"])

        desenhar_forma(t, forma, cor, tamanho)

    # Guardar imagem como .eps
    canvas = turtle.getcanvas()
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    pasta = "galeria"
    os.makedirs(pasta, exist_ok=True)
    eps_file = os.path.join(pasta, f"arte_{timestamp}.eps")
    png_file = os.path.join(pasta, f"arte_{timestamp}.png")
    canvas.postscript(file=eps_file)

    # Tentar converter para PNG (se Ghostscript estiver instalado)
    try:
        img = Image.open(eps_file)
        img.load(scale=10)
        img.save(png_file, "PNG")
        os.remove(eps_file)
        print(f"Imagem guardada como {png_file}")
        messagebox.showinfo("Concluído", f"Imagem guardada como {png_file}")
        webbrowser.open(png_file)
    except Exception as e:
        print("A conversão para PNG falhou. Talvez precises de instalar o Ghostscript.")
        print("Erro:", e)
        print(f"A imagem EPS foi guardada como {eps_file}")
        messagebox.showwarning("Erro", f"Apenas foi possível guardar como EPS. Ficheiro: {eps_file}")

    # Fechar a janela turtle após 5 segundos
    turtle.ontimer(turtle.bye, 5000)

# === Interface Gráfica ===
root = tk.Tk()
root.withdraw()

print("🖌️ Gerador de Arte Abstrata - Versão Avançada 🖌️")
modo = simpledialog.askstring("Modo", "Queres modo simples ou complexo?")
if not modo:
    modo = "simples"
simples = modo.lower().startswith("s")

quantidade = simpledialog.askinteger("Quantidade", "Quantas formas queres desenhar?")
if not quantidade or quantidade <= 0:
    quantidade = 10

simetria_input = simpledialog.askstring("Simetria", "Queres modo simétrico? (s/n)")
simetria = simetria_input and simetria_input.lower().startswith("s")

paleta = escolher_paleta()
gerar_arte(quantidade, paleta, simetria, simples)
