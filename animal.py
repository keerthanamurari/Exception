class Animal:
   
    def __init__(self, name="",guess=[]):
        self.name = name
        self.guess = guess
                
 
    def guess_who_am_i(self):
        print(" ")
        print("I will give you 3 hints, guess what animal I am")
        print(" ")
 
        for line in self.guess:
            print(line)
                userinput = input("Who am I?:")
                print(" ")
                if(userinput == self.name):
                    print("You got the answer")
                    break
                else:
                    print("Nope, try again!")
                    print(" ")
 
        print(" ")
        print(" ")
        if(userinput == self.name):
            return
        else:
            print("I'm out of hints! The answer is: " ,self.name)
                        
 
e = Animal("elephant",['I am the largest land-living mammal in the world',
                 'I have two tusks',
                 'My Name starts with e and ends with t'])
 
t = Animal("tiger",['I am the biggest cat',
                 'I come in black and white or orange and black',
                 'My Name starts with t and ends with r'])
 
l = Animal("lion",['I am The king of Jungle',
                 'My color is golden yellow',
                 'My name starts with L and ends with n'])
 
b = Animal("bear",['I am fat and black or brown and I love fish',
                 'I also comes in white color',
                 'My name starts with B and ends with R'])
 
 
 
e.guess_who_am_i()
t.guess_who_am_i()
l.guess_who_am_i()
b.guess_who_am_i()
