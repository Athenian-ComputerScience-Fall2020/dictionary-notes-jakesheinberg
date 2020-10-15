# Use this to take notes on the Edpuzzle video. Try each example rather than just watching it - you will get much more out of it!
#  
student={'name':'John', 'age':'25','courses':['math','compSci']}

age=student.pop('age')

for key,value in student.items():
    print(key, value)
#del student['age']
#student['phone']='555-555'
#student.update({'name':'jane'})
#print(student.get('phone','Not Found'))
print(student)
print(age)
print(len(student))