from productcard import (
    ProductCard,
)


class Menu:
    """Класс для описания меню."""

    def __init__(self):
        self.product_card = None

    def run(self):
        """Запуск главного меню."""

        running = True

        while running:
            self.print_main_menu()
            choice = input("Выберите действие: ").strip()

            match choice:
                case '0':
                    print("До свидания!")
                    running = False
                case '1':
                    self.create_product()
                case "2":
                    self.view_product()
                case "3":
                    self.edit_product()
                case "4":
                    self.accept_product()
                case "5":
                    self.write_off_product()
                case _:
                    print("Неверный выбор. Пожалуйста, выберите действие из меню.")

    @staticmethod
    def print_main_menu():
        """Отрисовка главного меню."""

        print(
             "УПРАВЛЕНИЕ КАРТОЧКАМИ ТОВАРОВ\n"
             "\n0. Выход\n"
             "1. Создать новую карточку товара\n"
             "2. Просмотреть информацию о товаре\n"
             "3. Редактировать карточку товара\n"
             "4. Принять товар к учёту\n"
             "5. Списать товар\n"
        )

    def check_product_exists(self) -> bool:
        """Проверка, существует ли карточка товара."""

        product_exists = True

        if self.product_card is None:
            print("\nОшибка: Сначала создайте карточку товара!")
            product_exists = False

        return product_exists

    def create_product(self):
        """Создание нового товара."""

        self.product_card = ProductCard()
        if self.product_card.create_from_input():
            print("Карточка успешно создана!")

    def view_product(self):
        """Просмотр информации о товаре."""

        if self.check_product_exists():
            self.product_card.get_information()

    def edit_product(self):
        """Редактирование товара."""

        if self.check_product_exists():
            self.product_card.edit_information()

    def accept_product(self):
        """Принятие товара к учёту."""

        if self.check_product_exists():
            self.product_card.accept_to_account()

    def write_off_product(self):
        """Списание товара."""

        if self.check_product_exists():
            self.product_card.write_off()


if __name__ == "__main__":
    menu = Menu()
    menu.run()
