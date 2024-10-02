from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self,name,grade,classes,gets_transportation=False):
        super().__init__(name,grade,classes)
        self.gets_transportation=gets_transportation

    def gets_transportation_message(self):
        if self.gets_transportation is True:
            return f"{self.name} gets ride to school"
        else: 
            return f"{self.name} does not get ride to school"

    def summary(self):
        student_summary = super().summary()
        transportation_message=self.gets_transportation_message()
        return "\n".join((student_summary,transportation_message))



        

# add MiddleSchoolStudent here
