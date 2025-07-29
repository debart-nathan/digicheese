# Digicheese

Implementation of a RESTful API meeting the needs of the DigiCheese company.
> DigiCheese is a fictitious company.

The project was carried out as part of the Data Engineer 2025-D04 training course at [Diginamic](https://www.diginamic.fr/)  


# Getting Started

## Installation 

1. Clone the repository
```bash
git clone https://github.com/debart-nathan/digicheese/tree/develop
```

2. Create a virtual environment
ex :
```bash
python -m venv .venv
.venv\Scripts\activate #under unix : source .venve/bin/activate
```

3. Installing dependencies
```bash
pip install -r requirements.txt
```

4. Set environment variables
```bash
cp .env.template .env
```
DB_USERNAME : database username  
DB_PASSWORD : database pasword   
DB_HOST : database host  
DB_NAME : database name  
SERVER_HOST : serveur host  
SERVER_PORT : serveur port  
SERVER_RELOAD : if you want to reload the server automatically (True or False)  

ex:
```bash
DB_USERNAME = "root"
DB_PASSWORD = "root"
DB_HOST = "localhost"
DB_NAME = "Digicheese"
SERVER_HOST = "localhost"
SERVER_PORT = "8000"
SERVER_RELOAD = "True"
```
## Run the API serveur

```bash
python run.py
```

# Contact

## Contributor

[@DEBART Nathan](github.com/debart-nathan)  
[@RAHANITRINIAINA Bernard](https://github.com/Bernardinh0)  
[@GUIDOUX Bluwen](https://github.com/Bluwen)

## Educational referent
[@Hotton Robin](mailto:rhotton@diginamic-formation.fr)  

## Client
[@MOMIN Valentin](mailto:vmomin@diginamic-formation.fr)