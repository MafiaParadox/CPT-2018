# -------------------------------------------------------------------------------
"Note: This game is glichy with the images once loaded &
I have no idea how to fix this. 
Allow one game round to happen then it should be normal. 
Also some collisions are a little off. "
# -------------------------------------------------------------------------------

player = PVector(620,900) 
player_size = 40
bullet_x = player.x 
bullet_y = player.y - 10
bullet_size = 15
bullet_t = False

alien = PVector(100,100)
alien_speed = PVector(4,0)
alien_size = 100
alien_hit = 0
attack = PVector(alien.x, alien.y)
attack_x = alien.x
attack_y = alien.y
attack_size = 30

speed = PVector(0, 5)
limit_speed = PVector(0, 15)

asteroid_1 = PVector(50, 50)
asteroid_1_size = 120

asteroid_2 = PVector(850, 100)
asteroid_2_size = 100

heart = PVector(40,40)
heart_size = 40
hit = 0

# Images
space_img = requestImage("space.jpg")
startscreen_img = requestImage("startscreen.png")
alien_img = requestImage("6EQUJ5.png")
instruction_img = requestImage("instructions.png")
asteroid_img = requestImage("Asteroid.png")
heart_img = requestImage("heart.jpg")
win_img = requestImage("winscreen.png")
FailGameover_img = requestImage("gameover.png")
WinGameover_img = requestImage("winscreen.png")

screen = "startscreen"

# -------------------------------------------------------------------------------
def setup():
    size(1200, 1000)
    
    for s in range(6000):
        background(0)
        fill(189, 240, 236)
        textSize(90)
        text("Loading...", 250, 500)
    
        if s >= 5999:
            background(0)
            screen = "startscreen"

def reset():
    global player, screen
    global alien_speed, alien_size, alien, alien_hit
    global attack, attack_x, attack_y, attack_size
    global bullet_t, bullet_x, bullet_y, speed
    global asteroid_1, asteroid_2, asteroid_2_size
    global asteroid_1_size, limit_speed
    global heart, heart_size, hit
    global space_img 
    global startscreen_img
    global alien_img
    global instruction_img
    global asteroid_img
    global heart_img
    player = PVector(620,900) 
    player_size = 40
    bullet_x = player.x 
    bullet_y = player.y - 10
    bullet_size = 15
    bullet_t = False
    alien = PVector(100,100)
    alien_speed = PVector(6,0)
    alien_size = 100
    alien_hit = 0
    attack = PVector(alien.x, alien.y)
    attack_x = alien.x
    attack_y = alien.y
    attack_size = 30
    speed = PVector(0, 5)
    limit_speed = PVector(0, 15)
    asteroid_1 = PVector(50, 50)
    asteroid_1_size = 120
    asteroid_2 = PVector(850, 100)
    asteroid_2_size = 100
    heart = PVector(40,40)
    heart_size = 40
    hit = 0
    # Images
    space_img = requestImage("space.jpg")
    startscreen_img = requestImage("startscreen.png")
    alien_img = requestImage("6EQUJ5.png")
    instruction_img = requestImage("instructions.png")
    asteroid_img = requestImage("Asteroid.png")
    heart_img = requestImage("heart.jpg")
    win_img = requestImage("winscreen.png")
    FailGameover_img = requestImage("gameover.png")
    WinGameover_img = requestImage("winscreen.png")
    screen = "startscreen"

# -------------------------------------------------------------------------------    
def draw():
    global player, screen
    global alien_speed, alien_size, alien
    global bullet_t, bullet_x, bullet_y, speed
    global asteroid_1, asteroid_2, asteroid_2_size
    global asteroid_1_size, limit_speed
    global heart, heart_size, hit, alien_hit
# Images
    global space_img 
    global startscreen_img
    global alien_img
    global instruction_img
    global asteroid_img
    global heart_img 
    
# Opening screen
    if screen == "startscreen":
        
    # Image not loaded
        if startscreen_img.width == 0:
            redraw()
            pass 
    # Error during loading
        elif startscreen_img.width == -1:
            redraw()
            pass 
        else:
            image(startscreen_img, 0, 0)

    #Title
        font = loadFont("AdobeDevanagari-Bold-48.vlw")
        textFont(font, 32)
        fill(209,170,26)
        textSize(120)
        text("PewPew", 250, 500)
    #Start
        textSize(40)
        text("Press 'Up Arrow' to Start", 220, 650)
    #Instructions
        textSize(25)
        text("Press 'Down Arrow' for Instructions", 250, 730)
        
# Instruction Screen
    if screen == "InstructionsScreen":
        image(instruction_img, 1, -1)
        
#Game Screen 
    if screen == "gamescreen":
        tint(143, 204, 222)
        image(space_img , 1, -1)    
    #Alien
        fill(249, 8, 8)
        attack.y += 10
        ellipse(attack.x, attack.y, attack_size, attack_size)
        attack.add(alien_speed)
        if attack.y >= height:
            attack.y = alien.y 
        noTint()
        image(alien_img, alien.x, alien.y, alien_size, alien_size)
        alien.add(alien_speed)
        if alien.x > 1120:
            alien_speed += PVector(-4,0)
        elif alien.x < 0:
            alien_speed += PVector(4,0)
            
    #PlayerShip
        noTint()
        strokeWeight(3)
        stroke(76, 76, 76)
        fill(191, 191, 191)
        ellipse(player.x,player.y, 40, 40)
        fill(157, 157, 157)
        rect(player.x+20,player.y-25 , 10, 40)
        rect(player.x-30,player.y-25 , 10, 40)
            
    #asteroid_1
        image(asteroid_img, asteroid_1.x, asteroid_1.y, asteroid_1_size, asteroid_1_size)
        asteroid_1.add(speed)
        if asteroid_1.y > height+200:
            asteroid_1.y = 0
            asteroid_1.x = random(width)
            if asteroid_1.x > width:
                asteroid_1.x <= width
            asteroid_1_size = random(80,400)
            speed += PVector(0, 1)
        if speed >= limit_speed:
            speed = PVector(0, 5)
    
    #asteroid_2
        image(asteroid_img, asteroid_2.x, asteroid_2.y, asteroid_2_size, asteroid_2_size)
        asteroid_2.add(speed)
        if asteroid_2.y > height+200:
            asteroid_2.y = -50
            asteroid_2.x = random(width)
            asteroid2_size = random(80,400)
            speed += PVector(0, 1)
        if speed >= limit_speed:
            speed = PVector(0, 5)
        
    #Bullet hits alien
        radius = bullet_size/2
        enemy_radius = alien_size/2
        a = bullet_x - alien.x
        b = bullet_y - alien.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            alien = PVector(-400,-100)
            bullet_x = player.x 
            bullet_y = player.y 
            alien_hit += 1
            if alien_hit == 1:
                screen = "Win"   
                
   #Bullet hits asteroid_1
        radius = bullet_size/2
        enemy_radius = asteroid_1_size/2
        a = bullet_x - asteroid_1.x
        b = bullet_y - asteroid_1.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            asteroid_1.y = 0
            asteroid_1.x = random(width)
            bullet_x = player.x 
            bullet_y = player.y 
            bullet_t = False      
        
    #Bullet hits asteroid_2
        radius = bullet_size/2
        enemy_radius = asteroid_2_size/2
        a = bullet_x - asteroid_2.x
        b = bullet_y - asteroid_2.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            asteroid_2.y = 0
            asteroid_2.x = random(width)
            bullet_x = player.x 
            bullet_y = player.y 
            bullet_t = False                   
 
    #asteroid_1 hit player
        radius = player_size/2
        enemy_radius = asteroid_1_size/2
        a = asteroid_1.x - player.x
        b = asteroid_1.y - player.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            hit += 1
            asteroid_1.x = random(0, width) 
            asteroid_1.y = (-11)  

    # asteroid_2 hit player
        radius = player_size/2
        enemy_radius = asteroid_2_size/2
        a = asteroid_2.x - player.x
        b = asteroid_2.y - player.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            hit += 1
            asteroid_2.x = random(0, width) 
            asteroid_2.y = (-15)

    # Attack hit player
        radius = player_size/2
        enemy_radius = attack_size/2
        a = attack.x - player.x
        b = attack.y - player.y
        distance = sqrt(a**2 + b**2) 
        if distance <= radius + enemy_radius:
            hit += 1
            attack.y = alien.y 

    #Keep player in the screen
        if player.x > width:
            player.x = width
         
    #Heart counter
        if hit == 0:
            for heart.x in range (63, 200, 55):
                image(heart_img, heart.x, heart.y, heart_size, heart_size)
        elif hit == 1:
            for heart.x in range (63, 150, 55):
                image(heart_img, heart.x, heart.y, heart_size, heart_size)
        elif hit == 2:
            for heart.x in range (63, 100, 55):
                image(heart_img, heart.x, heart.y, heart_size, heart_size) 
        elif hit >= 3:
           screen = "Failed"
           
    #Call Bullet
        if bullet_t == True:
            bullet()
#Win 
    if screen == "Win":
        image(WinGameover_img, 1, -1)                
#Fail
    if screen == "Failed":
        image(FailGameover_img, 1, -1)

def keyReleased():
    global screen
    global player
    global bullet_x 
    global bullet_t 
    
    if screen == "startscreen":
        if (key==CODED):
            if (keyCode== UP):
                screen = "gamescreen"
            if (keyCode== DOWN):
                screen = "InstructionsScreen"   
    
    elif screen == "InstructionsScreen":
        if (key==CODED):
            if (keyCode== DOWN):
                screen = "startscreen"
    
    elif screen == "gamescreen":
        if (key==CODED):
            if (keyCode == LEFT):
                if player.x > 0:
                    player.x = player.x -80
                    bullet_x = bullet_x -80 
            elif (keyCode == RIGHT):
                if player.x < width:
                    player.x = player.x +80
                    bullet_x = bullet_x +80 
            elif (keyCode == UP):
                bullet_t = True
    
#CHECK IF WORKING PROPERLY ----------------------------------------------->
    elif screen == "Failed" or screen == "Win":
        if (key == CODED):
            if (keyCode == DOWN):
                screen = "startscreen"
                reset()
            elif (keyCode == UP):
                screen = "gamescreen"
                reset()

def bullet():
    global player, bullet_x, bullet_y, bullet_t 
    
    bullet_y += -10
    fill(164, 255, 250)
    strokeWeight(2)
    stroke(0, 127, 120)
    ellipse(bullet_x + 24,bullet_y,bullet_size,bullet_size)
    if bullet_y <= 0:
         bullet_y = player.y - 24
         bullet_t = False
    ellipse(bullet_x - 26,bullet_y,bullet_size,bullet_size)
    if bullet_y <= 0:
         bullet_y = player.y - 26
         bullet_t = False