class ArraySet: 
       def __init__(self):
             self.array = [] 
             self.size = 0 

       def contains(self, e): 
              low, high = 0, self.size – 1
             
              while low <= high: 
                     mid = (low + high) // 2 
                     mid_val = self.array[mid] 
           
                     if mid_val == e: 
                            return True 

                     elif mid_val < e: 
                            low = mid + 1 

                     else: 
                           high = mid – 1
       return False 

def insert(self, e): 
       if not self.contains(e) and not self.isFull(): 
                 # 이진 탐색을 통해 원소를 삽입할 위치를 찾습니다. 
index = self._binary_search(e)

                 # 찾은 위치에 원소를 삽입합니다.          
                 self.array[index+1:self.size+1] = self.array[index:self.size]
             self.array[index] = e 
             self.size += 1 

# 나머지 메서드들은 동일하게 유지됩니다. 

def _binary_search(self, e): 
         # 이진 탐색을 통해 원소를 삽입할 위치를 찾습니다. 
       low, high = 0, self.size - 1 

       while low <= high: 
               mid = (low + high) // 2 
               mid_val = self.array[mid]

               if mid_val < e:
                      low = mid + 1
               elif mid_val > e: 
                      high = mid - 1 
               else: 
                     return mid # 이미 있는 경우 해당 인덱스 반환 

        return low # 찾은 위치를 반환
