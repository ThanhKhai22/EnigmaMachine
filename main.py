import pygame


from keyboard import Keyboard
from plugboard import Plugboard
from rotor import Rotor
from reflector import Reflector
from enigma import Enigma
from draw import draw

pygame.init()
pygame.font.init()
pygame.display.set_caption("ENIGMA MACHINE")

MONO = pygame.font.SysFont("FreeMono", 25)
BOLD = pygame.font.SysFont("FreeMono", 25, bold=True)


WIDTH = 1300
HEIGHT = 650
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
MARGINS = {"top":100, "bottom":50, "left":100, "right":100}
GAP = 100
INPUT = ""
OUTPUT = ""
PATH = []

I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
VI = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")

KB = Keyboard()
PB = Plugboard(["AR", "GK", "OX"])

ENIGMA = Enigma(A,I,II,III,PB,KB)

ENIGMA.set_rings((1,1,1)) #AAA

ENIGMA.set_key("DUT")

# message = "TEST"
# cipher_text = ""
# for letter in message:
#     cipher_text = cipher_text + ENIGMA.encipher(letter)
# print(cipher_text)

animating = True
while animating:
    SCREEN.fill("#333333")
    
    text = BOLD.render(INPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4))
    SCREEN.blit(text, text_box)
    
    text = MONO.render(OUTPUT, True, "white")
    text_box = text.get_rect(center = (WIDTH/2, MARGINS["top"]/4+25))
    SCREEN.blit(text, text_box)
    
    draw(ENIGMA, PATH, SCREEN, WIDTH, HEIGHT, MARGINS, GAP, BOLD)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                III.rotate()
            elif event.key == pygame.K_SPACE:
                INPUT = INPUT + " "
                OUTPUT = OUTPUT + " "
            else:
                key = event.unicode
                if key in "abcdefghijklmnopqrstuvwxyz":
                    letter = key.upper()
                    INPUT = INPUT + letter
                    PATH, cipher = ENIGMA.encipher(letter)
                    OUTPUT = OUTPUT + cipher
                    