from Tkinter import *
from functools import partial
import winsound
import random

'''
window = Tk()

window.geometry("1000x600")
'''
root = Tk()
root.geometry("1000x600")

list=['kick','snare','pit bull','hi-hat']
colors=['blue', 'red', 'pink','royal blue','green','orange','cyan','purple']

snare=['http://har-bal.com/reference/Percussion/fmcr2.wav', 'http://www.denhaku.com/r_box/rx11/hi_tune_1.wav'
      'http://files.chatnfiles.com/10000_sounds_and_songs/WAV/SNARE_3.WAV', 'http://www.nebo.edu/learning_resources/ppt/sounds/baboom.wav'
      'ftp://ftp.lysator.liu.se/pub/awe32/wav/808Snare.wav','http://www.denhaku.com/r_box/linn/sd1.wav',
      'http://www.barryrudolph.com/mix/breverb/wav/6.wav','http://www.denhaku.com/r_box/sr16/sr16sd/chromesn.wav',
      'http://www.daimi.au.dk/~pmn/spf02/CDROM/pr4/sound/amp300_16bit_mono/snare/snare1_4.wav','http://home1.swipnet.se/~w-33956/ifsd2.wav']

kick=['http://www.denhaku.com/r_box/sr16/sr16bd/dbl%20head.wav','http://www.denhaku.com/r_box/rx11/bd_md_1.wav',
      'http://www.zone0ne.com/bassics/wav/bassdrum.wav', 'ftp://sunsite.univie.ac.at/pub/sound/csound/utilities/pc/midi2cs/22050/bd1_s48k.wav',
      'http://soundcavern.free.fr/kits/Act%20Bass%20Drum.wav', 'http://veikko.pp.fi/Testi1/SAMPLEJA_PLUGAREITA/fl5_samlpleja_synia/Vintage/hhd1kck10.wav',
      'http://work.colum.edu/~nlinscheid/sound-library/sdif-tests/bassdrum.aiff', 'http://soundcavern.free.fr/kick/kick009.wav',
      'http://www.imjohn.com/PresonusJensenXfrmrs/sounds/16-44.1/Channel%20Indicator.wav', 'http://cstrike.csmegagaming.com/sound/misc/pb2.wav',]

pitbull=['http://free-sounds.net/sound-files/animal-sounds/dog-sounds/DOG15.WAV','http://www.presepioelettronico.it/downloads/audio/files/cani.wav',
         'http://www.gkgraphics.com/download/sounds/wav/mono/Bark.wav', 'http://www.gravomaster.com/alarm/sounds/Dog_Bark_02.wav',
         'http://www.nyanmilla.net/wav/dog00.wav', 'http://www-cs-students.stanford.edu/~echawkes/Snakebite/Bark.aiff',
         'http://www.threecaster.com/wavy/BarkingP.WAV', 'http://www.wavlist.com/soundfx/001/dog-bark5.wav',
         'http://www.nifter.com/sound_effects/animals_sounds/dog_barking_NifterDotCom.wav', 'http://www.mcello63.com/suonerie_varie/Latrato.mp3',]

hihat=['http://www.marksmart.net/gearhack/jazzpedalboard/Footprints4BarLoop.wav','http://machines.hyperreal.org/manufacturers/Casio/RZ-1/samples/tmp/casio-rz1/HCRZ.WAV',
       'http://www.denhaku.com/r_box/tr707/closed.wav', 'http://bigsamples.free.fr/d_kit/hithat/hat_2.wav',
       'http://bigsamples.free.fr/d_kit/hithat/hh1.wav', 'http://cd.textfiles.com/sigserieswin/SOUNDS/WAV/HIHAT.WAV',
       'http://www.vrsound.com/vrwaves/vrsound_hat2.wav', 'http://www.whitenote.dk/Download%20Frame/Whitenote%20Sampels/Aids%20virus/Hi-hat%202.wav',
       'http://tipiwiki.free.fr/snd/TimbaleCourte.wav', 'http://www.americanmusical.com/ItemFiles/MP3/PST5_14_medium_hats_chick.mp3',]

frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 0, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

#example values
for x in range(10):
    for y in range(4):
        btn = Button(frame,text=list[y] + " " +str(x+1), bg="white", activebackground=random.choice(colors))
        btn.bind("<Enter>", lambda event, b=btn: b.configure(bg=random.choice(colors)))
        btn.bind("<Leave>", lambda event, b=btn: b.configure(bg="white"))
        btn.bind("<Button-1>", lambda event, b=btn: b.configure(bg=random.choice(colors)))

        btn.grid(column=x, row=y, sticky=N+S+E+W)


for x in range(10):
  Grid.columnconfigure(frame, x, weight=1)

for y in range(5):
  Grid.rowconfigure(frame, y, weight=1)

root.mainloop()
'''
#Declaring Buttons
button1=Button(window,text= "13",  fg="navy blue", height = 5, width=25)
button2=Button(window,text= "Piano c", fg="navy blue",bg="white", height = 5, width=23)
button3=Button(window,text= "Piano C", fg="navy blue",bg="white", height = 5, width=23)
button4=Button(window,text= "Piano d", fg="navy blue",bg="white", height = 5, width=23)
button5=Button(window,text= "Piano e", fg="navy blue",bg="white", height = 5, width=23)
button6=Button(window,text= "Piano eb", fg="navy blue",bg="white", height = 5, width=23)
button7=Button(window,text= "Piano F", fg="navy blue",bg="white", height = 5, width=23)
button8=Button(window,text= "Piano f", fg="navy blue",bg="white", height = 5, width=23)
button9=Button(window,text= "Piano g", fg="navy blue",bg="white", height = 5, width=23)
button10=Button(window,text= "Piano G", fg="navy blue",bg="white", height = 5, width=23)
button11=Button(window,text= "Piano a", fg="navy blue",bg="white", height = 5, width=23)
button12=Button(window,text= "Piano b", fg="navy blue",bg="white", height = 5, width=23)
button13=Button(window,text= "Piano bb", fg="navy blue",bg="white", height = 5, width=23)
buttonPlay=Button(window,text= "Play", fg="navy blue",bg="white", height = 5, width=72)
buttonClear=Button(window,text= "Clear", fg = "navy blue",bg="white", height = 5, width=72)
button16=Button(window,text="Button16",fg = "navy blue", bg = "white", height = 5, width=23)
button17=Button(window,text="Button17",fg = "navy blue", bg = "white", height = 5, width=23)
button18=Button(window,text="Button18",fg = "navy blue", bg = "white", height = 5, width=23)
button19=Button(window,text="Button19",fg = "navy blue", bg = "white", height = 5, width=23)
button20=Button(window,text="Button20",fg = "navy blue", bg = "white", height = 5, width=23)
button21=Button(window,text="Button21",fg = "navy blue", bg = "white", height = 5, width=23)
button22=Button(window,text="Button22",fg = "navy blue", bg = "white", height = 5, width=23)
button23=Button(window,text="Button23",fg = "navy blue", bg = "white", height = 5, width=23)
button24=Button(window,text="Button24",fg = "navy blue", bg = "white", height = 5, width=23)
button25=Button(window,text="Button25",fg = "navy blue", bg = "white", height = 5, width=23)
button26=Button(window,text="Button26",fg = "navy blue", bg = "white", height = 5, width=23)
button27=Button(window,text="Button27",fg = "navy blue", bg = "white", height = 5, width=23)
button28=Button(window,text="Button28",fg = "navy blue", bg = "white", height = 5, width=23)
button29=Button(window,text="Button29",fg = "navy blue", bg = "white", height = 5, width=23)
button30=Button(window,text="Button30",fg = "navy blue", bg = "white", height = 5, width=23)
button31=Button(window,text="Button31",fg = "navy blue", bg = "white", height = 5, width=23)
button32=Button(window,text="Button32",fg = "navy blue", bg = "white", height = 5, width=23)
button33=Button(window,text="Button33",fg = "navy blue", bg = "white", height = 5, width=23)
button34=Button(window,text="Button34",fg = "navy blue", bg = "white", height = 5, width=23)
button35=Button(window,text="Button35",fg = "navy blue", bg = "white", height = 5, width=23)
button36=Button(window,text="Button36",fg = "navy blue", bg = "white", height = 5, width=23)
button37=Button(window,text="Button37",fg = "navy blue", bg = "white", height = 5, width=23)
button38=Button(window,text="Button38",fg = "navy blue", bg = "white", height = 5, width=23)
button39=Button(window,text="Button39",fg = "navy blue", bg = "white", height = 5, width=23)
'''
#binding Hover Function

#if someone can figure out how to make a function that makes this shorter that would be great, but I couldn't figure anything out
'''
button2.bind("<Enter>", lambda event, b=button2: b.configure(bg="red"))
button2.bind("<Leave>", lambda event, b=button2: b.configure(bg="white"))
button3.bind("<Enter>", lambda event, b=button3: b.configure(bg="cyan"))
button3.bind("<Leave>", lambda event, b=button3: b.configure(bg="white"))
button4.bind("<Enter>", lambda event, b=button4: b.configure(bg="green"))
button4.bind("<Leave>", lambda event, b=button4: b.configure(bg="white"))
button5.bind("<Enter>", lambda event, b=button5: b.configure(bg="purple"))
button5.bind("<Leave>", lambda event, b=button5: b.configure(bg="white"))
button6.bind("<Enter>", lambda event, b=button6: b.configure(bg="yellow"))
button6.bind("<Leave>", lambda event, b=button6: b.configure(bg="white"))
button7.bind("<Enter>", lambda event, b=button7: b.configure(bg="pink"))
button7.bind("<Leave>", lambda event, b=button7: b.configure(bg="white"))
button8.bind("<Enter>", lambda event, b=button8: b.configure(bg="gold"))
button8.bind("<Leave>", lambda event, b=button8: b.configure(bg="white"))
button9.bind("<Enter>", lambda event, b=button9: b.configure(bg="royal blue"))
button9.bind("<Leave>", lambda event, b=button9: b.configure(bg="white"))
button10.bind("<Enter>", lambda event, b=button10: b.configure(bg="green yellow"))
button10.bind("<Leave>", lambda event, b=button10: b.configure(bg="white"))
button11.bind("<Enter>", lambda event, b=button11: b.configure(bg="indigo"))
button11.bind("<Leave>", lambda event, b=button11: b.configure(bg="white"))
button12.bind("<Enter>", lambda event, b=button12: b.configure(bg="magenta"))
button12.bind("<Leave>", lambda event, b=button12: b.configure(bg="white"))
button13.bind("<Enter>", lambda event, b=button13: b.configure(bg="orange"))
button13.bind("<Leave>", lambda event, b=button13: b.configure(bg="white"))
buttonPlay.bind("<Enter>", lambda event, b=buttonPlay: b.configure(bg="plum"))
buttonPlay.bind("<Leave>", lambda event, b=buttonPlay: b.configure(bg="white"))
buttonClear.bind("<Enter>", lambda event, b=buttonClear: b.configure(bg="dark blue"))
buttonClear.bind("<Leave>", lambda event, b=buttonClear: b.configure(bg="white"))
button16.bind("<Enter>", lambda event, b=button16: b.configure(bg="red"))
button16.bind("<Leave>", lambda event, b=button16: b.configure(bg="white"))
button17.bind("<Enter>", lambda event, b=button17: b.configure(bg="red"))
button17.bind("<Leave>", lambda event, b=button17: b.configure(bg="white"))
button18.bind("<Enter>", lambda event, b=button18: b.configure(bg="red"))
button18.bind("<Leave>", lambda event, b=button18: b.configure(bg="white"))
button19.bind("<Enter>", lambda event, b=button19: b.configure(bg="red"))
button19.bind("<Leave>", lambda event, b=button19: b.configure(bg="white"))
button20.bind("<Enter>", lambda event, b=button20: b.configure(bg="red"))
button20.bind("<Leave>", lambda event, b=button20: b.configure(bg="white"))
button21.bind("<Enter>", lambda event, b=button21: b.configure(bg="red"))
button21.bind("<Leave>", lambda event, b=button21: b.configure(bg="white"))
button22.bind("<Enter>", lambda event, b=button22: b.configure(bg="red"))
button22.bind("<Leave>", lambda event, b=button22: b.configure(bg="white"))
button23.bind("<Enter>", lambda event, b=button23: b.configure(bg="red"))
button23.bind("<Leave>", lambda event, b=button23: b.configure(bg="white"))
button24.bind("<Enter>", lambda event, b=button24: b.configure(bg="red"))
button24.bind("<Leave>", lambda event, b=button24: b.configure(bg="white"))
button25.bind("<Enter>", lambda event, b=button25: b.configure(bg="red"))
button25.bind("<Leave>", lambda event, b=button25: b.configure(bg="white"))
button26.bind("<Enter>", lambda event, b=button26: b.configure(bg="red"))
button26.bind("<Leave>", lambda event, b=button26: b.configure(bg="white"))
button27.bind("<Enter>", lambda event, b=button27: b.configure(bg="red"))
button27.bind("<Leave>", lambda event, b=button27: b.configure(bg="white"))
button28.bind("<Enter>", lambda event, b=button28: b.configure(bg="red"))
button28.bind("<Leave>", lambda event, b=button28: b.configure(bg="white"))
button29.bind("<Enter>", lambda event, b=button29: b.configure(bg="red"))
button29.bind("<Leave>", lambda event, b=button29: b.configure(bg="white"))
button30.bind("<Enter>", lambda event, b=button30: b.configure(bg="red"))
button30.bind("<Leave>", lambda event, b=button30: b.configure(bg="white"))
button31.bind("<Enter>", lambda event, b=button31: b.configure(bg="red"))
button31.bind("<Leave>", lambda event, b=button31: b.configure(bg="white"))
button32.bind("<Enter>", lambda event, b=button32: b.configure(bg="red"))
button32.bind("<Leave>", lambda event, b=button32: b.configure(bg="white"))
button33.bind("<Enter>", lambda event, b=button33: b.configure(bg="red"))
button33.bind("<Leave>", lambda event, b=button33: b.configure(bg="white"))
button34.bind("<Enter>", lambda event, b=button34: b.configure(bg="red"))
button34.bind("<Leave>", lambda event, b=button34: b.configure(bg="white"))
button35.bind("<Enter>", lambda event, b=button35: b.configure(bg="red"))
button35.bind("<Leave>", lambda event, b=button35: b.configure(bg="white"))
button36.bind("<Enter>", lambda event, b=button36: b.configure(bg="red"))
button36.bind("<Leave>", lambda event, b=button36: b.configure(bg="white"))


#Laying out the grid
button2.grid(row=0, column=0, sticky = W)
button3.grid(row=0, column=1, sticky = W)
button4.grid(row=1,column=0, sticky = W)
button5.grid(row=1, column=1, sticky = W)
button6.grid(row=2,column=0, sticky = W)
button7.grid(row=2,column=1, sticky = W)
button8.grid(row=3,column=0, sticky = W)
button9.grid(row=3,column=1, sticky = W)
button10.grid(row=4,column=0, sticky = W)
button11.grid(row=4,column=1, sticky = W)
button12.grid(row=5,column=0, sticky = W)
button13.grid(row=5,column=1, sticky = W)
buttonPlay.grid(row=6,column=0,columnspan=3, sticky = W)
buttonClear.grid(row=6, column=3,columnspan=3, sticky = W)
button16.grid(row=0, column=2, sticky = W)
button17.grid(row=0, column=3, sticky = W)
button18.grid(row=1, column=2, sticky = W)
button19.grid(row=1, column=3, sticky = W)
button20.grid(row=2, column=2, sticky = W)
button21.grid(row=2, column=3, sticky = W)
button22.grid(row=3, column=2, sticky = W)
button23.grid(row=3, column=3, sticky = W)
button24.grid(row=4, column=2, sticky = W)
button25.grid(row=4, column=3, sticky = W)
button26.grid(row=5, column=2, sticky = W)
button27.grid(row=5, column=3, sticky = W)
button28.grid(row=0, column=4, sticky = W)
button29.grid(row=0, column=5, sticky = W)
button30.grid(row=1, column=4, sticky = W)
button31.grid(row=1, column=5, sticky = W)
button32.grid(row=2, column=4, sticky = W)
button33.grid(row=2, column=5, sticky = W)
button34.grid(row=3, column=4, sticky = W)
button35.grid(row=3, column=5, sticky = W)
button36.grid(row=4, column=4, sticky = W)
button37.grid(row=4, column=5, sticky = W)
button38.grid(row=5, column=4, sticky = W)
button39.grid(row=5, column=5, sticky = W)


window.mainloop()
'''