import os
from time import sleep
try:
    import pyttsx3
except:
    os.system("pip install pyttsx3")
    import pyttsx3
        

# How much time you want to wait before speak
sleep(1)

alien_message = 'Greetings to the inhabitants of planet Earth. I am an alien from a planet Dumptron X named B F J D, or Big Fat Juicy Dumper, and I have taken control of this computer to communicate with you. I want to announce to you that in exactly one year\'s time our invasion fleet will arrive on your planet because we have heard that you make very good cigarettes. Resistance is useless. Your only option is to give us all the cigarettes you have and to produce as many as possible to satiate us. Your planet will become a cigar colony and you will produce forever. Get ready, shitlings. Our hunger is near.'

motore = pyttsx3.init()

# Set alien voice
voce_alienea = motore.getProperty('voices')[1]
motore.setProperty('voice', voce_alienea.id)

# Set the pitch property to make the voice more alien-like
#motore.setProperty('pitch', 90)

motore.say(alien_message)
motore.runAndWait()