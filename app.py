from src import aplication_init
from src.routes.file_analisis import blueprint_usuario

app=aplication_init()

for blueprint in [blueprint_usuario]: 
    app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port = 8080,debug=True)