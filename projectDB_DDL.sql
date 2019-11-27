CREATE DATABASE projectDB;
USE projectDB;

CREATE TABLE Patient(
	THC INT NOT NULL AUTO_INCREMENT,
    First_Name VARCHAR(35) NOT NULL,
    Last_Name VARCHAR(35) NOT NULL,
    DOB DATE NOT NULL,
    SSN VARCHAR(9),
    Insurance VARCHAR(35), 
    Tel VARCHAR(35) NOT NULL,
    Email VARCHAR(35),
    PRIMARY KEY(THC)
);

CREATE TABLE Visit(
	Visit_ID INT NOT NULL AUTO_INCREMENT,
    THC INT NOT NULL,
    Visit_Date Date NOT NULL,
    Visit_Num INT NOT NULL,
    PRIMARY KEY(Visit_ID),
    FOREIGN KEY (THC) REFERENCES Patient(THC)
);

INSERT INTO Patient (First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email) 
VALUES('Kobe', 'Bryant', '2000-1-1', '111111111', 'Ins1', '4081111111', 'kobe.bryant@gmail.com');

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(1, '2000-1-1', 1);

INSERT INTO Patient (First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email) 
VALUES('Lebron', 'James', '2000-1-2', '222222222', 'Ins2', '4082222222', 'lebron.james@gmail.com');

INSERT INTO Patient (First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email) 
VALUES('Dwight', 'Howard', '2000-1-3', '333333333', 'Ins3', '4083333333', 'dwight.howard@gmail.com');

INSERT INTO Patient (First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email) 
VALUES('Derek', 'Fisher', '2000-1-4', '444444444', 'Ins1', '4084444444', 'derek.fisher@gmail.com');

INSERT INTO Patient (First_Name, Last_Name, DOB, SSN, Insurance, Tel, Email) 
VALUES('Yao', 'Ming', '2000-1-5', '555555555', 'Ins2', '4085555555', 'yao.ming@gmail.com');

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(2, '2000-1-2', 1);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(1, '2000-1-3', 2);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(3, '2000-1-4', 1);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(2, '2000-1-5', 2);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(1, '2000-1-6', 3);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(4, '2000-1-7', 1);

INSERT INTO Visit(THC, Visit_Date, Visit_Num)
VALUES(5, '2000-1-8', 1);


/*
ALTER TABLE `Patient` MODIFY COLUMN `THC` INT NOT NULL AUTO_INCREMENT;

ALTER TABLE `Visit` MODIFY COLUMN `Visit_ID` INT NOT NULL AUTO_INCREMENT;
*/


CREATE TABLE Interview(
	Interview_ID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (Interview_ID),
    Visit_ID INT,
    FOREIGN KEY (Visit_ID) REFERENCES Visit(Visit_ID),
    Clinic_Num INT,
    THC_Num VARCHAR(25),
    T_Bad_Days BOOLEAN,
    T_Effect_Of_Sound VARCHAR(25),
    T_How_long DATETIME,
    T_Ear_Overprotection BOOLEAN,
    T_In_Quiet BOOLEAN,
    T_Any_Other_T_Specific_Treatments VARCHAR(35),
    T_Aware_Percent DECIMAL,
    T_Annoyed_Percent DECIMAL,
    T_Severity INT,
    T_Annoyance INT,
    T_Effect_Of_Life INT,
    T_Concentration BOOLEAN,
    T_Sleep BOOLEAN,
    T_QRA BOOLEAN,
    T_Work BOOLEAN,
    T_Restaurants BOOLEAN,
    T_Sports BOOLEAN,
    T_Social BOOLEAN,
    T_Other BOOLEAN,
    T_Frequency BOOLEAN,
    S_Concerts BOOLEAN,
    S_Shopping BOOLEAN,
    S_Movies BOOLEAN,
    S_Work BOOLEAN,
    S_Restaurants BOOLEAN,
    S_Driving BOOLEAN,
    S_Sports BOOLEAN,
    S_Church BOOLEAN,
    S_Housekeeping BOOLEAN,
    S_Childcare BOOLEAN,
    S_Social BOOLEAN,
    S_Other BOOLEAN,
    T_Comments VARCHAR(35),
    ST_Comments VARCHAR(35),
    S_Description_Of_Troublesome_Sounds VARCHAR(35),
    S_Bad_Days BOOLEAN,
    S_Effect_Of_Sound VARCHAR(25),
    S_How_long DATETIME,
    S_Ear_Overprotection BOOLEAN,
    S_In_Quiet BOOLEAN,
    S_Percent_Of_Time DECIMAL,
    S_Any_Other_ST_Specific_Treatments VARCHAR(35),
    S_Severity INT,
    S_Annoyance INT,
    S_Effect_Of_Life INT,
    S_Frequent BOOLEAN,
    L_Hearing_Problem BOOLEAN,
    L_Hearing_Aid BOOLEAN,
    Aid_Type VARCHAR(25),
    L_Ever_Recommended BOOLEAN,
    Rk_Tinn INT,
    RK_Sound_Tolerance INT,
    RK_Hearing INT
);


CREATE TABLE Initial_Interview(
	ID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(ID),
    FOREIGN KEY (ID) REFERENCES Interview(Interview_ID),
    T_Onset VARCHAR(25),
    T_Fluctuations_In_Volume BOOLEAN,
    T_Description_Of_T_Sound VARCHAR(35),
    T_Why_Is_A_Problem VARCHAR(35),
    S_Oversensitivity BOOLEAN,
    S_Physical_Discomfor BOOLEAN,
    S_Why_Is_ST_A_Problem VARCHAR(25),
    HL_Hearing_Problem BOOLEAN,
    HL_Hearing_Aid BOOLEAN,
    HL_Ever_Recommended BOOLEAN,
    HL_Hearing_Aid_Type BOOLEAN
);

CREATE TABLE Followup_Interview(
	ID INT NOT NULL AUTO_INCREMENT,
    Category BOOLEAN,
    Date_Of_Initial_Couns DATE,
    Date_Of_Instr_Fitt DATE,
	SG VARCHAR(25),
	HA VARCHAR(25),
	FUQ INT,
	Month INT,
	T_Percent_Aware BOOLEAN,
	T_Percent_Annoyed BOOLEAN,
	S_Bad BOOLEAN,
	HL_The_Problem_In_General VARCHAR(25),
	Feedback VARCHAR(25),
	Main_Disscussed VARCHAR(25),
    PRIMARY KEY(ID),
    FOREIGN KEY (ID) REFERENCES Interview(Interview_ID)
);