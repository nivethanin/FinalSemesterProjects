class MyQueue {
    int arr[];
    int fir;
    int las;

    public MyQueue() {
        this.arr = new int[100];
        this.fir = 0;
        this.las = 0;
    }
    
    public void push(int x) {
        this.arr[this.fir] = x;
        this.fir++;
    }
    
    public int pop() {
        int temp = this.arr[this.fir];
        this.arr[this.fir] = 0;
        this.fir--;
        return this.temp;
    }
    
    public int peek() {
        return this.arr[this.fir];
    }
    
    public boolean empty() {
        if (this.fir==this.las) return true;
        else return false;
        
    }
    
    public static void main(String[] args) {
    Main myObj1 = new MyQueue();
    
    myObj1.push(3);

    System.out.println(myObj1.pop());

  }
}

