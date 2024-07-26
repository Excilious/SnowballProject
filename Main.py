#Made by Mohammed Al-Sady
#Started around 27/12/21
#Edits
#27/12/21
#30/12/21

Character = game.create_sprite(0, 0)#Creates the Main Character
RandomPosition = randint(0, 4)#Gives a Random Position so the Bot doesnt have to follow the MainCharacter
Bot = game.create_sprite(5, RandomPosition)#Creates the bot and uses the random position as its Y position
TimePause = 200#Gives the speed and difficulty of the Main Character
RandomDifficulty = randint(300,700)
BotsDifficulty = RandomDifficulty#Selects a random difficulty
BotsHealth = 50 #Main Bots Health
CharactersHealth = 50 #MainCharacter Health
DelayOfInput = 200 #Delays
TotalChanceOfSnowballThrow = 6 #The chance of the bot throwing a snowball
Score = 0 #Base score


#---Main Character---#
def MainCharacter():#Function of the main character
    global Character#Uses the variables created at the start
    global TimePause
    for i in range(4):#Looping movement of the sprite going up and down with the delay
        Character.change_yby(1)
        pause(TimePause)
    for i in range(4):
        Character.change_yby(-1)
        pause(TimePause)
basic.forever(MainCharacter)#Forever loop used
    
#---Bot---#
def AutoCharacter():
    global Bot#Allows the variable to be editied freely
    global TimePause
    global BotsHealth
    global TotalChanceOfSnowballThrow
    for i in range(4):
        Bot.change_yby(1)#Changes the bots position by 1, 4 times
        pause(BotsDifficulty)#DelayOfInput
        RandomLaunchEvent = randint(1, TotalChanceOfSnowballThrow)
        if RandomLaunchEvent > 3:
            OnBotSnowBallLaunched()
    for i in range(4):
        Bot.change_yby(-1)#Same but opposite
        pause(BotsDifficulty)
    if RandomLaunchEvent > 3:#Gives a random throw out
        OnBotSnowBallLaunched()
    CheckSpriteHealth()#Constantly checks on each of the sprites health
basic.forever(AutoCharacter)

def CheckSpriteHealth():#The function to check the health
    global BotsHealth#Variables
    global CharactersHealth
    global Score
    if BotsHealth <= 0:#If the bots health is equal or more to 0 (the health can decrease more than 0)
            basic.clear_screen()#Clears the screen
            pause(10)#delay
            basic.show_string("YOU WIN!")#Gives a victory screen
            pause(10)
            basic.show_string("YOUR SCORE IS ", Score)#Prints out the score
            pause(300)#Longer delay
            BotsHealth = 100#Resets the properties of the bot and characters health
            CharactersHealth = 100
    elif CharactersHealth <= 0:#Same as above
        basic.clear_screen()
        pause(10)
        basic.show_string("YOU LOSE!")
        pause(10)
        basic.show_string("YOUR SCORE IS ",Score)
        pause(300)
        CharactersHealth = 100
        BotsHealth = 100

def OnBotSnowBallLaunched():#When the bot snowball has been launched
    global Score#Variables to edit
    global Character
    global CharactersHealth
    BotSnowball = game.create_sprite(Bot.x() - 1, Bot.y())#Creates a sprite that is -1 away from the bot (since the bot is facing towards the user)
    BotSnowball.set_blink(200)#gives a blinking effect to see if it is a snowball
    BotsAmount = 1#Later on
    for i in range(5):#Changes the position of the snowball
        BotSnowball.change_xby(BotsAmount)
        pause(TimePause)
        BotsAmount = BotsAmount - 1
    if BotSnowball.is_touching(Character):#If the snowball hits the character
        Character.set_brightness(100)#Lowers the brightness to the position that it was hit
        pause(1000)
        Character.set_brightness(255)#Increases towards the original position
        Score = Score - 1#Removes the score by 1 due to the snowball hitting the character
        BotSnowball.delete()#Removes the sprite
        CharactersHealth = CharactersHealth - 1#Removes 1 health from the character
    if BotSnowball.x() == 0:#If went out of boundaries
        BotSnowball.delete()

    
#---ButtonAPressed Event---#
def SnowballOption1Launch():#Snowball for the user
    global Bot
    global BotsHealth
    global DelayOfInput
    global Score
    pause(DelayOfInput)
    Amount = 1
    CreateSnowball = game.create_sprite(Character.x() + 1, Character.y())#Similar to above except the score increases when hit to bot and the position is +1 whilst removing the bots health only
    CreateSnowball.set_blink(200)
    for i in range(5):
        CreateSnowball.change_xby(Amount)
        pause(TimePause)
        Amount = Amount + 1
    if CreateSnowball.is_touching(Bot):
        Bot.set_brightness(100)
        pause(1000)
        Bot.set_brightness(255)
        CreateSnowball.delete()
        BotsHealth = BotsHealth - 1
        Score = Score + 1
        CreateSnowball.set_blink(50)
        print(BotsHealth)
    if CreateSnowball.x() == 4:
        CreateSnowball.delete()
input.on_button_pressed(Button.A,SnowballOption1Launch)
    
#---ButtonBPressed Event---#
def SnowballOption2Launch():#Exactly the same towards the original one above
    global Bot
    global BotsHealth
    global DelayOfInput
    global Score
    pause(DelayOfInput)
    Amount = 1
    CreateSnowball = game.create_sprite(Character.x() + 1, Character.y())
    CreateSnowball.set_blink(200)
    for i in range(5):
        CreateSnowball.change_xby(Amount)
        pause(TimePause)
        Amount = Amount + 1
    if CreateSnowball.is_touching(Bot):
        Bot.set_brightness(100)
        pause(1000)
        Bot.set_brightness(255)
        CreateSnowball.delete()
        BotsHealth = BotsHealth - 1
        Score = Score + 1
        CreateSnowball.set_blink(50)
        print(BotsHealth)
    if CreateSnowball.x() == 4:
        CreateSnowball.delete()
input.on_button_pressed(Button.B,SnowballOption2Launch)
