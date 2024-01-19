#student no:122452762
from settings import Settings
import random
from wordlist_file import *
import os

class Game(Settings):#inheritance
    def __init__(self,filename,lives,difficulty):
        self._changes=2
        self._filename=filename
        self._word=""
        self._hidden=""
        self._lettersGuessed=""
        self._content=[]
        super().__init__(lives,difficulty)
    def __str__(self):
        return ("word: %s letters you've guess already: %s %s"%(self._hidden,self._lettersGuessed,super().__str__()))#interpolation
    def __eq__(self,other):
        if self._word==other or self._lives==0:
            return True
        return False
    def getword(self):
        return self._hidden
    def setword(self,ans):
        if len(self._content)!=0 and ans=="y":
            index=random.randint(0,len(self._content)-1)
            self._word=self._content[index]
            self._content.pop(index)
            self._hidden="_"*len(self._word)
            self._changes-=1
        else:
            print("error")
    word=property(getword,setword)
    def getwordlist(self):
        return self._content
    def setwordlist(self,aclass):
        if os.path.isfile(self._filename):#making sure that the file exists
            aclass.thelist=self._filename#aggregation
            self._content.append(aclass.thelist)
        else:
            raise ValueError
    wordlist=property(getwordlist,setwordlist)

    def checkletter(self,x):
        if x not in self._lettersGuessed:
            self._lettersGuessed+=x+"-"
        if x in self._word:
            return True
        else:
            return False
    def foundletter(self,x):
        for i,j in enumerate(self._word):
            if j==x:
                self._hidden=self._hidden[:i]+j+self._hidden[i+1:]
    def wrongguess(self):
        super().lifeloss()
    def checkwin(self):
        if self._hidden==self._word:
            return True
    def guessword(self,x):
        if x==self._word:
            return True
    def level(self):
        self._content=super().leveldiff(self._content)
        return self._content
    def randomWords(self):
        index=random.randint(0,len(self._content)-1)
        self._word=self._content[index]
        self._content.pop(index)
        self._hidden="_"*len(self._word)
if __name__=="__main__":
    try:
        file="/Users/pauljosephdunlea/Desktop/project/words.txt"#make sure to change this directory
        diff=input("what difficulty do you want to pick [easy|medium|hard]: ")        
        lives=int(input("how much lives do you want [<=10]: "))
        game=Game(file,lives,diff)
        game.wordlist=gamelist
        game.level()
        game.randomWords()
        change=input("amount of changes: %d,this is how long you're word is: %s, do you want to change [y/n]: "%(game._changes,game.word))
        while change=="y":
            game.word=change
            if game._changes!=0:
                change=input("changes left: %d,word: %s, change[y/n]: "%(game._changes,game.word))
            else:
                print("word: %s, you ran out of changes"%(game.word))
                break
        while game._lives!=0:
            print(game)
            letter=input("guess a letter: ")
            if game.checkletter(letter):
                game.foundletter(letter)
            else:
                game.wrongguess()
            if game.checkwin():
                print("you won the word was %s"%(game._word))
                break

        if game==0:
            print("you lose the word was %s"%(game._word))
    except ValueError as ve:
        print(ve)
    except ImportError as ie:
        print(ie)
    except Exception as ex:
        print(ex) 





        
    

