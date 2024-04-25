import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def clear(self):
        self.head = None
    
    def quickSort(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]

            return self.quickSort(less_than_pivot) + [pivot] + self.quickSort(greater_than_pivot)

    def jumpSearchID(self, id, tipe):
        current = self.head
        daftarId = []

        if tipe == "tugas":
            while current:
                daftarId.append(current.data["ID_Tugas"])
                current = current.next

        elif tipe == "laporan":
            while current:
                daftarId.append(current.data["ID_Laporan"])
                current = current.next

        daftarId = self.quickSort(daftarId)

        n = len(daftarId)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and daftarId[min(step, n) - 1] < id:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None

        while daftarId[prev] < id:
            prev += 1
            if prev == min(step, n):
                return None

        if daftarId[prev] == id:
            current = self.head
            if tipe == "tugas":
                while current:
                    if current.data["ID_Tugas"] == id:
                        return current
                    current = current.next
            if tipe == "laporan":
                while current:
                    if current.data["ID_Laporan"] == id:
                        return current
                    current = current.next
        else:
            return False