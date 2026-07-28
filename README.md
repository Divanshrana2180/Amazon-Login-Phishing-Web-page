Amazon-Login-Phishing-Web-page
Disclaimer: This project is an educational phishing simulation and security awareness tool designed to demonstrate how credential harvesting attacks work and to help organizations test user awareness. It is not affiliated with Amazon.com, Inc. or any of its affiliates.

🚀 Overview
This project is a high-fidelity login simulation built with Flask. It replicates the user interface and flow of a standard single-sign-on (SSO) page to demonstrate the mechanics of credential harvesting attacks.

It features a two-step authentication simulation:

Step 1: Captures user identity (email/phone).

Step 2: Simulates a password entry gate.

The primary goal of this project is to provide a safe, controlled environment for:

Educating users on how phishing sites mimic legitimate services.

Testing the effectiveness of security awareness training.

Demonstrating the importance of URL verification and Multi-Factor Authentication (MFA).

⚠️ Important Security Warning
This project is for educational and authorized testing purposes only.

🛑 Do not use this project to maliciously steal credentials from individuals without their consent.

🛑 Do not deploy this on a domain that infringes on trademarks (e.g., do not buy amazon-security.com).

✅ Do use this to test your own security protocols or to educate others on phishing risks.

Misuse of this tool for unauthorized credential collection may violate local laws and regulations regarding data privacy and computer fraud.

🛡️ Features
High-Fidelity UI: Replicates the visual style of major e-commerce login pages for realistic simulation.

Two-Step Flow: Mimics the split authentication process (Identity first, Password second) used by modern security systems.

Session Management: Uses secure Flask sessions to handle state between the two steps.

Real-Time Alerting: Integrated support for Discord Webhooks to notify administrators immediately upon credential submission (for authorized testing).

Responsive Design: Fully responsive CSS that adapts to mobile and desktop views.

Error Handling: Robust error handling for missing sessions or invalid data.

📂 Project Structure
. ├── main.py # Main Flask application logic

├── requirements.txt # Python dependencies

├── templates/

│ ├── index.html # Main login simulation template

│ └── error.html # Error/Redirect page template

├── static/

│ └── style.css # Custom CSS for UI replication

├── captured_data.txt # (Local only) Log file for captured data (if enabled)

└── README.md # This fileTextUnwrapCopied!Copy

🛠️ Installation & Setup
Prerequisites
Python 3.8 or higher

pip (Python package installer)

A GitHub account (for hosting)

(Optional) A Discord Webhook URL for real-time alerts

1. Clone the Repository
git clone <YOUR_REPOSITORY_URL>

cd <YOUR_REPOSITORY_NAME>2. Install DependenciesBashCopied!Copypip install -r requirements.txt3. Configuration (Optional but Recommended)To enable real-time alerts via Discord (useful for authorized testing):

Create a Discord Server.

Go to Server Settings > Integrations > Webhooks > New Webhook.

Copy the Webhook URL.

Set the URL as an environment variable:

Linux/Mac: export DISCORD_WEBHOOK="YOUR_WEBHOOK_URL"

Windows: set DISCORD_WEBHOOK=YOUR_WEBHOOK_URL

Heroku/Render: Set in the platform's Environment Variables settings.

4. Run the ApplicationBashCopied!Copypython main.pyThe application will start on http://127.0.0.1:8080.🌐 DeploymentThis project is designed to be deployed on cloud platforms for accessibility during authorized tests.

Render / Heroku / Railway:

These platforms are supported via the requirements.txt and gunicorn configuration.

Note: File-based logging (captured_data.txt) is not persistent on these platforms. You must use the Discord Webhook feature or integrate a database (e.g., PostgreSQL, SQLite with persistent volume) to store captured data.

Local Testing:

Running locally allows for file-based logging (captured_data.txt) for analysis.

🔒 Security & Privacy

Data Storage: By default, this project does not store credentials in a database. If configured for local logging, data is stored in a plain text file (captured_data.txt) which should be secured and deleted after testing.

Session Safety: The application uses Flask's built-in session management with a secret key to prevent session hijacking during the simulation.

No Third-Party Data Sharing: The application does not send data to any third party other than the optional Discord webhook configured by the administrator.

🎓 Educational Use Cases

Security Awareness Training: Show employees exactly what a phishing attack looks like in a controlled environment.

Red Team Exercises: Use as part of a broader, authorized social engineering assessment.

Web Development Learning: Study how Flask handles sessions, templates, and form data.

📜 LicenseThis project is licensed under the MIT License. See the LICENSE file for details.🤝 ContributingContributions are welcome! Please feel free to submit a Pull Request if you have improvements for:

Better security practices.

Enhanced educational warnings.

Integration with other alerting systems (Slack, Email).

📧 ContactFor questions regarding this project or security concerns, please open an issue on this repository.Created for educational purposes. Always ensure you have permission before testing phishing simulations on real users.TextUnwrapCopied!Copy
