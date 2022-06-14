from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Conectar a base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/dbpython-api"
# Desactivar mensajes de cambio
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# instanciamos modulos
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Modelo de base de datos
class Categoria(db.Model):
    cat_id = db.Column(db.Integer,primary_key=True)
    cat_nom = db.Column(db.String(100))
    cat_desc = db.Column(db.String(100))

    def __init__(self,cat_nom,cat_desc):
        self.cat_nom = cat_nom
        self.cat_desc = cat_desc

# creamos todas las bases de datos
db.create_all()

# Esquema categoria
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ('cat_id','cat_nom','cat_desc')



#Una sola respuesta
categoria_schema = CategoriaSchema()


# Muchas respuestas
categorias_schema = CategoriaSchema(many=True)


# get
@app.route('/categoria',methods=['GET'])
def get_categorias():
    all_categorias = Categoria.query.all()
    result = categoria_schema.dump(all_categorias)
    return jsonify(result)

# Get por id
@app.route('/categoria/<id>',methods=['GET'])
def get_categoria_x_id(id):
    una_categoria = Categoria.query.get(id)
    return categoria_schema.jsonify(una_categoria)


# Post
@app.route('/categoria',methods=['POST'])
def insertar_categoria():
    cat_nom = request.json['cat_nom']
    cat_desc = request.json['cat_desc']
    
    nuevo_registro = Categoria(cat_nom,cat_desc)
    db.session.add(nuevo_registro)
    db.session.commit()

    return categoria_schema.jsonify(nuevo_registro)


# Put
@app.route('/categoria/<id>',methods=["PUT"])
def actualizar(id):

    idcat = Categoria.query.get(id)
    
    data = request.get_json(force=True)
    cat_nom = data['cat_nom']
    cat_desc = data['cat_desc']

    idcat.cat_nom = cat_nom
    idcat.cat_desc = cat_desc

    db.session.commit()

    return categoria_schema.jsonify(idcat)


# delete
@app.route('/categoria/<id>',methods=["DELETE"])
def deleted(id):
    registro = Categoria.query.get(id)
    db.session.delete(registro)
    db.session.commit()
    return categoria_schema.jsonify(registro)

# mensaje bienvenida
@app.route('/', methods=["GET"])
def index():
    return jsonify({'Mensaje':"Bienvenido al tutorial API-REST python"})

# Ejecutamos la aplicacion
if __name__ == "__main__":
    app.run(debug=True,host="localhost")