"""
Необходимо создать класс карточки товара и задать функцию по созданию, изменению, извлечению данных данной карточки,
а также списания данной карточки с учёта, учитывая ошибки, которые могут возникнуть при этом. Также необходимо прописать
простой UI в консоли, для более удобного взаимодействия с пользователем. Необходимо учитывать, что полей у карточки
должно быть больше 10, например:

Наименование
Количество
Состояние (не менее 3 состояний)
Поставщик
Производитель
Стоимость
Местоположение
и др.

Списание карточки возможно только при состояние карточки "принято к учёту/состоит на учёте"
"""


class ProductCard:
    """Класс для описания карточки товара."""

    in_stock = "В наличии"
    out_of_stock = "Нет в наличии"
    accepted = "Принято к учёту/состоит на учёте"
    written_off = "Списано"

    valid_conditions = [in_stock, out_of_stock, accepted, written_off]

    def __init__(self, name: str="", count: int=0, condition: str="", supplier: str="", manufacturer: str="",
                 cost: int=0, location: str="", article_number: int=0, weight: int=0, dimensions: int=0,
                 category: str="") -> None:
        """Инициализация класса.

        Attributes:
            name: наименование товара,
            count: количество товара(число шт.),
            condition: состояние товара,
            supplier: поставщик товара,
            manufacturer: производитель товара,
            cost: стоимость товара(в руб.),
            location: местоположение товара,
            article_number: артикул товара(уникальный набор из 8 цифр),
            weight: вес товара(в кг),
            dimensions: габариты товара(в см^3),
            category: категория товара.
        """

        self.__name = name
        self.__count = count
        self.__condition = condition
        self.__supplier = supplier
        self.__manufacturer = manufacturer
        self.__cost = cost
        self.__location = location
        self.__article_number = article_number
        self.__weight = weight
        self.__dimensions = dimensions
        self.__category = category

    def get_name(self) -> str:
        """Геттер для наименования товара.

        Return:
            name: Наименование товара.
        """

        return f'Наименование товара: {self.__name}'

    def set_name(self, new_name: str) -> None:
        """Сеттер для наименования товара.

        Args:
            new_name: Наименование товара.
        """

        if not isinstance(new_name, str):
            raise TypeError("Наименование должно состоять из букв!")
        elif len(new_name.strip()) == 0:
            raise ValueError("Наименование не может быть пустым!")

        # Если не выкинуло ошибку выполняем следующий код:
        self.__name = new_name.strip()

    def get_count(self) -> str:
        """Геттер для количество товара.

        Return:
            count: Количество товара.
        """

        return f'Количество товара: {self.__count}'

    def set_count(self, new_count: int) -> None:
        """Сеттер для количества товара.

        Args:
            new_count: Количество товара.
        """

        if not isinstance(new_count, int):
            raise TypeError("Количество должно быть целым числом!")
        elif new_count < 0:
            raise ValueError("Количество не может быть отрицательным!")

        self.__count = new_count

    def get_condition(self) -> str:
        """Геттер для состояния товара.

        Return:
            condition: Состояние товара.
        """

        return f'Состояние товара: {self.__condition}'

    def set_condition(self, new_condition: str) -> None:
        """Сеттер для состояния товара.

        Args:
            new_condition: Состояние товара.
        """

        if new_condition and new_condition not in self.valid_conditions:
            raise ValueError(f"Недопустимое состояние! Допустимы: {', '.join(self.valid_conditions)}.")

        self.__condition = new_condition

    def get_supplier(self) -> str:
        """Геттер для поставщика товара.

        Return:
            supplier: Поставщик товара.
        """

        return f'Поставщик товара: {self.__supplier}'

    def set_supplier(self, new_supplier: str) -> None:
        """Сеттер для поставщика товара.

        Args:
            new_supplier: Поставщик товара.
        """

        if not isinstance(new_supplier, str):
            raise TypeError("Недопустимое имя поставщика!")
        elif len(new_supplier.strip()) == 0:
            raise ValueError("Необходмио написать поставщика!")

        self.__supplier = new_supplier.strip()

    def get_manufacturer(self) -> str:
        """Геттер для производителя товара.

        Return:
            manufacturer: Производитель товара.
        """

        return f'Производитель товара: {self.__manufacturer}'

    def set_manufacturer(self, new_manufacturer: str) -> None:
        """Сеттер для gроизводителя товара.

        Args:
            new_manufacturer: Производитель товара.
        """

        if not isinstance(new_manufacturer, str):
            raise TypeError("Недопустимое имя производителя!")
        elif len(new_manufacturer.strip()) == 0:
            raise ValueError("Необходмио написать производителя!")

        self.__manufacturer = new_manufacturer.strip()

    def get_cost(self) -> str:
        """Геттер для стоимости товара.

        Return:
            cost: Стоимость товара.
        """

        return f'Стоимость товара: {self.__cost}'

    def set_cost(self, new_cost: float) -> None:
        """Сеттер для стоимости товара.

        Args:
            new_cost: Стоимость товара.
        """

        if not (isinstance(new_cost, int) or isinstance(new_cost, float)):
            raise TypeError("Стоимость товара должна быть числом!")
        elif new_cost < 0:
            raise ValueError("Стоимость товара не может быть отрицательной!")

        self.__cost = float(new_cost)

    def get_location(self) -> str:
        """Геттер для местоположения товара.

        Return:
            location: Местоположение товара.
        """

        return f'Местоположение товара: {self.__location}'

    def set_location(self, new_location: str) -> None:
        """Сеттер для местоположения товара.

        Args:
            new_location: Местоположение товара.
        """

        if not isinstance(new_location, str):
            raise TypeError("Местоположение должно быть строкой!")
        elif len(new_location.strip()) == 0:
            raise ValueError("Необходмио написать местоположение!")

        self.__location = new_location.strip()

    def get_article_number(self) -> str:
        """Геттер для артикула товара.

        Return:
            article_number: Артикул товара.
        """

        return f'Артикул товара: {self.__article_number}'

    def set_article_number(self, new_article_number: int) -> None:
        """Сеттер для артикула товара.

        Args:
            new_article_number: Артикул товара.
        """

        if not isinstance(new_article_number, int):
            raise TypeError("Артикул должен быть числом!")
        elif not (10000000 <= new_article_number <= 99999999):
            raise ValueError("Артикул должен содержать ровно 8 цифр!")

        self.__article_number = new_article_number

    def get_weight(self) -> str:
        """Геттер для веса товара.

        Return:
            weight: Вес товара.
        """

        return f'Вес товара: {self.__weight}'

    def set_weight(self, new_weight: float) -> None:
        """Сеттер для веса товара.

        Args:
            new_weight: Вес товара.
        """

        if not (isinstance(new_weight, int) or isinstance(new_weight, float)):
            raise TypeError("Вес должен быть числом!")
        if new_weight < 0:
            raise ValueError("Вес не может быть отрицательным!")

        self.__weight = float(new_weight)

    def get_dimensions(self) -> str:
        """Геттер для габарита товара.

        Return:
            dimension: Габариты товара.
        """

        return f'Габариты товара: {self.__dimensions}.'

    def set_dimensions(self, new_dimensions: int) -> None:
        """Сеттер для габарита товара.

        Args:
            new_dimensions: Габариты товара.
        """

        if not (isinstance(new_dimensions, int) or isinstance(new_dimensions, float)):
            raise TypeError("Габариты должны быть определены числом!")
        if new_dimensions < 0:
            raise ValueError("Габариты не могут быть отрицательными!")

        self.__dimensions = new_dimensions

    def get_category(self) -> str:
        """Геттер для категории товара.

        Return:
            category: Котегория товара.
        """

        return f'Котегория товара: {self.__category}.'

    def set_category(self, new_category: str) -> None:
        """Сеттер для категории товара.

        Args:
            new_category: Категория товара.
        """

        if not isinstance(new_category, str):
            raise TypeError("Категория должна быть строкой!")
        elif len(new_category.strip()) == 0:
            raise ValueError("Необходмио написать категорию!")

        self.__category = new_category.strip()

    def update_availability(self) -> None:
        """Обновляет состояние на основе количества."""

        self.__condition = self.in_stock if self.__count > 0 else self.out_of_stock

    def write_off(self) -> bool:
        """Метод списания товара.

        Returns:
               True при успешном списании товара, False в противном случае.
        """

        condition_of_writting_off = False

        try:
            if self.__condition == self.accepted:
                self.__condition = self.written_off
                print(f"Товар '{self.__name}' успешно списан.")
                condition_of_writting_off = True
            elif self.__condition == self.in_stock:
                print("Переведите товар в состояние 'Принято к учёту' для списания!")
            elif self.__condition == self.out_of_stock:
                print("Ошибка: Товара нет в наличии. Списание невозможно.")
            elif self.__condition == self.written_off:
                print("Ошибка: Товар уже списан.")
            else:
                print(f"Ошибка: Неизвестное состояние товара: {self.__condition}")

        except Exception as e:
            print(f"Произошла ошибка при списании: {e}")

        return condition_of_writting_off

    def accept_to_account(self) -> bool:
        """Перевод товара в состояние 'Принято к учёту'."""

        condition_of_accepting = False

        try:
            if self.__condition == self.in_stock:
                self.__condition = self.accepted
                print(f"Товар '{self.__name}' принят к учёту.")
                condition_of_accepting = True
            elif self.__condition == self.accepted:
                print("Товар уже принят к учёту.")
            elif self.__condition == self.written_off:
                print("Ошибка: Списанный товар нельзя принять к учёту.")
            elif self.__condition == self.out_of_stock:
                print(f"Товара нет в наличии и его нельзя принять к учёту.")
            else:
                print(f"Ошибка: Неизвестное состояние товара: {self.__condition}")

        except Exception as e:
            print(f"Произошла ошибка при переводе: {e}")

        return condition_of_accepting

    def create_from_input(self) -> bool:
        """Создание карточки из пользовательского ввода."""

        condition_of_creating = False
        print("СОЗДАНИЕ КАРТОЧКИ ТОВАРА")

        fields = [
            ("наименование", "str"),
            ("количество", "int"),
            (f"состояние ({', '.join(self.valid_conditions)})", "condition"),
            ("поставщик", "str"),
            ("производитель", "str"),
            ("стоимость", "float"),
            ("местоположение", "str"),
            ("артикул", "int"),
            ("вес (кг)", "float"),
            ("габариты", "str"),
            ("категория", "str")
        ]

        # Список для хранения введённых значений
        values = []

        try:
            for field_name, field_type in fields:
                field_entered = False

                # Пока пользователь не введет поле правильно
                while not field_entered:
                    try:
                        value = input(f"Введите {field_name}: ").strip()

                        if field_type == "int":
                            value = int(value) if value else 0
                        elif field_type == "float":
                            value = float(value) if value else 0.0
                        elif field_type == "condition":

                            if value and value not in self.valid_conditions:
                                print(f"Ошибка: состояние должно быть одним из: {', '.join(self.valid_conditions)}")

                                # Для запроса значения заново
                                continue

                        values.append(value)

                        # Выход из цикла
                        field_entered = True

                    except ValueError as e:
                        print(f"Ошибка ввода: {e}. Попробуйте снова.")
                    except Exception as e:
                        print(f"Неожиданная ошибка: {e}. Попробуйте снова.")

            self.__init__(*values)
            print("Карточка товара успешно создана!")
            condition_of_creating = True

        except Exception as e:
            print(f"Ошибка при создании карточки: {e}")

        return condition_of_creating

    def edit_information(self):
        """Редактирование информации о товаре."""

        print(
             "Редактирование карточки товара"
             "Оставьте поле пустым, чтобы оставить значение без изменений"
        )

        fields = {
            "1": ("наименование", self.set_name, self.get_name),
            "2": ("количество", self.set_count, self.get_count),
            "3": ("состояние", self.set_condition, self.get_condition),
            "4": ("поставщик", self.set_supplier, self.get_supplier),
            "5": ("производитель", self.set_manufacturer, self.get_manufacturer),
            "6": ("стоимость", self.set_cost, self.get_cost),
            "7": ("местоположение", self.set_location, self.get_location),
            "8": ("артикул", self.set_article_number, self.get_article_number),
            "9": ("вес", self.set_weight, self.get_weight),
            "10": ("габариты", self.set_dimensions, self.get_dimensions),
            "11": ("категория", self.set_category, self.get_category)
        }

        running_editing = True
        while running_editing:
            print("\nВыберите поле для редактирования:")

            # getter - это ссылка на метод геттера, а getter() - выхов этого метода
            # Показываем всевозможные подменю для редактирования
            print("0. Завершить редактирование")
            for key, (name, _, getter) in fields.items():
                print(f"{key}. {name} (текущее: {getter()})")

            choice = input("Ваш выбор: ").strip()

            if choice == "0":
                running_editing = False
            elif choice in fields:
                field_name, setter, getter = fields[choice]
                current_value = getter()
                new_value = input(f"Введите новое значение для '{field_name}' (текущее: {current_value}): ").strip()

                if new_value:
                    try:
                        if field_name in ["количество"]:
                            new_value = int(new_value)
                        elif field_name in ["стоимость", "вес", "габариты"]:
                            new_value = float(new_value)

                        setter(new_value)
                        print(f"Поле '{field_name}' успешно обновлено!")

                    except ValueError as e:
                        print(f"Ошибка: {e}")
                    except TypeError as e:
                        print(f"Ошибка: {e}")
                    except Exception as e:
                        print(f"Неожиданная ошибка: {e}")
            else:
                print("Неверный выбор. Попробуйте снова.")

    def get_information(self):
        """Вывод всей информации о товаре."""

        print(
             "ИНФОРМАЦИЯ О ТОВАРЕ:\n"
             f"\nНаименование:     {self.__name}\n"
             f"Количество:       {self.__count}\n"
             f"Состояние:        {self.__condition}\n"
             f"Поставщик:        {self.__supplier}\n"
             f"Производитель:    {self.__manufacturer}\n"
             f"Стоимость:        {self.__cost} руб.\n"
             f"Местоположение:   {self.__location}\n"
             f"Артикул:          {self.__article_number}\n"
             f"Вес:              {self.__weight} кг\n"
             f"Габариты:         {self.__dimensions} см^3\n"
             f"Категория:        {self.__category}\n"
        )
