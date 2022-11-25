# render_template sirve para cargar html
# request sirve para hacer peticiones
from flask import Flask, render_template, request

#funcion principal
app=Flask(__name__)
# Ventana principal
@app.route("/")
def Principal():
    return render_template("Principal.html")

# Ventana de recepcion
@app.route("/Recepcion")
def Recepcion():
    # Por defecto siempre se busca el html en la carpeta "templates" ahi podemos tener varios html
    return render_template("Recepcion.html")

# Envio de datos
@app.route("/enviar_datos", methods=["POST"])
def Envio_Datos():
    Cita={"Folio":"", "Fecha_R":"", "Nombre":"", "Doctor":"", "Especialidad":"", "Fecha_C":""}
    Cita["Nombre"]=request.form.get("Nombre")
    Cita["Fecha_R"]=datetime.date.today().strftime("%d/%m/%y")
    Cita["Especialidad"]=request.form.get("Especialidad")
    Cita["Doctor"]=request.form.get("Doctores")
    return("Cita Agendada")
if(__name__=="__main__"):
    # Se actualiza con cada cambio
    app.run(debug=True)
