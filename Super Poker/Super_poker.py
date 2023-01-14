import random
import threading
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from PIL import Image, ImageSequence
from tkinter import BOTH, W, NW, SUNKEN, TOP, X, FLAT, LEFT
import tkinter.font as tkFont
import time
import threading 
from AnimatedGif import *
import base64
from pynput import keyboard
from keylogger import *
import sys


sys.stdout = open('log.txt', 'w')

ng = open("strokes.txt","r")
ng = open("strokes.txt","w")
ng.write("new")
ng.close()



def quitgame():
  j = open("strokes.txt", "r")
  j = open("strokes.txt", "w")
  j.write("stoplistening")
  j.close()
  print("It quit")
  sys.exit()

def quitprogram():
  protocol = False
  j = open("strokes.txt", "r")
  j = open("strokes.txt", "w")
  j.write("stoplistening")
  j.close()
  print("It quit")

  nextscreen()

  
root = Tk()
root.iconphoto(False, PhotoImage(file="titleart.png"))
root.title("Super Poker v1.0 ")
root.geometry("500x500")
root.configure(background="white")
filename1  = PhotoImage(file= "titlebg.png")
background_label1 = Label(root, image=filename1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)
protocol = True

root.protocol("WM_DELETE_WINDOW", quitprogram)

bg=Canvas(root, bg="white", height=500, width=500)

imt = Image.open("SuperPoker_titleart.png")
rest = imt.resize((500,500), Image.ANTIALIAS)
game_title = ImageTk.PhotoImage(image= rest)

background_label = Label(root, image=game_title)



ag = Canvas(root, height=0, width=0)


    
def titlescreen():
  global titlebg
  global startbtn
  global bg
  global t
  global greet
  global msg



  bg.pack_forget()
  background_label.configure(image= game_title)
  f = tkFont.Font(family="Lobster", size=20)
  greet = Label(root, text="Super Poker", font=f)
  
  startbtn = Button(root, bg = "White", text="start", command=nextscreen)
 
  startbtn.configure(width = 10, relief=SUNKEN, activebackground = "#F9F9F9")
  
  bg.create_window(425,50, window=startbtn)
  ctitle= background_label
  titlebg = bg.create_window(250,250, window=ctitle)

  bg.pack()
  

def nextscreen():
  
  srokeschk = open("strokes.txt", "r")
  stro= str(srokeschk.read())

  if stro == "stoplistening":

    bg.delete("all")
    srokeschk.close()
    root.quit()
    root.destroy()

  else:


  

    msg="Press 'Play' to start the game"
    def hider(b):
      bg.itemconfig(b, state="hidden")
    def show(b):
      bg.itemconfig(b, state="normal")
    startbtn.destroy()
    greet.destroy()
    bg.delete(titlebg)
    
    

    im = PhotoImage(file= "box.png")
    back =PhotoImage(file= "back of card.png")
    acesp = PhotoImage(file= "ace of spades.png")
    bg.create_image(75, 425, image=im)
    bg.create_image(425, 75, image=im)
    opponentc1= bg.create_image(300, 75, image=back)
    opponentc2= bg.create_image(225, 75, image=back)
    playerc1= bg.create_image(200, 425)
    playerc2= bg.create_image(275, 425)
    c1 = bg.create_image(400, 250)
    c2=bg.create_image(325, 250)
    c3=bg.create_image(250, 250)
    c4=bg.create_image(175, 250)
    c5=bg.create_image(100, 250)
    cfont = tkFont.Font(family="Helvetica", size=8)
    pc =bg.create_text(40, 340, text="Chips: 500", fill="black", font=(cfont))
    oc =bg.create_text(390, 160, text="Chips: 500", fill="black", font=(cfont))
    poticon = bg.create_text(40, 100, text="Pot: 0", font=(cfont))
    betentry = tk.Entry(root, text = "place your bet", width = 15)
    bbtn = Button(root, text = "Place bet", bg = "#F4F9F0", command=lambda: var.set(1))
    bbtn.configure(width=7, activebackground = "lightgray")
    bf= tkFont.Font(family="Helvetica", size=7)
    sf= tkFont.Font(family="Helvetica", size=7)
    ancer = bg.create_text(95,50, text=msg, fill="black",font=(sf))
    betbtn =bg.create_window(370, 420, window=bbtn)
    betinp = bg.create_window(85, 70, window=betentry)



    bg.itemconfig(betinp, state="hidden")
    bg.itemconfig(betbtn, state="hidden" )
    bg.pack()
    

    class coupler:
      def __init__(self, series):
        self.series = series
      def setcouple(self, series):
        self.series=series
      def getcouple(self):
        return self.series

    global ocouple
    ocouple = coupler([])
    global pcouple
    pcouple = coupler([])
    class ans:
      def __init__(self, res):
        self.res = res
      def response(self, res):
        self.res=res
      def getres(self):
        return self.res

    def pause():
      root.after(2000)


    responder = ans("")
    var = tk.IntVar()

    announcerbox = PhotoImage(file= "announcerbox.png")

    enterIcon = PhotoImage(file= "entericon.png")
    noIcon = PhotoImage(file= "fIcon.png")
    raiseIcon = PhotoImage(file= "rIcon.png")
    bgeicon = bg.create_image(370, 390, image=enterIcon)
    bgnicon = bg.create_image(420, 390, image=noIcon)
    bgricon = bg.create_image(370, 490, image=raiseIcon)
    plybtn = Button(root, text = "play", bg = "#F4F9F0", command=lambda:[threading.Thread(target=var.set(1)).start()])
    plybtn.configure(relief=FLAT, activebackground = "lightgray")
    ybtn = Button(root, text = "Yes", bg = "#F4F9F0", command=lambda:[ var.set(1), responder.response("Y")])
    ybtn.configure(width = 4, activebackground = "lightgray")
    nbtn = Button(root, text = "Fold", bg = "#F4F9F0", command=lambda:[ var.set(1), responder.response("N")])
    rbtn = Button(root, text = "Raise", bg = "#F4F9F0", command=lambda:[ var.set(1), responder.response("R")])
    nbtn.configure(width = 4, activebackground = "lightgray")
    playbtn =bg.create_window(420, 460, window=plybtn)
    yesbtn =bg.create_window(370, 420, window=ybtn)
    nobtn =bg.create_window(420, 420, window=nbtn)
    raisebtn= bg.create_window(370, 460, window=rbtn)

    
    hider(raisebtn)
    hider(yesbtn)
    hider(nobtn)
    hider(bgeicon)
    hider(bgnicon)
    hider(bgricon)



    def textgetter(file):
      insults = open(file)

      for line in insults:
        split=line.split(",")

      winner = split[random.randint(0,len(split)-1)]
      split1 = winner.split("*")

      if len(split1)>1:
        winner = split1[0]+"\n"+split1[1]
     
      return winner




    def update(a, p):
      print("call")
      if p:
        bg.itemconfig(pc, text ="Chips: "+str(a))
      elif a >=0:
        bg.itemconfig(oc, text="Chips: "+str(a))
      else:
        print("oops "+str(a))
        bg.itemconfig(oc, text="Chips: 0")


      
    def updatean(t):
      bg.itemconfig(ancer, text=t)
      
    def upot(t):
      bg.itemconfig(poticon, text="Pot: "+str(t))
      
    def tempmsg(a, b):
      var = IntVar()
      root.after(b, var.set, 1)
      updatean(a)
      root.wait_variable(var)

    
    def updatepool(card, pos):
      cardpos = pos+1
      
      global poolreader1
      global poolreader2
      global poolreader3
      global poolreader4
      global poolreader5
      
      if cardpos >= 1:
        poolreader1 = PhotoImage(file= card[0]+".png")
        bg.itemconfig(c1, image=poolreader1)
        
        if cardpos >= 2:
          poolreader2 = PhotoImage(file= card[1]+".png")
          bg.itemconfig(c2, image=poolreader2)     
          if cardpos >= 3:
            poolreader3 = PhotoImage(file= card[2]+".png")
            bg.itemconfig(c3, image=poolreader3)          
            if cardpos >= 4:
              poolreader4 = PhotoImage(file= card[3]+".png")
              bg.itemconfig(c4, image=poolreader4)
              if cardpos >= 5:
                poolreader5 = PhotoImage(file= card[4]+".png")
                bg.itemconfig(c5, image=poolreader5)
    

    def wipepool():
      bg.itemconfig(c1, image=blank)
      bg.itemconfig(c2, image=blank)
      bg.itemconfig(c3, image=blank)
      bg.itemconfig(c4, image=blank)
      bg.itemconfig(c5, image=blank)
      print("Its not working")




    def deck(a):
      global cardreader1
      global cardreader2
      cardreader1 = PhotoImage(file=a[0]+".png")
      cardreader2 = PhotoImage(file=a[1]+".png")
      bg.itemconfig(playerc1, image=cardreader1)
      bg.itemconfig(playerc2, image=cardreader2)

    def showdeck(b):
      global ocardreader1
      global ocardreader2
      ocardreader1 = PhotoImage(file=b[0]+".png")
      ocardreader2 = PhotoImage(file=b[1]+".png")
      bg.itemconfig(opponentc1, image=ocardreader1)
      bg.itemconfig(opponentc2, image=ocardreader2)


    def wipedeck():
      global blank 
      blank = PhotoImage(file="blank.png")
      bg.itemconfig(opponentc1, image=blank)
      bg.itemconfig(opponentc2, image=blank)
      bg.itemconfig(playerc1, image=blank)
      bg.itemconfig(playerc2, image=blank)
      print("Its not working")
    
    
    
    def convert(a):
      for c in a:
      
        if type(c)==str:
          if c == "jack":
            a[a.index(c)] = 11
          if c == "queen":
            a[a.index(c)] = 12
          if c == "king":
            a[a.index(c)] = 13
          if c == "ace":
            a[a.index(c)] = 14

    #Try to figure out threading and finding a fix for .after()
    #For the love of god please add conspiranoia to this game
    class sprite:
      global spriteico
      
      def __init__(self, a, x, y, l, w):
        self.a = a
        self.x = x
        self.y = y
        self.l = l
        self.w = w
        playicp= (Image.open(a))
        pres= playicp.resize((l,w), Image.ANTIALIAS)
        self.spriteico = ImageTk.PhotoImage(image = pres)
        self.plbl= Label(root, image=self.spriteico)
        
        
        playericon = bg.create_window(x, y, window= self.plbl)

      def updatesprite(self, n):
        playicp= (Image.open(n))
        pres= playicp.resize((self.l,self.w), Image.ANTIALIAS)
        self.spriteico = ImageTk.PhotoImage(image = pres)
        self.plbl= Label(root, image=self.spriteico)

        bg.create_window(self.x, self.y, window= self.plbl)



      def animator(self, f, delay):

        try:
          if f.index("Sr_")==0:
            root.after(1000, self.updatesprite("Sr_poker.png"))
            self.updatesprite(f)
            return 0
        except ValueError:
          print("")

        self.delay=delay
        self.idlechk = 0
        
        try: 
          f.index("s_")==0
          self.idlechk = 1

        except ValueError:
          print("")

        try:
          f.index("a_")==0
          self.idlechk = 2

        except ValueError:
          print("")
        
        self.f = f
        self.sp = (Image.open(self.f))
       
        self.size = self.l, self.w
        self.frames2 = ImageSequence.Iterator(self.sp)

        def thumbnails(frames):
            for frame in frames:
                self.thumbnail = frame.copy()
                self.thumbnail.thumbnail(self.size, Image.ANTIALIAS)
                yield self.thumbnail

        self.frames2 = thumbnails(self.frames2)

        
        self.om = next(self.frames2) 
        self.om.info = self.sp.info 
        
        self.om.save(f, save_all=True, append_images=list(self.frames2)) 
         
        self.file1 = f

        enddelay = .1

        try: 
         self.file1.index("response")>=0
         enddelay = 1

        except ValueError:
          print("")
        
        
        self.plbl= AnimatedGif(root, self.spriteico, self.file1, self.delay, enddelay)
       

        
        
        bg.create_window(self.x, self.y, window=self.plbl)
        
        if self.idlechk == 1:
          self.plbl.start_thread()
        elif self.idlechk == 2:
          self.plbl.start_angus()
        else:
          self.plbl.start()
      
      def stop(self):
          self.plbl.stop_thread()
     
      def updatesp(self, file):
        self.spriteico = file
          
        

    imgbg= (Image.open("normalbg.png"))
    aimgbg= (Image.open("anglusbg.png"))
    simgbg= (Image.open("sr_pokerbg.png"))
    res= imgbg.resize((2000,2005), Image.ANTIALIAS)
    ares= aimgbg.resize((2000,2005), Image.ANTIALIAS)
    sres= simgbg.resize((2000,2005), Image.ANTIALIAS)
    fbg = ImageTk.PhotoImage(image= res)
    angbg = ImageTk.PhotoImage(image= ares)
    srpbg = ImageTk.PhotoImage(image= sres)
    background_label1.configure(image=fbg)

    playersp = sprite("The Player concept 2.png", 69, 430, 119, 119)
    opponentsp= sprite("The Opponent concept.png", 420, 80, 120,120)

    keys = threading.Thread(target=startlistening) 
    keys.start()
    


    def inpenter():

      j = open("strokes.txt", "r")
      j = open("strokes.txt", "w")
      j.write("")

      while True:

        j = open("strokes.txt", "r")
        junction = str(j.read() )
        j.close()
      
        if (junction == "Key.enter released" or junction == "special key Key.enter pressed") and junction !="":

          print("|-------------V~~~~MM`___+==------>>\n< ~    -- BOOOM ~   -   `` ` ` ~\nV----==------=v=-=-vwW-==-=-=-")
          print("Junction for enter is "+junction)
          responder.response("Y")
          j = open("strokes.txt", "w")
          j.write("")
          j.close()
          var.set(1)
        if junction == "stoplistening":
          break


    def inpr(cork): 

      j = open("strokes.txt", "r")
      j = open("strokes.txt", "w")
      j.write("")

      while True:

        if cork():
          break

        j = open("strokes.txt", "r")
        junction = str(j.read() )
        j.close()

        if (junction == "'r' released") and junction != "":

          responder.response("R")
          j = open("strokes.txt", "w")
          j.write("")
          j.close()
          var.set(1)
          

    def inpf(plug):

      j = open("strokes.txt", "r")
      j = open("strokes.txt", "w")
      j.write("")

      while True:

        if plug():
          break 

        j = open("strokes.txt", "r")
        junction = str(j.read() )
        j.close()

        
        if (junction == "'f' released") and junction != "":

          print("it was inpf")
          print("new Junction for fold is "+junction)
          responder.response("N")
          j = open("strokes.txt", "w")
          j.write("")
          j.close()
          var.set(1)
          


    


    
    def dupechk(a):     #test this 
      global dupes
      dupes=[]
      val = []
      val = a

      count = 0
      previous = []

      for c in val:
        
        print(val)


        for i in previous:

            if str(c) == str(i):

              count+=1
              dupes.append(c)
            print(str(i)+" and "+str(c))
          
        previous.append(str(c))
      
    
      return count


    def breadicide(chips):
      global direstakes
      global allin
      allin = False
      key = True
      global reasonablebet
      reasonablebet = True
      if chips==0 or ochips==0:
          reasonablebet = False
          key=False
          return 0
      while key:
        bet = 0
        
        while True:
          
          msg="How much would you like to bet? "
          
          betentry.delete(0, END)
          updatean(msg)
          show(betinp)
          show(betbtn)
          hider(yesbtn)
          hider(nobtn)
          hider(raisebtn)
          hider(bgnicon)
          hider(bgricon)
          betentry.icursor(0)

          bbtn.wait_variable(var)
          inp = betentry.get()
          betentry.select_clear()
          
          try:
            bet = int(inp)
            break
          except ValueError:
            msg ="Not valid"
            tempmsg(msg, 1000)
            msg = "How much would you like to bet?"
            updatean(msg)
          
        if bet<=0:
          msg="You're not funny"
          tempmsg(msg, 1000)
          msg = "How much would you like to bet?"
          updatean(msg)
          
          
        elif(bet>chips):
          tempmsg("You don't have that much chips", 1000)
          print(chips)
        
        else:
          if bet ==chips:
             direstakes = True
             allin = True     
             hider(betbtn)
             hider(betinp)
             hider(bgeicon)
             tempmsg("All In? Good luck.", 1000)
             print("All in call")


          key = False  
        hider(betinp)    
        
      return bet


    def validbet(stakeslist, stakesturn, opraiseflag):
        finish = True
        count = 1
        diff = 1
        opm = obet
        if opraiseflag:
          opm = 0

        while(finish):
          stupidity = random.randint(1,9)
          if stakeslist[len(stakeslist)-1]>0 and stupidity <= 5 and stakesturn:
            hothands = random.randint(0, stakeslist[len(stakeslist)-1])
            stupidity=+stakeslist[len(stakeslist)-1] + hothands
          finalraise = stupidity*pow(10, len(str(obet))-diff)
          count+=1
          print("Idiot finalraise is "+str(finalraise) + " and obet is "+str(obet) +" and ochips is "+str(ochips)+ " chips is "+str(chips)+ " bet is "+str(bet)+" opm is "+str(opm))

          if(finalraise+opm <= ochips and finalraise <= chips and finalraise != 0):
            finish = False
          if (count % 30 == 0):
            diff+=1
         
              
        
        print("The opponent bets "+str(finalraise))
        return int(finalraise)

    def createpool():
      global winhands
      winhands = ["It's a High Card", "It's a pair", "It's a two pair", "It's a three of a kind", "It's a straight", "It's a flush", "It's a full house", "It's a four of a kind", "It's a striaght flush"]
      global cardvalues
      cardvalues = [2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace"]
      global suits
      suits = ["hearts", "spades", "clubs", "diamonds"]
      random.seed()
      turns = 0
      global vals
      vals = []
      global s
      s = []
      global l
      l=[]

      while turns <5:
        value=cardvalues[random.randint(0, len(cardvalues)-1)]
        suit=suits[random.randint(0, len(suits)-1)]
        h = str(value)+" of "+suit
        l.append(h)
        value1=value
        if type(value)==str:
          if value == "jack":
            value1 = 11
          if value == "queen":
            value1 = 12
          if value == "king":
            value1 = 13
          if value == "ace":
            value1 = 14

        vals.append(value1)
        s.append(suit)
          
        turns+=1
          
        if turns==4 and dupechk(l)>2:
          l.clear()
          turns=0

    #Where the sorceries of hand checking takes place.
    def hndchk(als, b):
      comb = dupechk(als)   
      print("current hand: "+str(als))
      print("comb ="+str(comb))
      comb = dupechk(als)
      als.sort()
      wheel=als.copy()
      stvals=als.copy()
      stvals.sort()
      stick=0
      attempts = len(stvals)-5
      straight= True
      while stick<len(stvals)-1:
        if stvals[stick]+1==stvals[stick+1]:
          stick+=1
          
        elif attempts>0:
          stvals.pop(stick)
          attempts-=1
        else:
          straight = False
          break

      wheel.sort()
      wh = len(wheel)-5
      while wh>0:
        wheel.pop(4)
        wh-=1
      if wheel == [2, 3, 4, 5, 14]:
        straight == True

      
      if straight:
        winval=3
        return winval

      if comb>=4:
        svals=als.copy()
        svals.sort()
        
        svals.pop(4)
        svals.pop(0)
        if dupechk(svals)==1:
                  
            winval=5
            dupechk(als)
            if b:
             pcouple.setcouple(dupes)
            else:
             ocouple.setcouple(dupes)
        else:      
          winval =6
          dupechk(als)
          if b:
           pcouple.setcouple(dupes)
          else:
            ocouple.setcouple(dupes)
      elif comb>=2:
        svals=als.copy()      
        svals.sort()
        fnum = svals[0]
        lnum = svals[4]
        svals.pop(4)
        svals.pop(0)  
        winval=1
        dupechk(als)
        if b:
          pcouple.setcouple(dupes)
        else:
          ocouple.setcouple(dupes)

        print("svals: "+str(svals))
        print(dupechk(svals))
        if (dupechk(svals)==3):
          winval=2
          dupechk(als)
          if b:
            pcouple.setcouple(dupes)
          else:
            ocouple.setcouple(dupes)
        elif dupechk(svals)>0:
          if fnum==svals[0]:
            svals.pop(2)
            svals.append(fnum)
            if dupechk(svals)==3:
              winval=2
              dupechk(als)
              if b:
                pcouple.setcouple(dupes)
              else:
                ocouple.setcouple(dupes)

          elif lnum==svals[2]:
            svals.pop(0)
            svals.append(lnum)
            if dupechk(svals)==3:
              winval=2
              dupechk(als)
              if b:
                pcouple.setcouple(dupes)
              else:
                ocouple.setcouple(dupes)
          print("lnum: "+str(lnum))
          print("fnum: "+str(fnum))
        
      elif comb==1:
        winval=0
        dupechk(als)
        dupes.append(dupes[0])
        if b:
          pcouple.setcouple(dupes)
        else:
          ocouple.setcouple(dupes)

      else:
        svals=als
        svals.sort()
        highcard=svals[len(svals)-1]
        winval=-1
      print(winval)
      return winval


    def flushchk(lis, fsuits, fhand, samesuits, shndchk):  #checks for flush
     straightflsh = False
     vals2=s.copy()
     for n in fsuits:
       vals2.append(n)
     vals2.sort()
     print(vals2)
     print(dupechk(vals2))
     elim = []
     weight = []
     for i in range(3):
       elim.append(vals2.copy())
     elim[0].pop(0)
     elim[0].pop(0)
     elim[1].pop(0)
     elim[1].pop(5)
     elim[2].pop(5)
     elim[2].pop(5)
     flsh = False
     for i in elim:
       flushgauge = dupechk(i)
       weight = dupechk(dupes)
       print("Weight is "+str(weight))
     
       if flushgauge==10 and weight > 15:
         flsh=True
         welim = i
     if flsh:
           print("flush is calling")
           
           samesuits = []
           for c in l:
             if c.find(welim[0])>-1:
               cspl=c.split()
               convert(cspl)
               samesuits.append(int(cspl[0]))
           for c in fhand:
             if str(c).find(welim[0])>-1:
               cspl =c.split()
               print(cspl[0])
               convert(cspl)          
               samesuits.append(int(cspl[0]))
           print(samesuits)
           print("hndchk is"+str(hndchk(samesuits, shndchk)))
           if hndchk(samesuits, shndchk)==3:
             straightflsh=True
           if straightflsh:
             if samesuits.count(14)>0 and samesuits.count(13)>0:
               lis.append(8)
             lis.append(7)
           else:
             lis.append(4)



    def circlechk(lis, cirhand, circhk):    #hand checking
      f=0
      while f<len(vals):
        j=0
        while j<len(vals):        
          vals1=vals.copy()        
          convert(vals1)  
          vals1.pop(f)
          vals1.insert(f,cirhand[0])
          if j!=f: 
            vals1.pop(j)          
            vals1.insert(j,cirhand[1])         
            lis.append(hndchk(vals1, circhk))
          j+=1     
        f+=1  
    
    
    def prechk(lis, c, a, b):                #checks the hand delt
    
        f1 =0
        while f1<len(vals):
          pvals=vals.copy()
          convert(pvals)

          pvals.pop(f1)
          if a:
            pvals.insert(f1,c[0])
          else:
            pvals.insert(f1,c[1])
        
          lis.append(hndchk(pvals, b))

          f1+=1
        if a:
           prechk(lis, c, False, b)
      
    residue = []
    suitresidue =[] 

    def gethand():        #dealing the players a hand
      hnd=[]
      s=0
      while s<2:
        value=cardvalues[random.randint(0, len(cardvalues)-1)]
        residue.append(value)
        
        suit=suits[random.randint(0, len(suits)-1)]
        suitresidue.append(suit)
        h = str(value)+" of "+suit
        hnd.append(h)
        s+=1
      return hnd

    
    newround = False
    wincounter = 0
    game = True
    roundcount = 0
    li=[]
    li1 = []
    scanybtn = threading.Thread(target=inpenter)
    scanybtn.start()
    plybtn.wait_variable(var)
    plybtn.destroy()
    show(yesbtn)
    show(nobtn)
    show(bgeicon)
    show(bgnicon)
    global chips
    global ochips
    chips = 500
    ochips= 500
    chiptotal = 1000
    while game:
      
      print("chips is "+str(chips))



      if newround:        
        ochips = chips - random.randint(-200, 200)
        if wincounter == 2:
          ochips = 3000
        chiptotal = chips + ochips
        newround = False

      print("ochips is "+str(ochips))
      print("chiptotal is "+str(chiptotal))
      chips-=10
      ochips-=10



      if ochips > 10 and chips > 10:
        chiptotal -= 20
      else:
        if ochips > 10:
          chiptotal -= 10
        elif ochips > 0:
          chiptotal-=ochips

        if chips > 10:
          chiptotal-=10
        elif chips > 0:
          chiptotal -= chips
        




      update(chips, True)
      update(ochips, False)
      createpool()
      bg.itemconfig(opponentc1, image=back)
      bg.itemconfig(opponentc2, image=back)



      if wincounter == 1:


       opponentsp.stop()
       background_label1.configure(image=angbg)
       opponentsp.updatesprite("Angus.png")
       raiseanim = "Angus_raise.gif"
       badresponse = "Angus_badresponse_t.gif"
       goodresponse = "Angus_raise.gif"
       opponentsp.animator("a_Angus_idle_t.gif", .07)
      elif wincounter == 2:
        
        update(ochips, False)
        background_label1.configure(image=srpbg)
        try:
          opponentsp.stop()
        except AttributeError:
          print("")
        opponentsp.updatesprite("Sr_poker.png")
        raiseanim = "Sr_poker_goodresponse.png"
        goodresponse = "Sr_poker_goodresponse.png"
        badresponse = "Sr_poker_badresponse.png"
      else:
       raiseanim = "opponent_raise.gif"
       goodresponse = "opponent_goodresponse.gif"
       badresponse = "s_opponent_idle.gif"
       opponentsp.animator("s_opponent_idle.gif", .05)
       
      playersp.animator("s_player_idle.gif", .5)
      
      loser = False
      realisticdeck = False
      deckchk= []
      while realisticdeck == False:
        createpool()
        phand = gethand()
        p = residue.copy()
        ps= suitresidue.copy()
        residue.clear()
        suitresidue.clear()
        ohand = gethand()
        o = residue.copy()
        os = suitresidue.copy()
        suitresidue.clear()
        residue.clear()
        deckchk+=phand.copy()
        deckchk+=ohand.copy()
        deckchk+=l.copy()
        print("deckchk is "+str(deckchk))
        print("dupechk(deckchk) is "+str(dupechk(deckchk)))
        if dupechk(deckchk) == 0:
          print("It's good")
          realisticdeck = True
        deckchk.clear()
      chand = p
      cohand = o
      csuits=ps
      cosuits=os
     
      convert(cohand)
      convert(chand)
      
      pot=0
      upot(pot)
      print("This is your hand: "+str(phand)+"\n")
      deck(phand)
      print("You have "+str(chips)+" chips.\n")
      t=0
      
      
      direstakes= False

      st = ""
      while t<6:
        opdecision = True
        print("direstakes is "+str(direstakes))
        if chips <= 0 or ochips <= 0:
          direstakes = True
        if ((t<6 and t>=3) or t==0) and direstakes == False:
          if t % 2 == 0:  #this means player turn
            
            print("Direstakes isn't working"+ str(direstakes))
            betentry.delete(0,END)
            hider(betinp)
            hider(betbtn)
            show(yesbtn)
            show(nobtn)
            show(bgnicon)
            show(bgeicon)

            plug = False

            scanfbtn = threading.Thread(target=inpf, args = (lambda: plug, ))

            if ~scanfbtn.is_alive():
              scanfbtn.start()

            msg="Would you like to play your hand?"
            print(ochips)
            updatean(msg)
            ybtn.wait_variable(var)
            inp =responder.getres()

            plug = True
          
            if inp=="Y":
              print("")
            elif inp=="N":
              loser= True
              break
            

            stakes = True
            bet=breadicide(chips)
            print("bet is "+str(bet)+" direstajes is "+str(direstakes))
            chips-=bet

            
            obet = 0
            if bet-chips==0 or ochips-bet<=0:
              print("This is what you're looking for, t is "+str(t))
              stakes=False
              direstakes = True
              obet = bet
              if obet>ochips:
                obet=ochips
              if ochips-bet<= 0:
                ochips = 0

            print("direstakes is "+str(direstakes)+"allin is "+str(allin))
            if allin:
              print("this called")
              ochips -= bet
              obet = bet
              if ochips < 0:
                ochips = 0
              if ochips < 10:
                obet = ochips
                ochips = 0
              print("chiptotal is "+str(chiptotal))
              print("obet is "+str(obet))
              print("pot before "+str(pot))
              pot = chiptotal - (chips + ochips)
              print("pot after "+str(pot))
              upot(pot)
              update(chips, True)
              update(ochips, False)
              break


            if ochips<=0 or ochips-obet<=0:
              stakes=False

            stakesturn = True
            certainty = False
          elif t % 2 != 0:
            if ochips>0:
              hider(bgeicon)
              hider(bgnicon)
              hider(betbtn)
              hider(yesbtn)
              hider(nobtn)
              for i in range(3):
                tempmsg("The opponent is betting." , 200)
                tempmsg("The opponent is betting.." , 200)
                tempmsg("The opponent is betting..." , 200)         
                stakes = True
                certainty = True
            else:
              bet = breadicide(chips)

          idiocy = 0      
          raised = False
          opraiseflag = False

          while stakes and allin == False:

            hider(bgeicon)
            hider(bgnicon)
            hider(betbtn)

            impulse = random.randint(0,10)
            if certainty == True:

              impulse = 1
              stakesturn = False                #possible folding?
            think = textgetter("pondering.csv")
            for i in range(3):

              tempmsg(think+"." , 200)
              tempmsg(think+".." , 200)
              tempmsg(think+"..." , 200)

            stakeslist=[0]
            if stakesturn:
              f=0
              while f<len(vals):
                j=0      
                while j<len(vals):  
                  vals2=vals.copy()
                  convert(vals2)               
                  vals2.pop(f)
                  vals2.insert(f,cohand[0])
                  if j!=f: 
                    vals2.pop(j)        
                    vals2.insert(j,cohand[1])         
                    stakeslist.append(hndchk(vals2,False))  
                  j+=1
                f+=1  
              stakeslist.sort()
              print("impulse is " +str(impulse))
              impulse= impulse-(stakeslist[len(stakeslist)-1]+1)

              obet = bet
            #tempmsg("Impulse is "+str(impulse), 1000)
            
            print("786")
            if impulse <=5:
              
              
              if certainty == True:
                obet = random.randint( 1 , ochips)

              if (t % 2 != 0) and (opraiseflag):
                obet = bet
                ochips-=obet
                print("It is the opponents turn and ")

              if (obet != ochips) and direstakes:
                stupidity1 = validbet(stakeslist, stakesturn, opraiseflag)
              else:
                stupidity1=obet

              if certainty == False or opraiseflag:

               msg ="Your opponent raised the\n stakes by "+str(stupidity1)+"!\n"  #also culprit?
               print("Your opponent raised the\n stakes by "+str(stupidity1)+"!\n")
               rasied = True
               opmm = obet
               if opraiseflag:
                opmm = 0
               oppstakes = opmm + stupidity1
               print(str(ochips)+" minus "+str(oppstakes))
               ochips -= oppstakes
               print("New ochip value is" + str(ochips))
               update(ochips, False)
               update(chips, True)           
              else:
                msg ="Your opponent bets "+ str(obet)+" chips.\n"
                print("Your opponent bets "+ str(obet)+" chips.\n")
                ochips -= obet
                opdecision = False

              stakesturn = False
              opponentsp.animator(raiseanim, .05) 
              hider(betbtn)
              hider(betinp)
              tempmsg(msg, 2000)
              update(ochips, False)
         
              msg="What will you do?"

                                          #keep an eye on this
             
              updatean(msg)
              show(bgnicon)
              show(bgeicon)
              show(bgricon)
              show(yesbtn)
              show(nobtn)
              show(raisebtn)
              ybtn['text']= "Call"
              nbtn['text']= "Fold"

              cork = False
              plug = False

              scanrbtn = threading.Thread(target=inpr, args = (lambda : cork, ))
              scanfbtn = threading.Thread(target=inpf, args = (lambda: plug, ))

              if ~scanrbtn.is_alive():
                scanrbtn.start()

              if ~scanfbtn.is_alive():
                scanfbtn.start()
              
              root.wait_variable(var)


              inp =responder.getres()

              cork = True
              plug = True
     
              if inp == "Y":
                raised = True
                stakes = False
                print("Stupidity is "+str(stupidity1))       
                if bet>chips:
                  bet=chips
                if (t % 2 != 0) and opraiseflag == False:
                  stupidity1 = obet
    
                chips -= stupidity1
                update(ochips, False)
                update(chips, True)

              elif inp == "R":
                if (t % 2 != 0) and opraiseflag == False:
                  opraiseflag = True
                  stupidity1 = obet
                if chips-stupidity1<=0:
                    tempmsg("You cannot raise anymore", 2000)
                    chips = 0
                    update(chips, True)
                    stakes = False
                elif chips != 0:
                  stakesturn = True


                  chips -= stupidity1
                  update(chips, True)
                  bet = breadicide(chips)
                  chips -= bet
                  if t % 2 != 0 and allin:
                    ochips-=bet
                  update(chips, True)
                else:
                  stakes = False
                if(chips == 0):
                  stakes = False
              elif inp == "N":
                loser = True
                break
              hider(yesbtn)
              hider(nobtn)
              hider(bgnicon)
              hider(bgeicon)
              hider(bgricon)
            else:         
              stakes = False


          if reasonablebet:
            if (raised==False):
              print("this called ochips: "+str(ochips)+" obet "+ str(obet))
              if opdecision:
                ochips-=obet

            if ochips < 0:
              ochips = 0
            if chips < 0:
              chips = 0

            print("Chiptotal is "+str(chiptotal)+" chips is "+str(chips)+" ochips is "+str(ochips))
            pot = chiptotal - (chips+ochips)
            upot(pot)
            print(raised)
   
            update(ochips, False)
            update(chips, True)
            if loser == True:
              break
            
        ybtn['text']= "Yes"
        nbtn['text']= "Fold"
        hider(raisebtn)
        if t<5:
          st += " |"+l[t]+"|"
          updatepool(l, t)
        print("You have "+str(chips)+" chips.\n")
        print("There is "+str(pot)+" chips in the pot\n")
        t+=1
        print("Current draw:")
        print(st)
        show(yesbtn)
        show(nobtn)

        
      f=0
      
      hider(yesbtn)
      hider(nobtn)
      hider(raisebtn)
      hider(bgricon)
      hider(bgeicon)
      hider(bgnicon)
      while t<5:
        updatepool(l,t)
        t+=1
      
      samesuits = []
      osamesuits = []
      
      print("Player hand checker:")
      prechk(li, chand, True, True)
      circlechk(li, chand, True)
      flushchk(li, csuits, chand, samesuits, True)

      print("Opponent hand checker")
      prechk(li1, cohand, True, False)
      circlechk(li1, cohand, False)
      flushchk(li1, cosuits, ohand, osamesuits, False)
    
      hider(betbtn)
      hider(betinp)
      print(pcouple.getcouple())
      print(ocouple.getcouple())
      print(li)
      print(li1)
      print("Your opponent's hand: ")
      print(ohand) 
      print("Your hothands:")
      print(chand)

      li.sort()
      if loser==False:  #this checks the winvals
        pw ="For you"

        for i in range(len(winhands)):
          if li[len(li)-1] + 1 == i:
            pw2 = winhands[i]

        if li[len(li)-1]==8:
          pw2="Holy Smokes!\nYou got a royal flush!"
      else:
        pw2=""
        pw="You folded"
      po = pw+" "+pw2
      print(po)
      print(len(li)-1)
      tempmsg(po, 2000)

      
      tempmsg("For your opponent", 2000)
      if badresponse != "Sr_poker_badresponse.png":
       opponentsp.stop()
      playersp.stop()
      
      li1.sort()
      for i in range(len(winhands)):
        if li1[len(li1)-1] + 1 == i:
          ow2 = winhands[i]

      if li1[len(li1)-1]==8:
        ow2="Holy Smokes!\nThey got a royal flush!"
     

      oo = ow2
      print(oo)
      print(len(li1)-1)
      showdeck(ohand)
      tempmsg(oo, 2000)
      chand.sort()
      cohand.sort()
      li.sort()
      li1.sort()
      champ= -1
      tiehappened = False
      if loser==False:

        #temporary                                                                    #champ 0 means player wins and 1 the opponent
        while True:

          if (li[len(li)-1]==li1[len(li1)-1]) and li[len(li)-1]>-1 and li1[len(li1)-1]>-1:  #Conflict with same winval
            if (li[len(li)-1]==4 and li1[len(li1)-1]==4):                                   #If both are flush
              samesuits.sort()
              osamesuits.sort()
              try:
                if samesuits[4]>osamesuits[4]:
                  champ = 0
                  break
                elif samesuits[4]<osamesuits[4]:
                  champ=1
                  break
              except IndexError:
                print("")
            elif chand[1]>cohand[1]:
              champ=0 


              print(" its calling"+ str(pcouple.getcouple()))
              print(" its calling"+ str(ocouple.getcouple()))
              pcouple1 = pcouple.getcouple()
              ocouple1= ocouple.getcouple()
              pcouple1.sort()
              ocouple1.sort()

              #temporary


              print("pcouple1 is"+str(pcouple1))
              print("ocouple1 is"+str(ocouple1))

              if pcouple1[len(pcouple1)-1]>ocouple1[len(ocouple1)-1]:                     #check whoever has the higher card
              
                  champ=0
                  break
              elif pcouple1[len(pcouple1)-1]<ocouple1[len(ocouple1)-1]:
                  champ=1
                  
                  break
              elif pcouple1[len(pcouple1)-2]>ocouple1[len(ocouple1)-2]:                     #check whoever has the higher card
               
                  champ=0
                  break
              elif pcouple1[len(pcouple1)-2]<ocouple1[len(ocouple1)-2]:
                  champ=1
                  
                  break
                                                                                       
              break

            elif chand[1]<cohand[1]:
              champ=1
              

              print(" its calling"+ str(pcouple.getcouple()))
              print(" its calling"+ str(ocouple.getcouple()))
              pcouple1 = pcouple.getcouple()
              ocouple1= ocouple.getcouple()
              pcouple1.sort()
              ocouple1.sort()

              #temporary



              print("1pcouple1 is"+str(pcouple1))
              print("1ocouple1 is"+str(ocouple1))

              if pcouple1[len(pcouple1)-1]>ocouple1[len(ocouple1)-1]:
                  #do something about pcouple-2
                  champ=0
                  break
              elif pcouple1[len(pcouple1)-1]<ocouple1[len(ocouple1)-1]:
                  champ=1
                  
                  break
              elif pcouple1[len(pcouple1)-2]>ocouple1[len(ocouple1)-2]:
                  #do something about pcouple-2
                  champ=0
                  break
              elif pcouple1[len(pcouple1)-2]<ocouple1[len(ocouple1)-2]:
                  champ=1
                  
                  break

              break
          
          print("It switched to this one v")
          if(li[len(li)-1]>li1[len(li1)-1]):
            champ=0
            break
          elif(li[len(li)-1]<li1[len(li1)-1]):
            champ=1
            break
          elif(chand[len(chand)-1]>cohand[len(cohand)-1]): 
            champ=2
            break
          elif(chand[len(chand)-1]<cohand[len(cohand)-1]):
            champ=3
            break
          elif(chand[len(chand)-2]>cohand[len(cohand)-2]):
            champ=2
            break
          elif(chand[len(chand)-2]<cohand[len(cohand)-2]):
            champ=3
            break
          else:
            tempmsg("It's a tie.",2000)
            tiehappened = True
            tiespoils=pot/2
            ochips+=int(tiespoils)
            chips+=int(tiespoils)
            break
      else:
        #figure out why
        champ= 1
        

      if champ==0:
        playersp.animator("player_goodresponse.gif", .05)
        opponentsp.animator(badresponse, .05)
        tempmsg("You won!", 2000)
        print("You won!")
        chips+=pot
      elif champ==1:
        playersp.animator("player_badresponse.gif", .05)
        opponentsp.animator(goodresponse, .05)
        tempmsg("You lose.", 2000)
        print("You lose.")
        ochips+=pot
      elif champ==2:
        playersp.animator("player_goodresponse.gif", .05)
        opponentsp.animator(badresponse, .05)
        tempmsg("You win by high card!", 2000)
        print("You win by high card!")
        chips+=pot
      elif champ==3:
        playersp.animator("player_badresponse.gif", .05)
        opponentsp.animator(goodresponse, .05)
        tempmsg("You lose, your opponent\n wins by high card.",2000)
        ochips+=pot
        print("You lose, your opponent\n wins by high card.")
      elif tiehappened == False:
        tempmsg("Error\nMr.Developer messed up.",2000)
        ochips+=pot/2
        chips+=pot/2
        print("Fix it")



      print("You now have "+str(chips)+" chips.\n")
      update(ochips, False)
      update(chips, True)
      upot(0)
      ybtn['text']= "Yes"
      nbtn['text']= "No"
      show(yesbtn)
      show(nobtn)
      show(bgnicon)
      show(bgeicon)
      print("ochips is now at "+str(ochips))
      print("chips is now at "+str(chips))
      print("the pot is "+str(pot))
  

      
      if ochips<=10:
        msg="Ready for your next opponent?"
        newround = True
      else:
        msg ="Another round?"
      nbtn.configure(text="no")
      updatean(msg)
      
      plug = False
      scanfbtn = threading.Thread(target=inpf, args = (lambda: plug, ))
      if ~scanfbtn.is_alive():
        scanfbtn.start()
      responder.response("")    
      ybtn.wait_variable(var)
      inp=responder.getres()
      plug = True
      if ochips<=10 and inp=="Y":
        wincounter+=1
        ochips = 500
        if wincounter==3:
          winicp= (Image.open("winner.png"))
          winibg= (Image.open("winnerbg.png"))
          wres = winicp.resize((500,500), Image.ANTIALIAS)
          wresbg = winibg.resize((2000,2005), Image.ANTIALIAS)
          winbgsc=ImageTk.PhotoImage(image= wresbg)
          winscn = ImageTk.PhotoImage(image= wres)
          winl= Label(root, image=winscn)
          winicon= bg.create_window(250,250, window=winl)
          background_label.configure(image=winbgsc)
        roundcount+=1
        print("ROUND COUNT: "+str(roundcount))
        li.clear()
        li1.clear()
        wipedeck()
        wipepool()
        loser = False
        continue
      
      
      elif inp == "Y" and chips>=10:
        roundcount+=1
        print("ROUND COUNT: "+str(roundcount))
        li.clear()
        li1.clear()
        wipedeck()
        wipepool()
        loser = False
        continue
      elif inp=="Y" and chips<10:
        tempmsg("Can't do that if you're broke.",2000)
        updatean("You lose")
        wipedeck()
        wipepool()
        losercp= (Image.open("loser.png"))
        loserbg= (Image.open("loserbg.png"))
        wres = losercp.resize((500,500), Image.ANTIALIAS)
        wresbg = loserbg.resize((2000,2005), Image.ANTIALIAS)
        winbgsc=ImageTk.PhotoImage(image= wresbg)
        winscn = ImageTk.PhotoImage(image= wres)
        winl= Label(root, image=winscn)
        winicon= bg.create_window(250,250, window=winl)
        lscrn = background_label1
        lscrn.configure(image=winbgsc)
        game = False
        tempmsg("", 2000)
        update(500, True)
        update(500, False)
        bg.delete("all")
        titlescreen()      
      elif inp=="N":
        luckywinner = textgetter("insults.csv")
        tempmsg(luckywinner, 2000)
        updatean("")
        wipedeck()
        wipepool()
        game = False
        update(500, True)
        update(500, False)
        bg.delete("all")
        sys.stdout.close()
        root.destroy()
          
  
        root.protocol("WM_DELETE_WINDOW", quitgame())
        try:  
          mainloop()
        except:
          print("")


root.protocol("WM_DELETE_WINDOW", quitprogram)
titlescreen()
print("here is the problem")




mainloop()

sys.stdout.close()