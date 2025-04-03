from biblioteca.models import Livro  # Substitua pelo nome correto do seu app e modelo

def limpar_espacos():
    livros = Livro.objects.all()  # Obt?m todos os registros
    for livro in livros:
        # Remover espa?os em branco de cada campo relevante
        livro.titulo = livro.titulo.strip() if livro.titulo else None
        livro.subtitulo = livro.subtitulo.strip() if livro.subtitulo else None
        livro.projeto = livro.projeto.strip() if livro.projeto else None
        livro.organizadores = livro.organizadores.strip() if livro.organizadores else None
        livro.autores = livro.autores.strip() if livro.autores else None
        livro.tipo = livro.tipo.strip() if livro.tipo else None
        livro.isbn = livro.isbn.strip() if livro.isbn else None
        livro.idioma = livro.idioma.strip() if livro.idioma else None
        livro.formato = livro.formato.strip() if livro.formato else None
        livro.disponibilidade = livro.disponibilidade.strip() if livro.disponibilidade else None
        livro.dimensoes = livro.dimensoes.strip() if livro.dimensoes else None
        livro.classificacao_tema = livro.classificacao_tema.strip() if livro.classificacao_tema else None
        livro.cdu_thema = livro.cdu_thema.strip() if livro.cdu_thema else None
        livro.palavras_chave = livro.palavras_chave.strip() if livro.palavras_chave else None
        livro.resumo = livro.resumo.strip() if livro.resumo else None
        livro.link_pdf = livro.link_pdf.strip() if livro.link_pdf else None

        # Salva as altera??es no banco de dados
        livro.save()
    print("Espaços removidos com sucesso!")