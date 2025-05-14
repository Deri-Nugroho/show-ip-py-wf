# Show IP Server with Python

A simple Python web application that displays the server's local IP address and port. Useful for local network diagnostics, development, or testing environments.

## 🖥️ Features

- Display server's IP address and port
- Built with Flask
- Ready for local deployment or Docker/container usage

---

## 🚀 Getting Started (Local Deployment)

### 1. Clone the Repository

```bash
git clone https://github.com/dihkaw/showipserverwithpython.git
cd showipserverwithpython
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Run the Application
```bash
python app.py
```
or
```bash
flask run --host=0.0.0.0 --port=5000
```
### 5. Access the Web App
Open your browser and go to:
```
http://localhost:5000
```
The app will show your local IP address and port used by the server.
