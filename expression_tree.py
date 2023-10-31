from tree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """An arithmetic expression tree."""

    def __init__(self, token, left=None, right=None):
        """Create an expression tree.

        In a single parameter form, the token should be a leaf value (e.g., 42),
        and the expression tree will have that value at an isolated node.

        In a three-parameter version, the token should be an operator,
        and left and right should be existing ExpressionTree instances
        that become the operands for the binary operator.
        """
        super().__init()  # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError("Token must be a string")
        self.add_root(token)  # use inherited, nonpublic method
        if left is not None:  # presumably three-parameter form
            if token not in "+-*x/":
                raise ValueError("Token must be a valid operator")
            self.attach(self.root(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        """Return a string representation of the expression."""
        pieces = []  # sequence of piecewise strings to compose
        self.parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def parenthesize_recur(self, p, result):
        """Append a piecewise representation of p's subtree to the resulting list."""
        if self.is_leaf(p):
            result.append(str(p.element()))  # leaf value as a string
        else:
            result.append("(")  # opening parenthesis
            self.parenthesize_recur(self.left(p), result)  # left subtree
            result.append(p.element())  # operator
            self.parenthesize_recur(self.right(p), result)  # right subtree
            result.append(")")  # closing parenthesis

    def evaluate(self):
        """Return the numeric result of the expression."""
        return self.evaluate_recur(self.root())

    def evaluate_recur(self, p):
        """Return the numeric result of the subtree rooted at p."""
        if self.is_leaf(p):
            return float(p.element())  # we assume the element is numeric
        else:
            op = p.element()
            left_val = self.evaluate_recur(self.left(p))
            right_val = self.evaluate_recur(self.right(p))
            if op == "+":
                return left_val + right_val
            elif op == "-":
                return left_val - right_val
            elif op == "/":
                return left_val / right_val
            else:
                return left_val * right_val  # treat "x" or as multiplication


def build_expression_tree(tokens):
    """Returns an ExpressionTree based on a tokenized expression."""
    S = []  # we use a Python list as a stack
    for t in tokens:
        if t in "+-x*/":  # t is an operator symbol
            S.append(t)  # push the operator symbol
        elif t not in '()':  # consider t to be a literal
            S.append(ExpressionTree(t))  # push a trivial tree storing the value
        elif t == ')':  # compose a new tree from three constituent parts
            right = S.pop()  # right subtree as per LIFO
            op = S.pop()  # operator symbol
            left = S.pop()  # left subtree
            S.append(ExpressionTree(op, left, right))  # repush the tree
            # We ignore a left parenthesis
    return S.pop()

