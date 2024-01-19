class Words:
    def __init__(self):
        self._content=[]
    def getcontent(self):
        return self._content
    def setcontent(self,filename):
        file=open(filename,"r")
        file=file.read()
        file=file.replace("\n"," ")
        self._content=file.split(" ")
        return self._content
    thelist=property(getcontent,setcontent)
    
gamelist=Words()
