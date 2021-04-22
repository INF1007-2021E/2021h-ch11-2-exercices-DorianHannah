"""
Chapitre 11.3
"""


import math
from inspect import *

from game import *


def simulate_battle():
	positive_vibes = Weapon("Énergies positives", 53, 4)
	rale = Weapon("Rallement", 40, 3)
	epee_de_feu = Weapon("Épée de feu", 63, 5)
	pain_choc = Weapon("Pain au chocolat", 48, 2)

	Titi = Character("Thibault le titan", 100, 65, 16, 6)
	Dodo = Character("Dodo la malice", 110, 52, 21, 4)
	Emma = Character("Emma la Rebelle", 140, 72, 11, 5)

	Jerry = Magician("Jerry le Mistigri", 74, 60, 70, 53, 32, 4)
	Valentin = Magician("Valentin le Panda Démoniaque", 95, 50, 48, 60, 50, 6)

	jet_croquette = Spell("Jet de croquettes enchantées", 42, 15, 3)
	eucalyptus = Spell("Poussière d'eucalyptus magiques", 40, 18, 4)

	Titi.weapon = epee_de_feu
	Dodo.weapon = positive_vibes
	Emma.weapon = epee_de_feu

	Jerry.spell = jet_croquette
	Valentin.spell = eucalyptus
	Jerry.using_magic = True
	Valentin.using_magic = True

	turns = run_battle(Dodo, Jerry)
	print(f"Le combat s'est terminé en {turns} tours !")


def main():
	simulate_battle()

if __name__ == "__main__":
	main()

