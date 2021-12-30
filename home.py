import pygame
pygame.init()
from isaacDates import *
from samanthaDates import *
from blakeDates import *
from riDates import *
from fionaDates import *
from skyDates import *
account = False
#load background image
website = pygame.image.load('website.png')
websiteRect = website.get_rect()

colours_Dict = { 'narrator': (202, 160, 245), 'sad': (23, 42, 102), 'confused': (235, 148, 122), 'normal': (77, 197, 155), 'white': (255, 255, 255), 'black': (0, 0, 0)}

# def display profiles
def displayProfiles (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, DATE):
  clock=pygame.time.Clock()
  #background
  screen.blit(website, websiteRect)
  show = 'choices'
  #instructions
  myfont = pygame.font.SysFont('Comic Sans MS', 100)
  screen.blit(myfont.render('Your Matches', False, colours_Dict['black']), (SCREEN_WIDTH/2 - 230, 60))
  myfont = pygame.font.SysFont('Comic Sans MS', 40)
  screen.blit(myfont.render('Click and drag on a profile to start a first or second date!', False, colours_Dict['black']), (500, 640))
  #isaac profile
  isaac_profile = pygame.image.load('isaac profile.png')
  isaacprofileRect = isaac_profile.get_rect()
  isaacprofileRect = isaacprofileRect.move((25, 150))
  screen.blit(isaac_profile, isaacprofileRect)
  #ri profile
  ri_profile = pygame.image.load('ri profile.png')
  riprofileRect = ri_profile.get_rect()
  riprofileRect = riprofileRect.move((225, 150))
  screen.blit(ri_profile, riprofileRect)
  #samantha profile
  samantha_profile = pygame.image.load('samantha profile.png')
  samanthaprofileRect = samantha_profile.get_rect()
  samanthaprofileRect = samanthaprofileRect.move((445, 150))
  screen.blit(samantha_profile, samanthaprofileRect)
  #fiona profile
  fiona_profile = pygame.image.load('fiona profile.png')
  fionaprofileRect = fiona_profile.get_rect()
  fionaprofileRect = fionaprofileRect.move((645, 150))
  screen.blit(fiona_profile, fionaprofileRect)
  #blake profile
  blake_profile = pygame.image.load('blake profile.png')
  blakeprofileRect = blake_profile.get_rect()
  blakeprofileRect = blakeprofileRect.move((870, 150))
  screen.blit(blake_profile, blakeprofileRect)
  #sky profile
  sky_profile = pygame.image.load('sky profile.png')
  skyprofileRect = sky_profile.get_rect()
  skyprofileRect = skyprofileRect.move((1070, 150))
  screen.blit(sky_profile, skyprofileRect)
  
  running = True
  while running:
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]

      if mx>25 and mx<218 and my>150 and my<614 and butt[0]== 1 and show == 'choices': #isaac
        DATE = 'isaac'
        running = False
      elif mx>226 and mx<420 and my>150 and my<614 and butt[0]==1 and show == 'choices': #ri
        DATE = 'ri'
        running = False
      elif mx>445 and mx<637 and my>150 and my<614 and butt[0]==1 and show == 'choices': #samantha
        DATE = 'samantha'
        running = False
      elif mx>645 and mx<842 and my>150 and my<614 and butt[0]==1 and show == 'choices': #fiona
        DATE = 'fiona'
        running = False
      elif mx>870 and mx<1066 and my>150 and my<614 and butt[0]==1 and show == 'choices': #blake
        DATE = 'blake'
        running = False
      elif mx>1070 and mx<1264 and my>150 and my<614 and butt[0]==1 and show == 'choices': #sky
        DATE = 'sky'
        running = False
    pygame.display.flip()
    #limit fps
    clock.tick(30)
  return DATE

def accountCreation(screen, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  click = 0
  running = True
  show = 'talking'
  load = 0
  clock=pygame.time.Clock()
  #load gerald's profile
  gerald_profile = pygame.image.load('gerald profile.png')
  geraldprofileRect = gerald_profile.get_rect()
  geraldprofileRect = geraldprofileRect.move((500, 0))
  while running:
    screen.blit(website, websiteRect)  
    if click == 0:
      mood = 'normal'
      dialogue = "You: I can't believe my friends convinced me to sign up for a dating site.   (press space to continue)"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      mood = 'normal'
      dialogue = "You: At least I'm done creating my profile."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      #display gerald's profile
      screen.blit(gerald_profile, geraldprofileRect)
      myfont = pygame.font.SysFont('Comic Sans MS', 50)
      screen.blit(myfont.render('Your profile:', False, colours_Dict['black']), (55, 55))
      myfont = pygame.font.SysFont('Comic Sans MS', 30)
      screen.blit(myfont.render('Press space to continue', False, colours_Dict['black']), (55, 200))
    if click == 3:
      #green loading bar fill up
      load += 8 #increments to fill up
      if load >= 400: #stop loading
        load = 400
      show = 'n/a' #can't continue
      myfont = pygame.font.SysFont('Comic Sans MS', 50)
      screen.blit(myfont.render('Finding hot singles near you ;)', False, colours_Dict['black']), (SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2))
      pygame.draw.rect(screen, (255, 255, 255), (590, 410, 400, 20))
      pygame.draw.rect(screen, (56, 213, 66), (590, 410, load, 20))
      if load == 400: 
        #prompt to continue
        screen.blit(myfont.render('Press space to view your matches', False, colours_Dict['black']), (SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT/2 + 200))
        show = 'talking'# can continue now that the bar is filled
    if click == 4: #stop running this part
      show = 'choices'
      running = False
      
    #monitor events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      #click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)


def secondDate(screen, proceed2, show):
  show = 'choices'
  bigfont = pygame.font.SysFont('Comic Sans MS', 30)
  myfont = pygame.font.SysFont('Comic Sans MS', 70)
  #black background
  screen.fill((0, 0, 0))
  #disclaimer!!!
  screen.blit(bigfont.render('Second dates are where things start to get serious (IN THIS WORLD!!!). Are you sure you want to commit to this individual?', False, (255, 255, 255)), (20, 300))
  #yes box
  pygame.draw.rect(screen, (255, 255, 255), (350, 400, 200, 100))
  screen.blit(myfont.render('YES', False, (0, 0, 0)), (390, 430))
  #no box
  pygame.draw.rect(screen, (255, 255, 255), (700, 400, 200, 100))
  screen.blit(myfont.render('NO', False, (0, 0, 0)), (760, 430))
  clock=pygame.time.Clock()
  running = True
  while running:
    
    #monitor events
    for event in pygame.event.get():
      print (event)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    
      if mx>350 and mx<550 and my>400 and my<500 and butt[0]== 1 and show == 'choices': #clicked yes
        proceed2 = True #will proceed to second date
        running = False #stop running function
      elif mx>700 and mx<900 and my>400 and my<500 and butt[0]== 1 and show == 'choices': #clicked no
        proceed2 = False #will not proceed to second date
        running = False # stop running function

    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)
  return proceed2