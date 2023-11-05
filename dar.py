import json
from datetime import datetime
import argparse

argparse = argparse.ArgumentParser()
argparse.add_argument("--Nmro", required=True, help="nmro de filmes")
argparse.add_argument("--minutos", default=90, help="minutagem total")
args = argparse.parse_args()

data = {
    "date": datetime.now().isoformat(),  # Converte o datetime para uma string ISO 8601
    "num_movies": args.Nmro,
    "total_minutes": args.minutos,
}

# Especifica o caminho para o arquivo JSON
json_file_path = "data.json"

# Abre o arquivo para escrita, sobrescrevendo se já existir
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file)

print(f"O dicionário foi salvo em '{json_file_path}'")
