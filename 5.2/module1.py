from random import choice, shuffle
from string import ascii_letters, digits

kasutajad = []
paroolid = []


def generate_password():
    """
    Loob 12-märgilise juhusliku parooli,
    mis sisaldab tähti, numbreid ja erimärke.
    """
    symbols = ".,:;!_*-+()/#%&"
    chars = list(ascii_letters + digits + symbols)
    shuffle(chars)
    return ''.join(choice(chars) for _ in range(12))


def is_valid_password(parool: str) -> bool:
    """
    Kontrollib, kas parool vastab nõuetele:
    - sisaldab numbrit
    - sisaldab väikest tähte
    - sisaldab suurt tähte
    - sisaldab erimärki
    """
    has_digit = False
    has_lower = False
    has_upper = False
    has_symbol = False

    for ch in parool:
        if ch.isdigit():
            has_digit = True
        elif ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        else:
            has_symbol = True

    return has_digit and has_lower and has_upper and has_symbol


def register_user():
    """
    Registreerib uue kasutaja.
    Kasutajanimi peab olema unikaalne.
    Parooli saab genereerida automaatselt või luua käsitsi.
    """
    username = input("Sisesta uus kasutajanimi: ")

    if username in kasutajad:
        print("Kasutajanimi on juba olemas.")
        return

    print("1 - Automaatne parool")
    print("2 - Loon ise parooli")
    choice_option = input("Valik: ")

    if choice_option == "1":
        password = generate_password()
        print("Sinu parool:", password)

    elif choice_option == "2":
        password = input("Sisesta parool: ")
        if not is_valid_password(password):
            print("Parool ei vasta nõuetele.")
            return
    else:
        print("Vale valik.")
        return

    kasutajad.append(username)
    paroolid.append(password)
    print("Kasutaja on edukalt loodud.")


def authorize():
    """
    Kontrollib kasutaja sisselogimist
    kasutajanime ja parooli alusel.
    """
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta parool: ")

    if username in kasutajad:
        idx = kasutajad.index(username)
        if paroolid[idx] == password:
            print("Sisselogimine õnnestus.")
        else:
            print("Vale parool.")
    else:
        print("Kasutajat ei leitud.")


def change_credentials():
    """
    Võimaldab muuta olemasoleva konto
    kasutajanime või parooli.
    """
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta parool: ")

    if username not in kasutajad:
        print("Kasutajat ei leitud.")
        return

    idx = kasutajad.index(username)
    if paroolid[idx] != password:
        print("Vale parool.")
        return

    print("1 - Muuda kasutajanimi")
    print("2 - Muuda parool")
    option = input("Valik: ")

    if option == "1":
        new_username = input("Sisesta uus kasutajanimi: ")
        if new_username in kasutajad:
            print("Kasutajanimi on juba olemas.")
            return
        kasutajad[idx] = new_username
        print("Kasutajanimi on muudetud.")

    elif option == "2":
        new_password = input("Sisesta uus parool: ")
        if not is_valid_password(new_password):
            print("Parool ei vasta nõuetele.")
            return
        paroolid[idx] = new_password
        print("Parool on muudetud.")

    else:
        print("Vale valik.")


def recover_password():
    """
    Kuvab kasutaja parooli,
    kui kasutajanimi on olemas.
    """
    username = input("Sisesta kasutajanimi: ")

    if username in kasutajad:
        idx = kasutajad.index(username)
        print("Sinu parool on:", paroolid[idx])
    else:
        print("Kasutajat ei leitud.")
