import os
from PIL import Image
# Function to rename multiple files
def main():
   i = 765
   path="/home/kushaldulani/Pictures/"
   for filename in os.listdir(path):
      im = Image.open(path + filename).convert('RGB').save('filename.jpg')
      i += 1
# Driver Code
if __name__ == '__main__':
   # Calling main() function
   main()
