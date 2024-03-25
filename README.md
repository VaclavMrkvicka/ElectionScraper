# ElectionScraper - Projekt ENGETO
Třetí Projekt na Python Akademii od ENGETO


# Popis projektu

Tento projekt slouží k extrahování výsledků z parlamentních voleb v roce 2017. Příklad stránky, kterou scrapujeme [ZDE](https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3107)


# Instalace knihoven

Knihovny, ktere jsou použity v kódu jsou uložene v souboru `requirements.txt`. Pro instalaci doporučuji použit nové virtuální prostřední a s naistalovaným manaženrem spustit následovně:

```
pip3 --version                                # oveření verze manažeru
pip3 install -r requirements.txt              # naistalování knihoven
```

# Spuštení projektu
Spuštění souboru `election_scraper.py` požaduje dva povinné argumenty, které zadáme do příkazového řádku
```
python election_scraper.py <URL uzemního celku> <Název-souboru.csv>
```
Následně se vam stahnou vysledky jako soubor s priponou `.csv`. 

NEZAPOMENOUT NA PŘÍPONU U DRUHÉHO ARGUMENTU

# Ukázka projektu

Výsledky hlasování pro okres Tábor:

1.argument: `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3107`

2.argument: `vysledky_tabor.csv`

Spuštění programu:

`python election_scraper.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3107" "vysledky_tabor.csv" `

Průběh stahování:

```
Spoustím script
Stahuji data ze zadaného URL, za chvili bude hotovo
DOKONČENO
```

Částečny výstup:
```
kod_obce,nazev_obce,volici_v_seznamu,vydane_obalky,platne_hlasy...
563251,Balkova Lhota,102,69,69,4,0,0,8,0,7,7,0,0,2,0,0,8,0,5,16,0,0,3,0,0,0,0,9,0
563366,Bečice,63,52,52,10,0,0,5,0,2,2,0,0,1,0,0,11,0,2,3,0,0,1,0,1,0,0,14,0
552054,Bechyně,4 405,2 774,2 752,255,5,3,189,4,103,355,27,18,53,4,8,242,2,230,793,2,9,105,1,31,4,10,283,16
560448,Běleč,153,106,102,12,0,0,7,1,7,20,0,1,3,0,0,5,0,4,30,0,0,7,0,0,0,0,5,0
552097,Borkovice,195,133,133,24,0,0,8,0,3,11,2,1,1,0,0,9,0,9,47,0,0,4,0,0,0,0,13,1
552101,Borotín,525,349,346,33,0,0,23,0,32,43,5,5,7,0,1,30,0,12,103,1,0,24,1,1,0,2,23,0
```

