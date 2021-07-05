import sys

class parametros:
    
    def metodo(opcion):

        if(opcion == 1):
            return "SMS"

        elif(opcion == 2):
            return "EMAIL"
    
        elif(opcion == 3):
            return "NTP"
    
        elif(opcion == 4):
            return "SYN"

        elif(opcion == 5):
            return "UDP"

        elif(opcion == 6):
            return "POD"

        elif(opcion == 7):
            return "ICMP"

        elif(opcion == 8):
            return "HTTP"

        elif(opcion == 9):
            return "SLOWLORIS"

        elif(opcion == 10):
            return "MEMCACHED"

        else:
           print("Ninguna opcion")
           sys.exit(1)
