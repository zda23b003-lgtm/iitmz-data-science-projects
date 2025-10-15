-- data.sql

-- Customers
INSERT INTO Customers(customer_id,name,phone_number,delivery_location )
VALUES (1, 'Ahlam Said', '0712000000', 'Mlandege'),(2, 'Amina Sadiq', '0713000000', 'Kikwajuni'),(3, 'Ajmal Said', '0714000000', 'Muembeni'),
(4, 'Shuwena Said', '0715000000', 'Kariakoo'),(5, 'Salim Said', '0716000000', 'Kigamboni'),(6, 'Ahlam Said', '0717000000', 'Mlandege'),(7, 'Afnan Said', '0718000000', 'Pemba'),
(8, 'Ahmad Said', '0718000000', 'Fuoni'),(9, 'Suleiman Said', '0719000000', 'Tunguu'),(10, 'Suheyl Said', '0721000000', 'Mbeya'),
(11, 'Fhardy khamis', '0722000000', 'Shinyanga'),(12, 'Zuwena Kassim', '0812000000', 'Kiyanga');

-- Product Categories
INSERT INTO ProductCategories( category_id,category_name,description)
VALUES (1, 'Cakes', 'All types of cakes'), (2, 'Cupcakes', 'Delicious cupcakes'),(3, 'Cookies', 'Crunchy cookies');
select * from ProductCategories;

-- Products
INSERT INTO Products(product_id ,product_name,category_id ,base_price)
VALUES (1, 'Chocolate Cake', 1, 20000),(2, 'Vanilla Cupcake', 2, 5000),
(3, 'Red Velvet Cake', 1, 22000),
 (4, 'Strawberry Cupcake', 2, 6000),
(5, 'Butter Cookies', 3, 3000),
 (6, 'Black Forest Cake', 1, 25000),
 (7, 'Lemon Cupcake', 2, 5500),
 (8, 'Chocolate Cookies', 3, 3500),
(9, 'Carrot Cake', 1, 21000),
 (10, 'Vanilla Cookies', 3, 2800),
 (11, 'Fruit Cake', 1, 23000),
 (12, 'Mango Cupcake', 2, 5800);

-- Customizations
INSERT INTO Customizations(customization_id ,topping ,design_type ,size)
VALUES (1, 'Strawberry', 'Heart', 'Large'),
 (2, 'Chocolate', 'Round', 'Small'),
 (3, 'Vanilla', 'Square', 'Medium'),
(4, 'Mango', 'Oval', 'Large'),
 (5, 'Blueberry', 'Star', 'Small'),
 (6, 'Mixed Fruit', 'Rectangle', 'Large'),
 (7, 'Orange', 'Triangle', 'Medium'),
 (8, 'Lemon', 'Round', 'Large'),
 (9, 'Banana', 'Heart', 'Small'),
 (10, 'Peach', 'Square', 'Medium'),
 (11, 'Grape', 'Oval', 'Large'),
 (12, 'Raspberry', 'Star', 'Small');

-- Orders
INSERT INTO Orders(order_id ,customer_id ,order_date ,total_amount)
VALUES (1, 1, '2025-06-01', 25000),
 (2, 2, '2025-06-05', 30000),
 (3, 3, '2025-06-07', 28000),
 (4, 4, '2025-06-10', 5000),
 (5, 5, '2025-06-12', 5500),
 (6, 6, '2025-06-14', 22000),
(7, 7, '2025-06-16', 8000),
 (8, 8, '2025-06-18', 12000),
 (9, 9, '2025-06-20', 25000),
 (10, 10, '2025-06-21', 15000),
 (11, 11, '2025-06-23', 23000),
(12, 12, '2025-06-25', 18000);

-- OrderDetails
INSERT INTO OrderDetails(order_detail_id ,order_id ,product_id ,customization_id,quantity,unit_price)
VALUES (1, 1, 1, 1, 1, 20000),
 (2, 2, 2, 2, 2, 5000),
 (3, 3, 3, 3, 1, 22000),
 (4, 4, 4, 4, 1, 6000),
(5, 5, 7, 5, 1, 5500),
 (6, 6, 6, 6, 1, 25000),
 (7, 7, 8, 7, 2, 7000),
(8, 8, 5, 8, 3, 9000),
(9, 9, 9, 9, 1, 21000),
 (10, 10, 10, 10, 2, 5600),
(11, 11, 11, 11, 1, 23000),
 (12, 12, 12, 12, 1, 5800);

-- Materials
INSERT INTO Materials (material_id,material_name ,unit ,quantity_in_stock)
VALUES (1, 'Flour', 'Kg', 50),
(2, 'Sugar', 'Kg', 30),
(3, 'Eggs', 'Dozen', 20),
 (4, 'Butter', 'Kg', 25),
 (5, 'Milk', 'Litre', 40),
 (6, 'Cocoa Powder', 'Kg', 15),
 (7, 'Vanilla Essence', 'Litre', 10),
 (8, 'Strawberry', 'Kg', 12),
 (9, 'Chocolate Chips', 'Kg', 18),
 (10, 'Fruits Mix', 'Kg', 14),
 (11, 'Baking Powder', 'Kg', 8),
 (12, 'Lemon', 'Kg', 10);

-- ProductMaterials
INSERT INTO ProductMaterials(product_id ,material_id ,quantity_required)
VALUES (1, 1, 2),(1, 2, 1),(2, 1, 1),
 (2, 2, 1),(3, 1, 2),(3, 3, 1),
 (4, 1, 1),(4, 8, 1),(5, 1, 1),
(5, 2, 1),(6, 1, 2),(6, 6, 1);

-- DeliveryExecutives
INSERT INTO DeliveryExecutives(executive_id ,name,phone_number)
VALUES (1, 'Ali Bakari', '0714000000'),
(2, 'Hussein Omar', '0715000000'),
 (3, 'Zubeda Said', '0716000000');

-- Deliveries
INSERT INTO Deliveries(delivery_id ,order_id ,delivery_executive_id ,delivery_location ,delivery_charge)
VALUES (1, 1, 1, 'Mlandege', 3000),
(2, 2, 1, 'Kikwajuni', 4000),
 (3, 3, 2, 'Mazizini', 3000),
 (4, 4, 3, 'Magomeni', 2000),
 (5, 5, 1, 'Kisauni', 3500),
(6, 6, 2, 'Mwembe Makumbi', 3000),
 (7, 7, 3, 'Vikokotoni', 2500),
 (8, 8, 1, 'Malindi', 3500),
(9, 9, 2, 'Fumba', 4000),
 (10, 10, 3, 'Kibweni', 2500),
 (11, 11, 1, 'Welezo', 3000),
 (12, 12, 2, 'Kilimahewa', 2800);

-- Feedback
INSERT INTO Feedback(feedback_id ,order_id ,rating ,comment)
VALUES (1, 1, 5, 'Delicious and on time!'),
 (2, 2, 4, 'Good cake but a bit late.'),
(3, 3, 5, 'Excellent service!'),
 (4, 4, 3, 'Cake was okay, could improve.'),
 (5, 5, 4, 'Loved the customization.'),
(6, 6, 5, 'Perfect delivery, well packaged.'),
 (7, 7, 4, 'Good, but the delivery was slow.'),
 (8, 8, 3, 'Taste was average.'),
(9, 9, 5, 'Fantastic cake and fast delivery!'),
 (10, 10, 4, 'Tasty cookies, will order again.'),
 (11, 11, 5, 'Great work, highly recommended!'),
(12, 12, 4, 'Very good, arrived on time.');




