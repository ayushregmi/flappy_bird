import pygame
import random
pygame.init()


#Game Window
screen = pygame.display.set_mode((288, 624))
pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load("assets/icon.ico")
pygame.display.set_icon(icon)


#Images
background_1 = pygame.image.load("assets/background-day.png")
background_2 = pygame.image.load("assets/background-night.png")
background = random.choice([background_2, background_1])
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

if background == background_2:
	fps = 6
else:
	fps = 1


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
bird = random.choice([bird_blue, bird_red, bird_yellow])

player_height = 24
player_width = 34


#Pipes
pipe_1 =  [
		pygame.image.load("assets/pipe-green-down.png"),
		pygame.image.load("assets/pipe-green-up.png")
		]
pipe_2 =  [
		pygame.image.load("assets/pipe-red-down.png"),
		pygame.image.load("assets/pipe-red-up.png")
		]

# pipe = random.choice([pipe_1, pipe_2])
pipe_x = 288
pipe_y = random.randint(192, 410)


#Functions
def load_bg():
	screen.blit(background,(0,0))


def load_base():
	screen.blit(base,(base_x,512))


def update_screen():
	pygame.display.update()


def draw_bird(x, y, t):
	screen.blit(bird[t % 3],(x, y))
	

def display_gameover():
	screen.blit(game_over_icon, (48, 178.5))


def display_number(img, x, y):
	screen.blit(img, (x, y))


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
	screen.blit(pipe[1], (x, y-320-90))


def import_highscore():
	global highscore
	file = open("highscore.txt","r")
	
	for score in file:
		if int(highscore) < int(score):
			highscore = score
	file.close()


import_highscore()


def collision(player_x, player_y, pipe_x, pipe_y, pipe_gap): #gap = 90
	if pipe_x <= player_x and player_x-34 <= pipe_x + 52:
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
	background = random.choice([background_1, background_2])
	bird = random.choice([bird_blue, bird_red, bird_yellow])
	if background == background_2:
		fps = 240
	else:
		fps = 240
	global jump
	global player_y
	global player_speed
	global pipe_x
	global pipe_y
	global run
	global pipe
	pipe = random.choice([pipe_1, pipe_2])
	

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
	#Game Loop
	run = True
	while run:
		
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
					i = 2

		if jump:
			if player_y <= jump_lim:
				jump = False
				i = 0
			else:
				player_y -= player_speed ** i
				i -= 0.11
		else:
			player_y += player_speed ** i
			i += 0.2
 		
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

		#Loading images
		load_bg()
		draw_pipe(pipe_x, pipe_y)
		load_base()
		draw_bird(player_x, player_y, t)
		show_score(score, 100)
		update_screen()

		#Collision with pipe
		if collision(player_x+player_width, player_y, pipe_x, pipe_y, 90):
			game_over()
			update_highscore(score)


def main_menu():
	global run_menu
	run_menu = True


	while run_menu:
		for event in pygame.event.get():
			
			#Exit
			if event.type == pygame.QUIT:
				run_menu = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					run_menu = False
				else:
					play_game()

		import_highscore()
		load_bg()
		load_base()
		screen.blit(message, (52, 178.5))
		show_score(highscore, 550)

		update_screen()


main_menu()

