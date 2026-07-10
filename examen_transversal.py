"""
libros = {
    'codigo' : ['titulo', 'autor', 'genero', 'año', 'editorial', 'es_novedad'],
    #Ejemplo:
    'L001' : ['Sombras del sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002' : ['Pytho en ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003' : ['Mar y viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004' : ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005' : ['Mundos Lejanos', 'L. Torres', 'ciencia', 2021, 'Orión', True],
    'L006' : ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
    ...
};
======================================================================================
prestamos = {
    'codigo' : ['pecio_multa', 'copias_dispoibles'],
    #Ejemplo:
    'L001' : [500, 4],
    'L002' : [700, 0],
    'L003' : [300, 10],
    'L004' : [400, 2],
    'L005' : [600, 1],
    'L006' : [350, 6],
    ...
};
"""
def menu():
    print('========== MENÚ PRINCIPAL ==========');
    print('1. Copias por género');
    print('2. Búsqueda de libros por rango de multa');
    print('3. Actualizar multa de libro');
    print('4. Agregar libro');
    print('5. Eliminar libro');
    print('6. Salir');
    print('======================================');

def leer_opcion():
    try:
        opc = int(input('Ingrese una opción del menú: '));
        if opc >= 1 and opc <= 6:
            return opc;
        else:
            raise ValueError
    except ValueError:
        print('El numero debe ser entero entre 1-6.');
        return;

def copias_genero(genero):
    pass;

def busqueda_multa(multa_min, multa_max):
    pass;

def buscar_codigo(codigo):
    pass;

def actualizar_multa(codigo, nueva_multa):
    pass;

# Validaciones
def validar_codigo(codigo):
    if codigo in len(libros):
        print('El codigo ya existe');
    else:
        return codigo.strip() != '';

def validar_titulo(titulo):
    return titulo.strip() != '';

def validar_autor(autor):
    return autor.strip() != '';

def validar_genero(genero):
    return genero.strip() != '';

def validar_año(año):
    try:
        if año > 0:
            return True;
        elif año <= 0:
            return False;
        else:
            raise ValueError;
    except ValueError:
        print('El año debe ser un número entero mayor que cero!');
        return;

def validar_editorial(editorial):
    editorial = input('Ingrese editorial: ');
    pass;

def validar_esNovedad(es_novedad):
    if es_novedad == 's':
        return True;
    else:
        return False;

def validar_precioMulta(precio_multa):
    try:
        if precio_multa > 0:
            return True;
        elif precio_multa <= 0:
            return False;
        else:
            raise ValueError;
    except ValueError:
        print('El valor debe ser un entero mayor que cero!');
        return;

def validar_copiasDisponibles(copias_disponibles):
    try:
        if copias_disponibles >= 0:
            return True;
        elif copias_disponibles < 0:
            return False;
        else:
            raise ValueError;
    except ValueError:
        print('El valor debe ser un entero mayor o igual a cero!');
        return;

def agregar_libro(codigo, titulo, autor, genero, año, editorial, es_novedad, precio_multa, copias_disponibles):
    pass;
    #.append()

def eliminar_libro(codigo):
    pass;
    #.pop()

# Sistema Principal
libros = {};
prestamos = {};
while True:
    menu();
    opc = leer_opcion();

    if opc == 1:
        pass;

    elif opc == 2:
        pass;

    elif opc == 3:
        pass;

    elif opc == 4:
        codigo = input('Ingrese cóigo del libro: ');
        validar_codigo(codigo);
        titulo = input('Ingrese título: ');
        validar_titulo(titulo);
        autor = input('Ingrese autor: ');
        validar_autor(autor);
        genero = input('Ingresegénero: ');
        validar_genero(genero);
        año = int(input('Ingrese año de publicación: '));
        validar_año(año);
        editorial = input('Ingrese precio de multa: ');
        validar_editorial(editorial);
        es_novedad = input('¿Es novedad? (s/n): ');
        validar_esNovedad(es_novedad);
        precio_multa = float(input('Ingrese precio de multa: '));
        validar_precioMulta(precio_multa);
        copias_disponibles = int(input('Ingrese copias disponibles: '));
        validar_copiasDisponibles(copias_disponibles);
        pass;

    elif opc == 5:
        pass;

    elif opc == 6:
        print('Programa finalizado.');
        break;
