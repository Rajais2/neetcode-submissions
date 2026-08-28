class MinStack:

    def __init__(self):
        # Intiailzing our stacks
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        # Append the number to our main stack
        self.st.append(val)

        # If the value is smaller than our current
        # minimum, add it to our minimum stack
        if not self.minSt or val <= self.minSt[-1]:
            self.minSt.append(val)

    def pop(self) -> None:
        # Pop from our main stack
        value = self.st.pop()

        # Removing the value from our minimum stack if
        # the value we're removing was the minimum
        if value == self.minSt[-1]:
            self.minSt.pop()

    def top(self) -> int:
        # Simply return the top value of our main stack
        return self.st[-1]

    def getMin(self) -> int:
        # Simply return the top of our minimum stack
        return self.minSt[-1]
