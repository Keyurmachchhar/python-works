class Employee:

    __Ename = None
    __Eage = None
    __Esalary = None

    def get_data(self):
        self.__Ename = input("Enter Employee Name : ")
        self.__Eage = int(input("Enter Employee Age : "))
        self.__Esalary= int(input("Enter Employee Salary : "))
    
    def put_data(self):
        print()
        print("Employee Name :",self.__Ename)
        print("Employee Age :",self.__Eage)
        print("Employee Salary :",self.__Esalary)
    
obj = Employee()

obj.get_data()
obj.put_data()