#include <iostream> 
#include <string> 
using namespace std; 
#define SIZE 5
template <class MST> class Stack { 
    public: Stack();
    void push(MST k);
    MST pop();
    MST topElement();
    bool isFull();
    bool isEmpty();
    private:
    int top;
    MST st[SIZE];
    };
    template <class MST> Stack<MST>::Stack() {
        top = -1; 
        
    } 
    template <class MST> void Stack<MST>::push(MST k) {
        if (isFull()) {
        cout << "Stack is full\n";
        }
        cout << "Inserted element " << k << endl; top = top + 1;
        st[top] = k;
    }
    template <class MST> bool Stack<MST>::isEmpty(){
        if (top == -1)
        return 1;
        else return 0;
    }
    template <class MST> bool Stack<MST>::isFull(){
        if (top == (SIZE - 1))	
        return 1; 
        else return 0;
    }

    template <class MST> MST Stack<MST>::pop(){
        MST popped_element = st[top]; top--; 
        return popped_element;
        
    }
    template <class MST> MST Stack<MST>::topElement(){
        MST top_element = st[top]; 
        return top_element;
    } 
int main(){
    Stack<int> integer_stack;
    Stack<string> string_stack;
    int a,b,c;
    cout<<"Enter the 3 Values to Push"<<endl;
    cin>>a>>b>>c;
    char i,j;
    cin>>i>>j;
    integer_stack.push(a);
    integer_stack.push(b);
    integer_stack.push(c);
    string_stack.push("Sahil");
    string_stack.push("Kumar");
    cout << integer_stack.pop() << " REMOVED" << endl; 
    cout << string_stack.pop() << " REMOVED "	<< endl; 
    cout << "Top elemenT: " << integer_stack.topElement()<< endl;
    cout << "Top element: " << string_stack.topElement()<< endl; return 0;
}
