
m_hp = 100
b_hp = 103
b_att = 9
b_def = 2

weapons = [
	[8,4],
	[10,5],
	[25,6],
	[40,7],
	[74,8]
]

armours = [
	[13,1],
	[31,2],
	[53,3],
	[75,4],
	[102,5]
]

rings = [
	[25,1,0],
	[50,2,0],
	[100,3,0],
	[20,0,1],
	[40,0,2],
	[80,0,3],
]

def will_win(m_att, m_def):
	return (m_hp-1)/(max(b_att-m_def,1)) >= b_hp/(max(m_att-b_def,1))
	
def win_price(weapon, armour, ring1, ring2):
	price = weapon[0]
	attack = weapon[1]
	defence = 0
	if armour:
		price += armour[0]
		defence += armour[1]
	if ring1:
		price += ring1[0]
		attack += ring1[1]
		defence += ring1[2]
	if ring2:
		price += ring2[0]
		attack += ring2[1]
		defence += ring2[2]
	return price if will_win(attack, defence) else 1000

def main():
	min_price = 1000
	for weapon in weapons:
		min_price = min(win_price(weapon, None, None, None), min_price)
		for armour in armours:
			min_price = min(win_price(weapon, armour, None, None), min_price)
			for (i, ring1) in enumerate(rings):
				min_price = min(win_price(weapon, armour, ring1, None), min_price)
				for (j, ring2) in enumerate(rings):
					if i != j:
						min_price = min(win_price(weapon, armour, ring1, ring2), min_price)
	print min_price

main()