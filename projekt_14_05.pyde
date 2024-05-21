strokeR = 0
strokeG = 0
strokeB = 0

sliderXR = 1000
sliderYR = 50

sliderXG = 1000
sliderYG = 140

sliderXB = 1000
sliderYB = 230

sliderXStroke = 1000
sliderYStroke = 320

sliderLength = 200
sliderHeight = 40

sliderValueR = 0.5
sliderValueG = 0.5
sliderValueB = 0.5
sliderValueStroke = 0.5

stroke_weight = 1

def setup():
    global stroke_weight
    size(1280,720)
    background(255)
    strokeWeight(stroke_weight)
def draw() :
    global strokeR, strokeG, strokeB, sliderXR, sliderYR, sliderXG, sliderYG, sliderXB, sliderYB, sliderLenght, sliderHeight, sliderValueR, sliderValueG, sliderValueB,sliderValueStroke,sliderXStroke,sliderYStroke, stroke_weight
    
    noStroke()
    fill(255,0,0)  
    rect(50,50,100,100)
    fill(90,89,89)
    rect(200,50,100,100)
    
    fill(200)
    rect(sliderXR, sliderYR, sliderLength, sliderHeight)
    fill(150) 
    rect(sliderXR + sliderValueR * sliderLength, sliderYR, 10, sliderHeight)
    
    fill(strokeR, strokeG, strokeB)
    rect(1000,300,140,50)
    
    fill(200)
    rect(sliderXG, sliderYG, sliderLength, sliderHeight)
    fill(150) 
    rect(sliderXG + sliderValueG * sliderLength, sliderYG, 10, sliderHeight)
    
    fill(200)
    rect(sliderXB, sliderYB, sliderLength, sliderHeight)
    fill(150) 
    rect(sliderXB + sliderValueB * sliderLength, sliderYB, 10, sliderHeight)
    
    fill(200)
    rect(sliderXStroke, sliderYStroke, sliderLength, sliderHeight)
    fill(150) 
    rect(sliderXStroke + sliderValueStroke * sliderLength, sliderYStroke, 10, sliderHeight)
    
    fill(255,0,0)
    rect(950,50,40,40)
    fill(0,255,0)
    rect(950,140,40,40)
    fill(0,0,255)
    rect(950,230,40,40)
    
    stroke(strokeR, strokeG, strokeB)
    
    strokeR = 255 * sliderValueR
    strokeG = 255 * sliderValueG
    strokeB = 255 * sliderValueB
    stroke_weight = 15 * sliderValueStroke
    strokeWeight(stroke_weight)
    
    if mousePressed:
        line(mouseX,mouseY,pmouseX,pmouseY)
        
        if mouseX > sliderXR and mouseX < sliderXR + sliderLength and mouseY > sliderYR and mouseY < sliderYR + sliderHeight:
            sliderValueR = constrain((float)(mouseX - sliderXR) / sliderLength, 0, 1)
            
        if mouseX > sliderXG and mouseX < sliderXG + sliderLength and mouseY > sliderYG and mouseY < sliderYG + sliderHeight:
            sliderValueG = constrain((float)(mouseX - sliderXG) / sliderLength, 0, 1)
            
        if mouseX > sliderXB and mouseX < sliderXB + sliderLength and mouseY > sliderYB and mouseY < sliderYB + sliderHeight:
            sliderValueB = constrain((float)(mouseX - sliderXB) / sliderLength, 0, 1)
            
        if mouseX > sliderXStroke and mouseX < sliderXStroke + sliderLength and mouseY > sliderYStroke and mouseY < sliderYStroke + sliderHeight:
            sliderValueStroke = constrain((float)(mouseX - sliderXStroke) / sliderLength, 0, 1)
        
def mouseClicked():
    global strokeR, strokeG, strokeB, stroke_weight, sliderValueR, sliderValueG, sliderValueB
    if mouseX >= 50 and mouseX <= 150 and mouseY >= 50 and mouseY <= 150:
        background(255)
    
    if mouseX >= 200 and mouseX <= 300 and mouseY >= 50 and mouseY <= 150:
       sliderValueR = 1
       sliderValueG = 1
       sliderValueB = 1
    
