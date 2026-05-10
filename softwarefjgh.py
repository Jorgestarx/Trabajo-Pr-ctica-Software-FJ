#Software FJ
#Sistema integral orientado objetos
#gestionar clientes, servicios y reservas

#Reservas de salas, alquiler de equipos y asesorías

from abc import ABC, abstractmethod


#Repasar excepciones
#Falta terminar de organizar excepciones en el input
while(True):
    try:
      tiempo_reserva = int(input("¿Cuántas horas desea pagar el servicio? "))
      break
    except ValueError:
        print("Por favor ingrese un número entero válido.")
        

#Revisar condicionales | verificar idea 
pservicio = input("¿Qué servicio desea reservar? (reserva de salas, alquiler de equipos o asesorías) ")
if pservicio == "reserva de salas":
    print("Ha seleccionado reserva de salas")
elif servicio == "alquiler de equipos":
    print("Ha seleccionado alquiler de equipos")
elif servicio == "asesorías":
    print("Ha seleccionado asesorías")


#------------------------------------------------------------------
#Faltan las validaciones del cliente
class cliente():
    _dni = input("Por favor ingrese su número de identificación: ")
    _teléfono = input("Favor ingrese su número de teléfono: ")
    _correo = input("Por favor ingrese su correo eléctronico: ")
    agregar_dni = info.append(_dni)
    agregar_teléfono = info.append(_teléfono)
    agregar_correo = info.append(_correo)

__info = []



#------------------------------------------------------------------

class servicios(ABC):
    @abstractmethod
    def precio():
        pass
    @abstractmethod
    def descripción():
        pass
    @abstractmethod
    def tipo():
        pass




#Falta integrar cliente
#Puede ser ABC, ya que pueden ser diferentes tipos de salas/servicio de sala 
class reserva_salas(servicios):
    def precio():
        precio_hora = 10000
        precio = tiempo_reserva * precio_hora
        print({precio})
    
    def descripción():
        print("Sala informática para el desarrollo de proyectos, con capacidad para 10 personas y equipada con PCs de alta gama")

    def duración():
        print({tiempo_reserva})

    
#Es posible que tenga que cambiar esta clase a ABC, debido a que pueden ser varios tipos de equipo
class alquiler_equipos(servicios):
    def precio():
        precio_hora = 10000
        precio = tiempo_reserva * precio_hora
        print({precio})
    
    def descripción():
        print("Alquiler de PCs de alta gama, especializados en tareas informáticas y de programación")
    
    def duración():
        print({tiempo_reserva})

class asesorías(servicios):
    def precio():
        precio_hora = 20000
        precio = tiempo_reserva * precio_hora
        print({precio})
    
    def descripción():
        print("Asesorías en gestión de equipos IA, programación de páginas web y hacking")
    
      def duración():
        print({tiempo_reserva})


        

class reserva(cliente, servicios):
    def __init__(self, servicios, cliente):

    def confirmación():

    def cancelación():

    def estado():



