import pygame, math, random, time
pygame.init()
pygame.mixer.init()
#pygame.mixer.music.load("thrust.mp3")

bulletSound = pygame.mixer.Sound('bullet.wav')
thrustSound = pygame.mixer.Sound('thrust.wav')
crushSound = pygame.mixer.Sound('cannon.wav')

music = pygame.mixer.music.load('starship_soundtrack.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(.5)

width = 640
height = 480
size = [width,height]
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Starship')
background_image = pygame.image.load("cosmos.jpg").convert()
background_speed = 0
n = 0
speed_step = 0.005
projectile_speed = 1
drag = 0#0.001
ship_image = []
ship_rect = []
ship_images = ['sp_R.png',
               'sp_L.png',
               'sp_U.png',
               'sp_D.png',
               'sp_RT.png',
               'sp_LT.png',
               'sp_UT.png',
               'sp_DT.png',
               ]
for i in ship_images:
    ship_image.append(pygame.image.load(i))
    

player_img = pygame.image.load("sp_R.png")
player_rect = player_img.get_rect()
player_rect2 = pygame.Rect(0,0,40,40)
projectile_image = pygame.image.load("light.png")
asteroid_image = pygame.image.load("asteroid1.png")
asteroid_rect = asteroid_image.get_rect()
asteroid_rect2 = pygame.Rect(0,0,100,100)
projectile_rect = pygame.Rect(0,0,16,16)

asteroid_count = 0
lives = 2
crush_counter = 1000

crash_image = pygame.image.load("crash.png")

font = pygame.font.SysFont("Stencil", 15)
font2 = pygame.font.SysFont("Stencil", 30)
clock = pygame.time.Clock()
a = int(width/2)
b = int(height/2)



class Ship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #self.size = size
        self.colour = (0, 0, 0)
        self.thickness = 0
        self.speed = 0
        self.angle = 0
        self.Xspeed = 0
        self.Yspeed = 0
        #self.rect = ship_image[0].get_rect()
        #ship_rect = ship_image[0].get_rect()

    def display(self):
        #pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.size, self.thickness)
        #screen.blit(ship_image,[int(self.x), int(self.y)])
        pass
        

    def move(self):
        #self.x += (math.sin(self.angle) * self.speed)
        #self.y -= (math.cos(self.angle) * self.speed)
        self.x += self.Xspeed
        #self.rect.x += self.Xspeed
        self.y += self.Yspeed

    def inf(self):
        if self.x > width+10:
            self.x = -80
            #self.angle = - self.angle
        elif self.x < -80:
            self.x = width+10
            #self.angle = - self.angle
        if self.y > height+10:
            self.y = -80
            #self.angle = math.pi - self.angle
        elif self.y < -80:
            self.y = height+10
            #self.angle = math.pi - self.angle


            
class Projectile(object):
    def __init__(self,x,y,radius,color, Xspeed, Yspeed):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.Xspeed = Xspeed
        self.Yspeed = Yspeed
        self.p_rect = projectile_rect

    def draw(self,screen):
        #pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
        screen.blit(projectile_image,[int(self.x), int(self.y)])
        self.p_rect.x = int(self.x)
        self.p_rect.y = int(self.y)
        #pygame.draw.rect(screen, [102, 255, 255], self.p_rect, 1)
        
        
                
    def move(self):
        #self.x += (math.sin(self.angle) * self.speed)
        #self.y -= (math.cos(self.angle) * self.speed)
        #self.x += self.Xspeed * projectile_speed
        #self.x -= drag
        self.x += self.Xspeed * projectile_speed
        self.y += self.Yspeed * projectile_speed
        

        
class Asteroid(Ship):
    def __init__(self, x, y, Xspeed, Yspeed):
        super().__init__(x, y)
        self.Xspeed = Xspeed
        self.Yspeed = Yspeed

    def draw(self,screen):
        #pygame.draw.circle(screen, self.color, (self.x,self.y), self.radius)
        screen.blit(asteroid_image,[int(self.x), int(self.y)])
        asteroid_rect = asteroid_image.get_rect()
        
    def inf(self):
        if self.x > width+10:
            self.x = -120
            #self.angle = - self.angle
        elif self.x < -120:
            self.x = width+10
            #self.angle = - self.angle
        if self.y > height+10:
            self.y = -120
            #self.angle = math.pi - self.angle
        elif self.y < -120:
            self.y = height+10
            #self.angle = math.pi - self.angle

        
            
screen.blit(background_image, [0, 0])

ship = Ship(a-40, b-40)
ship.speed = 0
ship.angle = math.radians(90)
#my_first_ship.display()
#bullet = projectile(a,b,3,(255,255,0))

projectiles = []
projectile_visible = False

asteroids = []
asteroid1 = Asteroid((random.randint(50, 450)),(random.randint(50, 450)),random.uniform(-.3, .3),random.uniform(-.3, .3))
asteroid_rect.x = asteroid1.x
for i in range(2):
    asteroids.append(Asteroid(random.randint(50, 450),random.randint(50, 450),random.uniform(-.5, .5),random.uniform(-.5, .5)))


#asteroid_rect = asteroid_image.get_rect()
#projectile_rect = projectile_image.get_rect()
#rect1.colliderect(rect2)
pygame.display.flip()

#pygame.time.delay(1000)

running = True
#pygame.time.delay(10000)
#pygame.quit()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                #ship.Xspeed -= speed_step
                n = 5
                thrustSound.play()
            if event.key == pygame.K_RIGHT:
                #ship.Xspeed += speed_step
                n = 4
                thrustSound.play()
            if event.key == pygame.K_UP:
                #ship.Yspeed -= speed_step
                n = 6
                thrustSound.play()
            if event.key == pygame.K_DOWN:
                #ship.Yspeed += speed_step
                n = 7
                thrustSound.play()
            if event.key == pygame.K_SPACE:
                bulletSound.play()
                
                if n == 5 or n == 1:
                    #bullet.Xspeed = -1
                    #bullet.Yspeed = 0
                    projectiles.append(Projectile(ship.x+32,ship.y+32,3,(255,255,0),-1,0))
                if n == 4 or n == 0:
                    #bullet.Xspeed = 1
                    #bullet.Yspeed = 0
                    projectiles.append(Projectile(ship.x+32,ship.y+32,3,(255,255,0),1,0))
                    
                if n == 6 or n == 2:
                    #bullet.Yspeed = -1
                    #bullet.Xspeed = 0
                    projectiles.append(Projectile(ship.x+32,ship.y+32,3,(255,255,0),0,-1))
                if n == 7 or n == 3:
                    #bullet.Yspeed = 1
                    #bullet.Xspeed = 0
                    projectiles.append(Projectile(ship.x+32,ship.y+32,3,(255,255,0),0,1))
            
                projectile_visible = True
                
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #ship.Xspeed -= speed_step
                n = 1
                thrustSound.stop()
            if event.key == pygame.K_RIGHT:
                #ship.Xspeed += speed_step
                n = 0
                thrustSound.stop()
            if event.key == pygame.K_UP:
                #ship.Yspeed -= speed_step
                n = 2
                thrustSound.stop()
            if event.key == pygame.K_DOWN:
                n = 3
                thrustSound.stop()
                
    keys_pressed = pygame.key.get_pressed()
    
    
    if keys_pressed[pygame.K_LEFT]:
        ship.Xspeed -= speed_step
       
    if keys_pressed[pygame.K_RIGHT]:
        ship.Xspeed += speed_step
        
    if keys_pressed[pygame.K_UP]:
        ship.Yspeed -= speed_step

    if keys_pressed[pygame.K_DOWN]:
        ship.Yspeed += speed_step

            
    screen.blit(background_image, [0, 0])
    
    rel_x = background_speed % background_image.get_rect().width
    screen.blit(background_image, [rel_x-background_image.get_rect().width, 0])
    if rel_x < 640:
        screen.blit(background_image, [rel_x, 0])
    background_speed -= .1
    
    #asteroid1.display()
    asteroid1.draw(screen)
    asteroid1.move()
    asteroid1.inf()
    asteroid_rect.x = asteroid1.x
    asteroid_rect.y = asteroid1.y
    asteroid_rect2.x = asteroid1.x+10
    asteroid_rect2.y = asteroid1.y+10

    
    #ship.display()
    player_rect.x = ship.x
    player_rect.y = ship.y
    player_rect2.x = ship.x+20
    player_rect2.y = ship.y+20
    screen.blit(ship_image[n],[int(ship.x), int(ship.y)])
    ship.move()
    ship.inf()
    if ship.Xspeed > 0:
        ship.Xspeed -= drag
    if ship.Xspeed < 0:
        ship.Xspeed += drag
    if ship.Yspeed > 0:
        ship.Yspeed -= drag
    if ship.Yspeed < 0:
        ship.Yspeed += drag
            
    #projectile.display()
    if projectile_visible:
        for projectile in projectiles:
            projectile.draw(screen)
            projectile.move()
            
            
            projectile_collide = projectile.p_rect.colliderect(asteroid_rect2)
            if projectile_collide:
                crushSound.play()
                crashhx,crashhy = projectile.x-35, projectile.y-35
                screen.blit(crash_image,[crashhx,crashhy])
                projectile.x, projectile.y = -200,-200
                asteroid1.x, asteroid1.y = (20, 240)
                asteroid1 = Asteroid(random.randint(50, 450),random.randint(50, 450),random.uniform(-.3, .3),random.uniform(-.3, .3))
                crush_counter = 300                
                asteroid_count += 1
                screen.blit(text4, [10, 10])
                screen.blit(text5, [10, 30])
                pygame.display.flip()
                time.sleep(0.2) 

    
    
    crush_active = True      
                                        
    
    text = font.render('X Speed: ' + str(round(ship.Xspeed, 2)), True, (102, 255, 255))
    text2 =font.render('Y Speed: ' + str(round(ship.Yspeed, 2)), True, (102, 255, 255))
    text4 =font.render('Destroyed asteroids: ' + str(asteroid_count), True, (102, 255, 255))
    text5 =font.render('Lives: ' + str(lives), True, (102, 255, 255))
    text3 =font.render('Starship coordinates: ' + str(round(int(ship.x),2)) +'  '+  str(round(int(ship.y),2)), True, (102, 255, 255))
    text6 =font.render('No crush: ' + str(crush_counter), True, (102, 255, 255))
    text_game_over = font2.render('GAME OVER!!!', True, (102, 255, 255))
    #text3 =font.render('Coordinates: ' + str(round(asteroid1_rect.x, 2)), True, (102, 255, 255))
    #text = font.render(, True, clr)
    
    #stats:
    #screen.blit(text, [320, 30])
    #screen.blit(text2, [320, 50])
    #screen.blit(text3, [320, 10])
    
    screen.blit(text4, [10, 10])
    screen.blit(text5, [10, 30])
    #screen.blit(text6, [10, 50])
    
    if crush_counter > 0:
        crush_active = False
        #screen.blit(text6, [10, 50])
        crush_counter -= 1
       
    
    if crush_active:
        collide = player_rect2.colliderect(asteroid_rect2)
        if collide:
            pygame.display.flip()
            crushSound.play()
            crashx,crashy = ship.x-10, ship.y-10
            screen.blit(crash_image,[crashx,crashy])
            asteroid1 = Asteroid(random.randint(50, 450),random.randint(50, 450),random.uniform(-.3, .3),random.uniform(-.3, .3))
            asteroid1.x, asteroid1.y = (20, 240)
            ship.x, ship.y = (280, 200)
            ship.Xspeed, ship.Yspeed = (0,0)
            lives -= 1
            pygame.display.flip()
            time.sleep(0.5)

    if lives < 0:
        #screen.blit(text6, [10, 70])
        ship.Xspeed, ship.Yspeed = (0,0)
        asteroid1.Xspeed, asteroid1.Yspeed = (0,0)
        screen.blit(background_image, [0, 0])
        screen.blit(text_game_over, [240, 220])
        pygame.display.flip()
        
        
    
    pygame.display.flip()
    clock.tick(250)
pygame.quit()
