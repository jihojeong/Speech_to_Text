#TTS (Text to Speech)
#STT (Speech to Text).|py

from gtts import gTTS
from playsound import playsound

# English
#t = "What the hell should I do when I am broke?"
#file_name = 'sample.mp3'
#tts_en = gTTS(text=t, lang="en")
#tts_en.save(file_name)



# Korean
file_name = 'korean.mp3'
test = '이것도 할수있는지 한번 테스트 해보도록 하겠습니다'
tts_ko = gTTS(text=test, lang='ko')
tts_ko.save(file_name)
playsound(file_name)


