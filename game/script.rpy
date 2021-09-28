init:
    $ style.default.font = "VL-Gothic-Regular.ttf"
    $ style.default.language = "eastasian"
    image me_wedding = im.Scale("me_wedding.png", 700, 700)
    image chiho_angry = im.Scale("chiho_angry.png", 850, 750)
    image chiho_annoy = im.Scale("chiho_annoy.png", 850, 750)
    image chiho_delight = im.Scale("chiho_delight.png", 850, 750)
    image chiho_laugh = im.Scale("chiho_laugh.png", 850, 750)
    image chiho_normal = im.Scale("chiho_normal.png", 850, 750)
    image chiho_sad = im.Scale("chiho_sad.png", 850, 750)
    image chiho_sleepy = im.Scale("chiho_sleepy.png", 850, 750)
    image chiho_shock = im.Scale("chiho_shock.png", 850, 750)
    image chiho_smile = im.Scale("chiho_smile.png", 850, 750)
    image chiho_smile2 = im.Scale("chiho_smile2.png", 850, 750)
    image chiho_smug = im.Scale("chiho_smug.png", 850, 750)
    image chiho_sad = im.Scale("chiho_sad.png", 850, 750)
    image chiho_wedding = im.Scale("Chiho_wedding.png", 800, 800)
    image chiho_wedding_kiss = im.Scale("Chiho_wedding_kiss.png", 800, 800)
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Chiho")
define m = Character('Yuu')
define p = Character('Priest')

# The game starts here.

###NOTES###
# 1. Think of the ring from KanoKari as gift from family
# 2. Think of resturant from KimiMachi where Yuzuki gets jealous of Haruto getting hit on


################################ Present Day ##########################################
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play music "wedding_dress.mp3"

    scene bg church2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy
    show me_wedding
    with dissolve

    # These display lines of dialogue.

    # "Dedicated to Emily"

    "The day finally came. As I stood here by the side watching you walk down the aisle..."

    "Should be me... It should be me! I kept thinking this to myself as I stood here."

    p "Is there anyone here that objects to the union between these two? Speak now or forever hold your peace."

    "Although the room was silent, I wanted to scream at the top of my lungs." 
    
    "Stop! It should be me!"

    hide me_wedding
    with dissolve

    show chiho_wedding_kiss
    with dissolve

    p "... you may now kiss the bride."

    hide chiho_wedding_kiss
    with dissolve
    
    show me_wedding
    with dissolve

    "I wonder how this all began...? Perhaps if I just said something back then..."

    menu:
        "Think about the past.":

            jump past_route

        "What's done is done.":

            jump bad_end_1

################################ Past 1 ##########################################
    label past_route:

    scene black
    with fade
    
    stop music fadeout 1.0
    play music "First Love.mp3"


    "Back in my 1st year in high school..."

    c "-ke up!"

    "Huh? Is someone calling me?"

    show bg class2
    with fade

    show chiho_annoy
    with dissolve

    c "Hey wake up!"

    m "Oh... its you Nakano-san."

    hide chiho_annoy
    show chiho_shock

    c "..."

    m "???"

    hide chiho_shock
    show chiho_sleepy

    c "Nakano-san... huh..."

    m "?"

    hide chiho_sleepy
    show chiho_normal

    m "So what did you call out to me for Nakano-san?"

    hide chiho_normal
    show chiho_smile

    c "I wanted to ask if you want to have lunch together?"

    menu:
        "Oh, sure.":
            
            jump lunch_together

        "Sorry, but I already made plans.":
            
            jump lunch_alone

################################ Past 1-1 ##########################################
    label lunch_together:

    m "Oh sure."

    hide chiho_delight
    with dissolve

    show bg cafeteria
    with fade

    show chiho_smile
    with dissolve

    c "So have you found any clubs you want to join yet?"

    m "Hmm... after some thought... I decided to go with Go Straight Home Club!"

    hide chiho_smile
    show chiho_annoy

    c "That is such a waste! You should join the Art Club!"

    m "Nah, art has never been a strong suit of mine."

    hide chiho_annoy
    show chiho_laugh

    c "That's okay because we welcome anyone that is willing to join."

    m "Well then I guess that I cannot join the Art Club then."

    hide chiho_laugh
    show chiho_shock

    c "Why is that?"

    m "Because I don't want to join the Art Club."

    hide chiho_shock
    show chiho_annoy

    c "もう！!*pouts*"

    "Thus ends another unevent day..."

    jump past2

################################ Past 1-2 ##########################################
    label lunch_alone:

    m "Sorry, but I already made plans."

    hide chiho_delight
    show chiho_sleepy

    c "Oh..."

    hide chiho_sleepy
    show chiho_smile

    c "Sorry for suddenly asking out of the blue. Perhaps next time?"

    m "Yeah, let's have lunch next time."

    c "Promise?"

    m "Yeah, I promise."

    hide chiho_smile
    show chiho_laugh

    c "Ok!"

    hide chiho_laugh
    with dissolve
    
    "It is not like I did not want to have lunch with Nakano or anything. However, since we entered high school, she continues to act as if we were still in elementary school and clinging to me all the time."
    "Enough where the other students have been asking if we were dating."

    jump past2

################################ Past 2 ##########################################
    label past2:

    stop music fadeout 1.0
    play music "Cheerful Days.mp3"

    scene bg spring day
    with fade

    "I was on my way to school one morning when I heard someone calling out to me."

    c "Wait up!"

    "I turned around and saw Chiho running up to me."

    show chiho_smile2
    with dissolve

    c "Good morning Yuu-kun!"

    m "Ah, morning Nakano-san."

    hide chiho_smile2
    show chiho_annoy

    c "You could of waited for me before you left this morning!"

    m "Sorry, sorry, but it isn't often that I get to be the one to leave on time."

    hide chiho_annoy
    show chiho_smile

    c "Come to think of it. This is the first time since we were kids, that you left for school before me."

    m "It isn't like you to oversleep neither. Were you up all night studying?"

    stop music fadeout 1.0
    play music "Cherry Blossoms.mp3"

    hide chiho_smile
    show chiho_sleepy

    c "..."

    m "Something wrong?"

    c "Actually Yoshioka-senpai and I were talking last night."

    m "Is that the senpai from your club?"

    "Why is she so quiet all of a sudden?"

    hide chiho_sleepy
    with dissolve

    stop music fadeout 1.0
    play music "After School.mp3"

    scene bg class2
    with fade

    "I never had a chance to speak with Chiho since this morning. During break and lunch time, she was surrounded by the other girls in class. They looked like they were having fun gossiping about something."

    "After class she also immediately went to the Art Club. Perhaps I should stop by to check up on things."

    ".. Then again everyone is already asking me if there is anything going on between Chiho and I and if I were to show up at her club after school then it would only raise more suspicions..."

    menu:
        "Go check on Chiho at her club.":

            jump confrontation

        "Go home.":

            jump encounter
    
################################ Past 2-1 ##########################################
    
    label confrontation:

    scene bg school hallway
    with fade
    
    stop music fadeout 1.0
    play music "glitter.mp3"

    "As I left the class and started making my way back towards the art club, I ran into Chiho."

    show chiho_shock
    with dissolve

    m "Hey Nakano-san."

    c "Yuu-kun..."

    "Why was she so shock from just running into me in the hallway?"

    m "I just thought that I would check and see how you are doing. You were a bit distant this morning."

    "From inside the art club room, I could hear someone calling out to Chiho. A moment later, Yoshioka-senpai stepped out calling out for Chiho again."

    hide chiho_shock
    show chiho_sleepy

    c "Sorry Yuu-kun, but Yoshioka-senpai and I are about to head out and pick up some art supplies."

    m "I thought the school normally provides the supplies?"

    c "Yoshioka-senpai and I were working on a report requesting for more club funds. We received the approval this morning."
    c "There were a lot of students ended up joining the club this year."

    "Chiho and Yoshioka-senpai then left to buy some more art supplies together."

    hide chiho_sleepy
    with dissolve

    jump past3_nakano

################################ Past 2-2 ##########################################

    label encounter:

    stop music fadeout 1.0
    play music "Around Session.mp3"

    scene bg city night
    with dissolve

    "I decided go head out to the game center and spent the evening there. By the time I left the game center, it was already dark outside."
    "It was getting late anyways, so I guess I better head home."

    scene bg train night
    with dissolve

    "As I took the train home, I thought to myself. What was Chiho up to right now? There is no way she isn't home right?"
    "I get off the train at my stop and started making my way home."

    scene bg spring night
    with dissolve

    "I notice someone in front of me walking alone. It can't be..."

    m "Hey Nakano-san, what are you still doing out this late?"

    show chiho_smile
    with fade

    stop music fadeout 1.0
    play music "glitter.mp3"

    c "Yuu-kun...? What are you doing here?"

    m "I should be asking you the same thing. Are you just getting home now? At this hour?"

    c "Sorry, we had a lot things to do for the club today."

    m "Ehh, sounds like things are tough in your club."

    hide chiho_smile
    show chiho_smug

    c "Things are really busy! We had to ask the staff for a bigger budget and we even had to buy our own supplies!"

    "She sounds like she is having a lot of fun with the Art Club."

    m "But it sounds like you are really enjoying yourself."

    c "It is not too late to join, you know?"

    m "Hmmm... I think I will pass still. Joining a club at this time is just weird. Plus everyone already knows one another and it will be difficult to get along with everyone now."

    hide chiho_smug
    show chiho_sad

    c "..."

    m "How is club activities coming along? Are you getting along with everyone?"

    c "..."

    m "What about Yoshioka-senpai? You said you were up all night talking to him right? What were you two talking about?"

    c "..."

    "I looked over to Chiho and noticed a sad expression on her face. Does she want me to join that badly?"

    m "Remember when we use to walk home together all the time?"

    hide chiho_sad
    show chiho_delight

    c "We would always walk to school together and back in middle school."

    m "Don't forget elementary as well. We were always in the same class back then as well."

    c "うん！ Un! Everyday was so much fun back then! We would often stop by the candy shop and buy a lot of candy!"

    m "Then our parents would yell at us for eating so much candy."

    c "That's right! You were such a bad influence on me back then!"

    m "Me?! It was your idea to get candy all the time. You said it helped you study!"

    hide chiho_delight
    show chiho_angry

    c "Don't you try to blame that on me!"

    hide chiho_angry
    show chiho_laugh

    "It has been a while since the two of us were able to talk like this. I somehow do miss this..."

    menu:
        "Hold her hand.":

            jump date1

        "Don't hold her hand.":

            jump go_home

################################ Past 2-3 ##########################################
    label date1:

    stop music fadeout 1.0
    play music "futari no kimochi.mp3"

    "Taking the opportunity, I decided to grab and held her hand."

    hide chiho_laugh
    show chiho_shock

    c "..."

    hide chiho_shock
    show chiho_smile

    m "..."

    c "..."

    m "It... has been a while since the two of us were able to go home and talk like this, isn't it?"

    c "Yeah..."

    m "Hey Chi- Nakano-san?"

    hide chiho_smile
    show chiho_annoy

    c "Chiho!"

    hide chiho_annoy
    show chiho_sad

    c "I prefer Chiho... Nakano feels so distant..."

    m "Sorry... I just thought since we are in high school now, you pre-"

    c "Don't go deciding that on your own!"

    m "You are right... sorry about that Chiho..."

    hide chiho_sad
    show chiho_shock

    c "..."

    hide chiho_shock
    show chiho_smile2

    "Without saying another word, the two of us the rest of the way home hand in hand."

    jump past3_chiho

################################ Past 2-4 ##########################################
    label go_home:

    "I decided not to do anything. We continued walking home while talking about nothing in particular."

    jump past3_nakano

################################ Past 3 ##########################################
    label past3_nakano:

    scene black
    # Have an event where Yuu starts calling her Chiho again.

    "To be continued in v1.02"
    
    return

################################ Past 3-1 ##########################################
    label past3_chiho:

    scene black

    # Write a scene similar to calling Rina by her first name after forgetting to do homework.

    return

    "To be continued in v1.02"

################################ Bad Ending 1 ##########################################
    label bad_end_1:

    scene bg sakura
    with fade
    
    stop music fadeout 1.0
    play music "Gameover.mp3"

    show chiho_wedding
    with dissolve

    "I continue watching as the newly wed couple walk out of the church and get into the limo and drive off."

    "I am such a coward..."

    "{b}Bad ending{/b}"

    # c "笑い会えるってすごく幸せなこと"

    # c "それをきみから教えてもらったんだよ"

    # Dedicated to Emily

    # This ends the game.

    return
