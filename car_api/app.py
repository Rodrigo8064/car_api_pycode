from fastapi import FastAPI, status

from car_api.routers import auth, brands, cars, users

app = FastAPI(
    title="Inventory API",
    description="""
API de lista de desejos para e-commerce.

## Como testar

Use as credenciais abaixo para autenticar:

| campo | valor |
|-------|-------|
| email | recrutador@teste.com |
| senha | teste123 |

**Passo a passo:**
1. Faça POST /api/auth/token com as credenciais acima
2. Copie o access_token retornado
3. Clique em **Authorize** 🔒 Ao lado
4. Cole o token no campo **Value** e clique em Authorize
5. Explore os endpoints à vontade!
    """,
    version="1.0.0",
)

@app.get('/health_check', status_code=status.HTTP_200_OK)
def health_check():
    return {'status': 'ok'}

app.include_router(
    router=auth.router,
    prefix='/api/v1/auth',
    tags=['authentication'],
)

app.include_router(
    router=users.router,
    prefix='/api/v1/users',
    tags=['users'],
)

app.include_router(
    router=brands.router,
    prefix='/api/v1/brands',
    tags=['brands'],
)

app.include_router(
    router=cars.router,
    prefix='/api/v1/cars',
    tags=['cars'],
)
