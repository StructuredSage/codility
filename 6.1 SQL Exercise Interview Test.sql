/*
Tabels
phones: 
    to store phone data
regions:    
    geo data  
customers: 
    customer info. Includes fk to region_id  
sales: 
    records of phone sales. I'm assuming the discounts are % of the total amount and not promotions. If it was the latter a separated table with promotions/discounts info would be benefitial. Includes fk to region_id. This is my fact table.

Notes:
- I added fk to region_id in both customer and sales to cover physical and online sales. The report by region can be filetered based on customers' need
- Since it is not specified, I will assume the database engine is Microsoft SQL Server 2014 or up since is the most commercial of them all.

*/


-- Creation of the Phones Table
CREATE TABLE Phones
(
    phone_id          INT IDENTITY (1,1) PRIMARY KEY,
    model_name        VARCHAR(255) NOT NULL,
    manufacturer      VARCHAR(255) NOT NULL,
    phone_description VARCHAR(MAX),
    unitary_cost      DECIMAL(10, 2)
);
GO
-- Creation of the Regions Table
CREATE TABLE Regions
(
    region_id INT IDENTITY (1,1) PRIMARY KEY,
    country   VARCHAR(255) NOT NULL,
    state     VARCHAR(255),
    city      VARCHAR(255) NOT NULL
);
GO
-- Creation of the Customers Table
CREATE TABLE Customers
(
    customer_id INT PRIMARY KEY,
    name        VARCHAR(255)        NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    join_date   DATE                NOT NULL,
    region_id   INT FOREIGN KEY REFERENCES regions (region_id)
);
GO
-- Creation of the Sales Table
CREATE TABLE Sales
(
    sale_id         INT IDENTITY (1,1) PRIMARY KEY,
    customer_id     INT,
    phone_id        INT,
    sale_date       DATE           NOT NULL,
    quantity        INT            NOT NULL,
    region_id       INT FOREIGN KEY REFERENCES regions (region_id),
    total_amount    DECIMAL(10, 2) NOT NULL,
    discount_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES Customers (customer_id),
    FOREIGN KEY (phone_id) REFERENCES Phones (phone_id),
    FOREIGN KEY (region_id) REFERENCES Regions (region_id)
);
GO