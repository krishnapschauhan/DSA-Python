class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == "" and goal == "":
            return True
        if len(s) == 1:
            return s == goal
        if s == goal and len(set(s)) == 1:
            return True
        if len(s) == len(goal):
            return goal in (s + s)




        
        