asteroids = []
exploding = False
explosionFrame = 0
gameOverX = 1700
restartY = 900
Level_1 = 1
currentState = Level_1
Lives = 3
startTime = 0


def setup_level1():
    global rocket, explosionFrames, rocketY, SpaceAge100, SpaceAge72, heart, startTime, SpaceAge32
    imageMode(CENTER)
    
    rocket = loadImage("Rocket.png")
    startTime = millis()
    explosionFrames = []
    for i in range(20):
        explosionFrames.append(loadImage("Explosion"+str(i)+".png"))

#Load in Asteroid & Hearts
    asteroidImage = loadImage("Asteroid1.png")
    heart = loadImage("heart.png")
    
    for i in range(25):
        x = random(width)
        y = random(height)
        size = random(60,120)
        rotation = random(TWO_PI)
        hit = False
        asteroids.append([x,y,size,asteroidImage,rotation,hit])
        
    SpaceAge100 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 100)
    SpaceAge72 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 72)
    SpaceAge32 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 32)

def draw_level1():
    global rocketY, exploding, explosionFrame, SpaceAge100, gameOverX, SpaceAge72, restartY, Level_1, currentState, heart, Lives, rocket, startTime, SpaceAge32
    
        
#Loading Asteroids, Movement & Explosion
    for asteroid in asteroids:
        x,y,size,asteroidImage,rotation,hit = asteroid
        
        if not exploding:
            asteroid[0] -= 2
            if asteroid[0] < -60:
                asteroid[0] = 1300
                asteroid[1] = random(height)
       
        if not exploding:
            pushMatrix()
            translate(x,y)
            rotate(rotation)
            image(asteroidImage,0,0,size,size)
            popMatrix()
            asteroid[0] -= 1
            asteroid[4] += random(0.02,0.05)
        
        if exploding:
            pushMatrix()
            translate(x,y)
            rotate(rotation)
            image(asteroidImage,0,0,size,size)
            popMatrix()
            asteroid[0] -= 10
            asteroid[4] += random(0.02,0.05)
            
            if asteroid[0] < -50:
                asteroids.remove(asteroid)
        
        if asteroid[4] > TWO_PI:
            asteroid[4] -= TWO_PI
                
        if not exploding and not hit and dist(175,mouseY,x,y) < size/2:
            Lives -= 1
            asteroid[5] = True
            if Lives == 0:
                exploding = True
                explosionFrame = 0
            
#Rocket Explosion
    if not exploding:
        image(rocket,175,mouseY,45,25)
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

#Instructoin Text
    if millis() - startTime < 10000:
            fill(255)
            textFont(SpaceAge32)
            textAlign(CENTER,CENTER)
            text("Avoid the Asteroids",width/2,100)

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
                    currentState = Level_1
                    reset_game()
                    
def reset_game():
    global rocketY, exploding, explosionFrame, gameOverX, restartY, Lives
    rocketY = 400
    exploding = False
    explosionFrame = 0
    gameOverX = 1700
    restartY = 900
    Lives = 3
    asteroids = []
    setup_level1()
    draw_level1()
    
