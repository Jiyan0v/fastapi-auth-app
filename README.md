# FastAPI Auth App

Staj başvurularım için geliştirdiğim bir kullanıcı kimlik doğrulama uygulaması. Backend tarafında nasıl güvenli bir giriş sistemi kurulduğunu öğrenmek istiyordum, bu yüzden sıfırdan geliştirmaya karar verdim.

FastAPI, SQLite ve JWT kullandım. Şifreler bcrypt ile hashleniyor, giriş yapınca JWT token üretiliyor. Hem web arayüzü hem de REST API olarak çalışıyor.

## Ne Yapıyor?

Kullanıcı kayıt olabiliyor, giriş yapabiliyor. Giriş sonrası JWT token üretiliyor ve dashboard'da gösteriliyor. `/api/me` endpoint'ine token göndererek kullanıcı bilgisi çekebiliyorsunuz.

## Kurulum

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Çalışınca tarayıcıda açın:

- `http://localhost:8000` — giriş sayfası
- `http://localhost:8000/docs` — Swagger arayüzü

## Proje Yapısı

```
auth_app/
├── main.py          # route'lar
├── database.py      # SQLAlchemy bağlantısı
├── models.py        # User modeli
├── schemas.py       # Pydantic şemaları
├── auth.py          # JWT ve bcrypt işlemleri
├── requirements.txt
└── templates/
    ├── login.html
    ├── register.html
    └── dashboard.html
```

## Kullanılan Teknolojiler

| Teknoloji | Neden Kullandım |
|-----------|-----------------|
| FastAPI | Hızlı ve modern Python framework'ü |
| SQLAlchemy | Veritabanını ORM ile yönetmek için |
| SQLite | Kurulum gerektirmeden çalışması için |
| Passlib/bcrypt | Şifreleri güvenli saklamak için |
| python-jose | JWT token üretimi için |
| Jinja2 | HTML sayfalarını render etmek için |
