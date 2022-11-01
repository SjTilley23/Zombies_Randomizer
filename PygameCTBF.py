def cursorTextBox(text, font, color, allowedWidth, window, shiftInY, rectColor):
    #splitting the text
    listOfStrings = [text]
    listOfStrings2 = []
    words = listOfStrings[0].split(" ")

    #List of text to enumerate
    widthOfString = 0
    oldWords = ""
    for index, amount in enumerate(words):
        renderTest = font.render(" " + amount,True,color)
        widthOfCurrentWord = renderTest.get_width()
        if widthOfString + widthOfCurrentWord > allowedWidth:
            listOfStrings2.append(str(oldWords))
            widthOfString = 0
            oldWords = ""
        widthOfString = widthOfCurrentWord + widthOfString
        oldWords = oldWords + " " + amount
    listOfStrings2.append(str(oldWords))
    
    # Rendering, and Displaying
    for index, amount in enumerate(listOfStrings2):
        pygame.draw.rect(window, rectColor, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],allowedWidth, shiftInY * index + font.get_height()))
    for index, amount in enumerate(listOfStrings2):
        rendering = font.render(str(amount), True, color)
        window.blit(rendering, (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1] + shiftInY * index ))