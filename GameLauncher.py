#import all needed librarys for the game
import os;
import turtle;
import math;
import time;
from pathlib import Path;
import random;
import importlib;

#clear screen and print loading incase computer takes longer than it should starting the GL
os.system('cls');
print('loading...')

#previous version/buildnumbers
#pre-Alpha.0.0.0.25-0

#define the version number of the game stage.major.minor.patch.buildNumber
gameVer = 'pre-Alpha.0.2.0';
buildNum = 'b - 52';

#name of game so I dont have to go threw the whole program when i come up with a tital
gameName = 'insert game tital later';

#holders for all needed char variables
userName = 'hold';
userNameLog = 'hold';
name = 'hold';
charName = 'hold';
gameToPlay = 'hold';


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
option1 = 'game1.py'
trueGameFile = 'game\\' + option1 ;

#login
def login():
    global userNameLog;
    global userFile;
    #get users username
    os.system('cls');
    userNameLog = input('What is your username? : ');
    #check if username exists
    userFile = userNameLog + '.py';
    if os.path.isfile(userFile):
        loginGood();
    else:
        errorLog();
    

#what to do if there was a login errorLog
def errorLog():
    os.system('cls');
    print('ERROR');
    print("This user profile doesn't exist or has issues try again or make a new profile");
    time.sleep(10);
    login();
    
    
#what to do if the login is good
def loginGood():
    global userFile;
    os.system('cls');
    global gameToPlay
    print('1. HOLDER')
    gameToPlay = input('Type the number corisponding to the game you want to play : ');
    if gameToPlay == '1':
        gameOneStart();
    else:
        gameError();


#define where the first game is located and how to load it
def gameOneStart():
    global userFile
    HP = importlib.import_module(userNameLog, 'HP');
    print(HP);
    time.sleep(10);
    mainMenu();

#what to do if there was a error in loading the selected game
def gameError():
    os.system('cls');
    print('This game does not exist or can not be loaded by the current launcher update from GitHub or try a diffrent game if this is not a valid option');
    time.sleep(5);
    os.system('cls');
    loginGood();


#create a account
def ca():
    global userName;
    global name;
    global charName;
    global userFile;
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
        cfile();
    cfile();


def cfile():
    global userName;
    global name;
    global charName;
    global userFile;
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
        f.write('def profile():');
        f.write("    global userName \n");
        f.write("    global name \n");
        f.write("    global charName \n");
        f.write("    global charRace \n");
        f.write("    global charAge \n");
        f.write("    global charHair \n");
        f.write("    global charSkin \n");
        f.write("    global charHight \n");
        f.write("    global charBody \n");
        f.write("    global HP \n");
        f.write("    global STR \n");
        f.write("    global MAG \n");
        f.write("    global SPD \n");
        f.write("    global LCK \n");
        f.write("    global DEF \n");
        f.write("    global RES \n");
        f.write("    global GOLD \n");
        f.write("    global SILVER \n");
        f.write("    global COPPER \n");
        f.write("    userName = " + '\'' + userName + '\'' + '\n');
        f.write("    name = " + '\'' + name + '\'' + '\n');
        f.write("    charName = " + '\'' + charName + '\'' + '\n');
        f.write("    charRace = " + '\'' + charRace+ '\'' + '\n');
        f.write("    charAge = " + '\'' + charAge + '\'' + '\n');
        f.write("    charHair = " + '\'' + charHair + '\'' + '\n');
        f.write("    charSkin = " + '\'' + charSkin + '\'' + '\n');
        f.write("    charHight = " + '\"\"\"' + charHight + '\"\"\"' + '\n');
        f.write("    charBody = " + '\'' + charBody + '\'' + '\n');
        f.write("    HP = " + '\'' + str(HP) + '\'' + '\n');
        f.write("    STR = " + '\'' + str(STR) + '\'' + '\n');
        f.write("    MAG = " + '\'' + str(MAG) + '\'' + '\n');
        f.write("    SPD = " + '\'' + str(SPD) + '\'' + '\n');
        f.write("    LCK = " + '\'' + str(LCK) + '\'' + '\n');
        f.write("    DEF = " + '\'' + str(DEF) + '\'' + '\n');
        f.write("    RES = " + '\'' + str(RES) + '\'' + '\n');
        f.write("    GOLD = " + '\'' + str(GOLD) + '\'' + '\n');
        f.write("    SILVER = " +'\'' + str(SILVER) + '\'' + '\n');
        f.write("    COPPER = " + '\'' + str(SILVER) + '\'' + '\n');
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
