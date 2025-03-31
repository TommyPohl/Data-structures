from LinkedList import LinkedList
from stack import stack


s = stack()

print(s.is_empty())
s.push(22)
s.push(23)
s.push(24)
print(s.peek())
print(s.pop())
print(s.peek())
print(s.is_empty())

"""l = LinkedList()

l.append(2)
l.append(3)
l.append("Ahoj")
l.append([1,2,3])

print(l.head)
print(l.head.next)
print(l.head.next.next)
print(l.head.next.next.next)"""