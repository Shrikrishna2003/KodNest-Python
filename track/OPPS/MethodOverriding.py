class Developer:
    def work(self):
        print("Developer is working")

    def attendMeeting(self):
        print("Developer is attending the meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("JavaDeveloper is working on Java")

    def doJavaProject(self):
        print("JavaDeveloper is building a Java project")

class PythonDeveloper(Developer):
    def work(self):
        print("PythonDeveloper is working on Python")

    def doPythonProject(self):
        print("PythonDeveloper is building a Python project")
 
dev = Developer()
dev.work()
dev.attendMeeting()

javaDev = JavaDeveloper()
javaDev.work()
javaDev.doJavaProject()

pyDev = PythonDeveloper()
pyDev.work()
pyDev.doPythonProject()

    