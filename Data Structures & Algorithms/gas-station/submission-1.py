class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Checking to see if a circuit is 
        # even possible
        if sum(gas) - sum(cost) < 0:
            return -1
        
        # We now know some candidate exists
        currentGas, start = 0, 0

        # Begin our scanning...
        for index in range(len(gas)):
            # Calculating our current gas
            currentGas += gas[index] - cost[index]

            # If our candidate fails, reset our current
            # gas and move our starting position up
            if currentGas < 0:
                start = index + 1
                currentGas = 0

        # Returning the candidate's index
        return start
