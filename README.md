# Simulando um ataque de Ransomware
## Objetivo
Esse projeto tem como objetivo Criptografar e Descriptografar arquivos, simulando como seria um ataque, onde um arquivo criptografado só seria libereado após o atendmento das exigências.

## Tecnologias:

### Python:

com a biblioteca pyaes que implementa o algoritmo de criptografia AES (Advanced Encryption Standard), um dos algoritmos mais seguros e utilizados.
Necessária a sua instalação: 

*apt install python3-pyaes*

 ## Funcionamento:
 ### Seleção do Arquivo:
 
 O script escolhe um arquivo txt específico para ser criptografado.

### Criptografia:

O conteúdo do arquivo é protegido usando o algoritmo AES com uma chave secreta.

### Remoção do Arquivo Original: 

O arquivo original é deletado para simular a exclusão dos dados.

Criação do Arquivo Criptografado: Um novo arquivo com a extensão ".ransomware_Virus" é gerado, contendo os dados criptografados.

### Descriptografia: 

A descriptografia foi realizada utilizando o mesmo algoritmo (AES) e a chave fornecida pelo atacante. O processo reverte a criptografia, retornando os dados à sua forma original.

https://github.com/user-attachments/assets/7bcc6fe0-d387-49f8-a47a-f6345556bfe1
