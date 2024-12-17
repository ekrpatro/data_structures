import pytest
from linked_list import LinkedList

def test_add_node():
    ll = LinkedList()
    ll.add_node("Task1")
    assert ll.head.data == "Task1"

def test_delete_node():
    ll = LinkedList()
    ll.add_node("Task1")
    ll.delete_node("Task1")
    assert ll.head is None
