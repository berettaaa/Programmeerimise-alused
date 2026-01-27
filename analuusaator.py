import glob
import os


def leia_projektifailid(laiend):
    return glob.glob(f"*{laiend}")


def analuusi_faili_sisu(failitee):
   
    ridade_kokku = 0
    tuhjad_read = 0
    marksona_arv = 0

    with open(failitee, "r", encoding="utf-8") as fail:
        for rida in fail:
            ridade_kokku += 1

            if rida.strip() == "":
                tuhjad_read += 1

            marksona_arv += rida.count("TODO")
            marksona_arv += rida.count("FIXME")

    return {
        "fail": failitee,
        "ridu_kokku": ridade_kokku,
        "tuhjad_read": tuhjad_read,
        "TODO_FIXME_arv": marksona_arv
    }


def loo_raporti_kataloog(nimi="Analüüsi_Raportid"):
    if not os.path.exists(nimi):
        os.mkdir(nimi)
    return nimi


def leia_failid_algustahega(taht):
    return glob.glob(f"{taht}*.*")
