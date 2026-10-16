import pygame
import sys

class PongGame:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong - Teste Inicial")
        self.clock = pygame.time.Clock()

        # Dimensões e posições
        self.paddle_width, self.paddle_height = 15, 100
        self.player1_y = self.height // 2 - self.paddle_height // 2
        self.player2_y = self.height // 2 - self.paddle_height // 2
        self.paddle_speed = 7

        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_dx = 5
        self.ball_dy = 5
        self.ball_size = 15

    def run(self):
        running = True
        while running:
            # Tratamento de Eventos (Teclado)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Controles via Teclado para teste local
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] and self.player1_y > 0:
                self.player1_y -= self.paddle_speed
            if keys[pygame.K_s] and self.player1_y < self.height - self.paddle_height:
                self.player1_y += self.paddle_speed

            if keys[pygame.K_UP] and self.player2_y > 0:
                self.player2_y -= self.paddle_speed
            if keys[pygame.K_DOWN] and self.player2_y < self.height - self.paddle_height:
                self.player2_y += self.paddle_speed

            # Física da Bola
            self.ball_x += self.ball_dx
            self.ball_y += self.ball_dy

            # Colisão com teto e chão
            if self.ball_y <= 0 or self.ball_y >= self.height - self.ball_size:
                self.ball_dy *= -1

            # Colisão com as raquetes
            # Raquete 1
            if 50 <= self.ball_x <= 65 and self.player1_y <= self.ball_y <= self.player1_y + self.paddle_height:
                self.ball_dx *= -1
            # Raquete 2
            if self.width - 65 <= self.ball_x <= self.width - 50 and self.player2_y <= self.ball_y <= self.player2_y + self.paddle_height:
                self.ball_dx *= -1

            # Reinicia se passar da tela
            if self.ball_x < 0 or self.ball_x > self.width:
                self.ball_x, self.ball_y = self.width // 2, self.height // 2
                self.ball_dx *= -1

            # Renderização
            self.screen.fill((0, 0, 0)) # Fundo preto
            
            # Desenha elementos
            pygame.draw.rect(self.screen, (255, 255, 255), (50, self.player1_y, self.paddle_width, self.paddle_height))
            pygame.draw.rect(self.screen, (255, 255, 255), (self.width - 65, self.player2_y, self.paddle_width, self.paddle_height))
            pygame.draw.ellipse(self.screen, (255, 255, 255), (self.ball_x, self.ball_y, self.ball_size, self.ball_size))

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()