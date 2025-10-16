print("Task 1")
# You have two text files. Find out if their lines match. If they don't, print the mismatched line from each files"


file1 = "./files/test.txt"
file2 = "./files/result.txt"

with open(file1, "r") as f1, open(file2, "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

for i, (line1, line2) in enumerate(zip(lines1, lines2), start=1):
    if line1.split() != line2.split():
        print(f"The Line: {i} differs")
        print(f"File1: {line1.strip()}")
        print(f"File2: {line2.strip()}")

if len(lines1) != len(lines2):
    print("The files have different numbers of lines.")


print("Task 2")
# You have a text file. Create a new file and write the following statistics based on the source file to it:
# Number of characters;
# Number of lines;
# Number of vowels;
# Number of consonants;
# Number of digits.

in_file = "./files/source.txt"
out_file = "./files/stats.txt"

with open(in_file, "r") as f:
    text = f.read()

num_chars = len(text)
num_lines = text.count("\n") + 1 if text else 0
vowels = "aeiouAEIOU"
num_vowels = sum(1 for c in text if c in vowels)
num_consonants = sum(1 for c in text if c.isalpha() and c not in vowels)
num_digits = sum(1 for c in text if c.isdigit())

with open(out_file, "w") as f:
    f.write(f"Number of characters: {num_chars}\n")
    f.write(f"Number of lines: {num_lines}\n")
    f.write(f"Number of vowels: {num_vowels}\n")
    f.write(f"Number of consonants: {num_consonants}\n")
    f.write(f"Number of digits: {num_digits}\n")

print(f"Statistics written to {out_file}")


print("Task 3")
# You have a text file. Delete the last line from it. Write the result to another file.

in_file1 = "./files/source.txt"
out_file1 = "./files/no_last_line.txt"

with open(in_file1, "r") as f:
    lines = f.readlines()

with open(out_file1, "w") as f:
    f.writelines(lines[:-1])

print(f"File without last line written to {out_file1}")


print("Task 4")
# You have a text file. Find the length of the longest line.

in_file2 = "./files/source.txt"

with open(in_file2, "r") as f:
    longest = max((len(line.strip()) for line in f), default=0)

print(f"The length of the longest line is: {longest}")


print("Task 5")
# You have a text file. Count how many times the word specified by the user occurs in it.

in_file3 = "./files/source.txt"
word = input("Enter the word to count: ")

with open(in_file3) as f:
    text = f.read().lower()

count = text.split().count(word.lower())
print(f"The word '{word}' occurs {count} times.")


print("Task 6")
# You have a text file. Find and replace the specified word. The user determines what to search for and to what it should be replaced.

in_file4 = "./files/source.txt"
out_file4 = "./files/replaced.txt"

originText = input("Enter a word to find: ").lower()
newtext = input("Enter a word to replace it with: ")

with open(in_file4, "r") as f:
    text = f.read().lower()

new_text = text.replace(originText, newtext)

with open(out_file4, "w") as f:
    f.write(new_text)
