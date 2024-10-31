from aiogram.dispatcher.filters.state import StatesGroup, State

class RestaurantReview(StatesGroup):
    name = State()
    phone_or_instagram = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()