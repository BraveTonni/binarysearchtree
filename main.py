# создать алгоритм для организации поиска по документу (.txt)
# простое бинарное дерево с индексами
import time
import tracemalloc

from dataclasses import dataclass

from typing import Optional


# каждый узел имеет не больше 2х потомков
# всё что слева - меньше
# всё что справа - больше
@dataclass(slots=True)
class Node:
    """узел, имеющий двух потомков: слева-справа"""
    index: int
    data: str

    left: Optional['Node'] = None
    right: Optional['Node'] = None


class FileManager:
    """Утилитный класс для управления файлами"""
    @staticmethod
    def get_lines(name: str) -> list[str]:
        """получение строчек из файла"""
        with open(name, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines()]

        return lines


class BinaryTree:
    """Класс бинарного дерева поиска"""
    def __init__(self):
        self.root: Optional[Node] = None  # корневой элемент дерева

    def append_node(self, node: Node) -> Node:
        """добавление узла в дерево"""
        # установка корневой вершины
        if self.root is None:
            self.root = node
            return node

        # сортировка узла влево/вправо в зависимости от длины корневой строки
        cursor = self.root
        while True:
            if node.data < cursor.data:
                if cursor.left is None:
                    cursor.left = node
                    return node
                
                cursor = cursor.left
                continue

            if cursor.right is None:
                cursor.right = node
                return node
            
            cursor = cursor.right

    def find(self, data: str) -> Optional[Node]:
        """поиск узла в дереве"""
        cursor = self.root

        while cursor:
            if data == cursor.data:
                return cursor
            elif data < cursor.data:
                cursor = cursor.left
            else:
                cursor = cursor.right

        return None


def main():
    tracemalloc.start()
    # TopRussian.txt
    lines = FileManager.get_lines(input("Введите имя файла: "))

    tree = BinaryTree()

    start = time.perf_counter()

    for i, line in enumerate(lines):
        node = Node(index=i, data=line)
        tree.append_node(node)
        if i % 20000 == 0:
            print(f"Добавлено {i} строк в дерево")

    end = time.perf_counter()
    print(f"Построение дерева заняло: {(end - start):.6f} секунд")

    # Замеряем ОЗУ после построения дерева
    current, peak = tracemalloc.get_traced_memory()

    print(f"current: {current / 1024 / 1024:.2f} MB")
    print(f"peak: {peak / 1024 / 1024:.2f} MB")

    while True:
        result: Optional[Node] = tree.find(input("ENTER: "))
        start = time.perf_counter()
                
        if result:
            print(f"Найдено на строке {result.index + 1}: {result.data}")
        else:
            print("Не найдено")


        end = time.perf_counter()
        print(f"- Алгоритм отработал за: {(end - start):.6f} секунд")


if __name__ == "__main__":
    main()