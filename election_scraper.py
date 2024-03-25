"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
author: Václav Mrkvička
email: vasek.mrkvicka@gmail.com
discord: spectra111
"""


import requests
from bs4 import BeautifulSoup
import csv
import sys

def scrapuj_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []

    for table in soup.find_all('table', {'class': 'table'}):
        for row in table.find_all('tr')[2:]:
            columns = row.find_all(['td', 'th'])
            if len(columns) >= 2:
                city_id = columns[0].text.strip()
                city_name = columns[1].text.strip()

                link_column = columns[0]
                link_tag = link_column.find('a')
                if link_tag:
                    base_url = "https://volby.cz/pls/ps2017nss/"
                    link_to_tables = base_url + link_tag.get('href', '')

                    additional_info = get_additional_info(link_to_tables)

                    data.append({
                        'kod_obce': city_id,
                        'nazev_obce': city_name,
                        'volici_v_seznamu': additional_info.get('volici_v_seznamu'),
                        'vydane_obalky': additional_info.get('vydane_obalky'),
                        'platne_hlasy': additional_info.get('platne_hlasy'),
                        'party_names': additional_info.get('party_names', []),
                        'party_votes': additional_info.get('party_votes', [])
                    })

    return data

def get_additional_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    volici_v_seznamu = soup.find('td', {'headers': 'sa2'})
    vydane_obalky = soup.find('td', {'headers': 'sa3'})
    platne_hlasy = soup.find('td', {'headers': 'sa6'})

    party_names = extract_party_names(soup)
    party_votes = extract_party_votes(soup, party_names)

    return {
        'volici_v_seznamu': volici_v_seznamu.text.strip() if volici_v_seznamu else '',
        'vydane_obalky': vydane_obalky.text.strip() if vydane_obalky else '',
        'platne_hlasy': platne_hlasy.text.strip() if platne_hlasy else '',
        'party_names': party_names,
        'party_votes': party_votes
    }


def extract_party_names(soup):
    party_names = [th.text.strip() for th in soup.find_all('td', class_="overflow_name")]
    return party_names


def extract_party_votes(soup, party_names):
    party_votes = {party_name: '' for party_name in party_names}

    # Najdi všechny tabulky s třídou 't2_470'
    party_votes_tables = soup.find_all('div', class_='t2_470')
    
    # Procházej všechny nalezené tabulky
    for party_votes_table in party_votes_tables:
        rows = party_votes_table.find_all('tr')[2:] 
        for row in rows:
            columns = row.find_all('td')
            if len(columns) >= 3:
                party_name = columns[1].text.strip()
                votes_text = columns[2].text.strip().replace('\xa0', '')  
                try:
                    party_votes[party_name] = int(votes_text)
                except ValueError:
                    
                    party_votes[party_name] = ''
    
    return party_votes



def save_to_csv(output_filename, data):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['kod_obce', 'nazev_obce', 'volici_v_seznamu', 'vydane_obalky', 'platne_hlasy'] + data[0].get('party_names', [])
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for row in data:
            row_data = {
                'kod_obce': row['kod_obce'],
                'nazev_obce': row['nazev_obce'],
                'volici_v_seznamu': row['volici_v_seznamu'],
                'vydane_obalky': row['vydane_obalky'],
                'platne_hlasy': row['platne_hlasy']
                
            }

           
            for party_name in row.get('party_names', []):
                row_data[party_name] = row['party_votes'].get(party_name, '')

            writer.writerow(row_data)


if __name__ == "__main__":
    # Kontrola počtu argumentů
    if len(sys.argv) != 3:
        print("Špatně zadane URL, název souboru nebo počet argumentů")
        print("Použití: python nazev_skriptu.py <url> <vysledny_soubor>")
    elif len(sys.argv) <2:
        print("Špatně zadane URL, název souboru nebo počet argumentů")
        print("Použití: python nazev_skriptu.py <url> <vysledny_soubor>")
    else:
        # Získání argumentů z příkazové řádky
        url = sys.argv[1]
        output_file = sys.argv[2]
        print("Spoustím script")
        print("Stahuji data ze zadaného URL, za chvili bude hotovo")
        # Volání funkce pro scrapování a ukládání
        complete_data = scrapuj_data(url)
        print("DOKONČENO")
        save_to_csv(output_file, complete_data)