class student:
   def __init__(self,name,rollno,age,gender):
      self.name=name
      self.rollno=rollno
      self.age=age
      self.gender=gender

class marks(student):
       def __init__(self,sub1,sub2,sub3,name,rollno,age,gender):
              self.sub1=sub1
              self.sub2=sub2
              self.sub3=sub3
              student.__init__(self, name, rollno, age, gender)
class Display(marks):
        def __init__(self , sub1, sub2,sub3 ,name, rollno, age, gender):
         marks.__init__(self,sub1,sub2,sub3,name,rollno,age,gender )
         self.total = sub1 + sub2+sub3

        def out_put(self):
            print("Name:", self.name)
            print("Rollnumber:", self.rollno)
            print("Total:", self.total)
sub1=int(input("enter your English mark="))
sub2=int(input("enter your Maths mark="))
sub3=int(input("enter yor computer mark="))
name=str(input("enter your name="))
rollno=int(input("enter your rollnumber="))
age=int(input("enter your age="))
gender=str(input("enter your gender="))
object=Display(sub1,sub2,sub3,name,rollno,age,gender)
object.out_put()
