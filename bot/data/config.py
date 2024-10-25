from environs import Env # type: ignore

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNEL_ID=env.str("CHANNEL_ID")
# IP = env.str("ip")  # Xosting ip manzili
# password = env.str("PASSWORD")  # Xosting ip manzili

