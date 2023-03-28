from .AI.imagga.barcodes import barcode_runner
from .AI.imagga.colors import colors_runner
from .AI.imagga.tags import ImaggaTagsEndpoint, tags_runner
from config import load_config, BASE_DIR


def run():
    config = load_config(BASE_DIR / '.env')
    image_url = input('Введите ссылку на картинку: ')
    command = int(input('Введите команду:\n'
                        '1: Получить самый вероятный объект с картинки\n'
                        '2: Получить значение штрих-кода\n'
                        '3: Получить цвета на картинке\nВвод: '))
    if command == 1:
        tags_runner(
            config.IMAGGA_API_KEY,
            config.IMAGGA_API_SECRET,
            image_url
        )
    elif command == 2:
        barcode_runner(
            config.IMAGGA_API_KEY,
            config.IMAGGA_API_SECRET,
            image_url
        )
    elif command == 3:
        colors_runner(
            config.IMAGGA_API_KEY,
            config.IMAGGA_API_SECRET,
            image_url
        )
    else:
        print('Неверная команда')
    run()
