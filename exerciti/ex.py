# task1
bad_path = input('Calea către fișierul cu "bad words": ')
text_path = input("Calea către fișierul de filtrat: ")
if not os.path.exists(bad_path) or not os.path.exists(text_path):
    print("Unul dintre fișiere nu există!")
else:
    with open(bad_path) as bad_file, open(text_path) as text_file, open(
        "fisiernou.txt", "w"
    ) as out_file:
        bad_words = bad_file.read().split()
        text = text_file.read().split()

        clean_words = [word for word in text if word not in bad_words]
        out_file.write(" ".join(clean_words))

print("Fișierul 'fisiernou.txt' a fost creat fără cuvintele interzise.")
