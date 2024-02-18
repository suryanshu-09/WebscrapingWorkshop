'''
class friend():
    def __init__(self,
                 name='',
                 phone='00000',
                 email='',
                 instaID=''):
        self.name = name
        self.phone = phone
        self.email = email
        self.instaID = instaID
    def printDetails(self):
        print(self.name, self.phone, self.email, self.instaID)
    def update(self,
               newName='',
               newPhone='0000',
               newEmail='',
               newInstaID=''):
        if (newName !=''):
            self.name = newName
        if (newPhone !=''):
            self.phone = newPhone
        if (newEmail !=''):
            self.email = newEmail
        if (newInstaID !=''):
            self.instaID = newInstaID
        self.printDetails()
friend1=friend(name='Tug',
               phone='12325',
               email='tugby@vit.com')
friend1.update(newName='Carlos')
class stud():
    def __init__(self,**info):
        self.info = []
        for x in range(len(info)):
            self.info.append(list(info.values())[x])
    def PrintInfo(self):
        return self.info
    def __iter__(self):
        inform = 0
        return self.info[inform]
    def __next__(self):
        x = inform
        inform += 1
        return self.info[x]
person1 = stud(name='Hauz',age='21')
print(next(myiter))class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

#print(*stud.PrintInfo(person1))
#print(stud.__next__(stud.__iter__(person1)))
'''
