# designed for splitting a dataset of images into training and test sets. It writes the paths of these images to train.txt and test.txt files, respectively.

import glob, os

# Current_dir is path to the unzipped dataset
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
current_dir = 'data/obj'

# Percentage of images to be used for the test set
percentage_test = 10;

# Create and/or truncate train.txt and test.txt
file_train = open('data/train.txt', 'w')
file_test = open('data/test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    # Using glob.iglob(), the code is generating an iterator that loops through all .jpg files in the current_dir directory.
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    # os.path.basename(pathAndFilename) retrieves the filename part from the full path. while 
    # os.path.splitext() splits the filename into two parts: the name (title) and the extension (ext).
    if counter == index_test:
        counter = 1
        file_test.write("data/obj" + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("data/obj" + "/" + title + '.jpg' + "\n")
        counter = counter + 1
