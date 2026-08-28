class Solution:
    def isValid(self, s: str) -> bool:
        # If our string is empty, it is automatically
        # not empty
        if not s:
            return False
        
        # Creating our stack
        st = []

        # Now traversing through each character in the string
        for character in s:
            # Checking if the current character is an opening bracket
            if character == '(' or character == '[' or character == '{':
                # If it is, simply append the character
                st.append(character)
            elif character == ')':
                # If we have a closing parenthese, checking if we have
                # a corresponding open parenthese
                if not st or st[-1] != '(':
                    # If not, then it is not valid
                    return False

                # Remove the top character from our stack
                st.pop()
            elif character == ']':
                # If we have a closing bracket, checking if we have
                # a corresponding open bracket
                if not st or st[-1] != '[':
                    # If not, then it is not valid
                    return False

                # Remove the top character from the stack
                st.pop()
            elif character == '}':
                # If we have a closing curly brace, checking if we have
                # a corresponding open curly brace
                if not st or st[-1] != '{':
                    # If not, then it is not valid
                    return False

                # Remove the top character from the stack
                st.pop()

        # If the stack is empty, that means the string
        # is valid
        return not st


            
