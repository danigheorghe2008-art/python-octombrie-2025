print("Task 1")
# Create an app that stores information about great basketball players.
#  Store the player's full name and height. Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.

# players = {
#     "Michael Jordan": "198 cm",
#     "LeBron James": "206 cm",
#     "Kobe Bryant": "198 cm",
#     "Shaquille O'Neal": "216 cm",
# }


# def add_player(name, height):
#     players[name] = height


# def delete_player(name):
#     if name in players:
#         del players[name]


# def search_player(name):
#     return players.get(name, "Player not found")


# def replace_player(name, new_height):
#     if name in players:
#         players[name] = new_height


# add_player("Stephen Curry", "188 cm")
# print(players)

# delete_player("LeBron James")
# print(players)

# print(search_player("Shaquille O'Neal"))

# replace_player("Michael Jordan", "170 cm")
# print(players)

print()
print("Task 2")
# Create an app English-French Dictionary. Store a word in English and its French translation.
#  Provide the possibility to add, delete, search, and replace data. Use a dictionary to store information.

# dictionary = {
#     "hello": "bonjour",
#     "goodbye": "au revoir",
#     "please": "s'il vous plaît",
#     "thank you": "merci",
#     "cat": "minou",
# }


# def add_translation(English, Franch):
#     dictionary[English] = Franch


# def delete_tranlation(English):
#     if English in dictionary:
#         del dictionary[English]


# def search_translation(English):
#     return dictionary.get(English, "Word not found")


# def replace_translation(English, new_translasion):
#     if English in dictionary:
#         dictionary[English] = new_translasion


# add_translation("yes", "oui")
# print(dictionary)

# delete_tranlation("hello")
# print(dictionary)

# print(search_translation("no"))

# replace_translation("cat", "chat")
# print(dictionary)

print()
print("Task 3")
# Create an app Company. Store the following information about a person: full name, phone number,
#  corporate email, job title, room number, skype. Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.

# company = {
#     "Alice Johnson": {
#         "Phone": "123-456-7890",
#         "Email": "alice.89@company.com",
#         "Job Title": "Project Manager",
#         "Room": "101",
#         "Skype": "aliec.johnson",
#     },
#     "Bob smith": {
#         "Phone": "987-654-3210",
#         "Email": "bob.675@company.com",
#         "Job Title": "Software Engineer",
#         "Room": "202",
#         "Skype": "bob.smith",
#     },
#     "Charlie Brown": {
#         "Phone": "555-123-4567",
#         "Email": "charlie.brown@company.com",
#         "Job Title": "HR Specialist",
#         "Room": "303",
#         "Skype": "charlie.brown",
#     },
# }


# def add_employee(name, phone, email, title, room, skype):
#     company[name] = {
#         "Phone": phone,
#         "Email": email,
#         "Job Title": title,
#         "Room": room,
#         "Skype": skype,
#     }
#     print(f"{name} added successfully.")


# def delete_employee(name):
#     if name in company:
#         del company[name]


# def search_employee(name):
#     return company.get(name, "empolyee not found")


# def replace_employee(name, info, new_info):
#     if name in company and info in company[name]:
#         company[name][info] = new_info
#         print(f"{info} updated for {name}")
#     else:
#         print("info not found")


# print(company)
# add_employee(
#     "Frank Castle",
#     "111-222-3333",
#     "frank.castle@company.com",
#     "Operations Manager",
#     "606",
#     "frank.castle",
# )

# delete_employee("Charlie Brown")

# print(search_employee("Bob smith"))

# replace_employee("Alice Johnson", "Email", "alice545@gmail.com")

# print(company)

print()
print("Task 4")
# Create an app Book Collection. Store the following information about books:
#  author, title, genre, year of release, publisher. Provide the possibility to add, delete, search, and replace data.
#  Use a dictionary to store information.

books = {
    "Moby-Dick": {
        "Author": "Herman Melville",
        "Genre": "Adventure, Epic",
        "Year": 1851,
        "Publisher": "Harper & Brothers",
    },
    "Harry Potter and the Philosopher's Stone": {
        "Author": "J.K. Rowling",
        "Genre": "Fantasy",
        "Year": 1997,
        "Publisher": "Bloomsbury",
    },
    "To Kill a Mockingbird": {
        "Author": "Harper Lee",
        "Genre": "Southern Gothic, Drama",
        "Year": 1960,
        "Publisher": "J.B. Lippincott & Co.",
    },
}


def add_book(title, author, genre, year, publisher):
    books[title] = {
        "Author": author,
        "Genre": genre,
        "Year": year,
        "Publisher": publisher,
    }


def delete_book(title):
    if title in books:
        del books[title]


def search_book(title):
    return books.get(title, "Book not found")


def replace_book(title, edit, new_edit):
    if title in books and edit in books[title]:
        books[title][edit] = new_edit


print(books)
add_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 1937, "George Allen & Unwin")

delete_book("To Kill a Mockingbird")

print(search_book("Harry Potter and the Philosopher's Stone"))

replace_book("Harry Potter and the Philosopher's Stone", "year", "1920")

print(books)
