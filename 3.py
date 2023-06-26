# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.
things = {"термос": 2, "кипятильник": 1, "палатка": 8, "спальник": 5, "кастрюля": 3, "лопата": 3}
def backpack_capacity(capacity: int, things: dict) -> list[str]:
    equipment_option = []
    for key, value in things.items():
        if value <= capacity:
            capacity -= value
            equipment_option.append(key)
    return equipment_option
print(backpack_capacity(15, things))