#!/usr/bin/python3
import sys
import os

def carregar_settings():
    settings = {}
    with open("settings.py", "r") as settings_file:
        config = settings_file.readlines()
        for line in config:
            key, value = line.strip().split(' = ')
            settings[key] = value.strip('\'"')
    return settings

def gera_conteudo_template(conteudo, settings):
    html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{settings['title']}</title>
</head>
<body>
    {conteudo}
</body>
</html>
"""

    return html

def gerar_template(nome_template, settings):

    with open(nome_template, 'r') as template_file:
        template_content = "".join(template_file.readlines())
        template_file.close()
    for key, value in settings.items():
        template_content = template_content.replace('{' + key + '}', value)

    return template_content

def salvar_como_html(output_filename, conteudo_render):
    with open(output_filename, 'w') as output_file:
        output_file.write(conteudo_render)

def renderiza():
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template_file>")
        return

    nome_template = sys.argv[1]
    if not nome_template.endswith('.template') or not os.path.exists(nome_template) or not os.path.isfile(nome_template):
        print("Template invalido")
        return

    settings = dict(carregar_settings())
    conteudo_render = gerar_template(nome_template, settings)
    teste = gera_conteudo_template(conteudo_render, settings)


    output_filename = nome_template.replace('.template', '.html')
    salvar_como_html(output_filename, teste)

    print(f"HTML gerado e salvo como {output_filename}")

if __name__ == '__main__':
    renderiza()