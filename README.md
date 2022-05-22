# Easy Room
Ein KT CE Projekt für eine einfache Raumbuchung mittels Raspberry Pi, NFC Reader und Display.

## Voraussetzungen

Zur Ausführung des Projekts wird ein 
Raspberry Pi 4 mit Raspberry Pi OS, 
[NFC Reader](https://www.amazon.de/gp/product/B01L9GC470/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1) und ein 
[Display](https://www.amazon.de/gp/product/B07WCRTKSF/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
vorausgesetzt. 
`Python 3.8` und `pip` (normalerweise bereits mit Python mitverpackt) werden benötigt um das Projekt auszuführen.

Begib dich in das Wurzelverzeichnis des Projekts, öffne darin das Terminal und führe folgenden Befehl aus
um die benötigten Dependencies zu installieren (bevorzugt innerhalb einer virtuellen Umgebung für Python):
```
pip install -r requirements.txt
```

## Starten

Easy Room lässt sich ganz einfach mittels des Skripts `start.py` starten.
Im selben Terminal führe folgenden Befehl aus:
```
python3 start.py
```
Dadurch wird der Webserver hochgefahren und danach automatisch die Skripte für den NFC Reader und das Display gestartet.

## Komponenten

![Architektur](Architektur.png)

* [Website/Flask-Webserver](/Website)

