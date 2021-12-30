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
blake_happy= pygame.image.load('blake_happy.png')
blake_confused = pygame.image.load('blake_confused.png')
blake_sad = pygame.image.load('blake_sad.png')
nothing = pygame.image.load('nothing.png')
speaker_List = [gerald_happy, gerald_emb, gerald_sad, blake_happy, blake_confused, blake_sad, nothing]

def blakeDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #-------------------------------------------FIRST DATE

  # blake introduces themself and compliments your hat

  #you order your food/drinks and find a booth near the back and sit down

  if click == 0:
    speaker = 6
    mood = 'narrator'
    dialogue = "You enter the cafe and look around. It's not too busy. You're looking for Blake when you feel a tap on your shoulder. You're frightened very briefly, but when you turn around, you are met with the face of Blake. They look just like their profile picture. You are relieved that they are not a 60 year old perv trying to scam you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: You're Gerald, right? I'm Blake. Cool hat."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, I'm Gerald and thank you. Nice to meet you, Blake."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #you order your food/drinks and find a booth near the back and sit down
  if click == 3:
    speaker = 6
    mood = 'narrator'
    dialogue = "You both walk up to the barista and order your food and drinks. Everything smells so good that you have trouble deciding what to get. Blake orders a strawberry milkshake and a strawberry scone. You decide to get the same thing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake leads you to a booth in the back of the cafe away from the few other diners. You both take a seat and lick off some whipped cream from your straws at the same time."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  #QUICK ! you need to initiate conversation
  if click == 5:
    speaker = 6
    mood = 'narrator'
    dialogue = "QUICK! Initiate conversation! Ask about their job!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  
def blakeDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #Gerald: So you're a _______ [teacher, streamer, clown]
  mood = 'normal'
  prompt = "They're a..."
  choice_List = ['Teacher', 'Streamer', 'Clown']
  show = 'choices'
  if choice == 0:
    drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #teacher? (makes blake sad)
    #blake: No, my profile says that I'm a Twitch Streamer
    #gerald: oh, my bad.
    #In an attempt to make up for that blunder, you ask Blake countless questions about their work, and it seems to work because they are smiling a few minutes later.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a teacher??"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: No. My profile says that I'm a streamer."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh...my bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #streamer? (makes blake happy)
    #blake: Yeah, how about you?
    #gerald: i'm a [insert occupation]
    #You both talk about your jobs and exchange stories. Admittedly, Blake's stories are more interesting than yours because of the sheer weirdness of people on the internet.
    if click ==6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a streamer?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: Yeah I am! It's cool that you remembered."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 8:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, of course I did."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  

  elif choice == 3:
    show = 'talking'
    #clown? (makes blake confused)
    #blake: excuse me?
    #gerald: oh, uh, nevermind
    #Blake informs you that they are a Twitch Streamer and you nod along, trying your best to recover from your blunder just now.
    if click == 6:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So you're a clown?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 7:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: Um, excuse me?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 8:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Uhhh...nevermind. Sorry."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "In an attempt to make up for that blunder, you ask Blake countless questions about their work, and it seems to work because they are smiling a few minutes later."
    elif choice == 2:
      dialogue = "You both talk about your jobs and exchange stories. Admittedly, Blake's stories are more interesting than yours because of the sheer weirdness of people on the internet."
    elif choice == 3:
      dialogue = "Blake informs you that they are a Twitch Streamer and you nod along, trying your best to recover from your blunder just now."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def blakeDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #Blake: So what is your entertainment platform of preference? [twitch, tiktok, myspace]
  if click == 10:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You both chat for a while about work before Blake asks you a question."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: So what is your entertainment platform of preference?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    mood = 'normal'
    prompt = "How will you respond?"
    choice_List = ['Twitch', 'Tiktok', 'MySpace']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
    #Twitch (makes blake happy)
    #blake: Really? You can be honest!
    #gerald: No, I'm serious. It's my favourite
    #You both exchange your favourite Twitch streamers. You learn that Blake follows over 300 twitch channels. Woah. 
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I watch TONS of Twitch content."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: Really? You can be honest with me, you don't have to pretend."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      speaker = 0
      mood = 'normal'
      dialogue = "You: No, I'm serious. It's my favourite!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #Tiktok (makes blake sad)
    #blake: Hm...I prefer Twitch.
    #gerald: I mean, Twitch is nice too
    #You try to defend your stance, and Blake listens without interrupting. They explain their viewpoint. It's a very civil conversation, and the two of you forget the conflict quickly.
    if click ==12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I spend a lot of late nights on Tiktok."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: Hm...I prefer Twitch."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
    if click  == 14:
      speaker = 1
      mood = 'confused'
      dialogue = "You: I mean, Twitch is nice too!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  

  elif choice == 3:
    show = 'talking'
    #MySpace (makes blake confused)
    #blake: What's that?
    #gerald: ...nevermind
    #Blake asks you to explain what MySpace is, but you don't want to sound old so you just avoid the question. Blake gets the hint and moves on with a new topic.
    if click == 12:
      speaker = 0
      mood = 'normal'
      dialogue = "You: I spend a lot of time perfecting my MySpace page."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 13:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: Uh, what's that???"
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
      dialogue = "You both exchange your favourite Twitch streamers. You learn that Blake follows over 300 twitch channels. Woah. Apparently, when they're not streaming on their own channel, they are modding for some online friends."
    elif choice == 2:
      dialogue = "You try to defend your stance, and Blake listens without interrupting. They explain their viewpoint. It's a very civil conversation, and the two of you forget the conflict quickly, instead opting to make fun of drama going on on the internet at the moment."
    elif choice == 3:
      dialogue = "Blake asks you to explain what MySpace is, but you don't want to sound old so you just avoid the question entirely. Blake gets the hint and moves on with a new topic by asking you what you think of 'the James Charles situation'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def blakeDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  #The conversation comes to a pause. Awkward
  #You should ask Blake a question! [twitch, video games, string theory]
  if click == 16:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You realize that Blake is a pretty cool snowperson."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 6
    mood= 'narrator'
    dialogue = "The conversation spans many topics, several of which, are related to pop culture."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 18:
    speaker = 6
    mood = 'narrator'
    dialogue = "However, as is natural, there is an awkward silence. You should do something!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 19:
    speaker = 6
    mood = 'normal'
    prompt = "What will you do?"
    choice_List = ['Ask about Twitch', "Ask about video games", 'Ask about string theory']
    show = 'choices'
    if choice == 0:
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'

    #Ask about Twitch - idk smth abt money? (makes blake sad)
    #blake: wow, just because i'm a streamer you think you can ask how much money i make on a first date?
    #gerald: that's not what i meant! I'm just curious about streamers!
    #Blake digests that for a minute. They eventually just shrug and change the subject. Oof.
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So how much money do Twitch Streamers make?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: Wow, just because I'm a streamer you think it's appropriate to ask how much money I make on a first date?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: that's not what I meant! I misworded that. I'm just curious about all streamers in general..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
    #Ask about video games (makes blake happy)
    #blake: I love video games! I've been playing a lot of Rhythm Doctor lately!
    #gerald: Same, it's so much fun!
    #You both share a few more games you enjoy playing and make soft plans to play 'It Takes Two' together.

    if click ==19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You like video games?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: I LOVE Video games! I've been playing a lot of Rhythm Doctor on stream lately! I've also been playing Apex with my friends recently."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click  == 21:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Same! It's so much fun!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)

  elif choice == 3:
    show = 'talking'
    #Ask about string theory (makes blake confused)
    #Blake: Uhhh...what?
    #gerald: Oh, uh, nevermind.
    #Blake apologizes and tells you that they didn't go to college in favour of streaming. You assure them that you don't care about that and try your best to change the subject
    if click == 19:
      speaker = 0
      mood = 'normal'
      dialogue = "You: So what are your thoughts on string theory?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 20:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: Um...what's that?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)  
    if click == 21:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh...uh...nevermind."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 22:
    #narrator lines
    speaker = 6
    mood = 'narrator'
    if choice == 1:
      dialogue = "Blake digests that for a minute. They eventually just shrug and change the subject. Oof."
    elif choice == 2:
      dialogue = "You both share a few more games you enjoy playing and make soft plans to play 'It Takes Two' together and exchange Steam accounts."
    elif choice == 3:
      dialogue = "Blake apologizes and tells you that they didn't go to college in favour of streaming. You assure them that you don't care about that and try your best to change the subject."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker) 
  return show

def blakeDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  #Blake: Well. It was nice meeting you!
  #You learn that Blake is a pretty cool person.
  #Blake: Well, it was nice meeting you!
  #Gerald: Likewise! Talk to you soon!
  #BYE
  #display date
  if click == 23:
    speaker = 6
    mood = 'narrator'
    dialogue = "A while later..."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 24:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: Well, I got to get going now, but it was really nice meeting you!"
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
def blakeDate_1 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  # put all parts together
  running = True
  click = 0
  diner = pygame.image.load("diner_1280x720.png")
  dinerRect = diner.get_rect()
  clock = pygame.time.Clock()
  while running:
    #background diner (clear/fill)
    screen.blit(diner, dinerRect)
    #intro
    blakeDate_1_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 6 and click < 11: # run part 1
      blakeDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_1_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 10:
      #run part 2
      blakeDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_1_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 16:
      blakeDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_1_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 23:
      blakeDate_1_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

    #monitor events
    for event in pygame.event.get():
      # print (event)
      # print (show)
      pos = pygame.mouse.get_pos()
      butt = pygame.mouse.get_pressed()
      mx = pos[0]
      my = pos[1]
      
      if mx>101 and mx<1179 and my>581 and my<614 and butt[0]== 1 and show == 'choices': #user clicked top option
        choice = 1
      elif mx>101 and mx<1179 and my>621 and my<654 and butt[0]==1 and show == 'choices': #user clicked middle option
        choice = 2
      elif mx>101 and mx<1179 and my>661 and my<694 and butt[0]==1 and show == 'choices': #user clicked bottom option
        choice = 3
      #click counter
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


def blakeDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
  # Blake opens the door for you and you both enter the building with a huge neon sign reading, "Arctic Arcade".
  # The inside is just as bright as the sign outside, but it's much louder (and kind of smellier) with all the games going on and kids crying and laughing.
  # Blake guides you over to the dining area which, thankfully, smells much better. They inspect each of the booths and only one of them isn't sticky. You both sit down there.
  # BLAKE: It was really nice to hear from you.
  # GERALD: Yeah, of course. So, am I correct in assuming you come here often?
  # BLAKE: Yep. One time the wifi in my place went out so I spent, like, a week here. Good times.
  # GERALD: A gamer's gotta do what a gamer's gotta do, I suppose.
  # The waitress comes to your table to take your order. Blake gets a vegan burger and a strawberry milkshake. You order a personal cheese pizza and some pop.
  # WAITRESS: Wait... You're that Twitch streamer who got pasta stuck in their nose on stream!
  # You are a bit confused so you look over to Blake, who has turned a few shades redder. You figure that means it's true.
  # Blake purses their lips into a tight smile and nods at the waitress.
  # WAITRESS: Oh my god! Do you mind if we get a picture together?
  # Before Blake can even respond, the waitress has shoved her phone into your hand and taken a seat next to Blake. Apparently, you're the photographer. You take a few pictures of the two of them and hand her phone back.
  # She winks once at Blake and heads to the kitchen. 
  # GERALD: So you definitely have to tell me the story about the pasta.
  if click == 0: #OUTSIDE
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake opens the door for you and you both enter the building with a huge neon sign reading, 'Arctic Arcade'."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 1:
    speaker = 6
    mood = 'narrator'
    dialogue = "The inside is just as bright as the sign outside, but it's much louder (and kind of smellier) with all the games going on and kids crying and laughing."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 2: #KITCHEN
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake guides you over to the dining area which, thankfully, smells much better. They inspect each of the booths and only one of them isn't sticky. You both sit down there."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 3:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: It was really nice to hear from you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 4:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Yeah, of course. So, am I correct in assuming you come here often?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 5:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: Yep. One time the wifi in my place went out so I spent, like, a week here. Good times."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 6:
    speaker = 0
    mood = 'normal'
    dialogue = "You: A gamer's gotta do what a gamer's gotta do, I suppose."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 7:
    speaker = 6
    mood = 'narrator'
    dialogue = "The waitress comes to your table to take your order. Blake gets a vegan burger and a strawberry milkshake. You order a personal cheese pizza and some pop."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 8: #INSERT WAITRESS ICON
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Wait... You're that Twitch streamer who got pasta stuck in their nose on stream!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 9:
    speaker = 6
    mood = 'narrator'
    dialogue = "You are a bit confused so you look over to Blake, who has turned a few shades redder. You figure that means it's true."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 10: #EMBARRASSED BLAKE
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake purses their lips into a tight smile and nods at the waitress."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 11: #WAITRESS ICon
    speaker = 6
    mood = 'narrator'
    dialogue = "Waitress: Oh my god! Do you mind if we get a picture together?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 12:
    speaker = 6
    mood = 'narrator'
    dialogue = "Before Blake can even respond, the waitress has shoved her phone into your hand and taken a seat next to Blake. Apparently, you're the photographer. You take a few pictures of the two of them and hand her phone back."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 13:
    speaker = 6
    mood = 'narrator'
    dialogue = "She winks once at Blake and heads to the kitchen."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 14:
    speaker = 0
    mood = 'normal'
    dialogue = "You: So you definitely have to tell me the story about the pasta."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)


def blakeDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
  # Blake chuckles and tells you they will tell you all about it another time, but would prefer not to right before eating. Understandable.
  # After the waitress brings over your food, you both talk while you eat. You are pleasantly surprised by the food.
  # BLAKE: Hey, do you mind if I vlog this?
  # How will you respond?
    # [Vlog?, Why?, No problem]
  if click == 15:
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake chuckles and tells you they will tell you all about it another time, but would prefer not to right before eating. Understandable."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 16:
    speaker = 6
    mood = 'narrator'
    dialogue = "After the waitress brings over your food, you both talk while you eat. You are pleasantly surprised by the food."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 17:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: Hey, do you mind if I vlog today?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click== 18:
      mood = 'normal'
      prompt = "How will you respond?"
      choice_List = ['Vlog?', 'Why?', 'No problem']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
  if choice == 1:
    show = 'talking'
  # CHOICE 1:  Vlog? (makes Blake confused)
    # GERALD: Vlog? What is that?
    # BLAKE: You've never heard of vlogs?
    # GERALD: Is it like a kind of food?
    # BLAKE: No...it's kind of like a video blog type thing.
    # That doesn't sound too bad.
    # You just shrug and tell Blake it wouldn't bother you if they did.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Vlog? What is that?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: You've never heard of vlogs?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Is it like...a kind of food?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: No...it's kind of like a video blog type thing..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6
      mood = 'narrator'
      dialogue = "That doesn't sound too bad."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "You just shrug and tell Blake it wouldn't bother you if they did."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Why? (makes Blake sad)
    # GERALD: Why would you want to do that?
    # BLAKE: Well, it's kind of my job... I can leave your face out of the video if that's what you're worried about.
    # GERALD: Hm... Alright then.
    # BLAKE: Thanks.
    # Blake ruffles their hair a bit before pulling a really fancy looking camera from their bag.
    # This will be interesting.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Why?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: Well, it's kind of my job, but if you don't want me to that's okay... I could leave your face out of the video if that would help."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Hm...Alright then."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: Thanks."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6
      mood = 'narrator'
      dialogue = "Blake ruffles their hair a bit before pulling a really fancy looking camera from their bag."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "This will be interesting."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: No problem (makes Blake happy)
    # GERALD: No problem.
    # BLAKE: You sure? Don't worry, I'll keep your face out of the video.
    # GERALD: Yeah, that works.
    # BLAKE: Thanks man.
    # Blake excitedly brings out their vlogging gear and it looks very very very expensive.
    # You watch as Blake begins recording themselves and begins explaining what is going on. They are quite the performer.
    if click == 18:
      speaker = 0
      mood = 'normal'
      dialogue = "You: No problem."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: You sure? Don't worry, I'll keep your face out of the video."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Yeah, that works."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: Thanks, man."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      speaker = 6
      mood = 'narrator'
      dialogue = "Blake excitedly brings out their vlogging gear and it looks very very very expensive."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      speaker = 6
      mood = 'narrator'
      dialogue = "You watch as Blake begins recording themselves and begins explaining what is going on. They are quite the performer."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show


def blakeDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
# Blake shows the camera their food and your food, but never lifts the camera high enough to get your face in the shot.
# You finish the last slice of pizza and Blake takes the last sip of their milkshake.
# You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. Blake has to bring the camera a bit closer to their face to be heard by the mic attached.
# Blake shows the camera the games around them and turns to you.
# BLAKE: Where should we go?
  # [Racing, Refuse to choose, Minecraft]
  if click == 24:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "Blake shows the camera their food and your food as well, but never lifts the camera high enough to get our face in the shot."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 25:
    speaker = 6
    mood = 'narrator'
    dialogue = "You finish the last slice of pizzle and Blake takes the last sip of their milkshake."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 26:
    speaker = 6
    mood = 'narrator'
    dialogue = "You split the bill and head over to the noisier part of the arcade with all of the games and flashing lights. Blake has to bring the camera a bit closer to their face to be heard by the mic attached."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 27:
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake shows the camera the games around the two of you and turns to face you."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 28:
    speaker = 3
    mood = 'normal'
    dialogue = "Blake: Where should we go first?"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if choice == 0:
    if click == 29:
      mood = 'normal'
      prompt = "Pick a station"
      choice_List = ['Racing', 'Refuse to choose', 'Minecraft']
      show = 'choices'
      drawOptions(screen, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, prompt, choice_List,choice, show)
      
  if choice == 1:
    show = 'talking'
  # CHOICE 1: Racing (makes blake happy)
    # GERALD: You want to go to the racing machine?
    # BLAKE: I like the way you think!
    # BLAKE: Prepare to witness god tier gaming.
    # GERALD: Someone's confident.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: You want to go to the racing machine?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: I like the way you think!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: Prepare to witness god tier gaming."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Someone's confident."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  # elif choice == 2:
  elif choice == 2:
    show = 'talking'
  # CHOICE 2: Refuse to choose (makes blake sad)
    # GERALD: Choose for yourself.
    # BLAKE: Oh... alright.
    # GERALD: I didn't mean for that to sound so mean. I just meant that you're probably more familiar with this place than I am.
    # BLAKE: Okay, well let me go flex my racing skills.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Choose for yourself."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 5
      mood = 'sad'
      dialogue = "Blake: Oh...alright."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Wait, I didn't mean for that to sound mean. I just meant that you're probably more familiar with this place than I am."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: I guess. Well, let me go flex my racing skills."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  elif choice == 3:
    show = 'talking'
  # CHOICE 3: Minecraft (makes blake confused)
    # GERALD: Minecraft, maybe?
    # BLAKE: I... don't think they have that here? 
    # GERALD: Oh, well I guess you can pick then...
    # Blake tells you and the camera that they want to head over to the racing station.
    if click == 29:
      speaker = 0
      mood = 'normal'
      dialogue = "You: Minecraft, maybe?"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      speaker = 4
      mood = 'confused'
      dialogue = "Blake: I... don't think they have... Minecraft here"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 31:
      speaker = 1
      mood = 'confused'
      dialogue = "You: Oh, well I guess you can pick then."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 32:
      speaker = 3
      mood = 'normal'
      dialogue = "Blake: There's a racing station over there. Let me impress you with my sick mechanics!"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)

  # The two of you head over to the racing station where you find that there is already another player waiting for someone to race with. You decide to sit this one out and let Blake play against them. You're happy to just be the cameraman for this.
  # Blake is absolutely cracked at this game. It may just be because their competition is an 8 year kid, but they are showing no mercy.
  # Blake wins by a landslide and the kid doesn't seem to happy about that. Blake offers them all the tickets they won (and there are a lot) but the kid doesn't seem to care. In fact, they start crying and their mother has to come over to comfort him. She sends you and Blake a dirty look before strutting away with her crying child.

  if click == 33:
    speaker = 6
    mood = 'narrator'
    dialogue = "The two of you head over to the racing station where you find that there is already another player waiting for someone to race with. You decide to sit this one out and let Blake play against them instead. You're happy to just be the cameraman for this."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 34:
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake is absolutely cracked at this game. It may just be because their competition is an 8 year child, but Blake is showing no mercy."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 35:
    speaker = 6
    mood = 'narrator'
    dialogue = "Blake wins by a landslide and the kid doesn't seem too happy about that. Blake offers them all the tickets they won (and there are a LOT) but the kid doesn't seem to want them. In fact, they start crying and their mother has to come over to comfort them. She sends you and Blake a dirty look before strutting away with her sobbing child."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show
  

def blakeDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show):
# You can't help but laugh a little bit at that and Blake also has trouble stifling their laughter. Well, now it's your turn to play something.
# Blake tells you to try your luck at a game called "CLOUDY WITH A SIDE OF APPLES". Not the most creative name, but it gets the message across.
# GERALD: Alright, prepare to witness superhuman gaming!
# INSERT GAME
  if click == 36:
    speaker = 6
    show = 'talking'
    mood= 'narrator'
    dialogue = "You can't help but laugh a little bit at that and Blake also has trouble stifling their laughter. Well, now it's your turn to play something."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 37:
    speaker = 6
    mood= 'narrator'
    dialogue = "Blake tells you to try your luck at a game called 'CLOUDY WITH A CHANCE OF APPLES'. Not the most creative name, but it gets the message across."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  if click == 38:
    speaker = 0
    mood = 'normal'
    dialogue = "You: Alright, prepare to witness some supersnowman gaming!"
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
  return show

def blakeDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click):
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



def blakeDate_2 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
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
    blakeDate_2_intro (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)
    if click >= 15 and click < 24: #run part 1
      blakeDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_2_P1 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    if click >= 24 and click < 36:
      #run part 2
      blakeDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_2_P2 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    #run part 3
    if click >= 36 and click < 39:
      blakeDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
      show = blakeDate_2_P3 (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click, choice, show)
    # run end
    if click >= 39:
      blakeDate_2_end (screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, click)

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

def blakeDate_3 (screen, SCREEN_WIDTH, SCREEN_HEIGHT, show, choice):
  running = True
  click = 0
  #load background image
  night = pygame.image.load("night_1280x720.png")
  nightRect = night.get_rect()
  #load polaroid
  blake_final = pygame.image.load("blake_final_40.png")
  blake_finalRect = blake_final.get_rect()
  blake_finalRect = blake_finalRect.move(370, 50)
  clock=pygame.time.Clock()
  mood = 'narrator'
  speaker = 6
  show = 'talking'
  while running:
    screen.blit(night, nightRect)
    if click < 2: 
      screen.fill((0, 0, 0))
    dialogue = "You asked Blake before what they were planning for the date."
    drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 1:
      dialogue = "They refused to tell you, insisting that it had to be a surprise, but they promised it would be worth it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 2:
      dialogue = "And they were completely correct, it was worth it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 3:
      dialogue = "The night sky kind of matches their hair. It’s pretty. "
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 4:
      dialogue = "They guide you to the top of a hill and pull a blanket out of their backpack and place it on the ground."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 5:
      dialogue = "Blake sits down and motions for you to do the same."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 6:
      dialogue = "You listen."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 7:
      dialogue = "You ask Blake how they found this place because it’s amazing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 8:
      dialogue = "They tell you that their orphanage used to take them there."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 9:
      dialogue = "Orphanage? You ask about it."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 10:
      dialogue = "Blake tells you that their father left their mother when she was pregnant and that their mother passed away during childbirth, so they spent their childhood in an orphanage with their older brother."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 11:
      dialogue = "You ask about what life was like because they don’t seem to be uncomfortable talking about this topic. You’re guessing it’s because they might have told their Twitch viewers about it already."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 12:
      dialogue = "They inform you that it was rough, but when they were 10, their brother saved up for a Nintendo 3DS and they would play games together. Once their brother turned 18, he legally adopted Blake and they lived in a garbage apartment for a while."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 13:
      dialogue = "Blake started streaming just as a hobby, but it took off and they’ve been able to buy a nice apartment for them and their brother."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 14:
      dialogue = "You tell Blake that’s really impressive."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 15:
      dialogue = "Blake asks you about your childhood."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 16:
      dialogue = "You don’t have much to say because anything you would have to say feels weird to say after Blake’s story. You just tell them you’re an only child whose parents worked a lot and didn’t spend much time at home."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 17:
      dialogue = "After that, you both stare at the sky for a little bit, both mesmerized by how beautiful it is."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 18:
      dialogue = "Blake turns to face you. They swivel their body around so that their body is now facing you."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 19:
      dialogue = "You turn your neck to face them."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 20:
      dialogue = "Blake tells you that you look very handsome."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 21:
      dialogue = "You tell Blake they look amazing."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 22:
      dialogue = "Blake smiles and begins to lean in."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 23:
      dialogue = "You can feel your heart pounding in your fingertips."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 24:
      dialogue = "It only gets louder as Blake leans in."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 25:
      dialogue = "Their lips meet your cheeks and you close your eyes, but you can’t contain the smile that breaks out onto your face."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 26:
      dialogue = "Blake pulls back and their cheeks are red."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 27:
      dialogue = "And you know…"
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 28:
      dialogue = "This is the beginning of something very special."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 29:
      screen.fill((0, 0, 0))
      dialogue = "SOME TIME LATER..."
      drawSpeechBox(screen, dialogue, mood, colours_Dict, SCREEN_WIDTH, SCREEN_HEIGHT, speaker_List, speaker)
    if click == 30:
      #final polaroid
      screen.fill((0, 0, 0))
      screen.blit(blake_final, blake_finalRect)

    #monitor events
    for event in pygame.event.get():
      print (event)
      print (show)
      print(click)
    
      if (event.type == KEYDOWN and event.key == K_SPACE) and show == 'talking':
        click += 1
        print(click) #click counter
      if click == 31: #stop running
        running = False

    # Flip the display
    pygame.display.flip()
    #limit fps
    clock.tick(30)