import json
from builder import Builder
from factory import Factory
from different_icon_family import *
from display_visitor import *
from display_visitor import *
from iterator import *

# 从文件中读取JSON数据
def load_data_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # 读取JSON数据
    json_file_path = 'data.json'
    data = load_data_from_file(json_file_path)
    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族1
    icon_family = ConstellationIconFamily()
    # 创建访问者
    visitor = TreeDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    # 创建访问者
    visitor = RectangleDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建tree工厂
    factory = Factory.get_factory("tree")
    # 创建节点树并展示
    builder = Builder(factory)
    root = builder.build(data)
    # 图标族2
    icon_family = NumberIconFamily()
    # 创建访问者
    visitor = TreeDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

    # 创建rectangle工厂
    factory = Factory.get_factory("rectangle")
    builder = Builder(factory)
    root = builder.build(data)
    # 创建访问者
    visitor = RectangleDisplayVisitor()
    iterator = Iterator(root)
    for node in iterator:
        node.accept(visitor, icon_family)
    print()

if __name__ == "__main__":
    main()