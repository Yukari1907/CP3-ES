class Filme:
    def __init__(self, titulo, duracao, genero):
        self.titulo = titulo
        self.duracao = duracao
        self.genero = genero

    def __str__(self):
        return f"{self.titulo} ({self.genero}) - {self.duracao} min"


class Avaliacao:
    def __init__(self, nota, comentario):
        self.nota = nota
        self.comentario = comentario
        self.filme = None

    def associar_filme(self, filme):
        self.filme = filme


class Usuario:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.plano = plano
        self.avaliacoes = []

    def avaliar(self, filme, avaliacao):
        avaliacao.associar_filme(filme)
        self.avaliacoes.append(avaliacao)

    def ver_avaliacoes(self):
        print(f"\nAvaliações de {self.nome}:")
        for av in self.avaliacoes:
            print(f"- {av.filme.titulo}: Nota {av.nota} | {av.comentario}")


class Catalogo:
    def __init__(self, titulo, qtdFilmes):
        self.titulo = titulo
        self.qtdFilmes = qtdFilmes
        self.filmes = []

    def add_filme(self, filme):
        self.filmes.append(filme)
        self.qtdFilmes += 1

    def listar_filmes(self):
        print(f"\nCatálogo: {self.titulo}")
        for filme in self.filmes:
            print(f"- {filme}")


class Plataforma:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
        self.catalogos = []

    def add_catalogo(self, catalogo):
        self.catalogos.append(catalogo)


# =========================
# TESTE (igual ao enunciado)
# =========================

netflix = Plataforma("Netflix", "EUA")

catalogo = Catalogo("Filmes em Destaque", 0)

filme1 = Filme("Oppenheimer", 180, "Drama")
filme2 = Filme("Barbie", 114, "Comédia")

catalogo.add_filme(filme1)
catalogo.add_filme(filme2)

netflix.add_catalogo(catalogo)

usuario = Usuario("Ana", "ana@email.com", "Premium")

avaliacao = Avaliacao(9.5, "Incrível! Assisti duas vezes")

usuario.avaliar(filme1, avaliacao)

catalogo.listar_filmes()
usuario.ver_avaliacoes()