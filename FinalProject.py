import math
import numpy as np
import pandas as pd
import statistics as stat

df = pd.read_csv('student_performance_data.csv')
print(df.head())

gender = df['gender']
study = df['study_hours_per_day']
att = df['attendance_percentage']
ass = df['assignment_score']
midterm = df['midterm_score']
final = df['final_exam_score']
part = df['participation_score']
internet = df['internet_access']
extra = df['extra_classes']
parent = df['parent_education']
sleep = df['sleep_hours']
overall = df['overall_score']
grade = df['grade']

