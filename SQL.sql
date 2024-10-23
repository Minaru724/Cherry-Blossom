CREATE DATABASE Cherry_Blossom;
USE Cherry_Blossom;

DROP TABLE IF EXISTS Predictions;
DROP TABLE IF EXISTS Data;
DROP TABLE IF EXISTS Locations;

CREATE TABLE Locations (
    City_ID INT AUTO_INCREMENT PRIMARY KEY,
    City VARCHAR(50)
);

CREATE TABLE Data (
    Year INT,
    Month INT,
    Day INT,
    City_ID INT,
    FOREIGN KEY (City_ID) REFERENCES Locations(City_ID)
);

CREATE TABLE Predictions (
    Month INT,
    Day INT,
    City_ID INT,
    FOREIGN KEY (City_ID) REFERENCES Locations(City_ID)
);

INSERT INTO Locations (
City) 
VALUES('稚内' );

INSERT INTO Data (
Year,
Month,
Day,
City_ID)
VALUES(2021,5,8,1);

INSERT INTO Predictions (
Month,
Day,
City_ID)
VALUES(5,13,1);
