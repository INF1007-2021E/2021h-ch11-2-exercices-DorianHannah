"""
Chapitre 11.3

Fonctions pour simuler un combat.
"""


import random

import utils
from character import *
from magician import *


def deal_damage(attacker: Character, defender: Character):
	if isinstance(attacker, Magician) and attacker.will_use_spell():
		weapon_used = attacker.spell
	else:
		weapon_used = attacker.weapon
	damage, crit = attacker.compute_damage(defender)
	defender.hp -= damage
	print(f"\t\t{attacker.name} a utilisé {weapon_used.name}")
	if crit:
		print("\t\t\tCoup critique!")
	print(f"\t\t{defender.name} prend {damage} dommages\n")

def run_battle(c1: Character, c2: Character):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	attacker = c1
	defender = c2
	turns = 1
	print(f"{attacker.name} commence un combat contre {defender.name}!")
	print(f"\t{attacker.name}: Ça va chauffer bebewwww !\n")
	print(f"\t{defender.name} : Vas-y approche toi pour voir !\n")
	while True:
		deal_damage(attacker, defender)
		if defender.hp == 0:
			print(f"{defender.name} a donné sa langue au chat... littéralement!")
			print(f"{attacker.name} a triomphé")
			break
		turns += 1
		attacker, defender = defender, attacker
	return turns
