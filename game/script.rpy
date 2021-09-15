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
define m = Character('Me')
define p = Character('Priest')


# The game starts here.

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

    c "Mou!"

    "Thus ends another unevent day..."

    jump past2

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

    label past2:

    scene bg class2
    with fade

    # continue with a new event
    return

    label bad_end_1:

    scene black
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