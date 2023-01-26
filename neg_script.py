import os
import shutil


# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_createsamples.exe
# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_createsamples.exe -img cropped/13.jpg -bg neg_v2.txt -info test/13.txt -num 128 -maxxangle 0.0 -maxyangle 0.0 -maxzangle 0.3 -bgcolor 255 -bgthresh 8 -w 48 -h 48
# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data final/ -vec pos_v2.vec -bg neg_v3.txt -numPos 1000 -numNeg 600 -numStages 10 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -w 48 -h 48
# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data 2000_2000/ -vec pos_v3.vec -bg neg_v4.txt -numPos 2000  -numNeg 2000 -numStages 5 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -w 48 -h 48

#C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data v3_1/ -vec pos_v3.vec -bg neg_v4.txt -numPos 2000 -numNeg 2000 -numStages 5 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -w 48 -h 48
def neg_desc():
    with open('neg_v1.txt', 'w') as f:
        for filename in os.listdir('negative_v1'):
            f.write('negative_v1/' + filename + '\n')


def replace():
    replacements = {'.jpg': '_12.jpg'}

    with open('C:/Users/benny/PycharmProjects/cascade/12/12.txt') as infile, open(
            'C:/Users/benny/PycharmProjects/cascade/12/12_new.txt', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


def rename():
    b = "C:/Users/benny/PycharmProjects/cascade/12/"
    for filename in os.listdir("C:/Users/benny/PycharmProjects/cascade/12"):
        if filename.endswith(".jpg"):
            os.rename(b + filename, (b + filename).replace(".jpg", "_12.jpg"))


def replace_multiple():
    for i in range(13, 34):
        j = str(i)
        replacements = {'.jpg': '_' + j + '.jpg'}

        with open('C:/Users/benny/PycharmProjects/cascade/' + j + '/' + j + '.txt') as infile, open(
                'C:/Users/benny/PycharmProjects/cascade/' + j + '/' + j + '_new.txt', 'w') as outfile:
            for line in infile:
                for src, target in replacements.items():
                    line = line.replace(src, target)
                outfile.write(line)


def rename_multiple():
    for i in range(13, 34):
        j = str(i)
        b = "C:/Users/benny/PycharmProjects/cascade/" + j + "/"
        for filename in os.listdir("C:/Users/benny/PycharmProjects/cascade/" + j):
            if filename.endswith(".jpg"):
                os.rename(b + filename, (b + filename).replace(".jpg", "_" + j + ".jpg"))


def merge_txt():
    lis = []
    for i in range(13, 34):
        lis.append('C:/Users/benny/PycharmProjects/cascade/positive_v3/' + str(i) + '_new.txt')
    with open('C:/Users/benny/PycharmProjects/cascade/positive_v3/positive.txt', 'wb') as wfd:
        for f in lis:
            with open(f, 'rb') as fd:
                shutil.copyfileobj(fd, wfd)
                wfd.write(b"\n")

def combine():
    with open('C:/Users/benny/PycharmProjects/cascade/positive_v2/positive.txt') as infile, open(
            'C:/Users/benny/PycharmProjects/cascade/positive_v2/pos_v3.txt', 'w') as outfile:
        for line in infile:
            line = "positive_v2/" + line
            outfile.write(line)
def merge():
    # current folder path
    current_folder = os.getcwd()

    list_dir = []

    # list of folders to be merged
    for i in range(13, 34):
        list_dir.append(str(i))

    # enumerate on list_dir to get the
    # content of all the folders and store
    # it in a dictionary
    content_list = {}
    for index, val in enumerate(list_dir):
        path = os.path.join(current_folder, val)
        content_list[list_dir[index]] = os.listdir(path)

    # folder in which all the content will
    # be merged
    merge_folder = "positive_v3"

    # merge_folder path - current_folder
    # + merge_folder
    merge_folder_path = os.path.join(current_folder, merge_folder)

    # loop through the list of folders
    for sub_dir in content_list:

        # loop through the contents of the
        # list of folders
        for contents in content_list[sub_dir]:
            # make the path of the content to move
            path_to_content = sub_dir + "/" + contents

            # make the path with the current folder
            dir_to_move = os.path.join(current_folder, path_to_content)

            # move the file
            shutil.move(dir_to_move, merge_folder_path)
