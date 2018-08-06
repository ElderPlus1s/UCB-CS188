    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """

        successors = []
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            # state contains two elements
            # first is the coordinate and the second is the numbers of remaining corners
            # state = (coordinate, NumberOfCorner)
            "*** YOUR CODE HERE ***"
            position, corners = state
            x, y = position
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            
            if not self.walls[nextx][nexty]:
                nextPosition = (nextx, nexty)
                cornerTemp = tuple(c for c in corners if c != nextPosition) 
                nextState = (nextPosition, cornerTemp)
                cost = 1
                successors.append((nextState, action, cost))

        self._expanded += 1  # DO NOT CHANGE
        return successors