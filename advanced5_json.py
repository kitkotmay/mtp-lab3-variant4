import json
class Student:
    """Класс студента с поддержкой сериализации в JSON."""
    def __init__(self, full_name, group, variant):
        self.full_name = full_name
        self.group = group
        self.variant = variant
    def to_json(self):
        """Преобразует объект в JSON."""
        return json.dumps(
            self.__dict__,
            ensure_ascii=False,
            indent=4,
        )
    @classmethod
    def from_json(cls, json_data):
        """Создаёт объект из JSON."""
        data = json.loads(json_data)
        return cls(
            data["full_name"],
            data["group"],
            data["variant"],
        )
    def show_info(self):
        """Выводит информацию о студенте."""
        print(f"ФИО: {self.full_name}")
        print(f"Группа: {self.group}")
        print(f"Вариант: {self.variant}")
def main():
    student = Student(
        "Ковалевич Александра Андреевна",
        "221141р",
        4,
    )
    json_data = student.to_json()
    print("Исходный объект:")
    student.show_info()
    print("\nJSON:")
    print(json_data)
    restored_student = Student.from_json(json_data)
    print("\nВосстановленный объект:")
    restored_student.show_info()
if __name__ == "__main__":
    main()
