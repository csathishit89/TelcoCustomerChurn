# 💬 Client Query Management System (CQMS)

**A comprehensive web application designed to efficiently track, manage, and resolve client inquiries, ensuring timely and effective communication.**

## ✨ Key Features

* **Query Tracking:** Log and track all client queries from submission to resolution.
* **Status Management:** Assign and update query statuses (e.g., Open, Closed, Resolved Rate).
* **User Roles:** Differentiated access for Clients (submit/view queries) and Support (resolve queries).

## 🛠️ Technologies & Stack

* **Frontend:** [Streamlit / HTML/CSS]
* **Backend:** [Python ]
* **Database:** [PostgreSQL ]
* **Hosting/Deployment:** [AWS / ]

## ⚙️ Installation and Setup

Follow these steps to get a local copy of the CQMS running:

### Prerequisites

* [Python ]
* [Database installed (e.g., PostgreSQL)]
* [Git ]

### 1. Clone the repository

```bash
git clone https://github.com/csathishit89/jioSupportManagementSystem.git
cd jioSupportManagementSystem

# Install backend dependencies
pip install -r requirements.txt

# Start the application server
streamlit run C:\MAMP\htdocs\clientQueryManagement\clientEnv\Scripts\app.py

The application should now be accessible at http://localhost:8501.

### 5. Usage

Explain how the system is used, focusing on the different user types.

```markdown
## 📖 Usage Guide

### Client Portal

1.  **Submit a Query:** Navigate to `/submit`, fill in the required fields (Query Heading, Query Description), and submit.
2.  **Track Queries:** Log in and visit the dashboard to view the status of all your submitted queries.

### Support Panel

1.  **Login:** Use your Support credentials at the `Support` page.
2.  **View New Queries:** New queries are visible on the Queries page.
3.  **Check Open query & Update:** Change the query status and update to Closed status once it is resolved.
4.  **Resolve:** Mark the query as "Closed"

