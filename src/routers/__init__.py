from .commande_router import  router as router_commande
from .client_router import router as router_client
from .colis_routeur import router as router_colis
from .commune_router import router as router_commune
from .departement_router import router as router_departement
from .detail_colis_router import router as router_detail_colis
from .detail_commande_router import router as router_detail_commande
from .objet_router import router as router_objet
from .variation_objet_router import router as router_variation_objet

"""
API Router Aggregation Module

This module serves as a central point to import and collect all individual API routers
for the application. It gathers routers from various domain-specific modules to
create a comprehensive API structure.


Usage:
1. Import this module in your main FastAPI application
2. Include these routers using app.include_router()
3. All routes will be properly namespaced under their respective prefixes
"""