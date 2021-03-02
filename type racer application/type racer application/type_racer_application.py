from tkinter import *
from timeit import default_timer as timer
import random
from time import sleep
import time

#TODO :: Add fun pictures and work on the GUI
#TODO :: open the window allowing user to read code, start 5 second timer, then allow user to type after 5 seconds
#TODO :: make an easy, medium, and hard mode
#TODO :: take every word in quote and put it into a list seperated by spaces, do the same for the user's input, and compare each element for mistakes, increment mistakes


x=0
y=0



def results(event): #TODO :: add all of the results to this function, clear the screen after user is done typing and lead to this screen showing results
    add_stuff=0

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
            main.after(self.sleep(10))
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
        for i in range(len(user_quote)): #counts the number of characters the user types
            num_char += 1
        wpm = ((num_char/5)-mistakes)/minutes_and_seconds #calculation for wpm
        print("Words per min:", wpm)
        wpm = ("%.2f" % wpm)
        wpm_string=str(wpm)
        wpm_results = wpm + " WPM" 
        wpm_label=Label(window,text=wpm_results,font='times 20') #wpm results label
        wpm_label.place(x=240,y=270)

        print(minutes_and_seconds) #tests
        print(time_minutes)
        print(time_seconds)

        time_minutes_string = str(time_minutes) #converts the minutes, seconds, and num_words to strings to fit into Label 
        time_seconds = '{0:.2g}'.format(time_seconds)
        time_seconds_string = str(time_seconds)
        num_words_string = str(num_words)

        if time_minutes > 0: #calculates final_results dependent on whether or not there was more than a minute used to type
            final_result= "It took you " + time_minutes_string + " minute(s) and " + time_seconds_string + " seconds to type " + num_words_string + " word(s)!"
        else:
            final_result= "It took you " + time_seconds_string + " seconds to type " + num_words_string + " words!"

        print(final_result)
        check_message=Label(window,text=final_result,font="times 18")  #label that show the amount of time used to type the quote
        check_message.place(x=25,y=450)

    with open('quotes.txt', 'r') as f: #opens the text file to create a list out of the quotes
        lines = f.read().splitlines()

    quote = random.randint(0,len(lines)-2) #grabs a random quote and displays it
    x2=Message(window,text = lines[quote],pady=100,font="times 15") 
    x2.pack(fill=X)
    x2.place(x=115,y=0)

    num_words = len(lines[quote].split()) #counts the words in the quote
    print(num_words)

    entry = Entry(width=70) #entry line that allows user to type the quote
    entry.place(x=115,y=50)
    entry.focus()

    #c1= Label(window,text="Begin!",font='times 20') #begin label 
    #c1.place(x=10,y=10)

    b2=Button(window,text="Press enter when finished",command=check_result,width=20,bg='red') #submit button binded to return key
    window.bind('<Return>', check_result)
    b2.place(x=240,y=225)

    start=timer() #timer that counts the time it takes to type quote

#main window
window = Tk() 
window.geometry("700x400")
window.title("Adam's typing speed test")
window.attributes('-topmost',True)
#window.lift()

#start screen
x1=Label(window,text = "Welcome to the typing speed test. Let's begin...", font = "times 14")
x1.place(x=165,y=140)
b1 = Button(window,text="Press Enter",command=game,width=12,bg='red')
b1.place(x=280,y=180)
window.bind('<Return>', game)

#run the GUI
window.mainloop()