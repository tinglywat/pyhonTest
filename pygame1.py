import pygame

background_colour = (255,255,255)
(width, height) = (300, 200)

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
fps = 10
clock = pygame.time.Clock()
running = True
print (pygame.time.get_ticks())
while running:
  clock.tick(fps)
  print (pygame.time.get_ticks())

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 4:   
        print(" Scroll UP ")
      if event.button == 5:
        print(" Scroll DOWN ")

pygame.quit ()
