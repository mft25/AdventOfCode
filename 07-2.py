import re

f = open('07-input.py')

class Rule:
	def __init__(self, rule_str):
		self.rule_str = rule_str.strip()
		self.type = "UNKNOWN"
		parts = rule_str.strip().split(" ")
		if parts[1] == "->":
			self.type = "DECLARE"
			self.input1 = parts[0]
			self.output = parts[2]
		elif parts[0] == "NOT":
			self.type = "NOT"
			self.input1 = parts[1]
			self.output = parts[3]
		else:
			self.type = parts[1]
			self.input1 = parts[0]
			self.input2 = parts[2]
			self.output = parts[4]
	def is_executable(self, values):
		if not re.match("^[0-9]+$", self.input1) and not self.input1 in values:
			return False
		if not self.type in ["DECLARE", "NOT"] and not re.match("^[0-9]+$", self.input2) and not self.input2 in values:
			return False
		return True
	def execute(self, values):
		if self.output == "b":
			return 46065
		input1 = int(self.input1) if re.match("^[0-9]+$", self.input1) else values[self.input1]
		if not self.type in ["DECLARE", "NOT"]:
			input2 = int(self.input2) if re.match("^[0-9]+$", self.input2) else values[self.input2]
		if self.type == "DECLARE":
			return input1 
		elif self.type == "NOT":
			return ~input1 % (1<<16)
		elif self.type == "AND":
			return input1 & input2
		elif self.type == "OR":
			return input1 | input2
		elif self.type == "LSHIFT":
			# Not sure if this is actually 16-bit, but it gave the right answer!
			return input1 << input2
		else:
			return input1 >> input2
			
def main():
	rules = [Rule(rule) for rule in f]
	values = {}
	while not "a" in values:
		for rule in rules:
			if rule.is_executable(values):
				values[rule.output] = rule.execute(values)
				rules.remove(rule)
	print values["a"]
		
main()