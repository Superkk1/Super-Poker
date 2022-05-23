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


root = Tk()
root.iconphoto(False, PhotoImage(file="titleart.png"))
root.title("Super Poker v1.0 ")
root.geometry("500x500")
root.configure(background="white")
filename1  = PhotoImage(file= "bg.png")
background_label1 = Label(root, image=filename1)
background_label1.place(x=0, y=0, relwidth=1, relheight=1)


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
  
  def update(a, p):
    print("call")
    if p:
      bg.itemconfig(pc, text ="Chips: "+str(a))
    else:
      bg.itemconfig(oc, text="Chips: "+str(a))
    
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
      self.delay=delay
      self.idlechk = False
      try: 
        f.index("s_")==0
        self.idlechk = True

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
      if self.idlechk:
        self.plbl.start_thread()
      else:
        self.plbl.start()
    
    def stop(self):
        self.plbl.stop_thread()
   
    def updatesp(self, file):
      self.spriteico = file
        
      

  imgbg= (Image.open("The Player concept 2.png"))
  res= imgbg.resize((2000,2005), Image.ANTIALIAS)
  fbg = ImageTk.PhotoImage(image= res)
  background_label1.configure(image=fbg)

  playersp = sprite("The Player concept 2.png", 69, 430, 119, 119)
  opponentsp= sprite("The Opponent concept.png", 420, 80, 120,120)

  
  
  
    
  def dupechk(a):
    global dupes
    dupes=[]
    
    val = a

    count = 0
    previous1 =""
    previous2 = ""
    previous3 =""
    previous4=""
    previous5=""
    previous6=""
    previous7=""
    for c in val:
        
      if str(c) == previous1:
        count+=1
        dupes.append(c)
        
      elif str(c) == previous2:
        count+=1
        dupes.append(c)
        
      elif str(c) == previous3:
        count+=1
        dupes.append(c)
        
      elif str(c) == previous4:
        count+=1
        dupes.append(c)
        
      elif str(c) == previous5:
        count+=1
        dupes.append(c)
      elif str(c)== previous6:
        count+=1
      elif str(c)== previous7:
        count+=1
        
    
      if val.index(c)==0:
        previous1=str(c)
      if val.index(c)==1:
        previous2=str(c)
      if val.index(c)==2:
        previous3=str(c)
      if val.index(c)==3:
        previous4=str(c)
      if val.index(c)==4:
        previous5=str(c)
      if val.index(c)==5:
        previous6=str(c)
      if val.index(c)==6:
        previous7=str(c)        
    
    return count


  def createpool():
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

    if comb>=3:
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
    elif comb==2:
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
      if (dupechk(svals)==2):
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
          if dupechk(svals)==2:
            winval=2
            dupechk(als)
            if b:
              pcouple.setcouple(dupes)
            else:
              ocouple.setcouple(dupes)
        elif lnum==svals[2]:
          svals.pop(0)
          svals.append(lnum)
          if dupechk(svals)==2:
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

  residue = []
  suitresidue =[]  
  def gethand():
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

  
  
  wincounter = 0
  game = True
  roundcount = 0
  li=[]
  li1 = []
  plybtn.wait_variable(var)
  plybtn.destroy()
  show(yesbtn)
  show(nobtn)
  global chips
  global ochips
  chips = 500
  ochips= 500
  while game:
    chips-=10
    ochips-=10
    update(chips, True)
    update(ochips, False)
    createpool()
    bg.itemconfig(opponentc1, image=back)
    bg.itemconfig(opponentc2, image=back)

    if wincounter == 1:
     opponentsp.stop()
     opponentsp.updatesprite("Angus.png")
     raiseanim = "Angus_raise.gif"
     badresponse = "Angus_badresponse1.gif"
     goodresponse = "Angus_raise.gif"
     opponentsp.animator("s_Angus_idle.gif", .5)
    elif wincounter == 2:
      opponentsp.stop()
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
    
    st = ""
    while t<5:
      if (t<5 and t>=3) or t==0:
        if t<5:
          betentry.delete(0,END)
          hider(betinp)
          hider(betbtn)
          show(yesbtn)
          show(nobtn)
          msg="Would you like to play your hand?"
          updatean(msg)
          ybtn.wait_variable(var)
          inp =responder.getres()
          if inp=="Y":
            print("")
          elif inp=="N":
            loser= True
            break
        stakes = True
        def breadicide(chips):
          
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
              updatean(msg)
              show(betinp)
              show(betbtn)
              hider(yesbtn)
              hider(nobtn)
              hider(raisebtn)
              bbtn.wait_variable(var)
              inp = betentry.get()
              
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
         
                 hider(betbtn)
                 hider(betinp)
                 tempmsg("All In? Good luck.", 1000)

                 
              key = False
          return bet

        bet=breadicide(chips)
        
        obet = 0
        if bet-chips==0 or bet-ochips<=0:
          stakes=False

          obet = bet
          if obet>ochips:
            obet=ochips
      
        stakesturn = True
        if ochips<=0 or obet-ochips<=0:
          stakes=False

        while stakes:
          impulse = random.randint(0,10)
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
            print("made it through 783")
          obet = bet
          #tempmsg("Impulse is "+str(impulse), 1000)
          print("786")
          if impulse <=5:
            stupidity = random.randint(1,9)
            if stakeslist[len(stakeslist)-1]>0 and stupidity != 5 and stakesturn:
              stupidity=+stakeslist[len(stakeslist)-1]

            while True:
              stupidity1 =stupidity*pow(10, len(str(bet))-1)
              if (ochips-stupidity1>0 or ochips==0):
                break


            msg ="Your opponent raised the\n stakes by "+str(int(stupidity1))+"!\n"  #also culprit?                   |
            stakesturn = False
            opponentsp.animator(raiseanim, .05) 
            hider(betbtn)
            hider(betinp)
            tempmsg(msg, 2000)
            
            msg="What will you do?"
           
            updatean(msg)
            show(yesbtn)
            show(nobtn)
            show(raisebtn)
            ybtn['text']= "Call"
            nbtn['text']= "Fold"
            
            ybtn.wait_variable(var)
            inp =responder.getres()
   
            if inp == "Y":
              stakes=False
              bet += int(stupidity1)  #culprit?
              if bet>chips:
                bet=chips
              obet+=int(stupidity1)
            elif inp == "R":
              
              breadicide()
            elif inp == "N":
              loser = True
              break
            hider(yesbtn)
            hider(nobtn)
          else:         
            stakes = False
            
        if reasonablebet:

          pot += int(bet)+obet
          upot(pot)
          chips-=int(bet)
          ochips-=obet
          if loser == True:
            break
          update(ochips, False)
          update(chips, True)
      ybtn['text']= "Yes"
      nbtn['text']= "Fold"
      hider(raisebtn)
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
    
    while t<5:
      updatepool(l,t)
      t+=1
    def prechk(c, a, b):
  
      f1 =0
      while f1<len(vals):
        pvals=vals.copy()
        convert(pvals)

        pvals.pop(f1)
        pvals.insert(f1,c)
        if b:
          li.append(hndchk(pvals, True))
        else:
          li1.append(hndchk(pvals, False))
        f1+=1
      if a:
        if b:
          prechk(chand[1], False, True)
        else:
          prechk(cohand[1],False, False)
    
    prechk(chand[0], True, True)
    print("Player hand checker:")
    while f<len(vals):
      j=0
      while j<len(vals):        
        vals1=vals.copy()        
        convert(vals1)  
        vals1.pop(f)
        vals1.insert(f,chand[0])
        if j!=f: 
          vals1.pop(j)          
          vals1.insert(j,chand[1])         
          li.append(hndchk(vals1, True))
        j+=1     
      f+=1

    print("Opponent hand checker")
    prechk(cohand[0], True, False)
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
          li1.append(hndchk(vals2,False))  
        j+=1
      f+=1

    straightflsh = False
    vals2=s.copy()
    for n in csuits:
      vals2.append(n)
    vals2.sort()
    print(vals2)
    print(dupechk(vals2))
    elim1 = vals2.copy()
    elim2 = vals2.copy()
    elim3 = vals2.copy()
    elim1.pop(0)
    elim1.pop(0)
    elim2.pop(0)
    elim2.pop(5)
    elim3.pop(5)
    elim3.pop(5)

    flsh = False
    if dupechk(elim1)==4:
      flsh=True
      welim = elim1
    elif dupechk(elim2)==4:
      flsh=True
      welim = elim2
    elif dupechk(elim3)==4:
      flsh=True
      welim = elim3

    if flsh:
          print("flush is calling")
          samesuits = []
          for c in l:
            if c.find(welim[0])>-1:
              cspl=c.split()
              convert(cspl)
              samesuits.append(int(cspl[0]))
          for c in phand:
            if c.find(welim[0])>-1:
              cspl =c.split()
              print(cspl[0])
              convert(cspl)          
              samesuits.append(int(cspl[0]))
          print(samesuits)
          if hndchk(samesuits, True)==3:
            straightflsh=True

          if straightflsh:
            if samesuits.count(14)>0 and samesuits.count(13)>0:
              li.append(8)
            li.append(7)
          else:
            li.append(4)

    ostraightflsh = False
    vals2=s.copy()
    for n in cosuits:
      vals2.append(n)
    vals2.sort()
    print(vals2)
    print(dupechk(vals2))
    elim1 = vals2.copy()
    elim2 = vals2.copy()
    elim3 = vals2.copy()
    elim1.pop(0)
    elim1.pop(0)
    elim2.pop(0)
    elim2.pop(5)
    elim3.pop(5)
    elim3.pop(5)

    flsh = False
    if dupechk(elim1)==4:
      flsh=True
      welim = elim1
    elif dupechk(elim2)==4:
      flsh=True
      welim = elim2
    elif dupechk(elim3)==4:
      flsh=True
      welim = elim3

    if flsh:
          print("welim is "+str(welim))
          print("flush is calling")
          osamesuits = []
          for c in l:
            if c.find(welim[0])>-1:
              cspl =c.split()
              print(cspl[0])
              convert(cspl)          
              osamesuits.append(int(cspl[0]))
          for c in ohand:
            if c.find(welim[0])>-1:
              cspl = c.split()
              convert(cspl)
              osamesuits.append(int(cspl[0]))
          print(osamesuits)
          if hndchk(osamesuits, False)==3:
            ostraightflsh=True

          if ostraightflsh:
            if osamesuits.count(14)>0 and osamesuits.count(13)>0:
              li1.append(8)
            li1.append(7)
          else:
            li1.append(4)


    
    
    hider(betbtn)
    hider(betinp)
    print(pcouple.getcouple())
    print(ocouple.getcouple())
    print(li)
    print(li1)
    print("Your opponent's hand: ")
    print(ohand) 
    
    li.sort()
    if loser==False:
      pw ="For you"
      if li[len(li)-1] <=-1:
        pw2="It's a High Card"
      if li[len(li)-1]==0:
        pw2="It's a pair"
      if li[len(li)-1]==1:
        pw2="It's a two pair"
      if li[len(li)-1]==2:
        pw2="It's a three of a kind"
        print(li)
      if li[len(li)-1]==3:
        pw2="It's a straight"
      if li[len(li)-1]==4:
        pw2="It's a flush"
      if li[len(li)-1]==5:
        pw2="It's a full house"
      if li[len(li)-1]==6:
        pw2="It's a four of a kind"
      if li[len(li)-1]==7:
        pw2="It's a striaght flush"
      if li[len(li)-1]==8:
        pw2="Holy Smokes!\nYou got a royal flush!"
    else:
      pw2=""
      pw="You folded"
    po = pw+" "+pw2
    print(po)
    print(len(li)-1)
    tempmsg(po, 2000)

    
    tempmsg("For your opponent...", 2000)
    if badresponse != "Sr_poker_badresponse.png":
     opponentsp.stop()
    playersp.stop()
    
    li1.sort()
    if li1[len(li1)-1] ==-1:
      ow2="It's a High Card"
    if li1[len(li1)-1]==0:
      ow2="It's a pair"
    if li1[len(li1)-1]==1:
      ow2="It's a two pair"
    if li1[len(li1)-1]==2:
      ow2="It's a three of a kind"
    if li1[len(li1)-1]==3:
      ow2="It's a straight"
    if li1[len(li1)-1]==4:
      ow2="It's a flush"
    if li1[len(li1)-1]==5:
      ow2="It's a full house"
    if li1[len(li1)-1]==6:
      ow2="It's a four of a kind"
    if li1[len(li1)-1]==7:
      ow2="It's a striaght flush"
    if li1[len(li1)-1]==8:
      ow2="Holy Smokes!\nThey got a royal flush!"
   

    oo = ow2
    print(oo)
    print(len(li1)-1)
    showdeck(ohand)
    tempmsg(oo, 2000)
    chand.sort()
    cohand.sort()
    champ= -1
    if loser==False:
      while True:
        if (li[len(li)-1]==li1[len(li1)-1]) and li[len(li)-1]>-1 and li1[len(li1)-1]>-1:
          if (li[len(li)-1]==4 and li1[len(li1)-1]==4):
            samesuits.sort()
            osamesuits.sort()
            if samesuits[4]>osamesuits[4]:
              champ = 0
              break
            elif samesuits[4]<osamesuits[4]:
              champ=1
              break
          elif chand[1]>cohand[1]:
            champ=0                                                      #Watch this 
            break
          elif chand[1]<cohand[1]:
            champ=1
            break

            print(" its calling"+ str(pcouple.getcouple()))
            print(" its calling"+ str(ocouple.getcouple()))
            pcouple1 = pcouple.getcouple()
            ocouple1= ocouple.getcouple()
            pcouple1.sort()
            ocouple1.sort()
            if pcouple1[len(pcouple1)-1]>ocouple1[len(ocouple1)-1]:
                #do something about pcouple-2
                champ=0
                break
            elif pcouple1[len(pcouple1)-1]<ocouple1[len(ocouple1)-1]:
                champ=1
                
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
      chips+=pot
    elif champ==1:
      playersp.animator("player_badresponse.gif", .05)
      opponentsp.animator(goodresponse, .05)
      tempmsg("You lose.", 2000)
      ochips+=pot
    elif champ==2:
      playersp.animator("player_goodresponse.gif", .05)
      opponentsp.animator(badresponse, .05)
      tempmsg("You win by high card!", 2000)
      chips+=pot
    elif champ==3:
      playersp.animator("player_badresponse.gif", .05)
      opponentsp.animator(goodresponse, .05)
      tempmsg("You lose, your opponent\n wins by high card.",2000)
      ochips+=pot


      
    print("You now have "+str(chips)+" chips.\n")
    update(ochips, False)
    update(chips, True)
    upot(0)

    if ochips<=0:
      msg="Ready for your next opponent?"
    else:
      msg ="Another round?"
    nbtn.configure(text="no")
    updatean(msg)
    ybtn.wait_variable(var)
    inp=responder.getres()

    if ochips<=0 and inp=="Y":
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
    
    

    elif inp == "Y" and chips>0:
      roundcount+=1
      print("ROUND COUNT: "+str(roundcount))
      li.clear()
      li1.clear()
      wipedeck()
      wipepool()
      loser = False
      continue
    elif inp=="Y" and chips<=0:
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
      insults = open("insults.csv")
      for line in insults:
        split=line.split(",")
      luckywinner = split[random.randint(0,len(split)-1)]
      split1 = luckywinner.split("*")
      print(split1)
      print(len(split1))
      if len(split1)>1:
        luckywinner = split1[0]+"\n"+split1[1]
      print(luckywinner)
      tempmsg(luckywinner, 3000)
      updatean("")
      wipedeck()
      wipepool()
      game = False
      update(500, True)
      update(500, False)
      bg.delete("all")
      titlescreen()

      
    mainloop()
    
titlescreen()
mainloop()
