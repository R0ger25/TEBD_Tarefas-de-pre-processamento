import re

nome_arquivo = "doril.txt"
nome_texto_pos_tags_html = "doril_pos_tags_html.txt"

with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

texto_original = conteudo

simbolos_html = r'<.*?>'

texto_pos_tags_html = re.sub(simbolos_html, '', texto_original)

with open(nome_texto_pos_tags_html, "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_pos_tags_html)