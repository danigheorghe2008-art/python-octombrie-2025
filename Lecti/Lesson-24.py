# # TODO
# path1 = "./files/test.txt"
# path2 = "./files/result.txt"

# import shutil
# import os
# import datetime


# # Backup the destination file if it exists
# if os.path.exists(path2):
#     timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_path = f"{path2}.{timestamp}.bak"
#     shutil.copy(path2, backup_path)
# with open(path1) as inFile, open(path2, "w") as outFile:
#     fileContents = inFile.read()
#     fileContents = fileContents.lower()
#     outFile.write(fileContents)


def replaceTextInFile(fileName, originText, newText):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = data.replace(originText, newText)

    with open(fileName, "w") as fileHandler:
        fileHandler.write(data)


# def readFromFile(fileName):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         print(data)


# myFile = "../Data/PythonAbout.txt"

# print("Original file content:")
# readFromFile(myFile)

# replaceTextInFile(myFile, "Python", "JavaScript")

# print("New file content:")
# readFromFile(myFile)


# def readFromFile(fileName):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         print(data)


# def wordCounter(fileName):
#     nWords = 0
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         words = data.split()
#         for word in words:
#             if not word.isnumeric():
#                 nWords += 1
#     return nWords


# myFile = "./files/test.txt"

# print("File content:")
# readFromFile(myFile)

# print("Number of words: {}".format(wordCounter(myFile)))


def removeLine(fileIn, fileOut, lineNumber):
    with open(fileIn) as fr:
        lines = fr.readlines()

        counter = 1  # position pointer

        with open(fileOut, "w") as fw:
            for line in lines:
                if counter != lineNumber:
                    fw.write(line)
                counter += 1


myFile = "../Data/Info.txt"
resultFile = "../Data/result.txt"

removeLine(myFile, resultFile, 2)
