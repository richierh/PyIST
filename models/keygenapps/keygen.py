import random
global lisensi
# import AppsSDS.authenticationFrameWarningKeyFF


class Lisensi():

	def __init__(self, parent):

		lisensi = parent
		self.hasil()

	def hasil(self):
		return lisensi


class Key():

	def __init__(self, key=''):
		global lisensi
# 		print ("sukses")
		if key == '':
			# self.key = self.generate()
			pass
		else:
			self.key = key.lower()

	def verify(self, lisensi):
		self.lisensi = lisensi
		print ("lewat sini")
		score = 0
		check_digit = self.key[0]
		check_digit_count = 0
		chunks = self.key.split('-')
		for chunk in chunks:
			if len(chunk) != 4:
				return False
			for char in chunk:
				if char == check_digit:
					check_digit_count += 1
				score += ord(char)
		if score == self.lisensi and check_digit_count == 3:
			return True
		return False

	def generate(self):
		# global lisensi
		key = ''
		chunk = ''
		check_digit_count = 0
		alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'
		while True:
			while len(key) < 25:
				char = random.choice(alphabet)
				key += char
				chunk += char
				if len(chunk) == 4:
					key += '-'
					chunk = ''
			key = key[:-1]
			if Key(key).verify(lisensi):
				return key
			else:
				key = ''

	def __str__(self):
	
		valid = 'Invalid'
		if self.verify(lisensi):
			valid = 'Valid'
			
		return self.key.upper() + ':' + valid

		
if __name__ == "__main__":
	key = Key('PJXJ-AC5Z-Y7CZ-3UAW-Q9FC')	
	# key = Key('0CQD-04NL-743Y-YQVT-H0ED')
	# key = Key('')
	# global lisensi
	lisensi = 1788
	total = 223452987
	# lisensi = self.nilai*4 + 223445435
	# lisensi = (total - 223445435)/4
	# lisensi = 1830
# 	print (key.verify(lisensi))
	print ("Sukses")
	print (Key('khkh'))
# 	print (lisensi)
	print (key.verify(lisensi))
	pass
