"""
Streamlit page for player stats.

Provides navigation to available actions such as listing players or playing games for logged-in users.
"""

import streamlit as st

from utils.api_client import api_client  # Import de l'instance déjà prête
from utils.log_init import get_page_logger

# Initialisation du logger
logger = get_page_logger("player_stats")

st.title("Player stats")

# 1. Récupération de l'ID via les paramètres d'URL (Maintenant id_player)
query_params = st.query_params

if "id_player" in query_params:
    try:
        # Conversion de la valeur reçue en entier
        player_id = int(query_params["id_player"])

        # 2. Utilisation de l'API Client
        # FIX: Changed "/players/" to "/player/" to match backend/README.md sequence diagram
        response = api_client.get(f"/player/{player_id}")

        if response["status_code"] == 200:
            player_data = response["data"]

            # 3. AFFICHAGE DES DONNÉES
            st.success(f"Données récupérées pour le joueur {player_id}")

            # Affichage structuré avec colonnes
            col1, col2 = st.columns(2)
            with col1:
                # Attributes match backend/src/business_object/player.py
                st.metric("Nom", player_data.get("username", "N/A"))
                st.metric("Email", player_data.get("email", "N/A"))
            with col2:
                # Using 'elo' as defined in backend/src/business_object/player.py
                st.metric("Elo Rating", player_data.get("elo", 0))

            # Affichage détaillé dans un expander
            with st.expander("Voir les détails complets (JSON)"):
                st.json(player_data)

            logger.info(f"Successfully displayed stats for player {player_id}")

        elif response["status_code"] == 404:
            st.error("Joueur introuvable.")
            logger.warning(f"Player {player_id} not found (404)")
        elif response["status_code"] == 0:
            st.error(f"Erreur de connexion : {response['data']}")
            logger.error(f"Connection error for player {player_id}: {response['data']}")
        else:
            st.error(f"Erreur API (Code {response['status_code']})")
            logger.error(f"API Error {response['status_code']} for player {player_id}")

    except ValueError:
        st.error("L'ID du joueur (id_player) doit être un nombre valide.")
        logger.error("Invalid id_player format in URL")
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue : {e}")
        logger.error(f"Unexpected error in player_stats: {e}")

else:
    # Cas où id_player est absent de l'URL
    st.warning("Aucun id_player spécifié dans l'URL. Veuillez sélectionner un joueur.")
    if st.button("Retour à la liste des joueurs"):
        st.switch_page("pages/list_players.py")
