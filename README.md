## Logic-gates

## (RU):

Это простая библиотека которая добавляет 1 функцию, которая добавляет логические вентили такие как AND, OR, XOR и из инвертирующие версии

## Как пользоваться:

```python
from lgcgear import mulgear
```

Не забудьте что что-бы использовать эту библеотеку в других скриптах вы должны обернуть этот файл в папку и все скрипты в неё!

**Порядок аргументов:**
Первым ставьте, будет ли вентиль инвертирующим (`True`/`False`), затем сам тип вентиля (`str`), и потом входы (их количество бесконечно).

**Лайфхак:** Чтобы сделать обычный вентиль **NOT** (НЕ), просто включите инверсию для вентиля **buf**:
```python
print(mulgear(True, "buf", False)) # Выведет: True
```

Например:
```python
print(mulgear(True, "and", False, True)) # выведет: True
```

## (EN):

This is a simple single-function library that adds digital logic gate simulations such as AND, OR, XOR, and their inverted versions (NAND, NOR, XNOR).

## How to use:

```python
from lgcgear import mulgear
```

Don't forget that to use this library in other scripts, you must wrap this file in a folder and all the scripts in it!

**Argument order:**
1. `ifnot` (bool) — whether to invert the gate result (`True`/`False`).
2. `geartype` (str) — the type of gate ("buf", "and", "or", "xor").
3. `*inputs` (bool) — gate inputs (you can pass an infinite number of arguments).

💡 **Tip:** To create a standard **NOT** gate, simply enable inversion on a **buf** gate:
```python
print(mulgear(True, "buf", False)) # Output: True
```

Example:
```python
print(mulgear(True, "and", False, True)) # Output: True
```
