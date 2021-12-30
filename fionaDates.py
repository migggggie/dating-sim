import pygame
pygame.init()
pygame.font.init()
from pygame.locals import * 
from isaacDates import *

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
fiona_happy= pygame.image.load('fiona_happy.png')
fiona_confused = pygame.image.load('fiona_confused.png')
fiona_sad = pygame.image.load('fiona_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, fiona_happy, fiona_confused, fiona_sad, nothing]

def fionaDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # fiona introduction and compliments your hat
  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Fiona when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with Fiona's face. She looks just like her profile picture. You are relieved that she is not a 60 year old man trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: You're Gerald, right? I'm Fiona. Cute hat!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I'm Gerald and thank you. Nice to meet you, Fiona."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Fiona orders a large cold chocolate and a croissant. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Fiona takes you to a booth in the back of the cafe away from the few other diners. You both take a seat and take a sip of your cold chocolates at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK ! you need to initiate conversation
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about her schooling!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def fionaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
#What is she majoring in? [engineering, elephants, math]
  mood = 'normal'
  prompt = "She's majoring in..."
  choice_List = ['Engineering', 'Elephants', 'Mathematics']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #Engineering (makes fiona happy)
    #Fiona: Yeah, you got it! I'm impressed that you remembered!
    #You: Of course I did, how could I not?
    #Fiona tells you about her classes and teachers. Apparently, one of her math professors only calls in the boys during class. You make sure to tell her that you think that is immoral and even ask her a math question to make up for her professor. She laughs at that.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Engineering?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: Yeah, you got it! I'm impressed that you remembered!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'normal'
      dialogue = "You: Of course I did, how could I not?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #Elephants (makes fiona confused)
    #Fiona: I'm sorry, did you say elephants?
    #You: Um...forget about it.
    #Fiona tells you she is an Engineering major and you try to cover up your earlier mistake by asking tons of questions about her schooling. She answers all your questions and asks you some questions in return.
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Elephants?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Fiona: I'm sorry, did you say elephants?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click  == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Heh...forget about it..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
  #Mathematics (makes fiona sad)
    #Fiona: No, my profile says that I'm an Engineering major...
    #You: Oh, that's my bad...
    #In order to recover from your mistake, you make sure to appear extremely invested as Fiona talks about her classes and professors. She seems to appreciate the effort and her smile is back quickly.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're majoring in Mathematics?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "Fiona: No...It said on my profile that I was an Engineering major."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh that's my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Fiona tells you about her classes and teachers. Apparently, one of her math professors only calls in the boys during class. You make sure to tell her that you think that is immoral and even ask her a math question to make up for her professor. She laughs at that."
    elif choice == 2:
      dialogue = "Fiona tells you she is an Engineering major and you try to cover up your earlier mistake by asking tons of questions about her schooling. She answers all your questions and asks you some questions in return."
    elif choice == 3:
      dialogue = "In order to recover from your mistake, you make sure to appear extremely invested as Fiona talks about her classes and professors. She seems to appreciate the effort and her smile is back quickly."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def fionaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #The conversation flows easily after that. You both jump from topic to topic and rarely face an awkward silence, however there still are a few. In one of them, Fiona asks you a question.
  #Fiona: What would be your spirit animal? [bird, potato, don't believe]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "The conversation flows easily after that. You both jump from topic to topic and rarely face an awkward silence, however there still are a few. In one of them, Fiona asks you a question."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: What would be your spirit animal?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Bird', 'Potato', "I don't believe in spirit animals"]
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #A bird (makes fiona sad)
    #Fiona: Ugh, I hate birds. Foul creatures
    #You: Wow. Tell me how you really feel...
    #Fiona collects herself for a minute. She apologizes and tells you she has some history with birds that she may reveal to you one day. You just nod.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I would definitely be a bird."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Fiona: Ugh, I hate birds. They're foul creatures."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Wow. Tell me how you really feel..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #A potato (makes fiona happy)
    #Fiona: Haha, relatable.
    #You: How about you?
    #Fiona ponders for a moment before telling you that she relates a lot to otters. Not a bad choice; otters are cute.
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: A potato, probably."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: Haha, relatable."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: How about you?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #I don't believe in spirit animals (makes fiona confused)
    #Fiona: Uh...I mean, you don't have to? It's just a question about your personality...
    #You: Hm...I suppose.
    #Fiona sheepishly tells you that she relates to otters a lot because of the way they hold hands with other otters. You try to act impressed because you don't want to offend her.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I don't believe in spirit animals."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Fiona: Uh...I mean, you don't have to? It's just a question about your personality."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Hm...I suppose."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Fiona collects herself for a minute. She apologizes and tells you she has some history with birds that she may reveal to you one day. You just nod."
    elif choice == 2:
      dialogue = "Fiona ponders for a moment before telling you that she relates a lot to otters. Not a bad choice; otters are cute."
    elif choice == 3:
      dialogue = "Fiona sheepishly tells you that she relates to otters a lot because of the way they hold hands with other otters. You try to act impressed because you don't want to offend her."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def fionaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #Fiona tries to change the topic.
  #She asks you what your favourite TV Show is [no tv, office us, office uk]

  #Fiona: What's your favourite TV Show?
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Fiona tries to change the topic."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "She asks you what your favourite TV Show is."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: What's your favourite TV show?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    speaker = 6
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ["Never heard of it", "The Office US", 'The Office UK']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #I've never heard of TV (makes fiona confused)
    #Fiona: You've...never...heard of TV? Really?
    #You: ...Yes...
    #She attempts to explain what TV is to you, but she doesn't seem like she actually believes you. She informs you that her favourite TV show is 'The Office'. You stare back at her blankly before she gives up and changes the topic.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: TV? Never heard of it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 4
      mood = 'confused'
      dialogue = "Fiona: You've never heard of TV? Really?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: ...Yes."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #The Office US (makes fiona happy)
    #Fiona: Really? Me too! Who's your favourite character?
    #You: Definitely Jim.
    #Fiona nods. You learn that she likes Jim, but her favourite character is actually Darryl. Unexpected, but you can understand it. You both talk about The Office US for what feels like an eternity, but you enjoy every second of it. Despite both of your enthusiasm towards the show, the conversation strays from the topic, but you're still just as engaged.
    if click ==19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: The Office US will always have a special place in my heart."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: Really? Me too! Who's your favourite character?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 21:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Definitely Jim."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #The Office UK (makes fiona sad)
    #Fiona: Really? I find it so difficult to watch. My favourite show is actually the US version.
    #You: You and everyone else...
    #Fiona tries to make you feel better by validating your opinion, but you tell her you're used to it by now. Most people have the same reaction when you tell them they prefer the UK version. She promptly changes the topic to literally anything else.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: The Office UK"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 4
      mood = 'sad'
      dialogue = "Fiona: Really? I find it so difficult to watch. My favourite show is actually the US version."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'sad'
      dialogue = "You: You and everyone else..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "She attempts to explain what TV is to you, but she doesn't seem like she actually believes you. She informs you that her favourite TV show is 'The Office'. You stare back at her blankly before she gives up and changes the topic."
    elif choice == 2:
      dialogue = "Fiona nods. You learn that she likes Jim, but her favourite character is actually Darryl. Unexpected, but you can understand it. You both talk about The Office US for what feels like an eternity, but you enjoy every second of it. Despite both of your enthusiasm towards the show, the conversation strays from the topic, but you're still just as engaged."
    elif choice == 3:
      dialogue = "Fiona tries to make you feel better by validating your opinion, but you tell her you're used to it by now. Most people have the same reaction when you tell them they prefer the UK version. She promptly changes the topic to literally anything else."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def fionaDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #You talk with Fiona and find yourself feeling very comfortable with her, despite only meeting her today. Her personality is very welcoming and her smile makes you want to smile as well. You feel yourself wanting to run your fingers through her hair, but that would definitely prove awkward over the table. Also you just met her, so you shouldn't do that.
  #Fiona: Well. It was nice meeting you!
  #You: Yeah, talk to you soon!
  #BYE
  #display date 
  if click == 23:
    speaker = 6
    mood = 'narrator'
    dialogue = "You talk with Fiona and find yourself feeling very comfortable with her, despite only meeting her today. Her personality is very welcoming and her smile makes you want to smile as well. You feel yourself wanting to run your fingers through her hair, but that would definitely prove awkward over the table. Also you just met her, so you shouldn't do that."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: Well, I got to get going now, but it was wonderful meeting you!"
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
def fionaDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the dates together
  running = True
  click = 0
  clock=pygame.time.Clock()
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running:
    #background diner (clear/fill)
    screen.blit(diner, dinerRect)
    #intro
    fionaDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    #run part 1
    if click >= 6 and click < 11:
      fionaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 10:
      #run part 2
      fionaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 16:
      fionaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run end
    if click >= 23:
      fionaDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      print (event)
      print (show)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    

      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices': #chooses top button
        choice = 1
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices': #chooses middle button
        choice = 2
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices': #chooses bottom button
        choice = 3

      #add to click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click)
      #reset choices
      if click == 10 or click == 16:
        choice = 0
        #stop running
      if click == 27:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)


def fionaDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Fiona brings you inside the building with a huge neon sign reading, "Arctic Arcade".
  # Once you're inside you are kind of thrown off by the sheer amount of flashing lights and the sound and smell of children everywhere.
  # Fiona makes a beeline for the dining area where the smell of children is fainter. She manages to find a booth with minimal stains you and both take a seat.
  # FIONA: It's really great to see you again, Gerald!
  # GERALD: Likewise. You look very pretty today.
  # FIONA: So do you.
  # GERALD: Haha, thanks.
  # A waitress makes her way over to your table and asks for your orders. Fiona and you both decide to share a large bucket of fried chicken and 2 fountain drinks.
  # WAITRESS: Coming right up! The waitress winks at Fiona when she thinks you aren't looking, but you are.
  # Fiona just rolls her eyes.
  # The waitress walks away, but her eyes linger on Fiona for just a second longer than they need to.
  # GERALD: Do you know her?
  # FIONA: Yeah, she's actually my best friend. She knows I'm on a date so she's just trying to embarrass me.
  # Ah, that makes sense.
  # GERALD: So is that how you found this place? Because your friend works here?
  # FIONA: No, actually I used to work here too, but I quit when I went to university. That's how I met her.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Fiona brings you inside a building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "Once you're inside you are kind of thrown off by the sheer amount of flashing lights and the sound and smell of children everywhere."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 6
    mood = 'narrator'
    dialogue = "Fiona makes a beeline for the dining area where the smell of children is fainter. She manages to find a booth with minimal stains and you both take a seat."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: It's really great to see you again, Gerald!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise. You look very pretty today."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 0
    mood = 'normal'
    dialogue = "Fiona: So do you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Haha, thanks"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 6
    mood = 'narrator'
    dialogue = "A waitress makes her way over to your table and asks for your orders. Fiona and you both decide to share a large bucket of fried chicken and 2 fountain drinks."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Coming right up!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress winks at Fiona when she thinks you aren't looking, but you are. Fiona just rolls her eyes."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress walks away, but her eyes linger on Fiona for just a second longer than they need to."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11: 
    speaker = 0
    mood = 'normal'
    dialogue = "You: Do you know her?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12: #EMbARRASSED FIONA ICON
    speaker = 4
    mood = 'confused'
    dialogue = "Fiona: Year, she's actually my best friend. She knows I'm on a date so she's just trying to embarrass me."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "Ah, that makes sense."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 0
    mood = 'normal'
    dialogue = "You: So is that how you found this place? Because your friend works here?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def fionaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # The waitress returns with your food and before she leaves, she pats Fiona on the head and wishes her good luck. It's kind of nice?
  # FIONA: Would you ever consider dying your hair?
  # How will you respond?
    # [No, What?, Maybe]
  if click == 15:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: No, actually I used to work here too, but I quit when I went to university. That's how I met her."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress returns with your food and before she leaves, she pats Fiona on the head and wishes her good luck. It's kind of nice?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: Would you ever consider dying your hair?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['No', 'What?', 'Maybe']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1: No (makes Fiona sad)
    # GERALD: No, not really.
    # FIONA: Really? Why not?
    # Well this is an awkward one...
    # GERALD: I'm bald?
    # FIONA: Oh... I couldn't tell with the hat, sorry.      #EMBARRASSED FIONA ICOn
    # GERALD: Haha, don't worry about it. It was an honest mistake.
    if click == 18:
      speaker = 1
      mood = 'confused'
      dialogue = "You: No, not really."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Fiona: Really? Why not?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 6
      mood = 'narrator'
      dialogue = "Well this is an awkward one..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: I'm bald?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6 #EMBARRASSED FIONA ICON
      mood = 'normal'
      dialogue = "Fiona: Oh... I couldn't tell with the hat, sorry."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Haha, don't worry about it. It was an honest mistake."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: What? (makes Fiona confused)
    # GERALD: What?
    # FIONA: I asked if you would ever consider dying your hair.
    # GERALD: No, I heard you the first time... It's just that I'm bald?
    # FIONA: Oh... Sorry, my bad. #EMBARRASSED FIONA ICON
    # GERALD: No problem. Honest mistake.
    # At least now you know that the hat works.
    if click == 18:
      speaker = 1
      mood = 'confused'
      dialogue = "You: What?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Fiona: I asked if you would ever consider dying your hair."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: No, I head you the first time... It's just that I'm bald?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: #EMBARRASSED FIONA ICON
      speaker = 6
      mood = 'confused'
      dialogue = "Fiona: Oh shoot! Sorry, my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: No problem. Honest mistake."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "At least now you know the hat works."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Maybe (makes Fiona happy)
    # GERALD: Uh, maybe?
    # FIONA: Really? What colour?
    # GERALD: Well, before any of that I would have to grow some hair first.
    # FIONA: Oh, sorry I just figured you had hair under the hat...
    # GERALD: Nope, but maybe one day.
    # Fiona apologizes again and you assure her that you're not upset. At least now you know that the hat works as intended.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Uh, maybe?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: Really? What colour?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Well, before any of that I would have to grow some hair first..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: #EMBARRASSED FIONA ICON
      speaker = 6
      mood = 'confused'
      dialogue = "Fiona: Oh, sorry. I just figured that you had hair under the hat..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Nope, but maybe one day."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "Fiona apologized again and you assure her that you're not upset. At least now you know that the hat works as intended."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def fionaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # Fiona tells you she's full and lets you take the last piece of chicken. You take it without being told twice.
  # Fiona's friend, the waitress, returns with the bill and asks how it's going so far. Fiona just shoos her away playfully.
  # You split the bill and follow Fiona to the noisier part of the arcade with all of the games and flashing lights. Fiona turns to face you. 
  # She has to lean in a bit to be heard over all of the noise.
  # FIONA: So where to?
    # [Bird Simulator, Pool, Wheel of Fortune]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Fiona tells you she's full and lets you take the last piece of chicken. You take it without needing to be told twice."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 6
    mood = 'narrator'
    dialogue = "Fiona's friend, the waitress, returns with the bill and asks how it's going so far. Fiona just shoos her away playfully."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'narrator'
    dialogue = "You split the bill and follow Fiona to the noisier part of the arcade with all of the games and flashing lights Fiona turns to face you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "She has to lean in a bit to be heard over all of the noise."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Fiona: So where to?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "Which station will you choose for Fiona?"
      choice_List = ['Bird Simulator', 'Pool', 'Wheel of Fortune']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Bird simulator (makes Fiona sad)
    # GERALD: I saw a bird simulator station over there.
    # FIONA: Ugh, please no birds.
    # GERALD: Oh yeah, my bad I forgot about that.
    # FIONA: There's a new Wheel of Fortune station I haven't tried yet that sounds fun.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I saw a bird simulator station over there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Fiona: Ugh, please no birds."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Oh yea, my bad, I forgot you don't like birds."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: There's a new Wheel of Fortune station I haven't tried yet that sounds fun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Pool (makes Fiona confused)
    # GERALD: How about the pool?
    # FIONA: Pool? I don't think arcades really have those...
    # GERALD: Oh. Well I guess you can choose then.
    # FIONA: They got a new Wheel of Fortune station that seems fun.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: How about the pool?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Fiona: Pool? I don't think arcades really have those..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh. Well, I guess you can choose then."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: I heard they got a new Wheel of Fortune station that seems fun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Wheel of Fortune (makes Fiona happy)
    # GERALD: That Wheel of Fortune station over there seems fun.
    # FIONA: I couldn't agree more! It's new too. I've been dying to try it.
    # GERALD: Sounds good.
    # The machine does look very new and bright in comparison to the other stations, which actually says a lot because almost everything here is neon
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: That Wheel of Fortune station over there seems fun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Fiona: I couldn't agree more! It's new too. I've been dying to try it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Sounds good."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 6
      mood = 'narrator'
      dialogue = "The machine does look very new and bright in comparison to the others stations, which actually says a lot because almost everything here is neon and bright."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # You both go to the Wheel of Fortune station and Fiona seems very excited to try it out.
  # And rightfully so. As you watch, you realize that she's an actual monster at this game. 
  # She wins easily and happily takes the tickets that she won from the machine. There's a lot of them.
  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both fo the Wheel of Fortune station and Fiona seems very excited to try it out."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Wow, and rightfully so. As you watch, you realize that she's an actual monster at this game."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "She wins easily and happily takes the tickets that she won from the machine. There are a lot of them."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def fionaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # You congratulate Fiona and offer to hold her tickets for her, but she refuses and tells you that it's your turn to play something.
  # Fiona suggests a game called "CLOUDY WITH A SIDE OF APPLES". Not the most creative name, but it gets the message across.
  # GERALD: Alright, prepare to witness superhuman gaming!
  if click == 36:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You congratulate Fiona and offer to hold her tickets for her, but she refuses and tells you that it's your turn to play something."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "Fiona suggests a game called 'CLOUDY WITH A CHANCE OF APPLES'. The name feels a bit derivative of an animated movie, but other than that it seems cool."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def fionaDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
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



def fionaDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
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
    fionaDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      fionaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      fionaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      fionaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = fionaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      fionaDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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


def fionaDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  running = True
  click = 0
  #load background image
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  fiona_final = pygame.image.load("fiona_final_40.png")
  #load polaroid
  fiona_finalRect = fiona_final.get_rect()
  fiona_finalRect = fiona_finalRect.move(370, 50)
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running:
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "Fiona seemed really excited to show you a surprise."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "Rightfully so because this is beautiful."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "You walk slowly next to Fiona, who is admiring the stars."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "She brings you to the top of the hill and reaches into her purse to pull out a blanket."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "She places it on the ground and takes a seat. She wraps her arms around her legs and sits staring at the night sky. You copy what she’s doing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "She asks you what you think about the place."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "You tell her honestly that it’s breathtaking and you’re very glad that she shared it with you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "She smiles and tells you that her parents took her here on picnics as a kid. Sometimes when she would feel homesick after moving out and going to college, she would come here just to feel more connected with her parents because they moved to Iceland for retirement."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "She said that she normally doesn’t share this place with anybody, but she wanted to show you because she thought you would appreciate it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "And you do."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "She asks you about your childhood."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "You tell her about your family dog, Chichi who passed away when you were 17."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "She rubs your back to comfort you as you tell her about it. Fiona is such a kind person."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "You tell her about your childhood best friend who you haven’t spoken to since you graduated from high school."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "You tell her about your parents working a lot to keep the family afloat, but you wished they spent more time with you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "You tell her about your insecurities from a young age."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "You keep talking because you feel very comfortable with Fiona and she’s a great listener."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "But after a while, you find yourself wanting to learn more about her."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "You ask her why she hates birds."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "She sighs. You tell her that she isn’t obligated to tell you if she doesn’t want to, but she raises her hand to silence you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "Apparently, she had a pet bird as a kid, but it pecked her mother’s eye in front of her. To this day, her mother has a glass eye and the image of the incident is ingrained in her mind."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "You tell her that you’re very sorry that happened. She smiles sadly back at you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "You rub her back like she did earlier to you. It makes her smile."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "'I feel safe with you.'"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "That warms your heart. Making Fiona feel safe suddenly feels like your highest accomplishment in life. She rests her head on your shoulder and scooches closer to you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      dialogue = "Your heart starts pounding and you wonder if Fiona can hear it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      dialogue = "You slowly raise your arm and wrap it around her to place your hand on her shoulder. You sit there in a comfortable silence for a few minutes, just staring at the stars."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 27:
      dialogue = "Eventually, Fiona begins humming a tune. You don’t recognize it, but her voice is lovely."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 28:
      dialogue = "The moment feels right."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 29:
      dialogue = "You take your other hand and brush some of the hair out of her face. She looks up at you expectantly, lips still curved in a smile."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      dialogue = "You slowly lean towards her and place a soft kiss on her forehead. You close your eyes and pull back hesitantly."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31: 
      dialogue = "She smiles looking up at you and snuggles her head deeper into the crook of your neck."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      dialogue = "In this moment, you know that this is something special."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 33:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 34:
      #final polaroid
      screen.fill((0, 0, 0))
      screen.blit(fiona_final, fiona_finalRect)

      
    for event in pygame.event.get():
      print (event)
      print (show)
      print(click)
    
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click) #click counter
      if click == 35:
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(30)