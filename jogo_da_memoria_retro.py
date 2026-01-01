from tkinter import font
import pygame

# Inicialização do Pygame
pygame.init()
screen = pygame.display.set_mode((1200, 800)) 
clock = pygame.time.Clock()
running = True

# VARIÁVEIS DE CORES
preto = (0, 0, 0)
amarelo = (255, 255, 0)

# Nome do jogo
pygame.display.set_caption("Jogo da Memória Retrô")

# Tela de fundo inicial
imagem_inicial = pygame.image.load("Imagens/Fundo/Tela inicial.png").convert()
imagem_fundo = pygame.transform.scale(imagem_inicial, (1200, 800))
color = imagem_inicial.get_at((0, 0))
imagem_inicial.set_colorkey(color)

# TELA DE FUNDO DE CARDS
imagem_cards = pygame.image.load("Imagens/Fundo/Tela dOS cards.png").convert()
imagem_fundo_cards = pygame.transform.scale(imagem_cards, (1200, 800))
color = imagem_cards.get_at((0, 0))
imagem_cards.set_colorkey(color)

# FONTE E TEXTOS
fonte = pygame.font.Font("Imagens/TTF/ModernDOS8x16.ttf", 110)
texto_titulo = fonte.render("Jogo da Memória\n     Retrô", True, (amarelo))

fonte = pygame.font.Font("Imagens/TTF/ModernDOS8x16.ttf", 40)
texto_pressionar = fonte.render("Pressione Space para Iniciar", True, (amarelo))

# DEFINIÇÃO DE ESTADOS
desenho = 1

# EVENTOS
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        desenho = desenho + 1
        
  # Apaga o quadro atual preenchendo a tela com a cor preta
  screen.fill(preto)

  # Lógica de jogo e renderização do novo quadro

  # Desenhar na tela

    # Tela inicial
  screen.blit(imagem_fundo, (0, 0))
  screen.blit(texto_titulo, (200, 300))
  screen.blit(texto_pressionar, (350, 750))

    # Tela dos cards
  if desenho != 1:
    screen.blit(imagem_fundo_cards, (0, 0))
  pygame.display.flip()

  clock.tick(60) 

pygame.quit()
