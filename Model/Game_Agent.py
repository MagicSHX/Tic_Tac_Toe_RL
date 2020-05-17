import numpy as np

class game_agent:
    def __init__(self, input_string, status):
        self.input_string = input_string
        self.status = status
        self.verify_Matrix = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        self.verify_Matrix = np.array(self.verify_Matrix)
        #print(self.verify_Matrix.argmax())
    def restart(self):
        print(self.input_string)
        return('abc')
    def next_action(self):
        print('next action')
    def result(self):
        if self.input_string[1,1] == 1:
            return True
        else:
            return False
    def verify_result(self):
        status = False
        for i in range(0,8):
            a = self.input_string[self.verify_Matrix[i,0]]
            b = self.input_string[self.verify_Matrix[i,1]]
            c = self.input_string[self.verify_Matrix[i,2]]
            #print(a,b,c)
            if verify_3_same_value(a,b,c) == True:
                #print(1)
                #print(a,b,c)
                status = True
                break
        return status

def verify_3_same_value(a,b,c):
    if (a == b) & (b == c) & (a != 0):
        return True
    else:
        return False