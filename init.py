#Define a function called main
def main():
    Name = input("Enter your name: ")
    Email = input("Enter your email: ")
    import os
    os.system("git config --global user.name " + Name)
    os.system("git config --global user.email " + Email)

#Are we running as a user?
if __name__ == "__main__":
    main()