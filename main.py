import random
import os
import tkinter as tk
import PIL.Image as Image
# import pyautogui

x = 1400
cycle = 0
check = 1
idle_num =[1,2,3,4]
sleep_num = [10,11,12,13,15]
walk_left = [6,7]
walk_right = [8,9]
event_number = random.randrange(1,3,1)

impath = os.path.join('imgs')

def make_img_path(file_name):
    return os.path.join(impath, file_name)

#transfer random no. to event
def event(cycle, check, event_number, x):
    if event_number in idle_num:
        check = 0
        print('idle')
        window.after(400, update, cycle, check, event_number, x)  # no. 1,2,3,4 = idle
    elif event_number == 5:
        check = 1
        print('from idle to sleep')
        window.after(100, update, cycle, check, event_number, x)  # no. 5 = idle to sleep
    elif event_number in walk_left:
        check = 4
        print('walking towards left')
        window.after(100, update, cycle, check, event_number, x)  # no. 6,7 = walk towards left
    elif event_number in walk_right:
        check = 5
        print('walking towards right')
        window.after(100, update, cycle, check, event_number, x)  # no 8,9 = walk towards right
    elif event_number in sleep_num:
        check  = 2
        print('sleep')
        window.after(1000, update, cycle, check, event_number, x)  # no. 10,11,12,13,15 = sleep
    elif event_number == 14:
        check = 3
        print('from sleep to idle')
        window.after(100, update, cycle, check, event_number, x)  # no. 15 = sleep to idle


#make the gif work
def gif_work(cycle, frames, event_number, first_num, last_num):
    if cycle < len(frames) -1:
        cycle += 1
    else:
        cycle = 0
        event_number = random.randrange(first_num, last_num + 1, 1)

    return cycle, event_number


# remove background color
def remove_background(img):
    img = Image.open(img)
    print(img, type(img))


def update(cycle,check,event_number,x):
    #idle
    if check == 0:
        frame = idle[cycle]
        cycle, event_number = gif_work(cycle, idle, event_number, 1, 9)
    #idle to sleep
    elif check ==1:
        frame = idle_to_sleep[cycle]
        cycle, event_number = gif_work(cycle, idle_to_sleep, event_number, 10, 10)
    #sleep
    elif check == 2:
        frame = sleep[cycle]
        cycle, event_number = gif_work(cycle, sleep, event_number, 10, 15)
    #sleep to idle
    elif check ==3:
        frame = sleep_to_idle[cycle]
        cycle, event_number = gif_work(cycle, sleep_to_idle, event_number, 1, 1)
    #walk toward left
    elif check == 4:
        frame = walk_positive[cycle]
        cycle, event_number = gif_work(cycle, walk_positive, event_number, 1, 9)
        x -= 3
    #walk towards right
    elif check == 5:
        frame = walk_negative[cycle]
        cycle, event_number = gif_work(cycle, walk_negative, event_number, 1, 9)
        x -= -3
    window.geometry('100x100+'+str(x)+'+800')
    label.configure(image=frame)
    window.after(1, event, cycle, check, event_number, x)

window = tk.Tk()
window.wm_attributes('-alpha', 0.5)

#call buddy's action .gif to an array
idle = [tk.PhotoImage(file=make_img_path('idle.gif'), format='gif -index %i' %(i)) for i in range(5)]#idle gif , 5 frames
idle_to_sleep = [tk.PhotoImage(file=make_img_path('will_sleep.gif'), format='gif -index %i' %(i)) for i in range(8)]#idle to sleep gif, 8 frames
sleep = [tk.PhotoImage(file=make_img_path('sleeping.gif'), format='gif -index %i' %(i)) for i in range(3)]#sleep gif, 3 frames
sleep_to_idle = [tk.PhotoImage(file=make_img_path('waking.gif'), format='gif -index %i' %(i)) for i in range(8)]#sleep to idle gif, 8 frames
walk_positive = [tk.PhotoImage(file=make_img_path('walking_left.gif'), format='gif -index %i' %(i)) for i in range(8)]#walk to left gif, 8 frames
walk_negative = [tk.PhotoImage(file=make_img_path('walking_right.gif'), format='gif -index %i' %(i)) for i in range(8)]#walk to right gif, 8 frames

#window configuration
label = tk.Label(window, bd=0, bg='red')

# window.wm_attributes("-transparent", True)
# window.overrideredirect(True)

# button
label.pack()

def mouse_click(event):
    print("mouse clicked", event)


def key_press(event):
    print("key pressing", event)


label.bind("<Button>", mouse_click)
label.bind('<KeyPress>', key_press)
#loop the program
window.after(1, update, cycle, check, event_number, x)
tk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()



