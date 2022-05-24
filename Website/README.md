# Website
Dieses Repository beinhaltet die Website für die Reservierung eines Raums zu einer bestimmten Uhrzeit. Zudem werden verschiedene Schnittstellen zur Verfügung gestellt, die für die "externen" Funktionalitäten (Display, NFC Reader) benötigt werden.

## Datenmodell
Beispiel:
```json
{
    "date": "Fri, 08 Apr 2022 00:00:00 GMT", 
    "from_time": "Fri, 08 Apr 2022 17:10:00 GMT", 
    "id": 1, 
    "name": "Max Mustermann", 
    "to_time": "Fri, 08 Apr 2022 19:10:00 GMT"
}
```

## Schnittstellen und Funktionalitäten

| Methode | Endpoint       | Beschreibung                                                                                                                                                                                      |
|---------|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GET     | /              | Gibt [index.html](./templates/index.html) zurück.                                                                                                                                                 |
| GET     | /reservation   | Gibt [reservation.html](./templates/reservation.html) zurück. Darin befindet sich ein Formular für die Reservierung eines Raums.                                                                  |
| GET     | /admin         | Admin View (Flask-admin-package)                                                                                                                                                                  |
| GET     | /api/data      | Gibt alle Reservierungen zurück.                                                                                                                                                                  |
| GET     | /isAvailable   | Gibt zurück, ob der Raum verfügbar (`True`) oder besetzt (`False`) ist. Zudem wird zurückgegeben, wie lange er noch verfügbar ist.                                                                |
| GET     | /done          | Gibt [done.html](./templates/done.html) zurück.                                                                                                                                                   |
| POST    | /reservation   | Hiermit wird eine Reservierung mittels eines Formulars in [reservation.html](./templates/reservation.html) in die Datenbank gespeichert.                                                          |
| GET     | /bycard/`name` | Für `name` wird eine Reservierung von `datetime.now()` bis `datetime.now() + 30 min` getätigt. Es wird zurückgegeben, ob die Reservierung möglich ist `True` oder nicht `False`. |
