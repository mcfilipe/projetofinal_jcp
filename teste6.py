import py5
import random
import tkinter as tk
from tkinter import simpledialog

# Variáveis globais para parâmetros definidos pelo utilizador
quantidade = 50
modo_simples = True
modo_simetrico = False
paleta = [
    (255, 0, 0),    # vermelho
    (255, 165, 0),  # laranja
    (255, 255, 0),  # amarelo
    (0, 128, 0),    # verde
    (0, 0, 255),    # azul
    (128, 0, 128),  # roxo
    (255, 255, 255) # branco
]

def escolher_parametros():
    global quantidade, modo_simples, modo_simetrico
    root = tk.Tk()
    root.withdraw()
    modo = simpledialog.askstring("Modo", "Queres modo simples ou complexo? (s/c)").lower()
    modo_simples = modo.startswith("s")
    quantidade = simpledialog.askinteger("Quantidade", "Quantas formas queres desenhar?")
    simetria = simpledialog.askstring("Simetria", "Queres modo simétrico? (s/n)").lower()
    modo_simetrico = simetria.startswith("s")
    root.destroy()

def setup():
    py5.size(600, 600)
    py5.background(0)
    py5.no_loop()  # só desenha uma vez
    escolher_parametros()

def draw():
    py5.background(0)
    if modo_simetrico:
        angulo = 360 / quantidade
        raio = 200
        py5.push_matrix()
        py5.translate(py5.width / 2, py5.height / 2)
        for i in range(quantidade):
            py5.push_matrix()
            py5.rotate(py5.radians(i * angulo))
            py5.translate(raio, 0)
            desenhar_forma()
            py5.pop_matrix()
        py5.pop_matrix()
    else:
        for _ in range(quantidade):
            py5.push_matrix()
            x = random.randint(0, py5.width)
            y = random.randint(0, py5.height)
            py5.translate(x, y)
            py5.rotate(random.uniform(0, py5.TWO_PI))
            desenhar_forma()
            py5.pop_matrix()
    # Guarda imagem
    py5.save_frame("arte_abstrata_py5.png")
    print("Imagem guardada como arte_abstrata_py5.png")

def desenhar_forma():
    cor = random.choice(paleta)
    py5.fill(*cor, 180)
    py5.no_stroke()
    tamanho = random.randint(20, 100)
    if modo_simples:
        py5.ellipse(0, 0, tamanho, tamanho)
    else:
        forma = random.choice(['circulo', 'poligono', 'estrela', 'espiral'])
        if forma == 'circulo':
            py5.ellipse(0, 0, tamanho, tamanho)
        elif forma == 'poligono':
            lados = random.randint(3, 8)
            py5.begin_shape()
            for i in range(lados):
                angle = py5.TWO_PI / lados * i
                x = py5.cos(angle) * tamanho / 2
                y = py5.sin(angle) * tamanho / 2
                py5.vertex(x, y)
            py5.end_shape(py5.CLOSE)
        elif forma == 'estrela':
            py5.begin_shape()
            pontos = 5
            for i in range(pontos * 2):
                r = tamanho / 2 if i % 2 == 0 else tamanho / 4
                angle = py5.TWO_PI / (pontos * 2) * i
                x = py5.cos(angle) * r
                y = py5.sin(angle) * r
                py5.vertex(x, y)
            py5.end_shape(py5.CLOSE)
        else:  # espiral simples
            py5.no_fill()
            py5.stroke(*cor)
            py5.stroke_weight(2)
            for i in range(50):
                py5.line(i * 2, 0, i * 2 + 5, 5)
                py5.rotate(py5.radians(45))

py5.run_sketch()
