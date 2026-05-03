# Anything in here was analysis that did not make it into the final project due to not being interesting or relevant, 
# but was still calculated at one point during the development process.

import pandas as pd
import statistics as stat

df = pd.read_csv('student_performance_data.csv')

# Extracting columns
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

#Covariances
study_midterm_cov = stat.covariance(study, midterm)
study_final_cov = stat.covariance(study, final)
midterm_final_cov = stat.covariance(midterm, final)
study_overall_cov = stat.covariance(study, overall)
sleep_midterm_cov = stat.covariance(sleep, midterm)
sleep_final_cov = stat.covariance(sleep, final)
sleep_overall_cov = stat.covariance(sleep, overall)
att_study_cov = stat.covariance(att, study)
att_ass_cov = stat.covariance(att, ass)
att_midterm_cov = stat.covariance(att, midterm)
att_final_cov = stat.covariance(att, final)
part_midterm_cov = stat.covariance(part, midterm)
part_final_cov = stat.covariance(part, final)

print("Covariances:")
print("Study vs Midterm:", study_midterm_cov)
print("Study vs Final:", study_final_cov)
print("Midterm vs Final:", midterm_final_cov)
print("Study vs Overall:", study_overall_cov)
print("Sleep vs Midterm:", sleep_midterm_cov)
print("Sleep vs Final:", sleep_final_cov)
print("Sleep vs Overall:", sleep_overall_cov)
print("Attendance vs Study:", att_study_cov)
print("Attendance vs Assignments:", att_ass_cov)
print("Attendance vs Midterm:", att_midterm_cov)
print("Attendance vs Final:", att_final_cov)
print("Participation vs Midterm:", part_midterm_cov)
print("Participation vs Final:", part_final_cov)
print()

#Correlations:
study_midterm_corr = stat.correlation(study, midterm)
study_final_corr = stat.correlation(study, final)
midterm_final_corr = stat.correlation(midterm, final)
study_overall_corr = stat.correlation(study, overall)
sleep_midterm_corr = stat.correlation(sleep, midterm)
sleep_final_corr = stat.correlation(sleep, final)
sleep_overall_corr = stat.correlation(sleep, overall)
att_study_corr = stat.correlation(att, study)
att_ass_corr = stat.correlation(att, ass)
att_midterm_corr = stat.correlation(att, midterm)
att_final_corr = stat.correlation(att, final)
part_midterm_corr = stat.correlation(part, midterm)
part_final_corr = stat.correlation(part, final)

print("Correlations:")
print("Study vs Midterm:", study_midterm_corr)
print("Study vs Final:", study_final_corr)
print("Midterm vs Final:", midterm_final_corr)
print("Study vs Overall:", study_overall_corr)
print("Sleep vs Overall:", sleep_overall_corr)
print("Sleep vs Midterm:", sleep_midterm_corr)
print("Sleep vs Final:", sleep_final_corr)
print("Attendance vs Study:", att_study_corr)
print("Attendance vs Assignments:", att_ass_corr)
print("Attendance vs Midterm:", att_midterm_corr)
print("Attendance vs Final:", att_final_corr)
print("Participation vs Midterm:", part_midterm_corr)
print("Participation vs Final:", part_final_corr)