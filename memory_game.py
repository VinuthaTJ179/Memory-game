import pygame, sys
import random
#Sys module is used to import functions and variable for python in general
from pygame.locals import*


shapesarrangement = []


#To choose rectangles randomly
rectangles = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]




''' To create a rectangle object we define four coordinates they are left, top, width and height '''
Rectangle1 = Rect(0,0,100,100)
Rectangle2 = Rect(100,0,100,100)
Rectangle3 = Rect(200,0,100,100)
Rectangle4 = Rect(300,0,100,100)
Rectangle5 = Rect(0,100,100,100)
Rectangle6 = Rect(100,100,100,100)
Rectangle7 = Rect(200,100,100,100)
Rectangle8 = Rect(300,100,100,100)
Rectangle9 = Rect(0,200,100,100)
Rectangle10 = Rect(100,200,100,100)
Rectangle11 = Rect(200,200,100,100)
Rectangle12 = Rect(300,200,100,100)
Rectangle13 = Rect(0,300,100,100)
Rectangle14 = Rect(100,300,100,100)
Rectangle15 = Rect(200,300,100,100)
Rectangle16 = Rect(300,300,100,100)
'''Instead of adding all 16 triangles we just take them as a tuple and iterate through them'''
RectangleObjects = (Rectangle1,Rectangle2,Rectangle3,Rectangle4,Rectangle5,Rectangle6,Rectangle7,Rectangle8,Rectangle9,Rectangle10,Rectangle11,Rectangle12,Rectangle13,Rectangle14,Rectangle15,Rectangle16)

#We call a function to draw all 16 rectangles instead of calling them one by one
def drawBackground():
    for i in range(16):
        pygame.draw.rect(Window,(255,0,0),RectangleObjects[i],10)
'''To draw different shapes'''
def drawRecShapes(x,color):
    if x==1:
        pygame.draw.rect(Window,color,Rect(20,20,60,60))
    elif x==2:
        pygame.draw.rect(Window,color,Rect(120,20,60,60))
    elif x==3:
        pygame.draw.rect(Window,color,Rect(220,20,60,60))
    elif x==4:
        pygame.draw.rect(Window,color,Rect(320,20,60,60))
    elif x==5:
        pygame.draw.rect(Window,color,Rect(20,120,60,60))
    elif x==6:
        pygame.draw.rect(Window,color,Rect(120,120,60,60))
    elif x==7:
        pygame.draw.rect(Window,color,Rect(220,120,60,60))
    elif x==8:
        pygame.draw.rect(Window,color,Rect(320,120,60,60))
    elif x==9:
        pygame.draw.rect(Window,color,Rect(20,220,60,60))
    elif x==10:
        pygame.draw.rect(Window,color,Rect(120,220,60,60))
    elif x==11:
        pygame.draw.rect(Window,color,Rect(220,220,60,60))
    elif x==12:
        pygame.draw.rect(Window,color,Rect(320,220,60,60))
    elif x==13:
        pygame.draw.rect(Window,color,Rect(20,320,60,60))
    elif x==14:
        pygame.draw.rect(Window,color,Rect(120,320,60,60))
    elif x==15:
        pygame.draw.rect(Window,color,Rect(220,320,60,60))
    elif x==16:
        pygame.draw.rect(Window,color,Rect(320,320,60,60))

def drawCirShapes(x,color):
    if x==1:
        pygame.draw.circle(Window,color,(50,50),30)
    elif x==2:
        pygame.draw.circle(Window,color,(150,50),30)
    elif x==3:
        pygame.draw.circle(Window,color,(250,50),30)
    elif x==4:
        pygame.draw.circle(Window,color,(350,50),30)
    elif x==5:
        pygame.draw.circle(Window,color,(50,150),30)
    elif x==6:
        pygame.draw.circle(Window,color,(150,150),30)
    elif x==7:
        pygame.draw.circle(Window,color,(250,150),30)
    elif x==8:
        pygame.draw.circle(Window,color,(350,150),30)
    elif x==9:
        pygame.draw.circle(Window,color,(50,250),30)
    elif x==10:
        pygame.draw.circle(Window,color,(150,250),30)
    elif x==11:
        pygame.draw.circle(Window,color,(250,250),30)
    elif x==12:
       pygame.draw.circle(Window,color,(350,250),30)
    elif x==13:
        pygame.draw.circle(Window,color,(50,350),30)
    elif x==14:
        pygame.draw.circle(Window,color,(150,350),30)
    elif x==15:
        pygame.draw.circle(Window,color,(250,350),30)
    elif x==16:
        pygame.draw.circle(Window,color,(350,350),30)

def drawTriShapes(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,( (10,20),(90,20),(50,80) ))
    elif x==2:
        pygame.draw.polygon(Window,color,( (110,20),(190,20),(150,80) ))
    elif x==3:
        pygame.draw.polygon(Window,color,( (210,20),(290,20),(250,80) ))
    elif x==4:
        pygame.draw.polygon(Window,color,( (310,20),(390,20),(350,80) ))
    elif x==5:
        pygame.draw.polygon(Window,color,( (10,120),(90,120),(50,180) ))
    elif x==6:
        pygame.draw.polygon(Window,color,( (110,120),(190,120),(150,180) ))
    elif x==7:
        pygame.draw.polygon(Window,color,( (210,120),(290,120),(250,180) ))
    elif x==8:
        pygame.draw.polygon(Window,color,( (310,120),(390,120),(350,180) ))
    elif x==9:
        pygame.draw.polygon(Window,color,( (10,220),(90,220),(50,280) ))
    elif x==10:
        pygame.draw.polygon(Window,color,( (110,220),(190,220),(150,280) ))
    elif x==11:
        pygame.draw.polygon(Window,color,( (210,220),(290,220),(250,280) ))
    elif x==12:
       pygame.draw.polygon(Window,color,( (310,220),(390,220),(350,280) ))
    elif x==13:
        pygame.draw.polygon(Window,color,( (10,320),(90,320),(50,380) ))
    elif x==14:
        pygame.draw.polygon(Window,color,( (110,320),(190,320),(150,380) ))
    elif x==15:
        pygame.draw.polygon(Window,color,( (210,320),(290,320),(250,380) ))
    elif x==16:
        pygame.draw.polygon(Window,color,( (310,320),(390,320),(350,380) ))

def drawDiamShapes(x,color):
    if x==1:
        pygame.draw.polygon(Window,color,( (10,50),(50,20),(90,50),(50,80) ))
    elif x==2:
        pygame.draw.polygon(Window,color,( (110,50),(150,20),(190,50),(150,80) ))
    elif x==3:
        pygame.draw.polygon(Window,color,( (210,50),(250,20),(290,50),(250,80) ))
    elif x==4:
        pygame.draw.polygon(Window,color,( (310,50),(350,20),(390,50),(350,80) ))
    elif x==5:
        pygame.draw.polygon(Window,color,( (10,150),(50,120),(90,150),(50,180) ))
    elif x==6:
        pygame.draw.polygon(Window,color,( (110,150),(150,120),(190,150),(150,180) ))
    elif x==7:
        pygame.draw.polygon(Window,color,( (210,150),(250,120),(290,150),(250,180) ))
    elif x==8:
        pygame.draw.polygon(Window,color,( (310,150),(350,120),(390,150),(350,180) ))
    elif x==9:
        pygame.draw.polygon(Window,color,( (10,250),(50,220),(90,250),(50,280) ))
    elif x==10:
        pygame.draw.polygon(Window,color,( (110,250),(150,220),(190,250),(150,280) ))
    elif x==11:
        pygame.draw.polygon(Window,color,( (210,250),(250,220),(290,250),(250,280) ))
    elif x==12:
       pygame.draw.polygon(Window,color,( (310,250),(350,220),(390,250),(350,280) ))
    elif x==13:
        pygame.draw.polygon(Window,color,( (10,350),(50,320),(90,350),(50,380) ))
    elif x==14:
        pygame.draw.polygon(Window,color,( (110,350),(150,320),(190,350),(150,380) ))
    elif x==15:
        pygame.draw.polygon(Window,color,( (210,350),(250,320),(290,350),(250,380) ))
    elif x==16:
        pygame.draw.polygon(Window,color,( (310,350),(350,320),(390,350),(350,380) ))


def startGame():
    for i in range(4):
        if i==0 or i==1:
            color = (0,0,255)
        else:
            color = (0,255,0)
        #Choose a random position of the rectangle
        x = random.choice(rectangles)
        shapesarrangement.append(x)
        #Draw the shape and fill it with color
        drawRecShapes(x,color)
        #Remove the position once added to reduce duplicates
        rectangles.remove(x)


    for i in range(4):
        if i==0 or i==1:
            color = (255,255,0)
        else:
            color = (0,255,255)
        #Choose a random position of the rectangle
        x = random.choice(rectangles)
        shapesarrangement.append(x)
        #Draw the shape and fill it with color
        drawCirShapes(x,color)
        #Remove the position once added to reduce duplicates
        rectangles.remove(x)



    for i in range(4):
        if i==0 or i==1:
            color = (255,0,255)
        else:
            color = (128,0,0)
        #Choose a random position of the rectangle
        x = random.choice(rectangles)
        shapesarrangement.append(x)
        #Draw the shape and fill it with color
        drawTriShapes(x,color)
        #Remove the position once added to reduce duplicates
        rectangles.remove(x)


    for i in range(4):
        if i==0 or i==1:
            color = (128,128,0)
        else:
            color = (128,0,128)
        #Choose a random position of the rectangle
        x = random.choice(rectangles)
        shapesarrangement.append(x)
        #Draw the shape and fill it with color
        drawDiamShapes(x,color)
        #Remove the position once added to reduce duplicates
        rectangles.remove(x)

def rightchoice(firstchoice,secondchoice):
    x = shapeIndex(firstchoice)
    y = shapeIndex(secondchoice)
    if(x==0 and y==1 or x==1 and y==0)\
    or (x==2 and y==3 or x==3 and y==2)\
    or (x==4 and y==5 or x==5 and y==4)\
    or (x==6 and y==7 or x==7 and y==6)\
    or (x==8 and y==9 or x==9 and y==8)\
    or (x==10 and y==11 or x==11 and y==10)\
    or (x==12 and y==13 or x==13 and y==12)\
    or (x==14 and y==15 or x==15 and y==14):
        return True
        
def shapeIndex(mouse_position):
    for i in range(16):
        if RectangleObjects[i].collidepoint(mouse_position):
            return shapesarrangement.index(i+1)    

def recNumber(mouse_position):
    for i in range(16):
        if RectangleObjects[i].collidepoint(mouse_position):
            return i+1
        
def hide(mouse_position):
    rectangle_number = recNumber(mouse_position)
    for i in range(16):
        if rectangle_number == i+1:
            pygame.draw.rect(Window,(255,255,255),RectangleObjects[i].inflate(-10,-10))

def show(mouse_position):
    rectanglenumber = recNumber(mouse_position)
    shapeindex = shapeIndex(mouse_position)
    if shapeindex==0 or shapeindex==1:
        color = (0,0,255)
        drawRecShapes(rectanglenumber,color)
    elif shapeindex==2 or shapeindex==3:
        color = (0,255,0)
        drawRecShapes(rectanglenumber,color)
    elif shapeindex==4 or shapeindex==5:
        color = (255,255,0)
        drawCirShapes(rectanglenumber,color)
    elif shapeindex==6 or shapeindex==7:
        color = (0,255,255)
        drawCirShapes(rectanglenumber,color)
    elif shapeindex==8 or shapeindex==9:
        color = (255,0,255)
        drawTriShapes(rectanglenumber,color)
    elif shapeindex==10 or shapeindex==11:
        color = (128,0,0)
        drawTriShapes(rectanglenumber,color)
    elif shapeindex==12 or shapeindex==13:
        color = (128,128,0)
        drawDiamShapes(rectanglenumber,color)
    elif shapeindex==14 or shapeindex==15:
        color = (128,0,128)
        drawDiamShapes(rectanglenumber,color)



def main():
#Here we are initializing pygame modules
    pygame.init()
#Each game has window to displayed so we're declaring them as window
#We're making it global so that we can use them in other functions
    global Window
#Pygame's module to initialize the width and height of the window
#The values inside the brackets are height and width respectively
    Window = pygame.display.set_mode((410,410))
    #This function is used to give color to the pygame window
    Window.fill((244,194,194))
    #This function is used to give name for your window
    pygame.display.set_caption("Memory Game")
    #To draw the rectangle we have->
    '''It is a pygame module to draw different shapes,
    first parameter: the surface we need to draw our rectangle on
    second parameter: color of the shape
    third parameter: dimensions of the rectangle
    fourth paramter: thickness of the border'''
    '''pygame.draw.rect(Window,(255,0,0),Rectangle1,10)'''
    #Calling the function to draw all 16 boxes
    drawBackground()
    '''
    #To draw a circle we have->
    pygame.draw.circle(Window,(255,255,0),(50,50),30)
    #To draw a polygon we have->
    pygame.draw.polygon(Window,(255,0,255),((110,20),(190,20),(150,80)))
    #To draw another polygon with the specified vertices->
    pygame.draw.polygon(Window,(0,255,0),((210,50),(250,20),(290,50),(250,80)))
    #To draw shapes like rectangle, circle and diamond
    drawRecShapes(14,(0,0,0))'''
    startGame()



    #The color and caption won't work unless it is updated it is done using ->
    pygame.display.update()

    #Wait for 3 seconds for the user to reckon the objects
    pygame.time.wait(3000)

    #After this flush the window white
    Window.fill((255,255,255))

    #Draw just the background after
    drawBackground()

    #Update them again
    pygame.display.update()


    #Based on choices of the user choose the rectangles
    flag = 0
    truechoices = []


    #wait till user quits, this code will open the window until the user closes it  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                #exit()
                pygame.quit()
                sys.exit()
            #elif event.type == MOUSEBUTTONUP:
                #print("Mouse is clicked")
                #elif event.type == KEYUP:
                #print("Keyboard button is pressed")'''
            elif event.type == pygame.MOUSEBUTTONUP:
                #This get_pos() returns the x and y of where the user has clicked
                mouse_position = pygame.mouse.get_pos()
                #Show the shape in that particular mouse position
                show(mouse_position)
                #Update the screen after the previous display
                pygame.display.update()
                if flag == 0:
                    firstchoice = mouse_position
                    if recNumber(firstchoice) in truechoices: flag = 0
                    else: flag = 1
                else:
                    secondchoice = mouse_position
                    if recNumber(secondchoice) in truechoices: flag = 1
                    else: flag = 0
                    if not (recNumber(firstchoice) in truechoices) and not (recNumber(secondchoice) in truechoices):
                        if rightchoice(firstchoice,secondchoice):
                            truechoices.append(recNumber(firstchoice))  
                            truechoices.append(recNumber(secondchoice)) 
                        else:
                            pygame.time.wait(1000)
                            hide(firstchoice)
                            hide(secondchoice)
                            pygame.display.update()
        if len(truechoices) == 16:
            Font1 = pygame.font.SysFont('arial',22,True,True)
            Window.fill((255,255,255))
            textsurface = Font1.render("You Won!!",True,(0,0,0))
            Window.blit(textsurface,(150,150))
            '''image = pygame.image.load('task5.jpeg')
            Window.blit(image,(0,0))'''
            pygame.display.update()






if __name__ == "__main__":
#This is a standard method to call main functions in pygame
    main()
