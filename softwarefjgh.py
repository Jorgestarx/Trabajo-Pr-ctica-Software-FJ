#Software FJ
# Software FJ
# Sistema integral orientado a objetos
# Gestiona clientes, servicios y reservas

from logger import logger
from Excepciones import Nombreinvalidoerror, Dniinvalidoerror, Correoivalidoerror, Telefónoinvalidoerror, Tiempoinvalidoerror, Servicioinvalidoerror
from abc import ABC, abstractmethod


# ------------------------------------------------------------------ #
# Clase abstracta base para los servicios                             #
# ------------------------------------------------------------------ #

class servicios(ABC):
    # Todo servicio debe tener precio, descripción y tipo
    @abstractmethod
    def precio(self):
        pass

    @abstractmethod
    def descripción(self):
        pass

    @abstractmethod
    def tipo(self):
        pass


# ------------------------------------------------------------------ #
# Clases de servicios específicos, heredan de servicios               #
# ------------------------------------------------------------------ #

class reserva_salas(servicios):
    # Calcula el precio según horas, impuesto y descuento
    def precio(self, impuesto=8000, descuento=0, tiempo_reserva=0):
        precio_hora = 20000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial) / 100)
        print(precio_final)

    def descripción(self):
        print("Sala informática para el desarrollo de proyectos, con capacidad para 10 personas y equipada con PCs de alta gama")

    def duración(self, tiempo_reserva):
        print(tiempo_reserva)


class alquiler_equipos(servicios):
    # Precio por hora más bajo que las salas
    def precio(self, impuesto=6000, descuento=0, tiempo_reserva=0):
        precio_hora = 10000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial) / 100)
        print(precio_final)

    def descripción(self):
        print("Alquiler de PCs de alta gama, especializados en tareas informáticas y de programación")

    def duración(self, tiempo_reserva):
        print(tiempo_reserva)


class asesorías(servicios):
    # Mismo precio por hora que salas pero diferente servicio
    def precio(self, impuesto=5000, descuento=0, tiempo_reserva=0):
        precio_hora = 20000
        precio_inicial = tiempo_reserva * precio_hora + impuesto
        precio_final = precio_inicial - ((descuento * precio_inicial) / 100)
        print(precio_final)

    def descripción(self):
        print("Asesorías en gestión de equipos IA, programación de páginas web y hacking")

    def duración(self, tiempo_reserva):
        print(tiempo_reserva)


# ------------------------------------------------------------------ #
# Clase cliente con validaciones para cada dato personal              #
# ------------------------------------------------------------------ #

class cliente():
    def __init__(self):
        self.info = []

        # Validación del nombre
        while True:
            try:
                _nombre = input("Por favor ingrese su nombre completo: ")
                if not _nombre.isalpha() or len(_nombre) < 2 or len(_nombre) > 40:
                    raise Nombreinvalidoerror("El nombre debe contener únicamente letras y tener entre 2 y 40 caracteres.")
            except Nombreinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El nombre ingresado es inválido: '{_nombre}'")
            else:
                print("Nombre registrado correctamente.")
                logger.info(f"Se registró el nombre correctamente: '{_nombre}'")
                break

        # Validación del DNI
        while True:
            try:
                _dni = input("Por favor ingrese su número de identificación: ")
                if not _dni.isdigit() or len(_dni) != 7:
                    raise Dniinvalidoerror("El número de identificación deben ser únicamente dígitos y tener 7.")
            except Dniinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El DNI ingresado es inválido: '{_dni}'")
            else:
                print("DNI registrado correctamente.")
                logger.info(f"Se registró el DNI correctamente: '{_dni}'")
                break

        # Validación del teléfono
        while True:
            try:
                _teléfono = input("Favor ingrese su número de teléfono: ")
                if not _teléfono.isdigit() or len(_teléfono) != 9:
                    raise Telefónoinvalidoerror("El número de teléfono deben ser únicamente dígitos, y debe tener 9")
            except Telefónoinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El número de teléfono ingresado es inválido: '{_teléfono}'")
            else:
                print("Número de teléfono registrado correctamente.")
                logger.info(f"Se registró el número de teléfono correctamente: '{_teléfono}'")
                break

        # Validación del correo
        while True:
            try:
                _correo = input("Por favor ingrese su correo electrónico: ")
                if ("@" not in _correo or
                    "." not in _correo or
                    _correo.startswith("@") or
                    _correo.endswith("@") or
                    _correo.startswith(".") or
                    _correo.endswith(".") or
                    " " in _correo or
                    ("gmail" not in _correo and "yahoo" not in _correo and "outlook" not in _correo) or
                    len(_correo) > 40 or
                    len(_correo) < 5):
                    raise Correoivalidoerror("El correo electrónico debe contener '@' y '.', no puede comenzar ni terminar con '@' o '.', no puede contener espacios, debe ser un correo válido de Gmail, Yahoo o Outlook, y debe tener entre 5 y 40 caracteres.")
            except Correoivalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El correo electrónico ingresado es inválido: '{_correo}'")
            else:
                print("Correo electrónico registrado correctamente.")
                logger.info(f"Se registró el correo electrónico correctamente: '{_correo}'")
                break

        # Guardamos los datos en la lista de info
        self.info.append(_nombre)
        self.info.append(_teléfono)
        self.info.append(_correo)
        self.info.append(_dni)


# ------------------------------------------------------------------ #
# Clase reserva, une cliente y servicio                               #
# ------------------------------------------------------------------ #

class reserva():
    def __init__(self, servicios, cliente):
        self.servicios = servicios
        self.cliente = cliente

        # Validación del tiempo de reserva
        while True:
            try:
                self.tiempo_reserva = int(input("¿Cuántas horas desea pagar el servicio? "))
                if self.tiempo_reserva <= 0:
                    raise Tiempoinvalidoerror("El tiempo de reserva debe ser un número entero positivo.")
            except ValueError as e:
                raise Tiempoinvalidoerror("El tiempo de reserva debe ser un número entero positivo.") from e
            except Tiempoinvalidoerror as e:
                print(f"Error: {e}")
                logger.warning(f"El tiempo de reserva ingresado es inválido: '{self.tiempo_reserva}'")
            else:
                logger.info(f"Se registró el tiempo de reserva correctamente: '{self.tiempo_reserva}' horas")
                print("Tiempo de reserva registrado correctamente.")
                break
            finally:
                logger.info("Intento de registro de tiempo finalizado")

    # Le pasa el tiempo y descuento al método precio del servicio
    def calcular_precio(self, descuento=0, impuesto=0):
        return self.servicios.precio(
            tiempo_reserva=self.tiempo_reserva,
            descuento=descuento,
            impuesto=impuesto
        )

    # Confirma o cancela según respuesta del cliente
    def confirmación(self):
        confreserva = input("¿Desea confirmar su reserva? (si/no): ")
        if confreserva == "sí":
            print(f"Reserva confirmada por {self.cliente}. ¡Gracias por elegir nuestro servicio!")
        elif confreserva == "no":
            print(f"Reserva cancelada por {self.cliente}. Si quiere realizar otra reserva, por favor vuelva a intentar.")

    def cancelación(self):
        cancelar_reserva = input("¿Desea cancelar su reserva? (si/no): ")
        if cancelar_reserva == "sí":
            print(f"Reserva cancelada por {self.cliente}. Lamentamos cualquier inconveniente")
        elif cancelar_reserva == "no":
            print(f"La reserva de {self.servicios} no fue cancelada, si desea cancelarla por favor vuelva a intentar.")


# ------------------------------------------------------------------ #
# Selección del servicio antes de arrancar el sistema                 #
# ------------------------------------------------------------------ #

while True:
    try:
        servicio = input("¿Qué servicio desea reservar? (reserva de salas, alquiler de equipos o asesorías) ")
        if servicio not in ["reserva de salas", "alquiler de equipos", "asesorías"]:
            raise Servicioinvalidoerror("El servicio ingresado no es válido. Por favor, elija entre 'reserva de salas', 'alquiler de equipos' o 'asesorías'.")
    except Servicioinvalidoerror as e:
        print(f"Error: {e}")
        logger.warning(f"El servicio ingresado es inválido: '{servicio}'")
    else:
        if servicio == "reserva de salas":
            print("Ha seleccionado el servicio de reserva de salas.")
        elif servicio == "alquiler de equipos":
            print("Ha seleccionado el servicio de alquiler de equipos.")
        elif servicio == "asesorías":
            print("Ha seleccionado el servicio de asesorías.")
        logger.info(f"Se seleccionó el servicio correctamente: '{servicio}'")
        break
    finally:
        logger.info("Intento de selección de servicio finalizado")


# ------------------------------------------------------------------ #
# Bloque principal, aquí se ejecuta todo el sistema                   #
# ------------------------------------------------------------------ #

if __name__ == "__main__":

    print("=== Bienvenido a Software FJ ===")

    # Registramos el cliente
    print("\n--- Registro de cliente ---")
    c1 = cliente()

    # Creamos el servicio según lo que eligió
    print("\n--- Creando servicio ---")
    if servicio == "reserva de salas":
        s1 = reserva_salas()
    elif servicio == "alquiler de equipos":
        s1 = alquiler_equipos()
    elif servicio == "asesorías":
        s1 = asesorías()

    # Creamos la reserva uniendo cliente y servicio
    print("\n--- Creando reserva ---")
    r1 = reserva(s1, c1)

    # Calculamos el precio con descuento opcional
    print("\n--- Calculando precio ---")
    descuento = int(input("Ingrese el descuento a aplicar (si no desea aplicar descuento, ingrese 0): "))
    r1.calcular_precio(descuento=descuento)

    # Confirmamos la reserva
    r1.confirmación()