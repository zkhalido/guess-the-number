import packages

if '__main__' == __name__:
    player = packages.interface.UserInterface()
    player.user_input()
    player.guess()
