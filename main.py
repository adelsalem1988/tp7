if temperature > 60:
    display.scroll("Alerte")
    music.play(music.BA_DING)
else:
    if light_level >= 100:  # Jour
        if 20 <= sound_level <= 100:
            display.scroll("Prix voiture: 2dt")
            music.play(music.NYAN)
        elif sound_level > 200:
            display.scroll("Prix camion: 3dt")
            music.play(music.ENTERTAINER)
        else:
            display.show("X")
            display.scroll("Interdit")
    else:  # Nuit
        display.scroll("Prix: 5dt")
        music.play(music.POWER_UP)

sleep(1000)