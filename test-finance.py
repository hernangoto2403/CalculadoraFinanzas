from finance import *
# creamos el menu 
def main():
# Creacion de una lista para almacenar las cuentas 
    accounts = []
    while  True:
        print("bienvenido a la calculadora de finanzas")
        print("1. crear cuenta")
        print("2. agregar transaccion")
        print("3. ver saldo de la cuenta")
        print("4. ver saldo total")
        print("5. salir")
        
# Capturar opcion seleccionada
         
        option = int(input("ingrese la opcion deseada: "))
        
        # Opcion de salida
        if option == 5:
            print("Cerrando calculadora de finanzas...")
            break

        # Creando una cuenta
        elif option == 1:

            name = input("Ingrese su nombre de cuenta: ")
            account_type = input("Ingrese el tipo de cuenta: ") 
            account_id = create_account(accounts, name, account_type)
            print(f"cuenta '{name}' creada con el id: '{account_id}'")
        
        # Agregando una transaccion 
        elif option == 2:

            account_id = int(input("Ingrese el id de la cuenta: "))
            description = input("ingrese el tipo de cuenta: ")
            amount = float(input("Ingrese el valor de la transaccion: "))
            add_transaction(accounts, account_id, amount)
            print(f"Transaccion de {amount} realizado en la cuenta {account_id}")
        
        # Consultando saldo 
        elif option == 3:
            
            account_id = int(input("Ingrese el id de la cuenta: "))
            balance = get_acc_balance(accounts, account_id)
            print(f"El saldo de la cuenta {account_id} es {balance}")
        
        # Consultar saldo total
        elif option == 4:

            total_balance = get_total_balance(accounts)
            print(f"el saldo total de las cuentas es: {total_balance}")
        
        # Mensaje de error en caso de que la opcion ingresada no sea valida 
        else:
            print("opcion no reconocida, por favor ingrese de nuevo ")
 
if __name__ == "__main__":
    main()