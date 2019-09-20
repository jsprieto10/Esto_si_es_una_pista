import ast


with open("comienzo.txt", "r") as input:
	with open("comienzo.ogg", "wb") as output:
		bytes_list = ast.literal_eval(input.read())

		output.write(bytes(bytes_list))