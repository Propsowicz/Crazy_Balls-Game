import pygame
import Player
import Enemy_1
import Enemy_2
import Enemy_3
import Enemy_4
import random
import Point
import HighScore
import WritingName

windowX = 800
windowY = 800
screen_window = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption("SQRBall by Propsowicz")
pygame.font.init()
text_font = pygame.font.SysFont("Arial", 60, bold = True)

# PLAYER CHARACTERISTICS
p_X = 170
p_Y = 400
radius = 7
velocity = 7
player_ball = Player.Player_ball(screen_window, windowX, windowY, radius, p_X, p_Y, velocity)



game_run= True
game_play = False
game_over = False
new_score_in_list = False
white = (255,255,255)
points = 0
high_score = HighScore.HighScore()
list_1 = ["_", "_", "_"]

write_name = WritingName.WriteName()


def start_screen():
    screen_window.fill((0, 0, 0))
    text_game_over_1 = text_font.render("HIGH SCORES:", False, white)
    screen_window.blit(text_game_over_1, (50, 20))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_name_1, False, white)
    screen_window.blit(text_game_over_1, (50, 90))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_sc_1, False, white)
    screen_window.blit(text_game_over_1, (600, 90))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_name_2, False, white)
    screen_window.blit(text_game_over_1, (50, 160))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_sc_2, False, white)
    screen_window.blit(text_game_over_1, (600, 160))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_name_3, False, white)
    screen_window.blit(text_game_over_1, (50, 230))
    text_game_over_1 = text_font.render(HighScore.HighScore().table_of_scores_sc_3, False, white)
    screen_window.blit(text_game_over_1, (600, 230))

    text_game_over_1 = text_font.render("PRESS SPACE TO PLAY", False, white)
    screen_window.blit(text_game_over_1, (100, 500))

    pygame.display.update()



def made_the_list():


    screen_window.fill((0, 0, 0))
    text_game_over = text_font.render("WOW!", False, white)
    screen_window.blit(text_game_over, (325, 200))
    text_game_over = text_font.render("YOU'VE JUST MADE THE LIST!", False, white)
    screen_window.blit(text_game_over, (27, 270))

    if points == 1:
        end = "POINT"
    else:
        end = "POINTS"

    text_game_over = text_font.render("YOU HAVE REACHED " + str(points) + " " + end, False, white)
    screen_window.blit(text_game_over, (25, 340))
    try:
        name = str(list_1[-3]) + str(list_1[-2]) + str(list_1[-1])
    except:
        name = "xxx"


    text_game_over = text_font.render("ENTER YOUR NAME:" , False, white)
    screen_window.blit(text_game_over, (50, 530))

    text_game_over = text_font.render(name, False, white)
    screen_window.blit(text_game_over, (50, 600))

    pygame.display.update()


def game_over_screen():
    screen_window.fill((0, 0, 0))
    text_game_over = text_font.render("GAME OVER", True, white)
    screen_window.blit(text_game_over, (250, 250))

    if points == 1:
        end = "POINT"
    else:
        end = "POINTS"

    text_game_over = text_font.render("YOU HAVE REACHED " + str(points) + " " + end, False, white)
    screen_window.blit(text_game_over, (25, 350))

    text_game_over = text_font.render("CLICK SPACE TO CONTINUE...", False, white)
    screen_window.blit(text_game_over, (35, 450))


    pygame.display.update()


def screen_update():
    screen_window.fill( (0,0,0))
    player_ball.screen()

    for enemy in list_of_enemies:
        enemy.screen(player_ball.X, player_ball.Y, list_of_point_rec[0].X, list_of_point_rec[0].Y)

    for pt in list_of_point_rec:
        pt.screen()







    pygame.display.update()






while game_run:
    key_pressed = pygame.key.get_pressed()
    list_of_enemies = [Enemy_1.Enemy_1(screen_window, windowX, windowY, p_X, p_Y, 10)]
    list_of_point_rec = [(Point.Point(screen_window, p_X, p_Y, windowX, windowY))]



    for event in pygame.event.get():
        if key_pressed[pygame.K_ESCAPE]:
            game_run = False
        if event.type == pygame.QUIT:
            game_run = False
        if key_pressed[pygame.K_SPACE]:
            game_play = True


    if game_play:
        while game_play:
            pygame.time.Clock().tick(30)
            key_pressed = pygame.key.get_pressed()

            # GAME QUITING ARGUMENTS

            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_play= False
                    player_ball.X = p_X
                    player_ball.Y = p_Y
                    del list_of_enemies[1:]
                    points = 0
                if event.type == pygame.QUIT:
                    game_play = False
                    game_run = False


            # COLLISION DETECTION - ENEMY

            for e in list_of_enemies:
                if (e.X + e.radius) in range(player_ball.X - radius, player_ball.X + radius) or (e.X - e.radius) in range(player_ball.X - radius, player_ball.X + radius) or e.X == player_ball.X:
                    if (e.Y + e.radius) in range(player_ball.Y - radius, player_ball.Y + radius) or (e.Y - e.radius) in range(player_ball.Y - radius, player_ball.Y + radius) or e.Y == player_ball.Y:

                        if high_score.get_score(points):
                            new_score_in_list = True
                            game_play = False
                            game_over = False
                        else:
                            game_over = True
                            game_play = False
                            new_score_in_list = False


        # COLLISION DETECTION - GET POINT
            rect_X_1 = list_of_point_rec[0].X - list_of_point_rec[0].rect_dim
            rect_X_2 = list_of_point_rec[0].X + list_of_point_rec[0].rect_dim
            rect_Y_1 = list_of_point_rec[0].Y - list_of_point_rec[0].rect_dim
            rect_Y_2 = list_of_point_rec[0].Y + list_of_point_rec[0].rect_dim

            if (player_ball.X + player_ball.radius) in range(rect_X_1, rect_X_2) or (player_ball.X - player_ball.radius) in range(rect_X_1, rect_X_2):
                if (player_ball.Y + player_ball.radius) in range(rect_Y_1, rect_Y_2) or (player_ball.Y - player_ball.radius) in range(rect_Y_1, rect_Y_2):
                    list_of_point_rec.append(Point.Point(screen_window, p_X, p_Y, windowX, windowY))
                    list_of_point_rec.pop(0)
                    # list_of_enemies.append(Enemy_1.Enemy_1(screen_window, windowX, windowY, p_X, p_Y, 10))


                    random_enemy =  random.choices([1, 2, 3, 4], weights=[60, 20, 10, 10], k = 1)
                    if random_enemy[0] == 1:
                        list_of_enemies.append(Enemy_1.Enemy_1(screen_window, windowX, windowY, p_X, p_Y, 10))
                    elif random_enemy[0] == 2:
                        list_of_enemies.append(Enemy_2.Enemy_2(screen_window, windowX, windowY, p_X, p_Y, 7))
                    elif random_enemy[0] == 3:
                        list_of_enemies.append(Enemy_3.Enemy_3(screen_window, windowX, windowY, p_X, p_Y, 15))
                    elif random_enemy[0] == 4:
                        list_of_enemies.append(Enemy_4.Enemy_4(screen_window, windowX, windowY, p_X, p_Y, 12))

                    points += 1
            player_ball.movement(key_pressed)
            screen_update()




    if game_over:
        while game_over:
            key_pressed = pygame.key.get_pressed()

            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    game_over = False
                if event.type == pygame.QUIT:
                    game_over = False
                    game_run = False
                if key_pressed[pygame.K_SPACE]:
                    game_over = False
                    player_ball.X = p_X
                    player_ball.Y = p_Y
                    del list_of_enemies[1:]
                    points = 0

            game_over_screen()




    if new_score_in_list:
        while new_score_in_list:
            key_pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if key_pressed[pygame.K_ESCAPE]:
                    new_score_in_list = False
                if event.type == pygame.QUIT:
                    new_score_in_list = False
                    game_run = False
                if key_pressed[pygame.K_SPACE]:
                    new_score_in_list = False
                    player_ball.X = p_X
                    player_ball.Y = p_Y
                    del list_of_enemies[1:]
                    name = str(list_1[-3]) + str(list_1[-2]) + str(list_1[-1])
                    high_score.add_new_score(name, points)
                    points = 0
                    list_1.pop()
                    list_1.pop()
                    list_1.pop()

                write_name.write_name(list_1, key_pressed)

            made_the_list()



    start_screen()
pygame.quit()

