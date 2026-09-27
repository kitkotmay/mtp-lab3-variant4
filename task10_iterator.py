class NumberIterator:
    """Итератор по целым числам в заданном диапазоне."""
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value
def main():
    numbers = NumberIterator(1, 10)
    print("Числа от 1 до 10:")
    for number in numbers:
        print(number)
if __name__ == "__main__":
    main()
