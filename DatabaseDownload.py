import kagglehub

# Download latest version
path = kagglehub.dataset_download("borovai0/student-performance-analytics-dataset")

print("Path to dataset files:", path)