import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics as stat

df = pd.read_csv('student_performance_data.csv')
print(df.head())


# Extracting columns
study = df['study_hours_per_day']
att = df['attendance_percentage']
ass = df['assignment_score']
midterm = df['midterm_score']
final = df['final_exam_score']
part = df['participation_score']
parent = df['parent_education']
sleep = df['sleep_hours']
overall = df['overall_score']
grade = df['grade']


# Finding the covariace between possibly related columns
sleep_study_cov = stat.covariance(sleep, study)
att_part_cov = stat.covariance(att, part)
study_overall_cov = stat.covariance(study, overall)
att_overall_cov = stat.covariance(att, overall)
ass_overall_cov = stat.covariance(ass, overall)
part_overall_cov = stat.covariance(part, overall)
midterm_overall_cov = stat.covariance(midterm, overall)
final_overall_cov = stat.covariance(final, overall)

print("Covariances:")
print("Sleep vs Study:", sleep_study_cov) # No correlation
print("Attendance vs Participation:", att_part_cov) # No correlation
print("Study vs Overall:", study_overall_cov) # No correlation
print("Attendance vs Overall:", att_overall_cov) # Positive correlation
print("Assignments vs Overall:", ass_overall_cov) # Positive correlation
print("Participation vs Overall:", part_overall_cov) # Positive correlation
print("Midterm vs Overall:", midterm_overall_cov) # Obvious positive correlation
print("Final vs Overall:", final_overall_cov) # Obvious Positive correlation
print()


#Calculating correlation coefficients
sleep_study_corr = stat.correlation(sleep, study)
att_part_corr = stat.correlation(att, part)
att_overall_corr = stat.correlation(att, overall)
ass_overall_corr = stat.correlation(ass, overall)
part_overall_corr = stat.correlation(part, overall)
midterm_overall_corr = stat.correlation(midterm, overall)
final_overall_corr = stat.correlation(final, overall)

print("Correlations:")
print("Sleep vs Study:", sleep_study_corr)
print("Attendance vs Participation:", att_part_corr)
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
0
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


#Internet access AND extra classes
yes = df[(df['internet_access'] == 'Yes') & (df['extra_classes'] == 'Yes')]
no = df[(df['internet_access'] == 'No') & (df['extra_classes'] == 'No')]

yes_midterm_mean = stat.mean(yes['midterm_score'])
yes_midterm_var = stat.variance(yes['midterm_score'])
yes_final_mean = stat.mean(yes['final_exam_score'])
yes_final_var = stat.variance(yes['final_exam_score'])
yes_overall_mean = stat.mean(yes['overall_score'])
yes_overall_var = stat.variance(yes['overall_score'])

no_midterm_mean = stat.mean(no['midterm_score'])
no_midterm_var = stat.variance(no['midterm_score'])
no_final_mean = stat.mean(no['final_exam_score'])
no_final_var = stat.variance(no['final_exam_score'])
no_overall_mean = stat.mean(no['overall_score'])
no_overall_var = stat.variance(no['overall_score'])

print("Comparison between students with internet access and extra classes:")
print("Students with internet access and extra classes - Midterm score:", yes_midterm_mean)
print("Students with internet access and extra classes - Final score:", yes_final_mean)
print("Students with internet access and extra classes - Overall score:", yes_overall_mean)
print("Students with internet access and extra classes - Midterm variance:", yes_midterm_var)
print("Students with internet access and extra classes - Final variance:", yes_final_var)
print("Students with internet access and extra classes - Overall variance:", yes_overall_var)
print("Students without internet access and without extra classes - Midterm score:", no_midterm_mean)
print("Students without internet access and without extra classes - Final score:", no_final_mean)
print("Students without internet access and without extra classes - Overall score:", no_overall_mean)
print("Students without internet access and without extra classes - Midterm variance:", no_midterm_var)
print("Students without internet access and without extra classes - Final variance:", no_final_var)
print("Students without internet access and without extra classes - Overall variance:", no_overall_var)
print()


#Parent Education
high = df[df['parent_education'] == 'High School']
bachelor = df[df['parent_education'] == 'Bachelor']
master = df[df['parent_education'] == 'Master']
phd = df[df['parent_education'] == 'PhD']

high_overall_mean = stat.mean(high['overall_score'])
high_overall_var = stat.variance(high['overall_score'])

bachelor_overall_mean = stat.mean(bachelor['overall_score'])
bachelor_overall_var = stat.variance(bachelor['overall_score'])

master_overall_mean = stat.mean(master['overall_score'])
master_overall_var = stat.variance(master['overall_score'])

phd_overall_mean = stat.mean(phd['overall_score'])
phd_overall_var = stat.variance(phd['overall_score'])

print("Comparison between students with high school and PhD educated parents:")
print("Students with high school educated parents - Average overall score:", high_overall_mean)
print("Students with high school educated parents - Overall variance:", high_overall_var)
print("Students with bachelor's degree educated parents - Average overall score:", bachelor_overall_mean)
print("Students with bachelor's degree educated parents - Overall variance:", bachelor_overall_var)
print("Students with master's degree educated parents - Average overall score:", master_overall_mean)
print("Students with master's degree educated parents - Overall variance:", master_overall_var)
print("Students with PhD educated parents - Average overall score:", phd_overall_mean)
print("Students with PhD educated parents - Overall variance:", phd_overall_var)
print()


#Key Observations
print("Key Observations (thus far):")
print("1. There is a slightly positive correlation between attendance and overall performance.")
print("2. There is a positive correlation between assignment scores and overall performance (the largest).")
print("3. There is a positive correlation between participation and overall performance.")
print("4. (Obviously) Both midterm and final exam scores have a positive correlation with overall performance, with the final exam score showing a slightly stronger correlation.")
print("5. Surprisingly, there is no correlation between sleep hours and study hours.")
print("6. There is no correlation between attendance and participation.")
print("7. Surprisingly, There is no correlation between study hours and overall performance.")
print("8. The performace of male and female students is relatively similar, however, female students gave slightly higher variances in their scores, indicating a wider range of performance")
print("9. Students with internet access and extra classes tend to perform better than those without. The final exam scores of these students however, show a slightly higher variance.")
print("10. The education level of the parents doesn't significantly impact the overall performance of their children, with a slight variation in performance across different education levels (highest being those with a Master's degree).")
print()


#Plots with Sample Data and correlation lines
dfsmall = df.sample(n=50)
plt.figure(1)
plt.scatter(dfsmall['attendance_percentage'], dfsmall['overall_score'])
m = np.polyfit(df['attendance_percentage'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['attendance_percentage'], b(df['attendance_percentage']), color='red', linestyle='--')
plt.xlabel('Attendance')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Attendance vs Overall Score')

plt.figure(2)
plt.scatter(dfsmall['assignment_score'], dfsmall['overall_score'])
m = np.polyfit(df['assignment_score'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['assignment_score'], b(df['assignment_score']), color='red', linestyle='--')
plt.xlabel('Assignment Score')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Assignment Score vs Overall Score')

plt.figure(3)
plt.scatter(dfsmall['participation_score'], dfsmall['overall_score'])
m = np.polyfit(df['participation_score'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['participation_score'], b(df['participation_score']), color='red', linestyle='--')
plt.xlabel('Participation')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Participation vs Overall Score')

plt.figure(4)
plt.scatter(dfsmall['study_hours_per_day'], dfsmall['overall_score'])
m = np.polyfit(df['study_hours_per_day'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['study_hours_per_day'], b(df['study_hours_per_day']), color='red', linestyle='--')
plt.xlabel('Study Hours')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Study Hours vs Overall Score')

plt.figure(5)
plt.scatter(dfsmall['sleep_hours'], dfsmall['study_hours_per_day'])
m = np.polyfit(df['sleep_hours'], df['study_hours_per_day'], 1)
b = np.poly1d(m)
plt.plot(df['sleep_hours'], b(df['sleep_hours']), color='red', linestyle='--')
plt.xlabel('Sleep Hours')
plt.ylabel('Study Hours')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Sleep Hours vs Study Hours')

plt.figure(6)
plt.scatter(dfsmall['attendance_percentage'], dfsmall['participation_score'])
m = np.polyfit(df['attendance_percentage'], df['participation_score'], 1)
b = np.poly1d(m)
plt.plot(df['attendance_percentage'], b(df['attendance_percentage']), color='red', linestyle='--')
plt.xlabel('Attendance')
plt.ylabel('Participation')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Attendance vs Participation')

plt.figure(7)
plt.scatter(dfsmall['midterm_score'], dfsmall['overall_score'])
m = np.polyfit(df['midterm_score'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['midterm_score'], b(df['midterm_score']), color='red', linestyle='--')
plt.xlabel('Midterm Exam Score')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Midterm Exam Score vs Overall Score')

plt.figure(8)
plt.scatter(dfsmall['final_exam_score'], dfsmall['overall_score'])
m = np.polyfit(df['final_exam_score'], df['overall_score'], 1)
b = np.poly1d(m)
plt.plot(df['final_exam_score'], b(df['final_exam_score']), color='red', linestyle='--')
plt.xlabel('Final Exam Score')
plt.ylabel('Overall Score')
plt.legend(['Data Points','Trend line m = ' + str(round(m[0], 2))])
plt.title('Final Exam Score vs Overall Score')

plt.show()