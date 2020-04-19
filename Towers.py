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
    pygame.draw.rect(screen, constant.RING_COLOR, ((self.x, self.y), (self.length, self.height)))

  def clickInRing(self, click_pos):
    if (click_pos[0] > self.x and (click_pos[0] < (self.x + self.length))) and \
      (click_pos[1] > self.y and (click_pos[1] < (self.y + constant.RING_HEIGHT))):
      return True
    else:
      return False

  # Operator Overloading
  def __eq__(self, other):  # equivalence operator 
    if (self.number == other.number):
      return True
    else:
      return False
  
  def __gt__(self, other):  # greater than operator 
    if(self.number > other.number):
      return True
    else:
      return False
  
  def __lt__(self, other):  # less than operator 
    if(self.number < other.number):
      return True
    else:
      return False


  def setPos(self, pos):
    # assumes that pos is the coordinates of the center of the ring
    self.x = pos[0] - (self.length / 2)
    self.y = pos[1] - (constant.RING_HEIGHT / 2)
  
  def getPos(self):
    return (self.x, self.y)
  
  def getPosCenter(self):
    # returns the position of the center of the ring
    return (self.x + (self.length / 2), self.y + (constant.RING_HEIGHT / 2))

class Pole:
  def __init__(self, x_pos, y_pos, rings):
    self.x = x_pos
    self.y = y_pos
    self.rings = rings
    
  def draw(self):
    pygame.draw.rect(screen, (0,0,0), ((self.x, self.y), (constant.POLE_WIDTH, constant.POLE_HEIGHT)))
    count = 0
    for ring in self.rings:
        ring.setPos((self.x + (constant.POLE_WIDTH / 2), (self.y + constant.POLE_HEIGHT) - (count * constant.RING_HEIGHT)))
        ring.draw()
        count += 1

  def getDistanceSqFromRing(self, ring):
    ringPos = ring.getPosCenter()
    return ((((self.x + (constant.POLE_WIDTH / 2)) - ringPos[0]) ** 2) + (((self.y + constant.POLE_HEIGHT) - ringPos[1]) ** 2))
    

  def removeRing(self, ring):
    if len(self.rings) > 0:
      if ring == self.rings[-1]:
        self.rings.pop()
        return True
    else:
      return False

  def addRing(self, ring):
    if len(self.rings) > 0:
      if ring < self.rings[-1]:
        self.rings.append(ring)
        return True
    else:
      self.rings.append(ring)
      return True
    return False
  
  def getRings(self):
    return self.rings


def drawBackground():
  screen.fill((245,245,245))



def main():
  done = False
  ring0 = Ring(0,'black')
  ring1 = Ring(1, 'black')
  ring2 = Ring(2, 'black')
  ring5 = Ring(5, 'black')
  rings = [ring5, ring2, ring1, ring0]
  pole1 = Pole(constant.POLE1_X_POS, constant.POLE1_Y_POS, rings)
  pole2 = Pole(constant.POLE2_X_POS, constant.POLE2_Y_POS, [])
  pole3 = Pole(constant.POLE3_X_POS, constant.POLE3_Y_POS, [])
  poles = [pole1, pole2, pole3]
  pressedRing = None
  pressedRingOldPole = None
  while not done:
      for event in pygame.event.get():
              if event.type == pygame.QUIT:
                      done = True


      drawBackground()

      if pygame.mouse.get_pressed() == (1,0,0):               # if clicked
        if pressedRing:
          pressedRing.setPos(pygame.mouse.get_pos())             # set pos of that ring to click
          pressedRing.draw()
        else:
          for pole in poles:                    # iterate through poles
            ringsInPole = pole.getRings()
            if len(ringsInPole) > 0:            # if there are rings on the pole
              smallestRing = ringsInPole[-1]      # get the smallest (last) ring on the pole
              if(smallestRing.clickInRing(pygame.mouse.get_pos())):     # if the click is inside that ring
                  pole.removeRing(smallestRing)           # remove the ring from that pole
                  pressedRing = smallestRing              # pressedRing is now that ring
                  pressedRingOldPole = pole               # keep track of the last pole the ring is on
        pygame.display.set_caption(str(pygame.mouse.get_pos())) # set caption of frame to pos of mouse click

      else:
        if pressedRing:                             # if the player is holding a ring
          minDist = poles[0].getDistanceSqFromRing(pressedRing)   # init minDist
          newPoleHome = poles[0]                      # init newPoleHome - where the ring might be next
          for pole in poles:
            dist = pole.getDistanceSqFromRing(pressedRing)      # find the distance from each pole to the ring
            if dist < minDist:
              newPoleHome = pole                      # set newPoleHome to pole with current least distance from pressedRing
              minDist = dist                            # set minDist to new found minDist
          if not newPoleHome.addRing(pressedRing):      # if not able to add pressedRing to newPoleHome
            pressedRingOldPole.addRing(pressedRing)     # put ring back on old Pole
          pressedRing = None
          pressedRingOldPole = None

      
      for pole in poles:
        pole.draw()
      pygame.display.update()

if __name__ == "__main__":
  print("We here")
  main()
