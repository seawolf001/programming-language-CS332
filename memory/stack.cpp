#include <cmath>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <cstring>
using namespace std;

class stack{
    public:
    int top;
    int *a;
    int size;
    stack(int n){
        size=n;
        a=(int *)malloc (n*sizeof(int));
        memset(a,0,n);
        top=n;
    }
    void push(int n)
	{

        if(top<=n){
            cout << "Error there is no space .Cant add Activation record of this size "<<"try adding AR of size less than ot equal to " <<top-1<<"\n"; 
            return;
        }
        int tmp=top;
        for(int i=0;i<n;i++){
            a[--tmp]=-1;
        }
        a[--tmp]=top;
        top=tmp;
    }
    void pop(){
        if(top==size){
            cout << "No Activation Record to pop\n";
            return;
        }
        int ar=a[top]-top-1;
        top=a[top];
        cout << "Activation record of size "<<ar<< " popped\n";
    }
    void print(){
        cout << "The stack is\n";
        for(int i=size-1;i>=top;i--){
            cout << a[i] <<" ";
        }
        for(int i=top-1;i>=0;i--){
            a[i]=0;
            cout << "0 ";
        }
        cout << "\n";
    }
    
    
};

int main() {
  
    int size;
    cout << "Give the size of stack\n";
    cin >> size;
    stack s(size);
    int select;
    while(1){
        cout << "Choose:\n 1:Push activation record\n 2:Pop an Activation Record \n 3:Print the stack\n 4:Exit\n";
        cin >> select;
            switch(select){
                case 1:
                    cout << "Give Activation Record size\n";
                    cin >> select;
                    s.push(select);
                    break;
                case 2:
                    s.pop();
                    break;
                case 3:
                    s.print();
                    break;
                default:
                    return 0;
                    break;
            }
    }
    
    
  return 0;
}