def renderTextWrap(text, font, color, allowedWidth, window, x, y, shiftInY):
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
        rendering = font.render(str(amount), True, color)
        window.blit(rendering, (x,y + shiftInY * index ))