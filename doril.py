import re
import nltk
import json
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from num2words import num2words
from spellchecker import SpellChecker

corretor = SpellChecker(language='pt')

nlp = spacy.load('pt_core_news_sm')

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
nome_texto_pos_espacos_em_branco = "doril_pos_espacos_em_branco.json"
nome_texto_pos_girias = "doril_pos_girias.json"
nome_texto_pos_numeros_convertidos = "doril_pos_numeros_convertidos.json"
nome_texto_pos_letras_minusculas = "doril_pos_letras_minusculas.json"
nome_texto_pos_stemização_ou_lematização = "doril_pos_stemização_ou_lematização"

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
girias = {
    "vc": "você",
    "cê": "você",
    "vcs": "vocês",
    "pq": "porque",
    "q": "que",
    "cd": "cadê",
    "kd": "cadê",
    "blz": "beleza",
    "vlw": "valeu",
    "flw": "falou",
    "msg": "mensagem",
    "zap": "whatsapp",
    "mano": "amigo",
    "parça": "amigo",
    "bro": "irmão",
    "mt": "muito",
    "mto": "muito",
    "td": "tudo",
    "fds": "fim de semana",
    "tmj": "tamo junto",
    "slc": "se liga",
    "ctz": "certeza",
    "sqn": "só que não",
    "kkk": "risada",
    "rs": "risada",
    "lol": "risada",
    "nois": "nós",
    "tpw": "tipo",
    "aq": "aqui",
    "aki": "aqui",
    "hj": "hoje",
    "dps": "depois",
    "aki": "aqui",
    "bjs": "beijos",
    "abs": "abraços",
    "pfv": "por favor",
    "pls": "por favor",
    "obg": "obrigado",
    "vlwflw": "valeu falou",
    "sq": "sei que",
    "miga": "amiga",
    "cringe": "vergonhoso",
    "xau": "tchau",
    "partiu": "vamos",
    "top": "legal",
    "gata": "garota",
    "gato": "garoto",
}

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
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO SEM AS PONTUAÇÕES E CARACTERES ESPECIAIS
with open(nome_texto_pos_pontuacao, 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()

# Remover espaços em branco excedentes;
tokens_sem_espacos = [token.strip() for token in conteudo]

# ARQUIVO SEM ESPAÇOS EM BRANCO
with open(nome_texto_pos_espacos_em_branco, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_sem_espacos, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()

#############################################################################
# ABRE ARQUIVO SEM ESPAÇOS EM BRANCO
with open(nome_texto_pos_espacos_em_branco, 'r', encoding='utf-8') as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()

# Substituir palavras usadas em chat por suas formas normais;
tokens_corrigidos = [girias.get(token, token) for token in conteudo]

# ARQUIVO SEM GIRIAS
with open(nome_texto_pos_girias, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_corrigidos, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO SEM GIRIAS
with open(nome_texto_pos_girias, "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()

# Converter números em palavras;
tokens_convertidos = []

for token in conteudo:
    if token.isdigit():
        numero = int(token)
        palavra_numero = num2words(numero, lang='pt_BR')
        tokens_convertidos.append(palavra_numero)
    else:
        tokens_convertidos.append(token)

# ARQUIVO COM NUMEROS CONVERTIDOS
with open(nome_texto_pos_numeros_convertidos, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_convertidos, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO COM NUMEROS CONVERTIDOS
with open(nome_texto_pos_numeros_convertidos, "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()
    
# Converter todo o texto para letras minúsculas;
tokens_minusculos = [token.lower() for token in conteudo]

# ARQUIVO COM LETRAS MINUSCULAS
with open(nome_texto_pos_letras_minusculas, "w", encoding="utf-8") as arquivo:
    json.dump(tokens_minusculos, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()
    
#############################################################################
# ABRE ARQUIVO COM LETRAS MINUSCULAS
with open(nome_texto_pos_letras_minusculas, "r", encoding="utf-8") as arquivo:
    conteudo = json.load(arquivo)
    arquivo.close()

# DEPENDE DO CECNÁRIO QUE VAI USAR. PARA A BULA NÃO É INDICADO, MAS PARA O JORNAL A TRIBUNA SIM.

# # Aplicar correção ortográfica;
# palavras_erradas = corretor.unknown(conteudo)

# for palavra in palavras_erradas:
#     sugestao = corretor.correction(palavra)
#     print(f"Para '{palavra}', a sugestão é '{sugestao}'")

#############################################################################
# Aplicar stemização | lematização

texto = " ".join(conteudo)

doc = nlp(texto)

lemas = [token.lemma_ for token in doc]

with open(nome_texto_pos_stemização_ou_lematização, "w", encoding="utf-8") as arquivo:
    json.dump(lemas, arquivo, ensure_ascii=False, indent=4)
    arquivo.close()