#import all needed librarys for the game
import os;
import turtle;
import math;
import time;
from pathlib import Path;
import random;

os = 'hold';
clear = 'cls';


os = input('1 for Windows 2 for Unix');


if os == '1':
    clear = 'cls'
if os == '2':
    clear = 'clear';
else:
    print('Defulting to Windows');
    clear = 'cls';



#clear screen and print loading incase computer takes longer than it should starting the GL
os.system(clear);
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
    os.system(clear);
    userName = input('What is your user name? : ');
    userFile = userName + '.py';
    if os.path.isfile(userFile):
	    loginGood();
    else:
        logError();

#if the login is good do this
def loginGood():
    global userFile;
    global gamer;
    print('1. ' + game1);
    gamer = input('Type the number of the game you want to play : ');
    if gamer == '1':
        os.system(clear);
        print('LOADING...')
        f = ('tans.temp' , 'w+');
        f.write(userName);
        f.write(random.randint(1, 1000));
    else:
        print('Game does not exitst');
        loginGood();
    os.system(clear);
    print('LOGIN GOOD');
    print('Loading your save please wait...');
    



#create a account
def ca():
    global userName;
    global name;
    global charName;
    global userFile;
    os.system(clear);
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
     


def cfile():
    global userName;
    global name;
    global charName;
    global userFile;
    print("Username is avalible. Continueing to character creation.");
    time.sleep(3);
    os.system(clear);
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
    os.system(clear);
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
        os.system(clear);
        #tell user loading
        print("Loading...");
        #satCreate();
        #make a new file
        f = open(userName + ".py", 'w+');
        #open file
        
        #write all char and user info to the user file
        f.write("global userName \n");
        f.write("global name \n");
        f.write("global charName \n");
        f.write("global charRace \n");
        f.write("global charAge \n");
        f.write("global charHair \n");
        f.write("global charSkin \n");
        f.write("global charHight \n");
        f.write("global charBody \n");
        f.write("global HP \n");
        f.write("global STR \n");
        f.write("global MAG \n");
        f.write("global SPD \n");
        f.write("global LCK \n");
        f.write("global DEF \n");
        f.write("global RES \n");
        f.write("global GOLD \n");
        f.write("global SILVER \n");
        f.write("global COPPER \n");
        f.write("userName = " + '\'' + userName + '\'' + '\n');
        f.write("name = " + '\'' + name + '\'' + '\n');
        f.write("charName = " + '\'' + charName + '\'' + '\n');
        f.write("charRace = " + '\'' + charRace+ '\'' + '\n');
        f.write("charAge = " + '\'' + charAge + '\'' + '\n');
        f.write("charHair = " + '\'' + charHair + '\'' + '\n');
        f.write("charSkin = " + '\'' + charSkin + '\'' + '\n');
        f.write("charHight = " + '\'' + charHight + '\'' + '\n');
        f.write("charBody = " + '\'' + charBody + '\'' + '\n');
        f.write("HP = " + '\'' + str(HP) + '\'' + '\n');
        f.write("STR = " + '\'' + str(STR) + '\'' + '\n');
        f.write("MAG = " + '\'' + str(MAG) + '\'' + '\n');
        f.write("SPD = " + '\'' + str(SPD) + '\'' + '\n');
        f.write("LCK = " + '\'' + str(LCK) + '\'' + '\n');
        f.write("DEF = " + '\'' + str(DEF) + '\'' + '\n');
        f.write("RES = " + '\'' + str(RES) + '\'' + '\n');
        f.write("GOLD = " + '\'' + str(GOLD) + '\'' + '\n');
        f.write("SILVER = " +'\'' + str(SILVER) + '\'' + '\n');
        f.write("COPPER = " + '\'' + str(SILVER) + '\'' + '\n');
        #close file
        f.close();
            
        os.system(clear);
        #print instructions
        print("""USER CREATION SUCSESS
                To login to your account when you return to the main menu press 1""");
        print("loading");
        time.sleep(10);
        mainMenu();
#exit from launcher
def lExit():
    os.system(clear);
    #ask if user actually wants to exit
    userInput = input("Are you sure you want to exit? (yes/no) : ");

    #check if the user wants to exit or not
    if userInput.lower() == 'yes':
        os.system(clear);
        print("Thank you for playing", gameName);
        time.sleep(3);
        exit();

    if userInput.lower() == 'no':
        os.system(clear);
        mainMenu();
    

def dis():
    os.system('color 0F');
    os.system('mode con cols=200');
    #clear screen as game loads
    os.system(clear);
    #print the game name and version number
    print(gameName, gameVer);
    #print the version disclaimer
    print("build number : ", buildNum);
    print("DISCLAIMER: this is a pre-Alpha release so there may be fatal bugs present in the game");
    print("             WE ARE NOT RESPONSIBLE FOR ANY DAMAGE TO YOUR DEVICE RUN AT YOUR OWN RISK");
    print("Loading...");
    #Sleep on the Disclaimer for 10 seonds
    time.sleep(10);
	
	
	
	
def momo():
    os.system('color F9');
    print(""":::::::::::::::::::::::::::::::::::::::::::----::::::::::::::::::::::::::///+++++oosoosssssssyyysyhhhhyyyyyyyyyyyyysssssssooo+++////::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::---::::::::::::::::::::::::-----::///:://////+osyyyyhddddhys++//////////::::::::::::::::::::::::::::---------:-------::::::::-----------:::::::::::::::-----
://///::::::::::::::::::::::::::::::::::::::---::::::::::::::::::::::::---------::/:/+syhdddddddmmmmmmmmmdyo/:::::::::::---::::::-:-:::::::::------------------------------------------::::-------------
/////////::::::::::::::::::::::::::::::::::::--:/://///::::::::::::::::-----------:/sdmdhyhddyo+ymmmmdydmmmdhs/::::::::--------:-----::-----------------------------------------------------------------
//////////::::::::::::::::::::::::::::::::::::-:///////:/:::::::::::::::---------:sdmhsoyddho::/:syddmsohdmdddhs/:::::----------------:-----------------------------------------------------------------
///////////:::::::::::::::::::::::::::::::::::-:///////::::::::::::::::::-------:ymmyosddhho/::/::ohhddo/yddddddh+::-------------:::::::::::::::/:------------------------------------------------------
///////////::::::::::::::::::::::::::::::::::::://////:::::::::::::::::::------:hdmyosdhdhs///://::sdhdd++hmdddddd+:------------:/+////////::://+:-----:----------------------------::::::::::::-----:::
///////////::::::::::::::::::::::::::::::::::::://////:::::::::::::::::::-----:sdmhoyhddyy////////:/ddddh+sdmmmmmdd/:---------:://///////++/::///:----::-------------------:::::::::::::::::::::::::::::
//////////::::::::::::::::::::::::::::::::::::::////:::::::::::::::::::::------ddmyyyddys+//++++/+//smmhm+sdmmmmmmdy:--------::/+////++-.-/+/:://:-----------------------:::::::::::::::::::::::::::::::
////////::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::------:dydsyhhyoy+++/++++//++dmyd+sdmmmmmmmd+--------:///////oo/::+o/:://:---------------------::::::::///////////////////////::
///////:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-------syyossyoos++++++ooo+++ymhhosdmNmmmmmms:------::/+/////+oooo+/::://---------------------:::::::///////////////////////////
///////::::::::::::::::::::::::::::::::::::::::::::::::::::::----:::::---------+yhysssoosoosyyhhdhyo+syhyoshmNmmmmmmh:------:://////+oooo++++////-------------------::::::://///////////////////////////
//////:::::::::::::::::::::::::::::::::::::::::::::::::::::::::---::::---------sdhddhsooosshdmhsssyhoosooooymmmmmmmmm/------::/+////+++++++++////------------------::::::://////////////////////////////
////:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::---:::----------+yddyhho++osdmdhy+//smoo+///ommmmmmmmms------::/+/+//+oo++++++///:-----------------:::::::///////////////////::::////////
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::--:::----------/ymdhhd+//+ohmdmmdoosmso////ommmmmmmmmd:-----::/+/+//+++++++++///:-----------------::::::////////////////////:::::///////
::::::::::::::::::::::::::::::::::::::::::::::-::::::::::::::::::::::----------/yhdddy+/:/+ohmddhhhdyo////+ymNmmmmmmmd/-----::/+////++++++++////:-------:---------:::::///////////////++/////:::////////
::::::::::::::::::::::::::::::::::::::::::::::-::::::::::::::::::::::----------/yhdhso/:://+shddddhs+///++oymNmmmmmNmds:----::/+////+ooooo++////:------::---------::::://////////////++++++/////////////
::::::::::::::::::::::::::::::::::::::::::::::-::::::::::::::::::::::---------::oyyoo+::://+oosyyyso++++osydmNmmmNNmmdy:----:://///osssssssoo///:------::--------:::::://////////////+++++++++++++++////
::::::::::::::::::::::::::::::::::::::::::::::-::::::::::::::::::::::---------:-ysooo/:::://+++ooooooosssshmmNmmmNNmmms/::-:::////+ssshdhssss+//:----::::--------:::::://////////////++++++++++++++++///
:::::::::::::::::::::::::::::::::::::::::::::--:::::::::::::::::::::::--------::sdyoososs+////++oosyyyyyhhmmNNmmNNNmmmo+:/::://+//+sssyhyssso///:--::::::--------:::::://///////////++++++ooooo++++++///
::::::::::::::::::::::::::::::::::::::::::::---:::::::::::::::::::::::-------:::smmooysoyy++///++osssshhyydmNNNmNNNmmm+/::---://///ossssssso////--:::::::--------:::::://///////////++++++ooooo+++++++//
:::::::::::::::::::::::------::::::::::::::----:::::::::::::::::::::::-------:::omNhooo++o++//+++ooyhhysyhdmNNNNNNNNmmo/:----:////://+ooo+////+/--:::::::--------::::::////////////++++++++o++++++++++//
::::::::::::::::::::::::-------:::::::::::-----:::::::::::::::::::::::--------:-+dNNyooo+++++++oyhdhssyhhdmNNNNNNNNmmm+:----::///++++++++++++++/--:::::::--------::::::////////////++++++++++++++++++++/
::::::::::::::::::::::::::-----::::::::::------::::::::::::::::::::::----------:oyNNNyooo++oshddhysssyhhdmNNNNNNNNNNmm/:----::/+++oooooooooooo+/:::::::::--------::::::////////////++++++++++++++++++++/
:::::::::::::::::::::::::::----:::::::::-------:::::::::::::::::::::::---------:oyNNNmhyhhdddhyssssyyhdmmmNNNNNNNNNNmm/------:///////++++++++/:::::::::::--------::::::///////////+++++++++++++++++++++/
::::::::::::::::::::::::::::---::::::::--------:::::::::////::::::::::---------:/ymNNNNmhyyyssssssyyhdmmmmmmNNNNNNNmmd:----------::::::::::::::::::::::::---------::::////////////+++++++++++++++++++++/
:::::::::::::::::::::::::::::::::::::::--------:::::://////:::::::::::---------:/smmNNNNNdysssssyyhhdddddmmmNmNNNNmmmm:-------------------:::::::::::::::--------:::::////////////+++++++++++++++++++++/
:::::::::::::::::::::::::::::::::::::::--------::::///////////:::::::::--------:/ommNNNNNNNdhhhyyyyyyyhddmmmNmNNNNmmmm/-------------------::::::::::::::/:-------:::::////////////+++++++++++++++++++++/
:::::::::::::::::::::::::::::::::::::::--------:::////////////::::::::::-------:/oNmNNNNNNNNmNNhysssyyhhdmmmNmNNNNmmmmo--------------------:::::::::::://:-------::::://///////////++++++++++++++++++++/
:::::::::::::::::::::::::::::::::::::::--------:://///////////:/::/::::::------:/oNmNNmmNNNNmNNdyssssyyhddmmmNNNNNNmmmdo/:-----------------:::::::::::://::------::::://////////////++++++++++++++++++//
:::::::::::::::::::::::::::::::::::::::--------:////////////////////::::::::---//+NmNdmmNNNNdmNmsysssyyhddmmmNNNNNNmmmmdyo/:---------------:::::::::::://::-----:::::://////////////+++++++ooo++++++++//
::::::::::::::::::::::::::::::::::::::::-------://////////////////////:::::::--:/omdNmmNNNNNmNNdoyysssyhhdmmmNNNNNNNmmmmmhhs/---::---------:::::::::::://:::----:::::://////////////++++ooooooooo+++++//
::::::::::::::::::::::::::::::::::::::::-------://////////////////+/////:::::::::ohmNmdmNNNNNNNdyhhyssyyhdmmmNNNNNNNmmddmmdhy+:-:/:--------:::::::::::////::----::::::////////////++++ooooooooooooo++++/
:::::::::::::::::::::::::::::::::::::::--------://///////////++++++++/////:::::/:+ydNdmmNNNNNNNmdddhyyyyhdmdmNNNNNNmmmhyyddmdd+-:+:--------:::::::::://///:::----:::::///////////++++oooosssssssooooo+++
::::::::::::::::::::::::::::::::::::::::-------:////////////++++++++++/////::::/:/shNdmNmNNNNNNddddhhyyyyhddmNNNNNNNmdyo++ooyddo++-----:::::::::///////++/:::---:::::://///////++++ooosssssssssssssoooo+
:::::::::::::::::::::::::::::::::::::::::------:////////////++++++++++//////:::::/+omdhNmNNNNNNdhyhhhhhyyhddmNNNNNNNNdho+///:/sdh/:-:::::::::::////////++/::::::::::::////////++++ooossssyyyyyysssssooo+
:::::::::::::::::::::::::::::::::::::::::------:///////////++++++++++++//////::://:omdsdNmNNNNmdyyyyyyhhhhhdmNNNNNNNmdhs+///+/:+ds::::::::::://///////+++//:::::::::://///////+++ooossssyyyyyyyyyssssooo
:::::::::::::::::::::::::::::::::::::::::------://////////++++++++++++++//////::::/oddoymdNNNNmdyyyyyyyyhdhddmNNNNNNNdhso+//+o/:sd+::::::::///////////+++//::::::::://////////+++ooosssyyyyyyyyyyssssooo
:::::::::::::::::::::::::::::::::::::::::------://////////++++++++++++++++/////:::/oyd/hmhNNmmmdyyyyyyyyyhhddmNNNNNNmhyso++++o+/+ms::::::::///////////+++//:::::::::://///////+++ooossssyyyyyyyyysssooo+
:::::::::::::::::::::::::::::::::::::::::------://////////+++++++++++++++++/////:::/+d+ddyNNmmmdhyyssssyyyydmmNNNNNNmhyso++++os++dy/::::::////////////+++//:::::::::://////////+++ooossssyyyyyyssssoooo+
:::::::::::::::::::::::::::::::::::::::::------:////////++++++++++++++++++++////::::+hodmymmydmdhyysssssyhhdmdNNNmmNdyysooo+oosssmy/::::::///////////++++/:::::::::::://////////+++ooossssssssssssooo+++
::::::::::::::::::::::::::::::::::::::::::-----://////++o++++++++++++++++++++/////::/oohmymmshdhhssssssssyddddNNmhhmdyhssooooooyyhs/:::::://////////+++++/::::---:::::://////////++++oooossssssooooo+++/
::::::::::::::::::::::::::::::::::::::::::-----://///+ossss+++++++++++++++++++////////+odddhyyyyysossssssyddhdmNmhydhhhyyssssooooso:::::///////////++++oo/:::-----:::::////////////++++oooooooooo+++++//
::::::::::::::::::::::::::::::::::::::::::-----/++++osyysoo++++++ooo+++++++++++++///////odddssss+oooooossyhhymdNmyyhyyhhyyssoo+///////////////////++++ooo/::------::::://///////////+++++++o+++++++++///
::::::::::::::::::::::::::::::::::::::::::-----/sssssoooo++++++ooooo+++++++++++++++//+///+hd+ooyo+ossssssyyyhdmmmysyyssysyyso+++/:/+///////////++++++oooo:::------:::::///////////++++++++++++++++++++++
:::::::::::::::::::::::::::::::::::::::::------/+++++oooo++++++ooooooo++++++++++++++++////+hoosssooosssyyyhyyhmhdhyssos+/osssooo+oss+////////++++++++oooo:::------::::///////+++++++++++++++++++++++++++
::::::::::::::::::::::::::::::::::::::::-------/oooooooo+++++oooooooooooooooo++++++++++////oyossssssoyyhdddoshhyhyhsyhh////+oyyyyyyso//////+++++++++oooso::-------:::://///+++++++++++++oooooooooooooooo
::::::::::::::::::::::::::::::::::::::::-------/ooooo++++++++ooooooooooooooooo+++++++o++++++sossssssssshddyosyoosooohmh//////hddhyyy+////+++++++++++oooso::-------:::://///+++++++++++oooooooooooooooooo
::::::::::::::::::::::::::::::::::::::::-------/+++++++++++++ooooooooooooooooooooooo+oo++++oossssssssysydhsoooooo+o+hmh//////yhyyyyo/////++++++++++ooosyo::-------::::://////++++++++++++++++oooooooooo+
::::::::::::::::::::::::::::::::::::::::-------/+++++++++++++ooooooooooooooooooooooooooooooossyyssssyyyyhhooooooooo+hmy/+++//hhysyy+////++++++++oooooosyo:---------::::://////////++++++++++++++++++++++
::::::::::::::::::::::::::::::::::::::::-------/+++++++++++++ooooooooooooooooooooooossssssssyhddddhhhyyhhyoooooooooodmy++++++hyssys///+++++++++oooooossyo:----------::::::::////////////////////////////
:::::::::::::::::::::::::::::::::::::::::------/++++++++++++oooooooooooooooooosssssssyssssydmmmmmmmmhyhdhddhhhyyysssdmy+++++ohsosyo++++++++ooooooooosssys:-----------:::::::::::::::::::::://///////////
:::::::::::::::::::::::::::::::::::::::::------/++++++++++++oooooooooooossssssssssyyyyysydmmmmmmmmddhhhdhyyyyyyyyyyydmhyyssoyyssyy++++++ooooooooooosssyys:----------------::::::::::::::::::::::::::::::
::::::::::////////::::::::::::::::::::::::-----/++++++++++++oooooooosssssssssssyyyyhhhhdmmmmddhyyssyhyyhhssssssooooodNs+oosydsosyyyyssooooooooooooosssyhs:----------------------------::::::::::::::::::
::::::://///////////::::::::::::::::::::::-----/++++++++++oooooooooosssssssssyyyhhhddmmmmdyyssssssshhyhhhyssssoooossdmyo+++shsossyddmmmmdddhhhyyyssssyyhs:--------------------------------------::::::::
::::////////////////:::::::::::::::::::::::----/++++++++++ooooooososssyyyyyyhhhhdddmmmdysssssssyyyhhhhddhhyysssoosssyyysssshysoss//oyddmmmmmmmmmmmmysyhhs:----------------------------------------::::::
::///////////////////:::::::::::::::::::::::---/+++++++++ooooooosssssyyyyyhhhdddmmmmdysssyyyyhhyyyyyhhhyyyyyssssssssyysssyhhyyyso/////oydmmmmmmmmmdyyyhhs::---------------------------------------::::::
///////////////////////:::::::::::::::::::::::-/++++++ooooooooosssssyyyyoosyhddmmmmhsssyhhhhhhddhyhhyyhhhyyyysssssyyyssssydhsssss+//////+ymmmmmmmmhyyhhds::----------------------------------------:::::
///////////////////////::::::::::::::::::::::::/oooooooooooooosssssyyyho///++o+osssossydddhdddhyhdddyhdhhhhyyyyyhhyyhhhsssyyssssoo+///////+dmmmmmmhyyhdds:::---------------------------------------:::::
////////////////////////:::::::::::::::::::::::/oooooooooooooosssyyyhhh///+++o+o+++/oo++ooshddyhddhyyhhhmmhyyyhdhhyysssssysoysososo+///////+dmmmmmhyhhdds//::---------------------------------------::::
//////////////////////////:::::::::::::::::::::/ooooooooooosssssyyyhhho/o++ossso+//+oo+////dmhhhyyhdhhyhdhyyyyyyyssssshhhssyhosysoo+////////ommmmmyyhddds+//:::-------------------------------------::::
///////////////////////////////////::::::::::::/oooooooosssssssyyyhhdh//os+sos++o/+sso////ohhhyyyydmhhyyyyyysyhdhysyyysosyyhsoydhso++////////dmmmdhhhddhsoo+//:::-----------------------------------::::
/////////////////////////////////////::::::::::+oooooosssssssyyyhhhdms/+oooooooosooo++o+//yyyyyyyymmhyyyyyyshddhyysosyysyysyooosdyso++///////dmmmdhhddmhsyso++//:::---------------------------------::::
///////////////////////////////////////::::::::+ooosssssssyyyyhhhdmNm+soo++o+++ooooo++o+/+yyyyyyysyyssssssshhyssssshddyyshdhsooohhh++++//+//smmmmmmmmmmyshyyso++//:::-------------------------------::::
/////////////////////////////////////////::::::+ssssssssyyyyhhhdmNNNs+++o+ooosysss+o+++//syyysssssooooooooossssssshdhysshdysoo+odho++++/+//ommmmmmNNNNmysdhhysso++//:::-----------------------------::::
///////////////////////////////////////////::::+sssssssyyyhhhdmNNNNm+++ooooo+so++ooosos/+yyyyssssoooooooooooooososmdsooohyo++++os++++++//+smmmmmmmNNNNmyyddhhyysso++/::::----:::--------------------::::
/////////////////////////////////////////////::+sssyhhhyyyyhhdmmmmmmmmddhhyssyossyoso+++syysysssssssssooooooosoooossooooooooooooooooooo+ohmmmmmmmmmmNNmdhddddhhyysoo+//:::::::::::-----------------:::::""");
	
	
	
def gunArt():
    print(""" _                                                                    
|_t+.__________________......_  /;_                                   
;________________/     :    \ t""o.\__   
:---|------------------t-----^-`--'  /      
 \__L___________________\____________\                                
              ""-. o .--. \--'/  l  .-t+.                             
                  \ (   l) ;""   : /                                  
                   l `--" o;      Y         
                    """""";:  .-. :\                                  
                          ::  '-'  ;\                                 
                           ;;      : ;                                
                           :: bug   ;|                                
                           ;'-------';                                
                           '"------"" """);
#create the Main Menu of the game
def mainMenu():
    #clear the screen
    os.system(clear);

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
    if userInput == '420':
        print('Blaze It');
        time.sleep(4);
        mainMenu();
    if userInput == 'gun':
        gunArt();
        time.sleep(5);
        mainMenu();
    if userInput == 'momo':
        momo();
        time.sleep(10);
        mainMenu();
    if userInput == 'res':
        print('resarting...');
        time.sleep(1);
        dis();
	
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
