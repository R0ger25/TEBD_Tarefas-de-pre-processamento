import re
import nltk
import json
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixar os pacotes necessários (só na primeira vez)
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')

# NOMES DOS ARQUIVOS
nome_arquivo = "doril.txt"
nome_texto_pos_tags_html = "doril_pos_tags_html.txt"
nome_texto_pos_urls = "doril_pos_urls.txt"
nome_texto_pos_emoji = "doril_pos_emoji.txt"
nome_texto_pos_stopwords = "doril_pos_stopwords.json"
nome_texto_pos_pontuacao = "doril_pos_pontuacao.json"

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
simbolos_pontuacao = r'[^a-zA-Z0-9\sàáâãéêíóôõúüçÀÁÂÃÉÊÍÓÔÕÚÜÇ]'


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

#############################################################################
# ABRE ARQUIVO SEM OS EMOJIS

with open(nome_texto_pos_emoji, "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    arquivo.close()

# Remover stopwords;
lista_stopwords = stopwords.words('portuguese')
tokens = word_tokenize(conteudo, language='portuguese')

tokens_limpos = []

for palavra in tokens:
    if palavra.lower() not in lista_stopwords:
        tokens_limpos.append(palavra)

# ARQUIVO SEM AS STOPWORDS
with open(nome_texto_pos_stopwords, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_limpos, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO SEM AS STOPWORDS
with open(nome_texto_pos_stopwords, 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()
    
tokens_sem_pontuacao = []

for token in conteudo:
    token = re.sub(simbolos_pontuacao, '', token)
    if token:
        tokens_sem_pontuacao.append(token)

# ARQUIVO SEM AS PONTUAÇÕES
with open(nome_texto_pos_pontuacao, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_sem_pontuacao, arquivo, ensure_ascii=False, indent=4)
    print(arquivo)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO SEM AS PONTUAÇÕES E CARACTERES ESPECIAIS