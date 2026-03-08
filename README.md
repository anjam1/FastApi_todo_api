# 🚀 FastAPI Todo Application

A modern, secure, and feature-rich Todo application built with FastAPI, SQLAlchemy, and JWT authentication. This project demonstrates best practices for building RESTful APIs with user authentication, authorization, and database relationships.

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-100000?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white)

## ✨ Features

### 🔐 Authentication & Security
- **JWT-based authentication** with access tokens
- **Password hashing** using bcrypt
- **Protected endpoints** with user-specific data isolation
- **Case-insensitive username validation** to prevent duplicates

### 📝 Todo Management
- **CRUD operations** for todos (Create, Read, Update, Delete)
- **User-specific todo isolation** - users can only access their own todos
- **Partial updates** for todo status (complete/incomplete)
- **Validation** for todo titles and descriptions

### 🏗️ Architecture
- **FastAPI** for high-performance API framework
- **SQLAlchemy ORM** for database operations
- **Pydantic schemas** for request/response validation
- **Modular structure** with separate routes, models, and schemas
- **Environment-based configuration** with dotenv

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) package manager (recommended) or pip
- PostgreSQL/MySQL/SQLite (SQLite works out of the box)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/todo-app.git
cd todo-app
```

2. **Install dependencies**
```bash
uv sync
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. **Run the application**
```bash
uv run fastapi dev main.py
```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once running, access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔧 API Endpoints

### Authentication
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/login` | User login | No |
| POST | `/users` | User registration | No |

### Todos
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/todos` | Get all user's todos | Yes |
| GET | `/todos/{id}` | Get specific todo | Yes |
| POST | `/todos` | Create new todo | Yes |
| PUT | `/todos/{id}` | Update todo | Yes |
| PATCH | `/todos/{id}/status` | Update todo status | Yes |
| DELETE | `/todos/{id}` | Delete todo | Yes |

### Users
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/users` | Register new user | No |

## 🗄️ Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    email VARCHAR UNIQUE NOT NULL,
    password VARCHAR NOT NULL
);
```

### Todos Table
```sql
CREATE TABLE "To Dos" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR NOT NULL,
    description VARCHAR NOT NULL,
    target_date DATE NOT NULL,
    is_complete BOOLEAN DEFAULT FALSE,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES users(id)
);
```

## 🛡️ Security Features

1. **Password Security**: Passwords are hashed using bcrypt before storage
2. **JWT Tokens**: Secure token-based authentication with expiration
3. **Input Validation**: All inputs validated using Pydantic schemas
4. **SQL Injection Protection**: SQLAlchemy ORM prevents injection attacks
5. **CORS**: Configured for secure cross-origin requests
6. **User Isolation**: Users can only access their own data

## 📁 Project Structure

```
todo_app/
├── main.py              # FastAPI application entry point
├── database.py          # Database configuration and connection
├── models.py            # SQLAlchemy models (User, Todos)
├── schemas.py           # Pydantic schemas for validation
├── oauth2.py            # JWT authentication utilities
├── utils.py             # Utility functions (password hashing)
├── routes/
│   ├── __init__.py
│   ├── auth.py          # Authentication routes
│   ├── todos.py         # Todo CRUD operations
│   └── users.py         # User management
├── pyproject.toml       # Project dependencies
├── uv.lock              # Locked dependencies
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🔐 Environment Variables

Create a `.env` file with the following variables:

```env
# Database Configuration
DATABASE_URL=sqlite:///./todos.db
# or for PostgreSQL: postgresql://user:password@localhost/todo_db

# JWT Configuration
JWT_SECRET_KEY=your-secret-key-here
# Generate with: openssl rand -hex 32

# Application Settings
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## 🧪 Testing the API

### 1. Register a new user
```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepassword123"
  }'
```

### 2. Login to get access token
```bash
curl -X POST "http://localhost:8000/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john@example.com&password=securepassword123"
```

### 3. Create a todo (with authentication)
```bash
curl -X POST "http://localhost:8000/todos" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive documentation for the FastAPI todo application",
    "target_date": "2024-12-31",
    "is_complete": false
  }'
```

## 🚀 Deployment

### Using Docker (Recommended)
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Manual Deployment
1. Set up production database (PostgreSQL recommended)
2. Configure environment variables for production
3. Use Gunicorn with Uvicorn workers:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation
- [JWT](https://jwt.io/) for authentication

## 📞 Support

For support, email yourname@example.com or open an issue in the GitHub repository.

---

**⭐ Star this repo if you found it useful!**