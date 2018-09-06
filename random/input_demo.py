names =  input('Enter names separated by commas:').split(',')
assignments =  input('Enter assignment counts separated by commas:').split(',')
grades =  input('Enter grades separated by commas (0-100):').split(',')

if len(names) != len(assignments) or len(assignments) != len(grades):
	print("Error: Lists were not equal length")
	exit()

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

print(names,assignments,grades)

def get_potential_grade(assignment_count, grade):
	potential_grade = int(assignment_count) * 2 + float(grade)
	return potential_grade

for name, assignment, grade in zip(names, assignments, grades):
	potential_grade = get_potential_grade( assignment, grade )
	final_message = message.format(name, assignment, grade, potential_grade )
	print( final_message )