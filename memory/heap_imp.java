import java.util.*;
class heap
{
	public static void main(String[] args) 
	{
		Scanner in = new Scanner(System.in);
		System.out.print("please provide  the heap size :\t");
		int heap_size = in.nextInt();
		int[] array = create_heap(heap_size);
		display_heap(array);
		int freeStart = 0; int nextfree = 0 ;
		while(true)
		{
			System.out.println("choose among the following : ");
			System.out.println("1 : allocate some memory ");
			System.out.println("2 : de-allocate some memory");
			int choice = in.nextInt(); int allocate = 0 ; int deallocate = 0;
			int current_allocation_index = 0;
			switch(choice)
			{
				case 1 :
						System.out.print("please provide  the size to allocate :\t");
						allocate = in.nextInt();
						nextfree = current_allocation_index+allocate ;
				break;
				case 2 :
						System.out.print("provide the entry id to be deallocated :\t");
						deallocate = in.nextInt();
				break;
			}
		}
	}
	public static int[] create_heap(int heap_size)
	{
		int[] array = new int[heap_size];
		for(int i = 0 ; i < array.length ; i++)
		{
			array[i] = -1 ;
		}
		return array;
	}
	public static void display_heap(int[] array)
	{
		int i = 0 ;
		System.out.println();
		for(i = array.length -1 ; i > -1 ; i--)
		{
			System.out.println(i + "  "+ array[i]);
		}
		System.out.println();
	}
}