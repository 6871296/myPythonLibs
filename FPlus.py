import os
class FPlus():
    def __init__(self,file:str,notice=False):
        self.r=open(file,'r')
        self.w=open(file,'w')
        self.a=open(file,'a')
        for i in range(len(file)):
            if file[i]=='.' and '/' not in file[i::] and file[i::] not in ['txt','md','py','c','cpp','jar','json','html','swift','js','log']:
                self.x=open(file,'x')
                self.rb=open(file,'rb')
                self.wb=open(file,'wb')
                self.ab=open(file,'ab')
                self.text_readable=False
                if notice:
                    print("*Notice:This FPlus isn't text-readable, it's a ."+file[i::]+" file. please use read_x() or read_b() to read this FPlus.")
                break
            else:
                self.text_readable=True
                self.x=None
                self.rb=None
                self.wb=None
                self.ab=None
                break
        self.path=file
    def read(self):
        return self.r.read()
    
    def write(self,str:str):
        self.w.write(str)
    
    def read_b(self):
        if not self.text_readable:
            return self.rb.read()
        else:
            FileExistsError("This FPlus isn't byte-readable, please use read() or write() to read or write the file.")

    def wrte_x(self,str:str):
        if not self.text_readable:
            self.x.write(str)
        else:
            FileExistsError("This FPlus isn't byte-readable, please use read() or write() to read or write the file.")
    def write_b(self,str:str):
        if not self.text_readable:
            self.wb.write(str)
        else:
            FileExistsError("This FPlus isn't byte-readable, please use read() or write() to read or write the file.")

    def append_b(self,str:str,starting=0):
        if not self.text_readable:
            self.ab.seek(len(self.ab.read()-starting,2))
            self.ab.write(str)
        else:
            FileExistsError("This FPlus isn't byte-readable, please use read() or write() to read or write the file.")
    
    def append(self,str:str,starting=0):
        self.a.seek(len(self.a.read()-starting,2))
        self.a.write(str)

    def close(self):
        self.r.close()
        self.w.close()
        self.a.close()
        if not self.text_readable:
            self.x.close()
            self.rb.close()
            self.wb.close()
            self.ab.close()
        del self
    
    def move_to(self,path:str):#please use i=i.move_to() to save the file!
        pth=self.path
        self.close()
        os.rename(pth,path)
        return FPlus(path,True)
    
    def save(self): #You can also change self.path and use save() to move the file! and, please use i=i.save() to save the file!
        path=self.path
        self.close()
        return FPlus(path,True)


def to_FPlus(file:__file__):
    return FPlus(os.path.abspath(file))