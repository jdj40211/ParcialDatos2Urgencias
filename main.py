import datetime
from Laboratorio import *
from Pacientes import *


# Método para que los pacientes sean atendidos

def tratamiento_medico(lista_pacientes):
    pacienteActual = lista_pacientes.first
    while pacienteActual is not None:
        paciente = pacienteActual.data
        paciente.recibir_atencion_medica()
        pacienteActual = pacienteActual.siguiente


# Salida de los pacientes
def determinar_salida(lista_pacientes):
    pacienteActual = lista_pacientes.first
    while pacienteActual is not None:
        paciente = pacienteActual.data
        paciente.determinar_salida()
        pacienteActual = pacienteActual.siguiente


# Encolar pacientes que necesitan medicamentos
def pacientes_laboratorio(lista_pacientes_1, lista_pacientes_2):
    paciente_medicado = Laboratorio()
    pacienteActual = lista_pacientes_1.first

    while pacienteActual is not None:
        paciente = pacienteActual.data
        if paciente.atencionMedicaRecibida == "Orden de medicamentos":
            paciente_medicado.insert(paciente)
        pacienteActual = pacienteActual.siguiente

    pacienteActual = lista_pacientes_2.first
    while pacienteActual is not None:
        paciente = pacienteActual.data
        if paciente.atencionMedicaRecibida == "Orden de medicamentos":
            paciente_medicado.insert(paciente)
        pacienteActual = pacienteActual.siguiente

    return paciente_medicado


# Método para que los pacientes sean atendidos en el laboratorio por orden de llegada

def atender_laboratorio(lista_pacientes):
    pacientes_atendidos = 0
    contador = 0
    grupo = 0

    pacienteActual = lista_pacientes.first
    while pacienteActual is not None:
        if contador < 10:
            paciente = pacienteActual.data
            paciente.reclamar_medicamentos()
            pacienteActual = pacienteActual.siguiente
            pacientes_atendidos += 1
            contador += 1
        else:
            grupo += 1
            contador = 0

    if pacientes_atendidos % 10 == 0:
        grupo += 1
        return f'Se entregaron los medicamentos a {pacientes_atendidos} pacientes en {grupo} grupos de 10 pacientes\n'
    elif grupo > 0:
        return f'Se entregaron los medicamentos a {pacientes_atendidos} pacientes en {grupo} grupos de 10 pacientes. Se atendieron a {pacientes_atendidos % 10} pacientes en el último grupo\n'
    else:
        return f'Se entregaron los medicamentos a {pacientes_atendidos} pacientes en {grupo} grupos de 10 pacientes. Al haber menos de 10 pacientes, se entregaron {pacientes_atendidos} pacientes en el último grupo\n'

# Contar categorías de atención médica
def contador_atencion_medica(pacientes):
    contador_orden_de_medicamentos = 0
    contador_examenes = 0
    contador_estabilizacion = 0
    contador_reanimacion = 0

    for paciente in pacientes:
        if isinstance(paciente, list):
            # handle list of lists
            atencion_medica = paciente[1]
        else:
            # handle list of Paciente objects
            atencion_medica = paciente.atencionMedicaRecibida

        if atencion_medica == "Orden de medicamentos":
            contador_orden_de_medicamentos += 1
        elif atencion_medica == "Exámenes":
            contador_examenes += 1
        elif atencion_medica == "Estabilización":
            contador_estabilizacion += 1
        elif atencion_medica == "Reanimación":
            contador_reanimacion += 1

    print(f'Cantidad de pacientes que recibieron orden de medicamentos: {contador_orden_de_medicamentos}\n')
    print(f'Cantidad de pacientes que recibieron exámenes: {contador_examenes}\n')
    print(f'Cantidad de pacientes que recibieron estabilización: {contador_estabilizacion}\n')
    print(f'Cantidad de pacientes que recibieron reanimación: {contador_reanimacion}\n')

# Contar categorías de salida
def contador_salidas(pacientes):
    contador_con_medicamentos = 0
    contador_alta = 0
    contador_fallecido = 0
    contador_unidad_cuidados_intensivos = 0
    contador_hospitalizacion = 0
    contador_especialista = 0
    contador_quirofano = 0

    for paciente in pacientes:
        if isinstance(paciente, Paciente):
            estado_salida = paciente.salida

        if pacientes.salida == "El paciente fue dado de alta con orden de medicamentos":
            contador_con_medicamentos += 1
        elif pacientes.salida == "El paciente fue dado de alta":
            contador_alta += 1
        elif pacientes.salida == "El paciente falleció":
            contador_fallecido += 1
        elif pacientes.salida == "El paciente fue trasladado a la UCI":
            contador_unidad_cuidados_intensivos += 1
        elif pacientes.salida == "El paciente fue remitido a hospitalizacion en otro centro de salud":
            contador_hospitalizacion += 1
        elif pacientes.salida == "El paciente será atentido por un especialista":
            contador_especialista += 1
        elif pacientes.salida == "Traslado al quirófano":
            contador_quirofano += 1

    print(f'Cantidad de pacientes que recibieron alta con medicamentos: {contador_con_medicamentos}\n')
    print(f'Cantidad de pacientes que recibieron alta sin medicamentos: {contador_alta}\n')
    print(f'Cantidad de pacientes que fallecieron: {contador_fallecido}\n')
    print(f'Cantidad de pacientes que fueron trasladados a la UCI: {contador_unidad_cuidados_intensivos}\n')
    print(
        f'Cantidad de pacientes que fueron remitidos a hospitalización en otro centro de salud: {contador_hospitalizacion}\n')
    print(f'Cantidad de pacientes que serán atendidos por un especialista: {contador_especialista}\n')
    print(f'Cantidad de pacientes que fueron trasladados al quirófano: {contador_quirofano}\n')


# Mostrar la lista de pacientes
def mostrar_lista_pacientes(lista_pacientes):
    resultado = ""
    pacienteActual = lista_pacientes.first
    while pacienteActual is not None:
        resultado += str(pacienteActual.data) + "\n"
        pacienteActual = pacienteActual.siguiente

    return resultado


# Info del hospital
def info_hospital():
    resultado = ""
    resultado += "Código azul: \n"
    resultado += mostrar_lista_pacientes(pacientes_codigo_azul)
    resultado += "Estabilidad urgente: \n"
    resultado += mostrar_lista_pacientes(pacientes_estabilidad_urgente)
    resultado += "Urgencias normales: \n"
    resultado += mostrar_lista_pacientes(pacientes_urgencias_normales)
    resultado += "Urgencias leves: \n"
    resultado += mostrar_lista_pacientes(pacientes_urgencias_leves)
    return resultado


# Archivo de texto
def archivo_texto(lista_pacientes, limite_pacientes, lista_medicados):
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archivo = f'Informe de pacientes {fecha}.txt'

    try:
        with open(archivo, 'w') as file:
            file.write(f'Informe de pacientes {fecha}\n')
            file.write(f'Cantidad de pacientes: {limite_pacientes}\n')

            for paciente in lista_pacientes:
                file.write(paciente.mostrar_sala_espera())
                file.write('\n')

            file.write(f'Cantidad de pacientes en urgencias leves: {str(pacientes_codigo_azul.size)}\n')
            file.write(f'Cantidad de pacientes en urgencias normales: {str(pacientes_estabilidad_urgente.size)}\n')
            file.write(f'Cantidad de pacientes en estabilidad urgente: {str(pacientes_urgencias_normales.size)}\n')
            file.write(f'Cantidad de pacientes en código azul: {str(pacientes_urgencias_leves.size)}\n')

    except IOError as e:
        print("Error al abrir el archivo")


# Mini informe en consola
def resumen_actividad_diaria(limite_pacientes ,numero_pacientes, pacientes, pacientes_medicados):
    fechaActual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f'Informe de pacientes {fechaActual}\n')
    print(f'Cantidad de pacientes: {numero_pacientes}\n')
    print(f'pacientes ingresados en el día: {str(numero_pacientes)}\n')
    print(f'Pacientes por categoría de gravedad: \n')
    print(f'Cantidad de pacientes en Código azul: {str(pacientes_codigo_azul.size)}\n')
    print(f'Cantidad de pacientes en Estabilidad urgente: {str(pacientes_estabilidad_urgente.size)}\n')
    print(f'Cantidad de pacientes en Urgencias normales: {str(pacientes_urgencias_normales.size)}\n')
    print(f'Cantidad de pacientes en Urgencias leves: {str(pacientes_urgencias_leves.size)}\n')

    print(f'atenciones mpedicas realizadas: \n')
    contador_atencion_medica(pacientes)

    print(f'laboratorio: \n')
    print(f'Cantidad de pacientes que recibieron orden de medicamentos: {str(pacientes_medicados.size)}\n')

    print(f'salidas: \n')
    contador_salidas(pacientes)


if __name__ == '__main__':

    pacientes = []
    pacientes_urgencias_leves = Laboratorio()
    pacientes_urgencias_normales = Laboratorio()
    pacientes_estabilidad_urgente = Laboratorio()
    pacientes_codigo_azul = Laboratorio()

    limite_pacientes = 100

    # Crear pacientes
    for _ in range(limite_pacientes):
        paciente = Paciente()
        pacientes.append(Paciente())

    for paciente in pacientes:
        paciente.triaje()

    # Clasificar pacientes
    for paciente in pacientes:
        if paciente.gravedad == "Urgencias Leves":
            pacientes_urgencias_leves.insert(paciente)
        elif paciente.gravedad == "Urgencias Normales":
            pacientes_urgencias_normales.insert(paciente)
        elif paciente.gravedad == "Estabilidad Urgente":
            pacientes_estabilidad_urgente.insert(paciente)
        elif paciente.gravedad == "Código Azul":
            pacientes_codigo_azul.insert(paciente)

    # Atender pacientes
    tratamiento_medico(pacientes_urgencias_leves)
    tratamiento_medico(pacientes_urgencias_normales)
    tratamiento_medico(pacientes_estabilidad_urgente)
    tratamiento_medico(pacientes_codigo_azul)

    # orden de medicamentos para pacientes (en caso de que aplique)
    pacientes_medicados = pacientes_laboratorio(pacientes_urgencias_leves, pacientes_urgencias_normales)
    atender_laboratorio(pacientes_medicados)

    # Salida de pacientes
    determinar_salida(pacientes_urgencias_leves)
    determinar_salida(pacientes_urgencias_normales)
    determinar_salida(pacientes_estabilidad_urgente)
    determinar_salida(pacientes_codigo_azul)

    # Imprime el informe
    resumen_actividad_diaria(limite_pacientes, len(pacientes), pacientes, pacientes_medicados)
