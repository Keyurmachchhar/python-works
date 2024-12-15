class Teacher:
    __stuName = None
    __subject = None
    __basic = None
    __DA = None
    __HRA = None
    __salary = None

    def get_data(self):
        Teacher.__stuName = input("Enter student name :")
        Teacher.__stuName = input("Enter subject name :")
        Teacher.__basic = int(input("Enter basic : "))
        Teacher.__DA = int(input("Enter DA : "))
        Teacher.__HRA = int(input("Enter HRA : "))
    
    def put_data(self):
        print("Student Name :",Teacher.__stuName)
        print("Subject Name :",Teacher.__subject)
        print("Basic :",Teacher.__basic)
        print("DA :",Teacher.__DA)
        print("HRA :",Teacher.__HRA)
        print("Slalry :",(Teacher.__basic+Teacher.__DA+Teacher.__HRA))

obj = Teacher()

obj.get_data()
obj.put_data()