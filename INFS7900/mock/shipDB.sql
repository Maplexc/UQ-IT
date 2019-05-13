create table ShipModels (
    model varchar(100),
    type varchar(100),
    country varchar(100),
    numGuns int,
    bore int,
    displacement int,
    primary key (model));

create table Battles(
    battleName varchar(100),
    date2 date, 
    primary key (battleName));

create table Ships (
    shipName varchar(100) , 
    model varchar(100), 
    launched int, 
    PRIMARY KEY (shipName), 
    foreign key (model) references ShipModels(model));

create table Outcomes(
    shipName varchar(100),
    battleName varchar(100),
    result varchar(100),
    primary key (shipName, battleName),
    foreign key (shipName) references Ships(shipName),
    foreign key (battleName) references Battles(battleName));



insert into ShipModels values ('Bismarch','bb','Germany', 8, 15, 42000);
insert into ShipModels values ('Iowa','bb','USA', 9, 16, 46000);
insert into ShipModels values ('Kongo','bc','Japan', 8, 14, 32000);
insert into ShipModels values ('North Carolina','bb','USA', 9, 16, 37000);
insert into ShipModels values ('Renown','bc','Britain', 6, 15, 32000);
insert into ShipModels values ('Revenge','bb','Britain', 8, 15, 29000);
insert into ShipModels values ('Tennessee','bb','USA', 12, 14, 32000);
insert into ShipModels values ('Yamoto','bb','Japan', 9, 18, 65000);

insert into Battles values ('Denmark','1941-05-25');
insert into Battles values ('Guadalcanal','1942-11-15');
insert into Battles values ('North Cape','1943-12-26');
insert into Battles values ('Surigao Strait','1944-10-25');

insert into Ships values("California", "Tennessee", 1921);
insert into Ships values("Haruna", "Kongo", 1915);
insert into Ships values("Hiei", "Kongo", 1914);
insert into Ships values("lowa", "Iowa", 1943);
insert into Ships values("Kirishma", "Kongo", 1915);
insert into Ships values("Kongo", "Kongo", 1913);
insert into Ships values("Missouri", "Iowa", 1944);
insert into Ships values("Musashi", "Yamoto", 1942);
insert into Ships values("New Jersey", "Iowa", 1943);
insert into Ships values("North Carolina", "North Carolina", 1941);
insert into Ships values("Ramillies", "Revenge", 1917);
insert into Ships values("Renown", "Renown", 1916);
insert into Ships values("Repulse", "Renown", 1916);
insert into Ships values("Resolution", "Revenge", 1916);
insert into Ships values("Revenge", "Revenge", 1916);
insert into Ships values("Royal Oak", "Revenge", 1916);
insert into Ships values("Royal Sovereign", "Revenge", 1916);
insert into Ships values("Tennessee", "Tennessee", 1920);
insert into Ships values("Washington", "North Carolina", 1941);
insert into Ships values("Wisconsin", "Iowa", 1944);
insert into Ships values("Yamota", "Yamoto", 1941);

insert into Outcomes values ('California','Surigao Strait','ok');
insert into Outcomes values ('Kirishma','Guadalcanal','sunk');
insert into Outcomes values ('Tennessee','Surigao Strait','ok');
insert into Outcomes values ('Washington','Guadalcanal','ok');
insert into Outcomes values ('Washington','North Cape','sunk');
insert into Outcomes values ('Royal Oak','North Cape','damaged');
insert into Outcomes values ('Royal Oak','Surigao Strait','sunk');
