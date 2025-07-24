from flask import Blueprint, request, jsonify

cliente = Blueprint('cliente', __name__)

@cliente.route('/cliente', methods = ['POST'])
def llamarservicio():
    ci = request.json.get('user')

    codRes, menRes, accion, nombre, apellido = inicializarVariable(ci)

    salida = {
        'codRes' : codRes,
        'menRes' : menRes,
        'accion' : accion,
        'ci' : ci,
        'accion' : accion,
        'nombre' : nombre,
        'apellido' : apellido
 
    }
    return jsonify(salida)

def inicializarVariable(ci):
    nombre = "Thiago"
    apellido = "Meza"
    codRes = "SIN_ERROR"
    menRes = "OK"
    ciLocal = "5844351"

    try:
        print("Verificar login")
        if ci == ciLocal:
            print("ci ok")
            accion = "succes"
        else:
            print("CI no correcto")
            accion = "cliente no est en el sistema"
            codRes = "Error"
            menRes = "ci incorrecta"
    except Exception as e:
        print("Error", str(e))
        codRes = 'ERROR'
        menRes = 'Msg ' + str(e)
        accion = "Error interno"
    return codRes, menRes, accion, nombre, apellido