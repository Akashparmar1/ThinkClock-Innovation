# ThinkClock-Innovation



## 📌 Project Overview
This project is a **Python-based Identity Reconciliation System** that processes customer records to identify and merge duplicate entries based on email and phone numbers. The system ensures that each unique customer is assigned a single unique ID.

## 🚀 Features
- Cleans and standardizes customer data.
- Identifies duplicate records using a **graph-based clustering approach**.
- Merges duplicate records under a single **unique customer ID**.
- Outputs a processed dataset with reconciled identities.
``

```
```
## 🛠️ Setup Instructions
``
```
### 1️⃣ Clone the Repository
```
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/identity_reconciliation.git
cd identity_reconciliation
```
```

### 2️⃣ Create a Virtual Environment
For macOS/Linux:
```sh
python -m venv venv
source venv/bin/activate
```
For Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install pandas networkx
```

### 4️⃣ Run the Script
```sh
python identity_reconciliation.py
```

### 5️⃣ Check the Output
```sh
cat resolved_customers.csv
```

## 📊 Example Input (`customers.csv`)
```csv
id,name,email,phone
1,Alice,alice@email.com,1234567890
2,Bob,bob@email.com,9876543210
3,Alice,alice@email.com,1234567890
4,Charlie,charlie@email.com,5556667777
5,Bob,bob@email.com,9876543210
```

## ✅ Example Output (`resolved_customers.csv`)
```csv
original_id,unique_id
1,1
2,2
3,1
4,4
5,2
```
```

## 📝 License
This project is open-source under the **MIT License**.

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request.

---

🚀 **Happy Coding!** Let me know if you need any modifications! 😊
```

