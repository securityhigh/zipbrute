#!/usr/bin/python
from zipfile import ZipFile
from sys import argv, exit
from os import path, system


database = argv[1]
file = argv[2]
dirname = path.dirname(file)


def unzip(directory, file, password):
	myzip = ZipFile(file, "r")
	myzip.setpassword(password.encode('utf-8'))
	myzip.extractall(directory)

	myzip.close()


def get_passwords(db):
	with open(db, "r") as file:
		return file.readlines()


def main():
	global file, database, dirname

	passwords = get_passwords(database)

	for password in passwords:
		try:
			unzip(dirname, file, password)
			print("success:", password)
			exit()

		except RuntimeError:
			pass

	print("password not found")


if __name__ == "__main__":
	main()