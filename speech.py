# Take the idea from the idea.txt and turn it into a speech and save it as speech

import gtts  
from playsound import playsound  
import datetime

# Inputs
textfile = open("Finalized_Ideas/FinalIdea.txt", "r")
text = textfile.readline()
language = 'en'




# make a request to google to get synthesis  
voiceclip = gtts.gTTS(text, lang=language, slow=False)  

# save the audio file  
todaytime = datetime.datetime.now()
voiceclip.save(f"Voices/clip.mp3")

# running the playsound to check if everything works fine
playsound(f"Voices/clip.mp3")