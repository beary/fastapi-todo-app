# fastapi-todo-app

![FastAPI](https://img.shields.io/badge/FastAPI-009485?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-FF4500?style=for-the-badge&logo=sqlalchemy&logoColor=white)
![postgresql](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![React Router](https://img.shields.io/badge/React_Router-CA4245?style=for-the-badge&logo=react-router&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![mui](https://img.shields.io/badge/MUI-007FFF?style=for-the-badge&logo=mui&logoColor=white)
![rtk-query](https://img.shields.io/badge/RTK_Query-FF4500?style=for-the-badge&logo=rtk-query&logoColor=white)

## Usage

### Install and run server

```bash
git clone https://github.com/beary/fastapi-todo-app.git
cd fastapi-todo-app

# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install python dependencies
python -m pip install -U pip
python -m pip install -U poetry
python -m poetry install

# Configure database (edit .env)
cp example.env .env

# Initialize database
python -m alembic upgrade head

# Run server
python -m fastapi run --app app app/main.py
```

### Install and run web

prerequisites:

- node
- pnpm

```bash
cd web
pnpm install
pnpm run dev
```

visit http://localhost:5173

![screenshot](docs/screenshot.png)
