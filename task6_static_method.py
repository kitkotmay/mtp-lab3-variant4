class MathHelper:
    """Вспомогательный класс с математическими методами."""
    @staticmethod
    def square(number):
        """Возвращает квадрат числа."""
        return number ** 2
    @staticmethod
    def is_even(number):
        """Проверяет, является ли число чётным."""
        return number % 2 == 0
    @staticmethod
    def maximum(first, second):
        """Возвращает большее из двух чисел."""
        if first > second:
            return first
        return second
def main():
    number = 8
    print(f"Число: {number}")
    print(f"Квадрат: {MathHelper.square(number)}")
    print(f"Чётное: {MathHelper.is_even(number)}")
    print(f"Максимум из 10 и 25: {MathHelper.maximum(10, 25)}")
if __name__ == "__main__":
    main()
