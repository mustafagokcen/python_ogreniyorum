def find_big_number(): # chapter 4 question 1
	number1 = input("Ilk sayiyi giriniz:")
	number2 = input("Ikinci sayiyi giriniz:")
	if(number1>number2):
		return number1
	else:
		return number2
def body_mass_index(): # chapter 4 question 2
	bmi = float(input("Kilonuzu giriniz:"))/(float(input("Boyunuzu metre cinsinden giriniz:")**2))
	if bmi<18.5:
		text = "Zayıfsınız."
	elif bmi<24.9:
		text = "Normal kilonuzdasınız."
	elif bmi<29.9:
		text = "Fazla kilolusunuz."
	elif bmi<39.9 :
		text = "Şişmansınız."
	else:
		text = "Obezsiniz."
	return text

def back_count(startingpoint,counting,lastpoint): # chapter 4 question 4 and 5 
	numbers = []
	number = startingpoint
	while(number>lastpoint):
		numbers.append(number-counting)
	return numbers

def limitation(first_number,second_number): # chapter 4 question 6
	number = float(input("{} le {} arasinda bir sayi giriniz.").format(first_number,second_number))
	if (number> first_number and number< second number):
		text = "Sayi {} ile {} arasindadir.".format(first_number,second_number)
	else:
		text = "Sayi {} ile {} arasinda degildir.".format(first_number,second_number)
	return text

def create_multiplication table(number): # chapter 4 question 7
	limitation(1,10)
	text = "{} x 1 = {}/n {} x 2= {}/n {} x 3 = {}/n {} x 4 = {}/n {} x 5 = {}/n {} x 6 = {}/n {} x 7 = {}/n {} x 8 = {}/n {} x 9 = {}/n".format(number,number,number,number*2,number,number*3,number,number*4,number,number*5,number,number*6,number,number*7,number,number*8,number,number*9)
	return text

