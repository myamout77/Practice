class Solution:
    def isValid(self, s: str) -> bool:
        stack = []                                                    ## create stack
        parantheses = {"(": ")", "[": "]", "{":"}"}                   ## create dictionary and store paranthesis pairs
        closed = list(parantheses.values())                           ## create a list for closed paranthesis which are the values of the paranthesis dictionary
        opened = list(parantheses.keys())                             ## create a list for closed paranthesis which are the values of the paranthesis dictionary
        found = False                                          ## create a bool variable that monitors when a successful opening and closing of brackets happens
        
        for i in s:                                                   ## search through the characters of the string
            if i in parantheses:                                      ## check if character is an open paranthesis
                if s.index(i) != (len(s) -1):                         ## makes sure that the paranthesis is not the last character
                    stack.append(i)                                   ## pushes paranthesis into end of stack
                else:
                    return False                                      ## if the open paranthesis inserted is the last character returns False
            if i in closed:                                           ## checks if character is a closed paranthesis
                if not stack:                                         ## checks if stack is empty, if yes returns false
                    return False  
                else:
                    if stack[-1] == opened[closed.index(i)]:          ## checks if the stack pushed value is valid
                        stack.pop()                                   ## removes pushed value from stack after successful open and close parantheses
                        found = True                                  ## successful removal of a parathesis pair
                    else:
                        return False
        if stack:                                        ## checks if anything in the stack is left, if yes, this means that not all paranthesis have been removed
            return False
        else:
            return found                                              ## returns True if successfully found parantheses pair, False if unsuccessful
