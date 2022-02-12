# Defines the lines and structure for the jumper's parachute.
class jumper:

    def __init__(self):
        # Each line, or string in the array is a chance for the player to get a letter wrong.
        # Perhaps in future versions, a character would be removed instead of an entire line.
        self.parachute = [' ___ ',
                        '/___\ ',
                        '\   /',
                        ' \ /']

        self.man = ['  o  ',
                    ' /|\ ',
                    ' / \ ',
                    '     ',
                    '^^^^^']
    
    # Removes the first line from the parachute.
    def cutLine(self):
        self.parachute.pop(0)