from utils import *
from datetime import datetime

def process_informations(response_api_json):    
    content = []

    for x in response_api_json["conteudo"]:
        layout = {
            "date_of_event": "",
            "meeting_subject": "",
            "meeting_location": "",
            "role" : "",
            "organization": "",
        }

        layout["date_of_event"] = datetime.strptime(x["dataEvento"], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d")
        layout["meeting_subject"] = format_text(x["descricao"])
        layout["meeting_location"] = extract_state(layout["meeting_subject"])
        layout["role"] = get_authority_by_role_id(extract_int_from_text(x["identificacaoAutoridade"]))
        layout["organization"] = "Banco Central do Brasil"

        content.append(layout)

    return sorted(content, key=lambda dictionary: dictionary["date_of_event"])
