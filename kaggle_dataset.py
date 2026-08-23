import kagglehub

# Download latest version
path = kagglehub.dataset_download("peopledatalabssf/free-7-million-company-dataset")

print("Path to dataset files:", path)