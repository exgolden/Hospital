from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/')
def ehlo():
    return 'Hola mundo'


@app.route('/hospital')
def hospital():
    return render_template('index.html')

@app.route('/enviar_datos', methods=['POST'])
def datos():
    print(request.form.get('Nombre'))
    print("Sistema de gestion de citas")
    Cita={"Folio":"", "Fecha_R":"", "Nombre":"", "Doctor":"", "Especialidad":"", "Fecha_C":""}
    Cita["Folio"]=(Base["Folio"].iat[-1])+1
    Cita["Fecha_R"]=datetime.date.today().strftime("%d/%m/%y")
    Cita["Nombre"]=request.form.get('Nombre')
    Cita["Doctor"]=request.form.get('Doctores')
    Cita["Especialidad"]=request.form.get('Especialidad')
    # Hora
    Cita["Fecha_C"]=str(input("Ingrese fecha y hora de consulta (dd/mm/aa hh:00): "))
    # Solo se puden ingrear horas cerradas
    if(Cita["Fecha_C"][-2: ]!="00"):
        print("Las consultas son de 1 hora, ingrese su consulta en una hora cerrada")
        Cita["Fecha_C"]=str(input("Ingrese fecha y hora de consulta (dd/mm/aa hh:00): "))
    # Checa la base para ver si hay citas disponibles ese dia
    # En este caso se tendria que revisar la disponibilidad por cada entrada, lo cual no tiene sentido, lo idela seria hacer un
    # solo query para mostrar los horarios libres del doctor en forma de calendario, esto solo es un ejemplo
    Check=Base.loc[(Base["Doctor"]==Cita["Doctor"]) & (Base["Fecha_C"]==Cita["Fecha_C"])].empty
    if(Check==False):
        print("Horario ocupado, eliga otro horario o fecha")
        Cita["Fecha_C"]=str(input("Ingrese fecha y hora de consulta (dd/mm/aa hh:00): "))
    Base=pd.concat([Base,pd.DataFrame([Cita]) ])
    Base.to_csv("Base.csv", index=False)
    print("Su cita se ha agendado correctacmente")
    return 'datos enviados con éxito'


if __name__ == '__main__':
    app.run(debug=True)