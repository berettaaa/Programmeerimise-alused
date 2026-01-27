import os
import datetime
import analuusaator

def kuva_failitüübid():
    failid = os.listdir()
    laiendid = []
    for f in failid:
        if os.path.isfile(f) and "." in f:
            ext = f.split(".")[-1]
            if ext not in laiendid:
                laiendid.append(ext)

    print("\nLeitud failitüübid:")
    for l in sorted(laiendid):
        print(f".{l}")

def analuusi_failid(laiend):
    failid = analuusaator.leia_projektifailid(laiend)
    if not failid:
        print("Selle laiendiga faile ei leitud.")
        return

    kokku_ridu = 0
    kokku_tuhjad = 0
    kokku_todo = 0
    detailid = []

    for f in failid:
        t = analuusaator.analuusi_faili_sisu(f)
        detailid.append(t)
        kokku_ridu += t["ridu_kokku"]
        kokku_tuhjad += t["tuhjad_read"]
        kokku_todo += t["TODO_FIXME_arv"]

    print("\nAnalüüsi kokkuvõte:")
    print(f"Failide arv: {len(failid)}")
    print(f"Ridu kokku: {kokku_ridu}")
    print(f"Tühje ridu: {kokku_tuhjad}")
    print(f"TODO/FIXME kokku: {kokku_todo}")

    return {
        "failide_arv": len(failid),
        "ridu_kokku": kokku_ridu,
        "tuhjad_read": kokku_tuhjad,
        "TODO_FIXME": kokku_todo,
        "detailid": detailid
    }

def salvesta_raport(statistika):
    if not statistika:
        print("Pole midagi salvestada.")
        return

    kataloog = analuusaator.loo_raporti_kataloog()
    kuupaev = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
    failinimi = f"{kataloog}/raport_{kuupaev}.txt"

    with open(failinimi, "w", encoding="utf-8") as f:
        f.write("ANALÜÜSI RAPORT\n================\n\n")
        f.write(f"Failide arv: {statistika['failide_arv']}\n")
        f.write(f"Ridu kokku: {statistika['ridu_kokku']}\n")
        f.write(f"Tühje ridu: {statistika['tuhjad_read']}\n")
        f.write(f"TODO/FIXME kokku: {statistika['TODO_FIXME']}\n\n")
        f.write("Failide detailid:\n")
        for d in statistika["detailid"]:
            f.write(f"{d['fail']} | read: {d['ridu_kokku']} | "
                    f"tühjad: {d['tuhjad_read']} | "
                    f"TODO/FIXME: {d['TODO_FIXME_arv']}\n")
    print(f"Raport salvestatud: {failinimi}")

def puhasta_logid():
    kataloog = "Analüüsi_Raportid"
    if not os.path.exists(kataloog):
        print("Raportite kausta ei eksisteeri.")
        return
    failid = os.listdir(kataloog)
    if not failid:
        print("Pole raporteid, mida kustutada.")
        return
    kinnitus = input("Kas kustutada kõik raportid? (j/e): ")
    if kinnitus.lower() == "j":
        for f in failid:
            os.remove(os.path.join(kataloog, f))
        print("Kõik raportid kustutatud.")
    else:
        print("Toiming katkestatud.")

def main():
    statistika = None
    print("Tere tulemast Koodiprojekti Analüsaatorisse!")
    kuva_failitüübid()

    while True:
        print("\nMENÜÜ")
        print("1 - Täisanalüüs")
        print("2 - Salvesta raport")
        print("3 - Puhasta raportid")
        print("4 - Otsi fail algustähe järgi")
        print("0 - Välju")
        valik = input("Vali tegevus: ")

        if valik == "1":
            laiend = input("Sisesta faililaiend (näiteks .py): ")
            statistika = analuusi_failid(laiend)
        elif valik == "2":
            salvesta_raport(statistika)
        elif valik == "3":
            puhasta_logid()
        elif valik == "4":
            taht = input("Sisesta algustäht: ")
            failid = analuusaator.leia_failid_algustahega(taht)
            if failid:
                print("Leitud failid:")
                for f in failid:
                    print(f)
            else:
                print("Faile ei leitud.")
        elif valik == "0":
            print("Programm lõpetatud. Head päeva!")
            break
        else:
            print("Tundmatu valik, proovi uuesti.")

if __name__ == "__main__":
    main()
