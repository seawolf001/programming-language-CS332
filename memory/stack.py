class StackOverflowException(Exception):
    def __init__(self,message):
        super(StackOverflowException, self).__init__(message)


class StackUnderflowException(Exception):
    def __init__(self, message):
        super(StackUnderflowException, self).__init__(message)


class InvalidQueryException(Exception):
    def __init__(self, message):
        super(InvalidQueryException, self).__init__(message)


class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = [-1]*size
        # print self.stack
        self.top = size

    def push(self,size):
        try:
            top = self.top
            top -= ( size + 1)
            if top < 0:
                raise StackOverflowException('Not Enough Space to allocate on stack')
            self.stack[top] = self.top
            self.top = top
        except IndexError:
            raise StackOverflowException('Not Enough Space to allocate on stack')

    def pop(self):
        try:
		  self.top = self.stack[self.top]
        except IndexError:
            raise StackUnderflowException('Nothing is allocated on the stack')


def print_help():
    print ''
    print 'pop -> pops the element from stack (raises StackUnderflowException if stack is empty)' 
    print 'push int -> push frame of size int to stack (raises StackOverflowException if enough space on stack not available)'
    print 'exit -> exits the program'
    print ''

while True:
    try:
        stack_size = int(raw_input('Enter Stack Size: '))
        stack = Stack(stack_size)
        break
    except ValueError:
        print 'Error : Enter proper integer'

print_help()
while True:
    query = raw_input('Enter query:\t').strip().rstrip().lower()
    try:
        if query == 'exit':
            break
        elif query == 'help':
        	print_help()
        elif query == 'pop':
            stack.pop()
        elif query.find('push') == 0:
            query = query.split()
            if len(query) != 2:
                raise InvalidQueryException('Invalid Push Query. Type "help" for knowing list of commands')
            stack.push(int(query[1]))
        else:
            raise InvalidQueryException('Invalid Query. Type "help" for knowing list of commands')
        # import pdb; pdb.set_trace()
    except InvalidQueryException as e:
        print e
    except StackUnderflowException as e:
        print e
    except StackOverflowException as e:
        print e
    except IndexError as e:
        print e
    except ValueError as e:
        print e