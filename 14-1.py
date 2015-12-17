
f = open('14-input.py')

def distance_by_time(speed, stamina, rest, time):
	complete_cycles = time/(stamina+rest)
	return complete_cycles*speed*stamina + min(time%(stamina+rest), stamina)*speed

def main(race_time):
	max_distance = 0
	for line in f:
		parts = line.split()
		distance = distance_by_time(int(parts[3]), int(parts[6]), int(parts[-2]), race_time)
		max_distance = max(distance, max_distance)
	print max_distance

main(2503)