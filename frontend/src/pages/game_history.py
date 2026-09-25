"""
Streamlit page for Game History.

Displays a detailed table of a player's past games, including mode, opponent, and results.
"""

import pandas as pd
import streamlit as st

from utils.api_client import api_client
from utils.log_init import get_page_logger

# Initialisation du logger
logger = get_page_logger("game_history")

st.title("🎮 Game History")

# 1. Récupération de l'ID via les paramètres d'URL (id_player)
query_params = st.query_params

if "id_player" in query_params:
    try:
        player_id = int(query_params["id_player"])

        # 2. Appel API pour récupérer l'historique des matchs
        # Note: Endpoint assumed based on existing patterns
        response = api_client.get(f"/game/history/{player_id}")

        if response["status_code"] == 200:
            games_list = response["data"]

            # 3. Vérification si le joueur a joué des parties
            if not games_list:
                st.info(
                    "Aucune partie jouée pour le moment. Allez jouer pour remplir votre historique !"
                )
                logger.info(f"No games found for player {player_id}")
            else:
                st.success(f"Historique des parties pour le joueur {player_id}")

                # 4. Transformation des données JSON en DataFrame
                # On extrait les champs demandés : Game Mode, Opponent, Opponent elo, Result
                processed_data = []
                for game in games_list:
                    processed_data.append({
                        "Game Mode": game.get("game_mode", "N/A"),
                        "Opponent": game.get("opponent_username", "N/A"),
                        "Opponent Elo": game.get("opponent_elo", 0),
                        "Result": game.get("result", "N/A"),  # Expected: win, loss, draw
                    })

                df = pd.DataFrame(processed_data)

                # 5. Affichage du tableau
                st.dataframe(df, use_container_width=True)

                logger.info(
                    f"Successfully displayed {len(games_list)} games for player {player_id}"
                )

        elif response["status_code"] == 404:
            st.error("Historique introuvable.")
            logger.warning(f"History 404 for player {player_id}")
        elif response["status_code"] == 0:
            st.error(f"Erreur de connexion : {response['data']}")
            logger.error(f"Connection error for player {player_id}")
        else:
            st.error(f"Erreur API (Code {response['status_code']})")
            logger.error(f"API Error {response['status_code']} for player {player_id}")

    except ValueError:
        st.error("L'ID du joueur (id_player) doit être un nombre valide.")
        logger.error("Invalid id_player format in URL")
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue : {e}")
        logger.error(f"Unexpected error in game_history: {e}")

else:
    st.warning("Aucun id_player spécifié dans l'URL. Veuillez sélectionner un joueur.")
    if st.button("Retour à la liste des joueurs"):
        st.switch_page("pages/list_players.py")

st.divider()
