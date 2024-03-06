from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    # реалізація класу
    # перевірка довжини номера
    def __init__(self, value):
        if not len(str(value)) == 10:
            raise ValueError("Please provide a 10-digit number.")
            
            
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        for to_remove in self.phones:
            if str(to_remove) == phone:
                self.phones.remove(to_remove)
                break

    def edit_phone(self, old_phone, new_phone):
        count = 0
        for p in self.phones:

            if old_phone == str(p):
                self.remove_phone(old_phone)
                self.add_phone(new_phone)
                count += 1
            elif count == 0:
                print("Phone number not found.")

    def find_phone(self, phone):
        for phone_to_find in self.phones:
            if phone == str(phone_to_find):
                return phone

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    # реалізація класу
    def __init__(self):
        self.data = {}

    def add_record(self, record):
        name = record.name.value
        name = record.name.value
        if name not in self.data:
            self.data[name] = record
        else:
            print("Record with this name already exist")

    def remove_record(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print("Record not found.")

    def find_record(self, name):
        return self.data.get(name)

    def add_phone_to_record(self, name, phone):
        if name in self.data:
            self.data[name].add_phone(phone)
        else:
            print("Record not found.")

    def delete(self, name):
        count = 0
        if name in self.data:
            self.data.pop(name)
            count += 1
        elif count == 0:
            print("Record not found.")

    def edit_phone_in_record(self, name, old_phone, new_phone):
        if name in self.data:
            self.data[name].edit_phone(old_phone, new_phone)
        else:
            print("Record not found.")

    def find(self, name):
        if name in self.data.keys():
            return self.data.get(name)
        else:
            print("Record not found.")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")


# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
book.find("Jane")
