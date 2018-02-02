import os

winx = 200
winy = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (winx, winy)
import pygame
import pdb

from random import randint
# x = (randint(0, 800))

class character:
    def __init__(self, name, strength,x,y):
        self.name = name
        self.strength = strength
        self.x=x
        self.y=y
class multiItem:
    def __init__(self, name, noise, dammage, uses):
        self.name = name
        self.uses = uses
        self.noise = noise
        self.dammage = dammage

    def use(self, who):
        if self.uses > 0:
            self.uses -= 1
            who.strength -= self.dammage
        print self.noise
class item:
    def __init__(self, name, noise, dammage):
        self.name = name
        self.noise = noise
        self.dammage = dammage

    def use(self, who):
        who.life -= self.dammage
        print self.noise
class itemInerte:
    def __init__(self, name, returns):
        self.name = name
        self.returns = returns

    def use(self):
        print self.returns
class space:
    def __init__(self,name, x, y, inside, locked, items):
        self.name = name
        self.x = x
        self.y = y
        self.inside = inside
        self.locked = locked
        self.items = items

"""Setting the game variables"""
# items
knife = item("knife", "Schwift!", 2)
pan = item("pan", "Clong!", 1)
fist = item("fist", "Flap!", 0)
talk = item("talk", "bla bla bla", 0)
scream = item("scream", "AAAAAAAAAAAAHHH!", 0)
hideout = item("Hideout", "You rapidly got into the hideout", 0)
call911 = item("911", "tititin tititin!", 1)
gun = multiItem("Gun", "pan!", 3, 6)
pipeCleanser = multiItem("Pipe cleanser acid", "Ssschaffff!", 3, 2)
tv=itemInerte("Tv","Tv is tuned to some American Football Match. Buttons are destroyed and dirty. It is impossible to change the channel or turn off")
mirror=itemInerte("Mirror","The mirror reflects your image. You look sad and tired.")
bed=itemInerte("Bed","The bed is undone and smell like urine, you probably shouldn't lie down there")
yourbed=itemInerte("Your bed","You lie for 5 minutes but you stand up again. It is no time to rest!")
milk=itemInerte("milk","Lily would probably need some of it. Good you thought of it")
toiletpaper=itemInerte("toilet paper","We could use some")
cereal=itemInerte("cereal","Lily loves this cereal")
# Characters
Joe = character("Joe", 10,2,3)
Lupe = character("Lupe", 5,1,1)
Lily = character("Lily", 3,3,2)
PoliceAgent = character("Police Agent", 1,0,0)
Dog = character("dog", 1,1,0)
Beggar = character("beggar", 1,1,0)
ShopAssitant = character("Shop Asistant", 1,2,0)
# spaces
toilet=space("toilet",1,2,True,False,[mirror])
LupeRoom= space("your room",1, 1,True,False, [yourbed])
kitchen = space("the kitchen",2, 1,True,False, [knife, pan])
living=space("the living room",2,2,True,False,[tv])
JoeRoom= space("Joes' room",2, 3,True,False, [bed])
LilyRoom= space("Lily's room",3, 2,True,False, [bed])
camino= space("the town path",1,0,False,False, [])
comisaria= space("the Sheriff's office",0, 0,False,False, [])
tienda= space("the town shop",2, 0,False,False, [cereal, pipeCleanser, toiletpaper, milk])

mapa={"12":toilet,"11":LupeRoom,"21":kitchen,"22":living,"23":JoeRoom,"32":LilyRoom,"10":camino,"00":comisaria,"20":tienda}


turn=0
alive=True
print "It's 6 in the morning. Time to wake up!"
while alive:  #empieza la aventura!
    yourlocationkey=str(Lupe.x)+str(Lupe.y)
    yourlocation=mapa[yourlocationkey]
    print "You're at "+yourlocation.name+". Around you there is:"
    for element in yourlocation.items:
        print "- "+element.name
    whatnext=raw_input("What do you want to do?")
    gun.use(Joe)
    print gun.uses
    print Joe.strength
    #print kitchen.items
    alive=False

##alive=True
##while alive==True:
##
##    pygame.init()
##    screen = pygame.display.set_mode((800, 700)) #,pygame.NOFRAME)
##    done = False
##    readytorestart=True
##
##
##    clock = pygame.time.Clock()
##    font = pygame.font.SysFont("comicsansms", 48)
##    font2 = pygame.font.SysFont("comicsansms", 24)
##    font3 = pygame.font.SysFont("comicsansms", 10, bold=True)
##    text = ""
##    text2 = font2.render("PRESS SPACE BAR TO RETRY", True, (255, 255, 255))
##    points = font2.render("", True, (255, 255, 255))
##
##    image = pygame.image.load('lunar_lander.png')
##
##    effect = pygame.mixer.Sound('rocket.wav')
##
####    pygame.mixer.music.load('music.mp3')
####    pygame.mixer.music.play(-1)
##
##    """Space creation"""
##
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            alive = False
##        
##    pressed = pygame.key.get_pressed()
##    if pressed[pygame.K_UP]:
##        pass
##    if pressed[pygame.K_LEFT]:
##        pass
##    if pressed[pygame.K_RIGHT]:
##        pass
##    if event.type == pygame.KEYUP: #when teh key is released
##        pass
##    screen.fill((0, 0, 0))
##    screen.blit(image, (x, y))
##    
##    gastext = font2.render("Gas: " + str(gas), True, (255, 255, 255))
##    screen.blit(gastext,(5, 670))
##
##    if fireshow==True:
##        screen.blit(fuego, (x+10, y+50))
##    if fireshowl==True:
##        screen.blit(firel, (x-5, y+10))
##    if fireshowr==True:
##        screen.blit(firer, (x+40, y+10))
##
##    #explodel= screen.get_at((int(x+5), int(y+45))) #gets pixel color at x,y position
##
##    clock.tick(60)
##    pygame.display.flip()
####
####        pygame.mixer.music.stop()
