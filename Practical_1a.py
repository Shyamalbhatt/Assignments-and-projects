'''
Write a program to store the elements in 1-D array and provide an option to perform 
the operatons like searching, sorting, merging, reversing the elements.
'''
class OneD:
    def __init__(self, a):
        self.array = a

    def search(self, e):
        if e in self.array:
            return True
        return False

    def sort(self):
        for i in range(len(self.array)):
            lowest_value_index = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[lowest_value_index]:
                    lowest_value_index = j
            self.array[i], self.array[lowest_value_index] = self.array[lowest_value_index], self.array[i]
        return self.array

    def merg(self,l):
        self.array = self.array + l
        return self.array

    def reverse(self):
        return self.array[::-1]

a = [5,6,7,89,2,5,6,1]
o = OneD(a)
print(o.sort())
print(o.search(89))
print(o.merg([8,5,7,9,3]))
print(o.reverse())
