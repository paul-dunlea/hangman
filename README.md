# hangman project
the goal of my work was to make a basic hangman game using object oriented programming design and language features of python also
my main goal was i wanted my program to be as user friendly as possible i did this but letting the user to input their own data
and other features, i have 4 files in total, 3 of them contain classes and the other 1 was a txt file that just contained random 
words. i demonstrated many techniques such as encapsulation, inheritance, aggregation, etc.

the classes Game and Settings are different because the features in settings allows the user to manually change something(within 
limits) that will fit their preference, the game class does allow features to be changed but its main purpose is to check whether
the user has won,lost,guessed wrong or right

the class called Words and txt file called hangman_words.txt were used to demonstrate how a list of random words could be 
created, what i did was i made a property in Words called thelist in this i had setcontent and getcontent, setcontent 
has an argument for the file name then it reads the txt files and splits it into a list called content which i make in the 
constructor of the class, i make an object for Words export over to the hangman.py file and aggregate it into the list using
a setter in the class

Examples of OOP and other features that i have learnt through this project:
class definition - i made both classes
encapsulation with constructors getters/setters and properties - in the constructors and methods of both my classes i do this
encapsulation - adding checks to confirm the data types passed to the contructors and setters in both classes if python throws
                an error i made it so that it prints back a user friendly error message
inheritance - super class is Settings, Settings class is inherited by Game class.
inhertiance - extension of the Settings class in the Game class.Both classes have string classes
getters and setters - i used getters and setters across all 3 classes i used to determine whether an input is valid and to show
                    it to the user, etc.
aggregation -  in the constructors i have used aggregation to define the attributes, example self._word=word
aggregation - i also used aggregation get the list of random words
operator overloading - defined the meaning of operations i used with methods called __eq__ and __nt__
interpolation - in the __str__ method i returned a string with the attributes of the Game class using interpolation


