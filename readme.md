# 📌 SocialMediaAPI

🚀 **SocialMediaAPI** is a RESTful API built with **FastAPI**, allowing users to create accounts, add posts, vote on posts, and authenticate via **OAuth2 JWT**.

## ✨ Features
- ✅ User registration and login  
- ✅ Create, edit, and delete posts  
- ✅ Vote on posts (add and remove votes)  
- ✅ JWT Authentication (OAuth2)  
- ✅ Automatic API documentation  

## 🛠 Technologies
- **FastAPI** - Web framework for building APIs  
- **SQLAlchemy** - ORM for managing the database  
- **PostgreSQL** - Database  
- **OAuth2 + JWT** - Authentication  
- **Pydantic** - Data validation  
- **Uvicorn** - ASGI server  

## 🚀 Installation and Setup
1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-user/SocialMediaAPI.git
   cd SocialMediaAPI

2. **Create and activate a virtual environment**
    ```bash
   python -m venv venv
    source venv/bin/activate  # dla Mac/Linux
    venv\Scripts\activate  # dla Windows
   ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up environment variables**

    Create a .env file in the root directory and add the following:

    ```bash
    SECRET_KEY=your_secret_key
    ALGORYTHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    DATABASE_URL=postgresql://user:password@localhost/dbname
    ```
5. **Run the server**
    
    ```bash
    uvicorn main:app --reload
    ```

## 📖 API Documentation
The API provides interactive documentation available at the following URLs:

🔹 Swagger UI → http://127.0.0.1:8000/docs 

🔹 Redoc → http://127.0.0.1:8000/redoc

## 🔑 Authentication
To use most of the endpoints, you need to:

Register via 
```bash
/users/
```
Log in via 
```bash
/login (OAuth2)
```
Obtain a JWT token and use it in the header
```
bash Authorization: Bearer <token>.
```

## 🤝 Contributing
Want to help improve the API? Feel free to fork and submit pull requests! 🔥

📩 Contact: If you have any questions, feel free to open an issue.