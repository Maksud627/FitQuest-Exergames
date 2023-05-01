import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import pygame
from pygame.locals import *
import pylab

def draw_graph(analytics_list1, analytics_list2, analytics_list3, total_calories, max_calories, max_right_reps, max_left_reps):
    # Header Bar Infos
    header_height = 70
    header_color = (154, 205, 50)

    # Create a Pygame surface for the header bar
    header_surface = pygame.Surface((1600, header_height))
    header_surface.fill(header_color)
    pinball_header_surface = pygame.Surface((1600, header_height))
    pinball_header_surface.fill(header_color)


    pinball_header = pygame.image.load('images/pinball_header.PNG')
    return_header = pygame.image.load("images/return_to_main.PNG")

    # Resize the logo image to fit within the header bar
    pinball_header_width = int(header_height * 3.8)
    pinball_header_height = int(pinball_header.get_height() * (pinball_header_width / pinball_header.get_width()))
    pinball_header = pygame.transform.scale(pinball_header, (pinball_header_width, pinball_header_height))

    return_header_width = int(header_height * 2.8)
    return_header_height = int(return_header.get_height() * (return_header_width / return_header.get_width()))
    return_header = pygame.transform.scale(return_header, (return_header_width, return_header_height))

    # Blit the logo onto the header bar surface
    pinball_header_x = int(header_height * 0.1)
    pinball_header_y = int(header_height * 0.1)
    pinball_header_surface.blit(pinball_header, (pinball_header_x, pinball_header_y))

    return_header_x = int(header_height * 0.1) + 1280
    return_header_y = int(header_height * 0.1) - 6
    pinball_header_surface.blit(return_header, (return_header_x, return_header_y))

    font2 = pygame.font.Font("Font/PressStart2P-Regular.ttf", 20)
    font3 = pygame.font.Font("Font/PressStart2P-Regular.ttf", 15)
    text_surface7 = font2.render("~~Lifetime Statistics~~", True, (0, 0, 0))

    text_width7, text_height7 = text_surface7.get_size()


    x7 = (1600 - text_width7) // 2 + 540
    y7 = (900 - text_height7) // 2 - 350

    # Define the button states
    BUTTON_STATE_NORMAL = 0
    BUTTON_STATE_HOVER = 1
    BUTTON_STATE_CLICKED = 2

    return_to_main_button = pygame.image.load("images/return_to_main.PNG")

    button7_width = return_to_main_button.get_width()
    button7_height = return_to_main_button.get_height()
    button7_x = 1600 / 2 - button7_width / 2 + 550
    button7_y = 900 / 2 - button7_height / 2 - 400
    button7_state = BUTTON_STATE_NORMAL



    matplotlib.use("Agg")


    plt.rcParams.update({
        "lines.marker": "o",         # available ('o', 'v', '^', '<', '>', '8', 's', 'p', '*', 'h', 'H', 'D', 'd', 'P', 'X')
        "lines.linewidth": "1.8",
        "axes.prop_cycle": plt.cycler('color', ['white']),  # line color
        # "text.color": "white",       # no text in this example
        "text.color": "black",
        "axes.facecolor": "black",   # background of the figure
        "axes.edgecolor": "lightgray",
        "axes.labelcolor": "black",  # no labels in this example
        "axes.grid": "True",
        "grid.linestyle": "--",      # {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
        "xtick.color": "black",
        "ytick.color": "black",
        "grid.color": "lightgray",
        "figure.facecolor": "black", # color surrounding the plot
        "figure.edgecolor": "black",
    })

    fig1 = pylab.figure(figsize=[10, 2], # Inches
                       dpi=100)        # 100 dots per inch, so the resulting buffer is 400x200 pixels
    fig1.patch.set_alpha(0.1)           # make the surrounding of the plot 90% transparent to show what it does

    fig2 = pylab.figure(figsize=[10, 2],  # Inches
                       dpi=100)  # 100 dots per inch, so the resulting buffer is 400x200 pixels
    fig2.patch.set_alpha(0.1)

    fig3 = pylab.figure(figsize=[10, 2],  # Inches
                       dpi=100)  # 100 dots per inch, so the resulting buffer is 400x200 pixels
    fig3.patch.set_alpha(0.1)

    ax1 = fig1.gca()

    ax2 = fig2.gca()

    ax3 = fig3.gca()


    ax1.plot([float(x) for x in analytics_list1])
    ax1.set_ylabel("Calories")
    ax2.plot([float(y) for y in analytics_list2])
    ax2.set_ylabel("Right Bicep Curls")
    ax3.plot([float(z) for z in analytics_list3])
    ax3.set_ylabel("Left Bicep Curls")

    canvas1 = agg.FigureCanvasAgg(fig1)
    canvas1.draw()
    canvas2 = agg.FigureCanvasAgg(fig2)
    canvas2.draw()
    canvas3 = agg.FigureCanvasAgg(fig3)
    canvas3.draw()
    renderer1 = canvas1.get_renderer()
    raw_data1 = renderer1.buffer_rgba()
    renderer2 = canvas2.get_renderer()
    raw_data2 = renderer2.buffer_rgba()
    renderer3 = canvas3.get_renderer()
    raw_data3 = renderer3.buffer_rgba()

    window = pygame.display.set_mode((1600, 900), DOUBLEBUF)
    screen = pygame.display.get_surface()

    size1 = canvas1.get_width_height()
    size2 = canvas2.get_width_height()
    size3 = canvas3.get_width_height()

    surf1 = pygame.image.frombuffer(raw_data1, size1, "RGBA")
    surf2 = pygame.image.frombuffer(raw_data2, size2, "RGBA")
    surf3 = pygame.image.frombuffer(raw_data3, size3, "RGBA")

    bg_color = (255, 255, 255)   # fill red as background color
    screen.fill(bg_color)
    # screen.blit(surf1, (100, 5)) # x, y position on screen
    # screen.blit(surf2, (100, 300))
    # screen.blit(surf3, (100, 595))
    screen.blit(surf1, (100, 150))  # x, y position on screen
    screen.blit(surf2, (100, 400))
    screen.blit(surf3, (100, 650))

    pinball_header_surface.blit(pinball_header, (pinball_header_x, pinball_header_y))
    screen.blit(pinball_header_surface, (0, 0))
    screen.blit(text_surface7, (x7, y7))
    text_surface8 = font3.render("Total calories burnt: " + str(total_calories) + " cal", True, (0, 0, 0))
    text_surface9 = font3.render("Highest Right Reps: " + str(max_right_reps), True, (0, 0, 0))
    text_surface10 = font3.render("Highest Left Reps: " + str(max_left_reps), True, (0, 0, 0))
    text_surface11 = font3.render("Highest calorie burn: " + str(max_calories) + " cal", True, (0, 0, 0))
    text_width8, text_height8 = text_surface8.get_size()
    text_width9, text_height9 = text_surface9.get_size()
    text_width10, text_height10 = text_surface10.get_size()
    text_width11, text_height11 = text_surface11.get_size()
    x8 = (1600 - text_width8) // 2 + 540
    y8 = (900 - text_height8) // 2 - 280

    x9 = (1600 - text_width9) // 2 + 540
    y9 = (900 - text_height9) // 2 - 220

    x10 = (1600 - text_width10) // 2 + 540
    y10 = (900 - text_height10) // 2 - 190

    x11 = (1600 - text_width11) // 2 + 540
    y11 = (900 - text_height11) // 2 - 250

    screen.blit(text_surface8, (x8, y8))
    screen.blit(text_surface9, (x9, y9))
    screen.blit(text_surface10, (x10, y10))
    screen.blit(text_surface11, (x11, y11))


    pygame.display.flip()

    global flag
    flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONUP:
                print(button7_state)
                mouse_pos = pygame.mouse.get_pos()
                if button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                        button7_y <= mouse_pos[1] <= button7_y + button7_height:
                    # Execute button click action here
                    button7_state = BUTTON_STATE_NORMAL
            elif event.type == pygame.MOUSEMOTION:
                print(button7_state)
                mouse_pos = pygame.mouse.get_pos()
                if button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                        button7_y <= mouse_pos[1] <= button7_y + button7_height:
                    button7_state = BUTTON_STATE_HOVER
                else:
                    button7_state = BUTTON_STATE_NORMAL

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(button7_state)
                mouse_pos = pygame.mouse.get_pos()
                if button7_x <= mouse_pos[0] <= button7_x + button7_width and \
                        button7_y <= mouse_pos[1] <= button7_y + button7_height:
                    button7_state = BUTTON_STATE_CLICKED
                    print("Button 7 clicked!")

            # Draw the buttons
            if button7_state == BUTTON_STATE_NORMAL:
                screen.blit(return_to_main_button, (button7_x, button7_y))
                flag = False
            elif button7_state == BUTTON_STATE_HOVER:
                # Apply a transparent overlay to simulate a hover effect
                hover_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                hover_overlay.fill((255, 255, 255, 128))
                screen.blit(return_to_main_button, (button7_x, button7_y))
                screen.blit(hover_overlay, (button7_x, button7_y))
                flag = False
            elif button7_state == BUTTON_STATE_CLICKED:
                # Apply a transparent overlay to simulate a clicked effect
                click_overlay = pygame.Surface((button7_width, button7_height), pygame.SRCALPHA)
                click_overlay.fill((255, 255, 255, 128))
                screen.blit(return_to_main_button, (button7_x, button7_y))
                screen.blit(click_overlay, (button7_x, button7_y))
                flag = True

        pygame.time.Clock().tick(30)  # Avoid 100% CPU usage
        if flag:
            return flag

if __name__ == "__main__":
    draw_graph()