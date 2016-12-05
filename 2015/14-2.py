
f = open('14-input.py')

def distance_by_time(speed, stamina, rest, time):
	complete_cycles = time/(stamina+rest)
	return complete_cycles*speed*stamina + min(time%(stamina+rest), stamina)*speed

def main(race_time):
	reindeer = []
	for line in f:
		parts = line.split()
		reindeer.append([0, 0, int(parts[3]), int(parts[6]), int(parts[-2])])
	for t in xrange(1, race_time + 1):
		max_distance = 0
		for racer in reindeer:
			distance = distance_by_time(racer[2], racer[3], racer[4], t)
			racer[0] = distance
			max_distance = max(distance, max_distance)
		for racer in reindeer:
			if racer[0] == max_distance:
				racer[1] += 1  
	print max([racer[1] for racer in reindeer])

main(2503)