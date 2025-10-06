# 🧠 FastAPI Backend de Práctica — Proyecto Python + MongoDB  
> API backend desarrollada para práctica profesional y refuerzo de conceptos clave de desarrollo backend moderno.  
> Este proyecto está orientado a la arquitectura RESTful, la asincronía con FastAPI y la persistencia de datos con MongoDB.

---

### 🏷️ Tecnologías principales

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688?logo=fastapi&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-7.0-47A248?logo=mongodb&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue)

---

### ⚙️ Stack Técnico

- **Framework:** FastAPI (Python 3.10)  
- **Base de datos:** MongoDB  
- **ORM/ODM:** `motor` (cliente asíncrono para MongoDB)  
- **Servidor de desarrollo:** Uvicorn  
- **Entorno:** `.env` gestionado con `python-dotenv`

---

### 🧩 Estructura del proyecto

```
practicaPython/
├── app/
│   ├── core/           # Conexión a la base de datos, configuración
│   ├── models/         # Modelos Pydantic
│   ├── routes/         # Endpoints REST
│   └── main.py         # Punto de entrada principal
├── .env                # Variables de entorno (conexión Mongo)
├── requirements.txt    # Dependencias del proyecto
└── README.md
```

---

### ⚡ Configuración y ejecución local

#### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Fedesin/fastapi-practica.git
cd fastapi-practica
```

#### 2️⃣ Crear entorno virtual e instalar dependencias

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 3️⃣ Configurar las variables de entorno

Crea un archivo `.env` con tu cadena de conexión a MongoDB:

```bash
MONGO_URI=mongodb://localhost:27017
DB_NAME=practica_db
```

#### 4️⃣ Ejecutar la API

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:  
➡️ `http://127.0.0.1:8000/docs` (Swagger UI)  
➡️ `http://127.0.0.1:8000/redoc` (Documentación alternativa)

---

### 📡 Endpoints principales

| Método | Endpoint         | Descripción                  |
|--------|------------------|------------------------------|
| `GET`  | `/users/`        | Listar todos los usuarios    |
| `POST` | `/users/`        | Crear un nuevo usuario       |
| `GET`  | `/users/{id}`    | Obtener usuario por ID       |
| `GET`  | `/`              | Estado de la API (ping)      |

---

### 🧱 Buenas prácticas aplicadas

- Arquitectura **modular y desacoplada** (core/models/routes).  
- Uso de **tipado fuerte** con `pydantic`.  
- Estructura asíncrona (`async/await`) para máxima eficiencia.  
- Conexión persistente con MongoDB vía `motor`.  
- Variables sensibles gestionadas por `.env`.  
- **Documentación automática** vía Swagger & Redoc.  
- Código limpio siguiendo principios **SOLID** y **Single Responsibility**.

---

### 🛣️ Próximos pasos

- ✅ CRUD completo con validaciones.  
- 🧠 Autenticación JWT + permisos por rol.  
- 📊 Métricas y logs estructurados.  
- 🧩 Integración con Redis (cola de tareas).  
- 🐳 Dockerización opcional del entorno.

---

### 👨‍💻 Autor

**Federico Simone**  
📍 Luján, Buenos Aires  
🔗 [GitHub](https://github.com/Fedesin) · [LinkedIn](https://linkedin.com/in/FedeSimone31)  

> Proyecto de práctica profesional para consolidar experiencia como **Desarrollador Backend & Linux Sysadmin**.
