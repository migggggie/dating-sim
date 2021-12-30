import pygame
from home import *
from tutorial import *
from credits import *

pygame.init()
clock=pygame.time.Clock()

colours_Dict = { 'narrator': (202, 160, 245), 'sad': (23, 42, 102), 'confused': (235, 148, 122), 'normal': (77, 197, 155), 'white': (255, 255, 255), 'black': (0, 0, 0)}

#screen size 16:9
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption('Finding Gerald Love')
# Run until the user asks to quit
running = True
show = 'talking'
choice = 0
click = 0
DATE = '' #who did they choose for a date
#first date true or false variables
# False = run first dates
isaacD1 = False
samanthaD1 = False
riD1 = False
fionaD1 = False
blakeD1 = False
skyD1 = False

# # SKIP FIRST DATES IF BELOW CODE IS RUN
# isaacD1 = True
# samanthaD1 = True
# riD1 = True
# fionaD1 = True
# blakeD1 = True
# skyD1 = True
#whether or not the user has confirmed that want to move to second date
proceed2 = False
#over?
END = False
#does the user want a tutorial?
needTutorial = True
#is it the first run?
firstRun = True

while running:
  #first time tutorial - yes or no
  if firstRun == True: #only show on first loop run
    needTut(screen, needTutorial, show)
    if needTut(screen, needTutorial, show) == True:
      tutorial_full (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
    #for first time run - show intro (account creation)
    accountCreation(screen, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    firstRun = False #
  #display the profiles and wait for click
  displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE)
  #isaac dates
  if displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'isaac':
    if isaacD1 == False: #first date not done yet
    #run first date
      isaacDate_1(screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      isaacD1 = True #first date done = true
    elif isaacD1 == True: #onto second date
      secondDate(screen, proceed2, show) #are u sure you want to commit? if yes then second date runs otherwise nothing happens
      if secondDate(screen, proceed2, show) == True:
        isaacDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  #ri dates
  elif displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'ri':
    if riD1 == False: #first date not done yet
    #run first date
      riDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      riD1 = True #first date done = true
    elif riD1 == True: #onto second date
      if secondDate(screen, proceed2, show) == True:#are u sure you want to commit? if yes then second date runs otherwise nothing happens
        riDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  #samantha dates
  elif displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'samantha':
    if samanthaD1 == False: #first date not done yet
    #run first date
      samanthaDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      samanthaD1 = True #first date done = true
    elif samanthaD1 == True: #onto second date
      if secondDate(screen, proceed2, show) == True:#are u sure you want to commit? if yes then second date runs otherwise nothing happens
        samanthaDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  #fiona dates
  elif displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'fiona':
    if fionaD1 == False: #first date not done yet
    #run first date
      fionaDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      fionaD1 = True #first date done = true
    elif fionaD1 == True: #onto second date
      if secondDate(screen, proceed2, show) == True:#are u sure you want to commit? if yes then second date runs otherwise nothing happens
        fionaDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  #blake dates
  elif displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'blake':
    if blakeD1 == False: #first date not done yet
    #run first date
      blakeDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      blakeD1 = True #first date done = true
    elif blakeD1 == True: #onto second date
      if secondDate(screen, proceed2, show) == True:#are u sure you want to commit? if yes then second date runs otherwise nothing happens
        blakeDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  #sky datesr
  elif displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE) == 'sky':
    if skyD1 == False: #first date not done yet
    #run first date
      skyDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
      skyD1 = True #first date done = true
    elif skyD1 == True: #onto second date
      if secondDate(screen, proceed2, show) == True:#are u sure you want to commit? if yes then second date runs otherwise nothing happens
        skyDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice)
  # if END == True:
    # credits(screen)


  # Did the user click the window close button?
  for event in pygame.event.get():
    print (event)
    if event.type == pygame.QUIT:
      running = False
  
  # Flip the display
  pygame.display.flip()
  clock.tick(30)
# Done! Time to quit.
pygame.quit()