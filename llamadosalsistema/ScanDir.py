a = 'C:/Users'
with os.scandir(a) as it: #scandir(path) regresa un iterador 
    for entry in it: 
        if entry.is_dir() and entry.name.startswith('D'):			#el método is_dir() regresa un valor booleano para determinar si entry es un directorio, mientras el método name.startswith('D') revisa que el directorio empiece con D 
            print(entry.name)				#Muestra los directorios que empiecen con D
