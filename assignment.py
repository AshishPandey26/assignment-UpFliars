import os

import shutil
# os.mkdir("test")
# os.chdir(r"C:\\\\Users\\\\HP\\\\OneDrive\\\\Desktop\\\\New folder\\\\Test")
# os.chdir("test")
# print(os.getcwd())

# fd = "one.txt" 
# file = open(fd, "x")
# fd = "two.txt" 
# file = open(fd, "x")
# fd = "one.pdf" 
# file = open(fd, "x")
# fd = "two.pdf" 
# file = open(fd, "x")
# fd = "one.png" 
# file = open(fd, "x")
# fd = "two.png" 
# file = open(fd, "x")
# fd = "one.jpg" 
# file = open(fd, "x")
# fd = "two.jpg" 
# file = open(fd, "x")
# fd = "one.jpeg" 
# file = open(fd, "x")
# fd = "two.jpeg" 
# file = open(fd, "x")

# os.mkdir("text_folder")
# os.mkdir("txt")
# os.mkdir("img_folder")




# os.chdir("txt")
# print(os.getcwd())
# # shutil.move("C:\\Users\\HP\\OneDrive\\Desktop\\New folder\\test", "C:\\Users\\HP\\OneDrive\\Desktop\\New folder\\test\\text_folder")

# for file_name in os.listdir():
#     if file_name.endswith('.txt'):
#         src_path = os.path.join(os.getcwd(), file_name)
#         dst_path = os.path.join(txt, file_name)
#         shutil.move(src_path, dst_path)
#         print(f"Moved {file_name} to {dst_path}")

# # Verify files moved
# print("Files in 'test' directory after moving:", os.listdir())
# print("Files in 'img_folder' directory:", os.listdir(txt))






# Step 1: Ensure the current directory is 'test'
os.chdir("test")
print("Current directory:", os.getcwd())

# Step 2: Define the 'img_folder' directory
img_folder = "../test/img_folder"  # Adjusting path to ensure it's outside 'test' folder

# Create the 'img_folder' directory if it doesn't exist
if not os.path.exists(img_folder):
    os.mkdir(img_folder)
    print(f"Created directory: {img_folder}")
else:
    print(f"Directory already exists: {img_folder}")

# Verify current files in 'test' directory
print("Files in 'test' directory before moving:", os.listdir())

# Step 3: Move .txt files to the 'img_folder' directory
for file_name in os.listdir():
    if file_name.endswith('.png'):
        src_path = os.path.join(os.getcwd(), file_name)
        dst_path = os.path.join(img_folder, file_name)
        shutil.move(src_path, dst_path)
        print(f"Moved {file_name} to {dst_path}")

