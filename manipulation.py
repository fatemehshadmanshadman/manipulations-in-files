import os,shutil

class Manipulator:
    def __init__(self) -> None:
        pass
    
    def read(self,file_address,type):
        contents=[]
        if type=="line":
            file=open(file_address,mode="r")
            
            while True:
                temp=file.readline()
                contents.append(temp) 
                
                if not temp:
                    file.close()
                    break

        elif type=="lines":
            file=open(file_address,mode="r",encoding="UTF8")
            contents=file.readlines()
            file.close()
        else:
            print("check correct method")
            
        return " ".join(contents)
    
    def write(self,file_address,content,mod="a+"):
        file=open(file_address,mod)
        file.write(content+'\n')
        return "succeed"
    
    def copy(self,f1,f2):
        content=self.read(f1,"lines")
        self.write(f2,content)
        
    def newfolder(self,folder_address):
        os.mkdir(folder_address)
    
    def exist(self,address):
        if os.path.exists(address):
            return "this file is exist"
        else:
            return "this file not exist"
        
    def remove(self,address):
        for item in address:
            if os.path.isfile(item):
                os.remove(item)
            elif os.path.isdir:
                shutil.rmtree(item)
        
    
mani=Manipulator()

content="i'm fine"
# print(mani.read("manipulate.txt",type="line"))
# print(mani.read("manipulate.txt",type="lines"))
# print(a.write("manipulate.txt",content))
# print(mani.exist("manipulate.txt"))
# mani.copy("manipulate.txt","manipulatecopy.txt")   
# mani.newfolder("project/folder")
# mani.remove(["manipulatecopy.txt"])   