from flask import Flask, jsonify, Response

app = Flask(__name__)

# Простой класс для сущностей
class Entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

# Создаем несколько сущностей
entities_model1 = [
    Entity(1, "Model Entity One"),
    Entity(2, "Model Entity Two"),
]

# Контроллер для получения всех сущностей
@app.route('/', methods=['GET'])
def get_all_entities():
    response = [{'id': entity.id, 'name': entity.name} for entity in entities_model1]
    return jsonify(response), 200

# Контроллер для проверки сервиса HealthCheck
@app.route('/health', methods=['GET'])
def healthcheck():
    return "Z-Z-Z-Z-Z", 200

if __name__ == '__main__':
    app.run(debug=True)
