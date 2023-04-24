# Tetris v Python PRU0059
## Instalace
Instalace potřebných balíčků do python prostředí
```
$ pip install -r requirements.txt
```
Popřípádě vytvoření virtuálního prostředí a instalace do něj
```
$ python3 -m venv venv/vm          # Vytvoří virtuální prostředí 
$ source venv/vm/bin/activate      # Aktivuje prostředí
(vm) $ pip install -r requirements.txt # Instalace do prostředí
```

## Spuštění
Ve složce se soubory spustit:
```
python main.py
```

## Popis programu
Periodicky se generuje jeden z náhodných tvarů. Generuje se na náhodne pozici. Tvary padají samostatně dolů Když se vyplní řádek, uživatel dostává body. Uživatel dostává body i za každý dopadnutý dílek
## Ovládání 
<kbd>↓</kbd> - Posun dolů

<kbd>←</kbd> - Posun doleva

<kbd>→</kbd> - Posun doprava

<kbd>↑</kbd> - Rotace dílku

<kbd>P</kbd> - Zrychlení padání dílku

<kbd>M</kbd> - Zpomalení padání dílku

<kbd>Space</kbd> - Rychlé posunutí dolů

<kbd>Esc</kbd> - Vypnutí hry
