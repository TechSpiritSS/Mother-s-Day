# pip install pygame
import pygame
from time import sleep
pygame.init()
window = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
pygame.mixer.init()
pygame.mixer.music.load('piano.mp3') # Your Music in the same directory as of source code
pygame.mixer.music.play()
image = pygame.image.load('pic.jpg') # Your Image in the same directory as of source code
window.blit(image,(650,100)) # use (0,0) for single image
image = pygame.image.load('pic2.jpg') # optional for adding other image
window.blit(image,(0,0)) # Second Image
pygame.display.update()
sleep(15) # Timer for display

# For me it worked best with 16:9 images
