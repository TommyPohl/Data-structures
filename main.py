from LinkedList import LinkedList

l = LinkedList()

l.append(2)
l.append(3)
l.append("Ahoj")
l.append([1,2,3])

print(l.head)
print(l.head.next)
print(l.head.next.next)
print(l.head.next.next.next)