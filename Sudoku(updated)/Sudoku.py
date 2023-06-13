
import random
import pygame
import numpy as np
import os

pygame.init()

class grid():

   def __init__(self):#config,gridPos):
      
      self.Config = np.array([None] * 5)
      self.squareImages = np.array([None] * 10)
      self.GridPos = np.empty((9,9), dtype=object)
      #self.GridPos = np.zeros((9,9)).astype(None)
      self.gridOutline = pygame.image.load('Files/ImageFiles/grid_outline.jpg')
      ##difficultyLevel = gameDiff.DifficultyLevel

      # Defining each record for grid configuration
      self.Config[0] = 'Files/GridConfigurations/Configuration1.txt'
      self.Config[1] = 'Files/GridConfigurations/Configuration2.txt'
      self.Config[2] = 'Files/GridConfigurations/Configuration3.txt'
      self.Config[3] = 'Files/GridConfigurations/Configuration4.txt'
      self.Config[4] = 'Files/GridConfigurations/Configuration5.txt'
      self.loadGrid()
      self.loadImages()

   def loadGrid(self):
      
      # Importing values of chosen grid configuration 
      configSelect = random.randint(0,4)      # Randomly chossing which grid configuration to load in 
      fGC = open(self.Config[configSelect], 'r')
      ##fGC = open('Files/GridConfigurations/' + self.difficultyLevel + '/Configuration' + str((configSelect + 1)), 'r')
      fVis = open('Files/GridConfigurations/Configuration' + str((configSelect + 1)) + 'Vis.txt', 'r')
      ##fVis = open('Files/GridConfigurations/' + self.difficultyLevel + '/Configuration' + str((configSelect + 1)) + 'Vis.txt', 'r')
      for importRow in range(0,9):
         cur_line = fGC.readline().strip()
         cur_line = np.array(cur_line.split(','))
         cur_line = cur_line.astype(np.int)

         cur_line_vis = fVis.readline().strip()
         cur_line_vis = np.array(cur_line_vis.split(','))
         cur_line_vis = cur_line_vis.astype(np.int)
         cur_line_vis = cur_line_vis.astype(np.bool)
         #print(cur_line)
         
         for importColumn in range(0,9):
            self.GridPos[importColumn][importRow] = square(cur_line_vis[importColumn], cur_line[importColumn])
            
            #self.GridPos[importRow][importColumn] = cur_line[importColumn]
      #print(self.GridPos)
      fGC.close()
      fVis.close()

   def loadImages(self):
      
      for counter in range(10):
         self.squareImages[counter] = pygame.image.load('Files/ImageFiles/square_' + str(counter) + '.png')
         self.squareImages[counter] = pygame.transform.smoothscale(self.squareImages[counter], [40, 40])

   def displayGrid(self, gameDisplay):

      for displayRow in range(0, 9):
        for displayColumn in range(0, 9):
           if self.GridPos[displayRow][displayColumn].Visible == True:
            gameDisplay.blit(self.squareImages[self.GridPos[displayRow][displayColumn].Value], [105+(44*displayRow), 185+(44*displayColumn)])
      
class square():

   def __init__(self,visible,value):#x,y):
     #pygame.sprite.Sprite.__init__(self)

     self.Visible = visible
     self.Value = value
     #self.rect.x = x
     #self.rect.y = y
        
     #squareImages = pygame.image.load('Files/ImageFiles/square_blank','Files/ImageFiles/square_one','Files/ImageFiles/square_two','Files/ImageFiles/square_three','Files/ImageFiles/square_four','Files/ImageFiles/square_five','Files/ImageFiles/square_six','Files/ImageFiles/square_seven','Files/ImageFiles/square_eight','Files/ImageFiles/square_nine')

class gridSquare(square): ##NOT IN USE##

   def __init__(self,name):

      self.Name = name

   def setXYPositions(self):

      setX = 302
      for xCount in range(0, 80):
         gridSquare[Xcount].x = setX
         if setX == 644:
            setX = 302
         elif setX == 386 or setX == 515:
            setX =+ 45
         else:
            setX =+ 42
         
      setY = 698
      yCount = 0
      for rowCount in range(0, 8):
         for columnCount in range(0, 8):
            gridSquare[Ycount].y = setY
            yCount =+ 1
         if setY == 614 or setY == 485:
            setY =- 45
         else:
            setY =- 42
         yCount =+ 1
            
   def displaySquares(self):
      
     visCk = 0 
     for displayRow in range(0, 8):
        for displayColumn in range(0, 8):
           if gPProperties[visCk].visible == False:
              gridSquare[displayRow][displayColumn] = squareImages[0]
           else:
              if gridPos[displayRow][displayColumn] == 1:
                 gridSquare[displayRow][displayColumn] = squareImages[1]
              elif gridPos[displayRow][displayColumn] == 2:
                 gridSquare[displayRow][displayColumn] = squareImages[2]
              elif gridPos[displayRow][displayColumn] == 3:
                 gridSquare[displayRow][displayColumn] = squareImages[3]
              elif gridPos[displayRow][displayColumn] == 4:
                 gridSquare[displayRow][displayColumn] = squareImages[4]
              elif gridPos[displayRow][displayColumn] == 5:
                 gridSquare[displayRow][displayColumn] = squareImages[5]
              elif gridPos[displayRow][displayColumn] == 6:
                 gridSquare[displayRow][displayColumn] = squareImages[6]
              elif gridPos[displayRow][displayColumn] == 7:
                 gridSquare[displayRow][displayColumn] = squareImages[7]
              elif gridPos[displayRow][displayColumn] == 8:
                 gridSquare[displayRow][displayColumn] = squareImages[8]
              else:
                 gridSquare[displayRow][displayColumn] = squareImages[9]
              visCk =+ 1
           visCk =+ 1

     for displaySqaure in range(0, 80):
        gridSquare.image.bilt(gridPos[guessRow][guessColumn](gridSquare[guessValue].x, gridSquare[guessValue].y))

class guessSqaure(square):

   def __init__(self,guess):

      self.Guess = guess
      

   def setXYPos(self):

      setX = 302
      for xAndY in range(0, 8):
         guessSquare[xAndY].x, guessSquare[xAndY].y = setX, 200
         setX =+ 42
      
class difficulty(): ##NOT IN USE##

   def __init__(self):

      self.DifficultyLevel = ""
      ##difficultyImages = pygame.image.load('Files/ImageFiles/difficulty_quick.jpg','Files/ImageFiles/difficulty_easy.jpg','Files/ImageFiles/difficulty_medium.jpg','Files/ImageFiles/difficulty_hard.jpg')

   def selectDiff(self):
      
      ##if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
         ##selectDiff = pygame.sprite.groupcollide(mouse,gridSquare)

      validDiff = False
      while validDiff == False:
         self.DifficultyLevel = input("Enter difficulty level. Quick, Easy, Medium or Hard(case-sensitive, enter as displayed): ")
         if self.DifficultyLevel != "Quick" or self.DifficultyLevel != "Easy" or self.DifficultyLevel != "Medium" or self.DifficultyLevel != "Hard":
            print(elf.DifficultyLevel + " not valid. Enter 'Quick', 'Easy', 'Medium' or 'Hard'(case-sensitive, enter as displayed).")
         else:
            validDiff = True
         
         
         ##if selectDiff == 0:
            ##numSelect = 45
         ##elif selectDiff == 1:
            ##numSelect = 40
         ##elif selectDiff == 2:
            ##numSelect = 34
         ##else:
            ##numSelect = 25

   ##def visible(self):
            
         # Setting all positions to be initially to be visible
         ##for visT in range(0, 80):
            ##gPProperties[visT].visible = True

         # Randomly selection of which grid locations to be blank
         ##visComplete = 0
         ##while visComplete != numSelect:
            ##visSelectR = random.randint(0, 8)
            ##visSelectC = random.randint(0, 8)
            ##getSingleValuePos = visValue(visSelectR, visSelectC)
            ##if gPProperties[visValue].visible == True:
               ##gPProperties[visValue].visible = False
               ##gridSquare.image.bilt(gridPos[visSelectR][visSelectC](gridSquare[visValue].x, gridSquare[visValue].y))
               ##visComplete =+ 1

class Leaderboard():

   def __init__(self):

      self.LB = np.array[userName, time, mistakes]


def displayInital(gameGrid):

   #displayWidth = 1000
   #displayHeight = 800

   #black = (0,0,0)
   #white = (255,255,255)
   
   #grid1 = grid()
   backgroundImage = pygame.image.load('Files/ImageFiles/background_image(1).jpg')
   windowText = pygame.image.load('Files/ImageFiles/window_text.png')
   gameDisplay.blit(backgroundImage, [0, 0])
   gameDisplay.blit(gameGrid.gridOutline, [100, 180])
   gameGrid.displayGrid(gameDisplay)
   gameDisplay.blit(windowText, [550, 180])
   pygame.display.flip()

def mainLoop(gameGrid):
   backgroundImage = pygame.image.load('Files/ImageFiles/background_image(1).jpg')
   # Main loop while game is in progress
   userMistakes = 0
   timer = pygame.time.Clock()
   time = 0
   gameDone = False
   while gameDone == False:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
           gameDone = True
      milli = timer.tick()
      seconds = milli/1000
      time += seconds
      displayTime = time
      int(round(displayTime))
      print("Time Since Start: " + str(displayTime) + " seconds")
      gameDisplay.fill((255,255,255))
      gameDisplay.blit(backgroundImage, [0, 0])
      gameDisplay.blit(gameGrid.gridOutline, [100, 180])
      gameGrid.displayGrid(gameDisplay)
      # Loop to check the user selected position is one to be inputted
      possibleGrS = False
      while possibleGrS == False:
         # Getting user selection of row & checking it is valid(1-9)
            ##guessRow = pygame.image.load('Files/ImageFiles/row_outline.png')
            # Getting user selection of column & checking it is valid(1-9)
            inputCValid = False 
            while inputCValid == False:
               guessColumn = int(input("Enter column for square to make guess on(1(left) -> 9(right)): "))
               if guessColumn < 1 or guessColumn > 9:
                  print("Not valid entry. Please enter number 1 to 9.")
               else:
                  inputCValid = True
            validInputR = False
            while validInputR == False:
               ##if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                  ##uGPos = pygame.mouse.get_pos()
               guessRow = int(input("Enter row for square to make guess on(1(top) -> 9(bottom)): "))
               if guessRow < 1 or guessRow > 9:
                  print("Not valid entry. Please enter number 1 to 9")
               else:
                  validInputR = True

            # Checking if the selected square is currently visible
            ##getSingleValuePos = guessValue(guessRow, guessColumn)
            if gameGrid.GridPos[guessColumn - 1][guessRow - 1].Visible == True:
               guessOutline = pygame.image.load('Files/ImageFiles/guess_outline.png')
               gameDisplay.blit(guessOutline, [105+(44*(guessColumn - 1)), 185+(44*(guessRow - 1))])
               pygame.display.flip()
               print("Square given. Please select another square.")
               print("-------")
            else:
               possibleGrS = True
               guessOutline = pygame.image.load('Files/ImageFiles/guess_outline.png')
               gameDisplay.blit(guessOutline, [105+(44*(guessColumn - 1)), 185+(44*(guessRow - 1))])
               pygame.display.flip()
            

      # Taking in users guess for position & chenking input is 1-9
      userGuess = int(input("Enter guess number: "))
      validGuS = False
      while validGuS == False:
         ##if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            ##pygame.sprite.groupcollide(mouse, gridSquare)
            ##pos = pygame.mouse.get_pos()
         if guessRow <= 1 and guessRow >= 9:
            print("Not valid entry. Please enter number 1 to 9.")
         else:
            validGuS = True

         userGuessedValues = 0
         if userGuess == gameGrid.GridPos[guessColumn - 1][guessRow - 1].Value: # Cheching if user's guess value is same a value of selected grid position
            gameGrid.GridPos[guessColumn - 1][guessRow - 1].Visible = True
            gameDisplay.blit(gameGrid.squareImages[gameGrid.GridPos[guessColumn - 1][guessRow - 1].Value], [105+(44*(guessColumn - 1)), 185+(44*(guessRow - 1))])
            ##userGuessedValues += 1  # Increasing the number of user correct guesses by 1
            print("-------")
            ##print(userGuessedValues)
         else:
            userMistakes += 1 # Increase user misktakes by 1
            print("Wrong number")
            print("Mistakes made: " + str(userMistakes))
            print("-------")
            

         ##if userGuessedValues == (81 - 36): # Checking if the number of user correct guesses is equal to the number values to be guessed         
            ##gameDone = True
         countVis = 0
         for countVisC in range(0, 9):
            for countVisR in range(0, 9):
               if gameGrid.GridPos[countVisC][countVisR].Visible == True:
                  countVis += 1
         print(countVis)
         if countVis == 81:
            gameDone = True
      pygame.display.flip()
   finalTime = time
   print("Time Taken: " + str(finalTime))
   print("Total Mistakes: " + str(userMistakes))

def getSingleValuePos():
   ##NOT IN USE##

   selectedRow = selectedRow - 1
   rowStart = 0
   if guessRow == 1:
      rowStart = 9
   elif guessRow == 2:
      rowStart = 18
   elif guessRow == 3:
      rowStart = 27
   elif guessRow == 4:
      rowStart = 36
   elif guessRow == 5:
      rowStart = 45
   elif guessRow == 6:
      rowStart = 54
   elif guessRow == 7:
      rowStart = 63
   elif guessRow == 8:
      rowStart = 72

   guessVal = rowStart + selectedColumn

def updateLB(Lb, gameGrid, userGame):
    
   ##NOT IN USE##
   # Open leaderboard file & read in data into variables
   fI = open('Files/Leaderboard/Leaderboard.txt')
   for importLB in range(0, EOF):
    fI.read(LbList.LB[importLB].userName, LbList.LB[importLB].time, LbList.LB[importLB].mistakes)
   fI.close()

   # Taking in username & checking charater length
   validLength = False
   while validLength == False:
    userNameIn = input('Enter username:')
    if len(userNameIn) < 1 and len(userNameIn) > 30:
       print("Username too short or too long. Should be 1 to 30 characters. Please re-enter.")
    else:
       validLength = True

   userNameIn = LbList.LB[len(LbList.LB) + 1].username, userGame.finalTime = LbList.LB[len(LbList.LB) + 1].time, userGame.userMistakes = LbList.LB[len(LbList.LB) + 1].mistakes
   # Insertion sort
   for outer in range(0, len(LbList.LB)):
    temp = LbList.LB[outer].time
    for inner in range(len(LbList.LB), 0, -1):
       if LbList.LB[inner].time <= temp:
          LbList.LB[inner + 1] = LbList.LB[inner]
       LbList.LB[inner + 1] = temp

   # Open leaderbord file & writing new/reordered version to it
   fO = open('Files/Leaderboard/Leaderboard.txt')
   for exportLB in range(0, len(LbList.LB)):
    fO.write(LbList.LB[exportLB])
   fO.close()

pygame.display.set_caption("Sudoku")
print("Plese Keep This Window Open For Input & Game Inforamtion")
gameDisplay = pygame.display.set_mode((800,600))
a = 0
b = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (a,b)
##gameDiff = difficulty()
gameGrid = grid()
display = displayInital(gameGrid)         
userGame = mainLoop(gameGrid)
##LbList = Leaderboard()
##uLB = updateLB(Lb, gameGrid, userGame)
