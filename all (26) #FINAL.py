#Hetalia themed paint program
#Lynn (Liying) Liu

#imports stuff from pygame/random/math/glob
from pygame import *
from random import *
from math import *
from glob import *

print("Welcome to Lynn's Hetalia Paint Game!")    
screen = display.set_mode((1200,900))
init() #initializes music player
background=image.load("hetalia background with purple7.png") #loads and blits backgroud
screen.blit(background,(0,0)) 
colourbox=image.load("color grid.png") #loads and blits colour palette
screen.blit(colourbox,(20,570))
colourRect = Rect(20,570,274,326) #assigns area for palette
canvasRect = Rect(447,120,730,500) #assigns area for canvas
draw.rect(screen,(255,255,255),canvasRect) #creates a blank canvas
drawColour=(0,0,0) #current colour (default-black)
infobarColour=screen.get_at((147,850)) #purple colour used for info display boxes

display.set_caption("Paint!Hetalia")
font.init() #initializes fonts
comicFontlarge = font.SysFont("Comic Sans MS", 18) #large Comic Sans font
comicFontsmall = font.SysFont("Comic Sans MS", 13) #small Comic Sans font

#MUSIC LOAD----------------------------------------------------------------
#loads and plays music infinitely
mixer.music.load("Playlist.mp3") 
mixer.music.play(-1)

#BAR ICONS------------------------------------------------------------
#area assigned for icons at the top right of screen 
hoverload = Rect(1100,30,48,48)
hoversave = Rect(1030,30,48,48)
hoverredo = Rect(960,30,48,48)
hoverundo = Rect(890,30,48,48)
hovernew = Rect(820,30,48,48)
hoverpause = Rect(750,30,48,48)
hoverplay = Rect(680,30,48,48)
#loads icons
hoverLoad = image.load("bar icon-Load lilac.png")
nohoverLoad = image.load("bar icon-Load black.png")
hoverSave = image.load("bar icon-Save lilac.png")
nohoverSave = image.load("bar icon-Save black.png")
hoverUndo = image.load("bar icon-Left lilac.png")
nohoverUndo = image.load("bar icon-Left black.png")
hoverRedo = image.load("bar icon-Right lilac.png")
nohoverRedo = image.load("bar icon-Right black.png")
hoverNew = image.load("bar icon-New lilac.png")
nohoverNew = image.load("bar icon-New black.png")
nohoverMusicplay = image.load("bar icon-Play black.png")
hoverMusicplay = image.load("bar icon-Play lilac.png")
nohoverMusicpause = image.load("bar icon-Pause black.png")
hoverMusicpause = image.load("bar icon-Pause lilac.png")

#ART ICONS--------------------------------------------------------------------
#area assigned for art tool icons at the left of the screen
pencilRect = Rect(20,300,60,60)
paintRect = Rect(100,300,60,60)
eraserRect = Rect(180,300,60,60)
penRect = Rect(260,300,60,60)
lineRect = Rect(20,380,60,60)
elipseRect = Rect(100,380,60,60)
rectRect = Rect(180,380,60,60)
eyedropperRect = Rect(260,380,60,60)
sprayRect = Rect(20,460,60,60)
fillRect = Rect(100,460,60,60)
magic1Rect = Rect(180,460,60,60)
magic2Rect = Rect(260,460,60,60)
#loads icons
artPaint = image.load("art icon-Brush.png")
artPencil = image.load("art icon-Pencil.png")
artEraser = image.load("art icon-Eraser.png")
artPen = image.load("art icon-Pen.png")
artLine = image.load("art icon-Ruler.png")
artElipse = image.load("art icon-Compass.png")
artRect = image.load("art icon-Rect.png")                                         
artSpray = image.load("art icon-Spray.png") 
artEyedropper = image.load("art icon-Eyedropper.png")
artFill = image.load("art icon-Fill.png")
artMagic1 = image.load("art icon-Magic1.png")
artMagic2 = image.load("art icon-Magic2.png")

#ICON SELECT BORDER IMAGE LOAD------------------------------------------------------
artselect = image.load("art icon-select border.png") #black border displayed around an art tool icon if it is selected
arthover = image.load("art icon-hover border.png") #green border displayed around an art tool icon if mouse hovers over it
stampselect = image.load("chibi icon select box.png") #black border displayed around a stamp tool icon if it is selected
stamphover = image.load("chibi icon hover box.png") #green border displayed around a stamp tool icon if mouse hovers over it
wallpaperselect = image.load("blit icon-select border.png") #black border displayed around flag when wallpaper tool is selected
wallpaper1hover = image.load("blit icon-UN 48.png") #3D-like UN flag icon displayed when mouse overs over UN flag
wallpaper2hover = image.load("blit icon-Olympics 48.png") #3D-like Olympics flag icon displayed when mouse overs over Olympics flag

#RADIUS SELECTOR------------------------------------------------------
#preset radius changer
#assigns area of/draws a small, medium, and large squares
largeRect=Rect(320,720,10,10)
draw.rect(screen,(0,0,0),largeRect)
largerRect=Rect(340,710,20,20)
draw.rect(screen,(0,0,0),largerRect)
largestRect=Rect(370,700,30,30)
draw.rect(screen,(0,0,0),largestRect)

#DEFS OF TOOLS--------------------------------------------------------------

def getName():
    ans = ""                    # final answer will be built one letter at a time.
    arialFont = font.SysFont("Times New Roman", 16)
    back = screen.copy()        # copy screen so we can replace it when done
    textArea = Rect(5,5,430,25) # 
    
    pics = glob("*.bmp")+glob("*.jpg")+glob("*.png")
    n = len(pics)
    choiceArea = Rect(textArea.x,textArea.y+textArea.height,textArea.width,n*textArea.height)
    draw.rect(screen,(220,220,220),choiceArea)        # draw the text window and the text.
    draw.rect(screen,(0,0,0),choiceArea,1)        # draw the text window and the text.
    for i in range(n):
        txtPic = arialFont.render(pics[i], True, (0,111,0))   
        screen.blit(txtPic,(textArea.x+3,textArea.height*i+choiceArea.y))
        
    typing = True
    while typing:
        for e in event.get():
            if e.type == QUIT:
                event.post(e)   # puts QUIT back in event list so main quits
                return ""
            if e.type == KEYDOWN:
                if e.key == K_BACKSPACE:    # remove last letter
                    if len(ans)>0:
                        ans = ans[:-1]
                elif e.key == K_KP_ENTER or e.key == K_RETURN : 
                    typing = False
                elif e.key < 256:
                    ans += e.unicode       # add character to ans
                    
        txtPic = arialFont.render(ans, True, (0,0,0))   #
        draw.rect(screen,(220,255,220),textArea)        # draw the text window and the text.
        draw.rect(screen,(0,0,0),textArea,2)            #
        screen.blit(txtPic,(textArea.x+3,textArea.y+2))
        
        display.flip()
        
    screen.blit(back,(0,0))
    return ans
def penciltool():
    #draws a thin line from old mouse position to current mouse position
    screen.set_clip(canvasRect)
    draw.aaline(screen,drawColour,(oldpos),(mpos),80)
    screen.set_clip(None)
def brushtool():
    #draws circles from old mouse position to current mouse position
    screen.set_clip(canvasRect)
    global sx, sy
    distance=(((mx-omx)**2)+((my-omy)**2))/2 #gets the distances of where the mouse first clicks down to the new mouse position
    if distance==0: #If mouse is not dragged a circle is drawn
        draw.circle(screen,drawColour,(mx,my),radius)
    if distance!=0:
        sx=(mx-omx)/distance #length of the smaller similar triangle
        sy=(my-omy)/distance #height of the smaller similar triangle
        for i in range(int(distance)):
            draw.circle(screen,drawColour,(int(sx*i+omx),int(sy*i+omy)),radius)
    screen.set_clip(None)
def erasertool():
    #draws white circles from old mouse position to current mouse position
    screen.set_clip(canvasRect)
    global sx, sy
    distance=(((mx-omx)**2)+((my-omy)**2))/2 #gets the distances of where the mouse first clicks down to the new mouse position
    if distance==0: #If mouse is not dragged a circle is drawn
        draw.circle(screen,(255,255,255),(mx,my),radius)
    if distance!=0:
        sx=(mx-omx)/distance #length of the smaller similar triangle
        sy=(my-omy)/distance #height of the smaller similar triangle
        for i in range(int(distance)):
            draw.circle(screen,(255,255,255),(int(sx*i+omx),int(sy*i+omy)),radius)
    screen.set_clip(None)
def pentool():
    #a calligraphy pen tool which draws a horizontal line where you click
    screen.set_clip(canvasRect)
    for i in range (-1*radius,radius): 
        draw.line(screen,drawColour,(mx+i,my),(omx+i,omy),1) #draws multiple lines side by side from old my to new my
    screen.set_clip(None)
def linetool():
    #draws one line from where mouse is first clicked to current mouse position
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0))  #only one line drawn
    draw.line(screen,drawColour,(startx,starty),mpos,radius)
    screen.set_clip(None)
def drawpoly():
    #draws a polygon
    if canvasRect.collidepoint(mx,my):
        screen.set_clip(canvasRect)
        global polyList
        startpoly=mx,my #where mouse first clicks
        polyList.append(startpoly) 
        if mb[0]==1:
            polyList.append((mx,my)) #adds mx,my to the list 
        if len(polyList)>=2:
            draw.line(screen,(drawColour),(polyList[-2]),polyList[-1],2) #draws a line from the second last coordinate in polyList to the last coordinate
        screen.set_clip(None)
def filledelipsedrawertool():
    #draws a filled ellipse
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0))  #only one ellipse drawn
    elli=Rect(startx,starty,mx-startx,my-starty) #area where the ellipse will be drawn in
    elli.normalize() #ensures that lengths are all positive integers
    draw.ellipse(screen,(drawColour),elli)
    screen.set_clip(None)
def emptyelipsedrawertool():
    #draws an empty ellipse
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0))  #only ellipse line drawn
    elli=Rect(startx,starty,mx-startx,my-starty) #area where the ellipse will be drawn in
    elli.normalize() #ensures that lengths are all positive integers
    if radius<(mx-startx) and radius<(my-starty): #if mouse drags towards lower right    
        draw.ellipse(screen,(drawColour),elli,int(radius/2))
    elif radius<(mx-startx)*-1 and radius<(my-starty): #if mouse drags towards lower left 
        draw.ellipse(screen,(drawColour),elli,int(radius/2))
    elif radius<(mx-startx) and radius<(my-starty)*-1: #if mouse drags towards upper right
        draw.ellipse(screen,(drawColour),elli,int(radius/2))
    elif radius<(mx-startx)*-1 and radius<(my-starty)*-1: #if mouse drags towards upper left
        draw.ellipse(screen,(drawColour),elli,int(radius/2))
    else: #if width and height of elli is smaller than the radius
        draw.ellipse(screen,(drawColour),elli,0)
    screen.set_clip(None)
def filledrectdrawertool():
    #draws a filled rectange
    screen.blit(screencopy,(0,0))  #only one rectangle drawn
    elli=Rect(startx,starty,mx-startx,my-starty)
    elli.normalize()
    draw.rect(screen,(drawColour),elli)
def emptyrectdrawertool():
    #draws an empty rectangle
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0))  #only one line drawn        
    elli=Rect(startx,starty,mx-startx,my-starty) #border
    elli.normalize() #ensures that lengths are all positive integers
    elli2=Rect(startx+radius/2,starty+radius/2,mx-startx-radius,my-starty-radius) #inner rect
    elli2.normalize() #ensures that lengths are all positive integers
    square1=Rect(startx,starty,radius/2,radius/2) #upper left square (squares fill in awkward empty space between lines)
    square1.normalize()
    square2=Rect(mx-radius/2,my-radius/2,radius/2,radius/2) #bottom right square
    square2.normalize()
    square3=Rect(mx-radius/2,starty,radius/2,radius/2) #upper right square
    square3.normalize()
    square4=Rect(startx,my-radius/2,radius/2,radius/2) #lower left square
    square4.normalize()
    draw.rect(screen,(drawColour),elli,1)
    draw.rect(screen,(drawColour),elli2,radius)
    draw.rect(screen,(drawColour),square1)
    draw.rect(screen,(drawColour),square2)
    draw.rect(screen,(drawColour),square3)
    draw.rect(screen,(drawColour),square4)
    screen.set_clip(None)
def eyedroppertool():
    #gets the colour from point where the mouse clicks within the program and sets that colour to use as current colour
    global drawColour
    drawColour=screen.get_at((mpos))
def spraytool():
    #colours in random pixels within radius of mouse position
    screen.set_clip(canvasRect)
    for i in range(radius):
        dx=randint(mx-radius,mx+radius) #random integer within the current radius from the mouse
        dy=randint(my-radius,my+radius) #random integer within the current radius from the mouse
        d=((dx-mx)**2+(dy-my)**2)**0.5 #the distance from dx to dy 
        if d<=radius: #changes the colour at dx,dy if d<=the radius (this is so that the spraypaint works in a circle shape)
            screen.set_at((dx,dy),(drawColour))
    screen.set_clip(None)
def filltool():
    #fills an area of the same colour with current colour
    bucketlist=[]
    bucketpoint=mx,my #where mouse clicks
    oldColour=screen.get_at((mx,my)) #old colour from where mouse clicks
    bucketlist.append(bucketpoint) 
    if oldColour!=drawColour:
        while len(bucketlist)>0:
            spot=bucketlist.pop() #spot=position of last one in list #removes spot from list
            if screen.get_at(spot) ==oldColour: #checks to see if spot has the same colour as oldColour
                screen.set_at(spot,drawColour) #colours spot with current colour
                #adds the points up, down, right, and left of spot to the bucketlist
                bucketlist.append((spot[0]+1,spot[1])) 
                bucketlist.append((spot[0],spot[1]+1))
                bucketlist.append((spot[0],spot[1]-1))
                bucketlist.append((spot[0]-1,spot[1]))
def magic1tool():
    #draws lines from current mouse position to a random point within radius of mouse position
    screen.set_clip(canvasRect)
    for i in range(radius):
        dx=randint(mx-radius,mx+radius) #random integer within the current radius from the mouse
        dy=randint(my-radius,my+radius) #random integer within the current radius from the mouse
        d=((dx-mx)**2+(dy-my)**2)**0.5 #the distance from dx to dy 
        if d<=radius: #draws a line from dx to dy if d<=the radius (this is so that the tool works in a circle shape)
            draw.line(screen,drawColour,(mx,my),(dx,dy),2)
    screen.set_clip(None)
def magic2tool():
    #confetti tool!
    #similar to spraytool, but instead draws randomly coloured circles within radius of mouse position
    #radius of these circles are 15% of current radius which means that they change size as the radius increases/decreases
    screen.set_clip(canvasRect)
    for i in range(radius):
        dx=randint(mx-radius,mx+radius) #random integer within the current radius from the mouse
        dy=randint(my-radius,my+radius) #random integer within the current radius from the mouse
        d=((dx-mx)**2+(dy-my)**2)**0.5 #the distance from dx to dy 
        if d<=radius: #draws a line from dx to dy if d<=the radius (this is so that the tool works in a circle shape)    
            draw.circle(screen,(randint(1,255),randint(1,255),randint(1,255)),(dx,dy),int(radius/15))
    screen.set_clip(None)
    
#CHIBI STAMP ICONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#area assigned for stamp selection icons/wallpaper tool icons
usRect=Rect(450,700,90,90)
ukRect=Rect(550,700,90,90)
franceRect=Rect(650,700,90,90)
russiaRect=Rect(750,700,90,90)
chinaRect=Rect(850,700,90,90)
germanyRect=Rect(450,800,90,90)
italyRect=Rect(550,800,90,90)
japanRect=Rect(650,800,90,90)
canadaRect=Rect(950,700,90,90)
bg1Rect=Rect(750,800,90,90)
bg2Rect=Rect(850,800,90,90)
#loads stamp/wallpaper tool icons
us=image.load("US icon small.png")
uk=image.load("UK icon small.png")
france=image.load("France icon small.png")
russia=image.load("Russia icon small.png")
china=image.load("China icon small.png")
germany=image.load("Germany icon small.png")
italy=image.load("Italy icon small.png")
japan=image.load("Japan icon small.png")
canada=image.load("Canada icon small.png")
bg1icon=image.load("blit icon-UN flat 48.png")
bg2icon=image.load("blit icon-Olympics flat 48.png")
#load actual character stamps
US=image.load("chibi!America.png")
UK=image.load("chibi!England2.png")
France=image.load("chibi!France.png")
Russia=image.load("chibi!Russia.png")
China=image.load("chibi!China.png")
Germany=image.load("chibi!Germany.png")
Italy=image.load("chibi!Italy2.png")
Japan=image.load("chibi!Japan.png")
Canada=image.load("chibi!Canada.png")
#loads wallpapers used in wallpaper tool
Blit1=image.load("bg blit-Hetalia_Gakuen.png")
Blit2=image.load("bg blit-soccer.png")

#DEFS OF STAMP TOOLS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#blits stamp icons of Hetalia characters
def USstamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=US.get_size() #width and height of stamp
    usstamp=transform.scale(US,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=usstamp.get_size() #width and height of resized stamp
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position 
    screen.blit(usstamp,(centerpt))
    screen.set_clip(None)
def UKstamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=UK.get_size()   
    ukstamp=transform.scale(UK,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=ukstamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position 
    screen.blit(ukstamp,(centerpt))
    screen.set_clip(None)
def Francestamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=France.get_size()
    francestamp=transform.scale(France,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=francestamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(francestamp,(centerpt))
    screen.set_clip(None)
def Russiastamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=Russia.get_size()
    russiastamp=transform.scale(Russia,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=russiastamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(russiastamp,(centerpt))
    screen.set_clip(None)
def Chinastamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=China.get_size() 
    chinastamp=transform.scale(China,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=chinastamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(chinastamp,(centerpt))
    screen.set_clip(None)
def Germanystamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=Germany.get_size()  
    germanystamp=transform.scale(Germany,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=germanystamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(germanystamp,(centerpt))
    screen.set_clip(None)
def Italystamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=Italy.get_size() 
    italystamp=transform.scale(Italy,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=italystamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(italystamp,(centerpt))
    screen.set_clip(None)
def Japanstamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=Japan.get_size()
    japanstamp=transform.scale(Japan,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=japanstamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(japanstamp,(centerpt))
    screen.set_clip(None)
def Canadastamp():
    screen.set_clip(canvasRect)
    screen.blit(screencopy,(0,0)) #only blits one stamp per click
    w,h=Canada.get_size()
    canadastamp=transform.scale(Canada,(int(w*resize),int(h*resize))) #resizes stamp if scroll up/down
    w2,h2=canadastamp.get_size()
    centerpt=(mx-int(w2/2),my-int(h2/2)) #centers the stamp around the current mouse position
    screen.blit(canadastamp,(centerpt))
    screen.set_clip(None)
def wallpaper1():
    screen.set_clip(canvasRect)
    screen.blit(Blit1,(447,120)) #blits wallpaper to fill the canvas
    screen.set_clip(None)
def wallpaper2():
    screen.set_clip(canvasRect)
    screen.blit(Blit2,(447,120)) #blits wallpaper to fill the canvas
    screen.set_clip(None)
    
#DEFAULT THINGS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
undolist=[screen.subsurface(canvasRect).copy()] #undo list
screencopy=screen.copy() #takes a copy of the screen
curTool="penciltool" #default tool
##mx=0
##my=0
radius=10 #size of art tools
resize=1 #size of stamps
iconselectcoordinates=(20,300) #icon select coordinates is the point where icon select borders will be blitted at
redolist=[] #redo list
polyList=[] #list of points of the vertices of the polygon in the poly tool
redopolyList=[] #a redo list for the poly tool
txtdrawColour = comicFontlarge.render("Colour:", True, (0,0,0)) #message indicating current colour
screen.blit(txtdrawColour,(307,815))

#running loop! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
running =True
while running:
                                     
    mpos=mx,my=mouse.get_pos() #current mouse position
    mb=mouse.get_pressed() #mouse clicks  
    clickUp = False
    clickDown = False
    for evnt in event.get():
        if evnt.type==MOUSEBUTTONUP:
            clickUp = True
            #adds a copy of the canvas to the undolist each time the mouse button comes up on the canvas
            if canvasRect.collidepoint(mpos):
                if mb[0]==1: #only takes a screenshot of the canvas and adds it to the undolist if you left click on the canvas
                    undolist+=[screen.subsurface(canvasRect).copy()]
                    redolist=[] #empties redolist
        if evnt.type==MOUSEBUTTONDOWN:
            clickDown = True
            if evnt.button == 1: #only undos/redos if left button is clicking
                startx,starty=mouse.get_pos()   #gets position of where mouse first clicks down
                screencopy=screen.copy()        #takes copy of screen
                
                if hoverundo.collidepoint(mpos) and len(undolist)>1:
                    screen.blit(undolist[len(undolist)-2],canvasRect) #blits the second-last thing in undolist onto the canvas
                    redolist.append(undolist.pop()) #removes the last thing in undolist and adds it to redolist
                    if len(polyList)>0: #doesn't remove from polyList if there isn't anything in it
                        redopolyList.append(polyList.pop())

                if hoverredo.collidepoint(mpos) and len(redolist)>=1:                   
                    screen.blit(redolist[len(redolist)-1],canvasRect) #blits the last thing in redolist onto the canvas
                    undolist.append(redolist[len(redolist)-1]) #adds the last thing from redolist back to the undolist
                    redolist.remove(redolist[len(redolist)-1]) #removes the last thing from redolist
                    if len(redopolyList)>0: #doesn't remove from redopolyList if there isn't anything in it
                        polyList.append(redopolyList.pop())
                    
            if evnt.button == 4: #increases radius and stamp size if mouse scrolls up
                   radius += 1 
                   if resize<1.2:
                       resize +=0.05
            if evnt.button == 5: #decreases radius and stamp size if mouse scrolls down
                if radius>2:
                   radius -= 1
                if resize>0.3:
                   resize -=0.05

        if evnt.type==QUIT:
            running=False           
    #blits bar/art tool/stamp/wallpaper tool icons
    screen.blit(nohoverLoad,(1100,30))
    screen.blit(nohoverSave,(1030,30))
    screen.blit(nohoverRedo,(960,30))
    screen.blit(nohoverUndo,(890,30))
    screen.blit(nohoverNew,(820,30))
    screen.blit(nohoverMusicpause,(750,30))
    screen.blit(nohoverMusicplay,(680,30))
    screen.blit(artPencil,(20,300))
    screen.blit(artPaint,(100,300))
    screen.blit(artEraser,(180,300))
    screen.blit(artPen,(260,300))
    screen.blit(artLine,(20,380))
    screen.blit(artElipse,(100,380))
    screen.blit(artRect,(180,380))
    screen.blit(artEyedropper,(260,380))
    screen.blit(artSpray,(20,460))
    screen.blit(artFill,(100,460))
    screen.blit(artMagic1,(180,460))
    screen.blit(artMagic2,(260,460))
    screen.blit(us,(450,700))
    screen.blit(uk,(550,700))
    screen.blit(france,(650,700))
    screen.blit(russia,(750,700))
    screen.blit(china,(850,700))
    screen.blit(germany,(450,800))
    screen.blit(italy,(550,800))    
    screen.blit(japan,(650,800))
    screen.blit(canada,(950,700))
    screen.blit(bg1icon,(750,800))
    screen.blit(bg2icon,(850,800))

#BAR TOOLS (PLAY/PAUSE/NEW/UNDO/REDO/SAVE/OPEN)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if hoverload.collidepoint(mx,my):
        screen.blit(hoverLoad,(1100,30)) #blits lilac load icon if mouse hovers over it
        if mb[0]==1:
            txtPic = comicFontsmall.render("Load a jpg, png, or bmp image. Make sure you type in the file extension too. Press enter to quit", True, (0,0,0))
            draw.rect(screen,(infobarColour),(447,625,730,27)) 
            screen.blit(txtPic,(447,625))
            txt = getName()                     #call getName function#main loop will stop looping until user hits enter
            if txt[-4:]==".jpg" or txt[-4:]==".png" or txt[-4:]==".bmp": #doesn't open anything if no extension is typed or if extension is typed incorrectly
                toget=image.load(txt) #loads the picture
                if toget.get_height()>500:
                    loadwidth=toget.get_width()
                    loadheight=toget.get_height()
                    toget=transform.scale(toget,((int(loadwidth*500/loadheight)),500)) #makes image width proportional to new height
                if toget.get_width()>730:
                    loadwidth=toget.get_width()
                    loadheight=toget.get_height()
                    toget=transform.scale(toget,(730,(int(loadheight*730/loadwidth))))#makes image height proportional to new width
                if toget.get_width()>730 and toget.get_height()>500:
                    toget=transform.scale(toget,(730,500))
                draw.rect(screen,(255,255,255),canvasRect) #clears old work
                screen.set_clip(canvasRect)
                screen.blit(toget,(447,120))
                screen.set_clip(None)
                undolist+=[screen.subsurface(canvasRect).copy()] #adds screenshot of canvas to undoList
                redolist=[] #empties redolist
    if hoversave.collidepoint(mx,my):
        screen.blit(hoverSave,(1030,30)) #blits lilac save icon if mouse hovers over it
        if mb[0]==1:
            txtPic = comicFontsmall.render("Save as a jpg, png, bmp or gif image. Not ready to save yet? Just press enter to quit", True, (0,0,0))
            draw.rect(screen,(infobarColour),(447,625,730,27)) 
            screen.blit(txtPic,(447,625))
            txt = getName()              
            if txt!="": #doesn't save file if nothing is typed before hitting enter
                if txt[-4:]==".jpg" or txt[-4:]==".png" or txt[-4:]==".bmp" or txt[-4:]==".gif":
                    image.save(screen.subsurface(canvasRect),txt)
                else:
                    txt+=".png" #if no file extension is specified default saves as a png file
                    image.save(screen.subsurface(canvasRect),txt)
    if hoverredo.collidepoint(mx,my):
        screen.blit(hoverRedo,(960,30)) #blits lilac redo icon if mouse hovers over it
    if hoverundo.collidepoint(mx,my): 
        screen.blit(hoverUndo,(890,30)) #blits lilac undo icon if mouse hovers over it
    if hovernew.collidepoint(mx,my): 
        screen.blit(hoverNew,(820,30)) #blits lilac new canvas icon if mouse hovers over it     
        if mb[0]==1:
            draw.rect(screen,(255,255,255),canvasRect) #fills canvas with white
            undolist=[screen.subsurface(canvasRect).copy()] #undolist is emptied expect for blank canvas
            redolist=[] #empties redolist/polyList/redopolyList
            polyList=[]
            redopolyList=[]
    if hoverpause.collidepoint(mpos):
        screen.blit(hoverMusicpause,(750,30)) #blits lilac pause canvas icon if mouse hovers over it 
        if mb[0]==1:
            mixer.music.pause() #pauses music
    if hoverplay.collidepoint(mpos):
        screen.blit(hoverMusicplay,(680,30)) #blits lilac play icon if mouse hovers over it 
        if mb[0]==1:
            mixer.music.unpause() #unpauses music

#color selection/radius--------------------------------------------------------------------    
    if mb[0]==1 and colourRect.collidepoint(mx,my):
        drawColour=screen.get_at((mx,my)) #gets current colour from colour palette
    if mb[0]==1 and largeRect.collidepoint(mx,my):
        radius=10 #changes radius to 10 if mouse clicks on small preset radius selector box    
    if mb[0]==1 and largerRect.collidepoint(mx,my):
        radius=30 #changes radius to 30 if mouse clicks on medium preset radius selector box          
    if mb[0]==1 and largestRect.collidepoint(mx,my):
        radius=50 #changes radius to 50 if mouse clicks on large preset radius selector box
        
#IF CLICKS ON ART TOOLS...----------------------------------------------------------
    if pencilRect.collidepoint(mx,my) and mb[0]==1:
        curTool="penciltool" 
    if paintRect.collidepoint(mx,my) and mb[0]==1:
        curTool="brushtool" 
    if eraserRect.collidepoint(mx,my) and mb[0]==1:
        curTool="erasertool" 
    if penRect.collidepoint(mx,my) and mb[0]==1:
        curTool="pentool" 
    if lineRect.collidepoint(mx,my) and mb[0]==1:
        curTool="linetool" 
    if lineRect.collidepoint(mx,my) and mb[2]==1:
        curTool="drawpolytool" 
    if elipseRect.collidepoint(mx,my) and mb[0]==1:
        curTool="filledelipsedrawertool" 
    if elipseRect.collidepoint(mx,my) and mb[2]==1:
        curTool="emptyelipsedrawertool" 
    if rectRect.collidepoint(mx,my) and mb[0]==1:
        curTool="filledrectdrawertool" 
    if rectRect.collidepoint(mx,my) and mb[2]==1:
        curTool="emptyrectdrawertool"   
    if eyedropperRect.collidepoint(mx,my) and mb[0]==1:
        curTool="eyedroppertool" 
    if sprayRect.collidepoint(mx,my) and mb[0]==1:
        curTool="spraytool" 
    if fillRect.collidepoint(mx,my) and mb[0]==1:
        curTool="filltool" 
    if magic1Rect.collidepoint(mx,my) and mb[0]==1:
        curTool="magic1tool" 
    if magic2Rect.collidepoint(mx,my) and mb[0]==1:
        curTool="magic2tool"  

#IF CLICKS ON STAMP TOOLS...----------------------------------------------------  
    if usRect.collidepoint(mx,my) and mb[0]==1:        
        curTool="USstamp"
        resize=1 #goes to default stamp size
    if ukRect.collidepoint(mx,my) and mb[0]==1:        
        curTool="UKstamp"
        resize=1 #goes to default stamp size
    if franceRect.collidepoint(mx,my) and mb[0]==1:        
        curTool="Francestamp"
        resize=1 #goes to default stamp size
    if russiaRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Russiastamp"
        resize=1 #goes to default stamp size
    if chinaRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Chinastamp"
        resize=1 #goes to default stamp size
    if canadaRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Canadastamp"
        resize=1 #goes to default stamp size
    if germanyRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Germanystamp"
        resize=1 #goes to default stamp size
    if italyRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Italystamp"
        resize=1 #goes to default stamp size
    if japanRect.collidepoint(mx,my) and mb[0]==1:
        curTool="Japanstamp"
        resize=1 #goes to default stamp size
    if bg1Rect.collidepoint(mx,my) and mb[0]==1:
        curTool="Wallpaper1"
    if bg2Rect.collidepoint(mx,my) and mb[0]==1:
        curTool="Wallpaper2"

#IF CLICK ON CANVAS...-------------------------------------------------------
    if curTool=="penciltool":
        txtPic = comicFontlarge.render("Basic pencil", True, (0,0,0)) #***txtPic is the message displayed in the info bar under the canvas***
        iconselectcoordinates=(20,300)
        selectborder = artselect #***selectborder is which border to use***
        if mb[0]==1 and canvasRect.collidepoint(mx,my): #***uses tool only if mouse clicks on canvas area***
            penciltool()
    elif curTool=="brushtool":
        txtPic = comicFontlarge.render("Circular paintbrush", True, (0,0,0))
        iconselectcoordinates=(100,300)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            brushtool()
    elif curTool=="erasertool":
        txtPic = comicFontlarge.render("Eraser tool", True, (0,0,0))
        iconselectcoordinates=(180,300)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            erasertool()
    elif curTool=="pentool":
        txtPic = comicFontlarge.render("Calligraphy tool", True, (0,0,0))
        iconselectcoordinates=(260,300)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            pentool()
    elif curTool=="linetool":
        txtPic = comicFontlarge.render("Line tool", True, (0,0,0))
        iconselectcoordinates=(20,380)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            linetool()
    elif curTool=="drawpolytool":
        txtPic = comicFontsmall.render("Poly tool (Click on the canvas to set the vertices of a polygon. Right click to close the polygon!)", True, (0,0,0))
        iconselectcoordinates=(20,380)
        selectborder = artselect
        if clickDown and canvasRect.collidepoint(mx,my):            
            drawpoly()
        if mb[2]==1:                
            if canvasRect.collidepoint(mx,my) and len(polyList)>2:
                draw.polygon(screen,(drawColour), polyList,2) #draws a polygon that connects all the points in polyList
                undolist+=[screen.subsurface(canvasRect).copy()] #adds a copy of the canvas to undolist (because undolist only works automatically if you left click on the canvas   
            polyList=[] #empties polyList when done               
    elif curTool=="filledelipsedrawertool":
        txtPic = comicFontlarge.render("Filled ellipses tool", True, (0,0,0))
        iconselectcoordinates=(100,380)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            filledelipsedrawertool()
    elif curTool=="emptyelipsedrawertool":
        txtPic = comicFontlarge.render("Empty ellipses tool", True, (0,0,0))
        iconselectcoordinates=(100,380)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            emptyelipsedrawertool()
    elif curTool=="filledrectdrawertool":
        txtPic = comicFontlarge.render("Filled rectangles tool", True, (0,0,0))
        iconselectcoordinates=(180,380)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            filledrectdrawertool()
    elif curTool=="emptyrectdrawertool":
        txtPic = comicFontlarge.render("Empty rectangles tool", True, (0,0,0))
        iconselectcoordinates=(180,380)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            emptyrectdrawertool()
    elif curTool=="eyedroppertool":
        txtPic = comicFontlarge.render("Eyedropper tool (Gets the colour of almost anywhere in the window)", True, (0,0,0))
        iconselectcoordinates=(260,380)
        selectborder = artselect
        if mb[0]==1:
            eyedroppertool()
    elif curTool=="spraytool":
        txtPic = comicFontlarge.render("Spraypaint tool", True, (0,0,0))
        iconselectcoordinates=(20,460)
        selectborder = artselect
        if mb[0]==1:
            spraytool()
    elif curTool=="filltool":
        txtPic = comicFontlarge.render("Fill tool", True, (0,0,0))
        iconselectcoordinates=(100,460)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            filltool()
    elif curTool=="magic1tool":
        txtPic = comicFontlarge.render("Textured brush (aka Tinsel tool)", True, (0,0,0))
        iconselectcoordinates=(180,460)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            magic1tool()
    elif curTool=="magic2tool":
        txtPic = comicFontlarge.render("Confetti tool!!", True, (0,0,0))
        iconselectcoordinates=(260,460)
        selectborder = artselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            magic2tool()
    elif curTool=="USstamp":
        txtPic = comicFontlarge.render("America stamp ~The hero!!", True, (0,0,0))
        iconselectcoordinates=(450,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            USstamp()
    elif curTool=="UKstamp":
        txtPic = comicFontlarge.render("England stamp ~Absolutely gentlemanly", True, (0,0,0))
        iconselectcoordinates=(550,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            UKstamp()
    elif curTool=="Francestamp":
        txtPic = comicFontlarge.render("France stamp ~Bonjour", True, (0,0,0))
        iconselectcoordinates=(650,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Francestamp()   
    elif curTool=="Chinastamp":
        txtPic = comicFontlarge.render("China stamp ~aru!", True, (0,0,0))
        iconselectcoordinates=(850,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Chinastamp()
    elif curTool=="Russiastamp":
        txtPic = comicFontlarge.render("Russia stamp ~Comes with a sunflower", True, (0,0,0))
        iconselectcoordinates=(750,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Russiastamp()
    elif curTool=="Canadastamp":
        txtPic = comicFontlarge.render("Canada stamp ~Who?", True, (0,0,0))
        iconselectcoordinates=(950,700)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Canadastamp()
    elif curTool=="Germanystamp":
        txtPic = comicFontlarge.render("Germany stamp ~Doitsu Doitsu...Do...Do...Doitsu!", True, (0,0,0))
        iconselectcoordinates=(450,800)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Germanystamp()
    elif curTool=="Italystamp":
        txtPic = comicFontlarge.render("Italy stamp ~PAAAASTAAAAAA!!!", True, (0,0,0))
        iconselectcoordinates=(550,800)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Italystamp()
    elif curTool=="Japanstamp":
        txtPic = comicFontlarge.render("Japan stamp ~...", True, (0,0,0))
        iconselectcoordinates=(650,800)
        selectborder = stampselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            Japanstamp()
    elif curTool=="Wallpaper1":
        txtPic = comicFontsmall.render("Wallpaper tool (Click on the canvas to blit on wallpaper ~Gakuen Hetalia)", True, (0,0,0))
        iconselectcoordinates=(750,800)
        selectborder = wallpaperselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            wallpaper1()
    elif curTool=="Wallpaper2":
        txtPic = comicFontsmall.render("Wallpaper tool (Click on the canvas to blit on wallpaper ~Soccer)", True, (0,0,0))
        iconselectcoordinates=(850,800)
        selectborder = wallpaperselect
        if mb[0]==1 and canvasRect.collidepoint(mx,my):
            wallpaper2()
#MESSAGES ETC.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    draw.rect(screen,(drawColour),(370,808,40,40)) #displays current colour in a box
    draw.rect(screen,(infobarColour),(447,625,730,27)) #draws an info bar (underneath the canvas)
    screen.blit(txtPic,(447,625)) #displays txtPic (message inside info bar)
    screen.blit(selectborder,(iconselectcoordinates)) #displays a border around the current tool
    draw.rect(screen,(infobarColour),(306,758,105,27)) #draws a rectangle that will be used to display the current radius
    txtRadius = comicFontsmall.render("Radius: "+str(radius), True, (0,0,0)) #message indicating current radius 
    screen.blit(txtRadius,(310,760))

    if canvasRect.collidepoint(mx,my): #if the mouse is in the canvas a box on the right of the info bar appears and blits a message indicating current mouse position
        mouseposition = comicFontsmall.render("mx,my= ("+str(mx-447)+","+str(my-120)+")", True, (0,0,0)) #message indicating current mouse position
        draw.rect(screen,(216,191,216),(1050,625,127,27)) #draws a rectangle that will be used to display the current mouse position
        screen.blit(mouseposition,(1055,627))
#HOVER BORDERS AND TOOL MESSAGES~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        
    if pencilRect.collidepoint(mx,my): #***if mouse collides with tool icon***
        screen.blit(arthover,(20,300)) #***blits green border around icon***
        if mb[0]==1:
            screen.blit(selectborder,(20,300)) #***displays a black border around icon if you press it***
    if paintRect.collidepoint(mx,my): 
        screen.blit(arthover,(100,300)) 
        if mb[0]==1:
            screen.blit(selectborder,(100,300)) 
    if eraserRect.collidepoint(mx,my): 
        screen.blit(arthover,(180,300))
        if mb[0]==1:
            screen.blit(selectborder,(180,300)) 
    if penRect.collidepoint(mx,my): 
        screen.blit(arthover,(260,300)) 
        if mb[0]==1:
            screen.blit(selectborder,(260,300)) 
    if lineRect.collidepoint(mx,my): 
        screen.blit(arthover,(20,380)) 
        hoverMessage = comicFontsmall.render("Left click: line tool, Right click: polygon tool", True, (0,0,0)) #***writes a message in the info bar explaining different tools when you left/right click***
        draw.rect(screen,(infobarColour),(447,625,730,27))
        screen.blit(hoverMessage,(447,625))
        if mb[0]==1:
            screen.blit(selectborder,(20,380)) 
    if elipseRect.collidepoint(mx,my): 
        screen.blit(arthover,(100,380)) 
        hoverMessage = comicFontsmall.render("Left click: filled ellipse tool, Right click: empty ellipse tool", True, (0,0,0)) 
        draw.rect(screen,(infobarColour),(447,625,730,27))
        screen.blit(hoverMessage,(447,625))
        if mb[0]==1 or mb[2]==1:
            screen.blit(selectborder,(100,380)) 
    if rectRect.collidepoint(mx,my): 
        screen.blit(arthover,(180,380)) 
        hoverMessage = comicFontsmall.render("Left click: filled rectangle tool, Right click: empty rectangle tool", True, (0,0,0)) #writes a message in the info bar explaining different tools when you left/right click
        draw.rect(screen,(infobarColour),(447,625,730,27))
        screen.blit(hoverMessage,(447,625))
        if mb[0]==1 or mb[2]==1:
            screen.blit(selectborder,(180,380)) 
    if eyedropperRect.collidepoint(mx,my): 
        screen.blit(arthover,(260,380)) 
        if mb[0]==1:
            screen.blit(selectborder,(260,380)) 
    if sprayRect.collidepoint(mx,my): 
        screen.blit(arthover,(20,460)) 
        if mb[0]==1:
            screen.blit(selectborder,(20,460)) 
    if fillRect.collidepoint(mx,my): 
        screen.blit(arthover,(100,460)) 
        if mb[0]==1:
            screen.blit(selectborder,(100,460)) 
    if magic1Rect.collidepoint(mx,my): 
        screen.blit(arthover,(180,460)) 
        if mb[0]==1:
            screen.blit(selectborder,(180,460)) 
    if magic2Rect.collidepoint(mx,my): 
        screen.blit(arthover,(260,460)) 
        if mb[0]==1:
            screen.blit(selectborder,(260,460)) 
    if usRect.collidepoint(mx,my): 
        screen.blit(stamphover,(450,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(450,700)) 
    if ukRect.collidepoint(mx,my): 
        screen.blit(stamphover,(550,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(550,700)) 
    if franceRect.collidepoint(mx,my): 
        screen.blit(stamphover,(650,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(650,700)) 
    if russiaRect.collidepoint(mx,my): 
        screen.blit(stamphover,(750,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(750,700)) 
    if chinaRect.collidepoint(mx,my):
        screen.blit(stamphover,(850,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(850,700)) 
    if germanyRect.collidepoint(mx,my): 
        screen.blit(stamphover,(450,800))
        if mb[0]==1:
            screen.blit(selectborder,(450,800)) 
    if italyRect.collidepoint(mx,my): 
        screen.blit(stamphover,(550,800)) 
        if mb[0]==1:
            screen.blit(selectborder,(550,800))
    if japanRect.collidepoint(mx,my): 
        screen.blit(stamphover,(650,800)) 
        if mb[0]==1:
            screen.blit(selectborder,(650,800)) 
    if canadaRect.collidepoint(mx,my): 
        screen.blit(stamphover,(950,700)) 
        if mb[0]==1:
            screen.blit(selectborder,(950,700))
    if bg1Rect.collidepoint(mx,my): 
        screen.blit(wallpaper1hover,(750,800)) #***blits 3D flag icon when hovered over***
        if mb[0]==1:
            screen.blit(selectborder,(750,800)) 
    if bg2Rect.collidepoint(mx,my): 
        screen.blit(wallpaper2hover,(850,800)) #***blits 3D flag icon when hovered over***
        if mb[0]==1:
            screen.blit(selectborder,(850,800)) 
    
    oldpos=omx,omy=mx,my #old mouse position
    display.flip()
quit()
