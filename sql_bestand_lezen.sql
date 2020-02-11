DROP DATABASE database_test;

CREATE DATABASE database_test;

use database_test;

CREATE TABLE vacatures
(
    id           INTEGER PRIMARY KEY AUTO_INCREMENT,
    woord        VARCHAR(50),
    beschrijving TEXT
);

INSERT INTO vacatures (woord, beschrijving)
VALUES ('product owner', 'Je hebt (natuurlijk) een grote passie voor het werk van de NOS.
Je hebt minimaal twee jaar ervaring als Product Owner van high traffic apps en websites. Ervaring in de mediasector is een grote pre.
Je bent analytisch, oplossingsgericht, denkt projecten goed uit en ziet geen enkel detail over het hoofd. Jij prioriteert werkzaamheden op basis van onze roadmap, data, onderzoek en je gezonde verstand.
Je hebt overtuigingskracht, organisatietalent en ontwikkelt gemakkelijk een netwerk in de organisatie.
Je bent technisch goed onderlegd en kunt inhoudelijk developers challengen op hun aanpak en oplossingen.
Als voorvechter van een agile methodiek hecht je grote waarde aan samenwerking en continue verbetering. Jouw stijl van werken motiveert en inspireert je collega’s.
Je deelt graag kennis met anderen en helpt je collega’s - gevraagd én ongevraagd.')

#de rollen waarvoor we appart 5 vacatures willen zijn:
# Back end, Front end, AI, Cloud, Pruduct owner (SCRUM