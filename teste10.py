# === py5: versão moderna ===
from py5 import *
import random
import os
from datetime import datetime

# === Parâmetros globais ===
simples = False
simetria = False
quantidade = 10
paleta_atual = []
formas_geradas = []
modo_atual = "complexo"

# === Paletas ===
paletas = {
    "1": [color(255, 0, 0), color(255, 165, 0), color(255, 255, 0), color(0, 128, 0), color(0, 0, 255), color(128, 0, 128), color(255)],
    "2": [color(247, 37, 133), color(114, 9, 183), color(58, 12, 163), color(67, 97, 238), color(76, 201, 240)],
    "3": [color(255, 190, 11), color(251, 86, 7), color(255, 0, 110), color(131, 56, 236), color(58, 134, 255)]
}

# === Funções ===
def definir_parametros():
    global paleta_atual
    paleta_atual = paletas["1"]
    gerar_formas()

def desenhar_forma(fx, fy, angulo, forma, cor, tamanho):
    push_matrix()
    translate(fx, fy)
    rotate(radians(angulo))
    fill(cor)
    no_stroke()

    if forma == "circulo":
        ellipse(0, 0, tamanho, tamanho)
    elif forma == "poligono":
        lados = random.randint(3, 8)
        begin_shape()
        for i in range(lados):
            angle = TWO_PI * i / lados
            x = cos(angle) * tamanho
            y = sin(angle) * tamanho
            vertex(x, y)
        end_shape(CLOSE)
    elif forma == "estrela":
        begin_shape()
        for i in range(10):
            r = tamanho if i % 2 == 0 else tamanho / 2
            angle = TWO_PI * i / 10
            vertex(cos(angle) * r, sin(angle) * r)
        end_shape(CLOSE)
    elif forma == "espiral":
        no_fill()
        stroke(cor)
        stroke_weight(2)
        begin_shape()
        for i in range(50):
            angle = radians(i * 45)
            r = i * 2
            vertex(cos(angle) * r, sin(angle) * r)
        end_shape()
    pop_matrix()

def gerar_formas():
    formas_geradas.clear()
    base_angle = 360 / quantidade if simetria else 0
    for i in range(quantidade):
        angulo = i * base_angle if simetria else random.randint(0, 360)
        fx = width / 2 + (cos(radians(angulo)) * 200 if simetria else random.randint(-300, 300))
        fy = height / 2 + (sin(radians(angulo)) * 200 if simetria else random.randint(-300, 300))
        cor = random.choice(paleta_atual)
        tamanho = random.randint(20, 100)
        forma = "circulo" if simples else random.choice(["circulo", "poligono", "estrela", "espiral"])
        formas_geradas.append((fx, fy, angulo, forma, cor, tamanho))

def draw():
    background(0)
    for fx, fy, angulo, forma, cor, tamanho in formas_geradas:
        desenhar_forma(fx, fy, angulo, forma, cor, tamanho)
    fill(255)
    text_size(14)
    text("[r] Regenerar | [s] Guardar | [1-3] Paleta | [m] Modo | [y] Simetria", 10, height - 20)
    text(f"Modo: {'Simples' if simples else 'Complexo'} | Simetria: {'Sim' if simetria else 'Não'}", 10, height - 40)

def key_pressed():
    global simples, simetria, paleta_atual
    if key == 's':
        guardar_imagem()
    elif key == 'r':
        gerar_formas()
    elif key == '1':
        paleta_atual = paletas["1"]
        gerar_formas()
    elif key == '2':
        paleta_atual = paletas["2"]
        gerar_formas()
    elif key == '3':
        paleta_atual = paletas["3"]
        gerar_formas()
    elif key == 'm':
        simples = not simples
        gerar_formas()
    elif key == 'y':
        simetria = not simetria
        gerar_formas()

def mouse_pressed():
    cor = random.choice(paleta_atual)
    tamanho = random.randint(20, 60)
    forma = random.choice(["circulo", "poligono", "estrela"])
    formas_geradas.append((mouse_x, mouse_y, random.randint(0, 360), forma, cor, tamanho))

def guardar_imagem():
    pasta = "galeria"
    os.makedirs(pasta, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = os.path.join(pasta, f"arte_{timestamp}.png")
    save_frame(path)
    print(f"Imagem guardada em {path}")

def setup():
    size(800, 800)
    title("py5 - Gerador de Arte Abstrata")
    definir_parametros()
