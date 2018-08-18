import java.util.*;
import java.lang.*;

public class Heap_new {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter size of heap:");
        int h = in.nextInt();
        memory m = new memory(h);
        while (true) {
            System.out.println("Enter\n1: To allocate heap memory using best fit\n2: To allocate heap memory using first fit\n3: To allocate heap memory using worst fit\n4: To deallocate a block\n5: To display heap\n6: Exit");
            int c = in.nextInt();
            switch (c) {
                case 1:
                    System.out.println("Size of area to allocate:");
                    int h1 = in.nextInt();
                    int resh1 = m.bestfit(h1);
                    if (resh1 == -2)
                        System.out.println("Heap already full");
                    else if (resh1 == -1)
                        System.out.println("Size heap left too small to allocate");
                    else {
                        System.out.println("The address of new block is: " + resh1);
                        m.displayheap();
                    }
                    break;
                case 2:
                    System.out.println("Size of area to allocate:");
                    int h2 = in.nextInt();
                    int resh2 = m.firstfit(h2);
                    if (resh2 == -2)
                        System.out.println("Heap already full");
                    else if (resh2 == -1)
                        System.out.println("Size heap left too small to allocate");
                    else {
                        System.out.println("The address of new block is: " + resh2);
                        m.displayheap();
                    }
                    break;
                case 3:
                    System.out.println("Size of area to allocate:");
                    int h3 = in.nextInt();
                    int resh3 = m.worstfit(h3);
                    if (resh3 == -2)
                        System.out.println("Heap already full");
                    else if (resh3 == -1)
                        System.out.println("Size heap left too small to allocate");
                    else {
                        System.out.println("The address of new block is: " + resh3);
                        m.displayheap();
                    }
                    break;
                case 4:
                    System.out.println("Address of block to deallocate:");
                    int add = in.nextInt();
                    m.deallocate(add);
                    break;
                case 5:
                    m.displayheap();
                    break;
                case 6:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Not a valid input.");
                    break;
            }
        }
    }
}

class memory {
    private int[] heap;
    public int top;
    private int freeStart;

    memory(int h) {
        this.heap = new int[h];
        this.heap[0] = h;
        this.heap[1] = -1;
        for (int i = 2; i < h; i++)
            heap[i] = -2;
        this.freeStart = 0;
    }

    int firstfit(int l) {
        if (this.freeStart == this.heap.length)
            return -2;
        int t = this.freeStart;
        while (t != -1) {
            if ((this.heap[t] - 1) >= l)
                break;
            t = this.heap[t + 1];
        }
        if (t == -1)
            return -1;
        return allocate(t, l);
    }

    int bestfit(int l) {
        if (this.freeStart == this.heap.length)
            return -2;
        int t = this.freeStart;
        int min = this.heap.length + 10;
        int index = -1;
        while (t != -1) {
            if ((this.heap[t] - 1) >= l) {
                if (this.heap[t] < min) {
                    min = this.heap[t];
                    index = t;
                }
            }
            t = this.heap[t + 1];
        }
        if (index == -1)
            return -1;
        return allocate(index, l);
    }

    int worstfit(int l) {
        if (this.freeStart == this.heap.length)
            return -2;
        int t = this.freeStart;
        int max = -1;
        int index = -1;
        while (t != -1) {
            if ((this.heap[t] - 1) >= l) {
                if (this.heap[t] > max) {
                    max = this.heap[t];
                    index = t;
                }
            }
            t = this.heap[t + 1];
        }
        if (index == -1)
            return -1;
        return allocate(index, l);
    }

    private int allocate(int index, int l) {
        int nextFree = -1;
        if ((index + 1) < this.heap.length)
            nextFree = this.heap[index + 1];
        int free = this.heap[index];
        this.heap[index] = l + 1;
        if (this.heap[index + 1] == -1) {
            int t = this.freeStart;
            while (t != -1) {
                if (this.heap[t + 1] == index)
                    break;
                t = this.heap[t + 1];
            }
            if (t != -1)
                this.heap[t + 1] = -1;
        }
        for (int i = index + 1; i <= index + l; i++) {
            this.heap[i] = 1;
        }
        if (l == (free - 1)) {
            if (this.freeStart == index) {
                if (nextFree != -1)
                    this.freeStart = nextFree;
                else
                    this.freeStart = this.heap.length;
            }
        } else if ((free - l - 1) == 1) {
            this.heap[index + l + 1] = -5;
            if (this.freeStart == index) {
                if (nextFree != -1)
                    this.freeStart = nextFree;
                else
                    this.freeStart = this.heap.length;
            }
        } else if ((free - l - 1) > 1) {
            this.heap[index + l + 1] = free - l - 1;
            if (this.freeStart == index)
                this.freeStart = index + l + 1;
            this.heap[index + l + 2] = nextFree;
        }
        return index;
    }

    void deallocate(int index) {
        if (index >= this.heap.length - 1 || index < 0) {
            System.out.println("Index either last word or invalid");
            return;
        }
        if (this.heap[index + 1] != 1) {
            System.out.println("Invalid block address");
            return;
        }
        if (this.heap[index] + index < this.heap.length) {
            if (this.heap[this.heap[index] + index] == -5) {
                this.heap[this.heap[index] + index] = 1;
                this.heap[index] = this.heap[index] + 1;
            }
        }
        int length = this.heap[index];
        for (int i = index; i < index + length; i++) {
            this.heap[i] = -2;
        }
        if (this.freeStart > index) {
            if ((index + length) == this.heap.length) {
                this.heap[index] = length;
                this.heap[index + 1] = -1;
                this.freeStart = index;
            } else if ((index + length) == this.freeStart) {
                if (this.freeStart < this.heap.length) {
                    this.heap[index + 1] = this.heap[this.freeStart + 1];
                    this.heap[index] = length + this.heap[this.freeStart];
                    this.heap[this.freeStart] = -2;
                    this.heap[this.freeStart + 1] = -2;
                    this.freeStart = index;
                }
            } else {
                if (this.freeStart == this.heap.length)
                    this.heap[index + 1] = -1;
                else
                    this.heap[index + 1] = this.freeStart;
                this.heap[index] = length;
                this.freeStart = index;
            }
        } else {
            int t = this.freeStart;
            int count = this.freeStart;
            int flag = 0;
            while (t != -1) {
                count = count + this.heap[t];
                if (count == index)
                    break;
                else {
                    if (this.heap[count + 1] == 1) {
                        if (this.heap[t + 1] > index || this.heap[t + 1] == -1)
                            flag = 1;
                    }
                }
                if (flag == 1)
                    break;
                t = this.heap[t + 1];
            }
            if (flag == 1) {
                if ((index + length) == this.heap.length) {
                    this.heap[index] = length;
                    this.heap[index + 1] = -1;
                    this.heap[t + 1] = index;
                } else if ((index + length) == this.heap[t + 1]) {
                    if (this.heap[t + 1] < this.heap.length && this.heap[t + 1] >= 0) {
                        this.heap[index + 1] = this.heap[this.heap[t + 1] + 1];
                        this.heap[index] = this.heap[this.heap[t + 1]] + length;
                        this.heap[t + 1] = index;
                    }
                } else {
                    this.heap[index + 1] = this.heap[t + 1];
                    this.heap[index] = length;
                    this.heap[t + 1] = index;
                }
            } else {
                if ((index + length) == this.heap.length) {
                    this.heap[index] = length;
                    this.heap[index + 1] = -1;
                    this.heap[t + 1] = index;
                } else if ((index + length) == this.heap[t + 1]) {
                    if (this.heap[t + 1] < this.heap.length && this.heap[t + 1] >= 0) {
                        int temp = this.heap[t + 1];
                        this.heap[t] = this.heap[t] + length + this.heap[this.heap[t + 1]];
                        this.heap[this.heap[t + 1]] = -2;
                        this.heap[t + 1] = this.heap[this.heap[t + 1] + 1];
                        this.heap[temp + 1] = -2;
                    }
                } else
                    this.heap[t] = this.heap[t] + length;
            }
        }
        displayheap();
    }

    void displayheap() {
        System.out.println("\nCurrent Heap");
        for (int i = this.heap.length - 1; i >= 0; i--) {
            System.out.print(i + ": ");
            if (this.heap[i] != -2 && this.heap[i] != -5)
                System.out.print(this.heap[i]);
            System.out.print("\n");
        }
        System.out.print("\n");
    }
}