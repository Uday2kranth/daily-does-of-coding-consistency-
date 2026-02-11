TRUNCATE superstore_orders;
COPY superstore_returns
FROM 'D:\sem3\excel\SuperStoreUS-orders.csv'
DELIMITER ',' 
CSV HEADER;
COPY superstore_returns
FROM 'D:\sem3\excel\SuperStoreUS-returns.csv'
DELIMITER ',' 
CSV HEADER;
COPY superstore_users
FROM 'D:\sem3\excel\SuperStoreUS-users.csv'
DELIMITER ',' 
CSV HEADER;

-- Table 1: SuperStore Orders
CREATE TABLE superstore_orders (
    "Row_ID" INTEGER,
    "Order_Priority" VARCHAR(255),
    "Discount" DECIMAL(10, 2),
    "Unit_Price" DECIMAL(10, 2),
    "Shipping_Cost" DECIMAL(10, 2),
    "Customer_ID" INTEGER,
    "Customer_Name" VARCHAR(255),
    "Ship_Mode" VARCHAR(255),
    "Customer_Segment" VARCHAR(255),
    "Product_Category" VARCHAR(255),
    "Product_Sub_Category" VARCHAR(255),
    "Product_Container" VARCHAR(255),
    "Product_Name" VARCHAR(255),
    "Product_Base_Margin" DECIMAL(10, 2),
    "Country" VARCHAR(255),
    "Region" VARCHAR(255),
    "State_or_Province" VARCHAR(255),
    "City" VARCHAR(255),
    "Postal_Code" INTEGER,
    "Order_Date" DATE,
    "Ship_Date" DATE,
    "Profit" DECIMAL(10, 2),
    "Quantity_ordered_new" INTEGER,
    "Sales" DECIMAL(10, 2),
    "Order_ID" INTEGER
);

-- Table 2: Returns
CREATE TABLE superstore_returns (
    "Order_ID" INTEGER,
    "Status" VARCHAR(255)
);

-- Table 3: Users (Managers)
CREATE TABLE superstore_users (
    "Region" VARCHAR(255),
    "Manager" VARCHAR(255)
);

select count(*) from superstore_orders;
-- consumer_complaints data set 
CREATE TABLE consumer_complaints (
    date_received DATE,
    product_name VARCHAR(255),
    sub_product VARCHAR(255),
    issue VARCHAR(255),
    sub_issue VARCHAR(255),
    consumer_complaint_narrative TEXT,
    company_public_response TEXT,
    company VARCHAR(255),
    state_name VARCHAR(50),
    zip_code VARCHAR(20),
    tags VARCHAR(100),
    consumer_consent_provided VARCHAR(50),
    submitted_via VARCHAR(50),
    date_sent_to_company DATE,
    company_response_to_consumer VARCHAR(255),
    timely_response VARCHAR(10),
    consumer_disputed VARCHAR(10),
    complaint_id BIGINT PRIMARY KEY
);
TRUNCATE consumer_complaints;
COPY consumer_complaints 
FROM 'D:\sem3\excel\P9-ConsumerComplaints.csv'
DELIMITER ',' 
CSV HEADER;


SELECT cOUNT(*) FROM consumer_complaints;