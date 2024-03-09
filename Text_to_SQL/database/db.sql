CREATE DATABASE A2ZDigital ;

USE A2ZDigital ;

## ---------------- Categories table ----------------

CREATE TABLE Category(Categoryid VARCHAR(30) PRIMARY KEY, 
                      Category VARCHAR(30)
);

INSERT INTO Category (Categoryid, Category) VALUES
('CTPH01', 'Phones'),
('CTLP01', 'Laptops'),
('CTAS01', 'Accessories');

## ---------------- Items table ----------------

CREATE TABLE Items (Itemid VARCHAR(30) PRIMARY KEY, 
                    Categoryid VARCHAR(30), 
                    Brand VARCHAR(50), 
                    ModelName VARCHAR(50), 
					Specifications VARCHAR(500), 
                    Price DECIMAL(10, 2),
                    FOREIGN KEY (Categoryid) REFERENCES Category(Categoryid)
);

-- Phones
INSERT INTO Items (Itemid, Categoryid, Brand, ModelName, Specifications, Price) VALUES 
('PH01', 'CTPH01', 'Samsung', 'Galaxy S21', '6.2-inch, 128GB storage, 8GB RAM', 70000.00),
('PH02', 'CTPH01', 'Apple', 'iPhone 13', '6.1-inch, 128GB storage, 4GB RAM', 79900.00),
('PH03', 'CTPH01', 'OnePlus', 'OnePlus 9 Pro', '6.7-inch, 256GB storage, 12GB RAM', 69999.00),
('PH04', 'CTPH01', 'Xiaomi', 'Redmi Note 10 Pro', '6.67-inch, 128GB storage, 6GB RAM', 17999.00),
('PH05', 'CTPH01', 'Google', 'Pixel 6', '6.4-inch, 128GB storage, 8GB RAM', 59999.00),
('PH06', 'CTPH01', 'Realme', 'Realme GT 5G', '6.43-inch, 128GB storage, 8GB RAM', 27999.00),
('PH07', 'CTPH01', 'Vivo', 'Vivo X70 Pro+', '6.78-inch, 256GB storage, 12GB RAM', 79990.00),
('PH08', 'CTPH01', 'Oppo', 'Oppo Reno 6 Pro', '6.55-inch, 128GB storage, 12GB RAM', 39990.00),
('PH09', 'CTPH01', 'Nokia', 'Nokia G50', '6.82-inch, 128GB storage, 4GB RAM', 14999.00),
('PH10', 'CTPH01', 'Motorola', 'Motorola Edge 20', '6.7-inch, 128GB storage, 8GB RAM', 34999.00) ;

-- Laptops
INSERT INTO Items (Itemid, Categoryid, Brand, ModelName, Specifications, Price) VALUES 
('LP01', 'CTLP01', 'Dell', 'Inspiron 15', '15.6-inch, Intel i5, 8GB RAM, 256GB SSD', 59990.00),
('LP02', 'CTLP01', 'HP', 'Pavilion 14', '14-inch, Ryzen 5, 8GB RAM, 512GB SSD', 52990.00),
('LP03', 'CTLP01', 'Lenovo', 'IdeaPad Slim 5', '15.6-inch, Intel i7, 16GB RAM, 1TB SSD', 79990.00),
('LP04', 'CTLP01', 'Asus', 'VivoBook 14', '14-inch, Intel i3, 4GB RAM, 1TB HDD', 39990.00),
('LP05', 'CTLP01', 'Acer', 'Aspire 7', '15.6-inch, AMD Ryzen 7, 16GB RAM, 512GB SSD', 65990.00),
('LP06', 'CTLP01', 'Microsoft', 'Surface Laptop 4', '13.5-inch, Intel i5, 8GB RAM, 256GB SSD', 91999.00),
('LP07', 'CTLP01', 'Apple', 'MacBook Air', '13.3-inch, M1 Chip, 8GB RAM, 256GB SSD', 92900.00),
('LP08', 'CTLP01', 'Samsung', 'Galaxy Book Pro', '15.6-inch, Intel i7, 16GB RAM, 512GB SSD', 104999.00),
('LP09', 'CTLP01', 'LG', 'Gram 14', '14-inch, Intel i5, 8GB RAM, 512GB SSD', 81990.00),
('LP10', 'CTLP01', 'Razer', 'Blade 15', '15.6-inch, Intel i7, 16GB RAM, 1TB SSD', 239990.00) ;

-- Accessories
INSERT INTO Items (Itemid, Categoryid, Brand, ModelName, Specifications, Price) VALUES 
('AS01', 'CTAS01', 'Boat', 'Rockerz 450', 'Wireless Headphones, Bluetooth', 1499.00),
('AS02', 'CTAS01', 'JBL', 'Flip 5', 'Bluetooth Speaker, Waterproof', 9999.00),
('AS03', 'CTAS01', 'Logitech', 'MX Master 3', 'Wireless Mouse, Ergonomic Design', 5999.00),
('AS04', 'CTAS01', 'Sony', 'WH-1000XM4', 'Noise Cancelling Headphones, Bluetooth', 24990.00),
('AS05', 'CTAS01', 'Bose', 'SoundLink Revolve+', 'Portable Bluetooth Speaker', 19990.00),
('AS06', 'CTAS01', 'Samsung', 'Galaxy Buds Pro', 'True Wireless Earbuds, Active Noise Cancelling', 15990.00),
('AS07', 'CTAS01', 'Apple', 'AirPods Pro', 'Wireless Earbuds, Active Noise Cancellation', 24900.00),
('AS08', 'CTAS01', 'Philips', 'SHB2505', 'Wireless Earphones, Bluetooth', 3499.00),
('AS09', 'CTAS01', 'Plantronics', 'BackBeat FIT 6100', 'Wireless Sport Headphones, Sweatproof', 7999.00),
('AS10', 'CTAS01', 'Beats', 'Powerbeats Pro', 'Wireless Earphones, Water Resistant', 15999.00) ;

## ---------------- Discount table ----------------

CREATE TABLE Discount (
    Itemid VARCHAR(30),
    Categoryid VARCHAR(30),
    Discount DECIMAL(5, 2) NOT NULL,
    LastUpdate DATETIME,
    PRIMARY KEY (Itemid),
    FOREIGN KEY (Itemid) REFERENCES Items(Itemid),
    FOREIGN KEY (Categoryid) REFERENCES Category(Categoryid)
);

-- Phones
INSERT INTO Discount (Itemid, Categoryid, Discount) VALUES
('PH01', 'CTPH01', 5.00),
('PH02', 'CTPH01', 10.00),
('PH03', 'CTPH01', 7.50),
('PH04', 'CTPH01', 15.00),
('PH05', 'CTPH01', 8.00),
('PH06', 'CTPH01', 12.00),
('PH07', 'CTPH01', 10.00),
('PH08', 'CTPH01', 7.00),
('PH09', 'CTPH01', 5.50),
('PH10', 'CTPH01', 10.00);

-- Laptops
INSERT INTO Discount (Itemid, Categoryid, Discount) VALUES
('LP01', 'CTLP01', 5.00),
('LP02', 'CTLP01', 7.50),
('LP03', 'CTLP01', 10.00),
('LP04', 'CTLP01', 8.00),
('LP05', 'CTLP01', 12.00),
('LP06', 'CTLP01', 10.00),
('LP07', 'CTLP01', 15.00),
('LP08', 'CTLP01', 7.00),
('LP09', 'CTLP01', 5.50),
('LP10', 'CTLP01', 10.00);

-- Accessories
INSERT INTO Discount (Itemid, Categoryid, Discount) VALUES
('AS01', 'CTAS01', 5.00),
('AS02', 'CTAS01', 7.50),
('AS03', 'CTAS01', 10.00),
('AS04', 'CTAS01', 8.00),
('AS05', 'CTAS01', 12.00),
('AS06', 'CTAS01', 10.00),
('AS07', 'CTAS01', 15.00),
('AS08', 'CTAS01', 7.00),
('AS09', 'CTAS01', 5.50),
('AS10', 'CTAS01', 10.00);

CREATE TRIGGER UpdateDiscountLastUpdate
BEFORE UPDATE ON Discount
FOR EACH ROW
SET NEW.LastUpdate = NOW();

## ---------------- Inventory Management ----------------

CREATE TABLE Stock (
    Itemid VARCHAR(30) PRIMARY KEY, 
    Categoryid VARCHAR(30), 
    Quantity INT,
    LastUpdate DATETIME,
    FOREIGN KEY (Categoryid) REFERENCES Category(Categoryid),
    FOREIGN KEY (Itemid) REFERENCES Items(Itemid)
);

-- Phones
INSERT INTO Stock (Itemid, Categoryid, Quantity) VALUES
('PH01', 'CTPH01', 100),
('PH02', 'CTPH01', 120),
('PH03', 'CTPH01', 80),
('PH04', 'CTPH01', 150),
('PH05', 'CTPH01', 90),
('PH06', 'CTPH01', 110),
('PH07', 'CTPH01', 130),
('PH08', 'CTPH01', 70),
('PH09', 'CTPH01', 140),
('PH10', 'CTPH01', 100);

-- Laptops
INSERT INTO Stock (Itemid, Categoryid, Quantity) VALUES
('LP01', 'CTLP01', 90),
('LP02', 'CTLP01', 100),
('LP03', 'CTLP01', 80),
('LP04', 'CTLP01', 110),
('LP05', 'CTLP01', 95),
('LP06', 'CTLP01', 105),
('LP07', 'CTLP01', 120),
('LP08', 'CTLP01', 85),
('LP09', 'CTLP01', 130),
('LP10', 'CTLP01', 90);

-- Accessories
INSERT INTO Stock (Itemid, Categoryid, Quantity) VALUES
('AS01', 'CTAS01', 200),
('AS02', 'CTAS01', 180),
('AS03', 'CTAS01', 220),
('AS04', 'CTAS01', 190),
('AS05', 'CTAS01', 210),
('AS06', 'CTAS01', 195),
('AS07', 'CTAS01', 205),
('AS08', 'CTAS01', 225),
('AS09', 'CTAS01', 185),
('AS10', 'CTAS01', 215);

CREATE TRIGGER UpdateStockLastUpdate
BEFORE UPDATE ON Stock
FOR EACH ROW
SET NEW.LastUpdate = NOW();

## ---------------- Sales ----------------

CREATE TABLE Sales (
    Itemid VARCHAR(30) PRIMARY KEY, 
    Categoryid VARCHAR(30), 
    QuantitySold INT,
    LastUpdate DATETIME,
    FOREIGN KEY (Categoryid) REFERENCES Category(Categoryid),
    FOREIGN KEY (Itemid) REFERENCES Items(Itemid)
);

INSERT INTO Sales (Itemid, Categoryid, QuantitySold) VALUES
('PH01', 'CTPH01', 5),
('PH02', 'CTPH01', 8),
('PH03', 'CTPH01', 3),
('LP01', 'CTLP01', 2),
('LP02', 'CTLP01', 4),
('LP03', 'CTLP01', 6),
('AS01', 'CTAS01', 10),
('AS02', 'CTAS01', 7),
('AS03', 'CTAS01', 9),
('PH04', 'CTPH01', 6);

CREATE TRIGGER UpdateLastUpdate
BEFORE UPDATE ON Sales
FOR EACH ROW
SET NEW.LastUpdate = NOW();

## ---------------- DataBase Manager ----------------

CREATE TABLE DBManager(UserId VARCHAR(30) PRIMARY KEY,
					   UserPassword INT 
) ;

INSERT INTO DBManager (UserId, UserPassword) VALUES
('Manager01', FLOOR(RAND() * 9000000) + 1000000),
('manager02', FLOOR(RAND() * 9000000) + 1000000);


SELECT * FROM STOCK ;
SELECT * FROM ITEMS ;
SELECT * FROM SALES ;
SELECT * FROM DISCOUNT;
SELECT * FROM DBMANAGER ;