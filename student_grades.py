student_grades = {
  "Jeffrey": 72,
  "Dean": 84,
  "Morgan": 92,
  "Walker": 90
}

def calculate_average_grade(grades_dict):
  max = 0
  for grade in grades_dict.values():
    max += grade 
  average = max / len(grades_dict) 
  return average

final = calculate_average_grade(student_grades)
print(f"{final}")


  
  
