
from flask import Flask, jsonify, request
from flask_cors import CORS
##import Red
##from predict import predict

app = Flask(__name__)
CORS(app)

from turnos import obternerTurno

@app.route('/')
def hello_world():
    return 'Hello, World'

@app.route('/rest/v1.0/ping')
def ping():
    return jsonify({"message":"pong!"})


##predict(prueba)


@app.route('/rest/v1.0/turnosNN')
def getTurnos():
    prueba = obternerTurno()
    turnoFound=[pruebas for pruebas in prueba]
    if(len(turnoFound)>0):
        return jsonify({"Body":prueba,"message":"Lista de turnos","code":200})
        
    return jsonify({"message":"lista vacia","code":200,"Body":prueba})



if __name__ == '__main__':
    app.run(debug=True,port=2500) 


#@app.route('/rest/v1.0/turnosNN/<string:idusuario>')
#def getTurno(idusuario):
#    usuarioFound=[turno for turno in prueba if turno['idusuario']==idusuario]
#    if(len(usuarioFound)>0):
#        return jsonify({"turno":usuarioFound})
#    return jsonify({"message":"Usuario no encontrado"})

#@app.route('/rest/v1.0/turnosNN',methods=['POST'])
#def addTurno():
#    new_turno ={
#        "idusuario": request.json['idusuario'],
#        "fecharegistro": request.json['fecharegistro'],
#        "estado": request.json['estado']
#    }
#    prueba.append(new_turno)
#    
#    return jsonify({"mesaje":"Agregado exitoso","turnos":prueba})
#
#@app.route('/rest/v1.0/turnosNN/<string:idusuario>', methods=['PUT'])
#def editTurno(idusuario):
#    usuarioFound = [turno for turno in prueba if turno['idusuario']==idusuario]
#    if (len(usuarioFound)>0):
#        usuarioFound[0]['idusuario'] = request.json['idusuario']
#        usuarioFound[0]['fecharegistro'] = request.json['fecharegistro']
#        usuarioFound[0]['estado'] = request.json['estado']
#        return jsonify({
#            "message":"actualizado con exito",
#            "turno": usuarioFound[0]
#        })
#    return jsonify({"mesage":"Usuario no encontrado"})
#
#@app.route('/rest/v1.0/turnosNN/<string:idusuario>', methods=['DELETE'])
#def deleteTurno(idusuario):
#    usuarioFound = [turno for turno in prueba if turno['idusuario']==idusuario]
#    if (len(usuarioFound)>0):
#        prueba.remove(usuarioFound[0])
#        return jsonify({
#            "message":"eliminado exitoso",
#            "turno": prueba
#        })
#    return jsonify({"mesage":"Usuario no encontrado"})


