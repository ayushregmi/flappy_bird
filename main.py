import random
import os
from re import I

try:
    import pygame
    from pygame import mixer
except:
    os.system("pip install pygame")
    import pygame
    from pygame import mixer

pygame.init()
mixer.init()
#Game Window
screen = pygame.display.set_mode((288, 624))
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("assets/icon.ico")
pygame.display.set_icon(icon)

#sound
# s = mixer.Sound("assets/sound.wav")
# mixer.music.load("assets/sound.wav")

#Images
background_1 = pygame.image.load("assets/background-day.png")
background_2 = pygame.image.load("assets/background-night.png")
bg_list = [background_1, background_2]
background = bg_list[0]

slider_list = [pygame.image.load("assets/slider_left.png"), pygame.image.load("assets/slider_right.png")]

base = pygame.image.load("assets/base.png")
game_over_icon = pygame.image.load("assets/gameover.png")
message = pygame.image.load("assets/message.png")
resume = pygame.image.load("assets/resume.png")
zero = pygame.image.load("assets/0.png")
one = pygame.image.load("assets/1.png")
two = pygame.image.load("assets/2.png")
three = pygame.image.load("assets/3.png")
four = pygame.image.load("assets/4.png")
five = pygame.image.load("assets/5.png")
six = pygame.image.load("assets/6.png")
seven = pygame.image.load("assets/7.png")
eight = pygame.image.load("assets/8.png")
nine = pygame.image.load("assets/9.png")

#Variables
base_x = 0
highscore = 0
clock = pygame.time.Clock()

flap = 0

if background == background_2:
	fps = 6
else:
	fps = 6


#Player
bird_blue = [
		pygame.image.load("assets/bluebird-downflap.png"), 
		pygame.image.load("assets/bluebird-midflap.png"), 
		pygame.image.load("assets/bluebird-upflap.png"),  
		pygame.image.load("assets/bluebird-midflap.png")
		]
bird_red = [
		pygame.image.load("assets/redbird-downflap.png"), 
		pygame.image.load("assets/redbird-midflap.png"), 
		pygame.image.load("assets/redbird-upflap.png"),  
		pygame.image.load("assets/redbird-midflap.png")
		]
bird_yellow = [
		pygame.image.load("assets/yellowbird-downflap.png"), 
		pygame.image.load("assets/yellowbird-midflap.png"), 
		pygame.image.load("assets/yellowbird-upflap.png"),  
		pygame.image.load("assets/yellowbird-midflap.png")
		]	

bird_list = [bird_blue, bird_red, bird_yellow]
	
bird = random.choice(bird_list)

player_height = 24
player_width = 34


#Pipes
pipe_1 =  pygame.image.load("assets/pipe-green-down.png"),	
pipe_2 =  pygame.image.load("assets/pipe-red-down.png"),
pipe_list = [pipe_1, pipe_2]
		
pipe = random.choice(pipe_list)
pipe_x = 288
pipe_y = random.randint(192, 410)


#Functions
def load_bg():
	screen.blit(background,(0,0))


def load_base():
	screen.blit(base,(base_x,512))


def update_screen():
	pygame.display.update()


def draw_bird(x, y, t, rotation):
	screen.blit(pygame.transform.rotate(bird[t % 3], rotation),(x, y))
	

def display_gameover():
	screen.blit(game_over_icon, (48, 178.5))


def display_number(img, x, y):
	screen.blit(img, (x, y))

def changeBird():
	global bird
	bird = bird_list[(bird_list.index(bird)+1) % len(bird_list)]

def changeBackground():
	global background
	background = bg_list[(bg_list.index(background) + 1) % len(bg_list)]

def changePipe():
	global pipe
	pipe = pipe_list[(pipe_list.index(pipe)+1) % len(pipe_list)]

def pause_menu():
	run_pause = True

	while run_pause:
		for event in pygame.event.get():
			#Exit
			if event.type == pygame.QUIT:
				global run_menu 
				global run
				global run_over
				run_menu = False
				run = False
				run_over = False
				run_pause = False

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					run_pause = False

			screen.blit(resume, (48, 285))
			update_screen()



def show_score(score, y):
	score_str = str(score)
	score_length = len(score_str)
	length = score_length * 24
	x = 144 - length/2
	
	for n in score_str:
		if ord(n) != ord('\n'):
			if int(n) == 0:
				display_number(zero, x, y)
				x += 24
			elif int(n) == 1:
				display_number(one, x, y)
				x += 16
			elif int(n) == 2:
				display_number(two, x, y)
				x += 24
			elif int(n) == 3:
				display_number(three, x, y)
				x += 24
			elif int(n) == 4:
				display_number(four, x, y)
				x += 24
			elif int(n) == 5:
				display_number(five, x, y)
				x += 24
			elif int(n) == 6:
				display_number(six, x, y)
				x += 24
			elif int(n) == 7:
				display_number(seven, x, y)
				x += 24
			elif int(n) == 8:
				display_number(eight, x, y)
				x += 24
			elif int(n) == 9:
				display_number(nine, x, y)
				x += 24


def draw_pipe(x, y):
	screen.blit(pipe[0], (x, y))
	screen.blit(pygame.transform.flip(pipe[0], 0, 1), (x, y-320-90))

def import_highscore():
	global highscore
	file = open("highscore.txt","r")
	
	for score in file:
		if int(highscore) < int(score):
			highscore = score
	file.close()

def drawSlider(index):
	screen.blit(slider_list[index], (250, 3))


import_highscore()


def collision(player_x, player_y, pipe_x, pipe_y, pipe_gap): #gap = 90
	if pipe_x <= player_x and player_x-34 <= pipe_x + 45:
		if player_y+24 >= pipe_y or player_y <= pipe_y - pipe_gap:
			return True
		else:
			return False
	else:
		return False


def update_highscore(score):
	file = open("highscore.txt","a+")
	file.write(str(score)+'\n')
	

def game_over():
	run_over = True
	# mixer.music.play()
	# s.play()
	while run_over:
		for event in pygame.event.get():
			#Exit
			if event.type == pygame.QUIT:
				global run_menu 
				global run
				run_menu = False
				run = False
				run_over = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					run_over = False
					run = False
		display_gameover()
		update_screen()


def play_game():
	global background
	global bird
	b_select = 0

	rotation = 0
	f = 0
	# background = random.choice([background_1, background_2])
	if background == background_2:
		fps = 240
	else:
		fps = 250
	global jump
	global player_y
	global player_speed
	global pipe_x
	global pipe_y
	global run
	global pipe
	# pipe = random.choice(pipe_list)
	

	pipe_x = 288
	pipe_y = random.randint(192, 410)

	player_x = 50
	player_y = 150
	player_speed = 1.2
	jump = False
	t = 0
	jump_lim = 0
	score = 0
	i = 0     
	initial_velocity = 0
	#Game Loop
	run = True
	inc_y = 0
	a = 0.00005
	while run:
     
		
		f += 1
		t += 1
		clock.tick(fps)
		for event in pygame.event.get():
			
			#Exit
			if event.type == pygame.QUIT:
				run = False
				global run_menu 
				run_menu  = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pause_menu()

				#Jump
				if event.key == pygame.K_SPACE:
					jump = True
					jump_lim = player_y-40
					initial_velocity = -0.003
					rotation = 45
					t  = 0
					a = -0.00006

		if jump:
			if player_y <= jump_lim:
				jump = False
				initial_velocity = 0.1
				t = 0
			else:
				player_y -= initial_velocity + (0.003-a)/2
				initial_velocity += (0.003-a) * t
				
		else:
			player_y += initial_velocity  + 0.008/2 
			initial_velocity += 0.0008 * t
			
    
		if background == background_1:
			flap = 20
		else:
			flap = 50
   
		#Border Collision
		if player_y >= 488:
			player_y = 488
			t = 3
			update_highscore(score)
			game_over()


		#Score
		if player_x == pipe_x + 34:
			score += 1


		#Pipe generation
		if pipe_x <= -52:
			pipe_x = 288
			pipe_y = random.randint(192, 410)
		else:
			pipe_x -= 1

		b_select += 1 if f % flap == 0 else 0
  
		if rotation <= -60:
			pass
		else:
			rotation -= 1 if f % 2 ==0 else 0
      
		#Loading images
		load_bg()
		draw_pipe(pipe_x, pipe_y)
		load_base()
		draw_bird(player_x, player_y, b_select, rotation)
		show_score(score, 100)
		update_screen()
  

		#Collision with pipe
		if collision(player_x+player_width, player_y, pipe_x, pipe_y, 95):
			game_over()
			update_highscore(score)


def main_menu():
	global run_menu
	run_menu = True
	global player_x
	global pipe_1

	mouse_pressed = False
	bird_pressed = False
	pipe_pressed = False
	slider_pressed = False

	t = 0
	b_select = 0

	while run_menu:
		t += 1
		if pygame.mouse.get_pressed(num_buttons=3)[0] :
			mouse_x , mouse_y = pygame.mouse.get_pos()
			bird_pressed = mouse_x >= 127 and mouse_x <= 127 + player_width and mouse_y >= 100 and mouse_y <= 100 + player_height
			slider_pressed = mouse_x >= 250 and mouse_x <= 250 + 32 and mouse_y >= 3 and mouse_y <= 3 + 32
			pipe_pressed = mouse_x >= 118 and mouse_x <= 118 + 52 and mouse_y >= 0 and mouse_y <= 0 + 70

			if (bird_pressed) or (slider_pressed) or pipe_pressed:
				mouse_pressed = True
				# print("change\n")
				# print(mouse_x, mouse_y)
		
			
		if mouse_pressed and not pygame.mouse.get_pressed(num_buttons = 3)[0]:
			mouse_pressed = False
			mouse_x , mouse_y = pygame.mouse.get_pos()

			bird_pressed = mouse_x >= 127 and mouse_x <= 127 + player_width and mouse_y >= 100 and mouse_y <= 100 + player_height
			slider_pressed = mouse_x >= 250 and mouse_x <= 250 + 32 and mouse_y >= 3 and mouse_y <= 3 + 32
			pipe_pressed = mouse_x >= 118 and mouse_x <= 118 + 52 and mouse_y >= 0 and mouse_y <= 0 + 70

			if bird_pressed :
				changeBird()
			elif slider_pressed:
				changeBackground()
			elif pipe_pressed:
				changePipe()
		
		if background == background_1:
			flap = 35
		else:
			flap = 100
		
		for event in pygame.event.get():
			#Exit
			if event.type == pygame.QUIT:
				run_menu = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run_menu = False
				else:
					play_game()
		
		b_select += 1 if t % flap ==0 else 0
		import_highscore()
		load_bg()
		load_base()
		screen.blit(message, (52, 178.5))
		show_score(highscore, 550)
		draw_bird(127, 100, b_select, 0)
		drawSlider(bg_list.index(background))
		# screen.blit(pygame.transform.scale(pygame.transform.flip(pipe[0], 0, 1), (10, 100)), (0, 0))
		screen.blit(pygame.transform.flip(pipe[0], 0, 1), (118, -250))
		update_screen()


main_menu()

