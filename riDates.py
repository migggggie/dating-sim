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
ri_happy= pygame.image.load('ri_happy.png')
ri_confused = pygame.image.load('ri_confused.png')
ri_sad = pygame.image.load('ri_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, ri_happy, ri_confused, ri_sad, nothing]

def riDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
#You enter looking for Ri
#He introduces himself and you order + go to a booth
  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Ri when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with the face of Ri. He looks just like his profile picture. You are relieved that he is not a Nigerian prince trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: You're Gerald, right? I'm Ri. Sick hat!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Thank you. Nice to meet you, Ri."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Ri orders water and banana bread. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Ri leads you to a booth in the back of the cafe away from the few other diners. You both take a seat and take a sip of your waters at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK! Initiate conversation! Ask about his job
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about his job!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def riDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
#He's a ______ [singer, actor, dancer]
  mood = 'normal'
  prompt = "He's a..."
  choice_List = ['Singer', 'Actor', 'Dancer']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #singer (makes ri sad)
    #ri: No. My profile says that I'm a dancer. Singing is just a hobby.
    #you: Oh, my bad.
    #You make sure to ask a bunch of questions about Ri's job to make up for your mistake. His passion for dancing is enough to distract him and he's beaming just a few minutes later.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you sing for a living?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "No, my profile says that I'm a dancer. Singing is just a hobby?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: My bad..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #actor (makes ri confused)
    #ri: Uh...no? What gave you that idea?
    #gerald: Um...nothing...
    #Ri informs you that he is actually a dancer. You make sure to look really excited and impressed by that. It appears to work because Ri begins smirking once more.
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're an actor?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: No. What gives you that idea?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click  == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Um...nothing..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #dancer (makes ri happy)
    #ri: Yeah I am! It's nice that you remembered.
    #you: Of course I did!
    #Ri talks a lot about dancing, and it's no surprise that he knows a whole lot about dancing. You never realized exactly how many variations of the woah there were.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a dancer?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Yeah I am! It's nice that you remembered."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Of course I did!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
  #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "You make sure to ask a bunch of questions about Ri's job to make up for your mistake. His passion for dancing is enough to distract him and he's beaming just a few minutes later."
    elif choice == 2:
      dialogue = "Ri informs you that he is actually a dancer. You make sure to look really excited and impressed by that. It appears to work because Ri begins smirking once more."
    elif choice == 3:
      dialogue = "Ri talks a lot about dancing, and it's no surprise that he knows a whole lot about dancing. You never realized exactly how many variations of the woah there were."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def riDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #During the dance conversation, Ri takes a second to get your opinion.
  #Ri: So what's your favourite dance move? [all, hold up roof, none]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "During the dance conversation, Ri takes a second to get your opinion."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: So what's your favourite dance move?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['All of them', 'Holding up the roof', 'None']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #I love them all! I can't pick just one favourite! (makes ri happy)
    #Ri: Me too, but I've been experimenting with some new Tiktok moves that I really like.
    #Gerald: You'll have to show me some time.
    #Ri chuckles, but then his expression goes all serious. He tells you he could show you right now. You try to turn him down, but he is nothing if not persistent. He gets up from his seat and begins dancing.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I love them all! I can't pick just one favourite!."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Me too, but I've been experimenting with some new Tiktok moves that I really like."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You'll have to show me some time."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #Uhh...I guess holding up the roof? (makes ri confused)
    #Ri: Do you mean raising the roof? That ones pretty cool, but I prefer some newer moves.
    #Gerald: Oh, uh, guess you can educate me one day and show me...
    #Ri nods and tells you he could show you right now. You try to turn him down, but he tells you that you should never put off learning. He gets up from his seat and begins dancing.
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Uh...I guess holding up the roof?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: Do you mean raising the roof? That one's pretty cool, but I prefer some newer moves."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
    if click  == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: I guess you can educate me one day and show me..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #I don't dance (makes Ri sad)
    #Ri: Really? Maybe you just need to find your style.
    #Gerald: Uh, maybe? I guess you could show me some time?
    #Ri's frown fades away immediately. He gets up from his seat and tells you he can show you right now. Despite your best attempts at nicely telling him to stop, he begins dancing in the middle of the diner.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I don't dance."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Ri: Really? You probably just have to find your style..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 2
      mood = 'confused'
      dialogue = "You: Um...maybe? I guess you would be the right person to show me some time?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Ri chuckles, but then his expression goes all serious. He tells you he could show you right now. You try to turn him down, but he is nothing if not persistent. He gets up from his seat and begins dancing."
    elif choice == 2:
      dialogue = "Ri nods and tells you he could show you right now. You try to turn him down, but he tells you that you should never put off learning. He gets up from his seat and begins dancing."
    elif choice == 3:
      dialogue = "Ri's frown fades away immediately. He gets up from his seat and tells you he can show you right now. Despite your best attempts at nicely telling him to stop, he begins dancing in the middle of the diner."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def riDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #Ri is dancing in the middle of the diner. You and pretty much everyone else in the diner is staring at him. He's moving in ways you can't comprehend and you're not sure if that's a good or bad thing. Either way, this may be the most eventful first date you've ever had.
  #Ri's movements suddenly stop and he turns to you in one solid movement.
  #Ri: So how was that? [huh?, amazing, meh]
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Ri is dancing in the middle of the diner. You and pretty much everyone else in the diner is staring at him. He's moving in ways you can't comprehend and you're not sure if that's a good or bad thing. Either way, this has to be the most eventful first date you've ever had."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "Ri's movements suddenly stop and he turns to you in one swift swivel."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: So how was that?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    speaker = 6
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Huh?', "Amazing", 'Meh']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #How was what (makes ri confused)
    #Ri: The dancing???
    #You: Oh yeah. That. It was uh...pretty good?
    #To be honest, you didn't sound that convincing, but Ri seems to be satisfied with your response.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Huh? How was what?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: The dancing?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh yeah, that. It was pretty good, I guess?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  #It was amazing! (makes ri happy)
    #Ri: That's very kind of you to say! What was your favourite part?
    #You: Definitely the part where you were spinning on the ground.
    #Ri's smile is wider than you thought would ever be humanly possible. Although you would never have the confidence to break out in dance in public where dancing is typically not expected, you admire Ri's confidence.
    if click ==19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: It was amazing!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: That's very kind of you to say! What was your favourite part?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 21:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Definitely the second time you were spinning on the ground."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  #I've seen better. (makes ri sad)
    #Ri: Oh...I guess I'm still working on a few things...
    #You: I'll say...
    #Ri's expression is disappointed, but he asks you what you think he could improve on. You give him your brutally honest feedback and he seems to actually appreciate it. He even thanks you for your criticism and promises that one day he'll show you the improvement. You tell him you look forward to it.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Meh. I've seen better."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 5
      mood = 'sad'
      dialogue = "Ri: Oh...I guess I still have some stuff to work on."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 2
      mood = 'sad'
      dialogue = "You: I'll say."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "To be honest, you didn't sound that convincing, but Ri seems to be satisfied with your response."
    elif choice == 2:
      dialogue = "Ri's smile is wider than you thought would ever be humanly possible. Although you would never have the confidence to break out in dance in public where dancing is typically not expected, you admire Ri's confidence."
    elif choice == 3:
      dialogue = "Ri's expression is disappointed, but he asks you what you think he could improve on. You give him your brutally honest feedback and he seems to actually appreciate it. He even thanks you for your criticism and promises that one day he'll show you the improvement. You tell him you look forward to it."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def riDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #You talk about non-dance related topics for quite a while. You learn about Ri's family and early childhood and share stories of your own in return.
  #A while later...
  #Exchange goodbyes
  #DATE END 
  if click == 23:
    speaker = 6
    mood = 'narrator'
    dialogue = "You talk about non-dance related topics for quite a while after that. You learn about Ri's family and early childhood and you share some stories of your own in return."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: Well, I got to get going now, but it was great meeting you!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise. Talk to you later!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'normal'
    dialogue = "DATE COMPLETE!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)



#-------------------------------------------FIRST DATE
def riDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  #put all the dates together
  running = True
  click = 0
  clock=pygame.time.Clock()
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running: #run until end
  #background diner
    screen.blit(diner, dinerRect)
    #run intro
    riDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11: # run part 1
      riDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 10:
      #run part 2
      riDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      #run part 3
    if click >= 16:
      riDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run the end
    if click >= 23:
      riDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      # print (event)
      # print (show)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
    

      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices': #click on top option
        choice = 1
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices': #click on middle option
        choice = 2
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices': #click on bottom option
        choice = 3
      
      #add click count
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1 
        print(click)
      #reset choices at new parts
      if click == 10 or click == 16:
        choice = 0
      #end running
      if click == 27:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)

def riDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Ri has brought you to a building with a huge neon sign reading, "Arctic Arcade".
  # As you enter, you're struck by a million flashing lights, a cacophony of noise, and the pungent scent of children. 
  # Ri guides you over to the dining area, where it is much more chill. He seeks out a booth with the least amount of sticky residue and you both take a seat.
  # RI: It's great to see you again.
  # GERALD: Yeah, I've been looking forward to hanging out with you again.
  # RI: Same here.
  # You flip through the menus on the table for a bit.
  # A waitress makes her way over to your table and asks for your orders. Ri orders a turkey sandwich and you choose spaghetti. Both of you choose iced tea for your beverage.
  # WAITRESS: Got it! Be right back with your drinks.
  # You: Thank you.
  # You chat with Ri about the weather as you wait for your drinks.
  # WAITRESS: Your drinks.
  # She places your drinks in front of the two of you and informs you that your food will be out in a few minutes
  # You continue with the small talk until the waitress brings over your food. It looks surprisingly good.
  # You hear a little kid crying in the distance as you eat.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Ri has brought you to a building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "As you enter, you're struck by a million flashing lights, a cacophony of noise, and the pungent scent of children."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 6
    mood = 'narrator'
    dialogue = "Ri guides you over to the dining area, where it is much more chill. He seeks out a booth with the least amount of sticky residue and you both take a seat."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: It's great to see you again."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I've been looking forward to hanging out with you again."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: Same here."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 6
    mood = 'narrator'
    dialogue = "You flip through the menus on the table for a bit."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 6
    mood = 'narrator'
    dialogue = "A waitress makes her way over to your table and asks for your orders. Ri orders a turkey sandwich and you choose spaghetti. Both of you choose iced tea for your beverage."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Got it! Be right back with your drinks."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: Thank you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10:
    speaker = 6
    mood = 'narrator'
    dialogue = "You chat with Ri about the weather as you wait for your drinks."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Your drinks."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12: 
    speaker = 6
    mood = 'narrator'
    dialogue = "She places your drinks in front of the two of you and informs you that your food will be out in a few minutes"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "You continue with the small talk until the waitress brings over your food. It looks surprisingly good."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 6
    mood = 'narrator'
    dialogue = "You hear a little kid crying in the distance as you eat."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def riDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # GERALD: It's kind of noisy over there.
  # RI: Haha, yeah.
  # RI: Have you ever been to an arcade before?
  # How will you respond?
    # [Ew no, A few times, Yeah a lot!]
  if click == 15:
    speaker = 0
    mood = 'normal'
    dialogue = "You: It's knd of noisy over there."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: Haha, yeah."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: Have you ever been to an arcade before?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['Ew, no', 'A few times', 'Yeah, a lot']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Ew, no (makes Ri sad)
    # GERALD: Ew, no.
    # RI: Wow, okay. If you wanna go somewhere else, we can...
    # Nice one, genius.
    # GERALD: Oh, THIS arcade isn't ew! I LOVE this arcade
    # RI: I'm just going to choose to believe you.
    # GERALD: Good choice.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Ew, no."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Ri: Wow, okay. I mean, if you wanna go somewhere else, we can..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 6
      mood = 'narrator'
      dialogue = "Nice one, genius."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, THIS arcade isn't ew! I LOVE this arcade!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22: 
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: I'm just going to choose to believe you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I appreciate that."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: A few times (makes Ri happy)
    # GERALD: Yeah, a few times.
    # RI: Nice, and what do you think of them?
    # GERALD: They were pretty cool. None of them were as big as this one though.
    # RI: This place plays the best music. That's why I come here. 
    # GERALD: I can't believe you can even hear the music over the noise.
    # RI: I guess absence makes the heart grow fonder.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, a few times."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Nice, and what did you think of them?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 0
      mood = 'normal'
      dialogue = "You: They were pretty cool. None of them were as big as this one though."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: 
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: This place plays the best music. That's why I come here."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I can't believe you can even hear the music over the noise."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: I guess you could say absence makes the heart grow fonder."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Yeah! (Makes Ri confused)
    # GERALD: Yeah, everyday!
    # RI: Really? Everyday? That seems a bit excessive.
    # GERALD: You have your routine. I have mine.
    # RI: I suppose...
    # GERALD: This one is cool. Never been here before.
    # RI: Considering your experience, that's pretty surprising.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, everyday!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: Really? Everyday? That seems a bit excessive."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: You have your routine. I have mine."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21: 
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: I suppose..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: This one is cool. Never been here before."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Considering your experience, that's pretty surprising."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def riDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # Ri finishes his sandwich first, but he waits patiently for you to finish your spaghetti.
  # Once you're both done, Ri asks the waitress for the bill and tries to pay, but you refuse. After a bit of bickering, you agree to split it.
  # You split the bill and Ri guides you back over to all of the noise and flashing lights.
  # Ri raises his voice and half-yells.
  # RI: You choose where I should go.
    # [Trivia Station, Point randomly, Dancing game]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Ri finishes his sandwich first, but he waits patiently for you to finish your spaghetti."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 6
    mood = 'narrator'
    dialogue = "Once you're both done, Ri asks the waitress for the bill and tries to pay, but you refuse. After a bit of bickering, you agree to split it."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'narrator'
    dialogue = "You split the bill and Ri guides you back over to all of the noise and flashing lights."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "Ri raises his voice and half-yells."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Ri: You choose where I should go."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "Which station will you choose for Ri?"
      choice_List = ['Trivia Station', 'Point randomly', 'Dancing game']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Trivia Station (makes Ri sad)
    # GERALD: I think there's a trivia station in the back.
    # RI: Hm, trivia isn't exactly my strongsuit. Besides, who goes to an arcade to be quizzed?
    # GERALD: Hm, fair enough. Where do you want to go?
    # RI: Let me flex a little at the dancing station.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I think there's a trivia station in the back."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Ri: Hm, trivia isn't exactly my strongsuit. Besides, who goes to an arcade to be quizzed?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 2
      mood = 'sad'
      dialogue = "You: Hm, fair enough. Where do you want to go?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Let me flex a little at the dancing station."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Point at something (makes Ri confused)
    # You point at a random part in the arcade. It's just your luck that your finger ends up pointing at the washroom doors.
    # RI: You want me to pee?
    # GERALD: Uh, no...
    # RI: You know, I'll just go to the dance station. Let me flex.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You point at a random part of the arcade. It's just your luck that your finger ends up pointing at the washroom doors."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Ri: You want me to pee?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: You: Uh, no..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: You know, I'll just go to the dance station. Let me flex."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Dancing game (makes Ri happy)
    # GERALD: I think the dancing game over there would be your forte.
    # RI: Excellent choice!
    # RI: I guess my dancing last time really left an impression.
    # Ri winks at you and quickly turns to run to the dance station. Thankfully, he doesn't see you blushing.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I think the dancing game over there would be your forte."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: Excellent choice!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 3
      mood = 'normal'
      dialogue = "Ri: I guess my dancing last time really left an impression."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 6
      mood = 'narrator'
      dialogue = "Ri winks at you and quickly turns to run to the dance station. Thankfully, he doesn't see you blushing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # You follow Ri to the dancing station that is blasting music.
  # Ri definitely is in his element playing this game. He reaches the high score with ease and nearly doubles it. He doesn't even lose to error, he just decides to stop and hops off. 
  # The ticket slot begins to flow with tickets faster than you could even try to count them.
  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "You follow Ri to the dancing station that is blasting music."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Ri definitely is in his element playing this game. He reaches the high score with ease and nearly doubles it. He doesn't even lose to error, he just decides to stop and hops off."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "The ticket slot begins to flow with tickets faster than you can even attempt to count."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def riDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # You give Ri your congratulations on a great run. He takes a dramatic bow.
  # You ask Ri where you should go, and he points at a game called "CLOUDY WITH A CHANCE OF APPLES". Wow, what a quirky and creative name that is not at all derivative of an animated meatball movie.
  # GERALD: Alright, prepare to witness superhuman gaming!
  if click == 36:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You give Ri your congratulations on a great run. He takes a dramatic bow."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "You ask Ri where you should go, and he points at a game called 'CLOUDY WITH A CHANCE OF APPLES'. Wow, waht a quirky and creative name that is not at all derivative of an animated meatball movie."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def riDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
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



def riDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
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
    riDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      riDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      riDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      riDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = riDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      riDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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


def riDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):

  running = True
  click = 0
  #load background image
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  #load polaroid
  ri_final = pygame.image.load("ri_final_40.png")
  ri_finalRect = ri_final.get_rect()
  ri_finalRect = ri_finalRect.move(370, 50)
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running:
    #background image (clear/fill each time)
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "Ri told you he had a surprise for you. After the spontaneous dancing session in the diner last time, you’re not sure how to feel about that."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "But this."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "This is a good surprise. The grass is so soft as it blows in the wind and the yellow flowers make you feel welcomed. The sky is so pretty."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "Ri moves a lot faster than you do, but he makes sure to pause once in a while to let you catch up."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "Once you reach the top of a hill, Ri pulls a blanket out of his duffel bag."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "He beckons for you to sit with him. You do as instructed."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "Ri tells you that he found this place because he was hired to perform in a park nearby for a concert. While he was on his lunch break, he wandered around and found this hill. He says he found it beautiful before, but it’s even better here with you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "You blush."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "You tell Ri that you admire his confidence."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "Ri’s smile falters very briefly, but you pick up on it. You apologize, but aren’t quite sure for what."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "He tells you that you don’t need to apologize. It’s just that…"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "His confidence is mostly an act."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "You’re surprised by his sudden vulnerability, but you’re not about to interrupt him."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "He tells you about his early childhood. Apparently, he moved here at the age of 8. He didn’t know the language and he was extremely shy. He never had a real friend until he was forced into joining the dance club because his older sister was the president."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "He sucked at first. He was too self conscious to ever actually dance, he was just in charge of lighting and music."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "But on the night of a concert, his sister was the lead dancer, but she fell and had a concussion, so she couldn’t perform. Her understudy unfortunately, had the flu."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "Ri explains that he was the only one who knew the routine because he had helped her practice many times at home. His sister practically pushed him onto stage and he actually fell in love with dancing right then and there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "He says that he was always told to fake it until you make it, so he doesn’t like to be vulnerable around people until he trusts them."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "'I know it’s early, but I trust you.''"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "You thank him for telling you all of that."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "All of a sudden, he stands up and extends an arm out to you. You look back at him quizzically."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "He motions for you to get up and take his hand."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "You reluctantly do so. You can kind of see where this is going."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "There’s no music, but Ri starts leading you in a slow dance. He guides one of your hands to his waist. You fumble around at first, but Ri’s an exceptional leader and you surprise yourself by actually getting the hang of it very quickly."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "Once you’re confident enough to stop staring at your feet, you look up at Ri, who has been smiling softly at you this entire time. You lock eyes and you can’t help the warm flood of blood that rushes to your cheeks."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      dialogue = "Ri tightens his grip on your hand and you do the same."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      dialogue = "You think to yourself…"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 27:
      dialogue = "This is something special."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 28:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 29:
      screen.fill((0, 0, 0))
      #final polaroid
      screen.blit(ri_final, ri_finalRect)

      
    for event in pygame.event.get():
      print (event)
      print (show)
      print(click)
    
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click) #click counter
      if click == 30:
        running = False

    # Flip the display
    pygame.display.flip()
    clock.tick(30)