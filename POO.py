# ===================== CLASSE PAI =====================
class Conteudo:
    def __init__(self, titulo, genero):
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(self.titulo, "-", self.genero)

# ===================== CLASSES FILHAS =====================

# ----------------------------- 1 ---------------------------
class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print("FILME:", self.titulo,
              "| Genero:", self.genero,
              "| Duracao:", self.duracao, "min")

# ----------------------------- 2 ---------------------------
class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print("SERIE:", self.titulo,
              "| Genero:", self.genero,
              "| Temporadas:", self.temporadas)

# ----------------------------- 3 ---------------------------
class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print("Documentario:", self.titulo,
              "| Genero:", self.genero,
              "| Tema:", self.tema)
# ----------------------------- 3 ---------------------------
class Podcast(Conteudo):
    def __init__(self, titulo, genero, entrevistado):
        super().__init__(titulo, genero)
        self.entrevistado = entrevistado

    def exibir_info(self):
        print("Podcast:", self.titulo,
              "| Genero:", self.genero,
              "| Entrevistado:", self.entrevistado)
# ===================== INSTANCIAÇÃO =====================

filme1 = Filme("Homem-aranha: um novo dia", "Ação", 169)
serie1 = Serie("The Office", "Sitcom", "4")
documentario1 = Documentario("Ilha das Flores", "Gênero misto", "Desigualdade socioeconômica")
podcast1 = Podcast("Nerdcast","Comédia","Tucano")

# ===================== EXIBIÇÃO =====================
catalogo = [
    Filme("Homem-aranha: um novo dia", "Ação", 169),
    Serie("The Office", "Sitcom", "4"),
    Documentario("Ilha das Flores", "Gênero misto", "Desigualdade socioeconômica"),
    Podcast("Nerdcast","Comédia","Tucano")

]

catalogo = [filme1, serie1, documentario1, podcast1]
for item in catalogo:
    item.exibir_info()
