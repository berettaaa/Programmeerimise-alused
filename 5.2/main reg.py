from module1 import *

while True:
    print("\n=== MENÜÜ ===")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine")
    print("3 - Nime või parooli muutmine")
    print("4 - Parooli taastamine")
    print("5 - Lõpetamine")

    choice = input("Vali tegevus: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        authorize()
    elif choice == "3":
        change_credentials()
    elif choice == "4":
        recover_password()
    elif choice == "5":
        print("Head aega.")
        break
    else:
        print("Tundmatu valik.")
