class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # If we have no tokens, sum is 0
        if len(tokens) == 0:
            return 0
        
        # Creating our stack
        st = []

        # Initializing our overall total sum
        total = 0

        # Traversing through each individual token
        for token in tokens:
            # Checking if the token is a number
            if token not in '+-*/':
                # If it is, push it onto the stack
                st.append(int(token))
            else:
                # Getting our two operands since we know
                # we are dealing with a mathematical operation
                if st:
                    right = st.pop()
                    left = st.pop()

                # Checking what operation we're handling and
                # acting accordingly
                if token == '+':
                    st.append(right + left)
                elif token == '-':
                    st.append(left - right)
                elif token == '*':
                    st.append(right * left)
                else:
                    st.append(int(left / right))

        # The top value in our stack holds the
        # final answer
        return st[-1]



            

        