import csv


def fn_question(question):
    return input(question)


def fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, plateforme, note):
    fichier_csv = "projet jeux du grenier.csv"
    header = ["nom_du_jeu", "genre", "éditeur", "année_de_sortie", "plateforme", "note"]
    data = [nom_du_jeu, editeur, genre, editeur, annee_de_sortie, plateforme, note]
    with open(fichier_csv, "w", encoding="utf-8", newline="") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(header)
        writer.writerow(data)


def fn_oldschool(annee_de_sortie):
    if (annee_de_sortie >= 2006):
        return True
    else:
        return False

q_nom_du_jeu= "Le nom du jeu :"
nom_du_jeu = fn_question(q_nom_du_jeu)
q_editeur = "L'éditeur :"
editeur = fn_question(q_editeur)
q_genre = "Le genre du jeu :"
genre = fn_question(q_genre)
q_annee_de_sortie = "L'année de sortie :"
annee_de_sortie = int(fn_question(q_annee_de_sortie))
q_plateforme = "Plateforme :"
plateforme = fn_question(q_plateforme)
q_note = "La note :"
note = fn_question(q_note)

fn_encode(nom_du_jeu, editeur, genre, annee_de_sortie, plateforme, note)


if fn_oldschool(annee_de_sortie):
    print(nom_du_jeu, "est un jeu récent")
else:
    print(nom_du_jeu, "est un jeu ancien")