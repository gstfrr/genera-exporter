import sys
import os
import pandas as pd
from bs4 import BeautifulSoup
from domain.Parente import Parente

parentes_divs = []


def div_to_parente(div):
    nomes = div.find_all('h5', class_='gen-text gen-heading mb-2 line-height-18')
    nome = nomes[0].string.strip()

    emails = div.find_all('p', class_='gen-text gen-text-metal-grey caption mb-0')
    email = emails[0].string.strip()

    parentescos = div.find_all('div', class_='suggestion')
    parentesco = parentescos[0].string.strip()

    dnas = div.find_all('div', class_='shared-dna d-flex justify-content-center align-items-center line-height-24')
    dna_compartilhado = dnas[0].string.strip()

    mt_dnas = div.find_all('div', class_='mt-dna')
    mt_dna = mt_dnas[0].string.strip() if mt_dnas[0].string else None

    y_dnas = div.find_all('div', class_='y-dna')
    y_dna = y_dnas[0].string.strip() if y_dnas[0].string else None

    parente = Parente(nome, email, parentesco, dna_compartilhado, mt_dna, y_dna)
    return parente


def open_html_files_in_folder(folder_path):
    try:
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.html'):
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    soup = BeautifulSoup(content, 'html.parser')
                    divs = soup.find_all('div', class_='gen-card relative')
                    for div in divs:
                        parentes_divs.append(div)
    except FileNotFoundError:
        print(f"Folder {folder_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_to_excel(parentes, output_file):
    data = [{
        'Nome': parente.nome,
        'Email': parente.email,
        'Parentesco': parente.parentesco,
        'DNA Compartilhado': parente.dna_compartilhado,
        'mtDNA': parente.mt_dna,
        'yDNA': parente.y_dna
    } for parente in parentes]

    df = pd.DataFrame(data)
    df.to_excel(output_file, index=False)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_folder> <output_excel_file>")
    else:
        folder_path = sys.argv[1]
        output_file = sys.argv[2] + '/resultado.xlsx'
        open_html_files_in_folder(folder_path)
        parentes = [div_to_parente(div) for div in parentes_divs]
        write_to_excel(parentes, output_file)
        print(f"Data written to {output_file}")
