#object oriented programing 

'''class student:
    name="yash singh" #attributes (variables)
    age="20"
#creating objects 
s1=student()# assign name of class
print(s1.name)#it will print the attribute 
print(s1.age)

class vehicles:
    colour="black"
    petrolordiesel="petrol"
    mileage="10"
#creating object 
car=vehicles()
car.colour="blue"
print(car.colour)   

bike=vehicles()
print(bike.petrolordiesel)

aeroplane=vehicles()
print(aeroplane.mileage)
print(aeroplane.colour)

class car:
    brand="mahindra"
    model="scorpio"
    manufactured="2019"
    run="100000km"
obj=car()
print("brand name of the car",obj.brand)
print("how many kilometers it has run till now" ,obj.run)


# two objects can assicess any attributes
class laptop:
    brand="macbook"
    RAM="8 GB"
    processor="RYZEN"
    price="40000"

laptop1=laptop()
laptop1.brand="lenovo"
laptop1.RAM="16 GB"
print("the laptop brand is ",laptop1.brand)
print("the ram of the laptop is ",laptop1.RAM)
print("the price of the laptop is",laptop1.price)

laptop2=laptop()
laptop2.price="100000"
print("the laptop brand is ",laptop2.brand)
print("the ram of the laptop is ",laptop2.RAM)
print("the price of the laptop is",laptop2.price)
'''

# init constructor : a function that runs auomatically whenever an object is created 
#used as an initial attributes
'''
class student:
    school="abc international"
    def __init__(self,name,course):
        #print("whenever a new object is created i am called automaticaly")
        #print(self)# this will print the location of the object
        self.name=name
        self.course=course
    def hello(self):# methods  : function inside class 
        print("HELLO",self.name)


student1=student("ankit","bsc")# init will automaticaly get called
student1.hello()
print("name of the student is",student1.name )# note you will get the same output as the init give in print(self)
print("course of the student is",student1.course)

student2=student("sumit","b.tech")
print("name of the student is",student2.name)
print("course of the student is",student2.course)'''


#creat clas student that has 3 marks and has a method average();

class student:
    #staticmethod
    def __init__(self,name,listofmarks):
        self.name=name
        self.listofmarks=listofmarks

    def average(self):
        sum=0
        for eachvalue in self.listofmarks:
            sum=sum+eachvalue
        average=sum/4    
        print("average is:",average)
student1=student("aditya",[90,89,98,98])
student1.average()



