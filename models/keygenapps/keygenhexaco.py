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
# 		print ("sukses")
		if key == '':
			self.key = self.generate()
		else:
			self.key = key.lower()

	def verify(self, lisensi):
		lisensi = lisensi
# 		print ("lewat sini")
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
		if score == lisensi and check_digit_count == 3:
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
	key = Key('K2UN-9I2O-78GZ-E93H-JFKK')	

	lisensi_total = input("Silahkan masukkan nomor referensi software\n")
# 	lisensi = 1853
# 	lisensi_total = 223452987
# 	lisensi = self.nilai*4 + 223445435
# 	lisensi = (int(lisensi_total) -)/4

	lastdigit = int(repr(int(lisensi_total))[0:4])
	lisensi = int(lastdigit/4)
	

# 	lisensi = 1830
# 	print (Key.verify(lisensi))
	print ("Sukses")
	print (Key())
	input = input("\n")

# 	print (lisensi)
# 	print (Key.verify(lisensi))
	pass
