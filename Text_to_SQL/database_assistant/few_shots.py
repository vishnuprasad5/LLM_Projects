few_shots = [
    {'Question': "What is the total revenue generated from all sales?",
     'SQLQuery': """
                  SELECT SUM(I.PRICE * S.QUANTITYSOLD) 
                  FROM ITEM AS I INNER JOIN SALES AS S 
                  ON I.ITEMSID = S.ITEMSID ;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "2267039.00"},

    {'Question': "What is the total value of phones currently in stock?",
     'SQLQuery': """
                  SELECT SUM(I.PRICE * S.QUANTITY) 
                  FROM ITEMS AS I INNER JOIN STOCK AS S 
                  ON I.ITEMID = S.ITEMID WHERE I.CATEGORYID = 'CTPH01';
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "52165330.00"},

    {'Question': "What is the total revenue loss due to discounts?",
     'SQLQuery': """
                  SELECT SUM((Price * (Discount / 100)) * QuantitySold) AS TotalRevenueLoss
                  FROM Items
                  JOIN Discount ON Items.Itemid = Discount.Itemid
                  JOIN Sales ON Items.Itemid = Sales.Itemid;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "195106.65"},

    {'Question': "Determine the percentage of revenue contributed by the Phones category to the total revenue.",
     'SQLQuery': """
                 SELECT 
                 ROUND((SUM(Items.Price * Sales.QuantitySold) / 
                 (SELECT SUM(Items.Price * Sales.QuantitySold) FROM Items JOIN Sales ON Items.Itemid = Sales.Itemid)) * 100, 2) 
                 AS PercentageRevenue
                 FROM Items JOIN Sales ON Items.Itemid = Sales.Itemid
                 JOIN Category ON Items.Categoryid = Category.Categoryid
                 WHERE Category.Category = 'Phones';
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "57.66"},

    {'Question': "Can you list all the items with a price higher than a 100000?",
     'SQLQuery': """
                 SELECT CONCAT(ITEMID,':', BRAND,' ', MODELNAME) FROM ITEMS WHERE PRICE > 100000;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "LP08:Samsung Galaxy Book Pro, LP10:Razer Blade 15"},

    {'Question': "Which item has the highest total sales revenue?",
     'SQLQuery': """
                 SELECT CONCAT(i.Itemid,':', i.Brand, ' ', i.ModelName), SUM(i.Price * s.QuantitySold) AS TotalRevenue
                 FROM Items AS i
                 JOIN Sales AS s ON i.Itemid = s.Itemid
                 GROUP BY i.Itemid, i.Brand, i.ModelName
                 ORDER BY TotalRevenue DESC LIMIT 1;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "PH02:Apple iPhone 13, 639200.00"},

    {'Question': "Which item has the highest ratio of sales revenue to stock value",
     'SQLQuery': """
                 SELECT CONCAT(i.Brand, ' ', i.ModelName) AS Item,
                 SUM(s.QuantitySold * i.Price) / SUM(st.Quantity * i.Price) AS Ratio
                 FROM Items AS i
                 JOIN Sales AS s ON i.Itemid = s.Itemid
                 JOIN Stock AS st ON i.Itemid = st.Itemid
                 GROUP BY i.Brand, i.ModelName
                 ORDER BY Ratio DESC
                 LIMIT 1;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Boat Rockerz 450, 0.076190"},

    {'Question': "What are the top three best-selling phones?",
     'SQLQuery': """
                 SELECT CONCAT(i.Brand, " ", i.ModelName), SUM(s.QuantitySold) AS TotalSold
                 FROM Items i
                 JOIN Sales s ON i.Itemid = s.Itemid
                 WHERE i.Categoryid = 'CTPH01'
                 GROUP BY i.Brand, i.ModelName
                 ORDER BY TotalSold DESC
                 LIMIT 3;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Apple iPhone 13, Xiaomi Redmi Note 10 Pro, Samsung Galaxy S21"},

    {'Question': "Which brand has the highest average discount percentage?",
     'SQLQuery': """
                 SELECT i.Brand, AVG(d.Discount) AS AvgDiscountPercentage
                 FROM Items i
                 JOIN Discount d ON i.Itemid = d.Itemid
                 GROUP BY i.Brand
                 ORDER BY AvgDiscountPercentage DESC
                 LIMIT 1;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Xiaomi, 15.000000"},

    {'Question': "What is the total sales revenue for each category?",
     'SQLQuery': """
                 SELECT c.Category, SUM(s.QuantitySold * i.Price) AS TotalRevenue
                 FROM Items i 
                 JOIN Category c ON i.Categoryid = c.Categoryid
                 JOIN Sales s ON i.Itemid = s.Itemid
                 GROUP BY c.Category;
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Accessories: 147968.00, Laptops: 811880.00, Phones: 1307191.00"},

    {'Question': "Can you list phones that haven't been sold yet?",
     'SQLQuery': """
                SELECT i.Brand, i.ModelName
                FROM Items i
                LEFT JOIN Sales s ON i.Itemid = s.Itemid
                WHERE s.Itemid IS NULL AND i.Categoryid = 'CTPH01';
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "Google Pixel 6, Realme GT 5G, Vivo X70 Pro+, Oppo Reno 6 Pro, Nokia G50, Motorola Edge 20, Sony Xperia 5 III"},

    {'Question': "How much percentage of revenue contributed by 12GB RAM phones to phones sales revenue",
     'SQLQuery': """
                SELECT (SUM(s.QuantitySold * i.Price) / (SELECT SUM(s.QuantitySold * i.Price) FROM Items i 
                JOIN Sales s ON i.Itemid = s.Itemid WHERE i.Categoryid = 'CTPH01')) * 100 AS PercentageOfRevenue
                FROM Items i JOIN Sales s ON i.Itemid = s.Itemid
                WHERE i.Categoryid = 'CTPH01' AND i.Specifications LIKE '%12GB RAM%';
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "16.06"},

    {'Question': "How much percentage of revenue contributed by 8GB RAM laptops to total revenue?",
     'SQLQuery': """
                SELECT (SUM(s.QuantitySold * i.Price) / (SELECT SUM(s.QuantitySold * i.Price) FROM Items i JOIN Sales s 
                ON i.Itemid = s.Itemid)) * 100 AS PercentageOfRevenue FROM Items i
                JOIN Sales s ON i.Itemid = s.Itemid WHERE  
                i.Categoryid = 'CTLP01' AND i.Specifications LIKE '%8GB RAM%';
                  """,
     'SQLResult': "Result of the SQL query",
     'Answer': "14.64"}
]