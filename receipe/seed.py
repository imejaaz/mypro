
from faker import Faker

fake = Faker()
from receipe.models import *  # Import models from the correct module
import random




def Report():
    current_rak = -1

    ranks = Student.objects.annotate(total_marks=Sum('marks')).order_by('-total_marks')

    i = 1
    for rank in ranks:
        studentReport.objects.create(
            student=rank,
            Rank=i
        )
        i = i + 1

def marks_db():
    try:
        stO = Student.objects.all()
        stS = Subject.objects.all()

        for student in stO:
            for subject in stS:
                Marks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0,100)
                )

    except Exception as e:
        print(e)




def seed_db(n=10):
    try:
        for i in range(1, n):  # You might want to include the n value itself in the loop
            student_name = fake.name()
            student_address = fake.address()
            student_age = random.randint(20, 30)
            student_mail = fake.email()
            student_id = f'STU-0{random.randint(111, 999)}'

            dpr = Department.objects.all()
            l = len(dpr)
            l = l - 1
            student_dpr = dpr[random.randint(0, l)]

            sId_obj = StudentReg.objects.create(sReg=student_id)
            st_obj = Student.objects.create(
                studentEmail=student_mail,
                studentAddress=student_address,
                studentAge=student_age,  # Corrected field name
                studentName=student_name,
                studentId=sId_obj,  # Use the created StudentReg object
                department=student_dpr  # Use the selected department object
            )

    except Exception as e:
        print(e)

