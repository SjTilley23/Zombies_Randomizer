import pygame
pygame.init()
def cursor_text_box(text, font, color, allowed_width, window, shift_in_y,
                    rect_color, edge_color=(0,0,0), edge_thickness=-1):
    #splitting the text
    list_of_strings = [text]
    list_of_strings_2 = []
    words = list_of_strings[0].split(" ")

    #List of text to enumerate
    width_of_string = 0
    old_words = ""
    for index, amount in enumerate(words):
        render_test = font.render(" " + amount,True,color)
        width_of_current_word = render_test.get_width()
        if width_of_string + width_of_current_word > allowed_width:
            list_of_strings_2.append(str(old_words))
            width_of_string = 0
            old_words = ""
        width_of_string = width_of_current_word + width_of_string
        old_words = old_words + " " + amount
    list_of_strings_2.append(str(old_words))

    # Rendering, and Displaying
    for index, amount in enumerate(list_of_strings_2):
        pygame.draw.rect(window, rect_color, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],
                allowed_width, shift_in_y * index + font.get_height()))
        pygame.draw.rect(window, edge_color, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],
                allowed_width, shift_in_y * index + font.get_height()), edge_thickness)
    for index, amount in enumerate(list_of_strings_2):
        rendering = font.render(str(amount), True, color)
        window.blit(rendering, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]
                                + shift_in_y * index ))
