""" Descripción: Imagina que estás creando un programa para procesar datos de estudiantes, 
y necesitas una función que realice diferentes operaciones utilizando otras cinco funciones.
 """

def procesar_datos_estudiantes(estudiantes):
    """ Esta función "procesar_datos_estudiantes" utiliza cinco funciones internas para calcular el promedio de notas,
        contar estudiantes aprobados, contar estudiantes reprobados, encontrar la nota máxima y encontrar la nota mínima. 
        Luego, le da formato a la informacion obtenida, los guarda en un archivo y por ultimo muestra la informacion leyendola
        desde el arvhivo e imprimiendola por consola.
    """
    def calcular_promedio(estudiantes):
        """ Cálculo del promedio de notas """
        total_calificaciones = len(estudiantes)
        suma_calificaciones = 0
        
        for estudiante in estudiantes:
            suma_calificaciones += estudiante['nota']
        
        #caluculo del promedio
        promedio= round((suma_calificaciones/total_calificaciones),2)
        
        return [total_calificaciones, promedio] #lista con: total de calificaciones y promedio de las mismas

    def calcular_aprobados(estudiantes):
        """ Cálculo de estudiantes aprobados """
        total_estudiantes = len(estudiantes)
        estudiantes_aprobados = 0
        #iteracion para averiguar la cantidad de estudiantes aprobados
        for estudiante in estudiantes:
            if estudiante['nota']>=6:
                estudiantes_aprobados+=1
        
        #calculo de porcentaje
        porcentaje_aprobados=round((estudiantes_aprobados*100/total_estudiantes),2)

        return [total_estudiantes, estudiantes_aprobados, porcentaje_aprobados] # lista con: total de estudiantes, aprobados y porcentaje

    def calcular_reprobados(estudiantes):
        """ Cálculo de estudiantes reprobados """
        total_estudiantes = len(estudiantes)
        estudiantes_reprobados = 0
        #iteracion para averiguar la cantidad de estudiantes aprobados
        for estudiante in estudiantes:
            if estudiante['nota']<6:
                estudiantes_reprobados+=1
        
        #calculo de porcentaje
        porcentaje_reprobados=round((estudiantes_reprobados*100/total_estudiantes),2)

        return [total_estudiantes, estudiantes_reprobados, porcentaje_reprobados]#lista con: total de estudiantes, reprobados y porcentaje

    def calcular_nota_maxima(estudiantes):
        """ Cálculo de la nota máxima """
        lista_calificaciones = []
        #obtener todas las calificaciones
        for estudiante in estudiantes:
            lista_calificaciones.append(estudiante['nota'])
        return [len(lista_calificaciones), max(lista_calificaciones), lista_calificaciones.count(max(lista_calificaciones))] #lista con: total de notas controladas, la nota maxima y la cantidad de estudiantes que obtuvieron esa calificacion

    def calcular_nota_minima(estudiantes):
        """ Cálculo de la nota mínima """
        lista_calificaciones = []
        #obtener todas las calificaciones
        for estudiante in estudiantes:
            lista_calificaciones.append(estudiante['nota'])
        return [len(lista_calificaciones), min(lista_calificaciones), lista_calificaciones.count(min(lista_calificaciones))] #lista con: total de notas controladas, la nota minima y la cantidad de estudiantes que obtuvieron esa calificacion

    # Llamadas a las funciones internas
    promedio = calcular_promedio(estudiantes)
    aprobados = calcular_aprobados(estudiantes)
    reprobados = calcular_reprobados(estudiantes)
    nota_maxima = calcular_nota_maxima(estudiantes)
    nota_minima = calcular_nota_minima(estudiantes)

    # formateo de informacion
    mensaje_promedio = f'El promedio de un total de {promedio[0]} calificaciones fue de {promedio[1]}'
    mensaje_aprobados = f'De un total de {aprobados[0]} estudiantes aprobaron {aprobados[1]}, lo que nos da un promedio de {aprobados[2]}% de aprobacion'
    mensaje_desaprobados = f'De un total de {reprobados[0]} estudiantes reprobaron {reprobados[1]}, lo que nos da un promedio de {reprobados[2]}% de reprobados'
    mensaje_nota_maxima = f'De un total de {nota_maxima[0]} calificaciones revisadas la mas alta fue de {nota_maxima[1]} y la obtuvieron {nota_maxima[2]} estudiantes'
    mensaje_nota_minima = f'De un total de {nota_minima[0]} calificaciones revisadas la mas baja fue de {nota_minima[1]} y la obtuvieron {nota_minima[2]} estudiantes'
    mensaje_completo = f'Analisis de datos de estudiantes:\n{mensaje_promedio}\n{mensaje_aprobados}\n{mensaje_desaprobados}\n{mensaje_nota_maxima}\n{mensaje_nota_minima}'
    
    #escribir archivo para persistencia de datos
    f = open ('analisis_de_estudiantes','w')
    f.write(mensaje_completo)
    f.close()
    
    #leer el archivo e imprimir los datos por consola
    file= open ('analisis_de_estudiantes','r')
    mensaje=file.read()
    print(mensaje)


#datos de estudiantes
estudiantes_bd = [
    {'nombre':'Jose', 'apellido':'Ramirez', 'edad':34, 'nota':10, 'id':1},
    {'nombre':'Maria', 'apellido':'Gutierrez', 'edad':42, 'nota':8, 'id':2},
    {'nombre':'Raul', 'apellido':'Lopez', 'edad':25, 'nota':9, 'id':3},
    {'nombre':'Valentina', 'apellido':'Vega', 'edad':21, 'nota':4, 'id':4},
    {'nombre':'Valeria', 'apellido':'Ortiz', 'edad':30, 'nota':7, 'id':5},
    {'nombre':'Yoel', 'apellido':'Perez', 'edad':26, 'nota':10, 'id':6},
    {'nombre':'Franco', 'apellido':'Fernandez', 'edad':28, 'nota':6, 'id':7},
    {'nombre':'Josua', 'apellido':'Riquelme', 'edad':27, 'nota':5, 'id':8},
    {'nombre':'Marissa', 'apellido':'Salon', 'edad':34, 'nota':9, 'id':9},
    {'nombre':'Cristina', 'apellido':'Gimenez', 'edad':22, 'nota':9, 'id':10},
    {'nombre':'Roberto', 'apellido':'Juarez', 'edad':21, 'nota':4, 'id':11},
    {'nombre':'Jacinto', 'apellido':'Piedrabuena', 'edad':25, 'nota':8, 'id':12},
    {'nombre':'Federico', 'apellido':'Cerezo', 'edad':26, 'nota':10, 'id':13},
    {'nombre':'Pablo', 'apellido':'Chavez', 'edad':24, 'nota':8, 'id':14}
    ]

procesar_datos_estudiantes(estudiantes_bd)
