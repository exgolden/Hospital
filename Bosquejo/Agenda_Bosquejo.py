import pandas as pd

Base=pd.read_csv("/Users/isaibb/Desktop/Progra/Python/Hospital/Base.csv")
Usuarios={"Dr. Kevin":"Simp", "Dr. Cris":"ESIT"}
User=str(input("ingrese su usuario: "))
Password=str(input("ingrese su contraseña: "))
if(User=="Dr. Kevin" and Password==Usuarios["Dr. Kevin"]):
    print(Base.loc[Base["Doctor"]==User])
elif(User=="Dr. Cris" and Password==Usuarios["Dr. Cris"]):
    print(Base.loc[Base["Doctor"]==User])
else:
    print("Usario o contraseña incorrecto")