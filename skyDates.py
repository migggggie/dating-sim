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
sky_happy= pygame.image.load('sky_happy.png')
sky_confused = pygame.image.load('sky_confused.png')
sky_sad = pygame.image.load('sky_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, sky_happy, sky_confused, sky_sad, nothing]


def skyDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # sky introduces himself and compliments your hat
  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Sky when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with the face of Sky themself. She looks just like his profile picture. You are relieved that they are not an escaped convict trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: You're Gerald, right? I'm Sky. Wonderful hat!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I'm Gerald and thank you. Nice to meet you, Sky."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Sky orders a medium chai latte and a plain scone. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Sky leads you to a booth in the back of the cafe away from the few other diners. You both take a seat and take a sip of your cold chocolates at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK ! you need to initiate conversation
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about his job!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def skyDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #You: So you're _____ [author, historical reenactor, electrician]
  mood = 'normal'
  prompt = "They're..."
  choice_List = ['An author', 'A historical reenactor', 'An electrician']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #An author (makes Sky happy)
    #Sky: Why yes I am. Impressive memory.
    #You: Thank you.
    #Sky tells you about some of the books she's published and you vaguely recognize some of the titles, but you can't put your finger on any of them. They tell you that if things go well, you can be a beta reader for some of his work in progresses.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're an author?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Why yes I am. Impressive memory."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Haha, thank you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #A historical reenactor (makes Sky confused)
    #Sky: What the heck gives you that idea?
    #You: Uh...nothing...
    #Sky laughs it off, but you can tell he's still kind of confused. He informs you that she is actually an author and tells you some of the books they've published. You nod along and attempt to look extremely interested.
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a historical reenactor?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Sky: What the heck gives you that impression?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
 
    if click  == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uh...nothing..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
  #An electrician? (makes sky sad)
    #Sky: My profile says that I am an author. Did you not read it?
    #You: I did, sorry, I misspoke.
    #Sky lets you off the hook, but you can tell they're disappointed. You try to appear extra attentive as she tells you about some books he's published and current work in progresses.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're an electrician?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: My profile says that I am an author. Did you not read it?."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: I did, sorry, I misspoke."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Sky tells you about some of the books she's published and you vaguely recognize some of the titles, but you can't put your finger on any of them. They tell you that if things go well, you can be a beta reader for some of his work in progresses."
    elif choice == 2:
      dialogue = "Sky laughs it off, but you can tell he's still kind of confused. He informs you that she is actually an author and tells you some of the books they've published. You nod along and attempt to look extremely interested."
    elif choice == 3:
      dialogue = "Sky lets you off the hook, but you can tell they're disappointed. You try to appear extra attentive as she tells you about some books he's published and current work in progresses."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def skyDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #The conversation about Sky's job leads him to the topic of what he looks for in an author.
  #He asks you about your favourite author
  #Sky: Who is your favourite author? Other than me, of course. I kid, I kid. [shakira, fredrik backman, no]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "The conversation about Sky's job leads him to the topic of what he looks for in an author. He asks you about your favourite author."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: Who is your favourite author? Other than me, of course. I kid, I kid."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Shakira', 'Fredrik Backman', 'No']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #Uh, that Shakira guy, I guess. (makes sky confused)
    #Sky: Are you talking about Shakespeare?
    #You: Ah, yes, that's his name
    #Sky chuckles at your mistake, but you can kind of feel him judging you. She informs you that they are a huge fan of Fredrik Backman's work. You listen to her talk about Backman's novels and writing style for quite a while. It's kind of cute how passionate he is about writing.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Uh...that Shakira guy, I guess."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Sky: Are you talking about Shakespeare?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Ah, yeah. That's his name."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #Fredrik Backman (makes Sky happy)
    #Sky: Are you for real? He's my favourite author as well!
    #You: Wow, crazy. I've been reading 'Beartown'.
    #Sky tells you that his favourite novel by Backman is 'A Man Called Ove' and you tell them you agree that it is a good book. She tells you that Beartown is a good read and anticipates that you will enjoy it.
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Fredrik Backman's works really speak to me."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Are you for real? He's my favourite author as well!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Wow, that's crazy! I've been reading 'Beartown' recently."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #I don't believe in reading (makes sky sad)
    #Sky: What does that mean?
    #You: I don't believe in it
    #Sky doesn't question you further, but she continues to tell you about their own favourite author. Some guy named Fredrik Backman. You just nod along and try to act interested so as to not hurt his feelings.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I don't believe in reading."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: What does that mean?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 2
      mood = 'sad'
      dialogue = "You: I don't believe in it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Sky chuckles at your mistake, but you can kind of feel him judging you. She informs you that they are a huge fan of Fredrik Backman's work. You listen to her talk about Backman's novels and writing style for quite a while. It's kind of cute how passionate he is about writing."
    elif choice == 2:
      dialogue = "Sky tells you that his favourite novel by Backman is 'A Man Called Ove' and you tell them you agree that it is a good book. She tells you that Beartown is a good read and anticipates that you will enjoy it."
    elif choice == 3:
      dialogue = "Sky doesn't question you further, but she continues to tell you about their own favourite author. Some guy named Fredrik Backman. You just nod along and try to act interested so as to not hurt his feelings."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def skyDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #The conversation goes fairly well after that. Sometimes Sky's vernaciluar intimidates you, but you find it fascinating to learn new words from context. At one point, after Sky says something you don't quite understand, there is an awkward silence. Sky chooses to ask you a question to fill it up.
  #Sky: What was your favourite course in high school? [nuggets, accounting, english]
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "The conversation goes fairly well after that."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "Sometimes Sky's vernaciluar intimidates you, but you find it fascinating to learn new words from context. At one point, after Sky says something you don't quite understand, there is an awkward silence. Sky chooses to ask you a question to fill it up."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: What was your favourite course in high school?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    speaker = 6
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Chicken Nuggets', "Accounting", 'English']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #Chicken nuggets (makes sky confused)
    #Sky: Huh?
    #You: Huh?
    #Sky decides to drop it. He tells you that their favourite subject in high school was English class, which is pretty straightforward for an author.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Chicken nuggets."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 4
      mood = 'confused'
      dialogue = "Sky: Huh?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Huh?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #Accounting (makes sky sad)
    #Sky: Anything math related was my worst subject in school...
    #You: Oh, that's ok...
    #Sky shakes off the frown and actually asks you why you enjoyed accounting, and he actually sounds interested. You explain, and he nods. He informs you that his favourite class in high school was actually English class, which you probably could have guessed.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I always looked forward to accounting class."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: Anything math related was my worst subject in school..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 21:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Oh...that's ok."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #English (makes sky happy)
    #Sky: Wow, that was my favourite course as well! Although, you probably could have guessed that.
    #You: Haha, I guess so.
    #You both discuss your experiences with English class. Sky definitely seems to have enjoyed it a bit more than you, but it's nice to see him so excited.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I absolutely loved English class in high school."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Wow, that was my favourite course as well! Although, you probably could have guessed that."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Haha, I guess so."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Sky decides to drop it. He tells you that their favourite subject in high school was English class, which is pretty straightforward for an author."
    elif choice == 2:
      dialogue = "You both discuss your experiences with English class. Sky definitely seems to have enjoyed it a bit more than you, but it's nice to see him so excited."
    elif choice == 3:
      dialogue = "You both discuss your experiences with English class. Sky definitely seems to have enjoyed it a bit more than you, but it's nice to see him so excited."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def skyDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
    #Sky rarely has trouble finding the words to say, so the conversation never gets dull. Admittedly, it's one of the more advanced vocubalary-filled conversations you've had in quite some time, but you enjoy it.

    #A while later
    #BYEs
    #DATE END 
  if click == 23:
    speaker = 6
    mood = 'narrator'
    dialogue = "Sky rarely has trouble finding the words to say, so the conversation never gets dull. Admittedly, it's one of the more advanced vocubalary-filled conversations you've had in quite some time, but you enjoy it."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: Well, I got to get going now, but it was really nice meeting you!"
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



def skyDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the parts together
  running = True
  click = 0
  clock=pygame.time.Clock()
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running:
    #background image (clear/fill)
    screen.blit(diner, dinerRect)
    #intro
    skyDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11: #run part 1
      skyDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 10:
      #run part 2
      skyDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 16:
      skyDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 23:
      skyDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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
      if click == 11 or click == 18:
        choice = 0
        #stop running
      if click == 27:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)



def skyDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Sky opens the door to the building with a huge neon sign reading, "Arctic Arcade".
  # The inside is just as bright as the sign outside, but it's much louder with all the games going on and kids crying and laughing.
  # You let Sky lead you to the dining area where it is much quieter and smells delicious. He picks out the booth with the least stains and you sit down with them.
  # SKY: It's lovely to see you again.
  # GERALD: Likewise. It's a nice place that you picked out. I wouldn't have thought a scholar such as yourself would like an arcade.
  # SKY: Well, I like to dabble in a bit of everything, I suppose.
  # GERALD: Impressive.
  # The waitress comes by and begins taking your order. You and Sky agree to share a cheese pizza with a side of chicken fingers.
  # WAITRESS: Coming right up! And may I just add that you two are such a cute couple!
  # Your eyes dart to Sky to see her reaction to the two of you being called a couple. It's not exactly wrong, this is a date, but it's a bit early, isn't it?
  # From just his eyes, you can see that Sky's having similar thoughts.
  # SKY: Thank you.
  # The waitress smiles, either not realizing she made things awkward, or actively choosing to ignore it.
  # Once she leaves Sky clears their throat chuckles a little bit.
  # Thankfully, Sky is always able to find the right words to say on account of her prowess in the English language.
  # Soon, both of you forget what the waitress said earlier and you listen as Sky goes on about some author you don't know with a very unfortunate last name, but you find the passion they have when speaking about literature very endearing.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Sky opens the door to the building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "The inside is just as bright as the sign outside, but it's much louder with all the games going on and kids crying and laughing. You let Sky lead you to the dining area where it is much quieter and smells delicious. He picks out the booth with the least stains and you sit down with them."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: It's lovely to see you again."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise. It's a nice place that you picked out. I wouldn't have thought a scholar such as                   yourself would like an arcade."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: Well, I like to dabble in a bit of everything, I suppose."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Impressive."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress comes by and begins taking your order. You and Sky agree to share a cheese pizza with a side of chicken fingers."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 6
    mood = 'normal'
    dialogue = "Waitress: Coming right up! And may I just add that you two are such a cute couple!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8:
    speaker = 6
    mood = 'narrator'
    dialogue = "Your eyes dart to Sky to see her reaction to the two of you being called a couple. It's not exactly wrong, this is a date, but it's a bit early, isn't it?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    speaker = 6
    mood = 'narrator'
    dialogue = "From just his eyes, you can see that Sky's having similar thoughts."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10: #EMBARRASSED SKY
    speaker = 5
    mood = 'confused'
    dialogue = "Sky: Thank you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress smiles, either not realizing she made things awkward, or actively choosing to ignore it."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    speaker = 6
    mood = 'narrator'
    dialogue = "Once she leaves Sky clears their throat chuckles a little bit."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "Thankfully, Sky is always able to find the right words to say on account of her prowess in the English language."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 6
    mood = 'narrator'
    dialogue = "Soon, both of you forget what the waitress said earlier and you listen as Sky goes on about some author you don't know with a very unfortunate last name, but you find the passion they have when speaking about literature very endearing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def skyDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # The conversation, somehow, strays away from literature and now that you can actually understand the topics you're discussing, you find yourself speaking much more.
  # SKY: Alright, well I have a question for you.
  # SKY: If you could travel to anywhere, where would you like to go?
  # [Pawnee, Indiana, Transylvania, The Bahamas]
  if click == 15:
    speaker = 6
    mood = 'narrator'
    dialogue = "The conversation, somehow, strays away from literature and now that you can actually understand the topics you're discussing, you find yourself speaking much more."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: Alright, well I have a question for you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: If you could travel to anywhere, where would you like to go?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "Where will you choose?"
      choice_List = ['Pawnee, Indiana', 'Transylvania', 'The Bahamas']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1:  Pawnee, Indiana (makes Sky confused)
    # Gerald: Definitely Pawnee, Indiana.
    # SKY: Where?
    # Gerald: Oh... it was a reference to...
    # Gerald: Never mind...
    # Noted: Stop making references to TV shows when you don't know if your audience has seen them or not.
    # Sky says she's always wanted to visit Transylvania because of the novel Dracula. He nudges your arm and says you should go together one day. They're kidding, right? It's only a second date...
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Definitely Pawnee, Indiana."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Sky: Where?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh... it was a reference to..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Nevermind..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6
      mood = 'narrator'
      dialogue = "Noted: Stop making references to TV shows when you don't know if your audience has seen them or not..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "Sky says she's always wanted to visit Transylvania because of the novel Dracule. He nudges your arm and says you should go together one day. They're kidding, right? It's only your second date..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Transylania (makes sky happy)
    # GERALD: I am going to have to go with Transylvania.
    # SKY:  A bold choice, but I am in agreement with you!
    # GERALD: Nice! A lot of people think it's a fictional place.
    # SKY: Haha, yes. I would love to see the homeland of Dracula, it's one of my favourite novels.
    # Sky and you make soft plans to visit one day. Of course, that would require the two of you being a couple, and it's not that serious yet.
    # Right?
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I am going to have to go with Transylvania."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: A bold choice, but I am in agreement with you!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Nice! A lot of people think it's a fictional place."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Haha, yes. I would love to see the homeland of Dracula, it's one of my favourite novels."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6
      mood = 'narrator'
      dialogue = "The two of you make soft plans to visit one day. Of course, that would require the two of you being a couple, and it's not that serious yet..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "Right?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: The Bahamas (makes sky sad)
    # Gerald: I love the sunny beaches in the Bahamas!
    # SKY: Hm...
    # GERALD: What's the problem?
    # SKY: Nothing, I'm just not a big fan of sunny beaches...not wanting to melt and all...
    # Oh right...that.
    # Sky tells you how they want to visit Transylvania and you eagerly agree to try to forget about your response. Sky jokes about going there together one day.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I love the sunny beaches in The Bahamas!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: Hm..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: What's the problem?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: Nothing, I'm just not a big fan of sunny beaches... not wanting to melt and all..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 1
      mood = 'confused'
      dialogue = "Oh right... that..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "Sky tells you how they want to visit Transylvania because of Dracula and you eagerly agree to try to forget about your own response. Sky jokes about going there together one day."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def skyDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
# All this talk of going on a couple's vacation has you a little bit overwhelmed and Sky is able to see it on your face.
# You finish the last slice of pizza and Sky finishes off the last of the chicken fingers.
# You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. You find that you need to raise your voice to hear yourself over all of the commotion.
# Sky looks around and then back at you.
# SKY: Where should I head to?
  # [Trivia, Animatronics, Ballpit]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "All this talk of going on a couple's vacation has you a little bit overwhelmed and Sky is able to see it on your face."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 6
    mood = 'narrator'
    dialogue = "You finish the last slice of pizza and Sky finishes off the last of the chicken fingers."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'narrator'
    dialogue = "You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. You find that you need to raise your voice to hear yourself over all of the commotion."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "Sky looks around and then back at you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Sky: Where should I head to?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['Trivia', 'Animatronics', 'Ballpit']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Trivia (makes sky happy)
    # GERALD: How about the trivia machine?
    # SKY: Where is it?
    # You point to the back of the arcade at a machine that looks like it hasn't gotten any use in ages. Apparently, people don't go to the arcade to be quizzed.
    # SKY: I like the way you think. Let's go.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: How about the trivia machine?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Where is it?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 6
      mood = 'narrator'
      dialogue = "You point to the back of the arcade at a machine that looks like it hasn't gotten any use in ages. Apparently, people dont go to the arcade to be quizzed."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: I like the way you think. Let's go!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Animatronics (makes sky sad)
    # GERALD: Maybe over to the animatronics?
    # SKY: What? They're so creepy. Besides, that's not a game.
    # GERALD: Oh...uh...
    # SKY: Let's just go to the trivia game over there.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Maybe over to the animatronics?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Sky: What? They're so creepy. Besides, that's not a game..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh...uh..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: Let's just go to the trivia game over there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Ball pit (makes sky confused)
    # GERALD: The ball pit looks fun.
    # SKY: The ball pit for children? I think we might get kicked out if we head over there without a child...
    # GERALD: Oh, yeah. You're probably right. So where to?
    # SKY: I see a trivia machine over there, let's go.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: The ball pit looks fun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Sky: The ball pit? For children? I think we might get kicked out if we head over there without a child..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, yeah... You're probably right. So where to?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Sky: I see a trivia machine over there, let's go."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # You both head over to the trivia machine and Sky wipes off a bit of dust from the screen.
  # Sky is an absolute beast at this game. How does he know everything? Did you know that the man who created the font Comic Sans only ever used it one time? Sky did.
  # A flawless round! The machine starts blasting victorious music and lights start flashing. Tickets begin flowing from the machine like a tub with a hole in it. By this rate, Sky will be able to purchase the entire arcade with her tickets.

  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both head over to the trivia machine and Sky wipes off a bit of dust from the screen."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Sky is an absolute beast at this game. How does he know everything? Did you know that the man who created the font Comic Sans only ever used it one time? Sky did."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "A flawless round! The machine starts blasting victorious music and lights start flashing. Tickets begin flowing from the machine like a tub with a hole in it. By this rate, Sky will be able to purchase the entire arcade with her tickets."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def skyDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # But now it's your turn. Sky gave you the chance to pick where they went, so you do the same.
  # Sky tells you to try your luck at a game called "CLOUDY WITH A SIDE OF APPLES". Not the most creative name, but it gets the message across.
  # GERALD: Alright, prepare to witness superhuman gaming!
  if click == 36:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "But now it's your turn. Sky gave you the chance to pick where they went, so you do the same."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "Sky tells you to try your luck at a game called 'CLOUDY WITH A CHANCE OF APPLES'. Not the most creative name, but it gets the message across."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def skyDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
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



def skyDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
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
    skyDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      skyDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      skyDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      skyDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = skyDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      skyDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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


def skyDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  running = True
  click = 0
  #load background image
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  #load polaroid
  sky_final = pygame.image.load("sky_final_40.png")
  sky_finalRect = sky_final.get_rect()
  sky_finalRect = sky_finalRect.move(370, 50)
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running:
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "Sky insisted on keeping the location a secret."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "And it was well worth the wait."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "This place is beautiful."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "The grass is ruffling as the sky above is the clearest you’ve ever seen."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "You follow Sky to the top of a hill and he lays down a blanket from his satchel."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "He lies down and you decide to do the same."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "They reach into their satchel and pull out a leather-clad book."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "She offers to read it to you and you happily agree. You always liked bedtime stories as a kid."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "Sky begins reading. You close your eyes as you listen to their voice. Admittedly, you’re not really paying that much attention to the story, you’re just enjoying the inflections and tones of Sky’s voice. It’s very soothing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "You open your eyes after a while and stare at the stars as Sky continues to read."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "Eventually, he puts the book down and tells you that the two of you can continue it next time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "Next time. You smile at the thought of next time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "You take this time to ask Sky how you should use her pronouns."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "They tell you that they don’t really care that much, but would prefer for people to use them all interchangeably and switch it up often."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "You promise that you’ll do your best."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "You ask Sky how they found this place and she smiles fondly."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "She says that he used to go on walks with their parents and he and their mother used to pick the flowers from this field."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "That’s cute."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "You realize that it’s getting pretty late. Sky spent quite a while reading to you. You feel Sky shuffling next to you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "You look down and see her hand open and palm-up, almost as an invitation."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "You look up at Sky and find that he’s already looking back at you. Your eyes lock and they nod."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "You reach down and interlock your fingers through Sky’s. They squeeze your hand reassuringly."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "You feel like you could lie here like this for years. Sky makes you feel very safe."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "Your heart is pounding and you’ve never felt this alive."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "You know that this is definitely something special."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      screen.fill((0, 0, 0))
      screen.blit(sky_final, sky_finalRect)

    #monitor events
    for event in pygame.event.get():
      print (event)
      print (show)
      print(click)

      #click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
      #stop running        
      if click == 27:
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(30)