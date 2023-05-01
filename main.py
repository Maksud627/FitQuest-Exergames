import pygame
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import jjtodino_
import bctopinball
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
from pygame.locals import *
import pylab
import random
from copy import deepcopy
import csv
import plot
import pinball_plot

# # Initialize Pygame
# pygame.init()
#
# # Set window size and title
# WINDOW_WIDTH = 400
# WINDOW_HEIGHT = 200
# WINDOW_TITLE = "Two Buttons"
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption(WINDOW_TITLE)
#
# # Define colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GRAY = (128, 128, 128)
#
# # Define font
# font = pygame.font.Font(None, 36)
#
# # Define button size and position
# BUTTON_WIDTH = 150
# BUTTON_HEIGHT = 50
# BUTTON_SPACING = 50
# BUTTON_TOP = WINDOW_HEIGHT // 2 - BUTTON_HEIGHT // 2
# BUTTON_LEFT_1 = WINDOW_WIDTH // 2 - BUTTON_WIDTH - BUTTON_SPACING // 2
# BUTTON_LEFT_2 = WINDOW_WIDTH // 2 + BUTTON_SPACING // 2
#
# # Create button surfaces and rectangles
# button1_surface = font.render("Button 1", True, WHITE)
# button2_surface = font.render("Button 2", True, WHITE)
# button1_rect = pygame.Rect(BUTTON_LEFT_1, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)
# button2_rect = pygame.Rect(BUTTON_LEFT_2, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)
#
# # Game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             # Quit the game when the close button is clicked
#             pygame.quit()
#             quit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             # Check if a button is clicked
#             if button1_rect.collidepoint(event.pos):
#                 print("Button 1 clicked!")
#                 # webbrowser.open("https://chromedino.com/")
#                 # webbrowser.open("chrome://dino")
#                 driver = webdriver.Chrome()
#                 # driver.get("chrome://dino")
#                 # driver.quit()
#
#
#                 try:
#                     # os.system("python jjtodino.py")
#                     subprocess.run(["python", "jjtodino.py"], check=True)
#                     # driver.get("chrome://dino")
#                     driver.get("google.com")
#                     # driver.quit()
#                 except WebDriverException or subprocess.CalledProcessError:
#                     pass
#
#                 driver.quit()
#
#                 # try:
#                 #     proc = subprocess.Popen(["python", "jjtodino.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#                 #     output, error = proc.communicate()
#                 #     if error:
#                 #         raise Exception(error)
#                 #     # navigate to the desired URL after the Python script finishes
#                 #     driver.get("chrome://dino")
#                 # except Exception as e:
#                 #     print("Error running script:", e)
#                 #
#                 # driver.quit()
#
#             elif button2_rect.collidepoint(event.pos):
#                 print("Button 2 clicked!")
#
#     # Fill the screen with gray color
#     screen.fill(GRAY)
#
#     # Draw the buttons
#     pygame.draw.rect(screen, BLACK, button1_rect)
#     pygame.draw.rect(screen, BLACK, button2_rect)
#     screen.blit(button1_surface, button1_rect.move(10, 10))
#     screen.blit(button2_surface, button2_rect.move(10, 10))
#
#     # Update the screen
#     pygame.display.update()
# calorie list

last_game_calories = 0.0
last_game_jumps = 0
last_game_squats = 0


analytics_list1 = []
analytics_list2 = []
analytics_list3 = []

pinball_analytics1 = []
pinball_analytics2 = []
pinball_analytics3 = []

global flag, flag2
global total_calories, max_calories, max_jumps, max_squats, pinball_total_calories, pinball_max_calories, max_left_reps, max_right_reps

def run_chrome():
    # Initialize Pygame
    pygame.init()

    # Set window size and title
    WINDOW_WIDTH = 1600
    WINDOW_HEIGHT = 900
    WINDOW_TITLE = "Two Buttons"
    screen1 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    # Define colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)

    # Define font
    font = pygame.font.Font(None, 36)

    # # Define button size and position
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 50
    BUTTON_SPACING = 50
    BUTTON_TOP = WINDOW_HEIGHT // 2 - BUTTON_HEIGHT // 2
    # BUTTON_LEFT_1 = WINDOW_WIDTH // 2 - BUTTON_WIDTH - BUTTON_SPACING // 2
    # BUTTON_LEFT_2 = WINDOW_WIDTH // 2 + BUTTON_SPACING // 2

    BUTTON_LEFT_3 = WINDOW_WIDTH // 2 - BUTTON_WIDTH - BUTTON_SPACING // 2
    BUTTON_LEFT_4 = WINDOW_WIDTH // 2 + BUTTON_SPACING // 2
    #
    # # Create button surfaces and rectangles
    # button1_surface = font.render("Play Dino", True, WHITE)
    # button2_surface = font.render("Play Pinball", True, WHITE)
    # button1_rect = pygame.Rect(BUTTON_LEFT_1, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)
    # button2_rect = pygame.Rect(BUTTON_LEFT_2, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)

    # button3_surface = font.render("View Analytics", True, WHITE)
    # button4_surface = font.render("Quit", True, WHITE)
    # button3_rect = pygame.Rect(BUTTON_LEFT_3, BUTTON_TOP+200, BUTTON_WIDTH, BUTTON_HEIGHT)
    # button4_rect = pygame.Rect(BUTTON_LEFT_4, BUTTON_TOP+200, BUTTON_WIDTH, BUTTON_HEIGHT)

    current_screen = screen1
    current_screen_title = "Screen 1"

    # Header Bar Infos
    header_height = 70
    header_height1 = 140
    header_color = (154, 205, 50)


    # Create a Pygame surface for the header bar
    header_surface = pygame.Surface((WINDOW_WIDTH, header_height1))
    header_surface.fill(header_color)
    dino_header_surface = pygame.Surface((WINDOW_WIDTH, header_height))
    dino_header_surface.fill(header_color)
    pinball_header_surface = pygame.Surface((WINDOW_WIDTH, header_height))
    pinball_header_surface.fill(header_color)

    # Load the logo image
    logo_image = pygame.image.load('images/fitquest_logo.PNG')
    dino_header = pygame.image.load('images/dino_header.PNG')
    pinball_header = pygame.image.load('images/pinball_header.PNG')

    # Resize the logo image to fit within the header bar
    logo_width = int(header_height1 * 3.8)
    logo_height = int(logo_image.get_height() * (logo_width / logo_image.get_width()))
    logo_image = pygame.transform.scale(logo_image, (logo_width, logo_height))

    dino_header_width = int(header_height * 3.8)
    dino_header_height = int(dino_header.get_height() * (dino_header_width / dino_header.get_width()))
    dino_header = pygame.transform.scale(dino_header, (dino_header_width, dino_header_height))

    pinball_header_width = int(header_height * 3.8)
    pinball_header_height = int(pinball_header.get_height() * (pinball_header_width / pinball_header.get_width()))
    pinball_header = pygame.transform.scale(pinball_header, (pinball_header_width, pinball_header_height))

    # Blit the logo onto the header bar surface
    logo_x = int(header_height1 * 0.1)
    logo_y = int(header_height1 * 0.1)
    header_surface.blit(logo_image, (logo_x, logo_y))

    dino_header_x = int(header_height * 0.1)
    dino_header_y = int(header_height * 0.1)
    dino_header_surface.blit(dino_header, (dino_header_x, dino_header_y))

    pinball_header_x = int(header_height * 0.1)
    pinball_header_y = int(header_height * 0.1)
    pinball_header_surface.blit(pinball_header, (pinball_header_x, pinball_header_y))

    # Blit the header bar onto the main screen
    # current_screen.blit(header_surface, (0, 0))
    # current_screen.blit(dino_header_surface, (0, 0))

    # making image as buttons
    dino_button = pygame.image.load("images/dino_button.PNG")
    pinball_button = pygame.image.load("images/pinball_button.PNG")
    see_analytics_button = pygame.image.load("images/see_analytics.PNG")
    quit_button = pygame.image.load("images/quit.PNG")
    return_to_main_button = pygame.image.load("images/return_to_main.PNG")

    # Define the position and size of the button
    # button1_rect = pygame.Rect(BUTTON_LEFT_1, BUTTON_TOP, BUTTON_WIDTH, BUTTON_HEIGHT)
    # button1_rect = dino_button.get_rect()
    # button1_rect.center = (500, 500)
    # button2_rect = pinball_button.get_rect()
    # button2_rect.center = (700, 500)
    # Get the size of the button image
    button1_width = dino_button.get_width()
    button1_height = dino_button.get_height()
    button2_width = pinball_button.get_width()
    button2_height = pinball_button.get_height()
    button3_width = see_analytics_button.get_width()
    button3_height = see_analytics_button.get_height()
    button4_width = quit_button.get_width()
    button4_height = quit_button.get_height()
    button5_width = see_analytics_button.get_width()
    button5_height = see_analytics_button.get_height()
    button6_width = quit_button.get_width()
    button6_height = quit_button.get_height()
    button7_width = return_to_main_button.get_width()
    button7_height = return_to_main_button.get_height()

    # Define the button coordinates
    button1_x = WINDOW_WIDTH / 2 - button1_width / 2 - 250
    button1_y = WINDOW_HEIGHT / 2 - button1_height / 2 + 150

    button2_x = WINDOW_WIDTH / 2 - button2_width / 2 + 250
    button2_y = WINDOW_HEIGHT / 2 - button2_height / 2 + 150

    button3_x = WINDOW_WIDTH / 2 - button3_width / 2 - 300
    button3_y = WINDOW_HEIGHT / 2 - button3_height / 2 + 300

    button4_x = WINDOW_WIDTH / 2 - button4_width / 2 + 500
    button4_y = WINDOW_HEIGHT / 2 - button4_height / 2 + 300

    button5_x = WINDOW_WIDTH / 2 - button5_width / 2 - 300
    button5_y = WINDOW_HEIGHT / 2 - button5_height / 2 + 300

    button6_x = WINDOW_WIDTH / 2 - button6_width / 2 + 500
    button6_y = WINDOW_HEIGHT / 2 - button6_height / 2 + 300

    button7_x = WINDOW_WIDTH / 2 - button7_width / 2
    button7_y = WINDOW_HEIGHT / 2 - button7_height / 2



    # Define the button states
    BUTTON_STATE_NORMAL = 0
    BUTTON_STATE_HOVER = 1
    BUTTON_STATE_CLICKED = 2
    # Set the initial button state to normal
    button1_state = BUTTON_STATE_NORMAL
    button2_state = BUTTON_STATE_NORMAL
    button3_state = BUTTON_STATE_NORMAL
    button4_state = BUTTON_STATE_NORMAL
    button5_state = BUTTON_STATE_NORMAL
    button6_state = BUTTON_STATE_NORMAL
    button7_state = BUTTON_STATE_NORMAL


    # Set up colors for the button
    inactive_color = (255, 255, 255)
    hover_color = (200, 200, 200)
    click_color = (150, 150, 150)

    # Display texts

    # Set up the font
    font1 = pygame.font.Font("Font/PressStart2P-Regular.ttf", 20)
    font2 = pygame.font.Font("Font/PressStart2P-Regular.ttf", 30)
    # Create a text surface
    text_surface1 = font1.render("Embark on your quest for fitness... with fun!", True, (0, 0, 0))
    text_surface2 = font2.render("Choose your game", True, (0, 0, 0))
    text_surface9 = font2.render("~~Your Performance Last Game~~", True, (0, 0, 0))

    # Get the size of the text surface
    text_width1, text_height1 = text_surface1.get_size()
    text_width2, text_height2 = text_surface2.get_size()
    text_width9, text_height9 = text_surface9.get_size()

    # Calculate the position to center the text
    x1 = (1600 - text_width1) // 2
    y1 = (900 - text_height1) // 2 - 250
    x2 = (1600 - text_width2) // 2
    y2 = (900 - text_height2) // 2 - 150

    x9 = (1600 - text_width9) // 2
    y9 = (900 - text_height9) // 2 - 270

    # Game loop
    total_calories = 0
    max_calories = 0
    max_jumps = 0
    max_squats = 0
    pinball_total_calories = 0
    pinball_max_calories = 0
    max_left_reps = 0
    max_right_reps = 0
    flag = False
    flag2 = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Quit the game when the close button is clicked
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                # Check if the mouse released the button
                mouse_pos = pygame.mouse.get_pos()
                if button1_x <= mouse_pos[0] <= button1_x + button1_width and \
                    button1_y <= mouse_pos[1] <= button1_y + button1_height:
                    # Execute button click action here
                    button1_state = BUTTON_STATE_NORMAL

                elif button2_x <= mouse_pos[0] <= button2_x + button2_width and \
                    button2_y <= mouse_pos[1] <= button2_y + button2_height:
                    # Execute button click action here
                    button2_state = BUTTON_STATE_NORMAL

                elif button3_x <= mouse_pos[0] <= button3_x + button3_width and \
                    button3_y <= mouse_pos[1] <= button3_y + button3_height:
                    # Execute button click action here
                    button3_state = BUTTON_STATE_NORMAL

                elif button4_x <= mouse_pos[0] <= button4_x + button4_width and \
                    button4_y <= mouse_pos[1] <= button4_y + button4_height:
                    # Execute button click action here
                    button4_state = BUTTON_STATE_NORMAL

                elif button5_x <= mouse_pos[0] <= button5_x + button5_width and \
                    button5_y <= mouse_pos[1] <= button5_y + button5_height:
                    # Execute button click action here
                    button5_state = BUTTON_STATE_NORMAL

                elif button6_x <= mouse_pos[0] <= button6_x + button6_width and \
                    button6_y <= mouse_pos[1] <= button6_y + button6_height:
                    # Execute button click action here
                    button6_state = BUTTON_STATE_NORMAL

                elif button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                    button7_y <= mouse_pos[1] <= button7_y + button7_height:
                    # Execute button click action here
                    button7_state = BUTTON_STATE_NORMAL

            elif event.type == pygame.MOUSEMOTION:
                # Check if the mouse is hovering over the button
                mouse_pos = pygame.mouse.get_pos()
                if button1_x <= mouse_pos[0] <= button1_x + button1_width and \
                    button1_y <= mouse_pos[1] <= button1_y + button1_height:
                    button1_state = BUTTON_STATE_HOVER
                else:
                    button1_state = BUTTON_STATE_NORMAL

                if button2_x <= mouse_pos[0] <= button2_x + button2_width and \
                    button2_y <= mouse_pos[1] <= button2_y + button2_height:
                    button2_state = BUTTON_STATE_HOVER
                else:
                    button2_state = BUTTON_STATE_NORMAL

                if button3_x <= mouse_pos[0] <= button3_x + button3_width and \
                    button3_y <= mouse_pos[1] <= button3_y + button3_height:
                    button3_state = BUTTON_STATE_HOVER
                else:
                    button3_state = BUTTON_STATE_NORMAL

                if button4_x <= mouse_pos[0] <= button4_x + button4_width and \
                    button4_y <= mouse_pos[1] <= button4_y + button4_height:
                    button4_state = BUTTON_STATE_HOVER
                else:
                    button4_state = BUTTON_STATE_NORMAL

                if button5_x <= mouse_pos[0] <= button5_x + button5_width and \
                    button5_y <= mouse_pos[1] <= button5_y + button5_height:
                    button5_state = BUTTON_STATE_HOVER
                else:
                    button5_state = BUTTON_STATE_NORMAL

                if button6_x <= mouse_pos[0] <= button6_x + button6_width and \
                    button6_y <= mouse_pos[1] <= button6_y + button6_height:
                    button6_state = BUTTON_STATE_HOVER
                else:
                    button6_state = BUTTON_STATE_NORMAL

                if button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                    button7_y <= mouse_pos[1] <= button7_y + button7_height:
                    button7_state = BUTTON_STATE_HOVER
                else:
                    button7_state = BUTTON_STATE_NORMAL

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if a button is clicked
                mouse_pos = pygame.mouse.get_pos()
                if button1_x <= mouse_pos[0] <= button1_x + button1_width and \
                    button1_y <= mouse_pos[1] <= button1_y + button1_height and current_screen_title == "Screen 1":
                    button1_state = BUTTON_STATE_CLICKED
                # if button1_rect.collidepoint(event.pos) and current_screen_title == "Screen 1":
                    print("Button 1 clicked!")
                    # button clickings


                    # webbrowser.open("https://chromedino.com/")
                    # webbrowser.open("chrome://dino")
                    # Create the second screen
                    screen2 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    # pygame.display.set_caption("Screen 2")
                    current_screen_title = "Screen 2"
                    current_screen = screen2

                    driver = webdriver.Chrome()

                    # driver.get("chrome://dino")
                    # driver.quit()

                    try:
                        # os.system("python jjtodino.py")
                        # subprocess.run(["python", "jjtodino.py"], check=True)
                        driver.get("chrome://dino")
                        # driver.get("google.com")
                        # driver.quit()
                    except WebDriverException:
                        jjtodino_.jumping_jack_to()
                        pass

                    # driver.quit()

                    # try:
                    #     proc = subprocess.Popen(["python", "jjtodino.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    #     output, error = proc.communicate()
                    #     if error:
                    #         raise Exception(error)
                    #     # navigate to the desired URL after the Python script finishes
                    #     driver.get("chrome://dino")
                    # except Exception as e:
                    #     print("Error running script:", e)

                    # driver.quit()

                elif button3_x <= mouse_pos[0] <= button3_x + button3_width and \
                    button3_y <= mouse_pos[1] <= button3_y + button3_height and current_screen_title == "Screen 2":
                    button3_state = BUTTON_STATE_CLICKED
                # elif button3_rect.collidepoint(event.pos) and current_screen_title == "Screen 2":
                    print("Button 3 clicked!")
                    screen3 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    # pygame.display.set_caption("Screen 2")
                    current_screen_title = "Screen 3"
                    current_screen = screen3

                elif button4_x <= mouse_pos[0] <= button4_x + button4_width and \
                    button4_y <= mouse_pos[1] <= button4_y + button4_height and current_screen_title == "Screen 2":
                    button4_state = BUTTON_STATE_CLICKED
                # elif button4_rect.collidepoint(event.pos) and current_screen_title == "Screen 2":
                    print("button 4")
                    pygame.quit()
                    quit()

                elif button5_x <= mouse_pos[0] <= button5_x + button5_width and \
                    button5_y <= mouse_pos[1] <= button5_y + button5_height and current_screen_title == "Screen 4":
                    button5_state = BUTTON_STATE_CLICKED
                # elif button3_rect.collidepoint(event.pos) and current_screen_title == "Screen 4":
                    print("Button 5 clicked!")
                    screen5 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    # pygame.display.set_caption("Screen 2")
                    current_screen_title = "Screen 5"
                    current_screen = screen5

                elif button6_x <= mouse_pos[0] <= button6_x + button6_width and \
                    button6_y <= mouse_pos[1] <= button6_y + button6_height and current_screen_title == "Screen 4":
                    button6_state = BUTTON_STATE_CLICKED
                # elif button4_rect.collidepoint(event.pos) and current_screen_title == "Screen 4":
                    print("button 6")
                    pygame.quit()
                    quit()

                elif button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                    button7_y <= mouse_pos[1] <= button7_y + button7_height and current_screen_title == "Screen 3":
                    button7_state = BUTTON_STATE_CLICKED
                    print("Button 7 clicked!")
                    current_screen = screen1
                elif button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                    button7_y <= mouse_pos[1] <= button7_y + button7_height and current_screen_title == "Screen 5":
                    button7_state = BUTTON_STATE_CLICKED
                    print("Button 7 clicked!")
                    current_screen = screen1

                elif button2_x <= mouse_pos[0] <= button2_x + button2_width and \
                    button2_y <= mouse_pos[1] <= button2_y + button2_height and current_screen_title == "Screen 1":
                    button2_state = BUTTON_STATE_CLICKED
                # elif button2_rect.collidepoint(event.pos) and current_screen_title == "Screen 1":
                    print("Button 2 clicked!")
                    screen4 = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
                    current_screen_title = "Screen 4"
                    current_screen = screen4

                    driver = webdriver.Chrome()
                    # webbrowser.open("https://chromedino.com/")
                    # webbrowser.open("chrome://dino")
                    driver = webdriver.Chrome()
                    # driver.get("chrome://dino")
                    # driver.quit()

                    try:
                        # os.system("python jjtodino.py")
                        # subprocess.run(["python", "jjtodino.py"], check=True)
                        driver.get("https://playpager.com/pinball-online/")
                        bctopinball.bicep_curl_to()
                        # driver.get("google.com")
                        # driver.quit()
                    except WebDriverException:
                        # bctopinball.bicep_curl_to()
                        pass

            # Fill the screen with gray color
            current_screen.fill(WHITE)

            # Draw the buttons
            if current_screen_title == "Screen 1":
                header_surface.blit(logo_image, (logo_x, logo_y))
                current_screen.blit(header_surface, (0, 0))
                current_screen.blit(text_surface1, (x1, y1))
                current_screen.blit(text_surface2, (x2, y2))

                # Draw the button
                if button1_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(dino_button, (button1_x, button1_y))
                elif button1_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button1_width, button1_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(dino_button, (button1_x, button1_y))
                    current_screen.blit(hover_overlay, (button1_x, button1_y))
                elif button1_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button1_width, button1_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(dino_button, (button1_x, button1_y))
                    current_screen.blit(click_overlay, (button1_x, button1_y))
                if button2_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(pinball_button, (button2_x, button2_y))
                elif button2_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button2_width, button2_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(pinball_button, (button2_x, button2_y))
                    current_screen.blit(hover_overlay, (button2_x, button2_y))
                elif button2_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button2_width, button2_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(pinball_button, (button2_x, button2_y))
                    current_screen.blit(click_overlay, (button2_x, button2_y))



                # current_screen.blit(text_surface, (x, y))


            elif current_screen_title == "Screen 2":
                dino_header_surface.blit(dino_header, (dino_header_x, dino_header_y))
                current_screen.blit(dino_header_surface, (0, 0))

                if flag == False:
                    with open('dummy.csv', 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        # next(csv_reader)  # skip header row if there is one
                        # analytics_list1, analytics_list2, analytics_list3 = [], [], []
                        for row in csv_reader:
                            analytics_list1.append(row[0])
                            analytics_list2.append(row[1])
                            analytics_list3.append(row[2])

                print("-----")
                print(analytics_list1)
                print(analytics_list2)
                print(analytics_list3)
                asd = round(float(analytics_list1[-1]), 2)
                text_surface3 = font2.render("Calories Burnt: " + str(asd), True, (0, 0, 0))
                text_surface4 = font2.render("Jumping Jacks Performed: " + str(analytics_list2[-1]), True, (0, 0, 0))
                text_surface5 = font2.render("Squats Performed: " + str(analytics_list3[-1]), True, (0, 0, 0))
                flag = True
                text_width3, text_height3 = text_surface3.get_size()
                text_width4, text_height4 = text_surface4.get_size()
                text_width5, text_height5 = text_surface5.get_size()

                x3 = (1600 - text_width3) // 2
                y3 = (900 - text_height3) // 2 - 100
                x4 = (1600 - text_width4) // 2
                y4 = (900 - text_height4) // 2
                x5 = (1600 - text_width5) // 2
                y5 = (900 - text_height5) // 2 + 100

                current_screen.blit(text_surface3, (x3, y3))
                current_screen.blit(text_surface4, (x4, y4))
                current_screen.blit(text_surface5, (x5, y5))
                current_screen.blit(text_surface9, (x9, y9))
                pygame.display.set_caption("Screen 2")
                if button3_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(see_analytics_button, (button3_x, button3_y))
                elif button3_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button3_width, button3_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(see_analytics_button, (button3_x, button3_y))
                    current_screen.blit(hover_overlay, (button3_x, button3_y))
                elif button3_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button3_width, button3_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(see_analytics_button, (button3_x, button3_y))
                    current_screen.blit(click_overlay, (button3_x, button3_y))

                if button4_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(quit_button, (button4_x, button4_y))
                elif button4_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button4_width, button4_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(quit_button, (button4_x, button4_y))
                    current_screen.blit(hover_overlay, (button4_x, button4_y))
                elif button4_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button4_width, button4_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(quit_button, (button4_x, button4_y))
                    current_screen.blit(click_overlay, (button4_x, button4_y))

            elif current_screen_title == "Screen 3":
                for item in analytics_list1:
                    total_calories += float(item)
                    max_calories = max(max_calories, float(item))

                for item in analytics_list2:
                    max_jumps = max(max_jumps, int(item))

                for item in analytics_list3:
                    max_squats = max(max_squats, int(item))
                pygame.display.set_caption("Screen 3")
                # return to main button
                if button7_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                elif button7_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                    current_screen.blit(hover_overlay, (button7_x, button7_y))
                elif button7_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                    current_screen.blit(click_overlay, (button7_x, button7_y))

                flag_value = plot.draw_graph(analytics_list1, analytics_list2, analytics_list3, total_calories, max_calories, max_jumps, max_squats)

                print(flag_value)
                if flag_value == True:
                    current_screen = screen1
                    current_screen_title = "Screen 1"

            elif current_screen_title == "Screen 4":
                pinball_header_surface.blit(pinball_header, (pinball_header_x, pinball_header_y))
                current_screen.blit(pinball_header_surface, (0, 0))
                if flag2 == False:
                    with open('dummy2.csv', 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        # next(csv_reader)  # skip header row if there is one
                        # pinball_analytics1, pinball_analytics2, pinball_analytics3 = [], [], []
                        for row in csv_reader:
                            pinball_analytics1.append(row[0])
                            pinball_analytics2.append(row[1])
                            pinball_analytics3.append(row[2])


                asd = round(float(pinball_analytics1[-1]), 2)
                text_surface6 = font2.render("Calories Burnt: " + str(asd) + " cal", True, (0, 0, 0))
                text_surface7 = font2.render("Right Bicep Curl Reps: " + str(pinball_analytics2[-1]), True, (0, 0, 0))
                text_surface8 = font2.render("Left Bicep Curl Reps: " + str(pinball_analytics3[-1]), True, (0, 0, 0))
                flag2 = True
                text_width6, text_height6 = text_surface6.get_size()
                text_width7, text_height7 = text_surface7.get_size()
                text_width8, text_height8 = text_surface8.get_size()

                x6 = (1600 - text_width6) // 2
                y6 = (900 - text_height6) // 2 - 100
                x7 = (1600 - text_width7) // 2
                y7 = (900 - text_height7) // 2
                x8 = (1600 - text_width8) // 2
                y8 = (900 - text_height8) // 2 + 100

                current_screen.blit(text_surface6, (x6, y6))
                current_screen.blit(text_surface7, (x7, y7))
                current_screen.blit(text_surface8, (x8, y8))
                current_screen.blit(text_surface9, (x9, y9))
                pygame.display.set_caption("Screen 4")
                if button5_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(see_analytics_button, (button5_x, button5_y))
                elif button5_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button5_width, button5_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(see_analytics_button, (button5_x, button5_y))
                    current_screen.blit(hover_overlay, (button5_x, button5_y))
                elif button5_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button5_width, button5_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(see_analytics_button, (button5_x, button5_y))
                    current_screen.blit(click_overlay, (button5_x, button5_y))

                if button6_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(quit_button, (button6_x, button6_y))
                elif button6_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button6_width, button6_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(quit_button, (button6_x, button6_y))
                    current_screen.blit(hover_overlay, (button6_x, button6_y))
                elif button6_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button6_width, button6_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(quit_button, (button6_x, button6_y))
                    current_screen.blit(click_overlay, (button6_x, button6_y))

            elif current_screen_title == "Screen 5":
                for item in pinball_analytics1:
                    pinball_total_calories += round(float(item), 2)
                    pinball_max_calories = max(pinball_max_calories, round(float(item), 2))

                for item in pinball_analytics2:
                    max_right_reps = max(max_right_reps, int(item))

                for item in pinball_analytics3:
                    max_left_reps = max(max_left_reps, int(item))

                # return to main button
                if button7_state == BUTTON_STATE_NORMAL:
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                elif button7_state == BUTTON_STATE_HOVER:
                    # Apply a transparent overlay to simulate a hover effect
                    hover_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                    hover_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                    current_screen.blit(hover_overlay, (button7_x, button7_y))
                elif button7_state == BUTTON_STATE_CLICKED:
                    # Apply a transparent overlay to simulate a clicked effect
                    click_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                    click_overlay.fill((255, 255, 255, 128))
                    current_screen.blit(return_to_main_button, (button7_x, button7_y))
                    current_screen.blit(click_overlay, (button7_x, button7_y))
                print(pinball_analytics1)
                print(pinball_analytics2)
                print(pinball_analytics3)
                pygame.display.set_caption("Screen 5")
                flag_value2 = pinball_plot.draw_graph(pinball_analytics1, pinball_analytics2, pinball_analytics3, pinball_total_calories, pinball_max_calories, max_right_reps, max_left_reps)

                print(flag_value2)
                if flag_value2 == True:
                    current_screen = screen1
                    current_screen_title = "Screen 1"

            # Update the screen
            pygame.display.update()



if __name__ == '__main__':
    run_chrome()
    print('hello')
    # jjtodino_.jumping_jack_to()