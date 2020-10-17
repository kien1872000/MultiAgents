# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"
      

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    
        "*** YOUR CODE HERE ***"
        newFood = newFood.asList()
        min_dFood = float("inf")
        ghostPosList = successorGameState.getGhostPositions()
        for ghostPos in ghostPosList:
          if(manhattanDistance(newPos,ghostPos)<2):
            i =  ghostPosList.index(ghostPos)
            if newScaredTimes[i] == 0:
              return -float("inf")  
        for foodPos in newFood:
          min_dFood = min(min_dFood, manhattanDistance(newPos, foodPos))

        return successorGameState.getScore() + 1/min_dFood

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        return self.getValue(gameState,0, 0)[1]
        util.raiseNotDefined()

    def getValue(self, gameState, index, depth):
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:
            return (gameState.getScore(), "")
        if index == 0:
            return self.maxValue(gameState, index, depth)
        return self.minValue(gameState, index, depth)

    def maxValue(self, gameState, index, depth):
        legalActions = gameState.getLegalActions(index)
        max_value = float("-inf")
        max_action = ""
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v= self.getValue(successor, successor_index, successor_depth)[0]
            if v > max_value:
                max_value = v
                max_action = action
        return (max_value, max_action)

    def minValue(self, gameState, index, depth):
        legalActions = gameState.getLegalActions(index)
        min_value = float("inf")
        min_action = ""
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v = self.getValue(successor, successor_index, successor_depth)[0]
            if v < min_value:
                min_value = v
                min_action = action
        return (min_value, min_action)
    
class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        return self.getValue(gameState,0, 0, float("-inf"), float("inf"))[1]
        util.raiseNotDefined()

    def getValue(self, gameState, index, depth, alpha, beta):
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:
            return (self.evaluationFunction(gameState), "")
        if index == 0:
            return self.maxValue(gameState, index, depth, alpha, beta)
        return self.minValue(gameState, index, depth, alpha, beta)

    def minValue(self, gameState, index, depth, alpha, beta):
        legalActions = gameState.getLegalActions(index)
        min_value = float("inf")
        min_action = ""
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v = self.getValue(successor, successor_index, successor_depth, alpha, beta)[0]
            if v < min_value:
                min_value = v
                min_action = action
            if min_value < alpha:
                return (min_value, min_action)
            beta = min(min_value, beta)
        return (min_value, min_action)

    def maxValue(self, gameState, index, depth, alpha, beta):
        legalActions = gameState.getLegalActions(index)
        max_value = float("-inf")
        max_action = ""
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v= self.getValue(successor, successor_index, successor_depth, alpha, beta)[0]
            if v > max_value:
                max_value = v
                max_action = action
            if max_value>beta:
              return (max_value, max_action)
            alpha = max(alpha, max_value)
        return (max_value, max_action)
class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        return self.getValue(gameState, 0, 0)[1]
        util.raiseNotDefined()
    def getValue(self, gameState, index, depth):
        if len(gameState.getLegalActions(index)) == 0 or depth == self.depth:
            return (self.evaluationFunction(gameState),"")
        if index == 0:
            return self.maxValue(gameState, index, depth)
        return self.expectedValue(gameState, index, depth)

    def maxValue(self, gameState, index, depth):
        """
        Returns the max utility value-action for max-agent
        """
        legalActions = gameState.getLegalActions(index)
        max_value = float("-inf")
        max_action = ""
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v = self.getValue(successor, successor_index, successor_depth)[0]
            if v > max_value:
                max_value = v
                max_action = action
        return (max_value, max_action)

    def expectedValue(self, gameState, index, depth):
        legalActions = gameState.getLegalActions(index)
        expected_value = 0
        successor_probability = 1.0 / len(legalActions)
        for action in legalActions:
            successor = gameState.generateSuccessor(index, action)
            successor_index = index + 1
            successor_depth = depth
            if successor_index == gameState.getNumAgents():
                successor_index = 0
                successor_depth += 1
            v= self.getValue(successor, successor_index, successor_depth)[0]
            expected_value += successor_probability * v

        return (expected_value, "")
def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

