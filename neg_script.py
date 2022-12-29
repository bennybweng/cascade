import os


# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_createsamples.exe
# C:/Users/benny/Desktop/Uni/opencv/opencv/build/x64/vc15/bin/opencv_traincascade.exe -data final/ -vec pos_v2.vec -bg neg_v3.txt -numPos 1000
# -numNeg 600 -numStages 10 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -w 48 -h 48

def neg_desc():
    with open('neg_v1.txt', 'w') as f:
        for filename in os.listdir('negative_v1'):
            f.write('negative_v1/' + filename + '\n')


def yo():
    replacements = {'.jpg': '_12.jpg'}

    with open('C:/Users/benny/PycharmProjects/cascade/12/12.txt') as infile, open(
            'C:/Users/benny/PycharmProjects/cascade/12/12_new.txt', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


def a():
    b = "C:/Users/benny/PycharmProjects/cascade/12/"
    for filename in os.listdir("C:/Users/benny/PycharmProjects/cascade/12"):
        if filename.endswith(".jpg"):
            os.rename(b + filename, (b + filename).replace(".jpg", "_12.jpg"))