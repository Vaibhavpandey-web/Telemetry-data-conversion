🛰️ Telemetry Data Conversion Dashboard
A private dashboard project built for Daikibo to monitor the real-time health status of 9 machines across 4 factory locations using telemetry data. Developed as part of a Deloitte Australia initiative.

📌 Project Overview
This project aims to visualize machine health using telemetry data collected from Daikibo’s factories. The main goal is to convert raw telemetry into meaningful insights and display them on a secure, user-friendly dashboard.

✅ Key Features
🔧 Real-time telemetry data processing

🏭 Factory-wise machine health status

📊 Custom private dashboards for internal use

🔐 Role-based secure access control

🗂️ Modular and scalable system architecture

🧱 System Architecture
pgsql
Copy
Edit
+-------------------------+
|   Telemetry Collector  |  <- MQTT / HTTP-based
+-------------------------+
            ↓
+-------------------------+
|  Data Converter & ETL   |  <- Converts raw telemetry to readable metrics
+-------------------------+
            ↓
+-------------------------+
|   Central Data Store    |  <- Time-series DB / Cloud Storage
+-------------------------+
            ↓
+-------------------------+
|     Backend Server      |  <- API for dashboard queries
+-------------------------+
            ↓
+-------------------------+
|   Frontend Dashboard    |  <- React / Vue Interface
+-------------------------+
🔐 Security Flow
🔒 OAuth 2.0 or JWT for user authentication

🧑‍💼 Admin vs Viewer roles with restricted access

🔍 Audit logs for every login/session

🌐 Encrypted API communication (HTTPS)

🖥️ Dashboard Preview
Wireframe diagram includes:

Factory selection dropdown

Machine health cards (Red/Green status)

Real-time status updates with timestamp

Alerts panel for anomalies

(Check the /design folder for full wireframes)

🛠️ Tech Stack
Component	Tech Used
Frontend	React.js / Tailwind CSS
Backend	Node.js / Express.js
Database	InfluxDB / MongoDB
Auth & Access	Firebase Auth / JWT
Hosting	AWS / Azure
Visualization	Chart.js / D3.js

🚀 Future Plans
📱 Mobile-friendly version

🧠 AI-based predictive maintenance alerts

📥 CSV / Excel export support

🌍 Multi-language support

🤝 Acknowledgments
This project was created as part of a training project for Deloitte Australia. Special thanks to mentors and the Daikibo team for telemetry data support.

📂 Folder Structure
bash
Copy
Edit
telemetry-dashboard/
├── backend/
├── frontend/
├── design/           # Wireframes, architecture diagrams
├── docs/
└── README.md
📧 Contact
For any questions or contributions, feel free to reach out:

Vaibhav Pandey
📧 vaibhavpandey98477@gmail.com 
💼 vaibhavpandey-web
