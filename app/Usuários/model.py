from ..extensions import db

class Usuarios(db.Model):
    __tablename__ = 'usuario'

    id_usuario = db.Column(db.Integer, primary_key=True)
    nome_de_usuario = db.Column(db.String(15), nullable=False, unique=True)
    idade = db.Column(db.Integer, nullable=False)
    data_de_inscricao = db.Column(db.Date(), nullable=False)
    n_de_posts = db.Column(db.Integer,default=0)

    post = db.relationship('Posts', backref='postagem')

    def json(self):
        return {
            "id:": self.id_usuario
            "nome": self.nome_de_usuario
            "idade": self.idade
            "data": self.data_de_inscricao
            "n_posts": self.n_de_posts
        }