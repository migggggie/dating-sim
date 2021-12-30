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

#load icon images and add to list
gerald_happy = pygame.image.load('gerald_happy.png')
gerald_emb = pygame.image.load('gerald_emb.png')
gerald_sad = pygame.image.load('gerald_sad.png')
isaac_happy= pygame.image.load('isaac_happy.png')
isaac_confused = pygame.image.load('isaac_confused.png')
isaac_sad = pygame.image.load('isaac_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, isaac_happy, isaac_confused, isaac_sad, nothing]


def drawIcon(screen, speaker_List, speaker):
  #icon = speaker_List index
  icon = speaker_List[speaker]
  icon = pygame.transform.scale(icon, (160, 160))
  iconRect = icon.get_rect()
  if speaker < 3: #gerald (left side)
    iconRect = iconRect.move((10, 550))
  else: #someone else (right side)
    iconRect = iconRect.move(1110, 550)

  screen.blit(icon, iconRect)

def drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker):
  #black box (outline)
  pygame.draw.rect(screen, colours_Dict['black'], (95, SCREEN_HEIGHT - 205, SCREEN_WIDTH - 190, 185))
  #smaller box (actual speech box)
  pygame.draw.rect(screen, colours_Dict[mood], (100, SCREEN_HEIGHT - 200, SCREEN_WIDTH - 200, 175))
  #font
  myfont = pygame.font.SysFont('Comic Sans MS', 30)
  # test = myfont.render(dialogue, False, colours_Dict['white']) 
  words = [word.split(' ') for word in dialogue.splitlines()]  # 2D array where each row is a list of words.
  space = myfont.size(' ')[0]  # The width of a space.
  #max width
  max_width = 1100 
  #where x starts
  x = 115
  y = SCREEN_HEIGHT - 185
  for line in words: #for multiple lines of text (scan through every addition of a word and see if the length is higher than the max width, if it is, the x is reset and it will start on a new line)
      for word in line:
          word_surface = myfont.render(word, 0, colours_Dict['white'])
          word_width, word_height = word_surface.get_size()
          word_height = word_height + 5 #line space
          if x + word_width >= max_width:
              x = 115  # Reset the x.
              y += word_height  # Start on new row.
          screen.blit(word_surface, (x, y))
          x += word_width + space #shift where next word starts
      x = 115  # Reset the x.
      y += word_height  # Start on new row.
  #remember to draw who is speaking
  drawIcon(screen, speaker_List, speaker)
  

def drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List, choice, show):
  show = 'choices' #
  #black box
  pygame.draw.rect(screen, colours_Dict['black'], (95, SCREEN_HEIGHT - 205, SCREEN_WIDTH - 190, 185))
  #draw 3 choice boxes
  choice1_box = pygame.draw.rect(screen, colours_Dict[mood], (100, SCREEN_HEIGHT - 140, SCREEN_WIDTH - 200, 35))
  choice2_box = pygame.draw.rect(screen, colours_Dict[mood], (100, SCREEN_HEIGHT - 100, SCREEN_WIDTH - 200, 35))
  choice3_box = pygame.draw.rect(screen, colours_Dict[mood], (100, SCREEN_HEIGHT - 60, SCREEN_WIDTH - 200, 35))
  myfont = pygame.font.SysFont('Comic Sans MS', 30)
  #prompt
  screen.blit(myfont.render(prompt, 1, colours_Dict['white']), (115,SCREEN_HEIGHT - 185))
  screen.blit(myfont.render(choice_List[0], 1, colours_Dict['white']), (115, 590))
  screen.blit(myfont.render(choice_List[1], 1, colours_Dict['white']), (115, 630))
  screen.blit(myfont.render(choice_List[2], 1, colours_Dict['white']), (115, 670))

def isaacDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # isaac introduces himself and compliments your hat
  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Isaac when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with the face of Isaac himself. He looks just like his profile picture. You are relieved that he is not a 60 year old man trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: You're Gerald, right? I'm Isaac. I like your hat!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I'm Gerald and thank you. Nice to meet you, Isaac."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Isaac orders a medium cold chocolate and a vanilla cupcake. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Isaac leads you to a booth in the back of the cafe away from the few other diners. You both take a seat and take a sip of your cold chocolates at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK ! you need to initiate conversation
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about his schooling!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def isaacDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #You: so you're majoring in ____ [cheese, chem, physics]
  mood = 'normal'
  prompt = "He's majoring in..."
  choice_List = ['Cheese', 'Chemistry', 'Physics']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #cheese (makes isaac confused)
    #isaac: What?
    #You: Nvm
    #you ask isaac a lot about his schooling and try to seem extra interested to make up for your earlier blunder
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Cheese?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: What?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uh... nevermind..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #chemistry (makes isaac happy)
    #isaac: yep! have you ever heard of H2O?
    #You: yeah it's crazy!
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Chemistry?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Yep! Have you ever heard of H2O?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 8:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, it's crazy."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
    #physics (makes isaac sad)
    #isaac: uh...no. my profile says I'm a Chemistry major
    #You: oh, my bad
    #you ask isaac a lot about his schooling and try to seem extra interested to make up for your earlier blunder.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Physics?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "Isaac: No...It said on my profile that I was a Chemistry major."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh...my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "You ask Isaac a lot about his schooling and try to seem extra interested to make up for your earlier blunder. It appears to work."
    elif choice == 2:
      dialogue = "Isaac tells you about some of his classmates and teachers. He seems really passionate about chemistry."
    elif choice == 3:
      dialogue = "You ask Isaac a lot about his schooling and try to seem extra interested to make up for your earlier blunder. You even throw in a dig at physics once in a while. It makes him laugh."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
  return show

def isaacDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #eventually, isaac asks you who your favourite band is [1D, Peach Tree Rascals, Tenacious D]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "A certain amount of time passes before Isaac changes the subject."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: So who's your favourite band?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['One Direction', 'Peach Tree Rascals', 'Tenacious D']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #One Direction (makes isaac sad)
    #isaac: That's the kind of music my 5 year old sister listens to
    #You: well, I like it
    #You sit in silence for a minute before Isaac apologizes if he offended you. He's working on it. You keep talking and talking.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I really enjoy One Direction's music."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Isaac: That's the kind of music my 5 year old niece listens to."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Well I like it..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #Peach Tree Rascals
    #isaac: Wow, me too!
    #You: Cool
    #The two of you discuss your favourite songs by Peach Tree Rascals and the conversation flows easily. 
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I really enjoy Peach Tree Rascals' music."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Wow, me too!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Really? That's cool!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
    #Tenacious D
    #isaac: who?
    #You: nvm
    #In an attempt to recover from that, you ask Isaac about his family. He lets you off the hook and continues on with the new topic. The conversation continues for a while after that
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I really enjoy Tenacious D's music."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: Who???"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uhhh...nevermind..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "You sit in silence for a minute before Isaac apologizes if he offended you with his reaction. He's working on it. You've never been one to hold grudges so the two of you keep talking and talking."
    elif choice == 2:
      dialogue = "The two of you discuss your favourite songs by Peach Tree Rascals and the conversation flows easily. Turns out you have very similar taste in music."
    elif choice == 3:
      dialogue = "In an attempt to recover from that, you ask Isaac about his family. He lets you off the hook and continues on with the new topic. The conversation continues for a while after that."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def isaacDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
    # You realize that Isaac is a pretty cool guy.
    #The conversation gets to a point where Isaac asks you:
    #Isaac: So are you looking for something serious?
    #[No, open to anything, yes]
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You realize that Isaac is a pretty cool guy."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "The conversation brings itself to a point where Isaac asks you another question."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: So are you looking for something serious?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    speaker = 6
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['No', "I'm open to anything right now", 'Yes']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #not with you (makes isaac sad)
    #isaac: oh...
    #You: I worded that wrong. I'm not looking for anything serious with ANYONE, not just you
    #isaac digests that for a moment, but he still seems kind of sad. Thankfully, it doesn't last too long and he's back to normal after a few minutes.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Not with you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 5
      mood = 'sad'
      dialogue = "Isaac: Oh...I see..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Sorry I worded that wrong!!! I'm not looking for anything serious with ANYONE, not just you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #I'm open to anything right now (makes isaac happy)
    #isaac: Same. I'm only 19 right now, so I'm not looking to commit right away, but I'm down to go with the flow.
    #You: That's completely fair
    #Isaac is pretty chatty. He tells you countless stories and you find yourself enjoying all of them. You notice the way he pushes his glasses up his face every now and then. It's cute.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I'm open to anything at the moment."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Same. I'm only 19 right now, so I'm not looking to commit right away, but I'm definitely down to go with the flow."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 21:
      speaker = 0
      mood = 'normal'
      dialogue = "You: That's fair."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
    #Yes, according to my 10 year plan, I should be married with kids in 2 years
    #isaac: oh...uh...well. I'm only 19, so I don't know how I feel about that
    #You: well, you have 2 years
    #isaac looks afraid for a second, but he is able to awkwardly push through the conversation and change the topic.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yes, according to my 10 year plan, I should be married with 3 kids in 2 years."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: Oh...uh...well. I'm only 19, so I don't know how I feel about that..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Well, you have 2 years."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Isaac digests that for a moment, but he still seems kind of sad. Thankfully, it doesn't last too long and he's back to normal after a few minutes."
    elif choice == 2:
      dialogue = "Isaac is pretty chatty. He tells you countless stories and you find yourself enjoying all of them. You notice the way he pushes his glasses up his face every now and then. It's cute."
    elif choice == 3:
      dialogue = "Isaac looks afraid for a second, but he is able to awkwardly push through the conversation and change the topic."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def isaacDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #Isaac: Well. It was nice meeting you!
  #You: Yeah, talk to you soon!
  #BYE
  #display date complete
  #end run
  if click == 23:
    speaker = 6
    mood = 'narrator'
    dialogue = "A while later..."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: Well, I got to get going now, but it was really nice meeting you!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise. Talk to you soon!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'normal'
    dialogue = "DATE COMPLETE!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)



#-------------------------------------------FIRST DATE
def isaacDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the dates together
  #declare clock
  clock=pygame.time.Clock()
  running = True
  click = 0
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running:
    screen.blit(diner, dinerRect) #clear screen/draw background
    isaacDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11:
      isaacDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)

    if click >= 10: #run part 2
      isaacDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)

    if click >= 16: # run part 3
      isaacDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)

    if click >= 23: # run the ending
      isaacDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    for event in pygame.event.get():
      # print (event)
      print (show)
      print(click)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    

      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices':
        choice = 1 #user selects first option
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices':
        choice = 2 #user selects second option
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices':
        choice = 3 #user selects third option
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1 #add one to click count (determines what dialogue to show)
        print(click)
      if click == 11 or click == 18:
        choice = 0 #reset choice before next time user is presented with a decision
      if click == 27:
        running = False #stop running
    # Flip the display
    pygame.display.flip()
    #limit frame rate
    clock.tick(30)


def isaacDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Isaac has brought you to a building with a huge neon sign reading, "Arctic Arcade".
  # You hold the door open for Isaac and are hit by the flashing lights and the sound and distinct scent of children everywhere.
  # Isaac brings you to the dining area where it's much quieter and smells less... musty. It's a welcome change of scene.
  # ISAAC: It's nice to see you again!
  # GERALD: Likewise!
  # ISAAC: How have you been recently?
  # GERALD: Pretty good, can't complain. You?
  # ISAAC: Yeah, same here.
  # Isaac adjusts his glasses and picks up a menu to read. You look through yours as well.
  # WAITRESS: What can I get you folks?
  # GERALD: I'll have a cheeseburger and root beer, please.
  # ISAAC: Can I please get a chicken cesar salad and an iced coffee?
  # WAITRESS: Coming right up!
  # Your food arrives a few minutes later and you both eat and engage in small talk.
  # ISAAC: How's your food?
  # GERALD: It's nice.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Isaac has brought you to a building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "You hold the door open for Isaac and are hit by the flashing lights and the sound and distinct scent of children everywhere."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 6
    mood = 'narrator'
    dialogue = "Isaac brings you to the dining area where it's much quieter and smells less... musty. It's a welcome change of scene."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: It's nice to see you again!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: How have you been recently?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Pretty good, can't complain. You?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: Yeah, same here."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8:
    speaker = 6
    mood = 'narrator'
    dialogue = "Isaac adjusts his glasses and picks up a menu to read. You look through yours as well."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: What can I get you folks?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10:
    speaker = 0
    mood = 'normal'
    dialogue = "You: I'll have a cheeseburger and root beer, please."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11: 
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: Can I please get a chicken cesar salad and an iced coffee?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Coming right up!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "Your food arrives a few minutes later and you both eat and engage in small talk."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: How's your food?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def isaacDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # GERALD: It's nice.."
  # ISAAC: Yeah, same. I've never actually eaten here before.
  # ISAAC: What do you think of this place?
  # How will you respond?
    # [It's kind of smelly, Reminds me of when I was a kid, Kinda spooky]
  if click == 15:
    speaker = 0
    mood = 'normal'
    dialogue = "You: It's nice..."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: Yeah, same. I've never actually eaten here before."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: What do you think of this place?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ["It's kind of smelly", "Reminds me of when I was a kid", "Kinda spooky"]
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1: It's kind of smelly (makes Isaac sad)
    # GERALD: It's kind of smelly here.
    # ISAAC: I mean... you're not wrong, but there are redeeming qualities.
    # GERALD: Yeah, definitely. But it still smells.
    # ISAAC: Haha, I guess yeah. #EMBARRASSED ISAAC ICON
    # GERALD: It's cool, though. So far the food is good.
    # ISAAC: True.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: It's kind of smelly"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Isaac: I mean... you're not wrong, but there are redeeming qualities."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Yeah, definitely. But it still smells."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: #EMBARRASSED ISAAC ICON
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: Haha, I guess."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "It's cool, though. So far the food is great."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: True."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Reminds me of when I was a kid (makes Isaac happy)
    # GERALD: It's nice. Arcades remind me of when I was a kid. My parents used to take me when I was younger.
    # ISAAC: Wow, same. I spent birthdays 7 through 11 at an arcade.
    # GERALD: That sounds like it was fun. Was it this one?
    # ISAAC: No, it was an arcade back home. This arcade is the only one in the area.
    # ISAAC: I'm glad you like this place though.
    # GERALD: I'm glad you took me here.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Reminds me of when I was a kid."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Wow, same. I spent birthdays 7 through 11 at an arcade."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 0
      mood = 'normal'
      dialogue = "You: That sounds like it was fun. Was it this one?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: No, it was an arcade back home. This arcade is the only one in the area."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: I'm glad you like this place though."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I'm glad you brought me here."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Kinda spooky (makes Isaac confused)
    # GERALD: Hm, it's kinda spooky.
    # ISAAC: Spooky? How so?
    # GERALD: All the flashing lights, they're practically flickering lights in an abandoned hospital.
    # ISAAC: Really? They're neon lights and there are people everywhere...
    # GERALD: Clearly you have not watched enough horror movies.
    # ISAAC: None that start like this... but don't worry, I'll protect you.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "It's kinda spooky."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: Spooky? How so?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 2
      mood = 'sad'
      dialogue = "You: All the flashing lights, they're practically flickering lights in an abandoned hospital."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: 
      speaker = 4
      mood = 'confused'
      dialogue = "Isaac: Really? They're neon lights and there are people everywhere..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Clearly you have not watched enough horror movies."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: None that start like this...but don't worry, I'll protect you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def isaacDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # You both take turns talking and eating.
  # Eventually, you're both done with your food and the waitress brings over your bill.
  # You split it and Isaac takes you over to the games with all of the lights and noise.
  # He half-yells in order to be heard.
  # ISAAC: You choose where I should go first
    # [Skeeball, Karaoke, Australia]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You both take turns talking and eating."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 6
    mood = 'narrator'
    dialogue = "Eventually, you're both done with your food and the waitress brings over your bill."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'narrator'
    dialogue = "You try to pay, but Isaac insists that he wil pay. You end up splitting it and Isaac takes you over to the games with all of the lights and noise."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "He half-yells in order to be heard."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Isaac: You choose where I should go first."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "Which station will you send Isaac to?"
      choice_List = ['Skeeball', 'Karaoke', 'Australia']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Skeeball (makes Isaac happy)
    # GERALD: You should try the skeeball machine.
    # ISAAC: Alright, bet.
    # GERALD: So, I made a good choice?
    # ISAAC: Amazing choice.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You should try the skeeball machine."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Alright, bet."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So, I made a good choice?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Amazing choice."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Karaoke (makes Isaac sad)
    # GERALD: You down for karaoke?
    # ISAAC: No, I'm not much of a singer. Plus, I don't think the karaoke machine is even open today.
    # GERALD: Oh, you can pick then.
    # ISAAC: Alright, well, the skeeball machine is always fun.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You down for karaoke?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Isaac: No, I'm not much of a singer. Plus, I don't think the karaoke machine is even open today."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, you can pick then."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Isaac: Alright, the skeeball machine is always fun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Australia (makes Isaac confused)
    # GERALD: Australia.
    # ISAAC: Huh? 
    # GERALD: Uh...
    # ISAAC: Let's just head over to the skeeball machine...
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Australia."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Huh?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uh..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 4
      mood = 'confused'
      dialogue = "Let's just head over to the skeeball machine."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # You follow Isaac to the skeeball machine and he stretches his fingers dramatically before picking up a ball.
  # Maybe there's actually a method to the finger stretching because he's dominating.
  # Isaac finishes his round and the machine spews out what you can only imagine to be, like, a million tickets.
  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "You follow Isaac to the skeeball machine and he stretches his fingers dramatically before picking up a ball."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Maybe there's actually a method to the finger stretching because he's dominating."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "Isaac finishes his around and the machine spews out what you can only imagine to be, like, a million tickets."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def isaacDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # GERALD: Alright, where should I go now?
  # Isaac points to a game called "CLOUDY WITH A CHANCE OF APPLES". Alright, here we go.
  # GERALD: Alright, prepare to witness superhuman gaming!
  if click == 36:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You: Alright, where should I go?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "Isaac points to a game called 'CLOUDY WIHT A CHANCE OF APPLES' Alright, here we go."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def isaacDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # INSERT GAME
  if click == 39:
    speaker = 6
    mood = 'narrator'
    dialogue = "insert game"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # if click == 23:
  #   speaker = 6
  #   mood = 'narrator'
  #   dialogue = "Sky rarely has trouble finding the words to say, so the conversation never gets dull. Admittedly, it's one of the more advanced vocubalary-filled conversations you've had in quite some time, but you enjoy it."
  #   drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # if click == 24:
  #   speaker = 3
  #   mood = 'normal'
  #   dialogue = "Sky: Well, I got to get going now, but it was really nice meeting you!"
  #   drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # if click == 25:
  #   speaker = 0
  #   mood = 'normal'
  #   dialogue = "You: Likewise. Talk to you soon!"
  #   drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # if click == 26:
  #   speaker = 6
  #   mood = 'normal'
  #   dialogue = "DATE COMPLETE!"
  #   drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)



def isaacDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the parts together
  running = True
  click = 0
  clock=pygame.time.Clock()
  # arcade interior image load
  arcadein = pygame.image.load("arcadein.png")
  arcadeinRect = arcadein.get_rect()
  #arcade exterior image load
  arcadeout = pygame.image.load("arcadeout.png")
  arcadeoutRect = arcadeout.get_rect()
  #kitchen image load
  kitchen = pygame.image.load("kitchen.png")
  kitchenRect = kitchen.get_rect()


  while running:
    #background image (clear/fill) 0, 1, 2, 27
    if click == 0:
      screen.blit(arcadeout, arcadeoutRect)
    if click == 1 or click >= 27:
      screen.blit(arcadein, arcadeinRect)
    if click >= 2 and click < 27:
      screen.blit(kitchen, kitchenRect)
    
    #intro
    isaacDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      isaacDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      isaacDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      isaacDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = isaacDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      isaacDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      print (event)
      print (show)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    

      if (mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1) and show == 'choices': #top button chosen
        choice = 1
      elif (mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1) and show == 'choices': #middle button chosen
        choice = 2
      elif (mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1) and show == 'choices': #bottom button chosen
        choice = 3
      
      #click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click)
        #reset choice
      if click == 17 or click == 24:
        choice = 0
        #stop running
      if click == 40:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)

def isaacDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):

  running = True
  click = 0
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  isaac_final = pygame.image.load("isaac_final_40.png")
  isaac_finalRect = isaac_final.get_rect()
  isaac_finalRect = isaac_finalRect.move(370, 50)
  #declare clock
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running: # run until end
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "To be honest, you expected to just hang out at a restaurant or watch a movie, but Isaac said he had a better idea."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "And he was right, this is a much better idea."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "The night is chilly, just the way you like it. Despite the lack of snow, it’s still beautiful."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "Isaac walks along ahead of you, and pulls a blanket out of his backpack. You were wondering why he brought a bag."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "He places the blanket on the grass and beckons for you to come over and sit with him. You do so."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "You both lie down on your backs and stare at the stars. Isaac points at the sky and begins naming constellations. You’re not really listening to everything he’s saying, moreso just appreciating his enthusiasm."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "At some point, you close your eyes and Isaac also stops talking. You’re not sleeping, but you are more relaxed than you’ve ever been in a long time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "Isaac breaks the silence by telling you that he’s glad you called. You tell him of course you were going to call."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "You ask Isaac how he found this place. He tells you a story about his parents’ divorce. Apparently, they would argue quite a bit, and in order to escape his house, he would run here with his dog."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "You’re a bit thrown off by the sudden vulnerability. Instead you ask about his dog."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "Isaac smiles fondly as he thinks of his pet. He tells you that she’s a nine year old beagle who loves snow people, but not so much other dogs. He says that next time, you should meet her."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "Next time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "You smile thinking of a next time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "You roll over a bit so that you are now facing Isaac. He takes notice and rolls over and locks eyes with you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "You can see yourself in the reflection in his glasses."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "You tell him he has cute glasses and his cheeks turn the deepest shade of red as he hesitantly pushes them up his carrot nose."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "He tells you that you have a cute face. Now it’s your turn to blush. He chuckles."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "He rolls back onto his back and excitedly points at the sky. You turn your head to look at the sky."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "There's a shooting star passing by."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "If you’re being honest, it’s slightly underwhelming. You’ve never seen one before, but you kind of expected blue fire and loud whistling sounds. Instead, it’s just a bright light travelling across the sky."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "But Isaac is so excited that you find yourself unable to look away from it. Until you look at Isaac that is."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "You tell him to make a wish."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "He closes his eyes for a few seconds and remains silent."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "You ask him what he wished for."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "He blushes."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      dialogue = "'I wished to hold your hand.'"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      dialogue = "You can make that happen. Your heart starts pounding just a little bit harder as you move your arm closer to Isaac and place your palm face up and open on the ground."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 27:
      dialogue = "You’re too nervous to face Isaac, but you hope he notices."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 28:
      dialogue = "A few seconds pass and you’re beginning to think he didn’t realize, but you feel fingers slowly interlocking between yours."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 29:
      dialogue = "Isaac squeezes just a little bit and you squeeze back."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      dialogue = "You can feel that this is the start of something new."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      #final polaroid
      screen.fill((0, 0, 0))
      screen.blit(isaac_final, isaac_finalRect)

      
    for event in pygame.event.get():
    
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click) #click counter
      if click == 33:
        running = False #stop runnign

    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)