import random
from colorama import Fore, Style, init

init(autoreset=True)

sonad = [
    "terav", "eesti", "põnev", "sadam", "kegel"
]

sonad = [s for s in sonad if len(s) == 5]

salasona = random.choice(sonad)
katsete_arv = 6
pikkus = len(salasona)

print(f"sõna pikkus on {pikkus}.")
print("-" * pikkus)

kasutatud_tahed = set()

def anna_tagasiside(pakkumine, salasona):
    tulemus = ""
    for i in range(len(pakkumine)):
        if pakkumine[i] == salasona[i]:
            tulemus += Fore.GREEN + pakkumine[i]
        elif pakkumine[i] in salasona:
            tulemus += Fore.YELLOW + pakkumine[i]
        else:
            tulemus += Fore.RED + pakkumine[i]
    return tulemus + Style.RESET_ALL

for katse in range(1, katsete_arv + 1):
    pakkumine = input(f"\nKatse {katse}/{katsete_arv}: ").lower()

    if len(pakkumine) != pikkus:
        print("Vale pikkus! Proovi uuesti.")
        continue

    kasutatud_tahed.update(pakkumine)

    print(anna_tagasiside(pakkumine, salasona))

    print("Kasutatud tähed:", " ".join(sorted(kasutatud_tahed)))

    if pakkumine == salasona:
        print(Fore.GREEN + "\n Õige! Arvasid sõna ära!")
        break
else:
    print(Fore.RED + f"\n Mäng läbi! Õige sõna oli: {salasona}")


