from tkinter import *
from timeit import default_timer as timer
import random
from time import sleep

#TODO :: reconfigure check_result() to display the accuracy of the user-typed string 
#TODO :: Create a countdown for the timer, stop the timer after hitting submit, and show the user their results
#TODO :: Add fun pictures and work on the GUI
#TODO :: Fix the .after() function countdown
#TODO :: open the window allowing user to read code, start 5 second timer, then allow user to type after 5 seconds
#TODO :: think about using text instead of entry for text box
#TODO :: make an easy, medium, and hard mode
#TODO :: calculate net WPM after figuring out how to calculate mistakes
#TODO :: stop the timer when user is done
#TODO :: make it so that when there is more or less characters in the user_quote that it tells the user to try again and that there is insufficient data to determine WPM (or fix it, whatever)

x=0
y=0

def game(event): #fix the event warning on console when manual enter is pressed
    global x
    global y
    if x==0: #clears the screen after starting the game
        def all_children(window): 
            _list = window.winfo_children()
            for i in _list:
                if i.winfo_children():
                    _list.extend(i.winfo_children())
            return _list
        widget_list=all_children(window)
        for i in widget_list:
            i.destroy()
        x=x+1

    if y==0: #FIXME :: countdown before the game starts to users can see the quote before they type it
        def countdown(self):
            self.sleep(10)
            print("test")

    def check_result(event): #checks if word is spelt correctly
        def compare(a,b,c): #counts the mistakes in the quote
            try: #excepts when strings are not the same length
                for i in range(len(a)): #manually counts the mistakes instead of zip()
                    if a[i]!=b[i]:
                        print(i)
                        c += 1
            except IndexError:
                print("Quotes are not the same length.")
            return c

        mistakes=0
        user_quote = entry.get() #takes the user's quote from entry
        print(compare(user_quote,lines[quote],mistakes)) 
        
        end=timer() 
        time_seconds = end-start
        time_seconds_stored = time_seconds #stores the seconds before converting to minutes and seconds
        time_minutes=0

        while time_seconds >= 60: #converts from seconds to minutes and seconds
            time_minutes += 1
            time_seconds = time_seconds-60

        minutes_and_seconds = time_minutes + (time_seconds / 60) #calculate the minutes
        #minutes_and_seconds = ("%.2f" % minutes_and_seconds)
        #time_seconds = ("%.2f" % time_seconds)

        num_char=0
        for i in range(len(user_quote)):
            num_char += 1
        wpm = ((num_char/5)-mistakes)/minutes_and_seconds
        print("Words per min:", wpm)
        wpm = ("%.2f" % wpm)
        #wpm_string=str(wpm)
        wpm_label=Label(window,text=wpm,font='times 20')
        wpm_label.place(x=700,y=50)

        print(minutes_and_seconds)
        print(time_minutes)
        print(time_seconds)

        time_minutes_string = str(time_minutes) #converts the minutes, seconds, and num_words to strings to fit into Label 
        time_seconds_string = str(time_seconds)
        num_words_string = str(num_words)

        if time_minutes > 0: #calculates final_results dependent on whether or not there was more than a minute used to type
            final_result= "It took you " + time_minutes_string + " minute(s) and " + time_seconds_string + " seconds to type " + num_words_string + " word(s)!"
        else:
            final_result= "It took you " + time_seconds_string + " seconds to type " + num_words_string + " words!"

        print(final_result)
        check_message=Label(window,text=final_result,font="times 18")  #label that show the amount of time used to type the quote
        check_message.place(x=25,y=450)

    with open('TextFile1.txt', 'r') as f: #opens the text file to create a list out of the quotes
        lines = f.read().splitlines()

    quote = random.randint(0,len(lines)-2) #grabs a random quote and displays it
    x2=Message(window,text = lines[quote],font="times 15") 
    x2.place(x=300,y=100)
    #x2.pack(ipadx=300,ipady=300)

    num_words = len(lines[quote].split()) #counts the words in the quote
    print(num_words)

    entry = Entry(width=50) #entry line that allows user to type the quote
    entry.place(x=150,y=55)
    entry.focus()

    c1= Label(window,text="Begin!!",font='times 20') #begin label 
    c1.place(x=10,y=10)

    b2=Button(window,text="Submit",command=check_result,width=12,bg='red') #submit button binded to return key
    window.bind('<Return>', check_result)
    b2.place(x=150,y=100)

    start=timer() #timer that counts the time it takes to type quote

#main window
window = Tk() 
window.geometry("900x500")
window.title("Adam's typing speed test")
window.attributes('-topmost',True)
#window.lift()

#start screen
x1=Label(window,text = "Welcome to the typing speed test. Let's begin...", font = "times 12")
x1.place(x=315,y=200)
b1 = Button(window,text="Press Enter",command=game,width=12,bg='red')
b1.place(x=400,y=250)
window.bind('<Return>', game)

#run the GUI
window.mainloop()