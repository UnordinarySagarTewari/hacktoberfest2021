import pygame,sys,random

#General Setup
pygame.init()
clock=pygame.time.Clock()

#Setting up Main Window
screen_width = 1000
screen_height = 640
size = (screen_width,screen_height) 
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PONG")
bg_image=pygame.image.load("bg4.PNG")

#Game Rectangles
ball=pygame.Rect(screen_width//2-15,screen_height//2-15,30,30)
player=pygame.Rect(screen_width -20,screen_height//2-70,10,140)
opponent=pygame.Rect(10,screen_height//2-70,10,140)

#Colors
bg_color=pygame.Color("grey12")
light_grey=(200,200,200)

#Speed
ball_speed_x=7
ball_speed_y=7
player_speed = 0
opponent_speed =7

#Game Animations
def ball_animation():
    global ball_speed_x,ball_speed_y,opponent_score,player_score,score_time
    ball.x+= ball_speed_x
    ball.y+= ball_speed_y

    if ball.top <=0 or ball.bottom >= screen_height:
        ball_speed_y*=-1
    if ball.left <=0:
        score_time=pygame.time.get_ticks()
        player_score+=1
    if ball.right >= screen_width:
        score_time=pygame.time.get_ticks()
        opponent_score+=1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1
def player_animation():
    player.y+=player_speed
    if player.top <= 0:
        player.y=0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def opponent_ai():
    if opponent.top <ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom > ball.y:
        opponent.top-=opponent_speed
    if opponent.top <= 0:
        opponent.y=0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
def ball_restart():
    global ball_speed_y,ball_speed_x,score_time

    current_time=pygame.time.get_ticks()
    ball.center=(screen_width//2,screen_height//2)

    if current_time -score_time<700:
        three=game_font.render("3",False,light_grey)
        screen.blit(three,(screen_width//2-16,screen_height//2-100))

    if 700<current_time -score_time<1400:
        three=game_font.render("2",False,light_grey)
        screen.blit(three,(screen_width//2-16,screen_height//2+48))

    if 1400<current_time -score_time<2100:
        three=game_font.render("1",False,light_grey)
        screen.blit(three,(screen_width//2-16,screen_height//2-100))

    if 2100<current_time -score_time<2500:
        three=game_font.render("START!!!",False,light_grey)
        screen.blit(three,(screen_width//2-120,screen_height//2+48))

    
    if current_time -score_time<2500:
        ball_speed_x,ball_speed_y=0,0
    else:
        ball_speed_y=7*random.choice((1,-1))
        ball_speed_x=7*random.choice((1,-1))
        score_time=None

#Text Variables
player_score=0
opponent_score=0
game_font=pygame.font.Font("freesansbold.ttf",64)

#Score_Timer
score_time=True #if u put it none at the first start it will be without counter

while True:
    #Handling Inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed-=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed+=7
                
    ball_animation()
    player_animation()
    opponent_ai()
    

    #Visuals
    screen.blit(bg_image,(0,0))
    pygame.draw.rect(screen,light_grey,player)
    pygame.draw.rect(screen,light_grey,opponent)
    #pygame.draw.circle(screen,light_grey,(screen_width//2,screen_height//2-15),15)
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.aaline(screen,light_grey,(screen_width//2,0),(screen_width//2,screen_height))

    if score_time:
        ball_restart()
    player_text=game_font.render(f"{player_score}",False,light_grey)
    screen.blit(player_text,(screen_width//2-64,screen_height//2-32))

    opponent_text=game_font.render(f"{opponent_score}",False,light_grey)
    screen.blit(opponent_text,(screen_width//2+32,screen_height//2-32))
    
    
    #Updating the Window
    pygame.display.flip()
    clock.tick(75)
