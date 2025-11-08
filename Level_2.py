exploding = False
explosionFrame = 0
Lives = 3
projectiles = []
asteroids = []
gameOverX = 1700
restartY = 900
lastShot = 0
fireRate = 100
Level_2 = 2
currentState = Level_2
startTime = 0
rocketX = 175
removed = []

def setup_level2():
    global rocket, blueProjectile, asteroidImage, asteroidRed, heart, explosionFrames, SpaceAge100, SpaceAge72, SpaceAge32, startTime
    imageMode(CENTER)
    rocket = loadImage("Rocket.png")
    blueProjectile = loadImage("ProjectileBlue.png")
    asteroidImage = loadImage("Asteroid1.png")
    asteroidRed = loadImage("Asteroidred.png")
    heart = loadImage("heart.png")

    startTime = millis()

    
    explosionFrames = []
    for i in range(20):
        explosionFrames.append(loadImage("Explosion"+str(i)+".png"))
    
    for i in range(40):
        x = random(width)
        y = random(height)
        size = random(60,120)
        rotation = random(TWO_PI)
        hit = False
        hits = 0
        asteroids.append([x,y,size,asteroidImage,rotation,hit,hits])
    
    SpaceAge100 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 100)
    SpaceAge72 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 72)
    SpaceAge32 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 32)
    
    
def draw_level2():
    global rocket, blueProjectile, exploding, explosionFrames, heart, Lives, explosionFrame, SpaceAge100, SpaceAge72, gameOverX, restartY, lastShot, fireRate, SpaceAge48, rocketX
        
    for asteroid in asteroids[:]:
        x,y,size,asteroidImage,rotation,hit,hits = asteroid
        
        if not exploding:
            asteroid[0] -= 2
            if asteroid[0] < -60:
                asteroid[0] = 1300
                asteroid[1] = random(height)
       

        pushMatrix()
        translate(x,y)
        rotate(rotation)
        image(asteroidImage,0,0,size,size)
        popMatrix()
        asteroid[0] -= 1
        asteroid[4] += random(0.02,0.05)
        
    for projectile in projectiles:
        px,py = projectile
        image(blueProjectile,projectile[0],projectile[1],20,20)
        projectile[0] += 5
        
        for asteroid in asteroids[:]:
            ax,ay,size,asteroidImage,rotation,hit,hits = asteroid
            if dist(px,py,ax,ay)<size/2:
                hits += 1
                asteroid[6] = hits
                asteroid[3] = asteroidRed
                projectiles.remove(projectile)
                
                
                if hits >= 7:
                    removed.append(asteroid)
                break
            if asteroid in removed:
                asteroids.remove(asteroid)
        
    for asteroid in asteroids[:]:
        ax, ay, size, asteroidImage, rotation, hit, hits = asteroid
        if exploding:
            pushMatrix()
            translate(ax,ay)
            rotate(rotation)
            image(asteroidImage,0,0,size,size)
            popMatrix()
            asteroid[0] -= 10
            asteroid[4] += random(0.02,0.05)
        
            if asteroid[0] < -50:
                asteroids.remove(asteroid)
    
        if asteroid[4] > TWO_PI:
            asteroid[4] -= TWO_PI
            
    for asteroid in asteroids[:]:
        ax,ay,size,asteroidImage,rotation,hit,hits = asteroid
        
        if not exploding and not hit and dist(175,mouseY,ax,ay) < size/2:
            Lives -= 1
            asteroid[5] = True
            if Lives == 0:
                exploding = True
                explosionFrame = 0

        
    if not exploding and keyPressed and key == ' ':
        if millis() - lastShot > fireRate:
            projectiles.append([195,mouseY+2])
            lastShot = millis()
            
    if not exploding:
        image(rocket,rocketX,mouseY,45,25)
    else:
        image(explosionFrames[explosionFrame], 175, mouseY, 60, 60)
        explosionFrame += 1
        
        if explosionFrame >= len(explosionFrames):
            explosionFrame = len(explosionFrames) - 1
            
#lives
    if Lives == 3:
        image(heart, 550,50,40,40)
        image(heart, 600,50,40,40)
        image(heart, 650,50,40,40)
    
    if Lives == 2:
        image(heart, 550,50,40,40)
        image(heart, 600,50,40,40)
    
    if Lives == 1:
        image(heart, 550,50,40,40)
 
 #Instruction Text
    if millis() - startTime < 20000:
            fill(255)
            textFont(SpaceAge32)
            textAlign(CENTER,CENTER)
            text("Destroy Asteroids with SPACEBAR",width/2,100)
 
 #Winner       
    if len(asteroids) == 0:
        rocketX += 15
        fill(255)
        textFont(SpaceAge100)
        textAlign(CENTER,CENTER)
        text("WINNER",width/2,height/2)
        return
        
            
#Game Over Text & Restart            
    if exploding:
        textFont(SpaceAge100)
        textAlign(CENTER,CENTER)
        text("GAME OVER", gameOverX, 400)
        
        if gameOverX > width/2:
            gameOverX -= 5 
            
        if gameOverX == width/2:
            textFont(SpaceAge72)
            text("RESTART", 600, restartY)
            
            if restartY > height/2+100:
                restartY -= 5
            
            if restartY == height/2+100:
                restartTextWidth = textWidth("RESTART")
                restartTextHeight = 50
                
                if (mouseX > 600-restartTextWidth/2 and mouseX < 600+restartTextWidth/2 and mouseY > restartY-restartTextHeight/2 and mouseY < restartY+restartTextHeight/2) and mousePressed:
                    currentState = Level_2
                    reset_game()
                    
def reset_game():
    global rocketY, exploding, explosionFrame, gameOverX, restartY, Lives
    rocketY = 400
    exploding = False
    explosionFrame = 0
    gameOverX = 1700
    restartY = 900
    Lives = 3
    asteroids.clear()
    setup_level2()
    draw_level2()
    
