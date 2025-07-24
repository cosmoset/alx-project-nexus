# 🎬 Movie Recommendation Backend — ProDev Case Study

This project simulates a real-world backend service for a **Movie Recommendation Application**, developed as part of the **ProDev Backend Engineering Program**.

---

## 📌 Overview

The backend system powers a movie recommendation app, offering APIs to retrieve trending and personalized movie suggestions, handle user authentication, and store user preferences.

Key backend goals:
- **API Development**: Serve trending and recommended movie data.
- **User Management**: Allow users to register, authenticate, and save favorite movies.
- **Performance Optimization**: Use caching to reduce latency and API load.
- **Documentation**: Provide clear, browsable API docs using Swagger.

---

## 🎯 Project Goals

- **API Creation**  
  - Endpoint to fetch trending and recommended movies via TMDb API.
- **User Management**  
  - JWT-based authentication.  
  - Favorite movie storage per user.
- **Performance Optimization**  
  - Redis caching for movie endpoints.
- **Comprehensive Documentation**  
  - Swagger UI at `/api/docs`.

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Django** | Web framework for backend logic |
| **PostgreSQL** | Relational database |
| **Redis** | In-memory caching for fast API responses |
| **TMDb API** | External movie data source |
| **Swagger / drf-yasg** | Interactive API documentation |
| **Docker** (optional) | Containerization for development & deployment |

---

## 🔑 Key Features

### 📽 Movie Recommendations API
- Integrate with **TMDb API** to fetch trending and recommended movies.
- Use error handling for failed third-party requests.

### 👤 User Authentication & Preferences
- JWT-based auth (via `djangorestframework-simplejwt`)
- Users can register, log in, and save favorite movies.

### 🚀 Performance Optimization
- Use **Redis** to cache trending/recommended movie data.
- Expire cache periodically to maintain freshness.

### 📖 Swagger Documentation
- Every API endpoint documented using Swagger (`drf-yasg`).
- Hosted at: [`/api/docs`](http://localhost:8000/api/docs)

---

## 🛠️ Git Commit Workflow

| Type | Example Commit Message |
|------|-------------------------|
| Initial Setup | `feat: set up Django project with PostgreSQL` |
| API Integration | `feat: integrate TMDb API for movie data` |
| Feature Dev | `feat: implement movie recommendation API` |
| Authentication | `feat: add JWT user auth and favorite movie model` |
| Optimization | `perf: add Redis caching to TMDb calls` |
| Documentation | `feat: add Swagger API docs` |
| ReadMe | `docs: update README with setup and features` |

---

## 🚧 Implementation Process

1. **Project Initialization**
   - Setup Django project, PostgreSQL DB, Redis (via Docker or system install).

2. **Movie API Integration**
   - Use `requests` or `httpx` to call TMDb.
   - Parse and return trending/recommended movies.

3. **User System**
   - Create user model (or extend default).
   - JWT Authentication via `djangorestframework-simplejwt`.
   - FavoriteMovie model to track user preferences.

4. **Caching**
   - Use `django-redis` to cache TMDb responses.
   - Set expiration to avoid stale data.

5. **Swagger Docs**
   - Use `drf-yasg` to auto-document endpoints.
   - Accessible at `/api/docs`.

---

## 🧪 Local Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/alx-project-nexus.git
cd alx-project-nexus

# Create virtual environment
python -m venv env
source env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your TMDb API key, DB config, etc.

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver

