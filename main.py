from pyscript import document

takenuser = {
    "Ancheta, Arthur Eugene Maximus Adarna" : ("Sapphire", "History"),
    "Asuncion, Miguelito Alonso Brigoli" : ("Sapphire", "Math"),
    "Battung, John Lorenzo Quisumbing" : ("Sapphire", "Physical Education"),
    "Victor Buenvenida" : ("Sapphire", "Physical Education"),
    "Cade Chua" : ("Sapphire", "Science")
}


def ShowClassmates(event):
    classmates = ""
    for username, (section, fav_subject) in takenuser.items():
        classmates += f"Name: {username}\nSection: {section}\nFavorite Subject: {fav_subject}\n\n"
    document.getElementById("classmate-list").innerText = classmates

def AddClassmate(event):

    username = document.getElementById("username").value.strip()
    section = document.getElementById("section").value.strip()
    fav_subject = document.getElementById("fav").value.strip()

    if not username or not section or not fav_subject:
        document.getElementById("signed").innerText = "Please fill in all fields"
    elif username in takenuser:
        document.getElementById("signed").innerText = "You're already here"
    else:
        takenuser[username] = (section, fav_subject)
        document.getElementById("signed").innerText = f"{username} added as a classmate!"

        document.getElementById("username").value = ""
        document.getElementById("section").value = ""
        document.getElementById("fav").value = ""