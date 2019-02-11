#import all needed librarys for the game
import os;
import turtle;
import math;
import time;
from pathlib import Path;
import random;

#previous version/buildnumbers
#pre-Alpha.0.0.0.25-0

#define the version number of the game stage.major.minor.patch.buildNumber
gameVer = 'pre-Alpha.0.0.1';
buildNum = 'b - 40';

#name of game so I dont have to go threw the whole program when i come up with a tital
gameName = 'insert game tital later';

#stat holders
HP = 0;
STR = 0;
MAG = 0;
SPD = 0;
LCK = 0;
DEF = 0;
RES = 0;
EXP = 0;
ATK = 0;
# 100 copper = 1 silver 100 silver = 1 gold
GOLD = 0;
SILVER = 0;
COPPER = 0;

#where the actual game is located
trueGameFile = 'insert where the game is located later';

#login
def login():
    print("Login");
    mainMenu();

#create a account
def ca():
    os.system('cls');
    print("Create user account");
    #get user information to create profile file
    #get username
    userName = input("What would you like to set your username to : ");
    #get real name
    name = input("What is your real name? : ");
    #get Character Name
    charName = input("What will your character be called? : ");
    #create the variable that will be the file location for the user file
    userFile = userName + '.py';
    #check if username is already taken
    if os.path.isfile(userFile):
        print("Username is already taken. Try a diffrent one.");
        time.sleep(5);
        ca();
    #if userneame is avalible run this
    else:
        print("Username is avalible. Continueing to character creation.");
        time.sleep(3);
        os.system('cls');
        #print already gathered info
        print("Your username is", userName);
        print("Your real namem is", name);
        print("Your characters name is", charName);
        #get character discription info
        #get character race i.e. Human Elf Demi-Human
        charRace = input("What is your characters race? : ");
        #get character age
        charAge = input("What is your characters age? : ");
        #get character hair color
        charHair = input("What is your characters hair color? : ");
        #get character skin color
        charSkin = input("What is your characters skin color? : ");
        #get characters hight
        charHight = input("What is your characters hight? : ");
        #get characters body shape i.e. Thin Stocky Muscular Fat
        charBody = input("What is your characters body shape? : ");
        print("Loading");
        time.sleep(4);
        os.system('cls');
        #check all char info is correct
        print("Your username is", userName);
        print("Your real name is", name);
        print("Your characters name is", charName);
        print("Your characters race is", charRace);
        print("Your characters age is", charAge);
        print("Your characters hair color is", charHair);
        print("Your characters skin color is", charSkin);
        print("Your character hight is", charHight);
        print("Your charactes body shape is", charBody);
        userInput = input("Is this corect if no the account creation proccess will reset? : ");
        #if incorect do this
        if userInput.lower() == 'no':
            print("Restarting Account Creation...");
            time.sleep(2);
            ca();
            #if correct do this
        if userInput.lower() == 'yes':
            #clear screen
            os.system('cls');
            #tell user loading
            print("Loading...");
            #satCreate();
            #make a new file
            f = open(userName + ".py", 'w+');
            #open file
            
            #write all char and user info to the user file
            f.write("global userName = " + '\'' + userName + '\'' + '\n');
            f.write("global name = " + '\'' + name + '\'' + '\n');
            f.write("global charName = " + '\'' + charName + '\'' + '\n');
            f.write("global charRace = " + '\'' + charRace+ '\'' + '\n');
            f.write("global charAge = " + '\'' + charAge + '\'' + '\n');
            f.write("global charHair = " + '\'' + charHair + '\'' + '\n');
            f.write("global charSkin = " + '\'' + charSkin + '\'' + '\n');
            f.write("global charHight = " + '\'' + charHight + '\'' + '\n');
            f.write("global charBody = " + '\'' + charBody + '\'' + '\n');
            #close file
            f.close();
            
            os.system('cls');
            #print instructions
            print("""USER CREATION SUCSESS
                   To login to your account when you return to the main menu press 1""");
            print("loading");
            time.sleep(10);
            mainMenu();
#exit from launcher
def lExit():
    os.system('cls');
    #ask if user actually wants to exit
    userInput = input("Are you sure you want to exit? (yes/no) : ");

    #check if the user wants to exit or not
    if userInput.lower() == 'yes':
        os.system('cls');
        print("Thank you for playing", gameName);
        time.sleep(3);
        exit();

    if userInput.lower() == 'no':
        os.system('cls');
        mainMenu();
    

def dis():
    os.system('mode con cols=150');
    #clear screen as game loads
    os.system('cls');
    #print the game name and version number
    print(gameName, gameVer);
    #print the version disclaimer
    print("build number : ", buildNum);
    print("DISCLAIMER: this is a pre-Alpha release so there may be fatal bugs present in the game");
    print("             WE ARE NOT RESPONSIBLE FOR ANY DAMAGE TO YOUR DEVICE RUN AT YOUR OWN RISK");
    print("Loading...");
    #Sleep on the Disclaimer for 10 seonds
    time.sleep(10);
#create the Main Menu of the game
def mainMenu():
    #clear the screen
    os.system('cls');

    #print the main menu
    print("Welcome to the", gameName, "Launcher")
    print('');
    print('');
    print("1. Login");
    print("2. Create Account");
    print("3. Exit");

    #get the user input
    userInput = input("Type the number of the action you would like to carry out : ");

    #check what the user wants to do
    if userInput == '1':
        print("Loading Login");
        login();
    if userInput == '2':
        print("Loading Create Account");
        ca();
    if userInput == '3':
        print('Exiting');
        lExit();
    #if user input is not valid run this
    else:
        print('please select a valid option')
        time.sleep(4);
        mainMenu();


#generate the stats for the user
#something in here doesnt work I think fix it later
def statCreate():
    #base HP stat 25 random chance of getting up to 10 added
    global HP;
    global STR;
    global MAG;
    global SPD;
    global LCK;
    global DEF;
    global RES;
    global GOLD;
    global SILVER;
    global COPPER;
    HP = 25 + random.randint(-10, 10);
    STR = random.randitn(10, 15);
    MAG = random.randit(1, 5);
    SPD = random.randit(5, 10);
    LCK = random.randit(1, 10);
    DEF = random.randit(1, 10);
    RES = random.randit(1, 5);
    # 100 copper = 1 silver 100 silver = 1 gold
    GOLD = 10;
    SILVER = 100;
    COPPER = 1000;
    #sleep for 10 seconds
    time.sleep(10);



dis();
mainMenu();
