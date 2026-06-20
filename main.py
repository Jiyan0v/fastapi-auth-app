from fastapi import FastAPI, Depends, HTTPException, status, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import timedelta
import models, schemas, auth
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Auth App")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def root():
    return RedirectResponse(url="/login")


@app.get("/login", response_class=HTMLResponse)
def login_page(request: Request, error: str = None, success: str = None):
    return templates.TemplateResponse("login.html", {
        "request": request, "error": error, "success": success
    })


@app.post("/login")
def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = auth.authenticate_user(db, username, password)
    if not user:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "error": "Kullanıcı adı veya şifre hatalı."
        })
    token = auth.create_access_token(data={"sub": user.username})
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "username": user.username,
        "token": token
    })


@app.get("/register", response_class=HTMLResponse)
def register_page(request: Request, error: str = None):
    return templates.TemplateResponse("register.html", {
        "request": request, "error": error
    })


@app.post("/register")
def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    existing = db.query(models.User).filter(
        (models.User.username == username) | (models.User.email == email)
    ).first()
    if existing:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "error": "Bu kullanıcı adı veya e-posta zaten kullanımda."
        })
    hashed = auth.get_password_hash(password)
    new_user = models.User(username=username, email=email, hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return RedirectResponse(url="/login?success=Kayıt başarılı! Giriş yapabilirsiniz.", status_code=303)


# --- REST API endpoints (bonus for CV) ---

@app.post("/api/token", response_model=schemas.Token)
def api_login(form_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Hatalı kimlik bilgileri")
    token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}


@app.get("/api/me", response_model=schemas.UserOut)
def api_me(current_user: models.User = Depends(auth.get_current_user)):
    return current_user
