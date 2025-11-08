stars = []

def setup_stars():
    #Adding values to Star list
    for i in range(100):
        x = random(width)
        y = random(height)
        stars.append([x,y])
        
        
def draw_stars():
    
    #Loading Star list and adding movement
    for star in stars:
        x,y = star
        stroke(255)
        circle(x,y,1)
        star[0] -= 1
        if star[0] < 0:
            star[0] = width
            star[1] = random(height)
