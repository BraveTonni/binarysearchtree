# binarysearchtree

Console tool that indexes a text file into a binary search tree and looks up lines from it.

## How it works

Each line of the file becomes a node together with its line number. Insert and search follow the usual rule: left is smaller, right is larger. Build time and memory usage are printed, so results can be compared against a linear scan.

## Usage

```bash
python main.py
```

Enter the file name, wait for the index to build, then type words at the `ENTER:` prompt:

```
Введите имя файла: TopRussian.txt
Добавлено 20000 строк в дерево
Построение дерева заняло: 1.234567 секунд
ENTER: слово
Найдено на строке 42: слово
- Алгоритм отработал за: 0.000012 секунд
```

## Requirements

Python 3.10+. Standard library only.
