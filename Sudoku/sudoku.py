#  Solve Sudoku
# This is an simple demo of solve Sudoku using Depth-First Traversal
# someday will try to use Dancing Links
# Coding by ALLENSLL in Apr 9th,2016
import time

class sudoku:
    class point:
        def __init__(self,x,y):
            self.x = x
            self.y = y
            self.available = []
            self.value = 0
        
    def __init__(self,s):
        self.S = s
        self.unList = []
        self.t_start = 0
        self.t_end = 0
        self.t_used = 0
        if len(self.S) == 9:
            for i in range(9):
                if len(self.S[i]) != 9:
                    print('\nNot a sudoku!(9x9)')
                    exit()
        else:
            print('\nNot a sudoku!(9x9)')
            exit()
        for i in range(9):
            for j in range(9):
                if self.S[i][j] not in range(0,10):
                    print('\nNot a sudoku!(0~9)')
                    exit()
        
        if self.checkRepeat():
            print('\nNot a sudoku!(no repeat)')
            exit()
        self.showSudoku()
        
    def do(self):
        self.t_start = time.time()
        self.initUnList()
        self.tryInsert()
        
    def checkRepeat(self):
        temp = []
        
        for i in range(9):
            for j in range(9):
                if self.S[i][j] != 0:
                    temp.append(self.S[i][j])            
            if len(temp) != len(set(temp)):
                return True
            temp = []
        for i in range(9):
            for j in range(9):
                if self.S[j][i] != 0:
                    temp.append(self.S[j][i])
            if len(temp) != len(set(temp)):
                return True
            temp = []
        for i in range(3):
            for j in range(3):
                for m in range(3):
                    for n in range(3):
                        if self.S[i*3+m][j*3+n] != 0:
                            temp.append(self.S[i*3+m][j*3+n])
                if len(temp) != len(set(temp)):
                    return True
                temp = []
        return False
        
    def getRow(self,p):
        row = set(self.S[p.x])
        row.remove(0)
        return row
    
    def getCol(self,p):
        col = []
        for i in range(9):
            col.append(self.S[i][p.y])
        col = set(col)
        col.remove(0)
        return col
    
    def getBlock(self,p):
        block_x = p.x//3
        block_y = p.y//3
        block = []
        for i in range(block_y*3,block_y*3+3):
            block.append(self.S[block_x*3][i])
            block.append(self.S[block_x*3+1][i])
            block.append(self.S[block_x*3+2][i])
        block = set(block)
        block.remove(0)
        return block

    def initUnList(self):
        for i in range(9):
            for j in range(9):
                if self.S[i][j] == 0:
                    p = self.point(i,j)
                    for k in range(1,10):
                        if k not in self.getRow(p):
                            if k not in self.getCol(p):
                                if k not in self.getBlock(p):
                                    p.available.append(k)
                    self.unList.append(p)
        
    def tryInsert(self):
        p = self.unList.pop()
        for i in p.available:
            p.value = i
            if self.checkPoint(p):
                self.S[p.x][p.y] = p.value
                if len(self.unList) <=0:
                    self.t_end = time.time()
                    self.t_used = self.t_end - self.t_start
                    self.showSudoku()
                    print('\nUsed Time: %f s'%(self.t_used))
                    exit()
                else:
                    self.tryInsert()
            self.S[p.x][p.y] = 0
        p.value = 0
        self.unList.append(p)

    def checkPoint(self,p):
        if p.value not in self.getRow(p) and p.value not in self.getCol(p) and p.value not in self.getBlock(p):
            return True
        else:
            return False
        
    def showSudoku(self):
        for n in range(9):
            for m in range(9):
                print('%d '%(self.S[n][m]),end=' ')
            print(' ')
        print('')

if __name__=='__main__':
    s = sudoku([
            [8,0,0,0,0,0,0,0,0],
            [0,0,3,6,0,0,0,0,0],
            [0,7,0,0,9,0,2,0,0],
            [0,5,0,0,0,7,0,0,0],
            [0,0,0,0,4,5,7,0,0],
            [0,0,0,1,0,0,0,3,0],
            [0,0,1,0,0,0,0,6,8],
            [0,0,8,5,0,0,0,1,0],
            [0,9,0,0,0,0,4,0,0],
            ])
    s.do()
            
            
            
            