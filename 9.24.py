# 이진 탐색 트리의 노드를 나타내는 클래스 정의
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # 왼쪽 자식 노드
        self.right = None  # 오른쪽 자식 노드

# 우선순위 큐를 구현하는 클래스 정의
class PriorityQueue:
    def __init__(self):
        self.root = None  # 우선순위 큐의 루트 노드

    # 우선순위 큐에 요소를 삽입하는 메서드
    def insert(self, value):
        if not self.root:  # 루트 노드가 비어있을 경우
            self.root = Node(value)  # 새로운 노드를 루트 노드로 설정
        else:
            self._insert_recursive(self.root, value)  # 재귀적으로 삽입 메서드 호출

    # 재귀적으로 삽입하는 메서드
    def _insert_recursive(self, current_node, value):
        if value >= current_node.value:  # 새로운 값이 현재 노드의 값보다 크거나 같은 경우
            if current_node.right is None:  # 오른쪽 자식이 비어있을 경우
                current_node.right = Node(value)  # 새로운 노드를 오른쪽 자식으로 추가
            else:
                self._insert_recursive(current_node.right, value)  # 오른쪽 자식으로 이동하여 재귀 호출
        else:  # 새로운 값이 현재 노드의 값보다 작은 경우
            if current_node.left is None:  # 왼쪽 자식이 비어있을 경우
                current_node.left = Node(value)  # 새로운 노드를 왼쪽 자식으로 추가
            else:
                self._insert_recursive(current_node.left, value)  # 왼쪽 자식으로 이동하여 재귀 호출

    # 최대값 노드를 찾는 메서드
    def _find_max_node(self, node):
        while node.right is not None:  # 노드의 오른쪽 자식이 None이 아닐 때까지 반복
            node = node.right  # 오른쪽 자식으로 이동
        return node  # 가장 큰 값을 가진 노드 반환

    # 최대 우선순위 요소를 추출하는 메서드
    def extract_max(self):
        if not self.root:  # 루트 노드가 비어있을 경우
            return None

        max_node = self._find_max_node(self.root)  # 최대값 노드 찾기

        if max_node == self.root:  # 최대값 노드가 루트 노드인 경우
            self.root = self.root.left  # 루트 노드를 왼쪽 자식으로 변경
        else:
            parent = self.root
            while parent.right != max_node:  # 부모 노드를 찾아서 최대값 노드의 위치 조정
                parent = parent.right
            parent.right = max_node.left  # 최대값 노드의 왼쪽 자식을 부모의 오른쪽으로 연결

        return max_node.value  # 최대값 반환

# 우선순위 큐 실행
priority_queue = PriorityQueue()
priority_queue.insert(5)
priority_queue.insert(2)
priority_queue.insert(10)
priority_queue.insert(7)

print(priority_queue.extract_max())  
print(priority_queue.extract_max()) 