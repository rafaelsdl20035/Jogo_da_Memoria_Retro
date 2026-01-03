import random
import pygame

# INICIALIZAÇÃO DO PYGAME
pygame.init()
screen = pygame.display.set_mode((1200, 800)) 
clock = pygame.time.Clock()
running = True

# VARIÁVEIS DE CORES
preto = (0, 0, 0)
amarelo = (255, 255, 0)

# TÍTULO DA JANELA
pygame.display.set_caption("Jogo da Memória Retrô")

# TELA INICIAL
imagem_inicial = pygame.image.load("Imagens/Fundo/Tela inicial.png").convert()
imagem_fundo = pygame.transform.scale(imagem_inicial, (1200, 800))
color = imagem_inicial.get_at((0, 0))
imagem_inicial.set_colorkey(color)

# TELA DE FUNDO DE CARDS
imagem_cards = pygame.image.load("Imagens/Fundo/Tela dos cards.png").convert()
imagem_fundo_cards = pygame.transform.scale(imagem_cards, (1200, 800))
color = imagem_cards.get_at((0, 0))
imagem_cards.set_colorkey(color)

# CARREGAMENTO DAS IMAGENS
# CARDS 
card_0 = pygame.image.load("Imagens/Cards/card para baixo.png").convert_alpha()
card_1 = pygame.image.load("Imagens/Cards/cards (1).png").convert_alpha()
card_2 = pygame.image.load("Imagens/Cards/cards (2).png").convert_alpha()
card_3 = pygame.image.load("Imagens/Cards/cards (3).png").convert_alpha()
card_4 = pygame.image.load("Imagens/Cards/cards (4).png").convert_alpha()
card_5 = pygame.image.load("Imagens/Cards/cards (5).png").convert_alpha()
card_6 = pygame.image.load("Imagens/Cards/cards (6).png").convert_alpha()
card_7 = pygame.image.load("Imagens/Cards/cards (7).png").convert_alpha()
card_8 = pygame.image.load("Imagens/Cards/cards (8).png").convert_alpha()
card_9 = pygame.image.load("Imagens/Cards/cards (9).png").convert_alpha()
card_10 = pygame.image.load("Imagens/Cards/cards (10).png").convert_alpha()
card_11 = pygame.image.load("Imagens/Cards/cards (11).png").convert_alpha()
card_12 = pygame.image.load("Imagens/Cards/cards (12).png").convert_alpha()

# CARDS REDIMENSIONADOS
def scale_card(imagens_redimensionadas):
    return pygame.transform.scale(imagens_redimensionadas, (100, 100))

card_para_baixo = scale_card(card_0)

cards_base = [
    scale_card(card_1), scale_card(card_2), scale_card(card_3),
    scale_card(card_4), scale_card(card_5), scale_card(card_6),
    scale_card(card_7), scale_card(card_8), scale_card(card_9),
    scale_card(card_10), scale_card(card_11), scale_card(card_12)
]

# CRIAÇÃO DA LISTA FINAL DE CARTAS
cards_para_cima = []
for card in cards_base:
    cards_para_cima.append(card)
    cards_para_cima.append(card)

random.shuffle(cards_para_cima)

# FONTE E TEXTOS
fonte = pygame.font.Font("Imagens/TTF/ModernDOS8x16.ttf", 110)
texto_titulo = fonte.render("Jogo da Memória\n     Retrô", True, amarelo)

fonte = pygame.font.Font("Imagens/TTF/ModernDOS8x16.ttf", 40)
texto_pressionar = fonte.render("Pressione Espaço para Iniciar", True, amarelo)

# CLASSE CARTA
class Carta:
    def __init__(self, frente, posicao):
        self.frente = frente
        self.verso = card_para_baixo
        self.rect = self.frente.get_rect(topleft=posicao)
        self.virada = False
        self.encontrada = False

    def desenhar(self, tela):
        if self.virada or self.encontrada:
            tela.blit(self.frente, self.rect)
        else:
            tela.blit(self.verso, self.rect)

# CRIAÇÃO DAS CARTAS
cartas = []
x_inicial, y_inicial = 240, 170
espaco = 120
indice_cards = 0

for linha in range(4):
    for coluna in range(6):
        posicao = (x_inicial + coluna * espaco, y_inicial + linha * espaco)
        cartas.append(Carta(cards_para_cima[indice_cards], posicao))
        indice_cards += 1

# ESTADOS
estado = "menu"  
selecionadas = [] 
tempo_espera = 0
tempo_memorizacao = 0

# LOOP PRINCIPAL
while running:
    # EVENTOS
    for event in pygame.event.get():
        
        # SAIR DO JOGO
        if event.type == pygame.QUIT:
            running = False

        # COMEÇAR O JOGO
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            estado = "memorizacao"          # INICIA A FASE DE MEMORIZAÇÃO 
            tempo_memorizacao = 0          # ZERA O TEMPO DE MEMORIZAÇÃO

        # SELECIONAR CARTAS
        if event.type == pygame.MOUSEBUTTONDOWN and estado == "jogo":
            for carta in cartas:
                if carta.rect.collidepoint(event.pos): 
                    if not carta.virada and not carta.encontrada and len(selecionadas) < 2:
                        carta.virada = True
                        selecionadas.append(carta)

    #FASE DE MEMORIZAÇÃO
    if estado == "memorizacao":
        tempo_memorizacao += clock.get_time()

        for carta in cartas:
            carta.virada = True

        if tempo_memorizacao > 5000:  # tempo de memorização das cartas (modifique aqui para alterar o tempo)
            for carta in cartas:
                carta.virada = False
            estado = "jogo"

    # LÓGICA DE COMPARAÇÃO
    if len(selecionadas) == 2:
        c1, c2 = selecionadas

        if c1.frente == c2.frente:
            c1.encontrada = True
            c2.encontrada = True
            c1.virada = True
            c2.virada = True
            selecionadas.clear()
            tempo_espera = 0
        else:
            tempo_espera += 1
            if tempo_espera > 30:
                c1.virada = False
                c2.virada = False
                selecionadas.clear()
                tempo_espera = 0

    # DESENHO
    screen.fill(preto)

    # TELA INICIAL
    if estado == "menu":
        screen.blit(imagem_fundo, (0, 0))
        screen.blit(texto_titulo, (200, 300))
        screen.blit(texto_pressionar, (350, 750))

    # FASE DE JOGO E MEMORIZAÇÃO
    if estado == "jogo" or estado == "memorizacao":
        screen.blit(imagem_fundo_cards, (0, 0))
        for carta in cartas:
            carta.desenhar(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
