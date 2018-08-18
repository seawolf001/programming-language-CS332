from __future__ import print_function
from collections import deque

class HeapAllocationError(Exception):
    def __init__(self,message):
        super(HeapAllocationError, self).__init__(message)

class HeapDeallocationError(Exception):
    def __init__(self, message):
        super(HeapDeallocationError, self).__init__(message)

class AllocationStrategyError(Exception):
    def __init__(self, message):
        super(AllocationStrategyError, self).__init__(message)


class Heap():
    '''
        Heap for allocating and deallocating objects dynamically
        Takes input size of heap and an allocation strategy
        Allocation Strategy -> 1. First Fit     2. Best Fit      3. Worst Fit
        Allocate using ->   allocate space_needed     
                            returns an identifier for that space allocated
                            raise HeapAllocationError if unable to allocate 
        Deallocate using -> deallocate identifier  
                            returns None
                            raises HeapDeallocation error if unable to deallocate 
        Defragments the heap every time HeapAllocation Error is raised 
    '''
    FIRST_FIT = 'First Fit'
    BEST_FIT = 'Best Fit'
    WORST_FIT = 'Worst Fit'

    def __init__(self, size, allocation_strategy):
        if allocation_strategy not in [Heap.FIRST_FIT, Heap.BEST_FIT, Heap.WORST_FIT]:
            raise AllocationStrategyError('Invalid Allocation Strategy')
        self.size = size
        self.heap = [None] * size
        self.allocation_strategy = allocation_strategy
        self.index = 0 # used for assigning random variable name to allocated space
        self.allocated_space = {}
        self.free_list = [[0,size-1]]

    def defragment(self):
        print('\n\n.......................Wait Defragmanting .....................\n\n')
        index = 0
        for key,value in self.allocated_space.iteritems():
            pre_index, size = value, self.heap[value]
            self.heap[index] = size
            self.allocated_space[key] = index
            index += size
        self.free_list = [[index,self.size-1]]


    def assign_block(self,size, free_list_index):
        self.index += 1
        identifier = 'p' + str(self.index)
        start, end = self.free_list[free_list_index]
        self.allocated_space[identifier] = start
        self.heap[start] = size + 1
        if start - end == size:
            self.free_list.pop(free_list_index)
        else:
            self.free_list[free_list_index][0] += size + 1
            if self.free_list[free_list_index][0] > self.free_list[free_list_index][1]:
                self.free_list.pop(free_list_index)
        return identifier

    def first_fit(self,size):
        flag = False
        length = len(self.free_list)
        for index, free_range in enumerate(self.free_list):
            start, end = free_range[0], free_range[1]
            if end - start>= size:
                identifier = self.assign_block(size,index)
                flag = True
        if flag:    
            return identifier
        else:
            raise HeapAllocationError('Not Enough Space to allocate stuff')

    def best_fit(self,size):
        flag = False
        length = len(self.free_list)
        minimum = self.size + 1
        min_index = -1
        for index, free_range in enumerate(self.free_list):
            start, end = free_range[0], free_range[1]
            if end - start >= size and end - start < minimum:
                minimum = end - start
                min_index = index
        if min_index == -1:
            raise HeapAllocationError('Not Enough Space to allocate stuff')
        else:
            identifier =  self.assign_block(size, min_index)
            return identifier

    def worst_fit(self,size):
        flag = False
        length = len(self.free_list)
        maximum = 0
        max_index = -1
        for index, free_range in enumerate(self.free_list):
            start, end = free_range[0], free_range[1]
            if end - start > maximum:
                maximum = end - start
                max_index = index
        if max_index == -1 or maximum < size:
            raise HeapAllocationError('Not Enough Space to allocate stuff')
        else:
            identifier =  self.assign_block(size, max_index)
            print(heap.free_list, heap.allocated_space)
            return identifier

    def _allocate(self,size):
        if self.allocation_strategy == Heap.FIRST_FIT:
            return self.first_fit(size)
        elif self.allocation_strategy == Heap.BEST_FIT:
            return self.best_fit(size)
        elif self.allocation_strategy == Heap.WORST_FIT:
            return self.worst_fit(size)
        else:
            raise AllocationStrategyError('Invalid Allocation Strategy')

    def allocate(self, size):
        try:
            identifier = self._allocate(size)
            return  'Identifier : ' + identifier + '   allocated at index ' + str(self.allocated_space[identifier]) +\
                    ' of size ' + str(self.heap[self.allocated_space[identifier]])
        except HeapAllocationError:
            self.defragment()
            identifier = self._allocate(size)
            return  'Identifier : ' + identifier + '   allocated at index ' + str(self.allocated_space[identifier]) +\
                    ' of size ' + str(self.heap[self.allocated_space[identifier]])

    def deallocate(self,identifier):
        try:
            start_index = self.allocated_space[identifier]
            end_index = start_index + self.heap[start_index] -1
            flag = False
            for index, free_range in enumerate(self.free_list):
                if free_range[0] == end_index + 1 :
                    self.free_list[index][0] = start_index
                    flag = True
                    break
                elif free_range[1] == start_index - 1:
                    self.free_list[index][1] = end_index
                    flag = True
                    break
            if not flag:
                self.free_list.append([start_index,end_index])
            del self.allocated_space[identifier]
        except KeyError:
            raise HeapDeallocationError('Invalid object identifier provided')


strategy_list = ['First Fit', 'Best Fit', 'Worst Fit','1','2','3']
while True:
    try:
        heap_size = int(raw_input('Enter the size of the heap : '))
        allocation_strategy = raw_input('Enter the allocation strategy\n1 First Fit\n2 Best Fit\n3 Worst Fit : ').strip().rstrip().title()
        if allocation_strategy not in strategy_list:
            allocation_strategy = 't '.join(allocation_strategy.split('t',1)).title()
            print(allocation_strategy)
            if allocation_strategy not in strategy_list:
                raise AllocationStrategyError('Please enter a valid choice of allocation strategy')
        index = strategy_list.index(allocation_strategy)
        break
    except ValueError:
        print('Enter a valid Integer. Try Again!!!!')
    except AllocationStrategyError as e:
        print(type(e).__name__, ' : ', e)

if index > 2:
    index -= 3
print('Heap Size Chosen : ', heap_size, '\nAllocation Strategy : ', strategy_list[index])
heap = Heap(size=heap_size, allocation_strategy=strategy_list[index])

print(Heap.__doc__)

while True:
    query = raw_input('Enter Query :  ').strip().rstrip()
    try:
        query = map(lambda a : a.title(), query.split())
        if query[0] == 'Exit':
            break
        elif query[0] == 'Help':
            print(Heap.__doc__)
        elif query[0] == 'Allocate':
            size = int(query[1])
            print(heap.allocate(size),end='\n\n')
        elif query[0] == 'Deallocate':
            heap.deallocate(query[1].lower())
            print('Successfully deallocated', query[1], end='\n\n')
    except (IndexError, ValueError):
        print('Invalid Query : Type \'help\' to see how to run query')
    except (HeapDeallocationError, HeapAllocationError, AllocationStrategyError) as e:
        print(type(e).__name__, ' : ', e, end='\n\n')