<img src="docs\GCPConnection.PNG">

# DDL Code
CREATE TABLE Report(\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Division of Records Number INT,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date Reported DATE,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Date Occurred DATE, Time Occurred TIME,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Latitude REAL,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Longitude REAL,  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crime Code REAL,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Weapon Used Code REAL,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO Code REAL,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Area INT,  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Premises Code INT,  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY(Division of Records Number),  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(Crime Code) REFERENCES(Crime Codes.Crime Code), \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(Weapon Used Code) REFERENCES(Weapon.Weapon Used Code),\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(MO Code) REFERENCES(Modus Operandi.MO Code), \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(Area) REFERENCES(Location.Area), \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;FOREIGN KEY(Premises Code) REFERENCES(Premises.Premises Code)\
);


CREATE TABLE Victim(\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Division of Record Number INT, \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Age INT,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sex VARCHAR(255), \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Descent VARCHAR(255), \
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Descent Description VARCHAR(255),  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY(Division of Record Number)\
);


CREATE TABLE Premises(\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Premises Code INT,\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Premises Description VARCHAR(255),  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRIMARY KEY(Premises Code)\
);


CREATE TABLE Location(\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Area INT,  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Area Name VARCHAR(255),\
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Report District Number INT,  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; PRIMARY KEY(Area)\
);


CREATE TABLE Weapon Used(\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Weapon Used Code REAL,   
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Weapon Description VARCHAR(255),  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY(Weapon Used Code)\
);


CREATE TABLE Modus Operandi(\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO Code REAL,  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MO Description VARCHAR(255),  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY(MO Code)  
);


CREATE TABLE Crime Codes(\
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crime Code REAL,  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Crime Code Description VARCHAR(255), \
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PRIMARY KEY(Crime Code)\
);
