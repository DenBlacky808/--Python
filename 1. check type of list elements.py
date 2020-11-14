elements = [12, 12.3, True,
            [1, 2], 'str', (1, 2),
            {'key_1': 500, 'key_2': 200}, None,
            (5 + 3J), {1, 2}, bytes(b'some type'), bytearray(b'some type'), Exception]

for element in elements:
    print(type(element))
