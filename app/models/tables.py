from app import db, UserMixin

class Users(UserMixin ,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return "<User {} {}".format(self.name, self.password)

class Chamados(db.Model):
    __tablename__ = "chamados"

    id = db.Column(db.Integer, primary_key=True)
    chamado = db.Column(db.String, unique=True)
    data = db.Column(db.String)
    cidade = db.Column(db.String)
    pedido = db.Column(db.String)
    pedido_of = db.Column(db.String)
    rota = db.Column(db.String)
    obs = db.Column(db.String)

    def __init__(self, chamado, data, cidade, pedido, pedido_of, rota, obs):
        self.chamado = chamado
        self.data = data
        self.cidade = cidade
        self.pedido = pedido
        self.pedido_of = pedido_of
        self.rota = rota
        self.obs = obs

    def __repr__():
        return "<Chamado {} Dia {} Rota {} da cidade {} pedido de peça {}>".format(self.chamado, self.data, self.rota,self.cidade,self.pedido)
