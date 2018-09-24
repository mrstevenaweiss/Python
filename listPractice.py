

# def makeSentence(aList):
#     front = aList[:-1]
#     back = aList[-1]
#
#     sentence = ''
#
#     for word in front:
#         sentence += word + ', '
#
#     return sentence + 'and ' + back
#
# spam = ['apples', 'bananas', 'tofu', 'cats']
#
# print(makeSentence(spam))


grid = [['.','.','.','.','.','.'],
        ['.','0','0','.','.','.'],
        ['0','0','0','0','.','.'],
        ['0','0','0','0','0','.'],
        ['.','0','0','0','0','0'],
        ['0','0','0','0','0','.'],
        ['0','0','0','0','.','.'],
        ['.','0','0','.','.','.'],
        ['.','.','.','.','.','.']]

def makeGrid(aGrid):

    for row in range(len(aGrid[0])):
        for button in range(len(aGrid)):
            print(aGrid[button][row], end='')
        print()

makeGrid(grid)
