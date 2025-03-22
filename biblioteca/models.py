from django.db import models

from django.db import models


class Livro(models.Model):
    capa = models.ImageField(
        upload_to="capas/", blank=True, null=True, verbose_name="Capa"
    )
    titulo = models.CharField(max_length=255, verbose_name="Título")
    subtitulo = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Subtítulo"
    )
    projeto = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Projeto"
    )
    organizadores = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Organizadores"
    )
    autores = models.TextField(verbose_name="Autores")
    tipo = models.CharField(max_length=50, verbose_name="Tipo")
    isbn = models.CharField(
        max_length=20, blank=True, null=True, unique=True, verbose_name="ISBN"
    )
    ano_publicacao = models.IntegerField(verbose_name="Ano de Publicação")
    numero_paginas = models.CharField(
        max_length=50, verbose_name="Número de Páginas"
    )  # Alterado para comportar '140 p.'
    idioma = models.CharField(max_length=50, verbose_name="Idioma")
    formato = models.CharField(max_length=100, verbose_name="Formato")
    disponibilidade = models.CharField(max_length=255, verbose_name="Disponibilidade")
    dimensoes = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Dimensões (cm)"
    )
    classificacao_tema = models.CharField(
        max_length=255, verbose_name="Classificação/Tema"
    )
    cdu_thema = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="CDU / Thema"
    )
    palavras_chave = models.TextField(verbose_name="Palavras-chave")
    resumo = models.TextField(verbose_name="Resumo")
    link_pdf = models.URLField(blank=True, null=True, verbose_name="Link PDF")
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.titulo
