#Basic Login System


usernames = ["m","dan","mark","tom","susan"]
password = ["2","asdf","1234","qwerty","4321"]

timeline = []


def signup():

    while True: 

        newUser = input("Create a username: ")
        if newUser in usernames:
             print("Print username taken")
             continue
        
        while True:
         
            newPass = input("Create a password: ")

            if len(newPass) < 4:
                 print("Password too short (atleast 4 characters) ")
                 continue

            confirmPass = input("Confirm password: ")

            if newPass != confirmPass:
                print("Passwords dont match try again")
                continue


            if newPass == confirmPass:
                print("New user created. Welcome", newUser,"!")
                usernames.append(newUser)
                password.append(confirmPass)  
                choice()          
               
    
def login():
    
    uname = input("Enter username: ")
    
    for i in range(3):
        pword = input("Enter password: ")
        if uname not in usernames or pword not in password :
            print("Incorrect username or password")
        if uname in usernames and pword in password:
            print("Successful Login")
            print("Hello ",uname)
            home()
           

def logOut():
     print("logged out good bye")
     
     
       

def choice():
     
     while True:
          choice = int(input("login (1) or signup (2) "))

          if choice == 1:
                    login()
                    break
          elif choice == 2:
                    signup()
                    break

def home():
     
     choice2 = int(input("View timeline (1) Add to the timeline (2) View Friends (3) Log Out (4)  \n"))

     if choice2 == 1:
          viewTimeline()
     elif choice2 == 2:
          addTimeline()
     elif choice2 == 3:
          viewUsers()
     elif choice2 == 4:
          logOut()

def viewTimeline():
     
     print(timeline)

     choice4 = input("Would you like to add to the timeline? Y/N")
     if choice4 == "y":
          addTimeline()
     else:
        home()
      
def addTimeline():
     
     post = input("Enter text to post: ")
     timeline.append(post)
     

     while True:
        choice3 = int(input("View timeline (1) or Add to the timeline (2) \n"))

        if choice3 == 1:
             viewTimeline()

        if choice3 == 2:
             addTimeline()

def viewUsers():
     print(' '.join(usernames))

#main program

choice()
