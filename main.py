import dataset
miBase = dataset.connect("sqlite:///info.db")
tabla = miBase["Personas"]

while True: 
    opciones = input("\nG - Busqueda multiple\nB - Buscar\nS - Salir\nA - agregar\nL - Listar\n*** Borrar ***\nN - Borrar por nombre\nI - Borrar por ID\n")
    
    match opciones:
        case "S":
            break
        case "G":
            nombre_a_buscar = input("\nBuscar (multiple): ").strip()
            encontro = tabla.find(Nombre=nombre_a_buscar)
            
            for encontrado in encontro:
                print(f'Se encontró a {encontrado["Nombre"]} en el ID: {encontrado["id"]}')
            
        case "B":
            nombreBuscar = input("\nNombre a buscar: ").strip()
            existe = tabla.find_one(Nombre=nombreBuscar)
            
            if existe:
                print(f"Se encontó {nombreBuscar}")
            else:
                print(f"*** NO se encontró {nombreBuscar} ***")
            
        
        case "N":
            borrarNombre = input("\nNombre persona a borrar: ")
            tabla.delete(Nombre=borrarNombre)
            print(borrarNombre + " Borrado con exito!\n")
        case "I":
            borrarPorID = int(input("\nID a borrar: "))
            tabla.delete(id=borrarPorID)
            print(f'{borrarPorID} fué borrado con exito!!')
            
        case "L":
            for persona in tabla:
                print(f'Nombre: {persona["Nombre"]} | Apellido: {persona["Apellido"]} | ID: {persona["id"]}')
                
        case "A":
            suNombre = input("\nNombre: ")
            suApellido = input("\nApellido: ")
            
            tabla.insert({"Nombre":suNombre,"Apellido":suApellido})
            
