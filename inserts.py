
from crud_operations import create_record


# INSERCIONES DE LA BASE DE DATOS:
publisher_1 = {
    "_id": "publisher_1",
    "type": "publisher",
    "name": "Awesome Games Studio",
    "totalsales": 200000
}

publisher_2 = {
    "_id": "publisher_2",
    "type": "publisher",
    "name": "Epic Developers",
    "totalsales": 700000
}

publisher_3 = {
    "_id": "publisher_3",
    "type": "publisher",
    "name": "Rockstar Games",
    "totalsales": 850000
}

publisher_4 = {
    "_id": "publisher_4",
    "type": "publisher",
    "name": "Poor Developers",
    "totalsales": 110000
}

publisher_5 = {
    "_id": "publisher_5",
    "type": "publisher",
    "name": "CapCom",
    "totalsales": 340000
}

create_record(publisher_1)
create_record(publisher_2)
create_record(publisher_3)
create_record(publisher_4)
create_record(publisher_5)

# INSERCIONES DE LOS VIDEOJUEGOS

videogame_1 = {
    "_id": "videogame_1",
    "type": "videogame",
    "name": "Space Invaders",
    "genre": "Arcade",
    "units_sold": 500,
    "publisher_id": "1"
}

videogame_2 = {
    "_id": "videogame_2",
    "type": "videogame",
    "name": "Zelda breath of the wild",
    "genre": "Adventure",
    "units_sold": 750000,
    "publisher_id": "2"
}

videogame_3 = {
    "_id": "videogame_3",
    "type": "videogame",
    "name": "Zuma deluxe",
    "genre": "Arcade",
    "units_sold": 750000,
    "publisher_id": "3"
}
videogame_4 = {
    "_id": "videogame_4",
    "type": "videogame",
    "name": "Minecraft",
    "genre": "Adventure",
    "units_sold": 1100000,
    "publisher_id": "1"
}
videogame_5 = {
    "_id": "videogame_5",
    "type": "videogame",
    "name": "Marvel vs DC",
    "genre": "Action",
    "units_sold": 750000,
    "publisher_id": "5"
}

create_record(videogame_1)
create_record(videogame_2)
create_record(videogame_3)
create_record(videogame_4)
create_record(videogame_5)

user_1 = {
    "_id": "user_1",
    "type": "user",
    "name": "John Doe",
    "email": "johndoe@example.com",
    "country": "USA"
}

user_2 = {
    "_id": "user_2",
    "type": "user",
    "name": "Jane Smith",
    "email": "janesmith@example.com",
    "country": "Canada"
}
user_3 = {
    "_id": "user_3",
    "type": "user",
    "name": "Julio carajito",
    "email": "julioCarajito@example.com",
    "country": "Canada"
}
user_4 = {
    "_id": "user_4",
    "type": "user",
    "name": "Isabella Zuluaga",
    "email": "IsaZulu@example.com",
    "country": "Colombia"
}
user_5 = {
    "_id": "user_5",
    "type": "user",
    "name": "Andrea Florez",
    "email": "andre99@example.com",
    "country": "Colombia"
}

create_record(user_1)
create_record(user_2)
create_record(user_3)
create_record(user_4)
create_record(user_5)

review_1 = {
    "_id": "review_1",
    "type": "review",
    "rating": 5,
    "comment": "Amazing game!",
    "user_id": "user_1",
    "videogame_id": "videogame_1"
}

review_2 = {
    "_id": "review_2",
    "type": "review",
    "rating": 4,
    "comment": "Really enjoyed it!",
    "user_id": "user_2",
    "videogame_id": "videogame_2"
}

review_3 = {
    "_id": "review_3",
    "type": "review",
    "rating": 3,
    "comment": "It was okay.",
    "user_id": "user_1",
    "videogame_id": "videogame_3"
}

review_4 = {
    "_id": "review_4",
    "type": "review",
    "rating": 5,
    "comment": "Best game ever!",
    "user_id": "user_4",
    "videogame_id": "videogame_4"
}

review_5 = {
    "_id": "review_5",
    "type": "review",
    "rating": 2,
    "comment": "Not great.",
    "user_id": "user_3",
    "videogame_id": "videogame_5"
}

create_record(review_1)
create_record(review_2)
create_record(review_3)
create_record(review_4)
create_record(review_5)
