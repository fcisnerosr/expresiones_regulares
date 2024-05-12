# Punto 1
# Extraer direcciones IP de los clientes que realizaron solicitudes al servidor
# Regular expresion: ^\d*\.\d*\.\d\.\d+
# import re; import os
# os.system('clear')

# pattern = re.compile(r'^\d*\.\d*\.\d\.\d+')

# with open('./log.csv', 'r') as f:
#     for line in f:
#         res = re.match(pattern, line)
#         if res:
#             print(res.group())

      
# Punto 2
# Contar cuántas solicitudes se realizaron con cada método HTTP (GET, POST, etc.).
# Reg1 = 'GET'
# Reg2 = 'POST'

# import re; import os
# os.system('clear')

# pattern1 = re.compile(r'\bGET\b')
# pattern2 = re.compile(r'(POST)')

# with open('./log.csv', 'r') as f:
#     v1 = []
#     v2 = []
#     for line in f:
#         res1 = re.search(pattern1, line)
#         if res1:
#             v1.append(1)
#         res2 = re.search(pattern2, line)
#         if res2:
#             v2.append(2)
        
#     print(f'GET  = {len(v1)}')
#     print(f'POST = {len(v2)}')
    

# Punto 3
# Encontrar todas las URLS que devolvieron un código de respuesta 404
# Regex: (T\s)(\w*/\w*[\./\w\d\s?=&]*)
# Regex: (\d{3,3})\s\d

# import re; import os
# os.system('clear')

# pattern1 = re.compile(r'(T\s)(\w*/\w*[\./\w\d\s?=&]*)')
# pattern2 = re.compile(r'(\d{3,3})\s\d')

# with open('./log.csv', 'r') as f:
#     for line in f:
#         re_error = re.search(pattern2, line)
#         if re_error:
#             if re_error.group(1) == '404':
#                 match = re.search(pattern1, line)
#                 print(match.group(2))

# Punto 4
# Analizar el tamaño medio de las respuestas del servidor
# import re; import os
# os.system('clear')

# # Regex = ^\d{3,3}.\d{3,3}.\d.\d\d?
# pattern = re.compile(r'^\d{3,3}.\d{3,3}.\d.\d\d?')

# with open('./log.csv', 'r') as f:
#     count = []
#     for line in f:
#         res = re.match(pattern, line)
#         if res:
#             count.append(1)
#     print(f'Tamaño medio = {len(count)/ 2} ')

# Punto 5
# Identificar las solicitudes que se realizaron a 
# recursos específicos (por ejemplo, todas las 
# solicitudes a archivos de imagen, archivos CSS, 
# archivos JavaScript, etc.)

# import os; import re
# os.system('clear')

# # Regex = \w*[^\d]\.\w{2,4}
# pattern = re.compile(r'\w*[^\d]\.\w{2,4}')

# with open('./log.csv', 'r') as f:
#     for line in f:
#         res = re.search(pattern, line)
#         if res:
#             print(res.group())


# Punto 7
# Buscar todas las solicitudes que contienen parámetros de
# consulta adicionales en la URL
# # Regex = (\?)(\w*=\w*&?\w*=?\w*)
# import os; import re
# os.system('clear')
# pattern = re.compile(r'(\?)(\w*=\w*&?\w*=?\w*)')

# with open('./log.csv', 'r') as f:
#     for line in f:
#         res = re.search(pattern, line)
#         if res:
#             print(res.group(2))

# Punto 8
# Encontrar todas las solicitudes que utilizaron 
# un protocolo HTTP esepecífico (ej, HTTP/1.0)
# regex = (\s)(/\w*\.?[\w?=&/\.]*)
# import re; import os
# os.system('clear')

# pattern  = re.compile(r'(\s)(/\w*\.?[\w?=&/\.]*)')
# pattern2 = re.compile(r'HTTP/1.0')

# with open('./log.csv', 'r') as f:
#     for line in f:
#         res  = re.search(pattern, line)
#         res2 = (re.search(pattern2, line))
#         if res2:
#             if res2.group() == 'HTTP/1.0':
#                 print(res.group(2))