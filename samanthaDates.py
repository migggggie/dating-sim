#----------------------------------------------FIRST DATE
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
samantha_happy= pygame.image.load('samantha_happy.png')
samantha_confused = pygame.image.load('samantha_confused.png')
samantha_sad = pygame.image.load('samantha_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, samantha_happy, samantha_confused, samantha_sad, nothing]


def samanthaDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #samantha introduces herself and compliments your hat

  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Samantha when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with the face of Samantha herself. She looks just like her profile picture. You are relieved that she is not a 60 year old man trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: You're Gerald, right? I'm Samantha. Nice hat."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I'm Gerald and thank you. Nice to meet you, Samantha."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Samantha orders a large black coffee and a chocolate chip cookie. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha leads you to a booth in the back of the cafe away from the few other diners. You both take a seat and take a bite of your chocolate chip cookies at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK ! you need to initiate conversation
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about her job!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def samanthaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #Gerald: so you're a _________ [mother, doctor, contractor]
  mood = 'normal'
  prompt = "She's a..."
  choice_List = ['Mother', 'Doctor', 'Contractor']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  #mother? (makes samantha confused)
  #samantha: uh, no. what gives you that idea?
  #gerald: oh, nothing...just wondering
  #samantha chuckles nervously at that. You quickly ask her what she does for a living and try to act extra interested to make up for your earlier blunder. It seems to work because Samantha is smiling again quickly
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a mother?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: Uh...no? What gives you that idea?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uh...nothing I was just wondering...sorry."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #Doctor? (makes samantha sad)
    #samantha: No. My profile says I'm a contractor
    #gerald: oh, my bad
    #You ask her about her work and make sure to seem extra interested to make up for your earlier blunder. It seems to work because Samantha is smiling again quickly
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a doctor?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "Samantha: No...my profile says that I'm a contractor."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
    #Contractor? (makes samantha sad)
    #samantha: yep! What about you?
    #gerald: I'm a [insert occupation]
    #You both discuss your jobs for a while.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a contractor?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: Yes I am! Thanks for remembering."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 8:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Of course."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Samantha chuckles nervously at that. You quickly ask her what she does for a living and try to act extra interested to make up for your earlier blunder. She's a contractor. It seems to work because Samantha is smiling again quickly."
    elif choice == 2:
      dialogue = "You ask Samantha about her work and make sure to seem extra interested to make up for your earlier blunder. It seems to work because Samantha is smiling again quickly."
    elif choice == 3:
      dialogue = "You both discuss your jobs for a while. Apparently, Samantha has a very extensive knowledge of roof shingles and different latches. You manage to remember about 5% of what she says."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def samanthaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #QUICK! Initiate conversation!
  #Samantha: enough talk about work. What's your ideal vacation? [staycation, hike, don't believe]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "A certain amount of time passes before Samantha changes the subject."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: Enough work talk. What's your ideal vacation?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Staycation at home with my computer', 'Going somewhere I can hike and breathe fresh air', "I don't believe in vacations"]
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #staycation at home with my computer (makes samantha sad)
    #samantha: really? you wouldn't prefer to go outdoors? you can stay inside anytime
    #gerald: i find it relaxing
    #Samantha goes on to explain how she prefers to be outdoors. You nod along and she seems to somehow get the idea that you agree with her, even though you don't.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I would want a staycation at home with my computer."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Samantha: Really? You wouldn't prefer to go outdoors? You can stay inside anytime."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 2
      mood = 'sad'
      dialogue = "You: I find staying indoors relaxing..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #going somewhere I can hike and breathe fresh air (makes samantha happy)
    #samantha: Same! I love the outdoors! I hate being cooped up indoors all the time!
    #gerald: Yeah, my family used to go hiking in the mountains a lot.
    #The two of you enthuse over hiking for a while. You make soft plans to go together one day.
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I would definitely want to go somewhere I can hike and breathe fresh air."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: Same! I love the outdoors! I hate being cooped up indoors all the time!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, my family used to go hiking in the mountains a lot when I was younger."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  

  elif choice == 3:
    show = 'talking'
    #I don't believe in vacations (makes samantha confused)
    #Samantha: Like you've never had one or?
    #gerald: no, i just don't believe in them.
    #samantha is visibly confused, but she doesn't push it. She instead goes on to talk about her ideal vacation, ignoring the fact that you just claimed to not believe in vacations.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I don't believe in vacations."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: Uh...like you've never had one before???"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: No, I just don't believe in them."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 15:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Samantha goes on to explain how she prefers to be outdoors. You nod along and she seems to somehow get the idea that you agree with her, even though you don't."
    elif choice == 2:
      dialogue = "The two of you enthuse over hiking for a while. You make soft plans to go together one day."
    elif choice == 3:
      dialogue = "Samantha is visibly confused, but she doesn't push it. She instead goes on to talk about her ideal vacation, ignoring the fact that you just claimed to not believe in vacations."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def samanthaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #The conversation is going fairly well, but eventually, there is a lull. It's your turn to do something [joke, family, nothing]
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Samantha has managed to bring the conversation to a brand new topic and you are happy to go with it."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "The conversation is going fairly well, but eventually, there is a lull. It's your turn to do something."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 6
    mood = 'normal'
    prompt = "What will you do?"
    choice_List = ['Tell a joke', "Ask about her family", 'Do nothing']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #tell a joke (makes samantha happy)
      #gerald: What do snowpeople do in the summer? Chill out.
      #samantha: hahahahahaha
      #It's not actually that funny, but Samantha seems to like it. She has a cute laugh and you notice the way her hair catches the light and it almost looks like it's glowing.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: What do snowpeople do in the summer? They chill out."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: OMG HAHAHA!!!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #ask about her family (makes samantha confused)
    #gerald: so...you got a family?
    #samantha: i have parents, if that's what you mean...
    #Oof. That didn't go too well. You proceed to ask about her parents. She seems kind of thrown off to be asked about her parents on a first date, but she goes with it.
    if click ==18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So...you got a family?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: I mean...I have parents? If that's what you mean?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  elif choice == 3:
    show = 'talking'
    #do nothing (makes samantha sad)
    #samantha: there's nothing you want to ask me?
    #You eventually clue in and ask about her favourite restaurant. She answers in a single word, and it's some french word you don't understand. You ask her a few more questions after, and she seems to forgive you for your silence earlier.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: ..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Samantha: So there's nothing you want to ask me?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
  if click == 20:
    #narrator lines
    show = 'talking'
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "It's not actually that funny, but Samantha seems to like it. She has a cute laugh and you notice the way her hair catches the light and it almost looks like it's glowing."
    elif choice == 2:
      dialogue = "Oof. That didn't go too well. You proceed to ask about her parents. She seems kind of thrown off to be asked about her parents on a first date, but she goes with it."
    elif choice == 3:
      dialogue = "You eventually clue in and ask about favourite restaurant. Samantha answers in a single word, and it's some french word you don't understand. You ask her a few more questions after, and she seems to forgive you for your silence earlier."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def samanthaDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #Samantha: Well. It was nice meeting you!
  #You: Yeah, talk to you soon!
  #BYE
  #display date
  show = 'talking'
  if click == 21:
    speaker = 6
    mood = 'narrator'
    dialogue = "A while later..."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: Well, I got to get going now, but it was really nice meeting you!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 23:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Likewise. Talk to you soon!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 6
    mood = 'normal'
    dialogue = "DATE COMPLETE!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)

#-------------------------------------------FIRST DATE
def samanthaDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):

  running = True
  click = 0
  clock=pygame.time.Clock()
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  while running:
    #background diner
    screen.blit(diner, dinerRect)
    #intro
    samanthaDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11: # run part 1
      samanthaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 10:
      #run part 2
      samanthaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 16:
      samanthaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run ending
    if click >= 21:
      samanthaDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      print (event)
      print (show)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
      
      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices': # top button chosen
        choice = 1
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices': #middle button chosen
        choice = 2
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices': #bottom button chosen
        choice = 3
      
      #click counter
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
      #reset choice
      if click == 10 or click == 16:
        choice = 0
      #stop running
      if click == 25:
        running = False
    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)


def samanthaDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Samantha brings you to a building with a huge neon sign reading, "Arctic Arcade".
  # Once you're in, you realize that the inside is just as bright as the sign outside, but louder (and... yes, sweatier) with all the games going on and kids crying and laughing.
  # Samantha skips the games and brings you to the dining area. She manages to find a booth without sticky residue and you take residence there.
  # SAMANTHA: I was really happy to hear from you.
  # GERALD: Well, I was happy you agreed to go out again.
  # SAMANTHA: Of course, how could I resist a cutie like you?
  # GERALD: I could say the same thing.
  # A waitress interrupts you both to take your order. Samantha orders a BLT and a mango smoothie. You settle on a grilled cheese sandwich and a caramel macchiato.
  # WAITRESS: Alright. Coming right up!
  # SAMANTHA: Thank you.
  # You ask Samantha about her day and a bunch of other small talk as you wait for your food.
  # WAITRESS: Here you go!
  # The waitress places your respective meals in front of you.
  # Samantha does not hesitate to dig in. You follow suit and are very impressed with your meal.
  # SAMANTHA: You like it?
  # GERALD: Yes, very much.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha brings you to a building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "Once you're in, you realize that the inside is just as bright as the sign outside, but louder (and... yes, sweatier) with all the games going on and kids crying and laughing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha skips the games and brings you to the dining area. She manages to find a booth without sticky residue and you take residence there."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: I was really happy to hear from you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Well, I was happy you agreed to go out again."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 0
    mood = 'normal'
    dialogue = "Samantha: Of course! How could I resist a cutie like you?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 0
    mood = 'normal'
    dialogue = "You: I could say the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 6
    mood = 'narrator'
    dialogue = "A waitress interrupts you both to take your order. Samantha orders a BLT and a mango smoothie. You settle on a grilled cheese sandwich and a caramel macchiato."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Alright. Coming right up!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: Thank you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10:
    speaker = 6
    mood = 'narrator'
    dialogue = "You ask Samantha about her day and a bunch of other small talk as you wait for your food."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11: #WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Here you go!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress places your respective meals in front of you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha does not hesitate to dig in. You follow suit and are very impressed with your meal."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: You like it?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def samanthaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # SAMANTHA: Me too.
  # SAMANTHA: If you could only eat one food for the rest of your life, what would it be?
  # How will you respond?
  # [Sushi, Pizza, Broccoli]
  if click == 15:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yes, very much."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: Same here!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: If you could only eat one food for the rest of your life, what would it be?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['Sushi', 'Pizza', 'Broccoli']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1:  Sushi (makes Samantha happy)
    # GERALD: Definitely sushi.
    # SAMANTHA: Ooh, nice choice. Honestly, I would probably choose the same thing.
    # SAMANTHA: We should go to a sushi buffet next time!
    # Next time. The idea of a next time makes you smile just a bit.
    # GERALD: Definitely.
    # SAMANTHA: It's a date.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Sushi 100%."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: Ooh, nice choice! Honestly, I would probably choose the same thing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: We should go to a sushi buffet next time!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 6
      mood = 'narrator'
      dialogue = "Next time. The idea of a next time makes you smile just a bit."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Definitely."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: It's a date."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Pizza (makes Samantha sad)
    # GERALD: Ooh, probably pizza.
    # SAMANTHA: Really? It's so greasy and salty though.
    # She's eating a BLT at the moment. Not the healthiest choice either, but ok.
    # SAMANTHA: I mean, it's nice sometimes. But for every single meal, I don't think I could deal with that.
    # GERALD: You may have a point. I still like it though.
    # Samantha tells you that she would choose sushi and you agree with her that it's a good pick despite the fact that you are still loyal to pizza.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Ooh, probably pizza."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Samantha: Really? It's so greasy and salty..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 6
      mood = 'narrator'
      dialogue = "She's eating a BLT at the moment. Not the healthiest choice either, but ok."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: I mean, it's nice sometimes. But for every single meal, I don't think I could deal with that."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You may have a point. I still like it though."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "Samantha tells you that she would choose sushi and you agree with her that it's a good pick despite the fact that you are still loyal to pizza."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Broccoli (makes Samantha confused)
    # GERALD: Broccoli.
    # SAMANTHA: Really? I mean, I'm all for eating healthy, but just broccoli?
    # GERALD: ...Yes.
    # Okay but really? Just broccoli? You do you, I guess.
    # SAMANTHA: Well, that's cool... I would pick sushi.
    # That is also a good pick.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Broccoli."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: Really? I mean, I'm all for eating healthy, but just broccoli?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: ...Yes"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 6
      mood = 'narrator'
      dialogue = "Okay, but really? Just broccoli? You do you, I guess."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: Well, that's cool... I would pick sushi."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "That is also a good pick."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def samanthaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # Samantha finishes off her burger and waits for you to eat the last of your sandwich.
  # SAMANTHA: You ready to play some games?
  # GERALD: Always.
  # You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. Samantha leans it to be heard over all of the noise to ask you a question.
  # SAMANTHA: Where should I go?
    # [???, Hunting, Basketball]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Samantha finishes off her burger and waits for you to eat the last of your sandwich."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: You  ready to play some games?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Always."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. Samantha leans in to be heard over all the noise to ask you a question."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Samantha: Where should I go?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['???', 'Hunting', 'Basketball']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: ??? (makes Samantha confused)
    # GERALD: Wait, you're leaving???
    # SAMANTHA: No... I just meant which game should I go to first...
    # GERALD: Oh... my bad.
    # Samantha suggests the hunting simulator and you follow her there.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Wait, you're leaving???"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Samantha: No... I just meant which game should I go to first..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Oh...my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 6
      mood = 'narrator'
      dialogue = "Samantha suggests the hunting simulator and you follow her there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Hunting (makes Samantha happy)
    # GERALD: The hunting simulator seems pretty cool.
    # SAMANTHA: Ooh, yes! Let's go!
    # GERALD: You hunt a lot?
    # SAMANTHA: Not in real life, but I like any game with nature in it.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: The hunting simulator seems pretty cool."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: Ooh, yes! Let's go!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You hunt a lot?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Samantha: Not in real life, but I like any game with nature in it!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Basketball (makes Samantha sad)
    # GERALD: How about basketball?
    # SAMANTHA: I kind of suck at basketball. I'm better with a gun.
    # GERALD: Oh, in that case maybe the hunting simulator?
    # Samantha nods, informing you that you have made a good decision. Well, second decision.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: How about basketball?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Samantha: I kind of suck at basketball. I'm much better with a gun."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, in that case maybe the hunting simulator?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 6
      mood = 'narrator'
      dialogue = "Samantha nods, informing you that you ahve made a good decision. Well, second decision."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # You both head over to the hunting simulator, which is more gruesome than you would have expected considering the place is filled with kids. There's a headless deer and a man in plaid holding the headless deer up like a trophy. Interesting.
  # Samantha is insane at this game. Someone get her signed because she's hitting headshots like nobody's business.
  # Samantha actually sets a new high score. The machine plays a little tune and begins spewing out tickets for what feels like years.
  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both head over to the hunting simulator, which is more gruesome than you would have expected considering the place is filled with kids. There's a headless deer and a man in plaid holding the headless deer up like a trophy. Interesting."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha is insane at this game. Someone get her signed because she's hitting headshots like nobody's business."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "Samantha actually sets a new high score. The machine plays a little tune and begins spewing out tickets for what feels like years."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def samanthaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # GERALD: Very impressive. Where should I go?
  # Samantha looks around and points to a machine with a big title reading, "CLOUDY WITH A SIDE OF APPLES". Not the most creative name, but it gets the message across.
  # GERALD: Alright, prepare to witness superhuman gaming!
  if click == 36:
    speaker = 0
    show = 'talking'
    mood= 'normal'
    dialogue = "You: Wow, very impressive! Where should I go?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "Samantha looks around and points to a machine with a big title reading, 'CLOUDY WITH A CHANCE OF APPLES'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def samanthaDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
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



def samanthaDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
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
    samanthaDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      samanthaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      samanthaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      samanthaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = samanthaDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      samanthaDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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


def samanthaDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  running = True
  click = 0
  #load background image
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  #load polaroid
  samantha_final = pygame.image.load("samantha_final_40.png")
  samantha_finalRect = samantha_final.get_rect()
  samantha_finalRect = samantha_finalRect.move(370, 50)
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running:
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "Samantha is the one who picks you up from your place this time. She tells you she has somewhere in mind that she thinks you’ll love."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "And she was right."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "This is amazing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "The night sky is gorgeous. It contrasts with Samantha’s hair beautifully."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "She skips ahead of you as you try to speed walk to keep up with her."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "Once you reach the top of the hill, you find that Samantha has already laid a blanket down on the grass and is lying on her back on top of it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "You decide to follow suit and lie down next to her."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "Samantha asks what you think of the place. You have no choice but to gush over it. In your peripheral vision, you can see that she is nodding in agreement."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "You ask her how she found it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "She says that her grandmother took her to the forest next door which is why she fell in love with the outdoors. Her grandmother encouraged her to become whatever she wanted to when her parents were pressuring her to go into more female-dominated jobs."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "You tell her that her grandmother sounds like a great lady."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "She tells you that she was."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "The mood today is drastically different than last time, but it’s not unwelcome."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "Abruptly, Samantha asks you what you think of her."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "You tell her you think she’s beautiful. She smiles, but it doesn’t quite meet her eyes."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "You ask her what’s wrong."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "She explains that people always jump to her appearance. She appreciates the compliment, but she wishes that people would notice her for her mind. It’s hard to be taken seriously when everyone thinks you’re just a head of hair."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "You nod along. That makes sense."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "You tell her that you think she’s very intelligent and strong."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "That makes her smile. You know that she just said she doesn’t want people always talking about her appearance, but you can’t help but notice how pretty she looks right now."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "“You’re not too bad yourself”"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "You feel her shuffle on the blanket."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "She sits up and looks down at you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "You look back at her and your eyes lock."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "Her smile is still there, but something about her expression seems much more serious now. Not upset, but her gaze is filled with intent."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      dialogue = "It makes your heart pound."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      dialogue = "You watch as she slowly lowers her body."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 27:
      dialogue = "Your heart is going nuts right now."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 28:
      dialogue = "She presses a soft kiss to your cheek. You close your eyes."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 29:
      dialogue = "As she pulls back, you feel her fingers brushing where her lips were. Presumably to wipe off lipstick residue. She giggles and so do you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      dialogue = "You can already tell that this is something special"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      #final polaroid
      screen.fill((0, 0, 0))
      screen.blit(samantha_final, samantha_finalRect)

      
    for event in pygame.event.get():
      print (event)
      print (show)
      print(click)
    
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click) #click counter
      if click == 33:
        running = False

    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)