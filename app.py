import os
import shutil

new_dir = "new_directory"
os.makedirs(new_dir, exist_ok=True)
print(f"Directory '{new_dir}' created.")

print("\nFiles and directories in the current working directory:")
print(os.listdir('.'))

file_path = os.path.join(new_dir, "example_file.txt")
with open(file_path, "w") as file:
    file.write("This is some sample content.")
print(f"\nFile 'example_file.txt' created in '{new_dir}' and content written to it.")

with open(file_path, "r") as file:
    content = file.read()
print(f"\nContent of 'example_file.txt':\n{content}")

new_file_path = os.path.join(new_dir, "renamed_file.txt")
os.rename(file_path, new_file_path)
print(f"\nFile renamed to 'renamed_file.txt'.")

print(f"\nFiles and directories in '{new_dir}' after renaming:")
print(os.listdir(new_dir))

shutil.rmtree(new_dir)
print(f"\nDirectory '{new_dir}' and its contents deleted.")
