INSERT INTO player(username, password, elo, email, pokemon_fan) VALUES
('admin',     '0000',  null,  'admin@project.io',     null),
('a',         'a',     1200,  'a@ensai.fr',           true),
('maurice',   '1234',  1000,  'maurice@ensai.fr',     true),
('batricia',  '9876',  1500,  'bat@project.io',       false),
('miguel',    'abcd',  1300,  'miguel@project.io',    true),
('gilbert',   'toto',  1100,  'gilbert@project.io',   false),
('junior',    'aaaa',  1200,  'junior@project.io',    true);



INSERT INTO game(id_player1, id_player2, game_mode, id_winner, detail) VALUES
(1, 2, 'coinflip', 1, 'Gilbert chose heads, result was heads'),
(3, 4, 'dice',     3, 'Maurice rolled 5, Batricia rolled 2'),
(3, 4, 'dice',     null, 'Maurice rolled 4, Batricia rolled 4'),
(4, 3, 'dice',     4, 'Batricia rolled 2, Maurice rolled 1'),
(3, 4, 'coinflip', 4, 'Maurice chose heads, result was tails');