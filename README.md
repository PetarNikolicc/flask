Flask Personregister Applikation

Denna Flask-applikation är ett enkelt personregister som tillåter användare att visa en lista över personer, lägga till nya personer och visa detaljerad information om varje person.

Funktioner
Visa en lista över alla personer i registret.
Visa detaljerad information om varje person.

Tekniker
Flask för backend.
SQLAlchemy för databasinteraktioner.
SQLite som databas.
Jinja2 för templating.
Installation
För att köra applikationen lokalt, följ dessa steg:

Klona repot till din lokala maskin:

Använd följande kommando för att klona GitHub-repot till din dator:

bash
Copy code
git clone https://github.com/PetarNikolicc/flask.git
cd flask
Skapa en virtuell miljö:

Använd detta kommando för att skapa en virtuell miljö med namnet venv:

Copy code
python3 -m venv venv
Aktivera den virtuella miljön:

På Windows, använd:

Copy code
venv\Scripts\activate
På MacOS/Linux, använd:

bash
Copy code
source venv/bin/activate
Installera beroenden:

Installera alla nödvändiga beroenden som listas i requirements.txt med pip:

Copy code
pip install -r requirements.txt
Kör applikationen:

Starta Flask-applikationen genom att köra:

arduino
Copy code
flask run
Applikationen kommer att vara tillgänglig på http://127.0.0.1:5000/.

Databas Initialisering
Databasen och dess tabeller skapas automatiskt när applikationen startas. Om du behöver återställa databasen, ta bort personregister.db filen och starta om applikationen.