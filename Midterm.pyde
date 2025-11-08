from Background import setup_stars, draw_stars
from Level_1 import setup_level1, draw_level1 
from Level_2 import setup_level2, draw_level2

START = 0
Level_1 = 1
Level_2 = 2
currentState = START
startTime = 0

def setup():
    global startTime, SpaceAge100
    size(1200,800)
    background(0)
    SpaceAge100 = createFont('/Users/milesphillips/Documents/Processing/Midterm/data/space age.ttf', 100)
    setup_stars()
    setup_level1()
    setup_level2()

    
    
def draw():
    global currentState
    background(0)
    draw_stars()
   
    if currentState == START:
        global SpaceAge100, currentState, rocket, startTime
        fill(255)
        textFont(SpaceAge100)
        textAlign(CENTER,CENTER)
        text("START",width/2,height/2)
        startTextWidth = textWidth("START")
        startTextHeight = 100
        if (mouseX > width/2-startTextWidth/2 and mouseX < width/2+startTextWidth/2 and mouseY > height/2-startTextHeight/2 and mouseY < height/2+startTextHeight/2) and mousePressed:
            currentState = Level_1
            startTime = millis()
    elif currentState == Level_1:
        draw_level1()
        if millis() - startTime > 25000:
            currentState = Level_2
    elif currentState == Level_2:
        draw_level2()
