import argparse
import json
from jinja2 import Template

parser= argparse.ArgumentParser(description='lê input')


parser.add_argument('--dict',required=True,help='O dicionario a ser passado')
args=parser.parse_args()
with open(args.dict, 'r', encoding='utf-8') as json_file:
    data_dict = json.load(json_file)

template_text = '''
Movies report
-------------------------------

Date : {{ date }}
Movies watched this month: {{ num_movies }}
Total minutes: {{ total_minutes }}

'''

# Criar um Template Jinja a partir do texto
template = Template(template_text)

# Renderizar o template com os dados
rendered_text = template.render(data_dict)

print(rendered_text)
