# Digicheese

Implementation of a RESTful API meeting the needs of the DigiCheese company.
> DigiCheese is a fictitious company.

The project was carried out as part of the Data Engineer 2025-D04 training course at [Diginamic](https://www.diginamic.fr/)  


# Project Structure
```
├───src/
│   ├───models/
│   ├───repositories/
│   ├───routers/
│   └───services/
├───tests/
├───README.md
├───.gitignore
├───.env.template
├───requirements.txt
└───run.py
```


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

# Test

## Run test

```bash
pytest tests/
```

## Coverage

```
============================================================================================= tests coverage ============================================================================================= 
____________________________________________________________________________ coverage: platform win32, python 3.13.2-final-0 _____________________________________________________________________________ 

Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
src\__init__.py                                      0      0   100%
src\database.py                                     12      4    67%
src\main.py                                         15      2    87%
src\models\__init__.py                               9      0   100%
src\models\client_model.py                          26      0   100%
src\models\colis_model.py                           18      0   100%
src\models\commande_model.py                        22      0   100%
src\models\commune_model.py                         18      0   100%
src\models\departement_model.py                     14      0   100%
src\models\detail_colis_model.py                    22      0   100%
src\models\detail_commande_model.py                 22      0   100%
src\models\objet_model.py                           15      0   100%
src\models\variation_objet_model.py                 20      0   100%
src\repositories\__init__.py                         9      0   100%
src\repositories\client_repository.py               32      1    97%
src\repositories\colis_repository.py                32      0   100%
src\repositories\commande_repository.py             32      0   100%
src\repositories\commune_repository.py              32      0   100%
src\repositories\departement_repository.py          32      1    97%
src\repositories\detail_colis_repository.py         32      0   100%
src\repositories\detail_commande_repository.py      32      0   100%
src\repositories\objet_repository.py                32      0   100%
src\repositories\variation_objet_repository.py      32      0   100%
src\routers\__init__.py                             10      0   100%
src\routers\client_router.py                        37      0   100%
src\routers\colis_routeur.py                        32      0   100%
src\routers\commande_router.py                      32      0   100%
src\routers\commune_router.py                       32      0   100%
src\routers\departement_router.py                   32      1    97%
src\routers\detail_colis_router.py                  32      0   100%
src\routers\detail_commande_router.py               32      0   100%
src\routers\objet_router.py                         31      0   100%
src\routers\variation_objet_router.py               31      0   100%
src\services\__init__.py                             1      0   100%
src\services\client_service.py                      48      0   100%
--------------------------------------------------------------------
TOTAL                                              860      9    99%
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