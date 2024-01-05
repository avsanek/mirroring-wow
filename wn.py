import keyboard as kb
import pyautogui as pg
import random
import time
import tkinter as tk

root = tk.Tk()
root.geometry("140x70+1350+75")
root.title("")  # clear the title bar
root.overrideredirect(True)  # remove standard elements (frame, close buttons, etc.)
root.attributes("-topmost", True)  # the window is always above other windows
button = tk.Canvas(root, width=140, height=70)  # color changing canvas
button.pack()
text = button.create_text(70, 35, fill="yellow", font="Times 20 italic bold", text="")


def start_on():
    button.configure(bg='purple')  # changes color to purple during operation
    button.itemconfig(text, text="Chill")


def end_on():
    button.configure(bg='green')
    button.itemconfig(text, text="Yea Buddy!")  # changes color to green when ready


def pause_on():
    button.configure(bg='blue')
    button.itemconfig(text, text="Pause")  # changes color to blue when pause


pg.PAUSE = 0  # removes the delay between up and down a key


def skip():
    pass


def delay_plus_use(funk=skip, funk2=skip, fir=0, sec=0, button=None):  # is used to press the keyboard and mouse or
    if button is None:  # just to take a break
        funk()
        up_mous_interval = random.uniform(fir, sec)
        time.sleep(up_mous_interval)
        funk2()
    else:
        funk(button)
        up_mous_interval = random.uniform(fir, sec)
        time.sleep(up_mous_interval)
        funk2(button)


def delay_plus_mous(win_1_x, win_2_x, win_1_y, win_2_y, fir, sec, funk=skip, dop_delay=None):  # is used to move
    win_2_x = random.uniform(win_1_x, win_2_x)  # the mouse by coordinates or to move the mouse relatively
    win_2_y = random.uniform(win_1_y, win_2_y)
    mousTo_interval = random.uniform(fir, sec)
    funk(win_2_x, win_2_y, mousTo_interval)  # + 0.05
    if dop_delay is not None:
        time.sleep(dop_delay - mousTo_interval)


def auto_run(button_2, button_3):  # it was necessary for automatic running
    pg.keyDown('w')
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyUp('w')
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyDown('w')
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyUp('w')
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyDown(button_2)
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyUp(button_2)
    up_mous_interval = random.uniform(0.06, 0.10)
    time.sleep(up_mous_interval)
    pg.keyDown(button_3)
    up_mous_interval = random.uniform(0.28, 0.32)
    time.sleep(up_mous_interval)
    pg.keyUp(button_3)


def q_e_interval(button_2, button_3): # imitation of sideways movement
    pg.keyDown(button_2)
    up_mous_interval = random.uniform(0.04, 0.06)
    time.sleep(up_mous_interval)
    pg.keyDown(button_3)
    up_mous_interval = random.uniform(0.28, 0.32)
    time.sleep(up_mous_interval)
    pg.keyUp(button_3)
    up_mous_interval = random.uniform(0.04, 0.06)
    time.sleep(up_mous_interval)
    pg.keyUp(button_2)


def back_button(buuton_2, button_3):    # the main function for mirroring clicks
    start_on()
    # first block
    # up key
    delay_plus_use(fir=0.12, sec=0.16)
    # move to monitor
    delay_plus_mous(-555, -187, 222, 422, 0.10, 0.13, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)
    # random mouse movement
    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)
    # second block
    # pressing a key 3
    delay_plus_use(pg.keyDown, pg.keyUp, 0.06, 0.10, buuton_2)
    # move to monitor 2
    delay_plus_mous(-1244, -856, 220, 420, 0.10, 0.13, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)
    # random mouse movement
    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)
    # the third block
    # pressing a key 4
    delay_plus_use(pg.keyDown, pg.keyUp, 0.06, 0.10, button_3)
    # move to monitor 3
    delay_plus_mous(512, 1325, 22, 129, 0.10, 0.13, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)
    end_on()


def back_button_no_delay(buuton_2, button_3):    # the same as (def back_button) but without delay
    start_on()
    # first block
    # up key
    delay_plus_use(fir=0.1, sec=0.1)
    # move to monitor
    delay_plus_mous(-555, -187, 222, 422, 0, 0, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0, 0)
    # random mouse movement
    delay_plus_mous(107, 164, 93, 149, 0, 0, pg.move)
    # second block
    # pressing a key 3
    delay_plus_use(pg.keyDown, pg.keyUp, 0, 0, buuton_2)
    # move to monitor 2
    delay_plus_mous(-1244, -856, 220, 420, 0, 0, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0, 0)
    # random mouse movement
    delay_plus_mous(107, 164, 93, 149, 0, 0, pg.move)
    # the third block
    # pressing a key 4
    delay_plus_use(pg.keyDown, pg.keyUp, 0, 0, button_3)
    # move to monitor 3
    delay_plus_mous(523, 1296, 210, 701, 0, 0, pg.moveTo)
    # mouse click
    delay_plus_use(pg.mouseDown, pg.mouseUp, 0, 0)
    end_on()


def up_wn():                                # duplicate of all keys used
    kb.unhook_all_hotkeys()
    kb.add_hotkey('2', two_wn)
    kb.add_hotkey('1', one_wn)
    kb.add_hotkey('shift+E', shift_e)
    kb.add_hotkey('j', j_wn)
    kb.add_hotkey('left', down_wn)
    kb.add_hotkey('5', five_wn)
    kb.add_hotkey('q', qq_wn)
    kb.add_hotkey('shift+1', shift_1)
    end_on()


def down_wn():                          # pause app - pressing "left" deletes all keys and add "right"
    kb.unhook_all_hotkeys()
    kb.add_hotkey('right', up_wn)       # when use "right" again adds all keys
    pause_on()
kb.add_hotkey('left', down_wn)


def two_wn():                     # when use 2 - are pressed on other monitors 3-4 etc.
    back_button('3', '4')
kb.add_hotkey('2', two_wn)


def one_wn():
    back_button('2', '3')
kb.add_hotkey('1', one_wn)


def five_wn():
    back_button('6', '7')
kb.add_hotkey('5', five_wn)


def qq_wn():
    back_button('4', '5')
kb.add_hotkey('q', qq_wn)


def shift_e():
    back_button('n', 'm')
kb.add_hotkey('shift+E', shift_e)


def shift_1():
    back_button('f6', 'f7')
kb.add_hotkey('shift+1', shift_1)





def shift_q(): # characters stand next to the main character when used
    start_on()

    delay_plus_use(fir=0.12, sec=0.16)

    delay_plus_mous(-555, -187, 222, 422, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)

    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)

    q_e_interval('w', 'e')

    delay_plus_mous(-1244, -856, 220, 420, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)

    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)

    q_e_interval('w', 'q')

    delay_plus_mous(523, 1296, 210, 701, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)
    end_on()


def j_wn():   # automatic forward running
    start_on()

    delay_plus_use(fir=0.12, sec=0.16)

    delay_plus_mous(-555, -187, 222, 422, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)

    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)

    auto_run('k', 'e')

    delay_plus_mous(-1244, -856, 220, 420, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)

    delay_plus_mous(107, 164, 93, 149, 0.10, 0.14, pg.move, dop_delay=0.19)

    auto_run('l', 'q')

    delay_plus_mous(523, 1296, 210, 701, 0.10, 0.13, pg.moveTo)

    delay_plus_use(pg.mouseDown, pg.mouseUp, 0.06, 0.10)
    end_on()

kb.add_hotkey('j', j_wn)

root.mainloop()  # method expects events - pressing the keys
# kb.wait()
