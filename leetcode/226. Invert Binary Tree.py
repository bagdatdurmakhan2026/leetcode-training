class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # Меняем местами левого и правого потомка
        root.left, root.right = root.right, root.left

        # Рекурсивно повторяем для обоих поддеревьев
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# --- Блок для локальной проверки ---
if __name__ == "__main__":
    # Собираем дерево из примера:
    #     4
    #    / \
    #   2   7
    #  / \ / \
    # 1  3 6  9
    root = TreeNode(
        4,
        left=TreeNode(2, TreeNode(1), TreeNode(3)),
        right=TreeNode(7, TreeNode(6), TreeNode(9)),
    )

    print("До инверсии:")
    print(f"Корень: {root.val}, левый: {root.left.val}, правый: {root.right.val}")
    print(f"Дети левого (2): {root.left.left.val}, {root.left.right.val}")

    # Вызываем функцию
    sol = Solution()
    inverted = sol.invertTree(root)

    print("\nПосле инверсии:")
    print(f"Корень: {inverted.val}, левый: {inverted.left.val}, правый: {inverted.right.val}")
    print(f"Дети нового левого (7): {inverted.left.left.val}, {inverted.left.right.val}")