import re

import os

def clear():
    """
    Clears  the console screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
# The function below is called whenever the program reaches the payment method stage.    
def payment_method(): #it displays payment method options when called and prompts user to choose a payment method
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Choose Payment Method:\n1. Main Account \n2. Airtel Money\n0 Return to home menu")
    option_pm = input()
    if option_pm == "1":
        pm_main_account()
    elif option_pm == "2":
        pm_airtel_money()
    elif option_pm == "0":
        print(home_menu)
    else:
        print("Invalid request")
        payment_method()


def pm_main_account(): # payment option 1 
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print(
        "Your transaction is being processed. You will receive a confirmation SMS soon. For the vest transaction experience use My Airtel App\n1) Download The App\n00 Back")
    selection = input()
    if selection == "1":
        print("Airtel Message")
        print("")
        print("Thank you. You will soon receive the link via text message")
    elif selection == "00":
        payment_method()
    else:
        pm_main_account()


def pm_airtel_money(): #payment method option 2
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Enter PIN")
    pin = input()
    str_pin = str(pin)
    if len(str_pin) == 4:
        print("Your transaction is being processed. You will receive a confirmation SMS soon. For the vest transaction experience use My Airtel App\n1) Download The App\n00 Back")
        selection = input()
        if selection == "1":
            print("Airtel Message")
            print("")
            print("Thank you. You will soon receive the link via text message")
        elif selection == "00":
            payment_method()
    else:
        print("Dear Customer you have enter the wrong PIN. If you enter the wrong PIN 5 times your account will be blocked")

#The lines of code below is for the Ikali-Data and Voice option 1 in the main menu (home menu) 
def home_menu_opt1(): 
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("1. K2=12 Min Allnet, 24Hrs\n2. K5=45 Airtel Min,24Hrs\n3. K10=75 Airtel Min,7Days 40sms\n4. K3=240MB,24Hrs\n5. K5=3GB,1Hrs\n6. K6=600MB,7Days\n7. K10=2GB,7Days")
    selection = input()
    if selection in ['1', '2', '3', '4', '5', '6' , '7',]:
        payment_method()
    else:
        print("Invalid request")
        print("Select:")
        home_menu_opt1()
    
    #The Ikali-Data and Voice option 1 ends here

#The lines of code below is the Soche Pack option 2 on the home menu or main menu

def daily_soche_pack():  #Option 2.1 For 24hours Daily Pack
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press:\n1. K2=9Min+100SMS\n2. K5=36Min+20MB+250SMS\n3. K10=90Min+50MB+500SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid Input")
        daily_soche_pack()

#Option 2.2 Weekly Pack
def weekly_soche_pack():  # the function is used when the program reaches a stage where the user selects Weekly Airtel Soche Pack in the Soche Pack options
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press:\n1. K20=180Min+100MB+500SMS\n2. K10=65Min+75MB+200SMS\n3. K5=20Min+100SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid Input")
        weekly_soche_pack()

#Option 2.3 Monthly Soche Pack
def monthly_soche_pack():  # the function is used when the program reaches a stage where
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press:\n1. K50=300Min+500MB+500SMS\n2. K100=800Min+1GB+1000SMS\n3. K200=200Min+3GB+2000SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid Input")
        monthly_soche_pack()

#The function below is used to validate a phone number that a user to promoted to enter an choosing option 4(Buy for others) in the Soche Pack options
#option 2.4
def number():
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        buy_for_others_soche()
    else:
        print("Dear customer the number you entered is not an Airtel number")

#After the phone number is validated the function belows displays options of Soche Pack, Buy for others (option 2.4) and prompts user to choose desired option
def buy_for_others_soche():
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("1. 24Hrs Daily pack\n2. Weekly Pack\n3. Monthly Pack\n0 Return to Home menu")
    selection = input()
    if selection == "1":
        daily_soche_pack()
    elif selection == "2":
        weekly_soche_pack()
    elif selection == "3":
        monthly_soche_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid Input\n Select:")
        buy_for_others_soche()

#option 2(Soche Pack) displays options available and prompts a user to select an option
def home_menu_opt2():  # Airtel Soche Pack
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("1. For 24Hrs Daily Pack\n2. For Weekly Pack\n3. For Monthly Pack\n4. Buy for Other\n0 Return to home menu")
    selection = input()
    if selection == "1":   #if option 1 is selected then the user proceeds to the next stage 24hrs Daily pack
        daily_soche_pack() #by calling option 2.1 
    elif selection == "2":
        weekly_soche_pack()
    elif selection == "3": 
        monthly_soche_pack()
    elif selection == "4":
        number()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request\n Select:")
        home_menu_opt2()


#Soche Pack ends here

#The lines of code below is for All networks Soche option 3

#option 3.1 (For the 24hours Daily Pack)
def daily_allnetworks_pack():  ##this function is called when a user is selects the option 1 in the All networks soche
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press:\n1. K2=7Min+100SMS\n2. K5=26Min+20MB+250SMS\n3. K10=60Min+50MB+250SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        daily_allnetworks_pack()

#option 3.2 (For Weekly Pack)
def weekly_allnetworks_pack(): #this function is called when a user selects option 2 in the All networks Soche
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press\n1. K50=350Min+250MB+500SMS\n2. K20=120Min+100MB+500SMS\n3. K10=45Min+75MB+200SMS\n4. K5=14Min+100SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid option")
        weekly_allnetworks_pack()

#option 3.3 (For Monthly Pack)
def monthly_allnetworks_pack():   #this function is called when a user selects option 3 in the All networks Soche
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press:\n1. K50=200Mins+500MB+500SMS\n2. K100=500Min+1GB+1000SMS\n3. K200=1200mins+3GB+2000SMS\n0 Return to home menu")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        monthly_allnetworks_pack()

#option 3.4 (Buy for Other)
def mobile_number_all(): #this function prompts user to enter a phone number and it validates the number
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        buy_for_others_allnetworks()
    else:
        print("Dear customer the number you entered is not an Airtel number")

#After the number is validated the function belows displays options of the All networks buy for other and it prompts the user to select an option
def buy_for_others_allnetworks():
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("1. 24Hrs Daily pack\n2. Weekly Pack\n3. Monthly Pack\n0 Return to Home menu")
    selection = input()
    if selection == "1":
        daily_allnetworks_pack()
    elif selection == "2":
        weekly_allnetworks_pack()
    elif selection == "3":
        monthly_allnetworks_pack()
    else:
        print("Invalid Input\n Select:")
        buy_for_others_allnetworks()

#option 3 (All networks Soche)
def home_menu_opt3():  #displays options of the all network soche and calls a specific function that is defined above according to which option the user selects
    clear() #it clears the function from the terminal when the functions purpose has been processed
    print("Press\n1. For 24Hrs Daily Pack\n2. For Weekly Pack\n3. For Monthly Pack\n4. Buy for Other\n0 Return to home menu")
    selection = input()
    if selection == "1":
        daily_allnetworks_pack()
    elif selection == "2":
        weekly_allnetworks_pack()
    elif selection == "3":
        monthly_allnetworks_pack()
    elif selection == "4":
        buy_for_others_allnetworks()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        home_menu_opt3()

#All networks Soche ends here

#OPTION 4 

def daily_tonse_bundle():  # Daily tonse
    clear()
    print("1. 100MB 24hrs-K2.0\n2. 350MB 24hrs-K5.0\n3. 1.2GB + 300MB Airtel TV Bundle-k10.0")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        daily_tonse_bundle()


def weekly_tonse_bundle():  # weekly tonse bundles
    clear()
    print("1. 800MB-K10.0")
    print("2. 2GB-K20.0")
    print("3. 6GB + 1.5GB Airtel TV Bundle-K50.0")
    if selection in ['1', '2', '3']:
        payment_method()
    else:
        print("Invalid request")
        weekly_tonse_bundle()


def monthly_tonse_bundle():  ##monthly tonse bundle
    clear()
    print("1. 5GB-K60.0\n2. 10GB-K100.0\n3. 25GB +5GB Airtel TV Bundle-K200.0\n4. 80GB-K400.0")
    selection = input()
    if selection in ['1', '2', '3', '4']:
        payment_method()
    else:
        print("Invalid request")
        monthly_tonse_bundle()


def tonse_days60or90():  # 60 or 90
    clear()
    print("60 or 90 Days bundles. Please select:")
    print("1. 35GB 60days-K700,0\n2. 50GB 90days-K900.0\n3. 100GB 90days-K1,500.0")
    selection = input()
    if selection in ['1', '2', '3']:
        payment_method()
    else:
        print("Invalid request")
        tonse_days60or90()


def tonse_days90():  # 90 tonse
    clear()
    print(
        "Please select:\n2. 1.5GB 90days-K100\n2. 5GB 90days-K200\n3. 12GB 90days-K350\n4. 25GB 90days-K7OO\n5. 35GB 90days-K850")
    if selection in ['1', '2', '3', '4', '5']:
        payment_method()
    else:
        print("Invalid request")
        tonse_days90()


def tonse_days180():  # this function dip
    clear()
    print("Please select:\n1. 1.5GB 180days-K150")
    print("2. 5GB 180days-K300")
    print("3. 12GB 180days-K600")
    print("4. 25GB 180days- k1,200")
    print("5. 35GB 180days-K2,100")
    print("6. 50GB 180days-K2,700")
    print("7. 100GB 180days-K4,500")
    if selection in ['1', '2', '3', '4', '5', '6', '7']:
        payment_method()
    else:
        print("Invalid request")
        tonse_days180()


def tonse_days360():
    clear()
    print("Please select:\n1. 1.5GB 365days-K200")
    print("2. 5GB 365days-K400")
    print("3. 12GB 365days-K800")
    print("4. 25GB 365days- k1,600")
    print("5. 35GB 365days-K2,800")
    print("6. 50GB 365days-K3,600")
    if selection in ['1', '2', '3', '4', '5', '6']:
        payment_method()
    else:
        print("Invalid request")
        tonse_days360()


def tonse_days90to360():
    clear()
    print("90 to 360 days bundles. Please select:\n1. 90 days bundles\n2. 180 days bundles\n3. 365 days bundles")
    selection = input()
    if selection == "1":
        tonse_days90()
    elif selection == "2":
        tonse_days180()
    elif selection == "3":
        tonse_days360()
    else:
        print("Invalid option")
        tonse_days90to360()


def tonse_no_expiry():
    clear()
    print("No expiry bundles. Please Select:\n1. 1GB-K90.0\n2. 2.5GB-K200.0\n3. 5.5GB-K400.0")
    selection = input()
    if selection == "1":
        print("You have selected 1GB bundle for K90. Please select:\n1. For Auto Renewal\n2. For Once Off\n3. Cancel")
        selection = input()
        if selection == "1":
            print("Invalid(empty)response")
        elif selection == "2":
            payment_method()
        elif selection == "3":
            print("Invalid (empty) Response")
    elif selection == "2":
        print("You have selected 2.5GB for K200. Please select:\n1. For Auto Renewal\n2. For Once Off\n3. Cancel")
        selection = input()
        if selection == "1":
            print("Invalid(empty)response")
        elif selection == "2":
            payment_method()
        elif selection == "3":
            print("Invalid (empty) Response")

#function containing the main menu offers
def tonse_internet_bundles():
    clear()
    print("1. Daily")
    print("2. Weekly")
    print("3. Monthly")
    print("4. 60 OR 90 Days")
    print("5.90 to 365 Days")
    print("6. No expiry bundles")
    selection = input()
    if selection == "1":
        daily_tonse_bundle()
    elif selection == "2":
        weekly_tonse_bundle()
    elif selection == "3":
        monthly_tonse_bundle()
    elif selection == "4":
        tonse_days60or90()
    elif selection == "5":
        tonse_days90to360()
    elif selection == "6":
        tonse_no_expiry()

#buy for others 
def mobile_for_others():  # this function is used when the program reaches the stage where the user decides to purchase data for another user this function is then called
    clear()
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        data_buy_for_others()
    else:
        print("Dear customer the number you entered is not an Airtel number")


def data_buy_for_others():
    clear()
    print("Please select a bundle type:\n1. Internet")
    selection = input()
    if selection == "1":
        tonse_internet_bundles()
    else:
        print("Invalid request ")
        data_buy_for_others()


def check_balance():
    clear()
    print("Balance/ validity check. Please select")
    print("1. Internet bundle\n2. Ikali\n3. No expiry bundle\n4. Hybrid Bundle")
    selection = input()
    if selection == "1":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    elif selection == "2":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    elif selection == "3":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    elif selection == "4":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    else:
        print("Invalid request")
        check_balance()


def night_Data():
    clear()
    print("Night Data Pack, 1.5GB at K5")
    print("1. buy")
    selection = input()
    if selection == "1":
        payment_method()
    else:
        print("Invalid request")
        night_Data()


def auto_cancel_renew():
    clear()
    print("To cancel auto renewal. Please select:\n1. Internet bundle")
    selection = input()
    if selection == "1":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    else:
        print("Invalid request")
        auto_cancel_renew()

#option 4 main menu
def home_menu_opt4():
    clear()
    print("1. Ikali - Data and Voice\n2. Tonse Internet Bundles\n3. Buy for Others\n4. Check Balance\n5. Night Data\n6. Cancel auto renewal")
    selection = input()
    if selection == "1":
        home_menu_opt1()
    elif selection == "2":
        tonse_internet_bundles()
    elif selection == "3":
        mobile_for_others()
    elif selection == "4":
        check_balance()
    elif selection == "5":
        night_Data()
    elif selection == "6":
        auto_cancel_renew()
    else:
        print("Invalid request")
        home_menu_opt4()



#THE LINES OF CODE BELOW ARE FOR OPTION 5
def daily_pack():
    clear()
    print(
        "Press:\n1. K2=9Min+100SMS\n2, K5=34Min_20MB+250SMS\n3. K10=90Min+50MB+500SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        airtel_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        daily_pack()


def weekly_pack():
    clear()
    print(
        "Press:\n1. K20=180Min+100MB+500SMS\n2. K10=65Min+75MB+200SMS\n3. K5=20Min+100SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        airtel_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        weekly_pack()


def monthly_pack():
    clear()
    print(
        "Press:\n1. K50=300Min+500MB+500SMS\n2. K100=800Min+1GB+1000SMS\n3. K200=200Min+3GB+2000SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        airtel_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        monthly_pack()


def airtel_pack():
    clear()
    print("Press:\n1. 24Hrs Daily pack\n2. Weekly Pack\n3. Monthly Pack\n0 Return to Home menu\n* Back\n# Home")
    selection = input()
    if selection == "1":
        daily_pack()
    elif selection == "2":
        weekly_pack()
    elif selection == "3":
        monthly_pack()
    elif selection == "0":
        home_menu()
    elif selection == "*":
        home_menu_opt5_menu()
    elif selection == "#":
        home_menu_opt5_menu()
    else:
        print("Invalid Input\n Select:")
        airtel_pack()


def allnetwork_daily_pack():
    clear()
    print(
        "Press:\n1. K2=7Min+100SMS\n2, K5=26Min_20MB+250SMS\n3. K10=60Min+50MB+500SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        allnetwork_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        allnetwork_daily_pack()


def allnetwork_weekly_pack():
    clear()
    print(
        "Press:\n1. K50=350Min+250MB+500SMS\n2. K20=129Min+100MB+500SMS\n3. K10=45Min+75MB+200SMS\n4. K5=14Min+75MB+200SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "4":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        allnetwork_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        allnetwork_pack()


def allnetwork_monthly_pack():
    clear()
    print(
        "Press:\n1. K50=200Min+500MB+500SMS\n2. K100=800Min+1GB+1000SMS\n3. K200=200Min+3GB+2000SMS\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        allnetwork_pack()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        allnetwork_monthly_pack()


def allnetwork_pack():
    clear()
    print("Press:\n1. 24Hrs Daily pack\n2. Weekly Pack\n3. Monthly Pack\n0 Return to Home menu\n* Back\n# Home")
    selection = input()
    if selection == "1":
        allnetwork_daily_pack()
    elif selection == "2":
        allnetwork_weekly_pack()
    elif selection == "3":
        allnetwork_monthly_pack()
    elif selection == "0":
        home_menu()
    elif selection == "*":
        home_menu_opt5_menu()
    elif selection == "#":
        home_menu_opt5_menu()
    else:
        print("Invalid request")
        allnetwork_pack()


def tonse_internet_daily():
    clear()
    print(
        "Press:\n1. 100MB 24hrs-K2.0\n2. 35OMB 24hrs-K5.0\n3. 1.2GB + 300MB Airtel TV Bundle-K10.0\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        tonse_internet()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        tonse_internet_daily()


def tonse_internet_weekly():
    clear()
    print(
        "Press:\n1. 800MB-K10.0\n2. 2GB-K20.0\n3. 6GB + 1.5GB Airtel TV Bundle-K50.0\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        tonse_internet()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        tonse_internet_weekly()


def tonse_internet_monthly():
    clear()
    print(
        "Press:\n1. 5GB-K60.0\n2. 1OGB-K100.0\n3. 25GB + 5GB Airtel TV Bundle-K200.0\n# Home\n* Back\n0 Return to main menu")
    selection = input()
    if selection == "1":
        payment_method()
    elif selection == "2":
        payment_method()
    elif selection == "3":
        payment_method()
    elif selection == "#":
        home_menu_opt5_menu()
    elif selection == "*":
        tonse_internet()
    elif selection == "0":
        home_menu()
    else:
        print("Invalid request")
        tonse_internet_monthly()


def tonse_internet():
    clear()
    print("Press:\n1. Daily\n2. Weekly\n3. Monthly\n# Home\n* Back\n0 Return to main menu")
    opt_tonse = input()
    if opt_tonse == "1":
        tonse_internet_daily()
    elif opt_tonse == "2":
        tonse_internet_weekly()
    elif opt_tonse == "3":
        tonse_internet_monthly()
    elif opt_tonse == "#":
        home_menu_opt5_menu()
    elif opt_tonse == "*":
        home_menu_opt5_menu()
    elif opt_tonse == "0":
        home_menu()
    else:
        print("Invalid request")
        tonse_internet()


def nightpack():
    clear()
    print("Please choose payment method. Press:\n1. Main\n2 Airtel Money\n# Home\n* Back\n0 Return to main menu")
    selecion = input()
    if selecion == "1":
        pm_main_account()
    elif selecion == "2":
        pm_airtel_money()
    elif selecion == "#":
        home_menu_opt5_menu()
    elif selecion == "*":
        home_menu_opt5_menu()
    elif selecion == "0":
        home_menu()
    else:
        print("Invalid request")
        nightpack()


def home_menu_opt5_menu():
    clear()
    print("1. Airtel Pack\n2. All network\n3. Tonse Internet Bundles\n4. 1.5GB Night Pack\n0 Return to main menu")
    selection = input()
    if selection == "1":
        airtel_pack()
    elif selection == "2":
        allnetwork_pack()
    elif selection == "3":
        tonse_internet()
    elif selection == "4":
        nightpack()
    elif selection == "0":
        home_menu()


def home_menu_opt5():
    clear()
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        home_menu_opt5_menu()
    else:
        print("Dear customer the number you entered is not an Airtel number")



#OPTION 6
#Balance check
def home_menu_opt6():  # Check balance
    clear()
    print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")

# OPTION 6 ENDS HERE


#OPTION 6 IS BELOW
#Siliza-Airtime Loan
def qualification():
    clear()
    print("To qualify you must have been an active Airtel subscriber for at least 1 month.\n Reply with\n1 to return")
    selection = input()
    if selection == "1":
        for_help()
    else:
        qualification()


def repayment():
    clear()
    print("The advanced amount should be paid back within 48hrs. To repay, please recharge your line.\n1 to return")
    selection = input()
    if selection == "1":
        for_help()
    else:
        repayment()


def for_help(): #if you selection opt 4 in the siliza menu this function is then called into the siliza main menu
    clear()
    print("Reply with:\n1. Qualification\n2. Repayment\n# home menu")
    selection = input()
    if selection == "1":
        qualification()
    elif selection == "2":
        repayment()
    elif selection == "#":
        home_menu_opt7()
    else:
        print("Reply with")
        for_help()


def home_menu_opt7():  # Siliza Airtime Loan: when option 7 on the main menu is selected it calls out this function
    clear()
    print(
        "Reply with:\n1. for Siliza Airtime\n2. for Eligibility Check\n3. for Payment\n4. for Help\n5. for Balance Check")
    selection = input()
    if selection == "4":
        for_help()
    elif selection == "5":
        print(
            "Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    elif selection == "3":
        print("Please Recharge with K0.0000 to full payback your loan.")
    elif selection == "2":
        print("Dear Customer, your request was unsuccessful\n You need to have been on the Airtel Network for a minimum of 30 days or your usage is low.\n Top up more to qualify")
    elif selection == "1":
        print("Dear Customer, your request was unsuccessful\n You need to have been on the Airtel Network for a minimum of 30 days or your usage is low.\n Top up more to qualify")
    else:
        print("Reply with:")

#OPTION 7 ENDS HERE  

#OPTION 9 STARTS BELOW
#INTL voice & Roaming

def main_account():
    clear()
    print("Your transaction is being processed. You will receive a confirmation SMS soon.")


def airtel_money():
    clear()
    print("Enter PIN")
    pin = int(input())
    str_pin = str(pin)
    if len(str_pin) == 4:
        print(
            "Your transaction is being processed. You will receive a confirmation SMS soon. For the vest transaction experience use My Airtel App\n1) Download The App\n00 Back")
        selection = input()
        if selection == "1":
            print("Airtel Message")
            print("")
            print("Thank you. You will soon receive the link via text message")
        elif selection == "00":
            pay_opt()
        else:
            exit
    else:
        print(
            "Dear customer you entered the wrong PIN. If your enter the wrong PIN 5 times your account will be blocked")

########## The lines of code below is for option 9 (INTL voice and roaming) ##################
def pay_opt2():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    selection = input()
    if selection == "00":
        buy_combo_bundles_for_destination_countries_opt2()
    elif selection == "1":
        main_account()
    elif selection == "2":
        airtel_money()
    else:
        pay_opt()


def pay_opt():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    selection = input()
    if selection == "00":
        buy_combo_bundles_for_destination_countries_opt1()
    elif selection == "1":
        main_account()
    elif selection == "2":
        airtel_money()
    else:
        pay_opt()


def buy_combo_bundles_for_destination_countries_opt1():
    clear()
    print("1. Proceed\n2. Cancel\n00 Back")
    selection = input()
    if selection == "00":
        buy_combo_bundles_for_destination_countries()
    elif selection == "1":
        pay_opt()
    elif selection == "2":
        print("Dear Customer, your transaction has been cancelled. Dial *113# for more services")
    else:
        buy_combo_bundles_for_destination_countries_opt1()


def buy_combo_bundles_for_destination_countries_opt2():
    clear()
    print("1. Proceed\n2. Cancel\n00 Back")
    selection = input()
    if selection == "00":
        buy_combo_bundles_for_destination_countries_next()
    elif selection == "1":
        pay_opt()
    elif selection == "2":
        print("Dear Customer, your transaction has been cancelled. Dial *113# for more services")
    else:
        buy_combo_bundles_for_destination_countries_opt2()


def buy_combo_bundles_for_destination_countries_next():
    clear()
    print("1. K225 (30days): Local Call 25Min+Call to Zambia 25Min+Incoming Call 25Min+250MB\n00 Back")
    selection = input()
    if selection == "00":
        buy_bundles_for_destination_countries()
    elif selection == "1":
        buy_combo_bundles_for_destination_countries_opt2()
    else:
        buy_combo_bundles_for_destination_countries_next()


def buy_combo_bundles_for_destination_countries():  # sub function of option 1 in the buy bundles for destination countries
    clear()
    print("Please Select a Bundle:")
    print("1. K110 (30 days): Local Call 10Min+Call to Zambia 10Min+Incoming Call 10Min=100MB\n2. Next\n00 Back")
    selection = input()
    if selection == "00":
        buy_bundles_for_destination_countries()
    elif selection == "1":
        buy_combo_bundles_for_destination_countries_opt1()
    elif selection == "2":
        buy_combo_bundles_for_destination_countries_next()


def dcdb_paymentopts():  # destination countries data bundle payment option when proceed is selected
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    selection = input()
    if selection == "00":
        destination_countries_data_bundles_opt1()
    elif selection == "1":
        main_account()
    elif selection == "2":
        airtel_money()
    else:
        dcdb_paymentopts()


def destination_countries_data_bundles_opt1():
    clear()
    print(
        "You have selected bundle valid for 7 days for K25 to be used on One Airtel Roaming Networks. Please Select:\n1. Proceed\n2. Cancel\n00 Back")
    selection = input()
    if selection == "00":
        destination_countries_data_bundles()
    elif selection == "1":
        dcdb_paymentopts()
    elif selection == "2":
        print("Dear Customer, your transaction has been cancelled. Dial *113# for more services")
    elif selection == "00":
        destination_countries_data_bundles()
    else:
        destination_countries_data_bundles_opt1()


def destination_countries_data_bundles_opt2():
    clear()
    print(
        "You have selected bundle valid for 30 days for K50 to be used on One Airtel Roaming Networks. Please Select:\n1. Proceed\n2. Cancel\n00 Back")
    selection = input()
    if selection == "00":
        destination_countries_data_bundles()
    elif selection == "1":
        dcdb_paymentopts()
    elif selection == "2":
        print("Dear Customer, your transaction has been cancelled. Dial *113# for more services")
    else:
        destination_countries_data_bundles_opt2()


def destination_countries_data_bundles_opt3():
    clear()
    print(
        "You have selected bundle valid for 30 days for K100 to be used on One Airtel Roaming Networks. Please Select:\n1. Proceed\n2. Cancel\n00 Back")
    selection = input()
    if selection == "00":
        destination_countries_data_bundles()
    elif selection == "1":
        dcdb_paymentopts()
    elif selection == "2":
        print("Dear Customer, your transaction has been cancelled. Dial *113# for more services")
    else:
        destination_countries_data_bundles_opt3()


def destination_countries_data_bundles():
    clear()
    print("Please Select a bundle:\n1. K25 (7 days):400MB\n2. K50 (30 days):1GB\n3. K100 (30days):3GB\n00 Back")
    selection = input()
    if selection == "00":
        buy_bundles_for_destination_countries()
    elif selection == "1":
        destination_countries_data_bundles_opt1()
    elif selection == "2":
        destination_countries_data_bundles_opt2()
    elif selection == "3":
        destination_countries_data_bundles_opt3()
    else:
        destination_countries_data_bundles()


def buy_bundles_for_destination_countries():  # opt 2 destination courtiesbuy bundles
    clear()
    print("Please select:\n1. Combo Bundles(In-Call, Out-Call, Data)\n2. Data Bundles\n00 Back")
    selection = input()
    if selection == "00":
        destination_countries()
    elif selection == "1":
        buy_combo_bundles_for_destination_countries()
    elif selection == "2":
        destination_countries_data_bundles()
    else:
        buy_bundles_for_destination_countries()


def buy_combo_bundles_for_destination_countries_next_menu():
    clear()
    print("1. K225 (30days): Local Call 25Min+Call to Zambia 25Min+Incoming Call 25Min+250MB\n00 Back")
    selection = input()
    if selection == "00":
        buy_bundles_for_destination_countries()
    elif selection == "1":
        buy_combo_bundles_for_destination_countries_opt2()
    elif selection == "00":
        buy_combo_bundles_for_destination_countries_menu()
    else:
        print("Invalid request")
        buy_combo_bundles_for_destination_countries_next_menu()


def buy_combo_bundles_for_destination_countries_menu():  # sub function of option 1 in the buy bundles for destination countries
    clear()
    print("Please Select a Bundle:")
    print("1. K110 (30 days): Local Call 10Min+Call to Zambia 10Min+Incoming Call 10Min=100MB\n2. Next\n00 Back")
    selection = input()
    if selection == "00":
        destination_countrie_buy_for_others_menu()
    elif selection == "1":
        buy_combo_bundles_for_destination_countries_opt1()
    elif selection == "2":
        buy_combo_bundles_for_destination_countries_next_menu()
    else:
        print("Invalid request")
        buy_combo_bundles_for_destination_countries_menu()


def destination_countrie_buy_for_others_menu():
    clear()
    print("1. Combo Bundles(In-Call, Out-Call, Data)\n2. Data Bundle\n# Home\n* Back\n00 Back")
    selected = input()
    if selected == "1":
        buy_combo_bundles_for_destination_countries_menu()
    elif selected == "2":
        destination_countries_data_bundles() #Create a function that has the real back option for the data bundle buy for 
    elif selected == "*":
        destination_countrie_buy_for_others()
    elif selected == "#":
        one_airtel_roaming()
    elif selected == "00":
        destination_countries()
    else:
        print("Invalid option")
        destination_countrie_buy_for_others_menu()


def destination_countrie_buy_for_others():
    clear()
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        destination_countrie_buy_for_others_menu()
    else:
        print("Dear customer the number you entered is not an Airtel number")


def destination_countries():  # option calls option 1 int airtel roaming
    clear()
    print("All Airtel Networks in Africa, Airtel India and Emtel Mauritius.\n1. Buy Bundles\n2. Buy for Other\n00 Back")
    selection = input()
    if selection == "1":
        buy_bundles_for_destination_countries()
    elif selection == "00":
        one_airtel_roaming()
    elif selection == "2":
        destination_countrie_buy_for_others()
    elif selection == "00":
        one_airtel_roaming()
    else:
        destination_countries()


def one_airtel_roaming():  # option 1 in the INTL Calling & Roaming options
    clear()
    print("1. Destination Countries\n2. Buy Bundles\n3. Buy for others\n00 Back")
    selection = input()
    if selection == "1":
        destination_countries()
    elif selection == "2":
        buy_bundles_for_destination_countries()
    elif selection == "3":
        destination_countrie_buy_for_others()
    elif selection == "00":
        home_menu_opt8()
    else:
        print("Invalid request")
        one_airtel_roaming()

##option 9.2.2 (global roaming)
def pay_opt1():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    selection = input()
    if selection == "00":
        voice_pay_method1()
    elif selection == "1":
        main_account()
    elif selection == "2":
        airtel_money()
    else:
        print("Invalid request")
        pay_opt1()


def voice_pay_method1():
    clear()
    print("K360(15days):30Min You have selected voice minutes valid for 15 days for K360 to be used on Global Roaming Networks. Please Select:\n1. proceed\n2 Cancel\n00 Back")
    vpay = input()
    if vpay == "1":
        pay_opt1()
    elif vpay == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif vpay == "00":
        global_voice()
    else:
        print("Invalid request")
        voice_pay_method1()


def pay_opt2():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    selection = input()
    if selection == "00":
        voice_pay_method2()
    elif selection == "1":
        main_account()
    elif selection == "2":
        airtel_money()
    else:
        pay_opt2()


def voice_pay_method2():
    clear()
    print(
        "K900(30days):75Min You have selected voice minutes valid for 30 days for K900 to be used on Global Roaming Networks. Please Select:\n1. proceed\n2 Cancel\n00 Back")
    vpay = input()
    if vpay == "1":
        pay_opt2()
    elif vpay == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif vpay == "00":
        global_voice()
    else:
        print("Invalid request")


def global_voice():
    clear()
    print("Incoming call, Local Call, Call to Zambia\n1. K360(15days):30Min\n2. K900(30days):75Min\n00 Back")
    voice = input()
    if voice == "1":
        voice_pay_method1()
    elif voice == "2":
        voice_pay_method2()
    elif voice == "00":
        global_roaming()
    else:
        print("global_voice")


def bundle_payment():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    pytm = input()
    if pytm == "00":
        bundle_pay1()
    elif pytm == "1":
        print(
            "Dear Customer your transaction is being processed. You will receive a confirmation text Message once the transaction is processed")
    elif pytm == "2":
        airtel_money()
    else:
        print("Invalid request")


def bundle_pay1():
    clear()
    print("1. Proceed\n2. Cancel\n00 Back")
    payj = input()
    if payj == "00":
        global_bundle()
    elif payj == "1":
        bundle_payment()
    elif payj == "2":
        print("Dear customer your transaction has been cancelled")
    else:
        print("Invalid request")
        bundle_pay1()


def bundle_payment2():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    pytm = input()
    if pytm == "00":
        bundle_pay2()
    elif pytm == "1":
        print(
            "Dear Customer your transaction is being processed. You will receive a confirmation text Message once the transaction is processed")
    elif pytm == "2":
        airtel_money()
    else:
        print("Invalid request")
        bundle_payment2()


def bundle_pay2():
    clear()
    print("1. Proceed\n2. Cancel\n00 Back")
    payj = input()
    if payj == "00":
        global_bundle()
    elif payj == "1":
        bundle_payment2()
    elif payj == "2":
        print("Dear customer your transaction has been cancelled")
    else:
        print("Invalid request")
        bundle_pay2()


def global_bundle():
    clear()
    print("Please Select a bundle:\n1. K360(15days):1.GB\n2. K900(30days):3.GB\n00 Back")
    bundle = input()
    if bundle == "1":
        bundle_pay1()
    elif bundle == "2":
        bundle_pay2()
    elif bundle == "00":
        buy_bundles_glo()
    else:
        print("Invalid request")
        global_bundle()

#option 9.2.2 (Buy bundles)
def buy_bundles_glo():
    clear()
    print("1. Voice\n2. Data Bundles\n00 Back")
    selected = input()
    if selected == "00":
        global_roaming()
    elif selected == "1":
        global_voice()
    elif selected == "2":
        global_bundle()
    else:
        print("Invalid request")
        buy_bundles_glo()


def global_buy_voice_opt1_proceed():
    clear()
    print("1. Main Account\n2. Airtel Money\n# Home\n* Back\n00 Back")
    buy = input()
    if buy == "1":
        print("Dear Customer, your transaction is being processed you will receive a confirmation text message shortly")
    elif buy == "#":
        global_buy_for_other()
    elif buy == "*":
        global_buy_voice_opt1()
    elif buy == "00":
        global_buy_for_other_menu()
    elif buy == "2":
        airtel_money()
    else:
        print("Invalid request")
        global_buy_voice_opt1_proceed()


def global_buy_voice_opt1():
    clear()
    print("You have chosen to purchase a ZMW360 Voice Roaming bundle. Select:\n1. proceed\n2. cancel\n# Home\n* Back\n00 Back")
    selection = input()
    if selection == "1":
        global_buy_voice_opt1_proceed()
    elif selection == "2":
        print("Dear Customer yor transaction has been cancelled")
    elif selection == "*":
        global_buy_voice()
    elif selection == "#":
        global_buy_for_other_menu()
    elif selection == "00":
        global_roaming()
    else:
        print("Invalid request")
        global_buy_voice_opt1()


def global_buy_voice_opt2_proceed():
    clear()
    print("1. Main Account\n2. Airtel Money\n# Home\n* Back\n00 Back")
    buy = input()
    if buy == "1":
        print("Dear Customer, your transaction is being processed you will receive a confirmation text message shortly")
    elif buy == "#":
        global_buy_for_other()
    elif buy == "*":
        global_buy_voice_opt2()
    elif buy == "00":
        global_buy_for_other_menu()
    elif buy == "2":
        airtel_money()
    else:
        print("Invalid request")
        global_buy_voice_opt2_proceed()


def global_buy_voice_opt2():
    clear()
    print("You have chosen to purchase a ZMW900 Voice Roaming bundle. Select:\n1. proceed\n2. cancel\n# Home\n* Back\n00 Back")
    selection = input()
    if selection == "1":
        global_buy_voice_opt2_proceed()
    elif selection == "2":
        print("Dear Customer yor transaction has been cancelled")
    elif selection == "*":
        global_buy_voice()
    elif selection == "#":
        global_buy_for_other_menu()
    elif selection == "00":
        global_roaming()
    else:
        print("Invalid request")
        global_buy_voice_opt2()


def global_buy_voice():
    clear()
    print("Incoming call, Local Call, Call Zambia\n1. K360(15days):30Min\n2. K900(30days):75Min\n# Home\n* Back\n00 Back")
    gbv = input()
    if gbv == "*":
        global_buy_for_other_menu()
    elif gbv == "#":
        global_buy_for_other()
    elif gbv == "00":
        global_roaming()
    elif gbv == "1":
        global_buy_voice_opt1()
    elif gbv == "2":
        global_buy_voice_opt2()
    else:
        print("Invalid request")
        global_buy_voice()

#option n.9.2.2 (Buy for other options)
def global_buy_for_other_menu():
    clear()
    print("1. Voice\n2. Data Bundles\n# Home\n* Back\n00 Back")
    select = input()
    if select == "1":
        global_buy_voice()
    elif select == "#":
        global_buy_for_other()
    elif select == "*":
        global_buy_for_other()
    elif select == "00":
        global_roaming()
    elif select == "2":
        global_bundle()
    else:
        print("Invalid request")
        global_buy_for_other_menu()

#option n.9.2.2 (Buy for other)
def global_buy_for_other(): #prompts users to enter a phone number and it is validated. if the number was correct it displays the option bt calling the above function
    clear()
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)\n00")
    pattern = r'^097\d{7}$|^077\d{7}$'
    select = input()
    if re.match(pattern, select):
        global_buy_for_other_menu()
    elif select == "00":
        global_roaming()
    else:
        print("Dear customer the number you entered is not an Airtel number")

#option n.9.2 (Global Roaming)
def global_roaming():
    clear()
    print("Please Select:\n1. Destination Countries\n2. Buy Bundles\n3. Buy for Others\n00 Back")
    selection = input()
    if selection == "1":
        print("Dear Customer, Your request has been successfully processed")
    elif selection == "2":
        buy_bundles_glo()
    elif selection == "00":
        home_menu_opt8()
    elif selection == "3":
        global_buy_for_other()
    else:
        print("Invalid request")
        global_roaming()


def int_bundles1_proceed():
    clear()
    print("1. Main Account\n2. Airtel money\n00 Back")
    proceed = input()
    if proceed == "1":
        print("Dear Customer your transaction is being processed. You will receive a confirmation text message ")
    elif proceed == "2":
        airtel_money()
    elif proceed == "0":
        int_bundles1()
    else:
        print("Invalid request")
        int_bundles1()


def int_bundles1():
    clear()
    print("You have selected Zone 1 International Voice Calling Bundle valid for 30 days for K25.Please Select\n1 proceed\n2. cancel\n00 Back")
    select = input()
    if select == "00":
        itn_bundles()
    elif select == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif select == "1":
        int_bundles1_proceed()
    else:
        print("Invalid option")
        int_bundles1()


def int_bundles2_proceed():
    clear()
    print("1. Main Account\n2. Airtel money\n00 Back")
    proceed = input()
    if proceed == "1":
        print("Dear Customer your transaction is being processed. You will receive a confirmation text message ")
    elif proceed == "2":
        airtel_money()
    elif proceed == "0":
        int_bundles2()
    else:
        print("Invalid request")
        int_bundles2_proceed()


def int_bundles2():
    clear()
    print("You have selected Zone 2 International Voice Calling Bundle valid for 30 days for K110.Please Select\n1 proceed\n2. cancel\n00 Back")
    select = input()
    if select == "00":
        itn_bundles()
    elif select == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif select == "1":
        int_bundles2_proceed()
    else:
        print("Invalid request")
        int_bundles2()


def int_bundles_next1_proceed():
    clear()
    print("1. Main Account\n2. Airtel money\n00 Back")
    proceed = input()
    if proceed == "1":
        print("Dear Customer your transaction is being processed. You will receive a confirmation text message ")
    elif proceed == "2":
        airtel_money()
    elif proceed == "00":
        int_bundles_next1()
    else:
        print("Invalid request")
        int_bundles_next1_proceed()


def int_bundles_next1():
    clear()
    print("You have selected Zone 3 International Voice Calling Bundle valid for 30 days for K260.Please Select\n1 proceed\n2. cancel\n00 Back")
    select = input()
    if select == "00":
        itn_bundles_next()
    elif select == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif select == "1":
        int_bundles_next1_proceed()
    else:
        print("Invalid request")
        int_bundles_next1()


def int_bundles_next2_proceed():
    clear()
    print("1. Main Account\n2. Airtel money\n00 Back")
    proceed = input()
    if proceed == "1":
        print("Dear Customer your transaction is being processed. You will receive a confirmation text message ")
    elif proceed == "2":
        airtel_money()
    elif proceed == "0":
        int_bundles_next2()
    else:
        print("Invalid request")
        int_bundles_next2_proceed()


def int_bundles_next2():
    clear()
    print(
        "You have selected Zone 4 International Voice Calling Bundle valid for 30 days for K360.Please Select\n1 proceed\n2. cancel\n00 Back")
    select = input()
    if select == "00":
        itn_bundles_next()
    elif select == "2":
        print("Dear Customer, your transaction has been cancelled")
    elif select == "1":
        int_bundles_next2_proceed()
    else:
        print("Invalid request")
        int_bundles_next2()


def itn_bundles_next():
    clear()
    print("3. Zone3: United Kingdom, UAE, Kenya, Germany, Ethiopia, South Africa, Mozambique,Botswana K260:30min")
    print("4. Zone4: Rwanda, Tanzania, Uganda, Malawi, Congo DR K360:30min\n00 Back")
    selection = input()
    if selection == "3":
        int_bundles_next1()
    elif selection == "4":
        int_bundles_next2()
    elif selection == "00":
        itn_bundles()
    else:
        print("Invalid request")
        itn_bundles_next()


def itn_bundles():
    clear()
    print("1. Zone1: USA, India, China K25:30min\n2. Zone2: Canada, Namibia, Nigeria, Angola K110:30min\nn next\n00 Back")
    selection = input()
    if selection == "1":
        int_bundles1()
    elif selection == "2":
        int_bundles2()
    elif selection == "00":
        international_voice_calling()
    elif selection == "n":
        itn_bundles_next()
    else:
        print("Invalid request")
        itn_bundles()
def international_buy_for_other_menu():
    clear()
    itn_bundles()

def int_buy_for_other():
    clear()
    print("Please enter the subscribers number you wish to purchase a So Che Pack for(097XXXXXXX/077XXXXXXX)")
    pattern = r'^097\d{7}$|^077\d{7}$'
    selection = input()
    if re.match(pattern, selection):
        international_buy_for_other_menu()
    else:
        print("Dear customer the number you entered is not an Airtel number")


def international_voice_calling():
    clear()
    print("Please Select a bundle:\n1. Buy Bundles\n2. Buy for Others\n00 Back")
    select = input()
    if select == "1":
        itn_bundles()
    elif select == "n":
        itn_bundles_next()
    elif select == "2":
        int_buy_for_other()
    elif select == "00":
        home_menu_opt8()
    else:  ##
        print("Invalid request")
        international_voice_calling()



def subscribe_zm_tp_pm():
    clear()
    print("1. Main Account\n2. Airtel Money\n00 Back")
    pm = input()
    if pm == "1":
        print("Dear Customer, your transaction is being processed. You will receive a confirmation message shortly")
    elif pm == "2":
        airtel_money()
    elif pm == "00":
        subscribe_zm_tp() 
    else:
        print("Invalid request")
        subscribe_zm_tp_pm()

def subscribe_zm_tp():
    clear()
    print("You have selected K350 tour pack. Please select")
    print("1. Proceed\n00 Back")
    zm = input()
    if zm == "1":
        subscribe_zm_tp_pm()
    elif zm == "00":
        zambia_tourist_pack()
    else:
        print("Invalid entry")
        subscribe_zm_tp()

def zambia_tourist_pack():
    clear()
    print("Welcome to Zambia! Get 250 local mins,250SMS,10GB,K100 for international calls")
    print("@ K350 valid 14 days")
    print("1. Subscribe\n2. Check Balance\n00 Back")
    packopt = input()
    if packopt == "1":
        subscribe_zm_tp()
    elif packopt == "00":
        home_menu_opt8()
    elif packopt == "2":
        print("Dear Customer, your check balance request is being processed. You will receive a confirmation message shortly")
    else:
        print("Invalid request")
        zambia_tourist_pack()

#option 9 INTL Calling & roaming home menu
def home_menu_opt8(): #Displays options of the INTL calling & roaming and prompts user to select an option and after selects an one of the functions above is called is accodance of the option selected  
    clear()
    print("Welcome to Airtel International Services.\n1. One Airtel Roaming\n2. Global Roaming\n3. International Voice Calling\n4. Balance Check\n5. Zambia Tourist Pack")
    selection = input()
    if selection == "1":
        one_airtel_roaming()
    elif selection == "2":
        global_roaming()
    elif selection == "4":
        print("Dear Customer, your balance request is being processed. You will receive a confirmation message shortly")
    elif selection == "3":
        international_voice_calling()
    elif selection == "5":
        zambia_tourist_pack()
    else:
        print("Invalid request.")
        home_menu_opt8()

#option 9 ends here 

#option n (NEXT)
def n_next(): # displays the intl calling option and when a user selects the intl option. This function calls the above function
    clear()
    print("9. INTL Calling & roaming\n0 Return to main menu")
    selection = input()
    if selection == "9":
        home_menu_opt8()
    elif selection == "0":
        home_menu()
    elif selection == "1":
        home_menu_opt1()        #calls out the function of the Ikali - Data and Voice
    elif selection == "2":      
        home_menu_opt2()        #Calls out the function of the Airtel SoChe Pack
    elif selection == "3":
        home_menu_opt3()        #Calls out the function of the All network SoChe Pack
    elif selection == "4":
        home_menu_opt4()        #Calls out the function of the Data Pack
    elif selection == "5":
        home_menu_opt5()        #Calls out the function for Buy for Other
    elif selection == "6":
        home_menu_opt6()        #Calls out the function for Balance Check 
    elif selection == "7":
        home_menu_opt7()        #Calls out the function for Siliza-Airtime Loan
    elif selection == "8":
        print("Dear Customer, your request is being processed, You will receive a confirmation message with a link shortly. Click the link to download the App")       
    elif selection == "9":
        home_menu_opt8() 
    else:
        print("Invalid request")
        home_menu()

# The below function is used to display the main menu options 
# And when an option is selected it calls out a function in accordance to the selected option

def home_menu(): # main menu options or home menu
    clear()
    print("1. Ikali-Data and Voice\n2. Airtel Soche Pack\n3. All networks Soche\n4. Data Packs\n5. Buy for Other\n6. Balance Check\n7. Siliza-Airtime Loan\n8. Get Airtel App(100MB)\nn next")
    selection = input()
    if selection == "1":
        home_menu_opt1()        #calls out the options of the Ikali - Data and Voice
    elif selection == "2":      
        home_menu_opt2()        #Calls out the options of the Airtel SoChe Pack
    elif selection == "3":
        home_menu_opt3()        #Calls out the options of the All network SoChe Pack
    elif selection == "4":
        home_menu_opt4()        #Calls out the options of the Data Pack
    elif selection == "5":
        home_menu_opt5()        #Calls out the options of Buy for Other
    elif selection == "6":
        home_menu_opt6()        #Calls out the options of Balance Check 
    elif selection == "7":
        home_menu_opt7()        #Calls out the options of Siliza-Airtime Loan
    elif selection == "8":
        print("Dear Customer, your request is being processed, You will receive a confirmation message with a link shortly. Click the link to download the App")       
    elif selection == "9":
        home_menu_opt8()
    elif selection == "n":
        n_next()                    #Calls out the function for the INTL calling & roaming
    else:                           #if the options selected was not displayed by the main menu.                      #it displays invalid entry and calls the function for the main menu again
        print("Invalid request")
        home_menu()   

#The lines of code below prompts the user to enter or input the value of the USSD
#If the USSD inputted is equal to *117# then it outputs the main menus options by calling out the function the function which represents the main menu
#Else if the USSD is no equal to *117# then the lines of code below does not call the main menu 
def ussd():
    print("Enter USSD: ")
    USSD = input()
    if USSD == "*117#":
        home_menu() # displays options of the main menus
    else:
        print("Connection problem or wrong MMI code")
ussd()
