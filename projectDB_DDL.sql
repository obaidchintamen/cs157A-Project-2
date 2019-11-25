CREATE DATABASE projectDB;
USE projectDB;

CREATE TABLE Patient(
	THC INT NOT NULL,
    First_Name VARCHAR(35) NOT NULL,
    Last_Name VARCHAR(35) NOT NULL,
    DOB DATE NOT NULL,
    SSN INT,
    Insurance VARCHAR(35), 
    Tel INT NOT NULL,
    PRIMARY KEY(THC)
);

CREATE TABLE Problem(
	Problem_ID INT NOT NULL,
    Problem_Name VARCHAR(35),
    PRIMARY KEY(Problem_ID)
);


CREATE TABLE Initial_Interview(
	Interview_ID INT NOT NULL,
    Email VARCHAR(25),
    Ptn_Decision VARCHAR(25),
    PRIMARY KEY(Interview_ID)
);

CREATE TABLE Follow_Up_Interview(
	Interview_ID INT NOT NULL,
	Category VARCHAR(1),
    Date_Of_Initial_Couns DATE,
    Date_Of_Instruction DATE,
    Problem_In_General VARCHAR(25),
    Feeling_Of_Giving_Instrument VARCHAR(35),
    Feedback VARCHAR(35),
    Problem_Discussed VARCHAR(35),
    PRIMARY KEY(Interview_ID)
);

CREATE TABLE Visit(
	Visit_ID INT NOT NULL,
    THC INT NOT NULL,
    Visit_Date Date,
    Comments VARCHAR(35),
    Visit_Num INT NOT NULL,
    PRIMARY KEY(Visit_ID)
);


CREATE TABLE Interview(
	Interview_ID INT NOT NULL,
    Visit_ID INT NOT NULL, 
    Problem_ID INT NOT NULL,
    Clinic_Num INT NOT NULL,
    Tinnituous_Ranking INT, 
    Sound_Tolerance_Ranking INT,
    Hearing_Ranking INT,
    Next_Visit DATE,
    T_Severity INT,
    T_Annyoyance INT,
    T_Effect_Of_Life INT,
    T_Activities_Prevented VARCHAR(35),
    ST_Severity INT,
    ST_Annyoyance INT,
    ST_Effect_Of_Life INT,
    ST_Activities_Prevented VARCHAR(35),
    HL_Hearing_Problem BOOLEAN,
    HL_Hearing_Aid BOOLEAN,
    HL_Ever_Recommended BOOLEAN
);

CREATE TABLE THI(
	Visit_ID INT NOT NULL,
	Question1 INT,
	Question2 INT,
    Question3 INT,
    Question_Point_Sum INT
);

CREATE TABLE TFI(
	Visit_ID INT NOT NULL,
	Question1 INT,
	Question2 INT,
    Question3 INT
);
