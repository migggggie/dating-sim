import pygame
pygame.init()
clock = pygame.time.Clock()

def credits(screen):
  y = 0
  creds = pygame.image.load('creds.png')
  credsRect = creds.get_rect()
  credsRect = credsRect.move(0, y)
  running = True

  while running: #runs forever wooooo
    y -= 0.03
    if y <= -12:
      y = -12
    credsRect = credsRect.move(0, y)
    screen.blit(creds, credsRect)

    for event in pygame.event.get():
      print (event)
      print(y)
    # Flip the display
    pygame.display.flip()
    clock.tick(15)