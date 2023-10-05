import random
import datetime
from Laboratorio import *

class Paciente:

    def __init__(self):

        # Parámetros de simulación para crear pacientes
        lista_nombres = ["Juan", "María", "Pedro", "Ana", "José", "Luis", "Carmen", "Francisco", "Isabel"]
        lista_apellidos = ["Pérez", "López", "García", "Martínez", "Rodríguez", "Sánchez", "González", "Fernández", "Gómez"]

        # Atributos básicos
        self.id = random.randint( 300356, 1034567)
        self.nombres = f'{random.choice(lista_nombres) + " " + random.choice(lista_apellidos)}'
        self.edad = random.randint(18, 80)
        self.sexo = random.choice(["Masculino", "Femenino"])
        self.gravedad = None
        self.sintomas = None
        self.atencionMedicaRecibida = None
        self.salida = None
        self.medicamentos = "Salió sin orden de medicamentos"

    # Asignación de triaje
    def triaje(self):

        #Síntomas según gravedad
        lista_sintomas_leves = ["Dolor de cabeza", "Fiebre", "Gripe", "Alergia"]
        lista_sintomas_normales = ["Herida Abieta", "Sangrado", "Dolor de estómago", "Dolor de garganta"]
        lista_sintomas_urgentes = ["Fractura", "Derrame cerebral", "Quemadura grave" , "Envenenamiento"]
        lista_sintomas_codigo_azul = ["Infarto", "Paro cardíaco", "Pérdida de conocimiento", "Inconsciente"]

        #Asignación de gravedad
        gravedad = random.choice(["Leve", "Normal", "Urgente", "Código Azul"])

        if gravedad == "Leve":
                sintomas = random.choice(lista_sintomas_leves)
                self.gravedad = "Urgencias Leves"

        elif gravedad == "Normal":
                sintomas = random.choice(lista_sintomas_normales)
                self.gravedad = "Urgencias Normales"

        elif gravedad == "Urgente":
                sintomas = random.choice(lista_sintomas_urgentes)
                self.gravedad = "Estabilidad Urgente"

        elif gravedad == "Código Azul":
                sintomas = random.choice(lista_sintomas_codigo_azul)
                self.gravedad = "Código Azul"

    def recibir_atencion_medica(self):

        atenciones_leves = ["Orden de medicamentos", "Inyección", "Alta sin medicamentos"]
        atenciones_normales = ["Exámenes", "Orden de medicamentos", "Alta sin medicamentos"]
        atenciones_urgentes = ["Estabilización", "Hospitalización"]
        atenciones_codigo_azul = ["Reanimación", "Hospitalización", "Monitoreo"]

        # Asignación de atención médica
        if self.gravedad == "Urgencias Leves":
            self.atencionMedicaRecibida = random.choice(atenciones_leves)
        elif self.gravedad == "Urgencias Normales":
            self.atencionMedicaRecibida = random.choice(atenciones_normales)
        elif self.gravedad == "Estabilidad Urgente":
            self.atencionMedicaRecibida = random.choice(atenciones_urgentes)
        elif self.gravedad == "Código Azul":
            self.atencionMedicaRecibida = random.choice(atenciones_codigo_azul)

    def reclamar_medicamentos(self):
        lista_medicamentos = ["Ibuprofeno", "Acetaminofen", "Paracetamol", "Amoxicilina", "Omeprazol", "Loratadina", "Dipirona", "Diclofenaco", "Aspirina", "Dexametasona"]

        if self.atencionMedicaRecibida == "Orden de medicamentos":
            self.medicamentos = random.choice(lista_medicamentos)


    def determinar_salida(self):

        #Opciones de salida según gravedad de cada paciente
        salidas_leves = ["El paciente fue dado de alta"]
        salidas_normales = ["El paciente fue dado de alta", "El paciente fue remitido a hospitalizacion en otro centro de salud"]
        salidas_urgentes = ["El paciente será atentido por un especialista", "Traslado al quirófano", "El paciente fue remitido a hospitalizacion en otro centro de salud"]
        salidas_codigo_azul = ["El paciente fue trasladado a la UCI", "El paciente falleció"]

        # Asignación de salida
        if self.gravedad == "Urgencias Leves":
            if self.atencionMedicaRecibida != "Orden de medicamentos":
                self.salida = random.choice(salidas_leves)
            else:
                self.salida = "El paciente fue dado de alta con orden de medicamentos"
        elif self.gravedad == "Urgencias Normales":
            if self.atencionMedicaRecibida != "Orden de medicamentos":
                self.salida = random.choice(salidas_normales)
            else:
                self.salida = "El paciente fue dado de alta con orden de medicamentos"

        elif self.gravedad == "Estabilidad Urgente":
            self.salida = random.choice(salidas_urgentes)
        elif self.gravedad == "Código Azul":
            self.salida = random.choice(salidas_codigo_azul)

    def mostrar_ingreso(self):
        return f'Nombre: {self.nombres} \n Identificación: {self.id}\n Edad: {self.edad}\n'

    def mostrar_sala_espera(self):
        return f'Nombre: {self.nombres} \n Identificación: {self.id}\n Edad: {self.edad}\n Gravedad: {self.gravedad}\n Síntomas: {self.sintomas}\n'

    def mostrar_paciente_procesado(self):
        return f'Nombre: {self.nombres} \n Identificación: {self.id}\n Edad: {self.edad}\n Gravedad: {self.gravedad}\n Síntomas: {self.sintomas}\n Atención médica recibida: {self.atencionMedicaRecibida}\n Salida: {self.salida}\n Medicamentos: {self.medicamentos}\n'

    def __str__ (self):
        return f'Nombre: {self.nombres} \n Identificación: {self.id}\n Edad: {self.edad}\n Gravedad: {self.gravedad}\n Síntomas: {self.sintomas}\n Atención médica recibida: {self.atencionMedicaRecibida}\n Salida: {self.salida}\n Medicamentos: {self.medicamentos}\n'
