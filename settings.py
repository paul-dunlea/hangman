
class Settings:
    def __init__(self,lives, difficulty):
        self._lives=lives
        self._difficulty=difficulty
    def __str__(self):
        return ("lives left: %d difficulty: %s")%(self._lives,self._difficulty)
    def getlives(self):
        return self._lives
    def setlives(self,lives):
        if type(lives)==int or lives<=10:#limiting the instance variable self._lives to only integers and below or at 10
            self._lives=lives
        else:
            print("error")
    lives=property(getlives,setlives)
    def lifeloss(self):
        self._lives-=1
    def leveldiff(self,mylist):
        newlist=[]
        if self._difficulty=="easy":
            for i in mylist[0]:
                if len(i)<5 and len(i)!=0:
                    newlist.append(i)
        elif self._difficulty=="medium":
            for i in mylist[0]:
                if len(i)<9 and len(i)>4:
                    newlist.append(i)
        elif self._difficulty=="hard":
            for i in mylist[0]:
                if len(i)>8:
                    newlist.append(i)
        return newlist
        



    

            