

def getValidMoves(curr, leftNeighbours, rightNeighbours):
   result = []
   if (curr.lower() == 'o'):
      return result
   if (len(leftNeighbours) == 2):
      if (leftNeighbours[0].lower() == 'x' and leftNeighbours[1].lower() == 'o'):
         result.append('L')
   if (len(rightNeighbours) == 2):
      if (rightNeighbours[0].lower() == 'x' and rightNeighbours[1].lower() == 'o'):
         result.append('R')
   return result

def checkAllValidMoves(gameBoard):
   i = 0
   allValidMoves = []
   for p in gameBoard:
      leftNeighbours = getLeftNeighbours(gameBoard, i)
      rightNeighbours = getRightNeighbours(gameBoard, i)
      validMoves = getValidMoves(p, leftNeighbours, rightNeighbours)
      for d in validMoves:
         allValidMoves.append((i, d))
      i += 1

   return allValidMoves

def getLeftNeighbours(gameBoard, index):
   if (index - 2 >= 0):
      return [gameBoard[index - 1], gameBoard[index - 2]]
   return []


def getRightNeighbours(gameBoard, index):
   if (index + 2 < len(gameBoard)):
      return [gameBoard[index + 1], gameBoard[index + 2]]
   return []

def checkWin(gameBoard):
   pegCount = 0
   for p in gameBoard:
      if (p.lower() == 'x'):
         pegCount += 1
   if (pegCount == 1):
      return True
   return False

def jump(gameBoard, validMove):
   lst = list(gameBoard)
   if (validMove[1] == 'L'):
      lst[validMove[0]] = 'o'
      lst[validMove[0] - 1] = 'o'
      lst[validMove[0] - 2] = 'X'
   if (validMove[1] == 'R'):
      lst[validMove[0]] = 'o'
      lst[validMove[0] + 1] = 'o'
      lst[validMove[0] + 2] = 'X'

   gameBoard = ''.join(lst)
   return gameBoard

def findPath(gameBoard, path):
   possibleMoves = checkAllValidMoves(gameBoard)
   if checkWin(gameBoard):
      return possibleMoves
   for move in possibleMoves:
      newBoard = jump(gameBoard, move)
      path = findPath(newBoard, path)
      if path is not None:
          return [move] + path
   return None

def pegsSolution(gameBoard):
   # Program your solution here
   return findPath(gameBoard, [])


