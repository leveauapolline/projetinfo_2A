-----------------------------------------------------
-- Player
-----------------------------------------------------
DROP TABLE IF EXISTS player CASCADE;
CREATE TABLE player (
    id_player    SERIAL PRIMARY KEY,
    username     VARCHAR(30) UNIQUE,
    password     VARCHAR(256),
    elo          INTEGER,
    email        VARCHAR(50),
    pokemon_fan  BOOLEAN,
    access_token VARCHAR(255)
);

-----------------------------------------------------
-- Game
-----------------------------------------------------


DROP TABLE IF EXISTS game;

CREATE TABLE game (
    id_game      SERIAL PRIMARY KEY,
    id_player1   INTEGER REFERENCES player(id_player),
    id_player2   INTEGER REFERENCES player(id_player),
    game_mode    VARCHAR(20),
    id_winner    INTEGER REFERENCES player(id_player),
    detail       VARCHAR(100),
    timestamp    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);