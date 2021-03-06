create table Zone (
	Id_zone INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Id_zone PRIMARY KEY,
	Title varchar(100) NOT NULL
);
create table Level (
	Id_level INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Id_level PRIMARY KEY,
	Title varchar(100) NOT NULL
);

create table Passenger (
	Id_passenger INT ,
	Id_cart BIGINT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Id_passenger PRIMARY KEY ,
	Name_p varchar(20) NOT NULL,
	Last_name varchar(50) NOT NULL,
	Middle_name varchar(50) NOT NULL,
	Rating int NOT NULL,
	Id_zone int NOT NULL,
	Id_level int NOT NULL,
	Nickname varchar(50) NOT NULL,
	FOREIGN KEY (Id_zone) REFERENCES Zone(Id_zone),
	FOREIGN KEY (Id_level) REFERENCES Level(Id_level)
);
create table Bus (
	Id_bus BIGINT NOT NULL,
	Id_route BIGINT NOT NULL,
	Id_validator BIGINT NOT NULL CONSTRAINT PK_Id_validator PRIMARY KEY,
	Number_bus varchar(9) NOT NULL
);

create table Transportation (
	Id_cart BIGINT NOT NULL,
	Id_validator BIGINT NOT NULL,
	Type_ticket varchar(50) NOT NULL,
	Ticket_number BIGINT NOT NULL,
	Date DATE NOT NULL,
	Time time NOT NULL,
	Id_exit BIGINT NOT NULL,
	FOREIGN KEY (Id_validator) REFERENCES Bus(Id_validator),
	FOREIGN KEY (Id_cart) REFERENCES Passenger(Id_cart)
);