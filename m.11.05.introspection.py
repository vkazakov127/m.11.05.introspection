# -*- coding: utf-8 -*-
# m.11.05.introspection.py
import inspect

def introspection_info(obj1):
    my_inspect = {}  # Словарь на выход
    # ----- type(obj1)
    type_str = str(type(obj1))
    # Избавляемся от ненужных букв
    type_str = (type_str.replace('class ', '')).replace('<', '')
    type_str = (type_str.replace('>', '')).replace("'", "")
    type_str = type_str.replace("__main__.", "")
    # Сохраняем всё нажитое непосильным трудом
    my_inspect['type'] = type_str
    # ----- getmodule(obj1)
    module_str = str(inspect.getmodule(obj1))
    # Избавляемся от ненужных букв
    module_str = ((module_str.replace("<module ", "")).replace('>', '')).replace("'", "")
    module_str = module_str[:module_str.find('from') - 1] if ('from' in module_str) else module_str
    # Сохраняем всё нажитое непосильным трудом
    my_inspect['module'] = module_str
    # ----- getmembers()
    methods = inspect.getmembers(obj1, inspect.ismethod)
    functions = inspect.getmembers(obj1, inspect.isfunction)
    attributes = inspect.getmembers(obj1, not inspect.ismethod)
    # Сохраняем всё нажитое непосильным трудом
    my_inspect['methods'] = methods
    my_inspect['functions'] = functions
    my_inspect['attributes'] = attributes
    return my_inspect


class SomeClass:  # Модель класса для испытания интроспекции
    def __init__(self):
        self.attribute1 = 27

    def some_method(self):
        self.attribute1 += 10


# --- int
print('--- int')
print(introspection_info(42))
# --- str
print('--- str')
print(introspection_info('String example'))
# --- tuple
print('--- tuple')
print(introspection_info((1, 2, 1, 2, 1, 2)))
# --- SomeClass
print('--- SomeClass')
print(introspection_info(SomeClass()))
print('----------- The End -----------')
