import math
import numpy as np
import pandas as pd
import statistics as stat

df = pd.read_csv('student_performance_data.csv')
print(df.head())


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


# Finding the covariace between possibly related columns
study_overall_cov = stat.covariance(study, overall)
att_overall_cov = stat.covariance(att, overall)
ass_overall_cov = stat.covariance(ass, overall)
part_overall_cov = stat.covariance(part, overall)
sleep_overall_cov = stat.covariance(sleep, overall)
midterm_overall_cov = stat.covariance(midterm, overall)
final_overall_cov = stat.covariance(final, overall)

study_midterm_cov = stat.covariance(study, midterm)

study_final_cov = stat.covariance(study, final)
midterm_final_cov = stat.covariance(midterm, final)

print("Covariances:")
print("Study vs Overall:", study_overall_cov)
print("Attendance vs Overall:", att_overall_cov) # Positive correlation
print("Assignments vs Overall:", ass_overall_cov) # Positive correlation
print("Participation vs Overall:", part_overall_cov) # Positive correlation
print("Sleep vs Overall:", sleep_overall_cov)
print("Midterm vs Overall:", midterm_overall_cov)
print("Final vs Overall:", final_overall_cov)
print("Midterm vs Final:", midterm_final_cov) 
print("Study vs Midterm:", study_midterm_cov)
print("Study vs Final:", study_final_cov)
print()


#Calculating correlation coefficients
att_overall_corr = stat.correlation(att, overall)
ass_overall_corr = stat.correlation(ass, overall)
part_overall_corr = stat.correlation(part, overall)
midterm_overall_corr = stat.correlation(midterm, overall)
final_overall_corr = stat.correlation(final, overall)

print("Correlations:")
print("Attendance vs Overall:", att_overall_corr)
print("Assignments vs Overall:", ass_overall_corr)
print("Participation vs Overall:", part_overall_corr)
print("Midterm vs Overall:", midterm_overall_corr)
print("Final vs Overall:", final_overall_corr)
print()


#male vs female
male = df[df['gender'] == 'Male']
female = df[df['gender'] == 'Female']

male_midterm_mean = stat.mean(male['midterm_score'])
male_midterm_var = stat.variance(male['midterm_score'])
male_final_mean = stat.mean(male['final_exam_score'])
male_final_var = stat.variance(male['final_exam_score'])
male_overall_mean = stat.mean(male['overall_score'])
male_overall_var = stat.variance(male['overall_score'])
female_midterm_mean = stat.mean(female['midterm_score'])
female_midterm_var = stat.variance(female['midterm_score'])
female_final_mean = stat.mean(female['final_exam_score'])
female_final_var = stat.variance(female['final_exam_score'])
female_overall_mean = stat.mean(female['overall_score'])
female_overall_var = stat.variance(female['overall_score'])

print("Comparison between males and females:")
print("Male midterm score:", male_midterm_mean)
print("Male final score:", male_final_mean)
print("Male overall score:", male_overall_mean)
print("Male midterm variance:", male_midterm_var)
print("Male final variance:", male_final_var)
print("Male overall variance:", male_overall_var)
print("Female midterm score:", female_midterm_mean)
print("Female final score:", female_final_mean)
print("Female final variance:", female_final_var)
print("Female overall score:", female_overall_mean)
print("Female overall variance:", female_overall_var)
print("Female midterm variance:", female_midterm_var)
print("Female final variance:", female_final_var)
print("Female overall variance:", female_overall_var)
print()


#Key Observations
print("Key Observations (thus far):")
print("1. There is a positive correlation between attendance and overall performance.")
print("2. There is a positive correlation between assignment scores and overall performance (the largest).")
print("3. There is a positive correlation between participation and overall performance.")
print("4. (Obviously) Both midterm and final exam scores have a positive correlation with overall performance, with the final exam score showing a slightly stronger correlation.")
print("5. The performace of male and female students is relatively similar, however, female students gave slightly higher variances in their scores, indicating a wider range of performance")
print()