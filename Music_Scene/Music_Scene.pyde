#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~-  Data Map  -~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#   Name            Purpose                                                        Type            Limit
##  machine         Holds the background image                                     Image           n/a
##  joycount        Holds the rotation counter for the joystick and logo           int             -40 - 40
##  joytf           Holds the direction of the rotation for the joystick/logo      boolean         True / False
##  logo            Holds logo image                                               Image           n/a
##  ship            Holds ship image                                               Image           n/a
##  medals          Holds medal image                                              Image           n/a
##  crt             Holds CRT filter image                                         Image           n/a
##  partmachine     Holds the image for part of the arcade machine                 Image           n/a
##  x               Holds x-position                                               int             0 - 800
##  y               Holds y-position                                               int             83 - 399
##  direction       Holds if x and/or y is increasing                              list            n/a
##  facing          Holds the direction the ship is facing (True=Left,False=Right) boolean         True or False
##  going           True if ship is travelling forwards, False if backwards        boolean         True or False
##  change          Holds if ship has changed direction                            boolean         True or False
##  minim           Initialized the minim library                                  n/a             n/a
##  player           Holds song                                                    SoundFile       n/a
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


add_library('minim')


def setup():
    global machine, joycount, joytf, logo, ship, x, y, direction, facing, change, going, medals, crt, partmachine
    size(800,600)
    machine = loadImage("Arcade Machine.png")
    joycount = 0
    joytf = False
    logo = loadImage("galaga.png")
    ship = loadImage("ship.png")
    medals = loadImage("Medals.png")
    crt = loadImage("crt2.png")
    partmachine = loadImage("Part of Arcade Machine.png")
    x = 386
    y = 385
    direction = [False, False]
    facing = True # True if left, False if right
    going = True # True if forwards, False if backwards
    change = False
    minim = Minim(this)
    player = minim.loadFile("Galaga Intro.mp3") # unfortunately had to swap out the JazzNESs' Galaga theme to be respectful to their work
    player.loop()

def draw():
    global machine, joycount, joytf, logo, ship, x, y, direction, facing, change, going, medals, crt, partmachine
    if direction[0]:
        x += 2
    else:
        x -= 2
    
    if direction[1]:
        y += 2
    else:
        y -= 2
    
    
    if joycount > 40:
        joytf = True
    elif joycount < -40:
        joytf = False
    
    if  joytf:
        joycount -=1
    else:
        joycount +=1
        
    background(255,255,255)
    imageMode(CORNER)
    image(machine, -5,0, machine.width, machine.height)
    imageMode(CENTER)
    
    
    
    if not facing:
        if going:
            pushMatrix()
            scale(-1.0,1.0)
            image(ship, x*-1, y, ship.width/8.0, ship.height/8.0)
            popMatrix()
        else:
            pushMatrix()
            scale(1.0,-1.0)
            image(ship, x, y*-1, ship.width/8.0, ship.height/8.0)
            popMatrix()
    else:
         if going:
            image(ship, x, y, ship.width/8.0, ship.height/8.0)
         else:
            pushMatrix()
            scale(-1.0,-1.0)
            image(ship, x*-1, y*-1, ship.width/8.0, ship.height/8.0)
            popMatrix()
    
    
    if (x + (ship.width / 16.0) + 30) >= 800:
        direction[1] = True
        direction[0] = False
        change = True
        going = False
    elif (x - (ship.width / 16.0) - 21) <= 0:
        direction[0] = True
        direction[1] = True
        change = True
        going = False
    
    elif (x == 400) and change:
        if facing:
            direction[0] = True
            direction[1] = False
            facing = False
            going = True
            change = False
        else:
            direction[0] = False
            direction[1] = False
            facing = True
            going = True
            change = False
    
    pushMatrix()
    translate(400, 120)
    rotate(radians(joycount/3.0))
    image(logo, 0,0, logo.width/4.0, logo.height/4.0)
    popMatrix()
    image(medals, 800 - (medals.width/2.0), 600 - (medals.height/2.0), medals.width/2.0, medals.height/2.0)
    
    
    
    
    imageMode(CORNER)
    image(crt, 24,22, (crt.width) , (crt.height))
    image(partmachine, 0, 0, partmachine.width, partmachine.height)
    

    pushMatrix()
    translate(235,600)
    rotate(radians(joycount))
    fill(0,0,0)
    rect(0, -45, 25, 70)
    fill(188, 17, 17)
    ellipse(10, -45, 60, 60)
    popMatrix()
    
    
    
    
    