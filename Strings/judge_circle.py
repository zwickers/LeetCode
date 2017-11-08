class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        # the 'trick' to determining if the robot
        # is back in it's starting position is just
        # checking to see if the U's and D's are balanced
        # and if the the L's and R's are balanced
        
        if moves.count('D') != moves.count('U'):
            return False
        
        if moves.count('L') != moves.count('R'):
            return False
        
        return True
