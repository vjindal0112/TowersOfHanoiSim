import pygame
import constant

pygame.init()
screen = pygame.display.set_mode((400, 300))
screen.fill((245,245,245))

class Ring:
  def __init__(self, number, color):
    self.number = number
    self.color = color
    self.length = constant.STARTER_RING_WIDTH + self.number * 18
    self.height = constant.RING_HEIGHT
    self.x = constant.POLE1_X_POS - (self.length / 2) + (constant.POLE_WIDTH / 2)
    self.y = constant.POLE1_Y_POS + (self.number * constant.RING_HEIGHT)

  def draw(self):
    pygame.draw.rect(screen, (255, 0, 0), ((self.x, self.y), (self.length, self.height)))

  def setPos(self, pos):
    # assumes that pos is the coordinates of the center of the ring
    self.x = pos[0] - (self.length / 2)
    self.y = pos[1] - (constant.RING_HEIGHT / 2)
  


class Pole:
  def __init__(self, x_pos, y_pos):
    self.x = x_pos
    self.y = y_pos
    
  def draw(self):
    pygame.draw.rect(screen, (0,0,0), ((self.x, self.y), (constant.POLE_WIDTH, constant.POLE_HEIGHT)))


def drawBackground():
  screen.fill((245,245,245))



def main():
  done = False
  ring0 = Ring(0,'black')
  ring1 = Ring(1, 'black')
  ring2 = Ring(2, 'black')
  ring5 = Ring(5, 'black')
  pole1 = Pole(constant.POLE1_X_POS, constant.POLE1_Y_POS)
  pole2 = Pole(constant.POLE2_X_POS, constant.POLE2_Y_POS)
  pole3 = Pole(constant.POLE3_X_POS, constant.POLE3_Y_POS)
  while not done:
          for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                          done = True
          drawBackground()
          if pygame.mouse.get_pressed() == (1,0,0):
            pygame.display.set_caption(str(pygame.mouse.get_pos()))
            ring0.setPos(pygame.mouse.get_pos())
          pole1.draw()
          pole2.draw()
          pole3.draw()


          ring0.draw()
          ring1.draw()
          ring2.draw()
          ring5.draw()
          pygame.display.update()

if __name__ == "__main__":
  print("We here")
  main()
