import pandas as pd
import os

os.chdir('D:/Estudio/Python')

funciones = "Funciones: \nAdministrar los recursos del hardware\nActuar como interfaz entre el usuario y la máquina\nRelacionar los dispositivos\nManejar las comunicaciones de redes\nFacilitar el uso del dispositivo"
with open('5FuncOS.txt','w') as fp:
    pass
    fp.write(funciones)

df = pd.DataFrame(
    {
        "Funciones": ["Administrar los recursos del hardware", "Actuar como interfaz entre el usuario y la máquina", "Relacionar los dispositivos", "Manejar las comunicaciones de redes", "Facilitar el uso del dispositivo"],
    }
)

df
