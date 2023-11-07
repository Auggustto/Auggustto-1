import requests
from bs4 import BeautifulSoup
import re

# URL da imagem de estatísticas do WakaTime
WAKATIME_STATS_IMAGE_URL = "https://wakatime.com/badge/user/Auggustto.svg"

# Substitua "YOUR_USER_ID" pelo seu ID de usuário do WakaTime

# URL do seu arquivo README no repositório do GitHub
README_URL = "https://raw.githubusercontent.com/Auggustto/Auggustto/main/README.md"

# Substitua "SEU_USUARIO" e "SEU_REPOSITORIO" pelos detalhes do seu repositório

# Faça uma solicitação à API do WakaTime
response = requests.get(WAKATIME_STATS_IMAGE_URL)

if response.status_code == 200:
    wakatime_stats_image = response.content

    # Atualize o README com a imagem das estatísticas do WakaTime
    response = requests.get(README_URL)
    if response.status_code == 200:
        readme_content = response.text

        # Use BeautifulSoup para encontrar a localização onde deseja inserir a imagem
        soup = BeautifulSoup(readme_content, 'html.parser')
        readme_content = str(soup)
        
        # Inclua a imagem no README
        updated_readme = re.sub(
            r'!\[WakaTime stats\]\(.*\)',
            f'![WakaTime stats]({WAKATIME_STATS_IMAGE_URL})',
            readme_content
        )

        # Atualize o README no repositório
        response = requests.put(README_URL, data=updated_readme)
        if response.status_code == 200:
            print("README atualizado com as estatísticas do WakaTime.")
        else:
            print(f"Falha ao atualizar o README. Código de status: {response.status_code}")
    else:
        print(f"Falha ao obter o conteúdo do README. Código de status: {response.status_code}")
else:
    print(f"Falha ao obter as estatísticas do WakaTime. Código de status: {response.status_code}")
