import asyncio
from sqlalchemy import select
from car_api.core.database import get_session
from car_api.core.security import get_password_hash
from car_api.models.users import User

async def main():
    async for db in get_session():
        existing = await db.scalar(
            select(User).where(User.email == 'recrutador@teste.com')
        )
        if existing:
            print('Usuário de teste já existe.')
            return

        user = User(
            username='recrutador',
            email='recrutador@teste.com',
            password=get_password_hash('teste123'),
        )
        db.add(user)
        await db.commit()
        print('Usuário de teste criado com sucesso!')

asyncio.run(main())
