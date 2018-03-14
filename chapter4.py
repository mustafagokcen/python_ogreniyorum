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

def create_multiplication_table(number): # chapter 4 question 7
	if(limitation(1,10)):
		text = "{} x 1 = {}/n {} x 2= {}/n {} x 3 = {}/n {} x 4 = {}/n {} x 5 = {}/n {} x 6 = {}/n {} x 7 = {}/n {} x 8 = {}/n {} x 9 = {}/n".format(number,number,number,number*2,number,number*3,number,number*4,number,number*5,number,number*6,number,number*7,number,number*8,number,number*9)
		return text
	else:
		text = "Sayi belirtilen aralikta degil."
		return text

def create_multiplication_with_recursive(number): # chapter 4 question 8
	for i in range(1,10):
		for j in range(1,10):
			text = "{%d}*{%d}=%d".format(i,j,i*j)
	return text


def create_new_string(): #chapter 4 question 9
	i = 0
	j = 0
	array = []
	while(i<20):
		if j==0:
			array.append("-1")
			j = 1
		else:
			array.append("1")
			j = 0
	return array

def decision_prime_number(number): # chapter 4 question 10
	if (limitation(1,500)):
		i=2
		while(i<number):
			if(number%i==0):
				text = "Sayı asal degildir ve %s sayisina bolunur".format(i)
				break
			else:
				continue
		if(i == number):
			text = "Sayı asaldır"
	else:
		text = "Sayi belirtilen aralikta degil"
	return text

def faktor(number): # chapter 4 question 11
	if(number>0):
		number = number*faktor(number-1)
	return number

def sin(x): # chapter 4 question 12
	sinx = x



question_number = int(input("Lutfen Question numarasini giriniz ve entera basiniz:"))
if(question_number == 1):
	find_big_number() # chapter 4 question 1
elif(question_number == 2):
	body_mass_index()
elif(question_number==4 or question_number==5):
	startingpoint = int(input("Lutfen baslangic noktasini giriniz:"))
	counting = int(input("Lutfen kacar kacar saymasını istediginizi giriniz:"))
	lastpoint = int(input("Lutfen bitis noktasini giriniz:"))
	back_count(startingpoint,counting,lastpoint)
elif(question_number==6):
	first_number = 1
	second_number = 100
	text = limitation(1,100)
elif(question_number==7):
	number = int(input("Lutfen carpim tablosunu gormek istediginiz sayiyi giriniz:"))
	create_multiplication_table(number)
elif(question_number==8):
	create_multiplication_with_recursive()
elif(question_number==9):
	create_new_string
