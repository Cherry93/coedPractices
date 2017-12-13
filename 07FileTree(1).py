'''

'''
import os
class Count:
    def __init__(self,dirCount,fileCount):
        self.dirCount = dirCount
        self.fileCount = fileCount
    def __str__(self):
        return dirCount and fileCount

class PrintFileTree(Count):
     def __init__(self,path,deep):
      super(PrintFileTree, self).__init__(dirCount,fileCount)
      self.path = path
      self.deep = deep
def printFileTree():
    files = os.listdir(self.path)

    for f in files:
        fpath = path + "/" + f
        print("|--"*self.deep,fpath)

        if os.path.isdir(fpath):
            PrintFileTree.printFileTree(fpath,self.deep + 1)
            self.dirCount += 1
        else:
            self.fileCount += 1
            pass

       # return dirCount,fileCount

if __name__ == '__main__':

  b = PrintFileTree(r"E:/MyProjects/",0)
  print(b.printFileTree)
  c = Count()
  print(c)
  # dirCount,fileCount =
  printFileTree()
  # print(dirCount,fileCount)
