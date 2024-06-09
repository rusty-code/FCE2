
from source.IOFILESTREEM import FileInstance as File
from source.TREE import BinaryTree

# validated data
def vdata(data):
    try:
        return int(data)
    except:
        return None

# validated path
def is_path(path : str) -> bool:
    for word in path:
        if not word in '01': return False
    return True

def main(path = "./source/files/resource2"):

    print()
    # read the data and div ' '
    data = []
    for line in File(path).data():
        data.append(line.split())

    # build tree
    tree = BinaryTree()
    for line in range(0, len(data)):
        apnd = data[line]
        
        if len(apnd) == 2:
            if not vdata(apnd[0]) is None and not vdata(apnd[1]) is None:
                if is_path(apnd[1]):
                    tree.append_bypath(data=int(apnd[0]), path=apnd[1])
                else:
                    print("(ОШИБКА) Некорректые данные:")
                    print(f"(ОШИБКА) Файл : {path}, строка : {line+1}, число : {apnd[0]}, путь : {apnd[1]}")    
            else:
                print("\n(ОШИБКА) Некорректые данные:")
                print(f"(ОШИБКА) Файл : {path}, строка : {line+1}, число : {apnd[0]}, путь : {apnd[1]}")
        else: 
            print(f"(ОШИБКА) Отсутвие или несоответсвие данных данных:")
            print(f"(ОШИБКА) Файл : {path}, строка : {line+1}")


    if not tree.verified(tree._head):
        print("(ОШИБКА) Исходные пути дерева не полные..")
        print("(ОШИБКА) Невозмоность сборки.")
        print("(ОШИБКА) Добавьте путь и значение к потомкам со значением 'None'")
        print("(ОШИБКА): ", end=' ')
    else:
        print()
        print("Дерево успешно построено.")


    print(tree.format(tree._head))
    print("\n(ОПИСАНИЕ ФОРМАТА ВЫВОДА ДЕРЕВА):")
    print("    <дерево>::=")
    print("        ((<левое поддерево>)<вершина>(<правоеподдерево>))")  
    print("        ((<левое поддерево>)<вершина>)") 
    print("        (<вершина>(<правое поддерево>))")
    print("    <вершина>::=")
    print("        <цифра><цифра>")
    print("        <цифра>")
    print("    <левое поддерево>::=")
    print("        <дерево>")
    print("    <правое поддерево>::=")
    print("        <дерево")


if __name__ == "__main__":
    main() 