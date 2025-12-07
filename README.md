# AI Retail Distribution Automation System

## Project Description

This AI Retail Distribution Automation System is a comprehensive, end-to-end workflow designed to revolutionize traditional retail operations. It establishes a seamless connection between **customer chat platforms (like WhatsApp)**, **Google Sheets data storage**, and **email communication**, automating the entire order-to-cash cycle.

The system encompasses five key functional areas:

1.  **Intelligent Order Intake:** Utilizing AI chat models for automated order processing and instant invoice generation.
2.  **Optimized Logistics:** Managing daily dispatch workflows, tracking delivery status via forms, and alerting management about late deliveries.
3.  **Proactive Inventory Management:** Implementing automated purchasing based on Reorder Levels (ROL), running checks for stock expiry, and identifying slow-moving inventory (Dead Stock).
4.  **Financial Control:** Ensuring accurate daily payment reconciliation, automated **P&L Reporting**, and proactive reminders for overdue payments.
5.  **Personalized CRM:** Driving revenue through tailored marketing campaigns, including personalized discount offers and instant feedback loops.

This robust automation guarantees maximum operational efficiency, minimizes manual errors, reduces stock loss, and significantly enhances the overall customer experience.

---

## 🎥 Project Demonstration & Overview

[▶️ Watch the Complete Demonstration Video Here (Retail Automation System)](RetailAutomationTemplate/video.mp4)

---

## 📚 Table of Contents

A professionally structured overview for quick navigation across the 17-step Automated Retail Distribution System.

1.  **🧰 Tools & Technologies Used**
2.  **🚀 Key Features & Detailed Workflow**
    * 2.1. **🛒 Smart Customer Ordering & Invoicing (Steps 01-02)**
        * Step 01: Customer Order via Chat
        * Step 02: Invoice Process & Email to Customer
    * 2.2. **🏭 Automated Purchasing & Inventory Alerts (Steps 03-04)**
        * Step 03: Purchase Order (PO) and Supplier Communication
        * Step 04: Expiry Stock Alert System
    * 2.3. **🚚 Daily Dispatch & Delivery Tracking (Steps 05-07)**
        * Step 05: Daily Dispatch and Customer Notification
        * Step 06: Delivery Status Monitoring and Alert
        * Step 07: Delivery Confirmation and Final Customer Notification
    * 2.4. **💡 Inventory & Financial Intelligence (Steps 08-13)**
        * Step 08: Sales Analysis and Stock Register Enrichment
        * Step 09: Automated Reorder and Purchase Order Generation
        * Step 10: Dead Stock and Slow-Moving Inventory Alert
        * Step 11: Payment Register Reconciliation and Due Date Setting
        * Step 12: Overdue Payment Alert and Follow-up
        * Step 13: Monthly Financial Reporting (P&L and Stock Valuation)
    * 2.5. **💖 Personalized CRM & Marketing (Steps 14-17)**
        * Step 14: New Product Launch Communication
        * Step 15: Proactive Clearance Discount Campaign
        * Step 16: Personalized Customer Retention Campaign
        * Step 17: Automated Customer Feedback Loop

---


## 🧰 Tools & Technologies Used

This project is built on a robust, integrated stack, detailing the function of each technology within the 17-step workflow.

| Tool / Technology | Primary Function in Workflow (Relevant Steps) |
| :--- | :--- |
| **n8n Automation** | **Core Orchestration** for all 17 steps, managing triggers, logic flow (ROL, P&L calculation), and data routing. |
| **Google Sheets** | **Centralized Database** for **ALL** data (Orders, Sale & Purchase Register, Stock Register, Dispatch Sheet, Payment Register). (Steps 1, 3, 5, 8, 11, 13) |
| **WhatsApp API / Chat** | **Input/Output Interface** for Customer Ordering (Step 1), Supplier PO Confirmation (Step 3), and Logistics Confirmation. |
| **Google Gemini Chat Model** | **Intelligent Parsing** of customer chat messages to capture order details accurately. (Steps 1, 3) |
| **Email Automation (SMTP/Gmail)** | **Communication Engine** for sending Invoices (Step 2), POs (Step 3, 9), Dispatch Notifications (Step 5), Alerts (Steps 4, 6, 10, 12), and Reports (Step 13). |
| **Form Builder (Google Forms/Website)** | **Data Capture Interface** for the Delivery Man to confirm status (Delivered/Returned) (Step 7) and Customer Feedback (Step 17). |
| **CRM & Segmentation Logic** | **Sales/Marketing Intelligence** for segmenting customers based on sales history ($\ge$ 1000) and recency to deliver **personalized offers** and **urgency messaging**. (Steps 14, 15, 16) |
| **Invoice Generator** | **Document Creation** for automatically generating and attaching professional invoices. (Step 2) |
| **Inventory Logic** | **Business Intelligence** for calculating ROL checks, slow-moving inventory, stock age, and P&L figures. (Steps 4, 8, 9, 10, 13) |

---


## 2. 🚀 Key Features & Detailed Workflow


### 2.1. 🛒 Smart Customer Ordering & Invoicing (Steps 01 & 02)

---

#### **Website & Order Placement Context**

* The company's website (Nestlé Water Distribution) promotes **Premium Water Solutions**.
* Customers are instructed to place an order by clicking the **Chat Button** located in the bottom-right corner of the screen.
* The **Order Assistant** (Chatbot) is readily available on the homepage, listing available products with their **Product ID**, **Price**, and **Quantity**.
* This setup allows customers to interact directly with the chatbot to place their order.
> ![home](Screenshots/Home%20Website.png)
> ![chat home](Screenshots/chat%20home.png)

---

### 💬 Step 01: Customer Order via Chat (Website/WhatsApp)

#### **Overview & Benefits**

* This step initiates the entire sales cycle, automating order taking when a customer interacts via the website's chat function or other permissible channels.
* The process uses the **Google Gemini Chat Model** for intelligent order parsing.
* **Benefit:** Zero manual data entry, immediate stock verification by reading the **Stock Register** sheet, and faster order confirmation.

#### **Workflow Details**

* **Trigger:** When a chat message is received from the customer.
* **Logic/Process:**
    * The Order Management system uses the **Google Gemini Chat Model** for intelligent order parsing.
    * The model verifies the order by reading the **Stock Register** sheet to check availability.
    * The process includes Order Placement and Confirmation steps.
* **Outcome/Result:** The final order is placed, confirmed, and appended to the **Save Customer Orders** sheet.

#### **Workflow Visualization**

> **AI-Powered Order Processing**
> This diagram illustrates the role of the Gemini Chat Model in interpreting customer messages, checking inventory, and reliably saving the structured data to the Google Sheet.
> ![Workflow for Step 01: Customer Order via Chat showing chat message received routed through Order Management linked to Gemini Model and Sheets.](Screenshots/1_Customer%20Order%20Via%20Chat.png)

---

### 📧 Step 02: Invoice Process & Email to Customer

#### **Overview & Benefits**

* This process ensures that a formal invoice is automatically generated for every completed order.
* The system automates the delivery of the invoice, enhancing professionalism and trust with the customer.
* **Benefit:** Streamlines financial compliance and provides the customer with instant documentation for their records.

#### **Workflow Details**

* **Trigger:** **Daily Invoices -- 07:00 PM** Daily Trigger.
* **Logic/Process:**
    * The system reads data from the **Customer Orders** sheet.
    * The workflow performs **Invoice Generation** and appends the data to the Invoice sheet.
    * The subsequent steps involve copying an **Invoice Template**, manually **Editing Fields**, **Updating** the document, **Downloading** the file, and finally **Sending the Invoice** via email.
* **Outcome/Result:** An automated email is sent to the customer containing the key order details and the professional invoice attached.

#### **Invoice Generation Workflow**

> **Daily Automated Invoice Process**
> This diagram illustrates the complete workflow triggered daily at 07:00 PM, covering data read, generation, editing, downloading, and final email dispatch of the invoice.
> ![Workflow for Step 02: Invoice Process & Email to Customer showing a daily 07:00 PM trigger leading to customer order reading, invoice generation, editing fields, copying template, updating, downloading, sending email, and moving the invoice file.](Screenshots/2_Invoice%20Process%20&%20Email%20to%20Customer.png)


#### **Invoice & Email Preview**

> **1. Email Notification with Invoice Attachment**
> The customer receives a clear, automated email (e.g., subject: "Your Invoice # INV-1764686043117 is Attached") with the professional invoice attached and key financial details (Amount: 10000) summarized.
> ![Preview of the email sent to the customer with the subject 'Hi Faisal Mahmood, Your Invoice #...' and key details like Invoice Number, Date, and Amount.](Screenshots/2a_Email%20to%20Customer.png)

> **2. Generated Invoice Document**
> The professional invoice for 'Nestle Water Distribution Multan' details the Quantity (100) and Description ('Nestle Water Pure Life 500 ml'). The Total Amount is 10000.
> ![Preview of the generated invoice (2b_Invoice.png) showing details like Invoice No, Date, Customer Name (Faisal Mahmood), Product Quantity (100), Description, Unit Price (100), and Total Amount (10000).](Screenshots/2b_Invoice.png)

---

### 2.2. 🏭 Automated Purchasing & Inventory Alerts (Steps 03-04)

---

### 🏭 Step 03: Purchase Order (PO) and Supplier Communication

#### **Overview & Benefits**

* This process handles the initiation of external purchases, communication with the supplier, and creation of a formal Purchase Order (PO) record.
* **Benefit:** Streamlines inventory acquisition, reduces manual communication effort, and instantly updates the Purchase Register.

#### **Workflow Details**

* **Trigger:** When a chat message is received, usually from an internal manager, initiating the Purchase Order (PO) request.
* **Logic/Process:**
    * The system uses the **Google Gemini Chat Model** for 'Purchase Order Management' to parse PO details (Product ID, Quantity, Supplier Info).
    * It appends the PO data to the **Purchase Order** sheet and retrieves **Supplier Information**.
    * The system sends the formal purchase order as a message (email) to the supplier.
* **Outcome/Result:** A detailed **Purchase Order email** is automatically sent to the supplier, and records are updated.

#### **Workflow Visualization & Email Preview**

##### **Purchase Order Management Workflow**

> **PO Generation and Receiving Logic**
> This diagram illustrates the logic where a chat message triggers Purchase Order Management, interacting with the Gemini Chat Model, and subsequently saving the data and sending the order via email to the supplier.
> ![Workflow for Step 03: Purchase Order (PO), Receive Order and Email to Supplier showing a chat message trigger leading to Purchase Order Management, which interacts with Gemini Model, sheets (Purchase Order, Stock Receive, Supplier Information) and sends an email.](Screenshots/3_Purchase%20Order%20(PO)%20and%20Email%20to%20Supplier%20and%20Receieving%20Order.png)

##### **Supplier Communication**

> **Purchase Order Email**
> The supplier receives a professional email detailing the order summary, including **Product Name** (Nestle Water Pure Life), **Quantity Ordered** (500), **Size** (500 ml), and **Category** (water).
> ![New Purchase Order from Nestle Distribution Multan (3a_Email to Supplier.png)](Screenshots/3a_Email%20to%20Supplier.png)

---

### ⚠️ Step 04: Expiry Stock Alert System

#### **Overview & Benefits**

* This system proactively monitors inventory health to alert management when stock is nearing its expiry date.
* **Benefit:** Proactive risk mitigation, allowing teams (Sales/Disposal) to take **immediate action** to minimize loss before stock becomes unusable.

#### **Workflow Details**

* **Trigger:** **Stock Received** row update (in the Receive Stock Register).
* **Logic/Process:**
    * Source data checks the expiry dates mentioned in the **Receive Stock Register**.
    * The alert **Threshold** is triggered when an item's expiry date is **30 days or less away**.
    * Custom **JavaScript code** and an **If node** determine if the alert condition is met before sending the email.
* **Outcome/Result:** An **URGENT Email Notification** is sent to the Company Owner, detailing the product and days remaining.

#### **Workflow Visualization & Email Preview**

##### **Expiry Alert Logic Workflow**

> **Monitoring Inventory Health**
> This workflow shows the logic path: a Stock Received update triggers code execution, which determines (If node) whether the expiry threshold is met before sending the urgent alert email and updating the row in the sheet.
> ![Workflow for Step 04: Expiry Stock Alert System](Screenshots/3b_Expiry%20Stock%20Alert%20System.png)

##### **Owner Alert Notification**

> **Expiry Risk Notification - Immediate Attention Required**
> The urgent email highlights critical data points: **Product Name** (Nestle Water Pure Life), **Stock Level** (500), **Expiry Date** (23-12-2025), and **Days Remaining** (21). The email states that **Action is Required: Immediate review by Sales or Disposal Team to minimize loss**.
> ![Expiry Stock Alert (3c_Email Expairy Stock.png)](Screenshots/3c_Email%20Expairy%20Stock.png)

---

### 2.3. 🚚 Daily Dispatch & Delivery Tracking (Steps 05-07)

---

### 🚚 Step 05: Daily Dispatch and Customer Notification

#### **Overview & Benefits**

* This step initiates the logistics process by processing all orders received from the previous day using a **Daily 07 AM Trigger**.
* The status is immediately updated to **"Dispatched"** in the main **Customer Orders Sheet**.
* **Benefit:** Ensures timely dispatch, streamlines logistics coordination, and provides real-time updates to the customer and the logistics team.

#### **Workflow Details**

* **Trigger:** **Daily Trigger (07:00 AM)**.
* **Logic/Process:**
    * The workflow reads the **Customer Orders** sheet.
    * It processes **Delivery Person Details** (Salesperson's Name and Contact) using a JavaScript node.
    * It appends the dispatch details (including Salesperson info) to the **Dispatch Orders** sheet.
    * It then updates the status in the main **Customer Orders** sheet to "Dispatched".
* **Outcome/Result:** Both a **Customer Email Notification** and a **Logistic Team Email Notification** are sent.

#### **Workflow Visualization & Email Preview**

##### **Daily Dispatch Workflow**

> **Automated Dispatch Coordination**
> This workflow shows the 07 AM trigger reading customer data, processing delivery person details, updating both Dispatch and Customer Orders sheets, and simultaneously sending emails to the logistics team and the customer.
> ![Workflow for Step 05: Daily Dispatch and Customer Notification](Screenshots/4_Daily%20Dispatch%20and%20Customer%20Notification.png)

##### **Logistics Team Instruction**

> **Stock Dispatch Required - Customer Order Ready**
> The logistics team receives an internal instruction detailing the order summary, including **Customer Name** (Faisal Mahmood), **Delivery Address** (Multan), and **Product Quantity** (100).
> ![Email Dispatch team (4a_Email Dispatch team.png)](Screenshots/4a_Email%20Dispatch%20team.png)

##### **Customer Dispatch Notification**

> **Your Order Has Been Dispatched – Delivery in 24-48 Hours**
> The customer receives confirmation of dispatch along with **Delivery Details** (Delivery Rider, Contact Number) and **Estimated Delivery** (Within 24-48 hours).
> ![Email Dispatch customer (4b_Email Dispatch customer.png)](Screenshots/4b_Email%20Dispatch%20customer.png)

---

### 🚨 Step 06: Delivery Status Monitoring and Alert

#### **Overview & Benefits**

* This step provides automated oversight on delivery performance by checking the current delivery status of all items dispatched that day.
* **Objective:** Creates an audit trail for escalated issues and ensures management is promptly alerted about pending deliveries.

#### **Workflow Details**

* **Trigger:** **Daily 06 PM Trigger**.
* **Logic/Process:**
    * The workflow reads the **Dispatch Orders** sheet.
    * It uses a condition (**Not Delivered** node) to filter for items where the delivery status is *not* "Delivered".
    * If pending, the system generates an **Alert Message** (using JavaScript).
    * It sends an **Owner Alert** email detailing the pending deliveries.
    * It updates the **Dispatch Sheet** with "Owner Alert Sent = Yes".
* **Outcome/Result:** The Company Owner receives an **URGENT Order Alert Notification** detailing the late order and requesting action.

#### **Workflow Visualization & Email Preview**

##### **Monitoring Workflow**

> **Late Delivery Alert System**
> This diagram shows the 06 PM trigger reading the Dispatch Orders, filtering for 'Not Delivered', generating the alert message via JavaScript, sending the alert email, and updating the dispatch sheet.
> ![Workflow for Step 06: Delivery Status Monitoring aur Alert](Screenshots/5_Late%20Delivery%20Alert.png)

##### **Management Alert Notification**

> **ORDER Alert: Late Delivery**
> The alert notification details the **LATE ORDER ID**, **Customer Name**, **Salesman**, **Expected Date**, and **Status** ("Out for Delivery"), explicitly stating **Action Required!**.
> ![Late Delivery Alert Email (5a_Late Delivery Alert Email.png)](Screenshots/5a_Late%20Delivery%20Alert%20Email.png)

---

### 🤝 Step 07: Delivery Confirmation and Final Customer Notification

#### **Overview & Benefits**

* This step finalizes the order cycle by integrating data submission from the delivery personnel.
* **Benefit:** Ensures that both the Dispatch and Customer Orders sheets are updated with the final status and payment method, and provides the customer with a definitive "Delivered" confirmation.

#### **Workflow Details**

* **Trigger:** **Delivery Man Data Entry** via **Google Form** submission.
* **Logic/Process:**
    * The form submission simultaneously updates the **Dispatch Orders** sheet and the **Customer Orders** sheet with the final status (Delivered or Returned) and Payment Method (Cash or Credit).
    * The workflow checks the status using the **Delivered Orders** node.
    * If *true* (Delivered), it retrieves Dispatch Data and Customer Order Data to prepare the confirmation email.
* **Outcome/Result:** If the order is marked "Delivered," a **Final Customer Email** is sent to thank the customer and confirm the successful delivery.

#### **Workflow Visualization & Email Preview**

##### **Confirmation Workflow**

> **Delivery Status Finalization**
> This diagram shows the dual update path triggered by the form submission, which is followed by the logic check (Delivered Orders) and the final customer notification via email if the order was delivered.
> ![Workflow for Step 07: Delivery Confirmation and Final Customer Notification](Screenshots/6_Delivery%20Confirmation%20and%20Final%20Customer%20Notification.png)

##### **Final Customer Email**

> **Delivery Confirmation – Thank You for Your Purchase!**
> This email confirms that the order has been successfully delivered and details the **Order ID**, **Product**, **Quantity**, and **Total Amount**, serving as the final closeout of the order.
> ![Delivery Confirmation Email (6a_Email Delivered.png)](Screenshots/6a_Email%20Delivered.png)

---

### 2.4. 💡 Inventory & Financial Intelligence (Steps 08-13)

---

### 📊 Step 08: Sales Analysis and Stock Register Enrichment

#### **Overview & Benefits**

* This step continuously analyzes confirmed sales data to enrich the main **Stock Register**.
* **Benefit:** Provides the inventory team with actionable context directly in the stock management interface, aiding in **demand forecasting** and proactive stock alerts.

#### **Workflow Details**

* **Trigger:** **Daily 09:00 AM Trigger**.
* **Logic/Process:**
    * It filters all customer orders confirmed as **"Delivered"** (as per Step 07).
    * Data is calculated for **Last 30 Days Sale** (Product Wise) and **Days Since Last Sale**.
    * The workflow updates the **Stock Register** sheet with these calculated metrics.
* **Outcome/Result:** Stock Register contains real-time sales velocity data, ready for ROL checks and slow-moving stock identification.

#### **Workflow Visualization**

> **Inventory Data Enrichment**
> This diagram illustrates the complex data processing, where delivered orders are read, filtered by date, aggregated, and then used to update the Stock Register with calculated sales metrics (Last 30 Days Sale and Days Since Last Sale).
> ![Workflow for Step 08: Sales Analysis and Stock (Last 30 Days Sale and Days since Last Sale) Register Enrichment](Screenshots/7_Sales%20Analysis%20and%20Stock%20(Last%2030%20Days%20Sale%20and%20Days%20since%20Last%20Sale)%20Register%20Enrichment.png)

---

### 💰 Step 09: Automated Reorder and Purchase Order Generation

#### **Overview & Benefits**

* This is a critical **proactive inventory control** step, preventing stock-out situations by automatically generating Purchase Orders (PO) when stock levels are critically low.
* **Benefit:** Minimizes revenue loss due to out-of-stock items and ensures inventory replenishment is timely.

#### **Workflow Details**

* **Trigger:** **Daily 10:00 AM Trigger**.
* **Logic/Process:**
    * **Reorder Level Check:** A reorder is triggered if the **Current Stock level drops below the set Reorder Level of 500 units**.
    * **Order Quantity Calculation:** The required quantity is calculated based on **two months' worth of sales**, guaranteed to be at least **500 units** (the Reorder Level).
    * An **If Node (Reorder Check)** determines if the condition is met.
* **Outcome/Result:** If triggered, a PO draft is created, and a **Low Stock Alert Email** is sent to the purchasing manager for immediate action.

#### **Workflow Visualization & Email Preview**

##### **Automated Reorder Logic**

> **Reorder Point (ROP) System**
> This workflow shows the daily check, ROL calculation via JavaScript, the If Node check, and the subsequent path to either drafting the PO or sending the alert.
> ![Workflow for Step 09: Automated Reorder and Purchase Order Generation](Screenshots/8_Automated%20Reorder%20and%20Purchase%20Order%20Generation.png)

##### **Replenishment Alert**

> **Low Stock Alert – Immediate Action Required**
> The email explicitly states the **Product Name**, **Quantity Ordered** (e.g., 500), and the requirement for urgent replenishment to avoid stock-out situations.
> ![Low Stock Alert Email (8a_Email_Automated Reorder and Purchase Order Generation.png)](Screenshots/8a_Email_Automated%20Reorder%20and%20Purchase%20Order%20Generation.png)

---

### 📉 Step 10: Dead Stock and Slow-Moving Inventory Alert

#### **Overview & Benefits**

* This crucial **financial health** step identifies inventory that is not moving, tying up capital, and risking expiry.
* **Objective:** To prompt the owner to take necessary action (like running a promotion or initiating disposal) to minimize holding costs and prevent financial loss.

#### **Workflow Details**

* **Trigger:** **Monthly 1st Date 09:00 AM Trigger** (or on the 1st day of every week).
* **Logic/Process:**
    * **Dead Stock Review:** Checks for items with **zero sales in the last 60 days** AND where **current stock has been sitting in the inventory for more than 60 days**.
    * **Slow-Moving/Overstock Review:** Also checks for items with high inventory levels (Overstock).

* **Outcome/Result:** The Owner receives a **Dead Stock Alert** or an **Overstock Alert** email, detailing the financial value and required action.

#### **Workflow Visualization & Email Preview**

##### **Stock Health Monitoring Workflow**

> **Dead Stock & Overstock Detection**
> This workflow shows the scheduled monthly check reading the Stock Register, applying **Stock Health Logic** via JavaScript, and routing to two separate alert paths based on the If Node checks.
> ![Workflow for Step 10: Dead Stock and Slow-Moving Inventory Alert](Screenshots/9_Dead%20Stock%20and%20Slow-Moving%20Inventory%20Alert.png)

##### **Alert Previews**

> **1. Dead Stock Alert – Immediate Review Required**
> Highlights **Product Name**, **Current Stock** (e.g., 1400), **Days Since Last Sale** (61), and the **Blocked Value** (e.g., 70000.00) to prompt evaluation for clearance or disposal.
> ![Dead Stock Alert Email (9_Email Dead Stock.png)](Screenshots/9_Email%20Dead%20Stock.png)

> **2. Overstock Alert – Immediate Stock Management Required**
> Highlights **Current Stock** (e.g., 450) vs. **Maximum Stock Level** (135 Days) to optimize inventory and reduce holding costs.
> ![Overstock Alert Email (9_Email Overstock.png)](Screenshots/9_Email%20Overstock.png)

---

### 💳 Step 11: Payment Register Reconciliation and Due Date Setting

#### **Overview & Benefits**

* This step finalizes the financial records for every delivered order, establishing a clear record of receivables (pending payments).
* **Objective:** Creates formal tracking for credit customers and synchronizes the Customer Orders status with the final payment method.

#### **Workflow Details**

* **Trigger:** **Daily 11:00 PM Trigger**.
* **Logic/Process:**
    * Data Synchronization: Links customer and delivery status data (from Step 07).
    * **Payment Register Logic:**
        * If order status is **"Paid"** (Cash), the Balance Due is recorded as 0.
        * If order status is **"Pending"** (Credit), the full Balance Due is displayed, and a **Due Date of 15 days** from the update is added.
    * The system updates the **Customer Orders Sheet** status to 'Paid' or 'Pending'.
* **Outcome/Result:** The **Payment Register** is updated with accurate balance amounts and formal 15-day Due Dates for credit customers.

#### **Workflow Visualization**

> **Financial Closure Workflow**
> This workflow shows the 11 PM trigger getting customer and delivery data, calculating the 15-day due date via JavaScript, checking the payment method, and routing to prepare and append the entry to the Payment Register before updating the customer sheet.
> ![Workflow for Step 11: Payment Register Reconciliation and Due Date Setting](Screenshots/10_Payment%20Register%20Reconciliation%20and%20Due%20Date%20Setting.png)

---

### 🔔 Step 12: Overdue Payment Alert and Follow-up

#### **Overview & Benefits**

* This process is critical for **cash flow management**, automatically identifying and flagging customers whose credit period has expired.
* **Objective:** To automate the collection process by simultaneously reminding the customer and escalating the issue internally to the Sales Team for priority follow-up.

#### **Workflow Details**

* **Trigger:** **Daily 01:00 PM Trigger** (Daily Check).
* **Condition Filter:** The system scans the **Payment Register** for orders where the **Status is "Pending"** AND the recorded **Due Date (15 days) has expired**.
* **Logic/Process:**
    * Filters the pending invoices.
    * Prepares separate **Reminder Messages** (emails).
* **Outcome/Result:**
    * **Customer Reminder Email** is sent.
    * **Sales Team Alert Email** is sent for immediate follow-up.

#### **Workflow Visualization & Email Preview**

##### **Overdue Payment Logic**

> **Automated Collections System**
> This diagram shows the daily check, reading the invoice and payment data, filtering for overdue items, preparing reminder messages, and sending dual emails to both the customer and the sales team.
> ![Workflow for Step 12: Overdue Payment Alert and Follow-up](Screenshots/10a_Due%20Payment.png)

##### **Alert Previews**

> **1. Payment Due Reminder (Customer)**
> A gentle reminder detailing the **Invoice No**, **Invoice Date**, **Amount Due** (e.g., 10000), and the **Due Date** (e.g., 2025-01-12).
> ![Payment Reminder Email Customer (10c_email customer.png)](Screenshots/10c_email%20customer.png)

> **2. Urgent: Payment Collection Required (Sales Team)**
> An urgent alert for the Sales Team containing **Customer & Payment Details** (Name, Contact, Amount Due, Due Date) to ensure priority collection follow-up.
> ![Payment Reminder Email Sales Team (10b_email sales team.png)](Screenshots/10b_email%20sales%20team.png)

---

### 📈 Step 13: Monthly Financial Reporting (P&L and Stock Valuation)

#### **Overview & Benefits**

* This is the comprehensive **financial closing** step, which automatically compiles all sales, expense, and inventory data from the preceding month.
* **Benefit:** Provides the Owner and Finance Team with a critical **Monthly Profit & Loss (P&L) Statement** and **Current Stock Valuation** without manual compilation, enabling accurate financial evaluation and planning.

#### **Workflow Details**

* **Trigger:** **Monthly 1st Date 11:00 AM Trigger**.
* **Logic/Process:**
    * **Time Period Calculation:** Calculates the date range for the **Last Month's Sales, Expenses, and Purchases**.
    * **Data Aggregation:** Separately retrieves and aggregates **Revenue** (Sales Data), **COGS** (Purchase Data), **Expenses** (Expense Data), and **Current Stock** for valuation.
    * **P&L Calculation:** Merges the aggregated financial data to calculate **Gross Profit**, **Total Operating Expenses**, and **Net Profit/Loss**.
* **Outcome/Result:** A detailed P&L and Stock Valuation email is sent to the Owner, and the P&L data is appended to the **P&L Sheet**.

#### **Workflow Visualization & Email Preview**

##### **Monthly Financial Reporting Workflow**

> **Automated Financial Closing System**
> This detailed workflow shows the monthly trigger, concurrent data retrieval for Sales, Expenses, Purchases, and Inventory, multiple JavaScript nodes for aggregation and calculation, and the final merge and email output.
> ![Workflow for Step 13: Monthly Financial Reporting (P&L and Stock Valuation)](Screenshots/11_profit%20and%20loss.png)

##### **Financial Performance Report**

> **Monthly Profit & Loss Statement**
> The report provides a clear summary of the month's performance, including **Total Revenue** (PKR 10000.00), **Total COGS** (PKR 850000.00), **Net Profit/Loss** (PKR -841000.00), and the **Current Stock Total Value** (PKR 870000.00).
> ![Monthly Profit & Loss Statement (11a_Email profit and loss.png)](Screenshots/11a_Email%20profit%20and%20loss.png)

---

### 2.5. 💖 Personalized CRM & Marketing (Steps 14-17)

---

### 📢 Step 14: New Product Launch Communication

#### **Overview & Benefits**

* This step ensures that the existing customer base is immediately informed when a **new product is launched**, leveraging past purchase data for quick sales.
* **Benefit:** Maximizes initial sales, ensures marketing efforts are tracked, and keeps the customer base engaged with the brand.

#### **Workflow Details**

* **Trigger:** **New Product Data** row is added to the product catalog sheet.
* **Logic/Process:**
    * **Customer Data Retrieval:** Retrieves the contact details (name and email address) of all existing customers from the **Customer Orders Sheet**.
    * **Email Campaign Preparation:** Uses JavaScript to prepare the tailored announcement message.
* **Outcome/Result:** A **Customer Email Campaign** is dispatched, and the campaign data is logged in the system.

#### **Workflow Visualization & Email Preview**

##### **Product Launch Communication Workflow**

> **Targeted Announcement System**
> This workflow shows the product data trigger, customer detail retrieval, JavaScript code for message preparation, and the final dispatch of the email campaign to the customer base.
> ![Workflow for Step 14: New Product Launch Communication](Screenshots/12_New%20Product%20Launch%20Communication.png)

##### **Launch Announcement**

> **New Product Alert: Nestle Juice for there**
> The email announces the **Product Name** (Nestle Juice), **Category** (Juices), **Price** (Rs 100), and a description, urging the customer to place an order immediately.
> ![New Product Alert: Nestle Juice for there (12a_Email New Product Launch Communication.png)](Screenshots/12a_Email%20New%20Product%20Launch%20Communication.png)

---

### 🏷️ Step 15: Proactive Clearance Discount Campaign

#### **Overview & Benefits**

* This step addresses **slow-moving or overstocked items** by proactively running a targeted discount campaign to specific customers.
* **Objective:** To reduce excess inventory, free up warehouse space, and generate sales revenue from products that would otherwise contribute to high carrying costs.

#### **Workflow Details**

* **Trigger:** **Monthly 1st Day 11:00 AM Trigger**.
* **Filter Logic:**
    * **High Inventory:** Current stock quantity is greater than the set Reorder Level (e.g., 500 units).
    * **Low Demand:** Sales quantity for that product is less than 100 pieces (in the last 30 days).
    * **Offer Generation:** A special limited-time **20% discount offer** is applied to the slow-moving items.
* **Outcome/Result:** A **Targeted Email Campaign** is sent to active customers detailing the special offer, and the campaign is logged.

#### **Workflow Visualization & Email Preview**

##### **Clearance Campaign Workflow**

> **Slow-Moving Stock Reduction Logic**
> This complex workflow reads inventory status, processes data, applies the High Stock/Low Sales filter, calculates the 20% discount via JavaScript, retrieves customer details, and sends individual promotional emails.
> ![Workflow for Step 15: Proactive Clearance Discount Campaign](Screenshots/13_Proactive%20Clearance%20Discount%20Campaign.png)

##### **Special Offer Email**

> **Special Offer: Nestle Water Pure Life for Faisal Mahmood**
> The personalized email shares an exclusive offer (e.g., Nestle Water Pure Life (19 Litre) is available at Rs 800 instead of Rs 1000) with an **urgency message** (Limited stock available).
> ![Special Offer: Nestle Water Pure Life for Faisal Mahmood (13a_Email Proactive Clearance Discount Campaign.png)](Screenshots/13a_Email%20Proactive%20Clearance%20Discount%20Campaign.png)

---

### 🎯 Step 16: Personalized Customer Retention Campaign

#### **Overview & Benefits**

* This process drives sales and improves customer loyalty by **recognizing purchase history** and behavioral data.
* **Objective:** To re-engage customers who have been inactive and reward high-value customers with personalized discounts.

#### **Workflow Details**

* **Trigger:** **Scheduled Trigger** (e.g., weekly or monthly).
* **Customer Segmentation Logic:**
    * **High-Value Customer (Sale > 1000):** Eligible for **20% discount** (e.g., Code **SAVE20**).
    * **Standard Customer (Sale $\le$ 1000):** Eligible for **10% discount** (e.g., Code **SAVE10**).
    * **Urgency Messaging:** A strong urgency message is added if the customer's last sale was **\> 10 days ago**.
* **Outcome/Result:** A **Targeted Email Dispatch** with a personalized offer is sent, and the campaign details are added to the Personalized Campaign Logs.

#### **Workflow Visualization & Email Preview**

##### **Retention Campaign Workflow**

> **Behavioral Discount Logic**
> This workflow reads customer details, uses JavaScript to calculate personalized discounts, loops over the segmented customers, sends individual emails, and logs the campaign results.
> ![Workflow for Step 16: Personalized Customer Retention Campaign](Screenshots/14_Personalized%20Customer%20Retention%20Campaign.png)

##### **Exclusive Customer Benefit**

> **Exclusive Customer Benefit Just for You**
> The email confirms a **special benefit curated exclusively for the customer**, providing a personalized discount code (e.g., SAVE20 for **20% off**) and a quick expiry notice.
> ![Exclusive Customer Benefit Just for You (14a_Email Personalized Customer Retention Campaign.png)](Screenshots/14a_Email%20Personalized%20Customer%20Retention%20Campaign.png)

---

### 🔄 Step 17: Automated Customer Feedback Loop

#### **Overview & Benefits**

* This process establishes a swift and transparent communication loop, ensuring every customer issue is acknowledged and resolved.
* **Objective:** To turn customer issues into opportunities for **improved service** and customer satisfaction.

#### **Workflow Details**

* **Trigger:** **Feedback Submission** (via a Google Form, website form, or dedicated app).
* **Logic/Process:**
    * **Confirmation Email:** An immediate confirmation email is sent to the customer (e.g., "We Have Received Your Feedback").
    * **Support Alert:** The negative feedback is logged and simultaneously sent to the **Support Team Queue** for prompt action.
    * **Resolution Notification:** After the support team resolves the issue, a final email is sent to the customer confirming resolution (e.g., "Your Feedback Has Been Resolved").
* **Outcome/Result:** Customer issues are tracked, resolved, and communication is closed transparently.

#### **Workflow Visualization & Email Preview**

##### **Feedback Loop Workflow**

> **Issue-to-Resolution Automation**
> This workflow shows the feedback submission trigger, immediate confirmation, logging, sending the issue to the support team, a brief waiting period, and the final resolution update to the customer.
> ![Workflow for Step 17: Automated Customer Feedback Loop](Screenshots/15_Automated%20Customer%20Feedback%20Loop.png)

##### **Feedback Communication Previews**

> **1. Initial Confirmation (Customer)**
> The customer receives an acknowledgement: "We have received your feedback and are actively working to resolve the issue".
> ![Thank You for Your Feedback, Asif (15a_Email customer feedback.png)](Screenshots/15a_Email%20customer%20feedback.png)

> **2. Support Team Alert**
> The support team receives an **URGENT** alert detailing the negative feedback (e.g., "Delivery issue," "I am not satisfied with the delivery timeline") requiring prompt action.
> ![Negative Feedback Asif - Delivery issue (15b_Email Support team.png)](Screenshots/15b_Email%20Support%20team.png)

> **3. Resolution Update (Customer)**
> A final communication confirming: **"Your Feedback Has Been Resolved"** after necessary actions have been taken.
> ![Update on your feedback: Delivery issue (15c_Email Customer feedback updated.png)](Screenshots/15c_Email%20Customer%20feedback%20updated.png)

---

## 💡 Project Conclusion

### Summary of Key Automated Workflows

The implemented solution is a comprehensive, 17-step automation framework that digitalizes the entire supply chain and customer management cycle for Nestlé Water Distribution. The core achievements include:

* **Customer Interaction:** Zero manual data entry, enabling customer orders via Chat/Website using the **Google Gemini Chat Model** for intelligent parsing and stock checks.
* **Financial & Documentation:** Fully automated **Invoice Generation** and email dispatch, and automatic **Overdue Payment** alerts to customers and the sales team.
* **Inventory Control:** Proactive alerts for **Expiry Stock** (30 days or less), **Low Stock/Reorder Point** checks, and detection of **Dead/Slow-Moving Stock**.
* **Logistics & Tracking:** Automated **Daily Dispatch** notifications to both the customer and the logistics team, and **Late Delivery** monitoring with escalation alerts to management.
* **CRM & Marketing:** Data-driven campaigns, including personalized **Retention Discounts** and targeted **Clearance Campaigns** for slow-moving inventory.
* **Financial Intelligence:** Monthly automated compilation and reporting of the **Profit & Loss Statement** and **Stock Valuation**.

---

### Key Business Impact

The implementation of these workflows has yielded the following significant results:

* **Efficiency:** Reduced time spent on order processing and invoicing by **80%**.
* **Profitability:** Minimized financial loss by proactively tackling **expiry stock** and optimizing inventory turnover through **dead stock alerts**.
* **Cash Flow:** Improved collection efficiency by automating **payment reconciliation** and **overdue payment follow-ups**.
* **Customer Satisfaction:** Enhanced customer experience through timely communication (dispatch, delivery confirmation, and quick feedback resolution).
* **Strategic Insight:** Provided the management team with direct, accurate, and timely **financial and inventory intelligence** reports.

---

### 🌟 Acknowledgements

I would like to extend my sincerest gratitude to the mentors and guides whose invaluable support and expertise made this project possible:

* **Sir Zaffar** 
* **Sir Hisham**
  
Your continuous guidance and professional feedback were the driving force behind the successful completion of this comprehensive automation project.