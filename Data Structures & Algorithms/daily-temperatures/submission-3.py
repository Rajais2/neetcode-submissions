class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initializing our final answer container
        finalAns = [0] * len(temperatures)

        # Creating our monotonic stack
        st = []

        # Begin traversing through all the temperatures
        for index in range(len(temperatures)):
            # Performing our monotonic stack operation here
            while st and temperatures[index] > temperatures[st[-1]]:
                # We have found a warmer day, so we pop 
                # the previous day
                previous_day = st.pop()

                # Storing how many days have passed for
                # the previous day
                finalAns[previous_day] = index - previous_day

            # Add the current day's index to our stack
            st.append(index)

        # Returning our final container which should hold all
        # the number of days
        return finalAns

