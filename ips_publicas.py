import socket

def obtener_dominios_desde_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.read().splitlines()
            dominios = []
            for linea in lineas:
                dominio = linea.split('/')[0]
                dominios.append(dominio)
            return dominios
    except FileNotFoundError:
        print(f'No se encontró el archivo "{nombre_archivo}"')
        return []

def obtener_ips(dominios):
    ips = []
    for dominio in dominios:
        try:
            ip = socket.gethostbyname(dominio)
            ips.append(ip)
        except socket.gaierror:
            ips.append('No se pudo resolver')
    return ips

nombre_archivo = input('Ingrese el nombre del archivo: ')
dominios = obtener_dominios_desde_archivo(nombre_archivo)
ips = obtener_ips(dominios)

print('Direcciones IP encontradas:')
for ip in ips:
    print(ip)
