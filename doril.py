import re

# NOMES DOS ARQUIVOS
nome_arquivo = "doril.txt"
nome_texto_pos_tags_html = "doril_pos_tags_html.txt"
nome_texto_pos_urls = "doril_pos_urls.txt"
nome_texto_pos_emoji = "doril_pos_emoji.txt"

# SIMBOLOS
simbolos_html = r'<.*?>'
simbolos_url = r'(?:http|https|www)\S+'
simbolos_emoji = re.compile(
    "["
    "\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\U0001F1E0-\U0001F1FF"  # flags (iOS)
    "\u2600-\u26FF"          # miscellaneous symbols
    "\u2700-\u27BF"          # dingbats
    "]+",
    flags=re.UNICODE
)


#############################################################################
# ABRE ARQUIVO PRINCIPAL
with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.close()

# Remover tags HTML;
texto_sem_html = re.sub(simbolos_html, '', conteudo)

# ARQUIVO SEM AS TAGS HTML
with open(nome_texto_pos_tags_html, "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_sem_html)
    arquivo.close()

#############################################################################
# ABRE ARQUIVO SEM AS TAGS HTML
with open(nome_texto_pos_tags_html, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.close()

# Remover URLs;
texto_sem_url = re.sub(simbolos_url, '', conteudo)

# ARQUIVO SEM AS URLs
with open(nome_texto_pos_urls, "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_sem_url)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO SEM AS URLs
with open(nome_texto_pos_urls, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.close()
    
# Remover emojis;
texto_sem_emoji = simbolos_emoji.sub(r'', conteudo)

# ARQUIVO SEM OS EMOJIS
with open(nome_texto_pos_emoji, "w", encoding="utf-8") as arquivo:
    arquivo.write(texto_sem_emoji)
    arquivo.close()