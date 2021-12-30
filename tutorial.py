from isaacDates import *

import pygame
pygame.init()
pygame.font.init()
from pygame.locals import * 

colours_Dict = { 'narrator': (202, 160, 245), 'sad': (23, 42, 102), 'confused': (235, 148, 122), 'normal': (77, 197, 155), 'white': (255, 255, 255), 'black': (0, 0, 0)}
dialogue = ''
speaker_List = []
speaker = 6
characters = ''
mood = ''
choice = 0

#load icons
gerald_happy = pygame.image.load('gerald_happy.png')
gerald_emb = pygame.image.load('gerald_emb.png')
gerald_sad = pygame.image.load('gerald_sad.png')
narrator = pygame.image.load('nothing.png')
generic= pygame.image.load('no pfp.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, narrator, generic]


def tutorial_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #start tutorial
  #space = continue
  #mouse/trackpad = choose something
  if click == 0:
    speaker = 3
    mood = 'narrator'
    dialogue = "Welcome to the tutorial for 'Finding Gerald Love'. Make sure your pygame window is maximized, otherwise your view of the game will be impacted negatively. The spacebar is your best friend. Press space right now to see what happens."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    #press space again
  if click == 1:
    speaker = 3
    mood = 'narrator'
    dialogue = "WOW! You moved on to the next dialogue piece. This feature works the same way in the actual game! Try it again, just to master it!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 3
    mood = 'narrator'
    dialogue = "Dang, you're a quick learner! There's still more to it though! Go ahead, move on to the next part!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    #introduce you (gerald)
  if click == 3:
    speaker = 0
    mood = 'normal'
    dialogue = "This is you. You are Gerald. You are one. The box is also a different colour now??? WOAH!!! Earlier     it was purple, indicating that the NARRATOR was speaking. This colour means normal dialogue."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #confused example
  if click == 4:
    speaker = 1
    mood = 'confused'
    dialogue = "This colour is confused/embarrassed depending on who is speaking. It'll make sense later."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #sad example
  if click == 5:
    speaker = 2
    mood = 'sad'
    dialogue = "Colour changed again! Oh no, now you're sad :("
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def tutorial_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # Show decision making tutorial (use mouse)
  mood = 'normal'
  prompt = "Use your mouse or trackpad to select an option by clicking on it."
  choice_List = ['1', '2', '3']
  show = 'choices'
  if click == 6: #show options
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    #1 selected
    show = 'talking'
    if click == 6:
      speaker = 3
      mood = 'narrator'
      dialogue = "You chose 1."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #2 selected
    if click ==6:
      speaker = 3
      mood = 'narrator'
      dialogue = "You chose 2."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
    #3 selected
    if click == 6:
      speaker = 3
      mood = 'narrator'
      dialogue = "You chose 3."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  #explain what choices do in game
  if click == 7:
    speaker = 3
    mood = 'narrator'
    dialogue = "Right now, what you choose doesn't really do anything, but it will in the real game! Remember space is to continue and mouse/trackpad is for choosing between options that the game will provide."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  return show

def tutorial_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #example with a date
  if click == 8:
    speaker = 3
    show = 'talking'
    mood= 'narrator'
    dialogue = "Let's introduce your date. This is Noname. To the right is their photo. Look, they're about to ask you a question!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #date asks question
  if click == 9:
    show = 'talking'
    speaker = 4
    mood = 'normal'
    dialogue = "Noname: What month is April Fool's Day in?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10:
    mood = 'normal'
    prompt = "How will you respond? Click on your answer."
    choice_List = ['January', 'December', 'April']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #january
    if click == 10:
      speaker = 0
      mood = 'normal'
      dialogue = "You: It's in January, right?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      speaker = 4
      mood = 'sad'
      dialogue = "Noname: No...it's in April."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      speaker = 3
      mood = 'narrator'
      dialogue = "I'm not one to judge people, but why the heck did you pick January? Were you just joking around or were you just curious what would happen if you did? Anyway, continue."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #december
    if click ==10:
      speaker = 0
      mood = 'normal'
      dialogue = "You: It's in December, right?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 11:
      speaker = 4
      mood = 'confused'
      dialogue = "Noname: Uh...no??? It's in April."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 12:
      speaker = 3
      mood = 'narrator'
      dialogue = "December? Really? You picked December??? No judgement, but you're probably that person who adds an option to a poll that is already there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
    #april
    if click == 10:
      speaker = 0
      mood = 'normal'
      dialogue = "You: April? Duh."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 11:
      speaker = 4
      mood = 'normal'
      dialogue = "Noname: Yeah, you got it!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      speaker = 3
      mood = 'narrator'
      dialogue = "That was kind of a gimme, but you get the idea."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def tutorial_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #one more decision tutorial
  if click == 13:
    speaker = 3
    show = 'talking'
    mood= 'narrator'
    dialogue = "Let's go through the decision making process one more time. Practice makes perfect, right?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 3
    mood= 'narrator'
    dialogue = "Just a quick disclaimer: sometimes, Repl will have a small click delay. You can try clicking again, and it should work after max a few tries. Anyway, let's keep going on with the tutorial."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    speaker = 4
    mood = 'normal'
    dialogue = "Noname: Do you like video games?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 6
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Yes', "No", 'Idk']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #yes
    if click == 16:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, I love them."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      speaker = 4
      mood = 'sad'
      dialogue = "Noname: Ew. So you're one of THEM..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Excuse me?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #no
    if click == 16:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Nah, I'm not a fan."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 17:
      speaker = 4
      mood = 'normal'
      dialogue = "Noname: Me neither. I prefer going outside and eating grass."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 18:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uh...ok"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
    #idk
    if click == 16:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I don't know."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 17:
      speaker = 4
      mood = 'confused'
      dialogue = "Noname: How can you not know?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      speaker = 1
      mood = 'confused'
      dialogue = "You: I just don't."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    #narrator lines
    speaker = 3
    mood = 'narrator'
    if choice == 1:
      dialogue = "Noname didn't seem to like that answer. No matter, you gotta be honest to yourself, right? Also, if someone reacts like that to you saying you like video games, you probably don't want to date them anyway."
    elif choice == 2:
      dialogue = "Wow. You managed to find another individual under the age of 40 who doesn't like video games...Good for you, I guess."
    elif choice == 3:
      dialogue = "Hm...even I'm confused...Whatever."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def tutorial_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #ending tutorial take care of gerald
  if click == 20:
    speaker = 3
    mood = 'narrator'
    dialogue = "Well, you seem to have a good grasp of the mechanics of the game. Good luck. And do me a favour and take good care of our boy Gerald, ok?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 21:
    speaker = 3
    mood = 'narrator'
    dialogue = "Well, it's about time I let you go off into the real world, or, I guess the real game. See you on the other side!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    speaker = 3
    mood = 'narrator'
    dialogue = "TUTORIAL COMPLETE! REAL GAME STARTING NOW!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)



#-------------------------------------------FIRST DATE
def tutorial_full (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the parts together
  clock=pygame.time.Clock()
  running = True
  click = 0
  #load diner
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running:
    #background (clear/fill)
    screen.blit(diner, dinerRect)
    #intro
    tutorial_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11: # part 1
      tutorial_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = tutorial_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #part 2
    if click >= 8:
      tutorial_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = tutorial_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #part 3
    if click >= 13:
      tutorial_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = tutorial_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 20:#tutorial ending
      tutorial_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    
      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices': #clicked top option
        choice = 1
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices': #clicked middle options
        choice = 2
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices': #clicked bottom options
        choice = 3
      
      #click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
      #reset choice
      if click == 8 or click == 13:
        choice = 0
      #end running
      if click == 23:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)

def needTut(screen, needTutorial, show):
  show = 'choices'
  clock=pygame.time.Clock()
  #declare fonts
  bigfont = pygame.font.SysFont('Comic Sans MS', 46)
  smallfont = pygame.font.SysFont('Comic Sans MS', 30)
  myfont = pygame.font.SysFont('Comic Sans MS', 70)
  #ask if they want tutorial
  screen.blit(bigfont.render('Would you like to go through a tutorial? (recommended for first timers)', False, (255, 255, 255)), (100, 300))
  #READ TXT FILE
  screen.blit(smallfont.render('Please read the 1_readme.txt file before playing!', False, (255, 255, 255)), (100, 360))
  #draw yes box
  pygame.draw.rect(screen, (255, 255, 255), (350, 400, 200, 100))
  screen.blit(myfont.render('YES', False, (0, 0, 0)), (390, 430))
  #draw no box
  pygame.draw.rect(screen, (255, 255, 255), (700, 400, 200, 100))
  screen.blit(myfont.render('NO', False, (0, 0, 0)), (760, 430))
  #doesn't need to be loop
  running = True
  while running:
    
    for event in pygame.event.get():
      print (event)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    
      if mx>350 and mx<550 and my>400 and my<500 and butt[0]== 1 and show == 'choices': #clicked yes
        needTutorial = True #will run tutorial
        running = False #stop running this function
      elif mx>700 and mx<900 and my>400 and my<500 and butt[0]== 1 and show == 'choices': #clicked no
        needTutorial = False #proceed without a tutorial
        running = False #stop running this function

    # Flip the display
    pygame.display.flip()
    clock.tick(30)
  return needTutorial