from ..extensions import db

class Posts(db.Model):
    __tablename__ = 'posts'

    id_post = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(200), nullable=False)
    n_curtidas = db.Column(db.Integer, default=0)
    n_comentarios = db.Column(db.Integer, default=0)
    n_compartilhamentos = db.Column(db.Integer, default=0)
    data_de_postagem = db.Column(db.Date(), nullable=False)

    id_usuario = db.Column(db.String(15), foreign_key('usuario.id_usuario'))

