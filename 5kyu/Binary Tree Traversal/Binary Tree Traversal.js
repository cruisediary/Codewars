/*
https://www.codewars.com/kata/5268956c10342831a8000135/train/javascript

Binary Tree Traversal

Given the root node of a binary tree (but not necessarily a binary search tree,) write three functions that will print the tree in pre-order, in-order, and post-order.

A Node has the following properties:

var data; // A number or string.
Node left; // Undefined if there is no left child.
Node right; // Undefined if there is no right child.
The structure of a tree looks like:

data Tree a = Nil | Node (Tree a) a (Tree a)
Pre-order means that we
1.) Visit the root.
2.) Traverse the left subtree (left node.)
3.) Traverse the right subtree (right node.)

In-order means that we
1.) Traverse the left subtree (left node.)
2.) Visit the root.
3.) Traverse the right subtree (right node.)

Post-order means that we
1.) Traverse the left subtree (left node.)
2.) Traverse the right subtree (right node.)
3.) Visit the root.

Let's say we have three Nodes.

var a = new Node("A");
var b = new Node("B");
var c = new Node("C");

a.left = b;
a.right = c;
Then, preOrder(a) should return ["A", "B", C"]
inOrder(a) should return ["B", "A", "C"]
postOrder(a) should return ["B", "C", A"]

What would happen if we did this?

var d = new Node("D");
c.left = d;
preOrder(a) should return ["A", "B", "C", "D"]
inOrder(a) should return ["B", "A", "D", "C"]
postOrder(a) should return ["B", "D", "C", "A"]

*/

/*
A Node has the following properties:
var data; // A number or string.
Node left; // Undefined if there is no left child.
Node right; // Undefined if there is no right child.
*/

// 1.) Root node, 2.) traverse left subtree, 3.) traverse right subtree.
function preOrder(node) {
  return node == undefined ? [] : [node.data].concat(preOrder(node.left), preOrder(node.right))
}

// 1.) Traverse left subtree, 2.) root node, 3.) traverse right subtree.
function inOrder(node) {  
  return node == undefined ? [] :inOrder(node.left).concat([node.data], inOrder(node.right))
}

// 1.) Traverse left subtree, 2.) traverse right subtree, 3.) root node.
function postOrder(node) {
  return node == undefined ? [] :postOrder(node.left).concat(postOrder(node.right), [node.data])
}

/*

Sample Tests

var a = new Node(5);
var b = new Node(10);
var c = new Node(2);
a.left = b;
a.right = c;

Test.assertSimilar(preOrder(a), [a.data, b.data, c.data], "preOrder failed, expected " + [a.data, b.data, c.data].toString());
Test.assertSimilar(preOrder(b), [b.data], "preOrder failed, expected " + [b.data].toString());
Test.assertSimilar(preOrder(c), [c.data], "preOrder failed, expected " + [c.data].toString());

Test.assertSimilar(inOrder(a), [b.data, a.data, c.data], "inOrder failed, expected " + [b.data, a.data, c.data].toString());
Test.assertSimilar(inOrder(b), [b.data], "inOrder failed, expected " + [b.data].toString());
Test.assertSimilar(inOrder(c), [c.data], "inOrder failed, expected " + [c.data].toString());

Test.assertSimilar(postOrder(a), [b.data, c.data, a.data], "postOrder failed, expected " + [b.data, c.data, a.data].toString());
Test.assertSimilar(postOrder(b), [b.data], "postOrder failed, expected " + [b.data].toString());
Test.assertSimilar(postOrder(c), [c.data], "postOrder failed, expected " + [c.data].toString());

*/
