class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Create our stack
        st = []

        # Traverse through all asteroids
        for asteroid in asteroids:
            # Tracking if the asteroid survives
            alive = True

            # Check for potential collisions
            while st and st[-1] > 0 and asteroid < 0:
                # Get our top asteroid
                top = st[-1]

                # Handling all three cases
                if abs(top) < abs(asteroid):
                    st.pop()
                    continue
                elif abs(top) == abs(asteroid):
                    st.pop()
                    alive = False
                    break
                elif abs(top) > abs(asteroid):
                    alive = False
                    break

            # If the current asteroid is still alive,
            # we have to add it to our stack
            if alive:
                st.append(asteroid)

        # Return our final stack
        return st