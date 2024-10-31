# ... импорты

async def add_dish(message: types.Message, state: FSMContext):


async def confirm_dish(message: types.Message, state: FSMContext):
    data = await state.get_data()
    with database.engine.connect() as conn:
        result = conn.execute(
            database.dishes.insert().values(
                name=data['name'],
                price=data['price'],
                category=data['category']
            )
        )