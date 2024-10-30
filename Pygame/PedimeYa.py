import pygame
import random
import time

pygame.init()
ANCHO_VENTANA = 900
ALTO_VENTANA = 630
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_BORDO = (128, 0, 32)
COLOR_GRIS = (128, 128, 128)
COLOR_AMARILLO = (255, 255, 0)
COLOR_CELESTE = ( 0, 0,128)
COLOR_AZUL = ( 0, 0, 255)
COLOR_MARRON = (139, 69, 19)
COLOR_PAN = (180, 140, 100) #PAN DE HAMBURGUESA
COLOR_PAPAS = (255, 223, 128) #PAPAS FRITAS
COLOR_NEGRO = (0,0,0,)
COLOR_PLATEADO = (192, 192, 192)
COLOR_PASTO = (34, 139, 34)

juego_en_progreso = False
tiempo_juego = 5.02 * 60
tiempo_inicio = time.time()

pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))

pygame.display.set_caption("Juego")
flag_correr = True

contador_pedidos = 0
contador_plata = 0

objetos_disponibles = ["pan", "morrón", "tomate", "lechuga", "papas", "mora"]

precios = {
    "pan": 1.0,
    "morrón": 2.5,
    "tomate": 0.5,
    "lechuga": 0.5,
    "papas": 1.5,
    "mora": 1.0
}

fuente = pygame.font.Font(None, 36)
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos,1000)
clock = pygame.time.Clock()

def generar_pedido():
    cantidad_pedido = random.randint(1, 6) 
    pedido = random.sample(objetos_disponibles, min(cantidad_pedido, len(objetos_disponibles)))
    return pedido

posicion_pan = [50, 550]
posicion_morron = [150, 550]
posicion_tomate = [250, 550]
posicion_lechuga = [350, 550]
posicion_mora = [450, 550]
posicion_papas = [550, 550]
posicion_bandeja_comida = [660, 480]
posicion_mesada = (0, 400, 900, 300)


pedido_actual = generar_pedido()

def mostrar_menu():
    pantalla.fill(COLOR_NEGRO)

    titulo = fuente.render("¡Bienvenido a Pedime Ya!", True, COLOR_BLANCO)
    pantalla.blit(titulo, (ANCHO_VENTANA // 2 - titulo.get_width() // 2, 50))

    instrucciones = [
        ("A - Pan", COLOR_PAN, 120),
        ("S - Morrón", COLOR_BORDO, 210),
        ("D - Tomate", COLOR_ROJO, 300),
        ("J - Lechuga", COLOR_VERDE, 390),
        ("K - Mora", COLOR_CELESTE, 480),
        ("L - Papas", COLOR_PAPAS, 570)
    ]

    x_circulo = ANCHO_VENTANA // 2 - 100  
    x_texto = ANCHO_VENTANA // 2 - 50

    for texto, color, y_pos in instrucciones:
        
        pygame.draw.circle(pantalla, color, (x_circulo, y_pos), 40)
        
        texto_renderizado = fuente.render(texto, True, COLOR_BLANCO)
        pantalla.blit(texto_renderizado, (x_texto, y_pos - 20))

    texto_comenzar = fuente.render("Presiona ESPACIO", True, COLOR_BLANCO)
    pantalla.blit(texto_comenzar, (660, 480,230,50))

    pygame.display.flip()

while flag_correr:
    if not juego_en_progreso:
        mostrar_menu()

    tiempo_transcurrido = time.time() - tiempo_inicio
    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag_correr = False
        
        if evento.type == pygame.KEYDOWN:
            if not juego_en_progreso and evento.key == pygame.K_SPACE:
                juego_en_progreso = True
                tiempo_inicio = time.time()
                contador_pedidos = 0
                contador_plata = 0
                pedido_actual = generar_pedido()
                

            if juego_en_progreso:
                
                if evento.key == pygame.K_a:
                    posicion_pan = posicion_bandeja_comida.copy()
                if evento.key == pygame.K_s:
                    posicion_morron = [posicion_bandeja_comida[0] + 60, posicion_bandeja_comida[1]]
                if evento.key == pygame.K_d:
                    posicion_tomate = [posicion_bandeja_comida[0] + 120, posicion_bandeja_comida[1]]
                if evento.key == pygame.K_j:
                    posicion_lechuga = [posicion_bandeja_comida[0] + 180, posicion_bandeja_comida[1]]
                if evento.key == pygame.K_k:
                    posicion_mora = [posicion_bandeja_comida[0] + 190, posicion_bandeja_comida[1] + 40]
                if evento.key == pygame.K_l:
                    posicion_papas = [posicion_bandeja_comida[0] + 100, posicion_bandeja_comida[1] + 50]

            if evento.key == pygame.K_r: 
                posicion_pan = [50, 550]
                posicion_morron = [150, 550]
                posicion_tomate = [250, 550]
                posicion_lechuga = [350, 550]
                posicion_mora = [450, 550]  
                posicion_papas = [550, 550] 

            if evento.key == pygame.K_RETURN:
                pedido_completo = True
                objetos_colocados = []
                if posicion_pan == posicion_bandeja_comida:
                    objetos_colocados.append("pan")
                if posicion_morron == [posicion_bandeja_comida[0] + 60, posicion_bandeja_comida[1]]:
                    objetos_colocados.append("morrón")
                if posicion_tomate == [posicion_bandeja_comida[0] + 120, posicion_bandeja_comida[1]]:
                    objetos_colocados.append("tomate")
                if posicion_lechuga == [posicion_bandeja_comida[0] + 180, posicion_bandeja_comida[1]]:
                    objetos_colocados.append("lechuga")
                if posicion_mora == [posicion_bandeja_comida[0] + 190, posicion_bandeja_comida[1] + 40]:
                    objetos_colocados.append("mora")
                if posicion_papas == [posicion_bandeja_comida[0] + 100, posicion_bandeja_comida[1] + 50]:
                    objetos_colocados.append("papas")

                pedido_completo = all(item in objetos_colocados for item in pedido_actual)

                if pedido_completo:
                    contador_pedidos += 1
                    for objeto in pedido_actual:
                        contador_plata += precios[objeto]
                    pedido_actual = generar_pedido()
                
                posicion_pan = [50, 550]
                posicion_morron = [150, 550]
                posicion_tomate = [250, 550]
                posicion_lechuga = [350, 550]
                posicion_mora = [450, 550]  
                posicion_papas = [550, 550]

        if juego_en_progreso:
            pantalla.fill(COLOR_CELESTE)

        pygame.draw.rect(pantalla, COLOR_PASTO, (0, 200, 900, 230))
        pygame.draw.circle(pantalla, COLOR_AMARILLO, (880, 50), 80)
        pygame.draw.rect(pantalla, COLOR_MARRON,posicion_mesada)

        
        pygame.draw.rect(pantalla, COLOR_PLATEADO, pygame.Rect(630, 440, 260, 150))
        pygame.draw.circle(pantalla, COLOR_PAN, posicion_pan, 40)
        pygame.draw.circle(pantalla, COLOR_BORDO, posicion_morron, 40)
        pygame.draw.circle(pantalla, COLOR_ROJO, posicion_tomate, 40)
        pygame.draw.circle(pantalla, COLOR_VERDE, posicion_lechuga, 40)
        pygame.draw.circle(pantalla, COLOR_CELESTE, posicion_mora, 40)
        pygame.draw.circle(pantalla, COLOR_PAPAS, posicion_papas, 40)

        texto_pedido = fuente.render("Pedido: " + ", ".join(pedido_actual), True, COLOR_BLANCO)
        pantalla.blit(texto_pedido, (20, 20))

        texto_pedidos = fuente.render(f"Pedidos completados: {contador_pedidos}", True, COLOR_BLANCO)
        pantalla.blit(texto_pedidos, (20, 60))

        texto_dinero = fuente.render(f"Dinero ganado: ${contador_plata:.2f}", True, COLOR_BLANCO)
        pantalla.blit(texto_dinero, (20, 100))
        
        tiempo_restante = max(0, tiempo_juego - tiempo_transcurrido)
        minutos = int(tiempo_restante // 60)
        segundos = int(tiempo_restante % 60)
        texto_tiempo = f"Tiempo restante: {minutos:02}:{segundos:02}"
        texto_renderizado_tiempo = fuente.render(texto_tiempo, True, COLOR_BLANCO)
        pantalla.blit(texto_renderizado_tiempo, (20, 140))


    if tiempo_transcurrido >= tiempo_juego:
        juego_en_progreso = False

    pygame.display.flip()

clock.tick(30) 

pygame.quit()

