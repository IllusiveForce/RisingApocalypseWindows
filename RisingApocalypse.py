




##Coded by Illusive_f0rce
##3rd person zombie shooter
__version__='0.5.6.5693456924562973459234765923475689'
import pygame as pg
import sys,random,time
from pygame.locals import *
zombie7Health=5
print(1.4142135623730950029591111111111*1.41421356237309500295911111111111)
fpsViewer=False
pg.init()
pg. display.set_caption('Rising Apocalypse v' + str(__version__))
loading=pg.transform.scale(pg.image.load('data/images/loading.png'),(800,700))
skorpion=False
FPS=100
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
darkgreen=(0,0,0)
yellow=(255,255,0)

clock=pg.time.Clock()

pg.display.set_icon(pg.image.load('data/images/icon.png'))

gameDisplay=pg.display.set_mode((800,700))
gameDisplay.blit(loading,(0,0))
pg.display.update()

x_change=8
y_change=0
selected=pg.image.load('data/images/ui/selected.png')
zombiey=100
zombiex=random.randint(5,850)
zombiex2=random.randint(5,850)
zombiey2=100
zombiex3=random.randint(5,850)
zombiey3=100
zombiex4=random.randint(5,850)
zombiey4=100
zombiex5=random.randint(5,850)
zombiey5=100
zombiex6=random.randint(5,850)
zombiey6=100
zombiex7=random.randint(5,850)
zombiey7=100 

x=400
y=400
scoreWriter=open('data/other/score.sta','r+')
score=int(scoreWriter.read())
inventory=[]
c=''

invWriter=open('data/other/inventory.sta','r+')
i=invWriter.read()

armorWriter=open('data/other/armor.sta','r+')
armors=armorWriter.read()

arsenalWriter=open('data/other/arsenal.sta','r+')
arsenalCode=arsenalWriter.read()

rebWriter=open('data/other/rebirths.sta','r+')
rebirths=int(rebWriter.read())
a=0
yourarmor=[]
arsenal=['Pistol']
try:
    while a<len(i):
        if i[a]!= '\n':
            c+=i[a]
        if i[a]=='\n':
            inventory.append(c)
            c=''
        a+=1
    a=0
    c=''
    while a<len(armors):
        if armors[a]!= '\n':
            c+=armors[a]
        if armors[a]=='\n':
            yourarmor.append(c)
            c=''
        a+=1
    c=''
    a=0
    while a<len(arsenalCode):
            if arsenalCode[a]!= '\n':
                c+=arsenalCode[a]
            if arsenalCode[a]=='\n':
                arsenal.append(c)
                c=''
            a+=1
except IndexError:
    pass








player=pg.image.load("data/images/Player.png")
player2=pg.image.load("data/images/Player.png")

playeri=pg.transform.scale(player,(70,90))
playeri2=pg.transform.scale(player2,(70,90))

playerLeft=pg.transform.rotate(pg.transform.scale(playeri,(70,90)),90)
playerRight=pg.transform.rotate(pg.transform.scale(playeri,(70,90)),-90)
playerBack=pg.transform.rotate(pg.transform.scale(playeri,(70,90)),180)

playerLeft2=pg.transform.rotate(pg.transform.scale(playeri2,(70,90)),90)
playerRight2=pg.transform.rotate(pg.transform.scale(playeri2,(70,90)),-90)
playerBack2=pg.transform.rotate(pg.transform.scale(playeri2,(70,90)),180)

backgrounda=pg.image.load("data/images/field.png")
bgX=-1000
bgY=-1000
bgRect=pg.Rect(bgX,bgY,19800,10800)
global healthw
health=10
counter=0

hx=10
hy=10
hx2=25
hy2=10
hx3=40
hy3=10
hx4=55
hy4=10
hx5=70
q1=0
bzx=500
bzy=50
hy5=10
flamethrower=False

BIGFONT=pg.font.Font('data/other/font.ttf',32)
font=pg.font.Font('data/other/font.ttf',28)
kindaBigFont=pg.font.Font('data/other/font.ttf',28)

bullets=40
bullet2x=0
bullet2img=pg.transform.scale(pg.image.load('data/images/ammocrate.png'),(40,40))

bulletsdisplay=BIGFONT.render('Bullets: '+str(bullets),False,darkgreen)
scoredisplay=BIGFONT.render('Kills:  ' +str(score),False,darkgreen)




z1=pg.image.load('data/images/zombie/skeleton-move_0.png')
z2=pg.image.load('data/images/zombie/skeleton-move_1.png')
z3=pg.image.load('data/images/zombie/skeleton-move_2.png')
z4=pg.image.load('data/images/zombie/skeleton-move_3.png')
z5=pg.image.load('data/images/zombie/skeleton-move_4.png')
z6=pg.image.load('data/images/zombie/skeleton-move_5.png')
z7=pg.image.load('data/images/zombie/skeleton-move_6.png')
z8=pg.image.load('data/images/zombie/skeleton-move_7.png')
z9=pg.image.load('data/images/zombie/skeleton-move_8.png')
z10=pg.image.load('data/images/zombie/skeleton-move_9.png')
z11=pg.image.load('data/images/zombie/skeleton-move_10.png')
z12=pg.image.load('data/images/zombie/skeleton-move_11.png')
z13=pg.image.load('data/images/zombie/skeleton-move_12.png')
z14=pg.image.load('data/images/zombie/skeleton-move_13.png')
z15=pg.image.load('data/images/zombie/skeleton-move_14.png')
z16=pg.image.load('data/images/zombie/skeleton-move_15.png')
z17=pg.image.load('data/images/zombie/skeleton-move_16.png')
zIterator=0
zombieImages=[z1,z2,z3,z4,z5,z6,z7,z8,z9,z10,z11,z12,z13,z14,z15,z16,z17]

image1=zombieImages[zIterator]
image3=zombieImages[zIterator]




p1=pg.image.load('data/images/player/player (1).png')
p2=pg.image.load('data/images/player/player (2).png')
p3=pg.image.load('data/images/player/player (3).png')
p4=pg.image.load('data/images/player/player (4).png')
p5=pg.image.load('data/images/player/player (5).png')
p6=pg.image.load('data/images/player/player (6).png')
p7=pg.image.load('data/images/player/player (7).png')
p8=pg.image.load('data/images/player/player (8).png')
p9=pg.image.load('data/images/player/player (9).png')
p10=pg.image.load('data/images/player/player (10).png')
p11=pg.image.load('data/images/player/player (11).png')
p12=pg.image.load('data/images/player/player (12).png')
p13=pg.image.load('data/images/player/player (13).png')
p14=pg.image.load('data/images/player/player (14).png')
p15=pg.image.load('data/images/player/player (15).png')
p16=pg.image.load('data/images/player/player (16).png')
p17=pg.image.load('data/images/player/player (17).png')
p18=pg.image.load('data/images/player/player (18).png')
p19=pg.image.load('data/images/player/player (19).png')
p20=pg.image.load('data/images/player/player (20).png')

playerImgs=[p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20]
playerIterator=0
playerImg=playerImgs[playerIterator]


pausemenu=pg.image.load('data/images/pausemenu.png')

image1=pg.transform.scale(image1,(50,50))
image3=pg.transform.rotate(pg.transform.scale(image3,(50,50)),180)

game=False

mainmenuimg=pg.transform.scale(pg.image.load('data/images/mainmenu.png'),(800,700))
mutated=pg.image.load('data/images/mutatedzombie.png')

mouserectpos=(0,0)

button=pg.draw.rect(gameDisplay,(0,0,100),Rect((800,650/2),(100,50)))
button2=pg.draw.rect(gameDisplay,(0,0,100),Rect((800,650/2+100),(100,50)))

mouserect=Rect((mouserectpos),(50,50))

heart1=pg.transform.scale(pg.image.load('data/images/ui/heart.png'),(10,10))
#Newer stuff
pauseButton=pg.draw.rect(gameDisplay,(0,0,0),Rect(800/2-25,0,80,20))

descriptions=['One step up from the pistol.','This weapon does little damage, but fires quickly.','Shoots lots of projectiles, so its good for close range.','More firepower makes this a deadly weapon.','Old and antique, but powerful.','Lots of firepower in a small package.','High damage and fire rate make this an essential.','Higher damage and higher fire rate make this more essential.','Lower spread and higher damage than the Shotgun make this very deadly.','Very efficient zombie killing machine.','Higher fire rate and capacity than the SCAR make this lethal.','Infects zombies with the deadly COVID-19 virus.','it yeets TNT at zombies','Yeets nuclear bombs at zombies, killing them.','Roasty Toasty.',"A sniper put a bullet in Maui's skull and is selling this weapon.",'Shoots bullets at the speed of light.','Super hot balls of gas. Excellent zombie exterminator.','Shoots concentrated beams of neutron radiation.'] 

dead=False


y_change=0
gameArcade=False
shotgun=False
gameSpeedRun=False
button3=pg.draw.rect(gameDisplay,(0,0,100),Rect((800/2-50,650/2+200),(100,50)))

zombie1Health=zombie2Health=zombie3Health=zombie4Health=zombie5Health=10
zombie6Health=15
gunStrength=2

backButton=pg.draw.rect(gameDisplay,black,Rect(1000,10,100,50))
mp5size=40

playerImg=playeri

mutatedzombiex=-100
mutatedzombiey=-100
mutatedzombie=pg.transform.scale(pg.image.load('data/images/mutatedzombie.png'),(50,50))
mutatedzombieRect=pg.Rect(mutatedzombiex,mutatedzombiey,50,50)
image6=mutatedzombie


zombie1frozen=False
zombie2frozen=False
zombie3frozen=False
zombie4frozen=False
zombie5frozen=False
mutatedzombiefrozen=False

shopItemsGuns=['Revolver','Skorpion','Shotgun','Uzi','Thompson','P90','AK47','M4A1','SPAS12','Scar','MP5','Corona16','TNT Yeeter','Nuke Yeeter','Flamethrower',"Maui's Fish Hook",'Raygun','Plasma Cannon','Neutron Beam']

shopItemIndex=0

protection=5
zombie7frozen=False

paused=False
mouserectpos2=(0,0)
rectMouse=pg.Rect((mouserectpos2),(10,10))
unpauseButton=pg.draw.rect(gameDisplay,(0,0,0),Rect(80022/2+25,0,80,20))
buttonImg=pg.transform.scale(pg.image.load('data/images/button.png'),(100,50))
i=-1
invTimer=0
infTimer=0
bloods=[]
s=0
thornTimer=0
speedTimer=0
movingForward=False
movingBack=False
movingLeft=False
movingRight=False
bullet2y=109
itemIndex=0

item=inventory[itemIndex]

FORWARDS='assssasdawsdasd'
BACKWARDS='efds'
LEFT='srdgsdfg'
RIGHT='dfgdgfgdg'

playerFacing=FORWARDS

mutatedzombieImg=image6
cursor=pg.image.load('data/images/pointer.png')
playerSpeed=5

guns=False
armor=True
gunsButton=pg.Rect(100,150,100,50)
armorButton=pg.Rect(400,150,100,50)

gunshot=1
zap=1
reload=1
explosion=11
hurt=1111111111
whoosh=1

pistolimg=pg.transform.scale(pg.image.load('data/images/weapons/pistol.png'),(200,90))
revolverimg=pg.transform.scale(pg.image.load('data/images/weapons/revolver.png'),(200,90))
uziimg=pg.transform.scale(pg.image.load('data/images/weapons/uzi.png'),(200,160))
thompsonimg=pg.transform.scale(pg.image.load('data/images/weapons/thompson.png'),(200,90))
ak47img=pg.transform.scale(pg.image.load('data/images/weapons/ak47.png'),(200,90))
M4A1img=pg.transform.scale(pg.image.load('data/images/weapons/m16.png'),(200,90))
skorpionimg=pg.transform.scale(pg.image.load('data/images/weapons/skorpion.png'),(200,90))
scarimg=pg.transform.scale(pg.image.load('data/images/weapons/scar.png'),(200,90))
coronaimg=pg.transform.scale(pg.image.load('data/images/weapons/corona.png'),(200,90))
tntimg=pg.transform.scale(pg.image.load('data/images/weapons/tnt.png'),(200,90))
nukeimg=pg.transform.scale(pg.image.load('data/images/weapons/nuke.png'),(200,90))
hookimg=pg.transform.scale(pg.image.load('data/images/weapons/fishhook.png'),(200,229))
rayimg=pg.transform.scale(pg.image.load('data/images/weapons/raygun.png'),(200,90))
plasmaimg=pg.transform.scale(pg.image.load('data/images/weapons/plasma.png'),(200,90))
neutronimg=pg.transform.scale(pg.image.load('data/images/weapons/neutronbeam.png'),(200,90))
shotgunimg=pg.transform.scale(pg.image.load('data/images/weapons/shotgun.png'),(200,90))
flameimg=pg.transform.scale(pg.image.load('data/images/weapons/flamethrower.png'),(200,90))
p90img=pg.transform.scale(pg.image.load('data/images/weapons/p90.png'),(200,90))
spasimg=pg.transform.scale(pg.image.load('data/images/weapons/spas.png'),(200,90))
mp5img=pg.transform.scale(pg.image.load('data/images/weapons/mp5.png'),(200,90))
p90=False
mp5=False
uzi=False
tommy=False
ak47=False
M4A1=False
scar=False

try:
    if arsenal[0]=='vagina':
        pass
except:
    arsenal.append('Pistol')

magsize=10
armagsize=30
revsize=6

hotbar=pg.image.load('data/images/ui/hotbar.png')
aaa=0

armorList=['Toilet Paper Suit','Chainmail Armor','Steel Armor','Diamond Armor','Hafnium Armor']

armorDescriptions=['Good for wiping your a**hole, but not much else.','Offers some protection from hordes of zombies.','It can deflect arrows, swords, and zombie bites.','this is an original idea, not from minecraft','Crafted with a rare material found in the cores of exoplanets.']

gun1=pg.mixer.Sound('data/sounds/gun1.wav')
gun2=pg.mixer.Sound('data/sounds/gun2.wav')
pickup=pg.mixer.Sound('data/sounds/pickup.wav')
z1=pg.mixer.Sound('data/sounds/zombie1.wav')
z2=pg.mixer.Sound('data/sounds/zombie2.wav')
z3=pg.mixer.Sound('data/sounds/zombie3.wav')
reload=pg.mixer.Sound('data/sounds/reload.wav')
reload2=pg.mixer.Sound('data/sounds/reload2.wav')
reload3=pg.mixer.Sound('data/sounds/reload3.wav')
gun3=pg.mixer.Sound('data/sounds/gun3.wav')
gun4=pg.mixer.Sound('data/sounds/gun4.wav')
gun5=pg.mixer.Sound('data/sounds/gun5.wav')
yeet=pg.mixer.Sound('data/sounds/yeet.wav')
a1=pg.mixer.Sound('data/sounds/ambient1.wav')
a2=pg.mixer.Sound('data/sounds/ambient2.wav')
explosion=pg.mixer.Sound('data/sounds/explode.wav')
click=pg.mixer.Sound('data/sounds/click.wav')
flameSound=pg.mixer.Sound('data/sounds/flame.wav')

zombie1Infected=False
zombie2Infected=False
zombie3Infected=False
zombie4Infected=False
zombie5Infected=False
zombie6Infected=False

pg.mixer.music.load('data/sounds/music.mp3')
pg.mixer.music.play(-1)
yeetsize=1
def gamequit():
    a=0
    scoreWriter.truncate(0)
    scoreWriter.seek(0)
    scoreWriter.write(str(score))
    scoreWriter.close()
    
    rebWriter.seek(0)
    rebWriter.truncate(0)
    rebWriter.write(str(rebirths))
    rebWriter.close()
    
    invWriter.seek(0)
    invWriter.truncate(0)
    while a<len(inventory):
        invWriter.write(inventory[a]+'\n')
        a+=1
    invWriter.close()
    a=0
    
    armorWriter.seek(0)
    armorWriter.truncate(0)
    while a<len(yourarmor):
        armorWriter.write(yourarmor[a]+'\n')
        a+=1
    armorWriter.close()
    arsenalWriter.seek(0)
    arsenalWriter.truncate(0)
    a=0
    
    while a<len(arsenal):
        if arsenal[a]!='Pistol':
            arsenalWriter.write(arsenal[a]+'\n')
        a+=1
    arsenalWriter.close()
    pg.quit()

wind1=pg.mixer.Sound('data/sounds/wind1.wav')
wind2=pg.mixer.Sound('data/sounds/wind2.wav')
wind3=pg.mixer.Sound('data/sounds/breath.wav')

toiletpaper=pg.transform.scale(pg.image.load('data/images/armor/toiletpaper.png'),(300,180))
chain=pg.transform.scale(pg.image.load('data/images/armor/chain.png'),(300,180))
steel=pg.transform.scale(pg.image.load('data/images/armor/steel.png'),(300,180))
diamond=pg.transform.scale(pg.image.load('data/images/armor/diamond.png'),(300,180))
hafnium=pg.transform.scale(pg.image.load('data/images/armor/hafnium.png'),(300,180))

stamina_icon=pg.image.load('data/images/ui/stamina.png')
bullet_icon=pg.image.load('data/images/ui/ammo.png')
bars=pg.image.load('data/images/ui/bars.png')
sprinting=False
stamina=100
flame=pg.image.load('data/images/flame.png')
v1=pg.transform.scale(pg.image.load('data/images/ui/1.png'),(800,800))
v2=pg.transform.scale(pg.image.load('data/images/ui/2.png'),(800,800))
v3=pg.transform.scale(pg.image.load('data/images/ui/3.png'),(800,800))
v4=pg.transform.scale(pg.image.load('data/images/ui/4.png'),(800,800))
v5=pg.transform.scale(pg.image.load('data/images/ui/5.png'),(800,800))
v0=pg.transform.scale(pg.image.load('data/images/ui/0.png'),(800,800))
vignette=v0

buttonImg2=pg.image.load('data/images/button2.png')

asdf=True



equippedarmor='a'
skull=pg.transform.scale(pg.image.load('data/images/ui/skull.png'),(30,30))
battery=100
batteries=10

spas12=False

def shop():
    shop2=True
    global mouserectpos,scoreSaver,shopItems,shopItemIndex,inventory,score,guns,armor,a,equippedarmor,asdf
    while shop2:
        gameDisplay.fill((57,90,0))
        pg.draw.rect(gameDisplay,(20,60,0),Rect(50,425,700,350))
        for event in pg.event.get():
            if event.type==KEYDOWN:
                if event.key==K_RETURN:
                    if guns:
                        if shopItemsGuns[shopItemIndex]=='Revolver' and 'Revolver' not in inventory:
                            if score>=150 and 'Revolver' not in inventory:
                                inventory.append('Revolver')
                                score-=150
                        if shopItemsGuns[shopItemIndex]=='Skorpion' and 'Skorpion' not in inventory:
                            if score>=200 and 'Skorpion' not in inventory:
                                inventory.append('Skorpion')
                                score-=200
                        if shopItemsGuns[shopItemIndex]=='Shotgun' and 'Shotgun' not in inventory:
                            if score>=300 and 'Shotgun' not in inventory:
                                inventory.append('Shotgun')
                                score-=300
                        if shopItemsGuns[shopItemIndex]=='Uzi' and 'Uzi' not in inventory:
                            if score>=250:
                                inventory.append('Uzi')
                                score-=250
                        if shopItemsGuns[shopItemIndex]=='P90' and 'P90' not in inventory:
                            if score>=500:
                                inventory.append('P90')
                                score-=500
                        if shopItemsGuns[shopItemIndex]=='Thompson' and 'Thompson' not in inventory:
                            if score>=400:
                                inventory.append('Thompson')
                                score-=400
                        if shopItemsGuns[shopItemIndex]=='AK47' and 'AK47' not in inventory:
                            if score>=500:
                                inventory.append('AK47')
                                score-=500
                        if shopItemsGuns[shopItemIndex]=='M4A1' and 'M4A1' not in inventory:
                            if score>=600:
                                inventory.append('M4A1')
                                score-=600
                        if shopItemsGuns[shopItemIndex]=='SPAS12' and 'SPAS12' not in inventory:
                            if score>=700:
                                inventory.append('SPAS12')
                                score-=700
                        if shopItemsGuns[shopItemIndex]=='Scar' and 'Scar' not in inventory:
                            if score>=800:
                                inventory.append('Scar')
                                score-=800
                        if shopItemsGuns[shopItemIndex]=='MP5' and 'MP5' not in inventory:
                            if score>=900:
                                inventory.append('MP5')
                                score-=900
                        if shopItemsGuns[shopItemIndex]=='Corona16' and 'Corona16' not in inventory:
                            if score>=1000:
                                inventory.append('Corona16')
                                score-=1000
                        if shopItemsGuns[shopItemIndex]=='TNT Yeeter' and 'TNT Yeeter' not in inventory:
                            if score>=1300:
                                inventory.append('TNT Yeeter')
                                score-=1300
                        if shopItemsGuns[shopItemIndex]=='Nuke Yeeter' and 'Nuke Yeeter' not in inventory:
                            if score>=1500:
                                inventory.append('Nuke Yeeter')
                                score-=1500
                        if shopItemsGuns[shopItemIndex]=='Flamethrower' and 'Flamethrower' not in inventory:
                            if score>=1600:
                                inventory.append('Flamethrower')
                                score-=1600
                        if shopItemsGuns[shopItemIndex]=="Maui's Fish Hook" and "Maui's Fish Hook" not in inventory:
                            if score>=1700:
                                inventory.append("Maui's Fish Hook")
                                score-=1700
                    if armor:
                        if armorList[shopItemIndex]=='Toilet Paper Suit' and 'Toilet Paper Suit' not in yourarmor:
                            if score>=100 and 'Toilet Paper Suit' not in yourarmor:
                                yourarmor.append('Toilet Paper Suit')
                                score-=100
                        if armorList[shopItemIndex]=='Chainmail Armor' and 'Chainmail Armor' not in yourarmor:
                            if score>=200 and 'Chainmail Armor' not in yourarmor:
                                yourarmor.append('Chainmail Armor')
                                score-=200
                        if armorList[shopItemIndex]=='Steel Armor' and 'Steel Armor' not in yourarmor:
                            if score>=300 and 'Steel Armor' not in yourarmor:
                                yourarmor.append('Steel Armor')
                                score-=300
                        if armorList[shopItemIndex]=='Diamond Armor' and 'Diamond Armor' not in yourarmor:
                            if score>=450 and 'Diamond Armor' not in yourarmor:
                                yourarmor.append('Diamond Armor')
                                score-=450
                        if armorList[shopItemIndex]=='Hafnium Armor' and 'Hafnium Armor' not in yourarmor:
                            if score>=550 and 'Hafnium Armor' not in yourarmor:
                                yourarmor.append('Hafnium Armor')
                                score-=550
            if event.type==MOUSEMOTION:
                mouserectpos=event.pos
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if mouserect.colliderect(backButton):
                        shop2=False
                        print('Event Detected: event.Event.Back')
                    if mouserect.colliderect(gunsButton):
                        shopItemIndex=0
                        guns=True
                        armor=False
                        print('Event Detected: event.Event.GunsButtonPress')
                    if mouserect.colliderect(armorButton):
                        shopItemIndex=0
                        guns=False
                        armor=True
                        print('Event Detected: event.Event.ArmorButtonPress')
                    if mouserect.colliderect(equipButton):
                        if len(arsenal)<3 and shopItemsGuns[shopItemIndex] in inventory and shopItemsGuns[shopItemIndex] not in arsenal and guns:
                            arsenal.append(shopItemsGuns[shopItemIndex])
                            print('Event Detected: event.Event.Equip')
                            asdf=False
                            
                        if shopItemsGuns[shopItemIndex] in arsenal and asdf and guns:
                            arsenal.remove(shopItemsGuns[shopItemIndex])
                            print('Event Detected: event.Event.UnEquip')
                            
                        if armor and armorList[shopItemIndex] in yourarmor:
                            equippedarmor=armorList[shopItemIndex]
                            print('Event Detected: event.Event.ArmorEquip')
                        asdf=True
                if event.button==4:
                    if not shopItemIndex==0:
                        shopItemIndex-=1
                if event.button==5:
                    if guns and not shopItemIndex==len(shopItemsGuns)-1:
                        shopItemIndex+=1
                    if armor and not shopItemIndex==len(armorList)-1:
                        shopItemIndex+=1
            if event.type==QUIT:
                gamequit()
        mouserect=pg.Rect((mouserectpos),(50,50))
        backButton=pg.Rect((10,10),(100,50))
        armorButton=pg.Rect((450,10),(100,50))
        gunsButton=pg.Rect((300,10),(100,50))
        equipButton=pg.Rect((390,340),(100,50))
        if mouserect.colliderect(backButton):
            gameDisplay.blit(buttonImg2,(10,10))
        else:
            gameDisplay.blit(buttonImg,(10,10))
            
        if mouserect.colliderect(armorButton):
            gameDisplay.blit(buttonImg2,(450,10))
        else:
            gameDisplay.blit(buttonImg,(450,10))
            
        if mouserect.colliderect(gunsButton):
            gameDisplay.blit(buttonImg2,(300,10))
        else:
            gameDisplay.blit(buttonImg,(300,10))
            
        if mouserect.colliderect(equipButton):
            gameDisplay.blit(buttonImg2,(390,340))
        else:
            gameDisplay.blit(buttonImg,(390,340))
        gameDisplay.blit(BIGFONT.render('Back',False,black),(20,20))
        gameDisplay.blit(BIGFONT.render('Guns',False,black),(310,20))
        if shopItemsGuns[shopItemIndex] in arsenal:
            equip=kindaBigFont.render('Unequip',False,black)
            
        else:
            equip=BIGFONT.render('Equip',False,black)
        try:
            if armorList[shopItemIndex]==equippedarmor:
                equip=kindaBigFont.render('Equipped',False,red)
            elif armor:
                equip=BIGFONT.render('Equip',False,black)
        except IndexError:
            pass
        gameDisplay.blit(equip,(400,350))
        gameDisplay.blit(BIGFONT.render('Armor',False,black),(460,20))
        gameDisplay.blit(BIGFONT.render('Use the scroll wheel to cycle through the items.',False,yellow),(10,80))
        gameDisplay.blit(BIGFONT.render('Use ENTER to buy.',False,yellow),(10,120))
        if 3-len(arsenal)==1:
            gameDisplay.blit(BIGFONT.render('You can equip 1 more weapon.',False,yellow),(10,160))
        else:
            gameDisplay.blit(BIGFONT.render('You can equip '+str(3-len(arsenal))+' more weapons.',False,yellow),(10,160)) # You don't want it to say 1 more weapons
        gameDisplay.blit(skull,(570,10))
        gameDisplay.blit(BIGFONT.render(':'+str(score),False,yellow),(600,20))
        if guns:
            gameDisplay.blit(kindaBigFont.render(shopItemsGuns[shopItemIndex],False,white),(30,300))
            gameDisplay.blit(font.render(descriptions[shopItemIndex],False,white),(400-font.render(descriptions[shopItemIndex],False,white).get_width()/2,640))
            if shopItemsGuns[shopItemIndex]=='Pistol':
                gameDisplay.blit(pistolimg,(300,450))
                if 'Pistol' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Revolver':
                gameDisplay.blit(BIGFONT.render('Price:150',False,white),(30,350))
                gameDisplay.blit(revolverimg,(300,450))
                if 'Revolver' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Skorpion':
                gameDisplay.blit(BIGFONT.render('Price:200',False,white),(30,350))
                gameDisplay.blit(skorpionimg,(300,450))
                if 'Skorpion' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Shotgun':
                gameDisplay.blit(BIGFONT.render('Price:300',False,white),(30,350))
                gameDisplay.blit(shotgunimg,(300,450))
                if 'Shotgun' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Uzi':
                gameDisplay.blit(BIGFONT.render('Price:250',False,white),(30,350))
                gameDisplay.blit(uziimg,(250,400))
                if 'Uzi' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))          
            if shopItemsGuns[shopItemIndex]=='Thompson':
                gameDisplay.blit(BIGFONT.render('Price:350',False,white),(30,350))
                gameDisplay.blit(thompsonimg,(300,450))
                if 'Thompson' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))

            if shopItemsGuns[shopItemIndex]=='P90':
                gameDisplay.blit(BIGFONT.render('Price:400',False,white),(30,350))
                gameDisplay.blit(p90img,(300,450))
                if 'P90' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='AK47':
                gameDisplay.blit(ak47img,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:500',False,white),(30,350))
                if 'AK47' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='M4A1':
                gameDisplay.blit(M4A1img,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:600',False,white),(30,350))
                if 'M4A1' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='SPAS12':
                gameDisplay.blit(spasimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:700',False,white),(30,350))
                if 'SPAS12' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Scar':
                gameDisplay.blit(scarimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:800',False,white),(30,350))
                if 'Scar' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='MP5':
                gameDisplay.blit(mp5img,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:900',False,white),(30,350))
                if 'MP5' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Corona16':
                gameDisplay.blit(coronaimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:1000',False,white),(30,350))
                if 'Corona16' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='TNT Yeeter':
                gameDisplay.blit(tntimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:1300',False,white),(30,350))
                if 'TNT Yeeter' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Nuke Yeeter':
                gameDisplay.blit(nukeimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:1500',False,white),(30,350))
                if 'Nuke Yeeter' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=='Flamethrower':
                gameDisplay.blit(flameimg,(300,450))
                gameDisplay.blit(BIGFONT.render('Price:1600',False,white),(30,350))
                if 'Flamethrower' in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=="Maui's Fish Hook":
                gameDisplay.blit(hookimg,(300,405))
                gameDisplay.blit(BIGFONT.render('Price:1700',False,white),(30,350))
                if "Maui's Fish Hook" in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=="Raygun":
                gameDisplay.blit(rayimg,(300,450))
                gameDisplay.blit(kindaBigFont.render('Unlock this weapon with the purchace of a Crate!',False,white),(30,350))
                if "Raygun" in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=="Plasma Cannon":
                gameDisplay.blit(plasmaimg,(300,450))
                gameDisplay.blit(kindaBigFont.render('Unlock this weapon with the purchace of a Crate!',False,white),(30,350))
                if "Plasma Cannon" in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if shopItemsGuns[shopItemIndex]=="Neutron Beam":
                gameDisplay.blit(neutronimg,(300,450))
                gameDisplay.blit(kindaBigFont.render('Unlock this weapon with the purchace of a Crate!',False,white),(30,350))
                if "Neutron Beam" in inventory:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
        if armor:
            gameDisplay.blit(kindaBigFont.render(armorList[shopItemIndex],False,white),(30,300))
            gameDisplay.blit(font.render(armorDescriptions[shopItemIndex],False,white),(400-font.render(armorDescriptions[shopItemIndex],False,white).get_width()/2,640))
            if armorList[shopItemIndex]=='Toilet Paper Suit':
                gameDisplay.blit(BIGFONT.render('Price:100',False,white),(30,350))
                gameDisplay.blit(toiletpaper,(300,450))
                if 'Toilet Paper Suit' in yourarmor:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if armorList[shopItemIndex]=='Chainmail Armor':
                gameDisplay.blit(BIGFONT.render('Price:200',False,white),(30,350))
                gameDisplay.blit(chain,(300,450))
                if 'Chainmail Armor' in yourarmor:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if armorList[shopItemIndex]=='Steel Armor':
                gameDisplay.blit(BIGFONT.render('Price:300',False,white),(30,350))
                gameDisplay.blit(steel,(300,450))
                if 'Steel Armor' in yourarmor:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
            if armorList[shopItemIndex]=='Diamond Armor':
                gameDisplay.blit(BIGFONT.render('Price:450',False,white),(30,350))
                gameDisplay.blit(diamond,(300,450))
                if 'Diamond Armor' in yourarmor:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))          
            if armorList[shopItemIndex]=='Hafnium Armor':
                gameDisplay.blit(BIGFONT.render('Price:550',False,white),(30,350))
                gameDisplay.blit(hafnium,(300,450))
                if 'Hafnium Armor' in yourarmor:
                    gameDisplay.blit(font.render('You already own this item',True,red),(30,400))
        gameDisplay.blit(cursor,(mouserectpos))
        pg.display.update()

hook=False
howtoplayOn=False
font2=pg.font.Font('data/other/font.ttf',30)
deathtexts=['You exploded!','You got zombied!','You held your poop for too long!','Your heart stopped!',"You got terminal cancer!",'You lost too much blood!','You lost too much semen!','You tried to escape North Korea and got landmined!','You got executed!']
porn=0
rebirth_price=500*rebirths




laser1=pg.image.load('data/images/laser1.png')
laser2=pg.image.load('data/images/laser2.png')
laser3=pg.image.load('data/images/laser3.png')
crateImg=pg.transform.scale(pg.image.load('data/images/weaponcrate.png'),(200,200))
def howtoplay():
    global mouserectpos,scoreSaver,shopItems,shopItemIndex,inventory,score,guns,armor,a,howtoplayOn,yourarmor
    while howtoplayOn:
        gameDisplay.fill((57,90,0))
        for event in pg.event.get():
            if event.type==MOUSEMOTION:
                mouserectpos=event.pos
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if mouserect.colliderect(backButton):
                        howtoplayOn=False
            if event.type==QUIT:
                gamequit()
        mouserect=pg.Rect((mouserectpos),(50,50))
        backButton=pg.Rect((10,10),(100,50))
        if mouserect.colliderect(backButton):
            gameDisplay.blit(buttonImg2,(10,10))
        else:
            gameDisplay.blit(buttonImg,(10,10))
        gameDisplay.blit(BIGFONT.render('Back',False,black),(20,20))
        
        gameDisplay.blit(font.render('You can get money by killing zombies. use the money to buy new stuff.',False,yellow),(30,500))
        gameDisplay.blit(font.render('If you run out of ammo, pick up supply crates to replenish your ammo.',False,yellow),(30,300))
        gameDisplay.blit(font.render('Use the wAsD keys to move around. Use the space key to shoot.',False,yellow),(30,100))
        gameDisplay.blit(font.render('In the top right corner, there is a health bar.',False,yellow),(30,200))
        gameDisplay.blit(font.render('Use the arrow keys to switch weapons.',False,yellow),(30,400))
        gameDisplay.blit(cursor,(mouserectpos))
        pg.display.update()

def rebirth():
    global mouserectpos,scoreSaver,shopItems,shopItemIndex,inventory,score,guns,armor,a,howtoplayOn, rebirths,yourarmor
    print('Event Detected: event.Event.Rebit=rth')
    while howtoplayOn:
        gameDisplay.fill((57,90,0))
        for event in pg.event.get():
            if event.type==MOUSEMOTION:
                mouserectpos=event.pos
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if mouserect.colliderect(backButton):
                        howtoplayOn=False
                        print('Event Detected: event.Event.Back')
                    if mouserect.colliderect(rebirthButton):
                        if score>=rebirth_price:
                            rebirths+=1
                            score=0
                            inventory=['Pistol']
                            arsenal=['Pistol']
                            yourarmor=[]
            if event.type==QUIT:
                gamequit()
        mouserect=pg.Rect((mouserectpos),(50,50))
        backButton=pg.Rect((10,10),(100,50))
        rebirthButton=pg.Rect((350,375),(100,50))
        if mouserect.colliderect(backButton):
            gameDisplay.blit(buttonImg2,(10,10))
        else:
            gameDisplay.blit(buttonImg,(10,10))
        gameDisplay.blit(BIGFONT.render('Back',False,black),(20,20))
        
        gameDisplay.blit(font.render('You can sacrifice all your money and weapons to rebirth.',False,yellow),(130,50))
        gameDisplay.blit(font.render('Kills will be worth more when you rebirth.',False,yellow),(130,80))
        gameDisplay.blit(font.render('You need '+str(rebirth_price)+' skulls to rebirth.',False,yellow),(130,110))
        gameDisplay.blit(font.render('You have '+ str(rebirths-1)+' Rebirths',False,yellow),(30,650))
        gameDisplay.blit(skull,(570,10))
        gameDisplay.blit(BIGFONT.render(':'+str(score),False,yellow),(600,20))
        gameDisplay.blit(buttonImg,(350,375))
        gameDisplay.blit(cursor,(mouserectpos))
        pg.display.update()

def crateshop():
    global mouserectpos,scoreSaver,shopItems,shopItemIndex,inventory,score,guns,armor,a,howtoplayOn, rebirths,yourarmor
    print('Event Detected: event.Event.Crates')
    while howtoplayOn:
        gameDisplay.fill((57,90,0))
        for event in pg.event.get():
            if event.type==MOUSEMOTION:
                mouserectpos=event.pos
            if event.type==MOUSEBUTTONDOWN:
                if event.button==1:
                    if mouserect.colliderect(backButton):
                        howtoplayOn=False
                        print('Event Detected: event.Event.Back')
                    if mouserect.colliderect(rebirthButton):
                        if score>=1000:
                            p=random.randint(0,5)
                            gameDisplay.fill((0,70,20))
                            gameDisplay.blit(BIGFONT.render('Congratulations!',False,yellow),(400-BIGFONT.render('Congratulations!',False,yellow).get_width()/2,60))
                            gameDisplay.blit(crateImg,(300,300))
                            gameDisplay.blit(kindaBigFont.render('You bought a Weapon Crate!',False,yellow),(400-kindaBigFont.render('You bought a Weapon Crate!',False,yellow).get_width()/2,100))
                            if p==0:
                                gameDisplay.blit(kindaBigFont.render('You unlocked Raygun as a reward!',False,yellow),(400-kindaBigFont.render('You unlocked DogPoop as a reward!',False,yellow).get_width()/2,550))
                                inventory.append('Raygun')
                            elif p==1:
                                gameDisplay.blit(kindaBigFont.render('You unlocked Plasma Cannon as a reward!',False,yellow),(400-kindaBigFont.render('You unlocked DogPoop as a reward!',False,yellow).get_width()/2,550))
                                inventory.append('Plasma Cannon')
                            elif p==2:
                                gameDisplay.blit(kindaBigFont.render('You unlocked Neutron Beam as a reward!',False,yellow),(400-kindaBigFont.render('You unlocked DogPoop as a reward!',False,yellow).get_width()/2,550))
                                inventory.append('Neutron Beam')
                            else:
                                p=random.randint(500,1000)
                                gameDisplay.blit(kindaBigFont.render('You got '+str(p)+' Skulls as a reward!',False,yellow),(400-kindaBigFont.render('You unlocked DogPoop as a reward!',False,yellow).get_width()/2,550))
                                score+=p
                            score-=1000
                            rebirthButton=pg.Rect((37750,99475),(100,50))
                            pg.display.update()
                            time.sleep(5)
                            
                                
            if event.type==QUIT:
                gamequit()
        mouserect=pg.Rect((mouserectpos),(50,50))
        backButton=pg.Rect((10,10),(100,50))
        rebirthButton=pg.Rect((350,375),(100,50))
        if mouserect.colliderect(backButton):
            gameDisplay.blit(buttonImg2,(10,10))
        else:
            gameDisplay.blit(buttonImg,(10,10))
        gameDisplay.blit(BIGFONT.render('Back',False,black),(20,20))
        
        
        gameDisplay.blit(font.render('You can buy a Weapon crate to unlock exclusive weapons!',False,yellow),(130,60))
        gameDisplay.blit(font.render('One single crate costs 1000 skulls.',False,yellow),(130,80))
        gameDisplay.blit(skull,(570,10))
        gameDisplay.blit(BIGFONT.render(':'+str(score),False,yellow),(600,20))
        if mouserect.colliderect(rebirthButton):
            gameDisplay.blit(buttonImg2,(350,375))
        else:
            gameDisplay.blit(buttonImg,(350,375))
        gameDisplay.blit(kindaBigFont.render('Buy',False,black),(400-kindaBigFont.render('Buy',False,black).get_width()/2,385))
        gameDisplay.blit(kindaBigFont.render('Crate',False,black),(400-kindaBigFont.render('Crate',False,black).get_width()/2,400))
        gameDisplay.blit(cursor,(mouserectpos))
        pg.display.update()

while True:
    while not game:
        
        gameDisplay.fill((57,80,0))
        gameDisplay.blit(mainmenuimg,(0,0))
        for event in pg.event.get():
            if event.type==QUIT:
                gamequit()
            if event.type==MOUSEMOTION:
                mouserectpos=event.pos
            if event.type==pg.MOUSEBUTTONDOWN:
                if button.colliderect(mouserect):
                    gameArcade=True
                    game=True
                    print('Event Detected: event.Event.PlayButtonPress')
                    click.play()
                if button2.colliderect(mouserect):
                    print('Event Detected: event.Event.ShopButtonPress')
                    click.play()
                    shop()
                    click.play()
                if button3.colliderect(mouserect):
                    print('Event Detected: event.Event.HowToPlay')
                    click.play()
                    howtoplayOn=True
                    howtoplay()
                    click.play()
                if button4.colliderect(mouserect):
                    print('Event Detected: event.Event.Rebirth')
                    click.play()
                    howtoplayOn=True
                    rebirth()
                    click.play()
                if button5.colliderect(mouserect):
                    print('Event Detected: event.Event.CrateShop')
                    click.play()
                    howtoplayOn=True
                    crateshop()
                    click.play()
                    
        mouserect=pg.Rect((mouserectpos),(5,5))
        button=pg.Rect(800/2-50,500/2,100,50)
        button2=pg.Rect(800/2-50,500/2+100,100,50)
        button3=pg.Rect(800/2-50,500/2+200,100,50)
        button4=pg.Rect(800/2-50,500/2+300,100,50)
        button5=pg.Rect(800/2-50,500/2+400,100,50)
        if mouserect.colliderect(button):
            gameDisplay.blit(buttonImg2,(800/2-50,500/2))
        else:
            gameDisplay.blit(buttonImg,(800/2-50,500/2))
        if mouserect.colliderect(button2):
            gameDisplay.blit(buttonImg2,(800/2-50,500/2+100))
        else:
            gameDisplay.blit(buttonImg,(800/2-50,500/2+100))
        if mouserect.colliderect(button3):
            gameDisplay.blit(buttonImg2,(800/2-50,500/2+200))
        else:
            gameDisplay.blit(buttonImg,(800/2-50,500/2+200))
        if mouserect.colliderect(button4):
            gameDisplay.blit(buttonImg2,(800/2-50,500/2+300))
        else:
            gameDisplay.blit(buttonImg,(800/2-50,500/2+300))
        if mouserect.colliderect(button5):
            gameDisplay.blit(buttonImg2,(800/2-50,500/2+400))
        else:
            gameDisplay.blit(buttonImg,(800/2-50,500/2+400))
        gameDisplay.blit(BIGFONT.render('Play',False,black),(400-BIGFONT.render('Play',False,black).get_width()/2,540/2-6))
        gameDisplay.blit(BIGFONT.render('Shop',False,black),(400-BIGFONT.render('Shop',False,black).get_width()/2,540/2+-6+100))
        gameDisplay.blit(BIGFONT.render('How to play',False,black),(800/2-40,540/2-6+200))
        gameDisplay.blit(kindaBigFont.render('Rebirth',False,black),(400-kindaBigFont.render('Rebirth',False,black).get_width()/2,540/2-6+300))
        gameDisplay.blit(cursor,(mouserectpos))
        clock.tick(FPS)
        pg.display.update()

    def death(message):
        scoreWriter.seek(0)
        dead=True
        invWriter.seek(0)
        a=0
        mouserectpos=(0,0)
        deathtext=deathtexts[random.randint(0,8)]
        while dead:
            print(a)
            gameDisplay.fill(red)
            text=BIGFONT.render(deathtext,False,black)
            gameDisplay.blit(text,(50,300))
            mouserect=pg.Rect((mouserectpos),(50,50))
            for event in pg.event.get():
                if event.type==QUIT:
                    gamequit()
                    
                if event.type==MOUSEMOTION:
                    mouserectpos=event.pos
                if event.type==pg.MOUSEBUTTONDOWN:
                    if button.colliderect(mouserect):
                        a=0
                        scoreWriter.truncate(0)
                        scoreWriter.seek(0)
                        scoreWriter.write(str(score))
                        scoreWriter.close()
                        rebWriter.seek(0)
                        rebWriter.truncate(0)
                        rebWriter.write(str(rebirths))
                        rebWriter.close()
                        invWriter.seek(0)
                        invWriter.truncate(0)
                        while a<len(inventory):
                            invWriter.write(inventory[a]+'\n')
                            a+=1
                        invWriter.close()
                        a=0
                        armorWriter.seek(0)
                        armorWriter.truncate(0)
                        while a<len(yourarmor):
                            armorWriter.write(yourarmor[a]+'\n')
                            a+=1
                        armorWriter.close()
                        pg.quit()
            gameDisplay.blit(cursor,(mouserectpos))
            button=pg.Rect(800/2-50,400,100,50)
            gameDisplay.blit(buttonImg,(800/2-50,400))
            pg.display.update()
        invTimer=5000
        
    class bullet:
        travelling=20
        x=-1000
        y=1000
        fromShooterZombie=False
        infect=False
        rect=pg.Rect(x,y,10,30)
        img=pg.image.load('data/images/bullet.png')
        facing=FORWARDS
        sideways=0
        age=0
        
    bulletsList=[bullet]
    imgg=pg.image.load('data/images/blood.png')
    bulletimg=pg.image.load('data/images/bullet.png')
    pistolCoolDown=50
    rifleCoolDown=8
    blasterCoolDown=7
    lightningRodCoolDown=8
    flamethrowerCoolDown=7
    sniperCoolDown=8
    blasterPenCoolDown=20
    orbofundyingCoolDown=1000

    pg.display.update()
    pg.mixer.music.stop()
    
    while game:# main game loop,arcade
        
        
        
            
        class blood:
            img=imgg
            x =-1000
            y=1000
            
        class bullet:
            x=-1000
            y=1000
            travelling=20
            rect=pg.Rect(x,y,18,23)
            facing=FORWARDS
            fromShooterZombie=False
            explode=False
            penetrate=False
            age=0
            sideways=0
            img=pg.image.load('data/images/bullet.png')
            infect=False
            
        rect=pg.Rect(x,y,96,64)
        
        if random.randint(0,75)==10 and health<9.3 and stamina>99:
            health=health+1
        elif random.randint(0,75)==10 and health<10:
            health+=0.1
        pg.display.set_caption('Rising Apocalypse '+__version__)
        for event in pg.event.get():
            if event.type==pg.KEYDOWN:
                if event.key==K_F1:
                    fpsViewer=True
                if event.key==K_ESCAPE and not paused:
                    paused=True
                    gameDisplay.blit(pausemenu,(0,0))
                    break
                if event.key==K_ESCAPE and paused:
                    paused=False
                    gameDisplay.blit(pausemenu,(1110,1110))
                if event.key==K_a:
                    movingLeft=True
                elif event.key==K_d:
                    movingRight=True
                if event.key==K_w:
                    movingForward=True
                elif event.key==K_s:
                    movingBack=True
                elif event.key==K_LSHIFT and stamina>1:
                    sprinting=True
                elif event.key==K_SPACE:
                    if item=='Pistol' and pistolCoolDown==50 and magsize>0:
                        gun3.play()
                        gunStrength=2
                        magsize-=1
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        bulletsList[-1].sideways=random.randint(-1,1)
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                    if item=='Raygun' and pistolCoolDown==50 and battery>0:
                        if battery>10:
                            battery-=random.randint(1,10)
                        else:
                            battery=0
                        gun4.play()
                        gunStrength=5
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                        bulletsList[-1].img=laser1
                    if item=='Plasma Cannon' and pistolCoolDown==50 and battery>0:
                        if battery>10:
                            battery-=random.randint(1,10)
                        else:
                            battery=0
                        gun4.play()
                        gunStrength=7
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                        bulletsList[-1].img=laser2
                    if item=='Neutron Beam' and pistolCoolDown==50 and battery>0:
                        if battery>10:
                            battery-=random.randint(1,10)
                        else:
                            battery=0
                        gun4.play()
                        gunStrength=10
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                        bulletsList[-1].img=laser3
                    if item=='Corona16' and pistolCoolDown==50 and magsize>0:
                        gun2.play()
                        gunStrength=0
                        magsize-=1
                        bulletsList[-1].penetrate=False
                        bulletsList.append(bullet)
                        bulletsList[-1].infect=True
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                    elif item=='Revolver' and pistolCoolDown==50 and revsize>0:
                        gun3.play()
                        gunStrength=3
                        revsize-=1
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].sideways=random.randint(-1,1)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                    elif item=='TNT Yeeter' and pistolCoolDown==50 and yeetsize>0:
                        yeet.play()
                        gunStrength=10
                        yeetsize-=1
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].sideways=random.randint(-1,1)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        bulletsList[-1].img=pg.image.load('data/images/tntProjectile.png')
                        bulletsList[-1].explode=True
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                    elif item=='Nuke Yeeter' and pistolCoolDown==50 and yeetsize>0:
                        yeet.play()
                        gunStrength=999
                        yeetsize-=1
                        bulletsList[-1].penetrate=False
                        bulletsList[-1].fromShooterZombie=False
                        bulletsList.append(bullet)
                        bulletsList[-1].sideways=random.randint(-1,1)
                        bulletsList[-1].x=x
                        bulletsList[-1].y=y-10
                        bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)  #Player image w=70 h=90
                        bulletsList[-1].img=pg.image.load('data/images/nukeProjectile.png')
                        bulletsList[-1].explode=True
                        if playerFacing==FORWARDS:
                            bulletsList[-1].facing=FORWARDS
                            bulletsList[-1].x=x +50
                        if playerFacing==BACKWARDS: 
                            bulletsList[-1].facing=BACKWARDS
                            bulletsList[-1].y=y + 70
                            bulletsList[-1].x=x +5
                        if playerFacing==LEFT:
                            bulletsList[-1].facing=LEFT
                            bulletsList[-1].y=y + 10
                        if playerFacing==RIGHT:
                            bulletsList[-1].y=y + 50
                            bulletsList[-1].x=x +50
                            bulletsList[-1].facing=RIGHT
                        pistolCoolDown=0
                    if item=='Uzi':
                        uzi=True
                    if item=='Flamethrower':
                        flamethrower=True
                    if item=='Shotgun' and revsize>0 and pistolCoolDown==50:
                        gun5.play()
                        shotgun=True
                        pistolCoolDown=0
                        revsize-=1
                        q1=0
                    if item=='SPAS12' and revsize>0 and pistolCoolDown==50:
                        gun5.play()
                        spas12=True
                        pistolCoolDown=0
                        revsize-=1
                        q1=0
                    elif item=='AK47':
                        ak47=True
                    elif item=='Thompson':
                        tommy=True
                    elif item=='P90':
                        p90=True
                    elif item=='M4A1':
                        M4A1=True
                    elif item=='Skorpion':
                        skorpion=True
                    elif item=='Scar':
                        scar=True
                    elif item=="Maui's Fish Hook":
                        hook=True
                    elif item=="MP5":
                        mp5=True
                    else:
                        uzi=False
                        ak47=False
                        tommy=False
                        M4A1=False
                        skorpion=False
                        scar=False
                        mp5=False
                        p90=False
                        hook=False
                
            if event.type==pg.MOUSEMOTION:
                mouserectpos2=event.pos
            if event.type==pg.MOUSEBUTTONDOWN:
                if rectMouse.colliderect(unpauseButton) and paused:
                    paused=False
            if event.type==QUIT:
                gamequit()
            if event.type==pg.KEYUP:

                
                if event.key==K_a:
                    movingLeft=False
                if event.key==K_F1:
                    fpsViewer=False
                elif event.key==K_LSHIFT:
                    sprinting=False
                elif event.key==K_d:
                    movingRight=False
                if event.key==K_w:
                    movingForward=False
                elif event.key==K_s:
                    movingBack=False
                elif event.key==K_LEFT:
                    if itemIndex==0:
                        itemIndex=0
                    else:
                        itemIndex-=1
                elif event.key==K_RIGHT:
                    if itemIndex==len(arsenal)-1:
                        pass
                    else:       #666 lines
                        itemIndex+=1
                if event.key==K_SPACE:
                    if item=='Uzi':
                        uzi=False
                    elif item=='AK47':
                        ak47=False
                    elif item=='Thompson':
                        tommy=False
                    elif item=='P90':
                        p90=False
                    elif item=='M4A1':
                        M4A1=False
                    elif item=='Skorpion':
                        skorpion=False
                    elif item=='Scar':
                        scar=False
                    elif item=="Maui's Fish Hook":
                        hook=False
                    if item=='Flamethrower':
                        flamethrower=False
                    if item=='MP5':
                        mp5=False
                
                    
                
        if paused:
            rectMouse=pg.Rect((mouserectpos2),(10,10))
            unpauseButton=pg.Rect(800/2-50,200,100,50)
            if rectMouse.colliderect(unpauseButton):
                gameDisplay.blit(buttonImg2,(800/2-50,200))
            else:
                gameDisplay.blit(buttonImg,(350,200))
            gameDisplay.blit(BIGFONT.render('UNPAUSE',False,black),(400-BIGFONT.render('UNPAUSE',False,black).get_width()/2,210))
            pg.display.update()
            print('h')
        if not paused:
            image1=pg.transform.scale(zombieImages[zIterator],(80,80))
            image3=pg.transform.rotate(pg.transform.scale(zombieImages[zIterator],(80,80)),180)
            if sprinting and stamina>1:
                playerSpeed=health/1.1
                stamina-=0.5
            else:
                playerSpeed=health/1.7
                
            porn+=1
            
            if random.randint(0,100)==1 and stamina<100 and not sprinting:
                stamina+=5
                
            if random.randint(1,1030)==1:
                z1.play()
                if random.randint(1,7)==1:
                    a1.play()
                if random.randint(1,7)==1:
                    a2.play()
            if random.randint(1,1033)==1:
                z2.play()
                if random.randint(1,7)==1:
                    a1.play()
                if random.randint(1,7)==1:
                    a2.play()
            if random.randint(1,1830)==1:
                z3.play()
                if random.randint(1,7)==1:
                    a1.play()
                if random.randint(1,7)==1:
                    a2.play()
            if random.randint(1,530)==1:
                wind1.play()
            if random.randint(1,5300)==1:
                wind2.play()
            if random.randint(1,530)==1:
                wind3.play()
            if random.randint(1,1500)==1:
                a1.play()
            
            if pistolCoolDown<50:
                pistolCoolDown+=1



            
            pausebuttonx=350
            unpauseButton=pg.draw.rect(gameDisplay,(0,0,0),Rect(pausebuttonx,0,30,30))
            rectMouse=pg.Rect((mouserectpos2),(10,10))
            gameDisplay.fill((255,0,0))
            gameDisplay.blit(backgrounda,(bgX,bgY))
            

            if magsize==0 and bullets>0:
                if aaa==0:
                    reload.play()
                    print('RELOADINg......')
                    aaa=1
                if porn%10==0:
                    aaa+=1
                    if aaa==20 and bullets>9:
                        magsize=10
                        bullets-=10
                        print('reloaded')
                        aaa=0
                    elif aaa==20 and bullets<10:
                        magsize=bullets
                        bullets=0
                        aaa=0
                        print('reloaded')

            if armagsize==0 and bullets>0:
                if aaa==0:
                    reload.play()
                    print('RELOADINg......')
                    aaa=1
                if porn%10==0:
                    aaa+=1
                    if aaa==20 and bullets>29:
                        armagsize=30
                        bullets-=30
                        aaa=0
                        print('reloaded')
                    elif aaa==20 and bullets<30:
                        armagsize=bullets
                        bullets=0
                        aaa=0
                        print('reloaded')
            if revsize==0 and bullets>0:
                if aaa==0:
                    if item=='Shotgun' or item=='SPAS12':
                        reload3.play()
                    else:
                        reload.play()
                    print('RELOADINg......')
                    aaa=1
                if porn%10==0:
                    aaa+=1
                    if aaa==20 and bullets>5:
                        revsize=6
                        bullets-=6
                        aaa=0
                        print('reloaded')
                    elif aaa==20 and bullets<6:
                        revsize=bullets
                        bullets=0
                        aaa=0
                        print('reloaded')
            if yeetsize==0 and bullets>0:
                if aaa==0:
                    print('reloading')
                    aaa=1
                    reload.play()
                if porn%10==0:
                    aaa+=1
                    if aaa==30 and bullets>1:
                        yeetsize=1
                        bullets-=1
                        print('reloaded')
                        aaa=0
            if mp5size==0 and bullets>0:
                if aaa==0:
                    reload.play()
                    print('RELOADINg......')
                    aaa=1
                if porn%10==0:
                    aaa+=1
                    if aaa==20 and bullets>39:
                        mp5size=40
                        bullets-=40
                        aaa=0
                        print('reloaded')
                    elif aaa==20 and bullets<40:
                        mp5size=bullets
                        bullets=0
                        aaa=0
                        print('reloaded')
            if battery<0.1 and batteries>0:
                if aaa==0:
                    print('reloading')
                    aaa=1
                    reload2.play()
                if porn%10==0:
                    aaa+=1
                    if aaa==30 and batteries>1:
                        battery=100
                        batteries-=1
                        print('reloaded')
                        aaa=0
            if zombie1Infected:
                zombie1Health-=0.125
            if zombie2Infected:
                zombie2Health-=0.125
            if zombie3Infected:
                zombie3Health-=0.125
            if zombie4Infected:
                zombie4Health-=0.125
            if zombie5Infected:
                zombie5Health-=0.125
            if zombie6Infected:
                zombie6Health-=0.125
            if shotgun and q1<6:
                gunStrength=1
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-5,5)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                q1+=1
            if spas12 and q1<6:
                gunStrength=1.5
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-3,3)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                q1+=1
            if uzi and counter%8==0 and armagsize>0:
                gun2.play()
                gunStrength=1
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                armagsize-=1
            if skorpion and counter%12==0 and armagsize>0:
                gun2.play()
                gunStrength=1
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                armagsize-=1
            if mp5 and counter%8==0 and mp5size>0:
                gun1.play()
                gunStrength=4
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                if 1:
                    mp5size-=1
            if p90 and counter%5==0 and armagsize>0:
                gun2.play()
                gunStrength=1
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                if 1:
                    armagsize-=1
            if ak47 and counter%10==0 and armagsize>0:
                gun1.play()
                gunStrength=3
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                if 1:
                    armagsize-=1
            if M4A1 and counter%12==0 and armagsize>0:
                gun1.play() 
                gunStrength=4
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                if 1:
                    armagsize-=1

            if scar and counter%12==0 and armagsize>0:
                gun1.play() 
                gunStrength=6
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
                if 1:
                    armagsize-=1
            if hook and counter%12==0:
                
                gun1.play() 
                gunStrength=7
                bulletsList.append(bullet)
                bulletsList[-1].sideways=random.randint(-1,1)
                bulletsList[-1].x=x
                bulletsList[-1].fromShooterZombie=False
                bulletsList[-1].y=y
                bulletsList[-1].x=x
                bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                bulletsList[-1].img=pg.image.load('data/images/darkenergy.png')
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
            if flamethrower:
                if battery>0:
                    flameSound.play()
                    battery-=0.1
                    gunStrength=0.3
                    bulletsList.append(bullet)
                    bulletsList[-1].x=x
                    bulletsList[-1].fromShooterZombie=False
                    bulletsList[-1].y=y
                    bulletsList[-1].sideways=random.randint(-4,4)
                    bulletsList[-1].x=x
                    bulletsList[-1].rect=pg.Rect(bulletsList[-1].x,bulletsList[-1].y,10,30)
                    bulletsList[-1].img=pg.image.load('data/images/flame.png')
                    age=1
                if playerFacing==FORWARDS:
                    bulletsList[-1].facing=FORWARDS
                    bulletsList[-1].x=x +50
                if playerFacing==BACKWARDS: 
                    bulletsList[-1].facing=BACKWARDS
                    bulletsList[-1].y=y + 70
                    bulletsList[-1].x=x +5
                if playerFacing==LEFT:
                    bulletsList[-1].facing=LEFT
                    bulletsList[-1].y=y + 10
                if playerFacing==RIGHT:
                    bulletsList[-1].y=y + 50
                    bulletsList[-1].x=x +50
                    bulletsList[-1].facing=RIGHT
            if movingForward and bgY<0:
                zombiey+=playerSpeed
                zombiey2+=playerSpeed
                zombiey3+=playerSpeed
                zombiey4+=playerSpeed
                zombiey5+=playerSpeed
                zombiey6+=playerSpeed
                bgY+=playerSpeed
                if not bullet2x==10000:
                    bullet2y+=playerSpeed
                for A in bloods:
                    A.y+=playerSpeed
                for AA in bulletsList:
                    AA.y+=playerSpeed
                if item=='thompson' or 'ak47' or 'M4A1':
                    playerImg=playeri
                else:
                    playerImg=player2
                playerFacing=FORWARDS
                playerIterator+=1
                if playerIterator==19:
                    playerIterator=0
            if movingBack and bgY>-7200:
                bgY-=playerSpeed
                zombiey-=playerSpeed
                zombiey2-=playerSpeed
                zombiey3-=playerSpeed
                zombiey4-=playerSpeed
                zombiey5-=playerSpeed
                zombiey6-=playerSpeed
                playerFacing=BACKWARDS
                if not bullet2x==10000:
                    bullet2y-=playerSpeed
                for B in bloods:
                    B.y-=playerSpeed
                for AA in bulletsList:
                    AA.y-=playerSpeed
                if item=='thompson' or 'ak47' or 'M4A1':
                    playerImg=playerBack
                else:
                    playerImg=playerBack2
                    print('pqpqperthjhf')
                if porn%2==0:
                    playerIterator+=1
                if playerIterator==19:
                    playerIterator=0
            if movingRight and bgX>-8200:
                bgX-=playerSpeed
                zombiex-=playerSpeed
                zombiex2-=playerSpeed
                zombiex3-=playerSpeed
                zombiex4-=playerSpeed
                zombiex5-=playerSpeed
                zombiex6-=playerSpeed
                playerFacing=RIGHT
                if not bullet2x==10000:
                    bullet2x-=playerSpeed
                for C in bloods:
                    C.x-=playerSpeed
                for AA in bulletsList:
                    AA.x-=playerSpeed
                if item=='thompson' or 'ak47' or 'M4A1':
                    playerImg=playerRight
                else:
                    playerImg=playerRight2
                    print('pqpqperthjhf')
                if porn%2==0:
                    playerIterator+=1
                if playerIterator==19:
                    playerIterator=0
            if movingLeft and bgX<0:
                bgX+=playerSpeed
                playerFacing=LEFT
                zombiex+=playerSpeed
                zombiex2+=playerSpeed
                zombiex3+=playerSpeed
                zombiex4+=playerSpeed
                zombiex5+=playerSpeed
                zombiex6+=playerSpeed
                if not bullet2x==10000:
                    bullet2x+=playerSpeed
                for V in bloods:
                    V.x+=playerSpeed
                for AA in bulletsList:
                    AA.x-=playerSpeed
                if item=='thompson' or 'ak47' or 'M4A1':
                    playerImg=playerLeft
                else:
                    playerImg=playerLeft2
                    print('pqpqperthjhf')
                    
                if porn%2==0:
                    playerIterator+=1
                if playerIterator==19:
                    playerIterator=0
                    
            for b in bloods:
                gameDisplay.blit(b.img,(b.x,b.y))
            for p in bulletsList:
                gameDisplay.blit(p.img,(p.x,p.y))
                p.rect=pg.Rect(p.x,p.y,18,23)
            gameDisplay.blit(vignette, (0,0))
            
            for t in bulletsList:
                if t.y<800 and t.x<800:
                    if t.facing==FORWARDS:
                        t.y-=t.travelling
                    if t.facing==BACKWARDS:
                        t.y+=t.travelling
                    if t.facing==LEFT:
                        t.x-=t.travelling
                    if t.facing==RIGHT:
                        t.x+=t.travelling
            for t in bulletsList:
                if t.facing==FORWARDS or t.facing==BACKWARDS:
                    t.x+=t.sideways
                if t.facing==LEFT or t.facing==RIGHT:
                    t.y+=t.sideways

            
            #Zombie healrh bars
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex,zombiey-20,zombie1Health*5,10))
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex2,zombiey2-20,zombie2Health*5,10))
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex3,zombiey3-20,zombie3Health*5,10))
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex4,zombiey4-20,zombie4Health*5,10))
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex5,zombiey5-20,zombie5Health*5,10))
            pg.draw.rect(gameDisplay,(0,255,0),Rect(zombiex6,zombiey6-20,zombie6Health/3*10,10))
            if playerFacing==FORWARDS:
                playerImg=pg.transform.scale(playerImgs[playerIterator],(70,90))
            if playerFacing==BACKWARDS:
                playerImg=pg.transform.rotate(pg.transform.scale(playerImgs[playerIterator],(70,90)),180)
            if playerFacing==LEFT:
                playerImg=pg.transform.rotate(pg.transform.scale(playerImgs[playerIterator],(70,90)),90)
            if playerFacing==RIGHT:
                playerImg=pg.transform.rotate(pg.transform.scale(playerImgs[playerIterator],(70,90)),270)
                
            if fpsViewer:
                gameDisplay.blit(pg.font.Font(None,20).render('FPS:'+str(clock.get_fps()),True,(0,0,0)),(0,170))  #FPS Counter
            
            playerHitBox=pg.Rect(x,y,70,90)
            gameDisplay.blit(playerImg,(x,y))

            #Zombie hitboxes
            zombie=pg.Rect(zombiex,zombiey,50,50)
            zombie2=pg.Rect(zombiex2,zombiey2,50,50)
            zombie3=pg.Rect(zombiex3,zombiey3,50,50)
            zombie4=pg.Rect(zombiex4,zombiey4,50,50)
            zombie5=pg.Rect(zombiex5,zombiey5,50,50)
            zombie6=pg.Rect(zombiex6,zombiey6,50,50)
            if porn%7==0:
                zIterator+=1
            if zIterator==16:
                zIterator=0
            
            bullet2=pg.Rect(bullet2x,bullet2y,40,40)
            gameDisplay.blit(bullet2img,(bullet2x,bullet2y))
            if health>9:
                vignette=v0
            if health<9:
                vignette=v1
            if health<8:
                vignette=v2
            if health<6:
                vignette=v3
            if health<4:
                vignette=v4
            if health<2:
                vignette=v5
            
            for t in bulletsList:
                if t.age<10:
                    t.x==99999999999
                if t.age>0:
                    t.age+=1
            gameDisplay.blit(image1,(zombiex-10,zombiey-7))
            gameDisplay.blit(image1,(zombiex2-10,zombiey2-7))
            gameDisplay.blit(image3,(zombiex3-10,zombiey3-7))
            gameDisplay.blit(image3,(zombiex4-10,zombiey4-7))
            gameDisplay.blit(image3,(zombiex5-10,zombiey5-7))
            gameDisplay.blit(image1,(zombiex6-10,zombiey6))
            gameDisplay.blit(mutated,(zombiex6,zombiey6+10))
            if not playerHitBox.colliderect(zombie) or not playerHitBox.colliderect(zombie2) or not playerHitBox.colliderect(zombie3) or not playerHitBox.colliderect(zombie4) or not playerHitBox.colliderect(zombie5) or not playerHitBox.colliderect(zombie6): 
                zombiey+=0.7
                zombiey2+=0.7
                zombiey3-=0.7
                zombiey4-=0.7
                zombiey5-=0.7
                zombiey6+=1.5
            scoredisplay=BIGFONT.render('SKULLS: '+str(score),False,darkgreen)
            if item=='Skorpion' or item=='Uzi' or item=='AK47' or item=='M4A1' or item=='Thompson' or item=='Scar' or item=='P90':
                if armagsize==0 and bullets>0:
                    bulletsdisplay=kindaBigFont.render('Reloading...',True,darkgreen)

                else:
                    bulletsdisplay=BIGFONT.render(str(armagsize)+'/'+str(bullets),True,darkgreen)
            elif item=='Pistol' or item=='Corona16':
                if magsize==0 and bullets>0:
                    bulletsdisplay=kindaBigFont.render('Reloading...',True,darkgreen)

                else:
                    bulletsdisplay=BIGFONT.render(str(magsize)+'/'+str(bullets),True,darkgreen)
            elif item=='Raygun' or item=='Plasma Cannon' or item=='Neutron Beam' or item=='Flamethrower':
                if magsize==0 and bullets>0:
                    bulletsdisplay=kindaBigFont.render('Recharging...',True,darkgreen)

                else:
                    bulletsdisplay=kindaBigFont.render(str(int(battery))+'%/'+str(batteries),True,darkgreen)
            elif item=='Revolver' or item=='Shotgun' or item=='SPAS12':
                if revsize==0 and bullets>0:
                    bulletsdisplay=kindaBigFont.render('Reloading...',True,darkgreen)

                else:
                    bulletsdisplay=BIGFONT.render(str(revsize)+'/'+str(bullets),True,darkgreen)
            elif item=='TNT Yeeter' or item=='Nuke Yeeter':
                if yeetsize==0 and bullets>0:
                    bulletsdisplay=kindaBigFont.render('Reloading...',True,darkgreen)

                else:
                    bulletsdisplay=BIGFONT.render(str(yeetsize)+'/'+str(bullets),True,darkgreen)
            elif item=="Maui's Fish Hook":
                bulletsdisplay=BIGFONT.render('inf',True,darkgreen)
            elif item=="MP5":
                bulletsdisplay=BIGFONT.render(str(mp5size)+'/'+str(bullets),True,darkgreen)
            if item=='Raygun' or item=='Plasma Cannon' or item=='Neutron Beam' or item=='Flamethrower':
                gameDisplay.blit(bulletsdisplay,(20,52))
            else:
                gameDisplay.blit(bulletsdisplay,(20,52))
            gameDisplay.blit(scoredisplay,(600,20))
            
            item=arsenal[itemIndex]
            gameDisplay.blit(kindaBigFont.render('ITEM: ' + item,False,darkgreen),(400-kindaBigFont.render('ITEM: ' + item,False,darkgreen).get_width()/2,600))
            bgRect=pg.Rect(bgX,bgY,9000,8000)
            #collision detect
            if zombiey>800:
                zombiex=random.randint(5,800)
                zombiey=-200
                zombie1infected=False
                zombie1Health=10
            if zombiey2>800:
                zombiex2=random.randint(5,850)
                zombiey2=-200
                zombie2infected=False
                zombie2Health=10
            if zombiey3<0:
                zombiex3=random.randint(5,850)
                zombiey3=1200
                zombie3infected=False
                zombie3Health=10
            if zombiey4<0:
                zombiex4=random.randint(5,850)
                zombiey4=1200
                zombie4infected=False
                zombie4Health=10
            if zombiey5<0:
                zombiex5=random.randint(5,850)
                zombiey5=1200
                zombie5infected=False
                zombie5Health=10
            if zombiey6>800:
                zombiex6=random.randint(5,850)
                zombiey6=-200
                zombie6infected=False
                zombie6Health=15
            if health<1:
                a=death('player was slain by Zombie')
                break
            if zombie.colliderect(playerHitBox) and not zombie1frozen and counter%protection==0 :
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=0.75
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=0.5
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.3
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.1
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.05
                else:
                    health-=1
            if zombie2.colliderect(playerHitBox) and not zombie2frozen and counter%protection==0:
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=0.75
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=0.5
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.3
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.1
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.05
                else:
                    health-=1
            if zombie3.colliderect(playerHitBox) and not zombie3frozen and counter%protection==0:
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=0.75
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=0.5
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.3
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.1
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.05
                else:
                    health-=1
            if zombie4.colliderect(playerHitBox) and not zombie4frozen and counter%protection==0:
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=0.75
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=0.5
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.3
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.1
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.05
                else:
                    health-=1
            if zombie5.colliderect(playerHitBox) and not zombie5frozen and counter%protection==0:
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=0.75
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=0.5
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.3
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.1
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.05
                else:
                    health-=1
            if zombie6.colliderect(playerHitBox) and not mutatedzombiefrozen and counter%(protection/2)==0:
                if equippedarmor=='Toilet Paper Suit':
                    hurt 
                    health-=1.5
                elif equippedarmor=='Chainmail Armor':
                    hurt 
                    health-=1
                elif equippedarmor=='Steel Armor':
                    hurt 
                    health-=0.6
                elif equippedarmor=='Diamond Armor':
                    hurt 
                    health-=0.2
                elif equippedarmor=='Hafnium Armor':
                    hurt 
                    health-=0.1
                else:
                    health-=2
            for s in bulletsList:
                if zombie.colliderect(s.rect):
                    zombie1Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            gameDisplay.blit(eIterator,(zombiex,zombiey))
                    if not s.penetrate:
                        s.y=1000000
                        s.x=1000000
                        s.travelling=0
                    if s.infect:
                        zombie1Infected=True
                if zombie2.colliderect(s.rect):
                    zombie2Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            if porn%10==0:
                                gameDisplay.blit(eIterator,(zombiex2,zombiey2))
                    if not s.penetrate:
                        s.y=10000000
                        s.x=10000000
                        s.travelling=0
                    if s.infect:
                        zombie2Infected=True
                if zombie3.colliderect(s.rect):
                    zombie3Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            if porn%10==0:
                                gameDisplay.blit(eIterator,(zombiex3,zombiey3))
                    if not s.penetrate:
                        s.y=10000
                        s.x=10000
                        s.travelling=0
                    if s.infect:
                        zombie3Infected=True
                if zombie4.colliderect(s.rect):
                    zombie4Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            gameDisplay.blit(eIterator,(zombiex4,zombiey4))
                    if not s.penetrate:
                        s.y=100000
                        s.travelling=0
                        s.x=100000
                    if s.infect:
                        zombie4Infected=True
                if zombie5.colliderect(s.rect):
                    zombie5Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            gameDisplay.blit(eIterator,(zombiex5,zombiey5))
                    if not s.penetrate:
                        s.y=1000000
                        s.x=1000000
                        s.travelling=0
                    if s.infect:
                        zombie5Infected=True
                if zombie6.colliderect(s.rect):
                    zombie6Health-=gunStrength
                    if s.explode:
                        explosion.play()
                        for eIterator in explosions:
                            gameDisplay.blit(image6,(zombiex6,zombiey6))
                            gameDisplay.blit(eIterator,(zombiex6,zombiey6))
                            clock.tick(200)
                            pg.display.update()
                    if not s.penetrate:
                        s.y=1000000
                        s.travelling=0
                        s.x=1000000
                    if s.infect:
                        zombie6Infected=True
            if zombie1Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex
                bloods[-1].y=zombiey
                zombiex=random.randint(5,800)
                zombiey=-100
                score=score + random.randint(1,10)*rebirths
                zombie1Health=10
                zombie1Infected=False
            if zombie2Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex2
                bloods[-1].y=zombiey2
                zombiex2=random.randint(5,800)
                zombiey2=-100
                score=score + random.randint(1,10)*rebirths
                zombie2Health=10
                zombie2Infected=False
            if zombie3Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex3
                bloods[-1].y=zombiey3
                zombiex3=random.randint(5,800)
                zombiey3=-100
                score=score + random.randint(1,10)*rebirths
                zombie3Health=10
                zombie3Infected=False
            if zombie4Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex4
                bloods[-1].y=zombiey4
                zombiex4=random.randint(5,800)
                zombiey4=-100
                score=score + random.randint(1,10)*rebirths
                zombie4Health=10
                zombie4Infected=False
            if zombie5Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex5
                bloods[-1].y=zombiey5
                zombiex5=random.randint(5,800)
                zombiey5=-100
                score=score + random.randint(1,10)*rebirths
                zombie5Health=10
                zombie5Infected=False
            if zombie6Health<1:
                bloods.append(blood)
                bloods[-1].x=zombiex6
                bloods[-1].y=zombiey6
                zombiex6=random.randint(5,800)
                zombiey6=-100
                score=score + random.randint(1,10)*rebirths
                zombie6Health=15
                zombie6Infected=False
           
            if playerHitBox.colliderect(bullet2) and (bullets<40 or batteries<10):  #Collectible bullet control
                pickup.play()
                batteries+=1
                if bullets<30:
                    bullets+=random.randint(10,15)
                    bullet2x=10000
                else:
                    bullets-=bullets-40
                    bullet2x=10000
                    




                    
            if random.randint(0,1000)==15 and bullet2x==10000:
                bullet2x=random.randint(4,650)
                bullet2y=random.randint(10,580)
           
            if random.randint(1,2)==1:
                if x<0:
                    xs=0
                if x>1000:
                    x=1000
                if zombiex<x+30:
                    zombiex+=clock.get_fps()/50
                if zombiex>x+30:
                    zombiex-=clock.get_fps()/50
                if zombiex2<x+30:
                    zombiex2+=clock.get_fps()/50
                if zombiex2>x+28:
                    zombiex2-=clock.get_fps()/50
                if zombiex3<x+26:
                    zombiex3+=clock.get_fps()/50
                if zombiex3>x+20:
                    zombiex3-=clock.get_fps()/50
                if zombiex4<x+25:
                    zombiex4+=clock.get_fps()/50
                if zombiex4>x+32:
                    zombiex4-=clock.get_fps()/50
                if zombiex5<x+31:
                    zombiex5+=clock.get_fps()/50
                if zombiex5<x+31:
                    zombiex5+=clock.get_fps()/50
            if random.randint(1,10)<30:
                if zombiex6>x+30:
                    zombiex6-=clock.get_fps()/50
                if zombiex6<x+30:
                    zombiex6+=clock.get_fps()/50
            try:
                if random.randint(0,400)==10:
                    del bloods[0]
            except IndexError:
                pass
            if not playerHitBox.colliderect(bgRect):
               text= BIGFONT.render("You are out of bounds! Game will throw you to 0,0",False,black)
               gameDisplay.blit(text,(0,200))
               pg.display.update()
               time.sleep(2)
               bgX=-1000
               bgY=-1000
            counter+=1
            clock.tick(FPS)
            gameDisplay.blit(heart1,(10,10))
            pg.draw.rect(gameDisplay,(39, 207, 198),Rect(5,30,stamina,20))
            gameDisplay.blit(stamina_icon,(8,27))
            gameDisplay.blit(bullet_icon,(10,55))
            gameDisplay.blit(bars,(0,0))
            gameDisplay.blit(hotbar,(250,625))
            pg.draw.rect(gameDisplay,(0,(health+10)*10,0),Rect(5,5,health*10,20))
            try:
                if arsenal[0]=='Revolver':
                    gameDisplay.blit(pg.transform.scale(revolverimg,(80,30)),(260,640))
                if arsenal[0]=='Pistol':
                    gameDisplay.blit(pg.transform.scale(pistolimg,(80,30)),(260,640))
                if arsenal[0]=='Skorpion':
                    gameDisplay.blit(pg.transform.scale(skorpionimg,(80,30)),(260,640))
                if arsenal[0]=='Shotgun':
                    gameDisplay.blit(pg.transform.scale(shotgunimg,(80,30)),(260,640))
                if arsenal[0]=='Uzi':
                    gameDisplay.blit(pg.transform.scale(uziimg,(80,30)),(260,640))
                if arsenal[0]=='Thompson':
                    gameDisplay.blit(pg.transform.scale(thompsonimg,(80,30)),(260,640))
                if arsenal[0]=='P90':
                    gameDisplay.blit(pg.transform.scale(p90img,(80,30)),(260,640))
                if arsenal[0]=='AK47':
                    gameDisplay.blit(pg.transform.scale(ak47img,(80,30)),(260,640))
                if arsenal[0]=='M4A1':
                    gameDisplay.blit(pg.transform.scale(M4A1img,(80,30)),(260,640))
                if arsenal[0]=='SPAS12':
                    gameDisplay.blit(pg.transform.scale(spasimg,(80,30)),(260,640))
                if arsenal[0]=='Scar':
                    gameDisplay.blit(pg.transform.scale(scarimg,(80,30)),(260,640))
                if arsenal[0]=='Corona16':
                    gameDisplay.blit(pg.transform.scale(coronaimg,(80,30)),(260,640))
                if arsenal[0]=='TNT Yeeter':
                    gameDisplay.blit(pg.transform.scale(tntimg,(80,30)),(260,640))
                if arsenal[0]=='Nuke Yeeter':
                    gameDisplay.blit(pg.transform.scale(nukeimg,(80,30)),(260,640))
                if arsenal[0]=='Flamethrower':
                    gameDisplay.blit(pg.transform.scale(flameimg,(80,30)),(260,640))
                if arsenal[0]=="Maui's Fish Hook":
                    gameDisplay.blit(pg.transform.scale(hookimg,(80,70)),(260,620))
                if arsenal[0]=='Raygun':
                    gameDisplay.blit(pg.transform.scale(rayimg,(80,30)),(260,640))
                if arsenal[0]=='Plasma Cannon':
                    gameDisplay.blit(pg.transform.scale(plasmaimg,(80,30)),(260,640))
                if arsenal[0]=='Neutron Beam':
                    gameDisplay.blit(pg.transform.scale(neutronimg,(80,30)),(260,640))

                if arsenal[1]=='Revolver':
                    gameDisplay.blit(pg.transform.scale(revolverimg,(80,30)),(360,640))
                if arsenal[1]=='Pistol':
                    gameDisplay.blit(pg.transform.scale(pistolimg,(80,30)),(360,640))
                if arsenal[1]=='Skorpion':
                    gameDisplay.blit(pg.transform.scale(skorpionimg,(80,30)),(360,640))
                if arsenal[1]=='Shotgun':
                    gameDisplay.blit(pg.transform.scale(shotgunimg,(80,30)),(360,640))
                if arsenal[1]=='Uzi':
                    gameDisplay.blit(pg.transform.scale(uziimg,(80,30)),(360,640))
                if arsenal[1]=='Thompson':
                    gameDisplay.blit(pg.transform.scale(thompsonimg,(80,30)),(360,640))
                if arsenal[1]=='P90':
                    gameDisplay.blit(pg.transform.scale(p90img,(80,30)),(360,640))
                if arsenal[1]=='AK47':
                    gameDisplay.blit(pg.transform.scale(ak47img,(80,30)),(360,640))
                if arsenal[1]=='M4A1':
                    gameDisplay.blit(pg.transform.scale(M4A1img,(80,30)),(360,640))
                if arsenal[1]=='SPAS12':
                    gameDisplay.blit(pg.transform.scale(spasimg,(80,30)),(360,640))
                if arsenal[1]=='Scar':
                    gameDisplay.blit(pg.transform.scale(scarimg,(80,30)),(360,640))
                if arsenal[1]=='Corona16':
                    gameDisplay.blit(pg.transform.scale(coronaimg,(80,30)),(360,640))
                if arsenal[1]=='TNT Yeeter':
                    gameDisplay.blit(pg.transform.scale(tntimg,(80,30)),(360,640))
                if arsenal[1]=='Nuke Yeeter':
                    gameDisplay.blit(pg.transform.scale(nukeimg,(80,30)),(360,640))
                if arsenal[1]=='Flamethrower':
                    gameDisplay.blit(pg.transform.scale(flameimg,(80,30)),(360,640))
                if arsenal[1]=="Maui's Fish Hook":
                    gameDisplay.blit(pg.transform.scale(hookimg,(80,70)),(360,620))
                if arsenal[1]=='Raygun':
                    gameDisplay.blit(pg.transform.scale(rayimg,(80,30)),(360,640))
                if arsenal[1]=='Plasma Cannon':
                    gameDisplay.blit(pg.transform.scale(plasmaimg,(80,30)),(360,640))
                if arsenal[1]=='Neutron Beam':
                    gameDisplay.blit(pg.transform.scale(neutronimg,(80,30)),(360,640))
                if arsenal[1]=='MP5':
                    gameDisplay.blit(pg.transform.scale(mp5img,(80,30)),(360,640))


                if arsenal[2]=='Revolver':
                    gameDisplay.blit(pg.transform.scale(revolverimg,(80,30)),(460,640))
                if arsenal[2]=='Pistol':
                    gameDisplay.blit(pg.transform.scale(pistolimg,(80,30)),(460,640))
                if arsenal[2]=='Skorpion':
                    gameDisplay.blit(pg.transform.scale(skorpionimg,(80,30)),(460,640))
                if arsenal[2]=='Shotgun':
                    gameDisplay.blit(pg.transform.scale(shotgunimg,(80,30)),(460,640))
                if arsenal[2]=='Uzi':
                    gameDisplay.blit(pg.transform.scale(uziimg,(80,30)),(460,640))
                if arsenal[2]=='Thompson':
                    gameDisplay.blit(pg.transform.scale(thompsonimg,(80,30)),(460,640))
                if arsenal[2]=='P90':
                    gameDisplay.blit(pg.transform.scale(p90img,(80,30)),(460,640))
                if arsenal[2]=='AK47':
                    gameDisplay.blit(pg.transform.scale(ak47img,(80,30)),(460,640))
                if arsenal[2]=='M4A1':
                    gameDisplay.blit(pg.transform.scale(M4A1img,(80,30)),(460,640))
                if arsenal[2]=='SPAS12':
                    gameDisplay.blit(pg.transform.scale(spasimg,(80,30)),(460,640))
                if arsenal[2]=='Scar':
                    gameDisplay.blit(pg.transform.scale(scarimg,(80,30)),(460,640))
                if arsenal[2]=='Corona16':
                    gameDisplay.blit(pg.transform.scale(coronaimg,(80,30)),(460,640))
                if arsenal[2]=='TNT Yeeter':
                    gameDisplay.blit(pg.transform.scale(tntimg,(80,30)),(460,640))
                if arsenal[2]=='Nuke Yeeter':
                    gameDisplay.blit(pg.transform.scale(nukeimg,(80,30)),(460,640))
                if arsenal[2]=='Flamethrower':
                    gameDisplay.blit(pg.transform.scale(flameimg,(80,30)),(460,640))
                if arsenal[2]=="Maui's Fish Hook":
                    gameDisplay.blit(pg.transform.scale(hookimg,(80,70)),(460,620))
                if arsenal[2]=='Raygun':
                    gameDisplay.blit(pg.transform.scale(rayimg,(80,30)),(460,640))
                if arsenal[2]=='Plasma Cannon':
                    gameDisplay.blit(pg.transform.scale(plasmaimg,(80,30)),(460,640))
                if arsenal[2]=='Neutron Beam':
                    gameDisplay.blit(pg.transform.scale(neutronimg,(80,30)),(460,640))
                if arsenal[2]=='MP5':
                    gameDisplay.blit(pg.transform.scale(mp5img,(80,30)),(460,640))
            except:
                pass

            if item==arsenal[0]:
                gameDisplay.blit(selected,(250,625))
            try:
                if item==arsenal[1]:
                    gameDisplay.blit(selected,(350,625))
            except:
                pass
            try:
                if item==arsenal[2]:
                    gameDisplay.blit(selected,(450,625))
            except:
                pass
            
            pg.display.update()

