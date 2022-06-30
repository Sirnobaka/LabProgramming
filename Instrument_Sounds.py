NOTE_C4 = 262
NOTE_CS4 = 277
NOTE_D4 = 294
NOTE_DS4 = 311
NOTE_E4  = 330
NOTE_F4  = 349
NOTE_FS4 = 370
NOTE_G4  = 392
NOTE_GS4 = 415
NOTE_A4  = 440
NOTE_AS4 = 466
NOTE_B4 =  494

def PlayGamma(kei):
    Gamma = [NOTE_C4, NOTE_D4, NOTE_E4, NOTE_F4, NOTE_G4, NOTE_A4, NOTE_B4]

    for note in Gamma:
        #print(note)
        kei.write('beeper.beep(0.1, '+str(note)+')')
    for note in Gamma[::-1][1:]:
        #print(note)
        kei.write('beeper.beep(0.1, ' + str(note) + ')')