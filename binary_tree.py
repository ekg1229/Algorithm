class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            node.key = self._get_min_value(node.right)
            node.right = self._delete_recursive(node.right, node.key)
        return node

    def _get_min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.key

# 이진 트리 생성 및 사용 예시
binary_tree = BinaryTree()

# 임의의 노드 삽입
binary_tree.insert(6)
binary_tree.insert(3)
binary_tree.insert(9)
binary_tree.insert(2)
binary_tree.insert(4)
binary_tree.insert(6)
binary_tree.insert(8)

# 특정 값 검색
search_key = 4
search_result = binary_tree.search(search_key)
if search_result:
    print(f"값 {search_key}를 찾았습니다.")
else:
    print(f"값 {search_key}를 찾지 못했습니다.")

# 특정 값 삭제
delete_key = 7
binary_tree.delete(delete_key)
print(f"값 {delete_key}를 삭제하였습니다.")
