#Define a function called main
def main():
    #Ask the user for their name and store it into "Name"
    Name = input("Enter your name: ")
    #Ask the user for their email and store it into "Email"
    Email = input("Enter your email: ")

    #Import a module (A group of code) called os.
    import os
    #Using the "System" item within the method, we can interact with the command line.
    #We run 2 commands
    #The first one sets the git user's name
    os.system("git config --global user.name " + Name)
    #The Second one sets the git user's email
    os.system("git config --global user.email " + Email)

#Are we running as a user?
if __name__ == "__main__":
    #If Yes, goto "Main"
    main()