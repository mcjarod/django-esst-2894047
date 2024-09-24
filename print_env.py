import os

print("Env. variables:")
for key, value in os.environ.items():
    print(f"{key}: {value}")
