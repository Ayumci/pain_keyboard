import keyboard
import pygame
import random
pygame.mixer.init()
sounds = [
     'am-i-laughing-no.mp3',
     'and-women-have-a-very-different-mentality-to-money-than-men-if-you-show-a-woman-how-to-make-1000-in-an-hour-shell-think-i-only-have-i-only-have-to-work-an-hour-a-week-whereas-if-you-show-a-man.mp3',
     'breath-air.mp3',
     'dumbass.mp3',
    'friend-on-the-other-hand-can-betray-you-and-betrayal-is-much-worse-than-an-attack-from-an-enemy-for-two-reasons-one-it-catches-you-by-surprise-thats-the-first-thing-and-the-second-thing-is.mp3',
     'fucking-stupid-it-didnt-cross-your-mind-at-some-point-that-permanently-suck-it-on-this-vape-was-gonna-damage-you-in-some-way-you-deserve-what-happens-to-your-dumb-ass-breathe-air-have-you-ever.mp3',
     'i-am-too-brilliant-a-man-too-perfect-in-every-single-metric-too-big-too-strong-too-smart-i-can-fight-too-well-im-caramel-im-beautiful-it-would-be-a-shame-for-me-to-not-service-these-femal.mp3',
     'i-called-this-virus-a-hoax-from-the-start-and-everyone-called-me-crazy-people.mp3',
     'i-know-a-lot-of-broke-people-who-are-very-arrogant-theyll-come-along-go-i-think-thats-a-scam-ohh-do-you-brokey-ohh-brokey-thinks-its-a-scam-ohh-tell-me-again-about-how-my-online-educatio.mp3',
     'i-really-i-decided-to-get-rich-rich',
    
]

def play_sound(e):
    sound_file = random.choice(sounds)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Bind the function to any key press event
keyboard.on_press(play_sound)

# Start the event loop
keyboard.wait()