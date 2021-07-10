from flask_sqlalchemy import SQLAlchemy
from __Avaliação07.aplicattion import app

db = SQLAlchemy(app)


class Cliente(db.Model):
    __tablename__ = "Cliente"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cnpjcpf = db.Column(db.Integer, unique=True)
    codigo = db.Column(db.Integer)
    notas = db.relationship('NotaFiscal', backref='cliente_da_nota')

    id_clientes = 0

    def __init__(self, nome, cnpfcpf, codigo):
        self.id = Cliente.id_clientes
        Cliente.id_clientes += 1
        self.nome = nome
        self.cnpjcpf = cnpfcpf
        self.codigo = codigo

    def __repr__(self):
        return '\nId: %r, Nome %r, Cnpjcpf: %r, Código: %r\n' % (self.id, self.nome, self.cnpjcpf, self.codigo)

    def dict(self):
        return {'ID': self.id, 'Nome': self.nome, 'Cnpj/CPF': self.cnpjcpf, 'Código': self.codigo}


class Produto(db.Model):
    __tablename__ = "Produto"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    descricao = db.Column(db.String(80))
    valor_unitario = db.Column(db.Float)
    itens = db.relationship('ItemNotaFiscal', backref='produto_do_item')

    id_produtos = 0

    def __init__(self, codigo, descricao, valor_unitario):
        self.id = Produto.id_produtos
        Produto.id_produtos += 1
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario

    def __repr__(self):
        return '\nId: %r, Codigo %r, Descrição: %r, Valor Unitário: %r\n' % (self.id,
                                                                             self.codigo,
                                                                             self.descricao,
                                                                             self.valor_unitario)

    def dict(self):
        return {'ID': self.id, 'Codigo': self.codigo, 'Descrição': self.descricao, "Valor Unit.": self.valor_unitario}


class ItemNotaFiscal(db.Model):
    __tablename__ = "ItemNotaFiscal"
    id = db.Column(db.Integer, primary_key=True)
    sequencial = db.Column(db.Integer)
    quantidade = db.Column(db.Integer)
    produto_id = db.Column(db.Integer, db.ForeignKey("Produto.id"))
    nota_id = db.Column(db.Integer, db.ForeignKey("NotaFiscal.id"))

    produto = db.relationship("Produto", foreign_keys=produto_id)
    nota = db.relationship("NotaFiscal", foreign_keys=nota_id)

    id_itens = 0

    def __init__(self, quantidade, produto_id, nota_id):
        self.id = ItemNotaFiscal.id_itens
        ItemNotaFiscal.id_itens += 1
        self.quantidade = quantidade
        self.produto_id = produto_id
        self.nota_id = nota_id

        # adendos
        self.sequencial = len(ItemNotaFiscal.query.filter_by(nota_id=nota_id).all())
        self.produto = self.get_produto()
        self.descricao = self.produto.descricao
        self.valor_item = self.quantidade * self.produto.valor_unitario

    def __repr__(self):
        return "\nID: %r, Quantidade: %r, Descrição: %r, Valor: %r\n" % (self.id,
                                                                         self.quantidade,
                                                                         self.descricao,
                                                                         self.valor_item)

    def dict(self):
        return {'ID': self.id, 'Sequencial': self.sequencial, 'Valor Unitário': self.produto.valor_unitario,
                'Quantidade': self.quantidade, 'Descrição': self.descricao, 'Valor': self.valor_item}

    def get_produto(self):
        return Produto.query.filter_by(id=int(self.produto_id)).first()

    def get_nota(self):
        return NotaFiscal.query.filter_by(id=int(self.nota_id)).first()


class NotaFiscal(db.Model):
    __tablename__ = "NotaFiscal"
    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.Integer)
    cliente_id = db.Column(db.Integer, db.ForeignKey("Cliente.id"))
    data = db.Column(db.String(10))
    itens = db.relationship('ItemNotaFiscal', backref='nota_do_item', overlaps="nota")
    cliente = db.relationship('Cliente', foreign_keys=cliente_id)

    id_notas = 0

    def __init__(self, codigo, cliente_id, data):
        self.id = NotaFiscal.idnotas
        NotaFiscal.idnotas += 1
        self.codigo = codigo
        self.cliente_id = cliente_id
        self.data = data

    def __repr__(self):
        return "\nID: %r, Código: %r, Cliente: %r, Data: %r QTD Itens: %r \n" % (self.id,
                                                                                 self.codigo,
                                                                                 self.cliente.nome,
                                                                                 self.data,
                                                                                 len(self.itens))

    def dict(self):
        dicionario = {'ID': self.id, 'Código': self.codigo, 'Cliente': self.cliente.nome,
                'Data': self.data, 'QTD Itens': len(self.itens)}
        dicionario.update(self.get_itens())

    def get_cliente(self):
        return Cliente.query.filter_by(id=int(self.cliente_id)).first().dict()

    def get_itens(self):
        return [item.dict() for item in ItemNotaFiscal.query.filter_by(nota_id=self.id).all()]

    def calcular_nota(self):
        valor = None
        itens = self.get_itens()
        if itens:
            for item in itens:
                valor += int(item['Valor'])
            return valor
        else:
            return "nota vazia"

    def imprimir_nota(self):
        cliente = self.get_cliente()
        dict_nf = {"Data": self.data,
                   "Cliente": cliente['ID'],
                   "Nome": cliente['Nome'],
                   "CPF/CNPJ": cliente['Cnpj/CPF']}

        for item in self.get_itens():
            dict_nf.update(item)

        dict_nf["Valor Final"] = self.calcular_nota()

        return dict_nf


db.create_all()