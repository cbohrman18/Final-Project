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
print()


#Internet Access
internet = df[df['internet_access'] == 'Yes']
no_internet = df[df['internet_access'] == 'No']

internet_midterm_mean = stat.mean(internet['midterm_score'])
internet_midterm_var = stat.variance(internet['midterm_score'])
internet_final_mean = stat.mean(internet['final_exam_score'])
internet_final_var = stat.variance(internet['final_exam_score'])
internet_overall_mean = stat.mean(internet['overall_score'])
internet_overall_var = stat.variance(internet['overall_score'])

no_internet_midterm_mean = stat.mean(no_internet['midterm_score'])
no_internet_midterm_var = stat.variance(no_internet['midterm_score'])
no_internet_final_mean = stat.mean(no_internet['final_exam_score'])
no_internet_final_var = stat.variance(no_internet['final_exam_score'])
no_internet_overall_mean = stat.mean(no_internet['overall_score'])
no_internet_overall_var = stat.variance(no_internet['overall_score'])

print("Comparison between students with and without internet access:")
print("Students with internet access - Midterm score:", internet_midterm_mean)
print("Students with internet access - Final score:", internet_final_mean)
print("Students with internet access - Overall score:", internet_overall_mean)
print("Students with internet access - Midterm variance:", internet_midterm_var)
print("Students with internet access - Final variance:", internet_final_var)
print("Students with internet access - Overall variance:", internet_overall_var)
print("Students without internet access - Midterm score:", no_internet_midterm_mean)
print("Students without internet access - Final score:", no_internet_final_mean)
print("Students without internet access - Overall score:", no_internet_overall_mean)
print("Students without internet access - Midterm variance:", no_internet_midterm_var)
print("Students without internet access - Final variance:", no_internet_final_var)
print("Students without internet access - Overall variance:", no_internet_overall_var)
print()


#Extra Classes
extra = df[df['extra_classes'] == 'Yes']
no_extra = df[df['extra_classes'] == 'No']

extra_midterm_mean = stat.mean(extra['midterm_score'])
extra_midterm_var = stat.variance(extra['midterm_score'])
extra_final_mean = stat.mean(extra['final_exam_score'])
extra_final_var = stat.variance(extra['final_exam_score'])
extra_overall_mean = stat.mean(extra['overall_score'])
extra_overall_var = stat.variance(extra['overall_score'])

no_extra_midterm_mean = stat.mean(no_extra['midterm_score'])
no_extra_midterm_var = stat.variance(no_extra['midterm_score'])
no_extra_final_mean = stat.mean(no_extra['final_exam_score'])
no_extra_final_var = stat.variance(no_extra['final_exam_score'])
no_extra_overall_mean = stat.mean(no_extra['overall_score'])
no_extra_overall_var = stat.variance(no_extra['overall_score'])

print("Comparison between students with and without extra classes:")
print("Students with extra classes - Midterm score:", extra_midterm_mean)
print("Students with extra classes - Final score:", extra_final_mean)
print("Students with extra classes - Overall score:", extra_overall_mean)
print("Students with extra classes - Midterm variance:", extra_midterm_var)
print("Students with extra classes - Final variance:", extra_final_var)
print("Students with extra classes - Overall variance:", extra_overall_var)
print("Students without extra classes - Midterm score:", no_extra_midterm_mean)
print("Students without extra classes - Final score:", no_extra_final_mean)
print("Students without extra classes - Overall score:", no_extra_overall_mean)
print("Students without extra classes - Midterm variance:", no_extra_midterm_var)
print("Students without extra classes - Final variance:", no_extra_final_var)
print("Students without extra classes - Overall variance:", no_extra_overall_var)
print()