player = PVector(620,900) 

bullet_x = player.x
bullet_y = player.y

bullet_size = 10
bullet_t = False

alien = PVector(620,100)
alien_speed = PVector(4,0)
alien_size = 100
attack = PVector(alien.x, alien.y)
attack_x = alien.x
attack_y = alien.y
attack_size = 30

player_size = 40

asteroid_1 = PVector(50, 50)
asteroid_1_size = 80

asteroid_2 = PVector(850, 100)
asteroid_2_size = 100

speed = PVector(0, 5)
limit_speed = PVector(0, 15)

heart = PVector(40,40)
heart_size = 40
hit = 0

def setup():
    size(1200, 1000)
    for s in range(5000):
        background(0)
        fill(189, 240, 236)
        textSize(90)
        text("Loading...", 250, 500)
        
        if s >= 4999:
            background(255,255,8)
            
def draw():
        
    background(255,255,8)
    global player
    global bullet_t, bullet_x, bullet_y 
    global alien, alien_speed, alien_size 
    global attack_x, attack_y, attack, attack_size

    global asteroid_1, speed
    global asteroid_1_size, limit_speed
    
    global heart, heart_size, hit 
    
#Bullet hits alien
    radius = bullet_size/2
    enemy_radius = alien_size/2
    a = bullet_x - alien.x
    b = bullet_y - alien.y
    distance = sqrt(a**2 + b**2) 
    if distance <= radius + enemy_radius:
        alien = PVector(-100,-110)
        attack = PVector(-100,-110)
        attack.y += 0
        bullet_x = player.x 
        bullet_y = player.y 
    if bullet_t == True:
        bullet()
        
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
 
#  asteroid_1
    fill(0)
    ellipse(asteroid_1.x, asteroid_1.y, asteroid_1_size, asteroid_1_size)
    asteroid_1.add(speed)
    if asteroid_1.y > height+200:
        asteroid_1.y = 0
        asteroid_1.x = random(width)
        asteroid_1_size = random(80,400)
        speed += PVector(0, 1)
    if speed >= limit_speed:
        speed = PVector(0, 5)
        
#  asteroid_2
    fill(0)
    ellipse(asteroid_2.x, asteroid_2.y, asteroid_2_size, asteroid_2_size)
    asteroid_2.add(speed)
    if asteroid_2.y > height+200:
        asteroid_2.y = 0
        asteroid_2.x = random(width)
        asteroid2_size = random(80,400)
        speed += PVector(0, 1)
    if speed >= limit_speed:
        speed = PVector(0, 5)

# asteroid_1 hit player
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

#Player
    fill(157, 157, 157)
    ellipse(player.x,player.y, 40, 40)
    rect(player.x+20,player.y-25 , 10, 40)
    rect(player.x-30,player.y-25 , 10, 40)
    
# Alien
    attack.y += 10
    ellipse(attack.x, attack.y, attack_size, attack_size)
    attack.add(alien_speed)
    if attack.y >= height:
        attack.y = alien.y        
    
    ellipse(alien.x, alien.y, alien_size, alien_size)
    alien.add(alien_speed)
    
    if alien.x > 1120:
        alien_speed += PVector(-4,0)
    elif alien.x < 0:
        alien_speed += PVector(4,0)
    
    
    if hit == 0:
        for heart.x in range (63, 200, 55):
            ellipse(heart.x, heart.y, heart_size, heart_size)
    elif hit == 1:
        for heart.x in range (63, 150, 55):
            ellipse(heart.x, heart.y, heart_size, heart_size)
    elif hit == 2:
        for heart.x in range (63, 100, 55):
            ellipse(heart.x, heart.y, heart_size, heart_size)
            
    if player.x > width:
        player.x = width
    
def keyPressed():
    global player, bullet_x 
    global bullet_t 
    
    if (key==CODED):
        if (keyCode == LEFT):
            if player.x > 0:
                player.x = player.x -10
                bullet_x = bullet_x -10 
        elif (keyCode == RIGHT):
            if player.x < width:
                player.x = player.x +10
                bullet_x = bullet_x +10 
        elif (keyCode == UP):
            bullet_t = True

def bullet():
    global player, bullet_x, bullet_y
    global bullet_t 

    bullet_y += -10
    ellipse(bullet_x + 24,bullet_y,bullet_size,bullet_size)
    if bullet_y <= 0:
         bullet_y = player.y - 24
         bullet_t = False
       
    ellipse(bullet_x - 26,bullet_y,bullet_size,bullet_size)
    if bullet_y <= 0:
         bullet_y = player.y - 26
         bullet_t = False