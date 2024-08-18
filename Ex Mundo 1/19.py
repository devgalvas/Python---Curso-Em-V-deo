from pygame import mixer

mixer.init()
mixer.music.load('gal.mp3')
mixer.play()
mixer.event.wait()