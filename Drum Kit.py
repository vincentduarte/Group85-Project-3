from Tkinter import *
from functools import partial
import winsound


window = Tk()
#List that sounds will be appended too
Beats = []


#Play Functions
def Play1(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav', winsound.SND_FILENAME)
def Play2(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-c.wav', winsound.SND_FILENAME)
def Play3(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano C.wav', winsound.SND_FILENAME)
def Play4(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-d.wav', winsound.SND_FILENAME)
def Play5(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-e.wav', winsound.SND_FILENAME)
def Play6(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-eb.wav', winsound.SND_FILENAME)
def Play7(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-f.wav', winsound.SND_FILENAME)
def Play8(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano F.wav', winsound.SND_FILENAME)
def Play9(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-g.wav', winsound.SND_FILENAME)
def Play10(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Piano G.wav', winsound.SND_FILENAME)
def Play11(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-a.wav', winsound.SND_FILENAME)
def Play12(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-b.wav', winsound.SND_FILENAME)
def Play13(event):
    winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\piano-bb.wav', winsound.SND_FILENAME)

#Functions for appending
def Bind1(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav')
def Bind2(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-c.wav')
def Bind3(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano C.wav')
def Bind4(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-d.wav')
def Bind5(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-e.wav')
def Bind6(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-eb.wav')
def Bind7(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-f.wav')
def Bind8(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano F.wav')
def Bind9(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-g.wav')
def Bind10(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\Piano G.wav')
def Bind11(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-a.wav')
def Bind12(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-b.wav')
def Bind13(event):
    Beats.append('C:\Users\Daniel\Desktop\Sound Clips\piano-bb.wav')

#Play Function and Loop function
def Loop(event):
    #for x in range(0,4):
        for player in Beats:
            winsound.PlaySound(player,winsound.SND_FILENAME)
#Clear function to make a different combination
def Clear(event):
    del Beats[:]

play = winsound.PlaySound('C:\Users\Daniel\Desktop\Sound Clips\Snare and Kick.wav', winsound.SND_FILENAME)


window.geometry("1000x600")
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

#binding Left Click to play sounds
button1.bind("<Button-1>",Play1)
button2.bind("<Button-1>",Play2)
button3.bind("<Button-1>",Play3)
button4.bind("<Button-1>",Play4)
button5.bind("<Button-1>",Play5)
button6.bind("<Button-1>",Play6)
button7.bind("<Button-1>",Play7)
button8.bind("<Button-1>",Play8)
button9.bind("<Button-1>",Play9)
button10.bind("<Button-1>",Play10)
button11.bind("<Button-1>",Play11)
button12.bind("<Button-1>",Play12)
button13.bind("<Button-1>",Play13)

#binding right click to create a loop
button1.bind("<Button-3>",Bind1)
button2.bind("<Button-3>",Bind2)
button3.bind("<Button-3>",Bind3)
button4.bind("<Button-3>",Bind4)
button5.bind("<Button-3>",Bind5)
button6.bind("<Button-3>",Bind6)
button7.bind("<Button-3>",Bind7)
button8.bind("<Button-3>",Bind8)
button9.bind("<Button-3>",Bind9)
button10.bind("<Button-3>",Bind10)
button11.bind("<Button-3>",Bind11)
button12.bind("<Button-3>",Bind12)
button13.bind("<Button-3>",Bind13)


buttonPlay.bind("<Button-1>",Loop)
buttonClear.bind("<Button-1>",Clear)

#binding Hover Function

#if someone can figure out how to make a function that makes this shorter that would be great, but I couldn't figure anything out
button2.bind("<Enter>", lambda event, b=button2: b.configure(bg="red"))
button2.bind("<Leave>", lambda event, b=button2: b.configure(bg="white"))
button3.bind("<Enter>", lambda event, b=button3: b.configure(bg="red"))
button3.bind("<Leave>", lambda event, b=button3: b.configure(bg="white"))
button4.bind("<Enter>", lambda event, b=button4: b.configure(bg="red"))
button4.bind("<Leave>", lambda event, b=button4: b.configure(bg="white"))
button5.bind("<Enter>", lambda event, b=button5: b.configure(bg="red"))
button5.bind("<Leave>", lambda event, b=button5: b.configure(bg="white"))
button6.bind("<Enter>", lambda event, b=button6: b.configure(bg="red"))
button6.bind("<Leave>", lambda event, b=button6: b.configure(bg="white"))
button7.bind("<Enter>", lambda event, b=button7: b.configure(bg="red"))
button7.bind("<Leave>", lambda event, b=button7: b.configure(bg="white"))
button8.bind("<Enter>", lambda event, b=button8: b.configure(bg="red"))
button8.bind("<Leave>", lambda event, b=button8: b.configure(bg="white"))
button9.bind("<Enter>", lambda event, b=button9: b.configure(bg="red"))
button9.bind("<Leave>", lambda event, b=button9: b.configure(bg="white"))
button10.bind("<Enter>", lambda event, b=button10: b.configure(bg="red"))
button10.bind("<Leave>", lambda event, b=button10: b.configure(bg="white"))
button11.bind("<Enter>", lambda event, b=button11: b.configure(bg="red"))
button11.bind("<Leave>", lambda event, b=button11: b.configure(bg="white"))
button12.bind("<Enter>", lambda event, b=button12: b.configure(bg="red"))
button12.bind("<Leave>", lambda event, b=button12: b.configure(bg="white"))
button13.bind("<Enter>", lambda event, b=button13: b.configure(bg="red"))
button13.bind("<Leave>", lambda event, b=button13: b.configure(bg="white"))
buttonPlay.bind("<Enter>", lambda event, b=buttonPlay: b.configure(bg="red"))
buttonPlay.bind("<Leave>", lambda event, b=buttonPlay: b.configure(bg="white"))
buttonClear.bind("<Enter>", lambda event, b=buttonClear: b.configure(bg="red"))
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