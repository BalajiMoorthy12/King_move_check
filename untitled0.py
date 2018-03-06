class direction:
    def __init__(self):
        self.left=(1,9,17,25,33,41,49,57)
        self.right=(8,16, 24, 32, 40, 48, 56, 64)
    def front_check(self,st):
    	start=int(self,st)
    	if start not in range(54,65) and (start+8) not in range(54,65):
    		return True
    	else:
    		return False    		
    def back_check(self,st):
    	start=int(self,st)
    	if start not in range(1,9) and (start-8) not in range(1,9):
    		return True
    	else:
    		return False
    def left_check(self,st):
        if int(st) not in self.left : return True
        else: return False   
    def right_check(self,st):
        if int(st) not in self.right : return True
        else: return False

if __name__ == '__main__':
    Start = input()
    Dest = input()
    objdir=direction()
    print(objdir.left)
    print(objdir.left_check(Start))