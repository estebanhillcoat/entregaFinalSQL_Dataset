import dataset                    # Importa la librería dataset para trabajar fácilmente con bases de datos SQLite

miBase = dataset.connect("sqlite:///info.db")  # Conecta a la base de datos info.db (la crea si no existe)

tabla = miBase["Personas"]        # Obtiene la tabla "Personas" (la crea si no existe)

while True:                       # Bucle principal del programa

    # Muestra el menú y guarda la opción elegida por el usuario
    opciones = input(
        "\nG - Busqueda multiple\n"
        "B - Buscar\n"
        "S - Salir\n"
        "A - agregar\n"
        "L - Listar\n"
        "*** Borrar ***\n"
        "N - Borrar por nombre\n"
        "I - Borrar por ID\n"
    )

    match opciones:               # Evalúa la opción ingresada

        case "S":
            break                 # Sale del programa

        case "G":
            # Solicita un nombre para buscar
            nombre_a_buscar = input("\nBuscar (multiple): ").strip()

            # Busca todos los registros que tengan ese nombre
            encontro = tabla.find(Nombre=nombre_a_buscar)

            # Recorre todos los resultados encontrados
            for encontrado in encontro:
                print(
                    f'Se encontró a {encontrado["Nombre"]} '
                    f'en el ID: {encontrado["id"]}'
                )

        case "B":
            # Solicita un nombre para buscar
            nombreBuscar = input("\nNombre a buscar: ").strip()

            # Busca el primer registro que coincida
            existe = tabla.find_one(Nombre=nombreBuscar)

            # Comprueba si encontró un resultado
            if existe:
                print(f"Se encontó {nombreBuscar}")
            else:
                print(f"*** NO se encontró {nombreBuscar} ***")

        case "N":
            # Solicita el nombre de la persona a eliminar
            borrarNombre = input("\nNombre persona a borrar: ")

            # Borra todos los registros con ese nombre
            tabla.delete(Nombre=borrarNombre)

            # Mensaje de confirmación
            print(borrarNombre + " Borrado con exito!\n")

        case "I":
            # Solicita el ID a eliminar y lo convierte a entero
            borrarPorID = int(input("\nID a borrar: "))

            # Borra el registro cuyo ID coincida
            tabla.delete(id=borrarPorID)

            # Mensaje de confirmación
            print(f'{borrarPorID} fué borrado con exito!!')

        case "L":
            # Recorre todos los registros de la tabla
            for persona in tabla:

                # Muestra nombre, apellido e ID
                print(
                    f'Nombre: {persona["Nombre"]} | '
                    f'Apellido: {persona["Apellido"]} | '
                    f'ID: {persona["id"]}'
                )

        case "A":
            # Solicita nombre
            suNombre = input("\nNombre: ")

            # Solicita apellido
            suApellido = input("\nApellido: ")

            # Inserta un nuevo registro en la tabla
            tabla.insert({
                "Nombre": suNombre,
                "Apellido": suApellido
            })


Observación: find() puede devolver varios registros, mientras que find_one() devuelve solamente el primero que encuentre. Por eso en "G" usás un for, pero en "B" no hace falta.
