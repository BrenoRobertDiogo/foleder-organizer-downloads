from os import mkdir, system
import os
import re
from time import sleep
import shutil

#input('O arquivo TEM que estar na pasta downloads')

identificar = r"(.*)[.](.*)"

pastaAtual = r'C:\Users\breno\Downloads'

for root, dirs, files in os.walk(pastaAtual):

	for file in files:
		caminhoAntigo = os.path.join(root, file)
		
		encontrar = re.search(identificar, file)
		print(f'O {encontrar.group(1)} está sendo movido', end='...')

		print('\n')
		print('==============='*5)
		sleep(0.5)
		novo = encontrar.group(2)
		caminhoNovo = os.path.join(fr"{pastaAtual}\{novo}", file)
		print(caminhoNovo, '\n', caminhoAntigo)

		if file != 'organizar.py' and caminhoAntigo!=caminhoNovo:
			
			try:
				mkdir(fr"{pastaAtual}\\{novo}")
				
				print(fr"{pastaAtual}\\{novo}\n{novo}")
				shutil.move(caminhoAntigo, caminhoNovo)

				print(f'=== {file} foi movido com sucesso ===')

			except FileExistsError as e:
				shutil.move(caminhoAntigo, caminhoNovo)
				print(f'         |{file} foi movido com sucesso         |')

			print('==============='*5)
		elif file != 'organizar.py' and caminhoAntigo == caminhoNovo: 
			print(f'         |{file} foi já tinha sido movido         |')