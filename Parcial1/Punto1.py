import pandas as pd
import os
#Directorio de trabajo
os.chdir('D:/Python')

funciones = "Funciones: \nAdministrar los recursos del hardware\nActuar como interfaz entre el usuario y la máquina\nRelacionar los dispositivos\nManejar las comunicaciones de redes\nFacilitar el uso del dispositivo"
#Separa por cambios de linea
b = funciones.splitlines()
#Crea o sobreescribe un archivo con txt con las funciones
with open('5FuncOS.txt','w') as fp:
    pass
    fp.write(funciones)

#Crea un data frame con las funciones
df = pd.DataFrame(
    {
        b[0]: b[1:6],
    }
)
#Importa el data frame a un archivo de excel
df.to_excel("FuncionesSO.xlsx", sheet_name="Funciones")