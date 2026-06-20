# 🔐 FastAPI Auth App

Staj başvurusu için geliştirilmiş, **FastAPI + SQLite + JWT** tabanlı kullanıcı kimlik doğrulama uygulaması.

## Özellikler

- ✅ Kullanıcı kaydı (Register)
- ✅ Giriş (Login) + JWT token üretimi
- ✅ Bcrypt ile şifre hashleme
- ✅ SQLAlchemy ORM + SQLite veritabanı
- ✅ REST API endpointleri (`/api/token`, `/api/me`)
- ✅ Jinja2 HTML template sistemi
- ✅ FastAPI otomatik Swagger dokümantasyonu (`/docs`)

## Kurulum

```bash
# 1. Bağımlılıkları yükle
pip install -r requirements.txt

# 2. Uygulamayı başlat
uvicorn main:app --reload

# 3. Tarayıcıda aç
# Web arayüzü → http://localhost:8000
# API dokümantasyonu → http://localhost:8000/docs
```

## Proje Yapısı

```
auth_app/
├── main.py          # FastAPI route'ları
├── database.py      # SQLAlchemy bağlantısı
├── models.py        # Veritabanı modelleri
├── schemas.py       # Pydantic şemaları
├── auth.py          # JWT & bcrypt işlemleri
├── requirements.txt
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

## Kullanılan Teknolojiler

| Teknoloji | Amaç |
|-----------|------|
| FastAPI | Web framework |
| SQLAlchemy | ORM |
| SQLite | Veritabanı |
| Passlib/bcrypt | Şifre hashleme |
| python-jose | JWT token |
| Jinja2 | HTML templating |
