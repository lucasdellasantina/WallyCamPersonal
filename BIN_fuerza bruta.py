import itertools
import shutil

palabras1 = ["","recovery", "demo","P02","Personal","personalcam","E4AAECA69937","TELEAR_CamPan","CamPan","Cam","Pan","Pan3", "PersonalCam"]
palabras2 = ["personal", "Personal", "Pam", "Cam", "HL_PAN3", "PersonalCam", "P02A0000", "F00A0000","P02","Personal","personalcam","E4AAECA69937","TELEAR_CamPan","CamPan","Cam","Pan","Pan3", "PersonalCam"]

def generar_combinaciones():
    combinaciones_totales = []
    for palabra1 in palabras1:
        for palabra2 in palabras2:
            combinacion = f"{palabra1}_{palabra2}"
            combinaciones_totales.append(combinacion)
    return combinaciones_totales

def generar_copias_archivo(nombre_archivo, combinaciones_totales):
    for combinacion in combinaciones_totales:
        nombre_nuevo = f"{combinacion}.bin"
        shutil.copy(nombre_archivo, nombre_nuevo)
        print(f"Copia de '{nombre_archivo}' generada como '{nombre_nuevo}'.")


# Ejemplo de uso
nombre_archivo = "E:/CAMARAS/reco.bin"
todas_combinaciones = generar_combinaciones()
generar_copias_archivo(nombre_archivo, todas_combinaciones)

