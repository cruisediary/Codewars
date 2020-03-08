"""
https://www.codewars.com/kata/55847fcd3e7dadc9f800005f/train/python

Binary Tree Compare

Given the node object:

Node:
  val: <int>,
  left: <Node> or null,
  right: <Node> or null
write a function compare(a, b) which compares the two trees defined by Nodes a and b and returns true if they are equal in structure and in value and false otherwise.

Examples:

1       1
| \     | \
2  3    2  3
=> true

1       1
| \     | \
3  3    2  3
=> false (values not the same 2 != 3)

1       1
| \     |
2  3    2
        |
        3
=> false (structure not the same)

"""

def compare(a, b):
    if a and b:
        return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)
    return True if not a and not b else False
        

"""

Sample Tests


class Node:
  def __init__(self, val, left, right):
    self.val = val
    self.left = left
    self.right = right

a_node = Node(1, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)

Test.describe("example tests")

results1 = compare(a_node, b_node);
Test.it("Should return true for equal nodes")
Test.assert_equals(results1, True)

results2 = compare(a_node, c_node);
Test.it("Should return false for non-equal nodes")
Test.assert_equals(results2, False)


"""
