#Software FJ
#Sistema integral orientado objetos
#gestionar clientes, servicios y reservas

#Reservas de salas, alquiler de equipos y asesorías

from logger import logger
from Excepciones import Nombreinvalidoerror, Dniinvalidoerror, Correoivalidoerror, Telefónoinvalidoerror, Tiempoinvalidoerror, Servicioinvalidoerror
from abc import ABC, abstractmethod

#tal vez debido a la sobrecarga de argumento no sea necesario el input de tiempo_reserva, ya que se puede agregar como argumento en el método precio de cada clase
#Repasar excepciones
#Falta terminar de organizar excepciones en el input
while(True):
    try:
      tiempo_reserva = int(input("¿Cuántas horas desea pagar el servicio? "))
      break
    except ValueError:
        print("Por favor ingrese un número entero válido.")
        

#Revisar condicionales | verificar idea 
servicio = input("¿Qué servicio desea reservar? (reserva de salas, alquiler de equipos o asesorías) ")
if servicio == "reserva de salas":
    print("Ha seleccionado reserva de salas")
elif servicio == "alquiler de equipos":
    print("Ha seleccionado alquiler de equipos")
elif servicio == "asesorías":
    print("Ha seleccionado asesorías")


#------------------------------------------------------------------
#Ya están las validaciones del cliente, pero creo que se pueden agregar varias más
class cliente():
 def __init__(self, _dni, _nombre, _teléfono, _correo):
        self.info = []
        while(True):
            try:
        
              _nombre = input("Por favor ingrese su nombre completo: ")
              if not _nombre.isalpha() or len(_nombre) < 2 or len(_nombre) > 40:
               raise Nombreinvalidoerror ("El nombre debe contener únicamente letras y tener entre 2 y 40 caracteres.")
            except Nombreinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El nombre ingresado es inválido: '{_nombre}'")
            else:
                print("Nombre registrado correctamente.")
                logger.info(f"Se registró el nombre correctamente: '{_nombre}'")
                break


        while(True):
            try:
              _dni = input("Por favor ingrese su número de identificación: ")
              if not _dni.isdigit() or len(_dni) !=7:
                raise DniInvalidoError("El número de identificación deben ser únicamente dígitos y tener 7.")
            except DniInvalidoError as e:
                print(f"Error: {e}")
                logger.warning(f"El DNI ingresado es inválido: '{_dni}'")
            else:
                print("DNI registrado correctamente.")
                logger.info(f"Se registró el DNI correctamente: '{_dni}'")
                break


        while(True):
            try:
             _teléfono = input("Favor ingrese su número de teléfono: ")
             if not _teléfono.isdigit() or len(_teléfono) != 9:
                 raise TelefonoInvalidoError("El número de teléfono deben ser únicamente dígitos, y debe tener 9")
            except TelefonoInvalidoError as e:
                print(f"Error: {e}")
                logger.warning(f"El número de teléfono ingresado es inválido: '{_teléfono}'")
            else:
                print("Número de teléfono registrado correctamente.")
                logger.info(f"Se registró el número de teléfono correctamente: '{_teléfono}'")
                break


        while(True):
            try:
             _correo = input("Por favor ingrese su correo eléctronico: ")
             if ("@" not in _correo and "." not in _correo and _correo.startswith("@") or _correo.endswith("@") or _correo.startswith(".") or _correo.endswith(".") and " " in _correo and "gmail" not in _correo and "yahoo" not in _correo and "outlook" not in _correo and len(_correo) > 40 or len(_correo) < 5):
                raise Correoinvalidoerror("El correo electrónico debe contener '@' y '.', no puede comenzar ni terminar con '@' o '.', no puede contener espacios, debe ser un correo válido de Gmail, Yahoo o Outlook, y debe tener entre 5 y 40 caracteres.")
            except Correoinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El correo electrónico ingresado es inválido: '{_correo}'")
            else:
                print("Correo electrónico registrado correctamente.")
                logger.info(f"Se registró el correo electrónico correctamente: '{_correo}'")
                break
        
        self.info.append(_nombre)
        self.info.append(_teléfono)
        self.info.append(_correo)
        self.info.append(_dni)
        






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





#Puede ser ABC, ya que pueden ser diferentes tipos de salas/servicio de sala 
class reserva_salas(servicios):
    def precio(self, impuesto = 0, descuento = 0, tiempo_reserva = 0):
        precio_hora = 20000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial)/100)
        print({precio_final})
    
    def descripción():
        print("Sala informática para el desarrollo de proyectos, con capacidad para 10 personas y equipada con PCs de alta gama")

    def duración():
        print({tiempo_reserva})

    
#Es posible que tenga que cambiar esta clase a ABC, debido a que pueden ser varios tipos de equipo
class alquiler_equipos(servicios):
    def precio(self,impuesto = 0, descuento = 0, tiempo_reserva = 0):
        precio_hora = 10000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial)/100)
        print({precio_final})

    def descripción():
        print("Alquiler de PCs de alta gama, especializados en tareas informáticas y de programación")
    
    def duración():
        print({tiempo_reserva})

class asesorías(servicios):
    def precio(self,impuesto = 0, descuento = 0, tiempo_reserva = 0):
        precio_hora = 20000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial)/100)
        print({precio_final})
    
    def descripción():
        print("Asesorías en gestión de equipos IA, programación de páginas web y hacking")
    
    def duración():
        print({tiempo_reserva})


        
#Clase reserva y reserva_salas creo que son representación de lo mismo, es posible que sea necesario implementar método de reserva en reserva_salas
class reserva(cliente, servicios):
    def __init__(self, servicios, cliente, duración):
        self.servicios = servicios
        self.cliente = cliente
        self.duración = duración
    


    def confirmación():
        confreserva = input("¿Desea confirmar su reserva? (si/no): ")
        if confreserva == "sí":
            print(f"Reserva confirmada por {self.cliente}. ¡Gracias por elegir nuestro servicio!")
        elif confreserva == "no":
            print(f"Reserva cancelada por {self.cliente}. Si quiere realizar otra reserva, por favor vuelva a intentar.")

    def cancelación():
        cancelar_reserva = input("¿Desea cancelar su reserva? (si/no): ")
        if cancelar_reserva == "sí":
            print(f"Reserva cancelada por {self.cliente}. Lamentamos cualquier incomveniente")
        elif cancelar_reserva == "no":
            print(f"La reserva de {self.servicio} no fue cancelada, si desea cancelarla por favor vuelva a intentar.")

#No sé del todo bien como aplicar esté método estado, VERIFICAR antes de continuar



