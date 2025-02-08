from app import db,Student,app

with app.app_context():
    student_john = Student(firstname='john', lastname='doe',
                        email='jd@example.com', age=23,
                        bio='Biology student')
    db.session.add(student_john)
    db.session.commit()

'''
Can use flask shell

>flask shell
>sammy = Student(firstname='Sammy',
               lastname='Shark',
               email='sammyshark@example.com',
               age=20,
               bio='Marine biology student')

carl = Student(firstname='Carl',
               lastname='White',
               email='carlwhite@example.com',
               age=22,
               bio='Marine geology student')

db.session.add(sammy)
db.session.add(carl)
db.session.commit()
'''
