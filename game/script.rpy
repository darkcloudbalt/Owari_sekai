init:
    $ style.default.font = "VL-Gothic-Regular.ttf"
    $ style.default.language = "eastasian"
    image me_wedding = im.Scale("me_wedding.png", 700, 700)
    image chiho_school = im.Scale("chiho_school.png", 700, 700)
    image chiho_wedding = im.Scale("Chiho_wedding.png", 800, 800)
    image chiho_wedding_kiss = im.Scale("Chiho_wedding_kiss.png", 700, 700)
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

    "Although the room was silent, my mind screamed Stop! It should be me!"

    hide me_wedding
    with dissolve

    show chiho_wedding_kiss
    with dissolve

    p "... you may not kiss the bride."

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

    show chiho_school
    with dissolve

    c "Hey wake up!"

    "To be continued..."

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

    # This ends the game.

    return