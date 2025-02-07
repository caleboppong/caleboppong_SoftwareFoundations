#----Software Foundations Assessment
#--Generated  : 27.12.2024 - Caleb Oppong
#--Modified : 20/01/2025 - Caleb Oppong
#--Description : Python file v004

#This functions determine the grade input of students based on their average score
def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 95:
        return 'A'
    elif average >= 85:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

#-----End Funtions---------------

# importing csv file
import csv



# starting the students list
students = []

# reading csv file
#with open('Students_input.csv','r') as file:
with open('Students_input.csv','r') as file:
        # creating a csv reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader) 
        
        # extracting field names through first row
        for row in reader:
            name, geography, history, maths = row
            #average = calculate_average([int(math), int(science), int(english)])
            m_grade = assign_grade(int(geography))
            s_grade = assign_grade(int(history))
            e_grade = assign_grade(int(maths))
            students.append([name, geography, m_grade, history, s_grade, maths, e_grade])

with open('Students_output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Geography', 'Geography_Grade','History','History_Grade', 'Maths', 'Maths_Grade'])
        writer.writerows(students)

print('Results saved to Student_output.csv')