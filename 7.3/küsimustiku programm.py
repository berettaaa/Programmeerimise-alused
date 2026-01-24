import random
import os

M = 3
N = 5
TOOANDJA_EMAIL = "tootaja@firma.ee"


def loe_kusimused():
    kus_vas = {}
    if not os.path.exists("kusimused_vastused.txt"):
        open("kusimused_vastused.txt", "w", encoding="utf-8").close()

    with open("kusimused_vastused.txt", "r", encoding="utf-8") as f:
        for rida in f:
            if ":" in rida:
                k, v = rida.strip().split(":", 1)
                kus_vas[k] = v.lower()
    return kus_vas


def genereeri_email(nimi):
    osad = nimi.lower().split()
    return f"{osad[0]}.{osad[-1]}@example.com"


def loe_testitud():
    testitud = set()
    if os.path.exists("koik.txt"):
        with open("koik.txt", "r", encoding="utf-8") as f:
            for rida in f:
                testitud.add(rida.split(",")[0])
    return testitud


def saada_email_vastajale(nimi, email, punktid, edukas):
    print(f"\nSaadetud: {email}")
    print(f"Tere {nimi}!")
    print(f"Sinu õigete vastuste arv: {punktid}.")
    if edukas:
        print("Sa sooritasid testi edukalt.")
    else:
        print("Kahjuks testi ei sooritatud edukalt.")


def alusta_kusimustikku():
    kus_vas = loe_kusimused()
    if len(kus_vas) < N:
        print("Küsimusi on failis liiga vähe.")
        return

    testitud = loe_testitud()
    tulemused = []

    for _ in range(M):
        nimi = input("\nSisesta vastaja nimi: ").strip()

        if nimi in testitud:
            print("See inimene on juba testitud.")
            continue

        email = genereeri_email(nimi)
        kysimused = random.sample(list(kus_vas.keys()), N)
        oiged = 0

        for k in kysimused:
            vastus = input(f"{nimi}, {k} ").lower().strip()
            if vastus == kus_vas[k]:
                oiged += 1

        edukas = oiged > N / 2
        tulemused.append((nimi, oiged, email, edukas))

        with open("koik.txt", "a", encoding="utf-8") as f:
            f.write(f"{nimi},{oiged},{email}\n")

        if edukas:
            with open("oiged.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi} – {oiged} õigesti\n")
        else:
            with open("valed.txt", "a", encoding="utf-8") as f:
                f.write(f"{nimi}\n")

        saada_email_vastajale(nimi, email, oiged, edukas)

    saada_koondraport(tulemused)
    kuva_tulemused(tulemused)


def saada_koondraport(tulemused):
    if not tulemused:
        return

    parim = max(tulemused, key=lambda x: x[1])

    print(f"\nSaadetud: {TOOANDJA_EMAIL}")
    print("\nTere!\n")
    print("Tänased küsimustiku tulemused:\n")

    for i, (nimi, punktid, email, edukas) in enumerate(tulemused, 1):
        staatus = "SOBIS" if edukas else "EI SOBINUD"
        print(f"{i}. {nimi} – {punktid} õigesti – {email} – {staatus}")

    print(f"\nParim vastaja: {parim[0]} ({parim[1]} õigesti)")
    print("\nLugupidamisega,\nKüsimustiku Automaatprogramm")


def kuva_tulemused(tulemused):
    print("\nEdukalt vastanud:")
    for nimi, punktid, _, edukas in tulemused:
        if edukas:
            print(f"{nimi} – {punktid} punkti")

    print("\nTulemused saadetud e-posti aadressidele.")


def lisa_kusimus():
    k = input("Sisesta uus küsimus: ").strip()
    v = input("Sisesta õige vastus: ").strip().lower()

    with open("kusimused_vastused.txt", "a", encoding="utf-8") as f:
        f.write(f"{k}:{v}\n")

    print("Küsimus lisatud.")


def menuu():
    while True:
        print("\n1. Alusta küsimustikku")
        print("2. Lisa uus küsimus")
        print("3. Välju")

        valik = input("Vali: ")

        if valik == "1":
            alusta_kusimustikku()
        elif valik == "2":
            lisa_kusimus()
        elif valik == "3":
            break
        else:
            print("Vale valik.")


menuu()
