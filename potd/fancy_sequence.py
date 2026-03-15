class Fancy:

    def __init__(self):
        self.arr = []
        self.a = 1
        self.b = 0
        self.MOD = 10**9+7

    def append(self, val: int) -> None:
       inv_a = pow(self.a, self.MOD -2, self.MOD)
       stored = (val - self.b) * inv_a % self.MOD
       self.arr.append(stored)

    def addAll(self, inc: int) -> None:
        self.b = (self.b +inc)%self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m)%self.MOD
        self.b = (self.b * m)%self.MOD
        
    def getIndex(self, idx: int) -> int:
        if idx >= len(self.arr):
            return -1
        return (self.arr[idx] *self.a + self.b) % self.MOD                         
    

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)   
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
if __name__ == "__main__":
    obj = Fancy()
    obj.append(2) # arr = [2]
    obj.addAll(3) # arr = [5]
    obj.append(7) # arr = [5, 7]
    print(obj.getIndex(0)) # o/p 5
    obj.multAll(2) # arr = [10, 14]
    print(obj.getIndex(0)) # o/p 10
    print(obj.getIndex(1)) # o/p 14
    obj.addAll(3) # arr = [13, 17]
    obj.append(10) # arr = [13, 17, 10]
    obj.multAll(2) # arr = [26, 34, 20]
    print(obj.getIndex(0)) # o/p 26
    print(obj.getIndex(1)) # o/p 34
    print(obj.getIndex(2)) # o/p 20

# 1622. Fancy Sequence    
# lazy math transformation here we tried the operations as a linear transformation of the form f(x) = ax + b, where a and b are updated based on the operations performed.
# When we append a value, we need to store the inverse transformation to retrieve the original value later when we call getIndex. 
# This way, we can efficiently handle all operations without needing to update every element in the array for each operation. so instead of applying the transformations to all elements in the array, 
# we can just keep track of the parameters a and b, and apply them on-the-fly when retrieving values. This allows us to perform addAll and multAll operations in O(1) time, 
# so all operations can take o(1) time, and getIndex can also take o(1) time. The space complexity is O(n) for storing the appended values.
# ax+b=val, Solving for x:x=(val-b)/a
# we store: stored = (val - b) / a and when we retrieve, we apply the transformation: result = stored * a + b. We also need to take care of the modulo operation to ensure that our 
# calculations remain within bounds.
# stored_value → (multiply by a) → (add b) → real_value
# Division is not allowed in modular arithmetic.
# Instead we multiply by the modular inverse.x/a≡x *a**(-1) (mod MOD):  a**(-1)=a**(MOD-2)(modMOD) (using Fermat's Little Theorem because MOD is prime)
