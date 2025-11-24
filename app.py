from flask import Flask, jsonify, request

app = Flask(__name__)


tareas = [{"id": 1, "tarea": "Llamando a AWService", "hecho": False}]

@app.route('/')
def home():
    return "¡Hola! La API está funcionando en AWS."


@app.route('/tareas', methods=['GET'])
def get_tareas():
    return jsonify(tareas)


@app.route('/tareas', methods=['POST'])
def add_tarea():
    nueva = {"id": len(tareas)+1, "tarea": request.json['tarea'], "hecho": False}
    tareas.append(nueva)
    return jsonify(nueva), 201

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=5000)