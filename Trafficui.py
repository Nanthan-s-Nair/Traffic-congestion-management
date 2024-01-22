import pygame
import random
pygame.init()
fps = 60
WIDTH = 800 ; HEIGHT = 800
timer=pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('GAME')
bg_img = pygame.image.load('bg2.png')
bg_img = pygame.transform.scale(bg_img,(800,800))
cars=[]
for i in range(4):
    img=pygame.transform.scale(pygame.image.load(f'car{i+1}.png'),(46,25))
    cars.append(img)
class Car(pygame.sprite.Sprite) :
    choice=0
    def __init__(self,spawn_direction,turn_dir,ambu) :
        super().__init__()
        self.is_ambulance = ambu
        if self.is_ambulance:
            self.carimg=pygame.transform.scale(pygame.image.load("ambulance.png"),(69,38))
            self.image=self.carimg
        else:    
            self.choice=random.randint(0,3)
            self.carimg=cars[self.choice]
            self.image=self.carimg
        #0 - North, 1 - East, 2 - South, 3 - West
        self.displacement = 25
        self.s_dir = spawn_direction
        self.turn_dir = turn_dir
        self.notstopped = True
        self.image_update()
        self.turned = False
        
        self.rect = self.image.get_rect(center = (self.cx,self.cy))
        

        self.displace()
        
        self.next_dir = None
        self.type = None
        
    def image_update(self) :
        if self.s_dir == 0 :
            self.image = pygame.transform.rotate(self.carimg,-90)
            self.cx = WIDTH/2 ; self.cy = HEIGHT/8
            self.dx = 1
            self.dy = 1
        if self.s_dir == 1 :
            self.image = pygame.transform.rotate(self.carimg,180)
            self.cx = WIDTH*7/8 ; self.cy = HEIGHT/2
            self.dx = -1
            self.dy = 1
        if self.s_dir == 2 :
            self.image = pygame.transform.rotate(self.carimg,90)
            self.cx = WIDTH/2 ; self.cy = HEIGHT*7/8
            self.dx = 1
            self.dy = -1
        if self.s_dir == 3 :
            self.image = self.carimg
            
            self.cx = WIDTH/8 ; self.cy = HEIGHT/2
            self.dx = 1
            self.dy = 1

    def update(self) :
        #self.counter += 1
        self.move_flag = 1
        if self.s_dir == 0 :
            #if self.rect.bottom == HEIGHT : self.dy *= -1
            if not(self.notstopped and not signal0.state and self.rect.bottom == centerrect.top) :  
                projRect = self.image.get_rect(center = (self.rect.centerx,self.rect.centery + 20))
                for car in car_group :
                    if projRect.colliderect(car) :
                        if projRect.bottom > car.rect.top and projRect.bottom < car.rect.bottom :
                            self.move_flag = 0
                          
                
                if self.move_flag : self.rect.centery += self.dy

        if self.s_dir == 1 :
            #if self.rect.left == 0 : self.dx *= -1
            if not(self.notstopped and not signal1.state and self.rect.left == centerrect.right) : 
                projRect = self.image.get_rect(center = (self.rect.centerx-20,self.rect.centery))
                for car in car_group :
                    if projRect.colliderect(car) :
                        if projRect.left < car.rect.right and projRect.right > car.rect.right :
                            self.move_flag = 0
                if self.move_flag: self.rect.centerx += self.dx

        if self.s_dir == 2 :
            #if self.rect.top == 0 : self.dy *= -1
            if not(self.notstopped and not signal2.state and self.rect.top == centerrect.bottom) :
                projRect = self.image.get_rect(center = (self.rect.centerx,self.rect.centery - 20))
                for car in car_group :
                    if projRect.colliderect(car) :
                        if projRect.top < car.rect.bottom and projRect.bottom > car.rect.bottom :
                            self.move_flag = 0
                if self.move_flag: self.rect.centery += self.dy
                
        if self.s_dir == 3 :
            #if self.rect.right == WIDTH : self.dx *= -1
            if not(self.notstopped and not signal3.state and self.rect.right == centerrect.left) : 
                projRect = self.image.get_rect(center = (self.rect.centerx+20,self.rect.centery))
                for car in car_group :
                    if projRect.colliderect(car) :
                        if projRect.right > car.rect.left and projRect.left < car.rect.left :
                            self.move_flag = 0
                if self.move_flag: self.rect.centerx += self.dx

        self.turn()
        #print(self.rect.centerx,self.rect.centery)

    def inner_image_update(self) :
            self.notstopped = False
            self.s_dir = self.turn_dir
            self.image_update()
            if self.s_dir == 0:
                self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))
            if self.s_dir == 1:
                self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))
            if self.s_dir == 2:
                self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))
            if self.s_dir == 3:
                self.rect = self.image.get_rect(center = (WIDTH/2,HEIGHT/2))
            self.displace()


    def turn(self) :
        

        if self.s_dir == 0 or self.s_dir == 2 :
            if self.rect.centery == HEIGHT/2:
                self.inner_image_update()
        if self.s_dir == 1 or self.s_dir == 3 :
            if self.rect.centerx == WIDTH/2:
                self.inner_image_update()
        

        
    
    def displace(self) :
        if self.s_dir == 0 : self.rect.centerx += self.displacement
        if self.s_dir == 1 : self.rect.centery += self.displacement
        if self.s_dir == 2 : self.rect.centerx -= self.displacement
        if self.s_dir == 3 : self.rect.centery -= self.displacement


class Signal(pygame.sprite.Sprite) :
    def __init__(self,dir,xy) :
        super().__init__()
        self.direction = dir
        #0 - stop | 1 - go
        self.state = 0
        self.redstate = (255,0,0)
        self.greenstate = (0,0,0)
        self.xlen = 50
        self.ylen = 100
        
        self.x = xy[0] ; self.y = xy[1]
        

    def update(self) :
        self.draw_circle()
        #print("yes")
        
        if count == self.direction : 
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.update_state(0)
            if keys[pygame.K_DOWN]:
                self.update_state(1)

        
    def update_state(self,state) :
        
        self.state = state
        
        if self.state == 1 : 
            self.redstate = (0,0,0) ; self.greenstate = (0,255,0)
        if self.state == 0 : 
            self.redstate = (255,0,0) ; self.greenstate = (0,0,0)

    def draw_circle(self) :
        pygame.draw.circle(screen, self.redstate, (self.x + self.xlen/2,self.y + self.ylen/4), self.xlen/2)
        pygame.draw.circle(screen, self.greenstate, (self.x + self.xlen/2,self.y + self.ylen*3/4), self.xlen/2)
        if count == self.direction : pygame.draw.rect(screen,(255,255,0), (self.x-10,self.y-10,self.xlen+20,self.ylen+20),2)







centerrect = pygame.Rect(WIDTH/2 - 45, HEIGHT/2 - 45, 90,90)
    

#signal2 = Signal(2)
signal0 = Signal(0,(500,100))
signal1 = Signal(1,(500,500))
signal2 = Signal(2,(100,500))
signal3 = Signal(3,(100,100))
car0 = Car(2,3,False)




car_group = pygame.sprite.Group()
signal_group = pygame.sprite.Group()
#car_group.add(car0)
#car_group.add(Car(1,0))
#car_group.add(Car(3,2))
#car_group.add(Car(0,3))
#car_group.add(Car(0,1))

signal_group.add(signal0)
signal_group.add(signal1)
signal_group.add(signal2)
signal_group.add(signal3)

signal_list = [signal0,signal1,signal2,signal3]

cars_no = [0,0,0,0]


count = 0
green_signal = 0
there_is_a_car = False
there_is_an_ambulance = False

#signals = [signal0,signal1,signal2,signal3]
def get_car_number() :
    for car in car_group :
        if car.notstopped :
            cars_no[car.s_dir] += 1
    return cars_no.index(max(cars_no))

def check_signal() :
    global green_signal
    global there_is_a_car
    global there_is_an_ambulance
    there_is_a_car = False
    there_is_an_ambulance = False
    for car in car_group :
        if car.s_dir == green_signal and car.notstopped :
            there_is_a_car = True

        if car.is_ambulance and car.notstopped : 
            green_signal = car.s_dir
            there_is_an_ambulance = True
    
    if there_is_an_ambulance : 
        signal_list[0].update_state(0)
        signal_list[1].update_state(0)
        signal_list[2].update_state(0)
        signal_list[3].update_state(0)
        signal_list[green_signal].update_state(1)
    
    elif there_is_a_car == False :
        signal_list[green_signal].update_state(0)
        green_signal = get_car_number()
        signal_list[green_signal].update_state(1)





def add_cars() :
    f = 100
    x,y = pygame.mouse.get_pos()
    if x <WIDTH/2 + f/2 and x  > WIDTH/2 - f/2 and y < f and y > 0 :
        car_group.add(Car(0,random.randint(0,3),False))

    if x <WIDTH/2 + f/2 and x  > WIDTH/2 - f/2 and y < HEIGHT and y > HEIGHT-f :
        car_group.add(Car(2,random.randint(0,3),False))

    if x <f and x  > 0   and y > HEIGHT/2 - f/2 and y < HEIGHT/2 + f/2 :
        car_group.add(Car(3,random.randint(0,3),False))

    if x > WIDTH-f and x < WIDTH and y > HEIGHT/2 - f/2 and y < HEIGHT/2 + f/2:
        car_group.add(Car(1,random.randint(0,3),False))

def add_ambulance() :
    f = 100
    x,y = pygame.mouse.get_pos()
    if x <WIDTH/2 + f/2 and x  > WIDTH/2 - f/2 and y < f and y > 0 :
        car_group.add(Car(0,random.randint(0,3),True))

    if x <WIDTH/2 + f/2 and x  > WIDTH/2 - f/2 and y < HEIGHT and y > HEIGHT-f :
        car_group.add(Car(2,random.randint(0,3),True))

    if x <f and x  > 0   and y > HEIGHT/2 - f/2 and y < HEIGHT/2 + f/2 :
        car_group.add(Car(3,random.randint(0,3),True))

    if x > WIDTH-f and x < WIDTH and y > HEIGHT/2 - f/2 and y < HEIGHT/2 + f/2:
        car_group.add(Car(1,random.randint(0,3),True))

def lines():
    #middleline
    pygame.draw.line(screen, (255,0,0), (WIDTH/2,0), (WIDTH/2,HEIGHT), 2)
    pygame.draw.line(screen, (255,0,0), (0,HEIGHT/2), (WIDTH,HEIGHT/2), 2)
    #borderline
    pygame.draw.line(screen, (0,0,255), (WIDTH/2 + displacement,0), (WIDTH/2 + displacement,HEIGHT), 2)
    pygame.draw.line(screen, (0,0,255), (0,HEIGHT/2 + displacement), (WIDTH,HEIGHT/2 + displacement), 2)
    pygame.draw.line(screen, (0,0,255), (WIDTH/2 - displacement,0), (WIDTH/2 - displacement,HEIGHT), 2)
    pygame.draw.line(screen, (0,0,255), (0,HEIGHT/2 - displacement), (WIDTH,HEIGHT/2 - displacement), 2)
    #centerrect
    pygame.draw.rect(screen,(255,0,255), (WIDTH/2 - 45, HEIGHT/2 - 45, 90, 90),2)

run = True
#signal0.update_state(1)
while run :
    timer.tick(fps)
    screen.fill((64,64,64))
    displacement = 30
    screen.blit(bg_img,(0,0))

    #lines()
 

    car_group.draw(screen)
    #signal_group.draw(screen)
    
    for event in pygame.event.get() :
        if event.type==pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT :
                count -= 1
                count %= 4
            if event.key == pygame.K_RIGHT :
                count += 1
                count %= 4
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 :
                add_cars()
            if event.button == 3:
                add_ambulance()
        
        
    
    car_group.update()
    signal_group.update()
    check_signal()
    pygame.display.flip()

pygame.quit()