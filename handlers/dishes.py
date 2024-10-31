async def show_dishes(message: types.Message):
    with database.engine.connect() as conn:
        result = conn.execute(database.dishes.select())
        dishes = result.fetchall()

        text = "Наши блюда:\n"
        for dish in dishes:
            text += f"- {dish.name} ({dish.price}) - {dish.category}\n"
        await message.answer(text)

async def filter_dishes(message: types.Message):
    category = message.text.lower()

    with database.engine.connect() as conn:
        result = conn.execute(database.dishes.select().where(database.dishes.c.category == category))
        dishes = result.fetchall()
