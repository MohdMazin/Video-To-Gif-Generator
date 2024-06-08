import os
import fnmatch 
from moviepy.editor import *

print("Warning The File Should be Mp4 ⚠")
print("Save The Python file in the Folder where Your Video File Is.")

videonam = input("Enter the File Name You want to Convert to GIF (including extension, ex- hello.mp4): ")
print("The Start Time Should Be like For Example 00, 01, 02, etc.\n")
print("The End timing could be like 3, 4, 8, 9, etc.\n")
timst = int(input("Enter the Start Timing for your Video: "))
timlt = int(input("Enter the End Timing for your Video: "))

print("The Time You Wrote For the start -->", timst)
print("The Time You Wrote For the end -->", timlt)

chantim = input("Want to Change The Time? (Y/N): ").upper()

if chantim == "Y":
    def changeAGAIN():
        global timst, timlt  # Make the variables global to update them
        timst = int(input("Enter the Start Timing for your Video: "))
        timlt = int(input("Enter the End Timing for your Video: "))
    changeAGAIN()  # Call the function after defining it
else:
    print("OK, we won't change it!")

def find_file(filename, search_path):
    result = []
    for root,dir,files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result 

search_path = "/"
found_files = find_file(videonam,search_path)

if not found_files:
    print(f"the file {videonam} does not exist in the computer.")
else:
    for file_path in found_files:
        print(f"Files Found: {file_path}")
        try:
            video = VideoFileClip(file_path).subclip(timst, timlt)
            gifnam = input("Enter what GIF name you want (with .gif extension): ")
            video.write_gif(gifnam)
            print(f"GIF saved as {gifnam}")
            break  # If you want to convert only the first found file
        except OSError as e:
            print(f"An error occurred: {e}")
            print("Please check that you entered the correct path and file name.")
            

