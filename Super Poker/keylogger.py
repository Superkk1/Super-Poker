from pynput import keyboard
from pynput.mouse import Listener
import sys




def on_press(key):
    f = open("strokes.txt", "r")
    fs= str(f.read())
    if fs != "stopreading":

        try:
            print('alphanumeric key {0} pressed'.format(
                key.char))
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

def on_release(key):
   clog = False
   print('{0} released'.format(key))

   f = open("strokes.txt", "r")
   fs= str(f.read())
   if fs == "stoplistening":
    clog = True
    f = open("strokes.txt", "w")
    f.write(str('f released'))
    f.close()
   else:
       f = open("strokes.txt", "w")
       f.write(str('{0} released'.format(key)))
       f.close()
       print('{0} released'.format(key))
   if clog:
    print("clog is "+str(clog))
   if key == keyboard.Key.esc or clog:
       # Stop listener
       print("branch")
       return False
       sys.exit()





def startlistening():
    
    

    with keyboard.Listener(
              on_press=on_press,
              on_release=on_release) as listener:
          print("listener is "+str(listener))
          if listener == False:
            print("call to the branch")
            listener.stop()
          listener.join()
     
      # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)   




    
    

        

