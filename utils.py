import re
import html

def extract_int_from_text(text:str):
    return ''.join([caractere for caractere in text if caractere.isdigit()])

def extract_state(text:str):
    states = [
        "Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará", "Distrito Federal", "Brasília", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso",
        "Mato Grosso do Sul", "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco","Piauí", "Rio de Janeiro", "Rio Grande do Norte",
        "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina", "São Paulo", "Sergipe", "Tocantins", "Lisboa, República Portuguesa", "Atenas, Grécia",
        "videoconferência", "Washington DC, EUA", "Washington, D.C. (EUA)", "Basileia, Suíça", "são Paulo", "Marraquexe, Marrocos"
        ]

    present_states = [state for state in states if state in text]

    return "/".join(present_states) if len(present_states) != 0 else "Desconhecido"

def get_authority_by_role_id(role_id:str):
    role_by_id = {
        "01": "Presidente",
        "02": "​​​Diretor de Administração​",
        "03": "​Diretor de Assuntos Internacionais e de Gestão de Riscos Corporativos​",
        "04": "Diretor de Fiscalização",
        "05": "​​Diretor de Organização do Sistema Financeiro e Resolução",
        "06": "Diretor de Política Econômica",
        "07": "​Diretor de Política Monetária",
        "08": "Diretor de Regulação",
        "09": "Diretora de Relacionamento, Cidadania e Supervisão de Conduta",
        "10": "Procurador-Geral​",
        "11": "Secretário-Executivo",
        "12": "Chefe de Gabinete do Presidente",
     }
    
    return role_by_id[role_id]

def format_text(text:str):
    text = re.sub("</div>", "\n", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub("&amp;", "&", text)
    text = re.sub("&lt;", "<", text)
    text = re.sub("&gt;", ">", text)
    text = re.sub("&apos;", "'", text)
    text = re.sub("&quot;", '"', text)
    text = re.sub(u"\u200b", " ", text)
    text = re.sub(u"\xa0", " ", text)
    text = re.sub("\xa0", " ", text)
    text = re.sub("&nbsp", " ", text)
    text = re.sub("\n", " ", text)

    return html.unescape(text)

# Convertendo o tamanho do arquivo para uma forma legível
def file_size(size):
    for unidade in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f}{unidade}"
        size /= 1024.0