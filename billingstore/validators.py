from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify

def validate_ruc(document_id):
	accepted_length= 13
	third_digit_accepted = 6
	base_module = 11
	position_digit_calculator = 9
	coefficients = [3, 2, 7, 6, 5, 4, 3, 2]
	establishment_number = [0,0,0,1]
	provincial_codes = list(range(1,25))

	received_length = len(str(document_id))
	if not equal_values(accepted_length,received_length):
		raise ValidationError(
			_('%(document_id)s Solo se permiten %s caracteres'  %(accepted_length)),
			params={'document_id': document_id},)
	else:
		ruc_array = list(map(int,str(document_id)))
		third_digit_received = ruc_array[2]
		establishment_number_received = ruc_array[9:]
		if not equal_values(third_digit_accepted, third_digit_received) or not\
			   equal_values(establishment_number, establishment_number_received):
			   raise ValidationError(
			   	_('%(document_id)s Formato de RUC invalido'),
			   	params={'document_id': document_id},)
		else:
			#los dos primeros digitos deben estar entre 01 y 24
			provicincial_code_received = int(str(document_id)[:2])
			new_array_ruc = []
			if (provicincial_code_received in provincial_codes):
				sequential_digits_received = ruc_array[:8]
				for i in range(0,8):
					new_array_ruc.append(sequential_digits_received[i] * coefficients[i])
				
				resulting_module_value = add_digits(new_array_ruc) % base_module
				if resulting_module_value == 0:
					check_digit = 0
				else:
					check_digit = base_module - resulting_module_value

				if equal_values(check_digit, ruc_array[position_digit_calculator-1]):
					return True
				else:
					raise ValidationError(
						_('%(document_id)s Formato de RUC invalido'),
						params={'document_id': document_id},)
			else:
				raise ValidationError(
						_('%(document_id)s Formato de RUC invalido'),
						params={'document_id': document_id},)

def validate_ruc_natural_juridical(document_id):
	accepted_length= 13
	third_digit_accepted = 9
	base_module = 11
	position_digit_calculator = 10
	coefficients = [4, 3, 2, 7, 6, 5, 4, 3, 2]
	establishment_number = [0,0,0,1]
	provincial_codes = list(range(1,25))
	foreings_provincial_code = 30

	received_length = len(str(document_id))
	if not equal_values(accepted_length,received_length):
		raise ValidationError(
			_('%(document_id)s Solo se permiten %s caracteres'  %(accepted_length)),
			params={'document_id': document_id},)
	else:
		ruc_array = list(map(int,str(document_id)))
		third_digit_received = ruc_array[2]
		establishment_number_received = ruc_array[9:]
		if not equal_values(third_digit_accepted, third_digit_received) or not\
			   equal_values(establishment_number, establishment_number_received):
			   raise ValidationError(
				_('%(document_id)s Formato de RUC invalido'),
				params={'document_id': document_id},)
		else:
			#los dos primeros digitos deben estar entre 01 y 24
			provicincial_code_received = int(str(document_id)[:2])
			new_array_ruc = []
			if (provicincial_code_received in provincial_codes) or\
				(equal_values(foreings_provincial_code, provicincial_code_received)):

				sequential_digits_received = ruc_array[:9]
				for i in range(0,9):
					new_array_ruc.append(sequential_digits_received[i] * coefficients[i])
				
				resulting_module_value = add_digits(new_array_ruc) % base_module
				if resulting_module_value == 0:
					check_digit = 0
				else:
					check_digit = base_module - resulting_module_value

				if equal_values(check_digit, ruc_array[position_digit_calculator-1]):
					return True
				else:
					raise ValidationError(
						_('%(document_id)s Formato de RUC invalido'),
						params={'document_id': document_id},)
			else:
				raise ValidationError(
					_('%(document_id)s Formato de RUC invalido'),
					params={'document_id': document_id},)

def validate_document_person(document_id):
	received_length = len(str(document_id))
	accepted_length = [10,13]
	if (received_length not in accepted_length):
		return False
	else:
		return True

def validate_ruc_natural(document_id):
	accepted_length= 13
	third_digit_accepted = list(range(0,6))
	base_module = 10
	position_digit_calculator = 10
	coefficients = [2, 1, 2, 1, 2, 1, 2, 1, 2]
	establishment_number = [0,0,1]
	provincial_codes = list(range(1,25))
	foreings_provincial_code = 30

	received_length = len(str(document_id))
	if not equal_values(accepted_length,received_length):
		return False
	else:
		ruc_array = list(map(int,str(document_id)))
		third_digit_received = ruc_array[2]
		establishment_number_received = ruc_array[10:]
		if not (third_digit_received in third_digit_accepted) or not\
			   equal_values(establishment_number, establishment_number_received):
			return False
		else:
			#los dos primeros digitos deben estar entre 01 y 24
			provicincial_code_received = int(str(document_id)[:2])
			new_array_ruc = []
			if (provicincial_code_received in provincial_codes) or\
				(equal_values(foreings_provincial_code, provicincial_code_received)):

				sequential_digits_received = ruc_array[:9]
				for i in range(0,9):
					new_array_ruc.append(sequential_digits_received[i] * coefficients[i])
				#print(new_array_ruc)
				valid_array_ruc = digits_not_more_than_nine(new_array_ruc)
				resulting_module_value = add_digits(valid_array_ruc) % base_module
				#print(resulting_module_value)
				if resulting_module_value == 0:
					check_digit = 0
				else:
					check_digit = base_module - resulting_module_value

				if equal_values(check_digit, ruc_array[position_digit_calculator-1]):
					return True
				else:
					return False
			else:
				return False

def validate_document_natural(document_id):
	accepted_length= 10
	third_digit_accepted = list(range(0,6))
	base_module = 10
	position_digit_calculator = 10
	coefficients = [2, 1, 2, 1, 2, 1, 2, 1, 2]
	provincial_codes = list(range(1,25))
	foreings_provincial_code = 30

	received_length = len(str(document_id))
	if not equal_values(accepted_length,received_length):
		return False
	else:
		document_array = list(map(int,str(document_id)))
		third_digit_received = document_array[2]
		if not (third_digit_received in third_digit_accepted):
			return False
		else:
			#los dos primeros digitos deben estar entre 01 y 24
			provicincial_code_received = int(str(document_id)[:2])
			new_array_ruc = []
			if (provicincial_code_received in provincial_codes) or\
				(equal_values(foreings_provincial_code, provicincial_code_received)):

				sequential_digits_received = document_array[:9]

				even_array = set_array_of_even(sequential_digits_received)
				impar_array = set_array_of_impares(sequential_digits_received)
				pares_multiplied = []

				for i in even_array:
					num = i * 2
					if num > 9:
						num = num - 9
					pares_multiplied.append(num)

				final_result = add_digits(pares_multiplied) + add_digits(impar_array)

				resulting_module_value = final_result % base_module

				#print(resulting_module_value)
				if resulting_module_value == 0:
					check_digit = 0
				else:
					check_digit = base_module - resulting_module_value

				if equal_values(check_digit, document_array[position_digit_calculator-1]):
					return True
				else:
					return False
			else:
				return False

def set_array_of_even(array_digit):
	even_array = []
	for i in range(0,len(array_digit)):
		if ((i+1) % 2) == 0:
			even_array.append(array_digit[i])
	return even_array

def set_array_of_impares(array_digit):
	impar_array = []
	for i in range(0,len(array_digit)):
		if ((i+1) % 2) != 0:
			impar_array.append(array_digit[i])
	return impar_array

def digits_not_more_than_nine(array_digit):
	new_array = []
	for i in array_digit:
		if i > 9:
			new_array.append(i - 9)
		else:
			new_array.append(i)
	return new_array

def add_digits(array_digit):
	#add digits into an array
	if len(array_digit) == 1:
		return array_digit[0]
	else:
		return array_digit[0] + add_digits(array_digit[1:])

def equal_values(value_acepted, value_received):
	if value_acepted == value_received:
		return True
	return False

