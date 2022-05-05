import pygame

class Input(object):

    def __init__(self):
        # has the user quit the application?
        self.quit = False
        

    def update(self):
        #iterate over all user input event (such as keyboard or mouse)
        #that occursed since the last time event were checked.
        #For events in pygame.event.get():
        #quit event occurs by clicking button to close window

        if pygame.event.get() == pygame.QUIT:
            self.quit = True


    