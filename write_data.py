import sqlite3
import read_data
import cocktail_api


def create_database(cursor):
    command = """
    create table City
(
   id           INTEGER
       constraint City_pk
           primary key autoincrement,
   plz          int,
   name         text,
   country_name text,
   state        name
);

create table Anschrift
(
   id            INTEGER
       constraint Anschrift_pk
           primary key autoincrement,
   city_id       INTEGER
       references City,
   street        text,
   street_number int
);

create table Bar
(
   name   text,
   id     INTEGER not null
       constraint Bar_pk
           primary key autoincrement,
   ort_id INTEGER
       references Anschrift
);

create unique index Bar_id_uindex
   on Bar (id);

create table Drinks
(
   id   INTEGER
       constraint Drinks_pk
           primary key autoincrement,
   name text
);

create table Extras
(
   name text,
   id   INTEGER
       constraint Extras_pk
           primary key autoincrement
);

create table Spirituosen
(
   alcohol_gehalt real    not null,
   name           text,
   id             INTEGER not null
       constraint Spirituosen_pk
           primary key autoincrement
);

create table glas
(
   name   text,
   id     INTEGER
       constraint glas_pk
           primary key autoincrement,
   volume int
);

create table Cocktail
(
   name    text,
   id      INTEGER not null
       constraint Cocktail_pk
           primary key autoincrement,
   glas_id int
       references glas
);

create table Cocktail_Drinks
(
   cocktail_id INTEGER
       references Cocktail
           on update restrict on delete restrict,
   drink_id    INTEGER
       references Drinks
           on update cascade on delete cascade,
   Menge       int
);

create table Cocktails_Bar
(
   cocktail_id int
       references Cocktail,
   bar_id      int
       references Bar,
   price       int
);

create table Extra_Cocktail
(
   extra_id    int
       references Extras,
   cocktail_id int
       references Cocktail,
   Menge       int
);

create table Sprituosen_Cocktails
(
   cocktail_id  INTEGER
       references Cocktail,
   spritosen_id INTEGER
       references Spirituosen,
   Menge        int
);

create table user
(
   user_name    text,
   email_adress text,
   password     text,
   id           INTEGER
       constraint user_pk
           primary key autoincrement,
   wohn_ort     INTEGER
       references Anschrift
);

create table BarReview
(
   text    text,
   user_id int
       references user,
   bar_id  int
       references Bar,
   stars   int
);

create table CocktailReview
(
   text        text,
   created_by  int
       references user,
   cocktail_id int
       references Cocktail,
   stars       int,
   id          INTEGER not null
       constraint Review_pk
           primary key autoincrement
);

create unique index user_id_uindex
   on user (id);
"""
    statements = command.split(";")
    for st in statements:
        cursor.execute(st)


def insert_cocktail(cursor, cocktail_name):
    command = f"INSERT INTO Cocktail(name) VALUES ('{cocktail_name}');"
    cursor.execute(command)


def insert_glass(cursor, glass_name):
    command = f"INSERT INTO glas(name) VALUES ('{glass_name}')"
    cursor.execute(command)


def insert_cocktail_names(c, count):
    cocktail_names = cocktail_api.get_cocktail_names(count)

    for cn in cocktail_names:
        insert_cocktail(c, cn)


def insert_glass_names(c, count):
    glasses = cocktail_api.get_glasses(count)
    for glas in glasses:
        insert_glass(c, glas)


if __name__ == '__main__':
    conn = sqlite3.connect("new_cocktails.db")
    c = conn.cursor()
    insert_glass_names(c, 100)
    conn.commit()
    c.close()
    conn.close()

