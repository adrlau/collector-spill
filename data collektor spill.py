# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 23:36:19 2018

@author: admin
"""

# -*- coding: utf-8 -*- 
""" 
Created on Tue Dec  4 14:29:58 2018 
  
@author: admin 


your data is running away and is splatted around ... 

help me get it back before the time runs upp and ...

i have visualised the data as red dots.  kollekt all of them to stay alive.


use wasd or arrows to move    (if you arre busy quit by q  or esc)

initalising         placing data


won if lvl 10


keep avay from  white circkles they are virus.

""" 
  
import pygame
import pylab
import time 
import math
  
pygame.init() # starting pygame 
port = 50
startime =   time.clock()
tidtaker = 0
tidk = 0
timeleft = 105

# Define some esential colors 
BLACK = (20, 20, 20) 
WHITE = (255, 255, 255) 
GREEN = (0, 255, 0) 
RED = (255, 0, 0) 
BLUE = (0, 0, 255) 

#hvis en trenger en tilfeldig farge.   velger ut fra ett utvalg for å unngå alle mulige nyansene 
def randcollor(): 
     
     #liste med ulike fargeferdier 
    collor = [[0,250,0],[0,180,0],[0,100,0],[185,0,0],[0,185,0],[0,0,185],[185,40,15],[0,150,180],[150,150,0],[150,0,150]] 
     
     
    x = pylab.randint(0, len(collor)) 
     
    y = collor[x] 
                     
    return y
  
txtc = 0  
# game logics variables 
  
#setting varaibles for player cordinates 
plrx = 200 
plry = 300  
  
#spillerens størrelse 
plrsize = 50
  
#hvor fort spilleren beveger seg 
plrspeed = 7
  

#leveltil bygninger og frukt

score = 0

lvl = 10



#arrow / wasd  status 
up = 0 
  
down = 0 
  
left = 0
  
right = 0
  
  
  
  
  
# setting the display size  will affekt the size of the window opened 
dispx = 1280 
dispy = 700 
  
display = (dispx,dispy) 
  
screen = pygame.display.set_mode(display) 
  
pygame.display.set_caption("D@ta C0llek1er") 
  
# Loop until the user clicks the close button. 
done = False
  
# Used to manage how fast the screen updates 
clock = pygame.time.Clock() 
  
  
  
applesice = 15

applex = 0
appley = 0


virusice = 15

virusx = 0
virusy = 0
  
  
#  game logic funktions 
  
def text_objects(text, font):
    
    global txtc
    
    if txtc == 0:
        textSurface = font.render(text, True, (0,140,0))
    else:   
        textSurface = font.render(text, True, randcollor())
    
    
    
    return textSurface, textSurface.get_rect()





def message_display(text,x,y):
    
    
    largeText = pygame.font.Font('freesansbold.ttf',50)
    
    
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((x),(y))
    screen.blit(TextSurf, TextRect)
    
    
    

def do_circle_demo(surface, counter):
        x = surface.get_width() // 2
        y = surface.get_height() // 2
        max_radius = min(x, y) * 4 // 5
        radius = abs(int(math.sin(counter * 3.14159 * 2 / 200) * max_radius)) + 1
        color = (0, 140, 255) # marineblå
        pygame.event.pump() # brukes for å si til windows at programmet jobber med interne prosesser
        # Draw a circle 
        pygame.draw.circle(surface, color, (x, y), radius)
        
 

#høyt nivå av inspirasjon og muligens litt låning av kode   men med verdiendringer    
def rotate_3d_points(points, angle_x, angle_y, angle_z):
        new_points = []
        for point in points:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                new_points.append([x, y, z])
        return new_points

# samme som rotate 3d points     men  har forstått hvordann å bruke 
def do_line_demo(surface, counter):
        color = (0, 140, 0) # green
        cube_points = [
                [-1, -1, 1],
                [-1, 1, 1],
                [1, 1, 1],
                [1, -1, 1],
                [-1, -1, -1],
                [-1, 1, -1],
                [1, 1, -1],
                [1, -1, -1]]
                
        connections = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
                ]
                
        t = counter * 2 * 3.14159 / 60
        

        points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
        flattened_points = []
        for point in points:
                flattened_points.append(
                        (point[0] * (1 + 1.0 / (point[2] + 3)),
                         point[1] * (1 + 1.0 / (point[2] + 3))))
        
        for con in connections:
                p1 = flattened_points[con[0]]
                p2 = flattened_points[con[1]]
                x1 = p1[0] * 60 + 200
                y1 = p1[1] * 60 + 150
                x2 = p2[0] * 60 + 200
                y2 = p2[1] * 60 + 150
                
                # dette er den viktigste linjen: 
                pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)
                





  
def slutt():
    global dispx
    global dispy
    global score
    global done
    global txtc
    txtc = 0
    
    screen.fill(BLACK)
    
    
    message_display('$y$1em 0verl0@d',dispx / 2, dispy / 2)
    pygame.display.update()
    time.sleep(1)

    screen.fill(BLACK)
    
    message_display('y0u f@!led at sector...',dispx / 2, dispy / 2)
    pygame.display.update()
    
    time.sleep(1)
    
    screen.fill(BLACK)
    
    message_display(str(lvl/10),dispx / 2, dispy / 2)
    pygame.display.update()
    
    time.sleep(1)
    
    
    done = True
    
    return
   



def lvlup():  
    global tidtaker
    global lvl
    global score
    global plrx
    global plry
    global dispx
    global dispy
    global timeleft
    global up
    global down
    global right
    global left
    global txtc
    plyrmovment()
    txtc = 0
    
    #setter til midten for ikke å overaske    må runde av fordi float ikke akseptert i tegne sirkel
    plrx = 150
    plry = round(dispy/2)
    up = 0
    down = 0
    left = 1
    right = 0
               
    
    score = 0
    
    lvl += 10
    
    
    for i in range(10, 200):
        time.sleep(0.01)
        screen.fill(BLACK) 
        do_circle_demo(screen, i)
        message_display('LVL up',dispx / 2, dispy / 2)
        pygame.display.update()
    
    fort = False    
    screen.fill(BLACK) 
    while fort == False:
    
        message_display('Y0u d!d w£ll',dispx / 2, dispy / 2 - 240)
        pygame.display.update()
        time.sleep(0.5)
            

        
    
        message_display('y0u w!ll be rew@rd..',dispx / 2, dispy / 2 - 190)
        pygame.display.update()
        time.sleep(0.5)
        

        message_display('and become a user...',dispx / 2, dispy / 2 - 140)
        pygame.display.update()
        time.sleep(0.5)
          
        message_display('But da1a !s...',dispx / 2, dispy / 2 - 90)
        pygame.display.update()
        time.sleep(0.5)

        
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:                     
                if event.key == ord('c'):
                    print('stop')
                    fort = True
            if event.type == pygame.QUIT: 
                        pygame.quit()        
        
        message_display(' s1!ll uns1able',dispx / 2, dispy / 2 - 40)
        pygame.display.update()
        time.sleep(0.5)

        
        message_display('7h!s w!ll be h@rder',dispx / 2, dispy / 2 + 20)
        pygame.display.update()
        time.sleep(0.5)
        
            
        message_display('c@n y0u ge7 10 m0re',dispx / 2, dispy / 2 + 70)
        pygame.display.update()
        time.sleep(0.5)
        
        message_display('press c to continue',dispx / 2, dispy / 2 + 130)
        pygame.display.update()
        time.sleep(1.5)

        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN:                     
                if event.key == ord('c'):
                    print('stop')
                    fort = True
            if event.type == pygame.QUIT: 
                        pygame.quit()
    

   #3d firkant og .. for å varsle at det starter 
    for i in range(10, 50):
        time.sleep(0.01)
        screen.fill(BLACK) 
        do_line_demo(screen, i)
        message_display('...',190,360)
        pygame.display.update()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT: 
                    pygame.quit()
                        
    #for å skifte mellom grønn eller tilfeldig det likner

    txtc = 1
    
    tidtaker = int(time.clock() - startime)
    
    timeleft = tidtaker + 100
    virus()
    apple()
    plyrmovment()
    return  
 
    
# sett deg inn i dette
def plyrmovment(): 
    
    
    
     
    #keys() 
     
    #bruker de globale verdiene istedet for å sende inn 
     
    #spillers x og y pos 
    global plrx 
    global plry 
     
    global plrspeed 
    global txtc
    
    #trenger for å fortsette i en retning 
    #taster 
    global up 
    global down 
    global right 
    global left 
     
    global BLACk
    
    #skjermstørrelsen  
    global dispx 
    global dispy 
     
    global done 
  
    global lvl
    
    global score
    
    global plrsize
     
        # endrer spiller x og y og tegner in øyne
         

     
    if event.type == pygame.KEYDOWN:
        
        if down == 0:
                     
            if event.key == pygame.K_UP or event.key == ord('w'): 
                        
                        #plry -= plrspeed
                        
                        up = 1
                        down = 0
                        left = 0
                        right = 0
                        
        if up == 0:
                
            if event.key == pygame.K_DOWN or event.key == ord('s'):
             
                        
                        #plry += plrspeed
                        
                        up = 0
                        down = 1
                        left = 0
                        right = 0
        if right == 0:                
            if event.key == pygame.K_LEFT or event.key == ord('a'):
             
                        #plrx -= plrspeed
                        
                        up = 0
                        down = 0
                        left = 1
                        right = 0 
        if left == 0:
            if event.key == pygame.K_RIGHT or event.key == ord('d'): 

                        #plrx += plrspeed                        
                        up = 0
                        down = 0
                        left = 0
                        right = 1
                        
        
        
        #skal kunne quitte eller avslutte underveis med enten q eller esc hvis en ønsker å slutte
        if event.key == pygame.K_ESCAPE or event.key == ord('q'):                         
                        done = True
    
    
    #for debugging og juksing
        if event.key == ord('l'):
                        lvl += 10
                        
                        time.sleep(1)
    #for debugging og juksing
        if event.key == ord('k'):
                        lvl -= 10
                        
                        time.sleep(1)
    #for debugging og juksing
        if event.key == ord('j'):
                        score -= 10
                        
                        time.sleep(1)
    #for debugging og juksing
        if event.key == ord('i'):
                        score += 10
                        
                        time.sleep(1)
                        
        if event.key == ord('o'):
                        for i in range(10, 80):
                            time.sleep(0.1)
                            screen.fill(BLACK) 
                            do_circle_demo(screen, i)
                            pygame.display.update()
                            
                            
        if event.key == ord('p'):                         
                        time.sleep(3)
                        up = 0 
  
                        down = 0 
  
                        left = 0
  
                        right = 0
                        
    
                        
        if event.key == ord('m'):
                        txtc = 0
                        screen.fill(BLACK) 
                        message_display('made by:',dispx / 2, dispy / 2)
                        pygame.display.update()
                        time.sleep(1.5)
                        screen.fill(BLACK) 
                        message_display('Adrian Gunnar Lauterer',dispx / 2, dispy / 2)
                        pygame.display.update()
                        time.sleep(1.5)
                        screen.fill(BLACK) 
                        message_display('and',dispx / 2, dispy / 2)
                        pygame.display.update()
                        time.sleep(1.5)
                        screen.fill(BLACK) 
                        message_display('Anne Marie Botterud',dispx / 2, dispy / 2)
                        pygame.display.update()
                        time.sleep(1.5)
                        txtc = 1
    
    #kan legge til kode her for hvis treffer rammene eller legge det inn nøstet under bevegelsen 
    if plrx + plrsize > dispx: 
                slutt()
         
    if plry + plrsize > dispy: 
                slutt() 
         
    if plrx - plrsize < 0: 
                slutt() 
         
    if plry - plrsize < 60: 
                slutt()
     
    return 
  
def apple():
    global applex
    global appley
    global applesice
    
    applex = pylab.randint(applesice +60, dispx-applesice-60)
    appley = pylab.randint(applesice + 120, dispy-applesice-60)
    
    while (applex - applesice) >= (plrx - plrsize) and (applex + applesice) <= (plrx + plrsize) and (appley - applesice) >= (plry - plrsize) and (appley + applesice) <= (plry + plrsize):

        applex = pylab.randint(applesice +60, dispx-applesice-60)
        appley = pylab.randint(applesice + 120, dispy-applesice-60)
    
    return

# virus koden
def virus():
    global virusx
    global virusy
    global virusice
    global applex
    global appley
    global applesice
    global plrx 
    global plry 
    global plrsize
    
   # virusx = pylab.randint(virusice +60, dispx-virusice-60)
   # virusy = pylab.randint(virusice + 120, dispy-virusice-60)
    
   
    virusx = pylab.randint(virusice +60, dispx-virusice-60)
    virusy = pylab.randint(virusice + 120, dispy-virusice-60)
    
    print('virus started')
      
    if (virusx - virusice) >= (plrx - (plrsize*2)) and (virusx + virusice) <= (plrx + (plrsize*2)) and (virusy - virusice) >= (plry - (plrsize*2)) and (virusy + virusice) <= (plry + (plrsize*2)):           
            print('awoided')    
            rnd = pylab.randint(0,10)
            if rnd < 3:
                virusx += 200
            elif rnd > 3 and rnd < 5:
                virusx -= 200
            elif rnd > 5 and rnd < 7:
                virusy +=200
            else:
                virusy -= 200
              

# spill start/intro
for i in range(10, 300):
        time.sleep(0.01)
        screen.fill(BLACK) 
        do_line_demo(screen, i)
        message_display('initalising...',190,360)
        pygame.display.update()
        for event in pygame.event.get():    
            if event.type == pygame.QUIT: 
                    pygame.quit()
                        


txtc = 0
   
fort = False

while fort == False:
    
    screen.fill(BLACK) 
    message_display('Hello. i`m you`r guide',dispx / 2, dispy / 2 - 250)
    pygame.display.update()
    time.sleep(0.7)
    message_display('Y0ur da1a !$ dissapering.',dispx / 2, dispy / 2 - 200)
    pygame.display.update()
    time.sleep(0.7)
    
    message_display('1he da1a !s GR££N circles.',dispx / 2, dispy / 2 - 150)
    pygame.display.update()
    time.sleep(0.7)
    message_display('Y0u have to c0llec1 !1.',dispx / 2, dispy / 2 - 100)
    pygame.display.update()
    time.sleep(0.7)
    
    for event in pygame.event.get():    
        if event.type == pygame.KEYDOWN:                     
            if event.key == ord('c'):
                print('stop')
                fort = True
        if event.type == pygame.QUIT: 
                pygame.quit()
#for at windows skal se spillet som aktivt
    pygame.event.pump()
    message_display('0r £lse the system will fail.',dispx / 2, dispy / 2 - 50)
    pygame.display.update()
    time.sleep(0.7)
    #for at windows skal se spillet som aktivt
    pygame.event.pump()
    message_display('t0 m0ve,wasd 0r arr0ws',dispx / 2, dispy / 2)
    pygame.display.update()
    time.sleep(0.7)
    
    pygame.event.pump()
    message_display('Be aw@re 0f 1he white virus',dispx / 2, dispy / 2 + 50)
    pygame.display.update()
    time.sleep(0.7)
    #for at windows skal se spillet som aktivt
    
    message_display('press c to continue',dispx / 2, dispy / 2 + 100)
    pygame.display.update()
    time.sleep(1.5)

    for event in pygame.event.get():    
        if event.type == pygame.KEYDOWN:                     
            if event.key == ord('c'):
                print('stop')
                fort = True
        if event.type == pygame.QUIT: 
                pygame.quit()


screen.fill(BLACK)
message_display('G00d luck',dispx / 2, dispy / 2)
pygame.display.update()
time.sleep(2)


# for at personen skal starte stillestående    
txtc = 1    
up = 0
down = 0
left = 0
right = 0  
virus() 


# -------- Main Program Loop ----------- 
while done == False: 
     
     
    # --- Main event loop 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            screen.fill(BLACK) 
            message_display('sys1em shutd0wn',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1)
            pygame.quit() 
            
        
            
    screen.fill(BLACK)    # nulstiller skjermen til svart for å skrive ut ett nytt vindu. 
     
    plyrmovment()
    pygame.draw.rect(screen,BLUE,(0,(dispy/2)-(plrsize+40),30,(plrsize*2)+80))
    pygame.draw.rect(screen,BLUE,(dispx-30,(dispy/2)-(plrsize+40),30,(plrsize*2)+80))        
    
    if plrx + plrsize > dispx - 10 and plry > (dispy/2)-50 and plry < (dispy /2) + 50 :
            plrx = plrsize+15
            up = 0
            down = 0
            left = 0
            right = 1
            
            
    elif plrx - plrsize < 10 and plry > (dispy/2)-50 and plry < (dispy /2) + 50 :
            plrx = (dispx-plrsize)-15
            up = 0
            down = 0
            left = 1
            right = 0

            
            
    
    #hvis treffer data/eple øk score med 1
     
    # regner med en firkantet hitbox fordi det krever midre regnekraft og fordi 
    # akkuratt overlappen mellom hjørnene i firkantene ikke er for stor en kan se på det som firkenter men hjørnene er visuellt avrundet for en bedre estetikk 
    
    # registrer om truffet fra eple
    
    if (applex - applesice) >= (plrx - plrsize) and (applex + applesice) <= (plrx + plrsize) and (appley - applesice) >= (plry - plrsize) and (appley + applesice) <= (plry + plrsize):
                    score += 1
                    apple()
                    virus() 
                    print('gathered')
    
    
    message_display('DLeft', 85 , 30)
    message_display(str(lvl - score), 245 , 30)
       
    
    # regner for treff fra virus    
    if (virusx - virusice) >= (plrx - plrsize) and (virusx + virusice) <= (plrx + plrsize) and (virusy - virusice) >= (plry - plrsize) and (virusy + virusice) <= (plry + plrsize)  :
                screen.fill(BLACK) 
                message_display('v!ru$ de1ec1ed',dispx / 2, dispy / 2)
                pygame.display.update()
                time.sleep(1)    
                screen.fill(BLACK) 
                message_display('$y$1em c0n1am!n@1ed',dispx / 2, dispy / 2)
                pygame.display.update()
                time.sleep(1)         
                slutt()
                    
                    
        
        
        
        # registrerer ønsket reisevei for spilleren 
     
    tidtaker = int(time.clock() - startime)
    
    message_display(str(timeleft - tidtaker), dispx-60 , 30)
    
    if timeleft < tidtaker:
        slutt()
    
    
# level for å øke hastigheten på deg og data/eple for å øke kaoset og vanskeligheten / tilfeldigheter 

#  vet at er resurskrevende men elseif lnsket ikke å fungere
    
# endrer stats etter lvl     
    
    if lvl <= 20:
        
        plrsize = 70
        
        spwn = 7
        
        sped = 7
    
    if lvl > 20:
        
        plrsize = 60
        
        spwn = 7
        
        sped = 9    
        
        
    if lvl >= port:
        pygame.draw.rect(screen, WHITE,(round(dispx/2)-10,0,20,dispy)) 
        
        plrsize = 50
        spwn = 5
        sped = 10
    
        if plrx + plrsize > dispx/2 -10 and plrx - plrsize < dispx/2 +10 :
            slutt()
        
    if lvl >= 70:
            plrsize = 30
            spwn = 3
            sped = 15

     
    if lvl >= 110:
            print('ferdig')
            #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK) 
            message_display('Y0r servi$e w@s',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK) 
            message_display('awesome',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            screen.fill(BLACK) 
            message_display('you will now become',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('A USER',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('....',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('You are given...',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('A life in luxury',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('Hope you will...',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('Be...be a good user',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
                        #for at windows skal se spillet som aktivt
            pygame.event.pump()
            screen.fill(BLACK)
            message_display('time to convert',dispx / 2, dispy / 2)
            pygame.display.update()
            time.sleep(1.5)
            
            done = True
            
        
        

        
        
    

        
    
    if tidk < tidtaker:
        virus()
        apple()
        
        tidk += spwn
     
     
        
    if score >= lvl:
        lvlup()  
        print('lvl up')
        
       
    message_display('Sector', dispx /2 -10, 30)    
    message_display(str(lvl/10), dispx /2 +200 , 30)    
        
        #tegner opp en grenselinje for å skille info og spillbrett
    message_display('--------------------------------------------------------------------------------', dispx /2 -60, 60)
        
    
    
    pygame.draw.circle(screen, randcollor(), (plrx, plry), plrsize,)
     
    pygame.draw.circle(screen, GREEN, (applex, appley), applesice,)
    pygame.draw.circle(screen, WHITE, (virusx, virusy), virusice,)
    
    if left == 0 and right == 0 and down == 0 and up == 0: 
            print('')
         
         
    if left == 1 and right == 0 and down == 0 and up == 0: 
         
        plrx -= plrspeed
        pygame.draw.circle(screen, BLUE, (plrx - round(plrsize/2), plry - round(plrsize/3)), round(plrsize/4),)
    elif left == 0 and right == 1 and down == 0 and up == 0: 
         
        plrx += plrspeed 
        pygame.draw.circle(screen, BLUE, (plrx + round(plrsize/2), plry - round(plrsize/3)), round(plrsize/4),)
     
    elif left == 0 and right == 0 and down == 0 and up == 1: 
         
        plry -= plrspeed
        
        pygame.draw.circle(screen, BLUE, (plrx, plry - round(plrsize/2)), round(plrsize/4),)
     
    elif left == 0 and right == 0 and down == 1 and up == 0: 
        
        pygame.draw.circle(screen, BLUE, (plrx, plry + round(plrsize/2)), round(plrsize/4),)
        
        plry += plrspeed
    
    # --- Go ahead and update the screen with what we've drawn. 
    pygame.display.flip() 
  
    # --- Limit to 30 frames per second 
    clock.tick(30) 
    
# Close the window and quit. 
pygame.event.pump()    
screen.fill(BLACK) 

message_display('Err0r.....',dispx / 2, dispy / 2)
pygame.display.update()
time.sleep(0.5)
screen.fill(BLACK) 

message_display('Err0r.....',dispx / 2, dispy / 2)
pygame.display.update()
time.sleep(0.5)  

screen.fill(BLACK) 
message_display('sys1em shutd0wn',dispx / 2, dispy / 2)
pygame.display.update()
time.sleep(1)
pygame.quit() 