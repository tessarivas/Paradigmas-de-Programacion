'''
NOMBRE: Teresa Rivas Gómez
MATRICULA: 372565
MATERIA: Paradigmas de la Programación
PROGRAMA: Sistema Bancario
FECHA INICIO: 19/05/2024
FECHA FINAL: 23/05/2024

FUNCIONES:
- MENU INICIO (REGISTRAR O INICIAR SESION) INGRESAR DATOS (NOMBRE, NUM CUENTA)
- TRANSACCIONES (TRANSFERIR, RETIRAR, DEPOSITAR) CON NUM DE CUENTA Y CANTIDAD
- MOSTRAR SALDO (NOMBRE, NUM DE CUENTA Y SALDO ACTUAL)
- REALIZAR OTRA PARA SALIR

DEBE CONTENER:
- CLASES, OBJETOS Y ABSTRACCION
- ENCAPSULAMIENTO, HERENCIA Y POLIMORFISMO
'''

# CLASE PARA PROPIETARIO DE UNA CUENTA
class Cuenta:
    def __init__(self, nombre, numero):
        self._nombre = nombre
        self._numero = numero

    @property
    def nombre(self):
        return self._nombre

    @property
    def numero(self):
        return self._numero

# CLASE PARA EL BANCO, TRANSACCIONES A REALIZAR
class Banco(Cuenta):
    def __init__(self, nombre, numero, saldo=0.0):
        super().__init__(nombre, numero)
        self._saldo = saldo

    # MOSTRAR DATOS DE CUENTA: NOMBRE, NUMERO Y SALDO
    def mostrar(self):
        print('-------------------------------------')
        print('           C  U  E  N  T  A          ')
        print('-------------------------------------')
        print(f'Propietario: {self.nombre.upper()}')
        print(f'Numero: {self.numero}')
        print(f'Saldo actual: ${self._saldo:.2f}')

    # DEPOSITAR DINERO A MI CUENTA
    def depositar(self, cantidad):
        self._saldo += cantidad

    # RETIRAR DINERO DE MI CUENTA
    def retirar(self, cantidad):
        if self._saldo < cantidad:
            print('Saldo insuficiente.')
        else:
            self._saldo -= cantidad
            print(f'Retiro: ${cantidad:.2f}.')
            print(f'Saldo actual es ahora de: ${self._saldo:.2f}')

    # TRANSFERIR A OTRA CUENTA
    def transferir(self, cuenta_destino, cantidad):
        if self._saldo < cantidad:
            print('Saldo insuficiente.')
        else:
            self._saldo -= cantidad
            cuenta_destino.depositar(cantidad)
            print(f'Transferencia de ${cantidad:.2f} exitosa.')

    # TRANSACCIONES QUE PUEDO REALIZAR DESDE MI CUENTA
    def transaccion(self, usuarios):
        while True:
            # DESPLIEGUE DEL MENU
            print('''
-------------------------------------                 
            B  A  N  C  O
-------------------------------------
    Menu:
    1. Mostrar
    2. Depositar
    3. Retirar
    4. Transferir
    5. Salir
-------------------------------------
            ''')
            try:
                opcion = int(input('Ingresa una opcion: '))
                if opcion == 1:
                    # MOSTRAR CUENTA
                    self.mostrar()
                elif opcion == 2:
                    # DEPOSITAR
                    print('-------------------------------------')
                    print('      D  E  P  O  S  I  T  A  R      ')
                    print('-------------------------------------')
                    cantidad = float(input('Ingrese la cantidad que desea depositar: '))
                    self.depositar(cantidad)
                    print(f'Deposito: ${cantidad:.2f}.')
                    print(f'Saldo actual es ahora de: ${self._saldo:.2f}')
                elif opcion == 3:
                    # RETIRAR
                    print('-------------------------------------')
                    print('         R  E  T  I  R  A  R         ')
                    print('-------------------------------------')
                    cantidad = float(input('Ingrese la cantidad que desea retirar: '))
                    self.retirar(cantidad)
                elif opcion == 4:
                    # TRANSFERIR
                    print('-------------------------------------')
                    print('      T  R  A  N  S  F  E  R  I  R   ')
                    print('-------------------------------------')
                    numero_destino = input('Ingrese el numero de cuenta de destino: ')
                    if numero_destino in usuarios:
                        cantidad = float(input('Ingrese la cantidad que desea transferir: '))
                        self.transferir(usuarios[numero_destino], cantidad)
                    else:
                        print('Cuenta de destino no encontrada.')
                elif opcion == 5:
                    # SALIR DE LA CUENTA
                    print('Saliste de la cuenta.')
                    break
                else:
                    print('Opción no valida.')
            except ValueError:
                print('Error: Solo numeros indicados.\n')

def menu_inicio():
    usuarios = {}
    while True:
        print('''
-------------------------------------                 
      M  E  N  U | B  A  N  C  O
-------------------------------------
    1. Registrar
    2. Iniciar Sesión 
    3. Salir
-------------------------------------
        ''')
        try:
            opcion = int(input('Ingresa una opcion: '))
            if opcion == 1:
                # REGISTRAR NUEVA CUENTA
                print('-------------------------------------')
                print('      R  E  G  I  S  T  R  A  R      ')
                print('-------------------------------------')
                nombre = input('Ingrese su nombre: ')
                numero = input('Ingrese numero de cuenta: ')
                if numero in usuarios:
                    print('La cuenta ya existe.')
                else:
                    usuarios[numero] = Banco(nombre, numero)
                    print(f'Cuenta registrada exitosamente.\nPara {nombre} con numero {numero}.\n')
            elif opcion == 2:
                # INICIAR SESION EN CUENTA YA EXISTENTE
                print('-------------------------------------')
                print('         I  N  I  C  I  A  R         ')
                print('-------------------------------------')
                numero = input('Ingrese numero de cuenta: ')
                if numero in usuarios:
                    print(f'Bienvenido de nuevo, {usuarios[numero].nombre}.\n')
                    usuarios[numero].transaccion(usuarios)
                else:
                    print('Cuenta no encontrada.\nPor favor registrese primero.\n')
            elif opcion == 3:
                # SALIR DEL BANCO
                print('Gracias por usar el sistema bancario.')
                break
            else:
                print('Opcion no valida.')
        except ValueError:
            print('Error: Solo numeros indicados.\n')

if __name__ == "__main__":
    menu_inicio()