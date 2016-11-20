from __future__ import print_function
import json

def read_json(file_path):
	with open(file_path, 'r') as file:
		data = json.load(file)
	return data

def check_unique(string):
	if len(string) <= 1:
		return True
	sorted_str = sorted(string)
	next_char = sorted_str[1]
	for char in sorted_str:
		if char == next_char:
			return False
		next_char = char
	return True


def check_unique_bit(string):
	check = 0
	for char in string:
		aux = ord(char) - ord('a')
		if check & 1 << aux > 0:
			return False
		check = check | 1 << aux
	return True

data = read_json("sample.json")
for i in data.values():
	print(check_unique(i))
	print(check_unique_bit(i))

