
public class hup {
	public static void setXY(Node node,int[]arr) {
		double n = 100.0;
		double m = 0.0;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]==1 || arr[i] == 3) {
				n-=(n-m)/2;
			}
			if(arr[i]==2 || arr[i] == 4) {
				m+=(n-m)/2;
			}
		}
		node.x = (n+m)/2;
		n = 100.0;
		m = 0.0;
		for(int i=0;i<arr.length;i++) {
			if(arr[i]==3 || arr[i] == 4) {
				n-=(n-m)/2;
			}
			if(arr[i]==1 || arr[i] == 2) {
				m+=(n-m)/2;
			}
		}
		node.y = (n+m)/2;
	}
	public static double getx(Node node) {
		double x=0;
		int one = 0,two = 0, three = 0,four=0;
		if(node.one!=null) {x+= (node.one.data*node.one.x); one = node.one.data;}
		if(node.two!=null) {x+= (node.two.data*node.two.x); two = node.two.data;}
		if(node.three!=null) {x+= (node.three.data*node.three.x); three = node.three.data;}
		if(node.four!=null) {x+= (node.four.data*node.four.x); four = node.four.data;}
				
		x /= (one+two+three+four);
		node.x = x;
		node.data = (one+two+three+four);
		return x;
	}
	public static double gety(Node node) {
		double y=0;
		int one = 0,two = 0, three = 0,four=0;
		if(node.one!=null) {y+= (node.one.data*node.one.y); one = node.one.data;}
		if(node.two!=null) {y+= (node.two.data*node.two.y); two = node.two.data;}
		if(node.three!=null) {y+= (node.three.data*node.three.y); three = node.three.data;}
		if(node.four!=null) {y+= (node.four.data*node.four.y); four = node.four.data;}
				
		y /= (one+two+three+four);
		node.y=y;
		node.data = (one+two+three+four);
		return y;
	}
	public static void addChild(int data,Node temp,int[]arr) {
		
		for(int i =0;i < arr.length - 1;i++) {
			if(arr[i] == 1) {
				if(temp.one == null)
					temp.one = new Node(-1);
				temp = temp.one;
			}
			else if(arr[i] == 2) {
				if(temp.two == null)
					temp.two = new Node(-1);
				temp = temp.two;
			}
			else if(arr[i] == 3) {
				if(temp.three == null)
					temp.three = new Node(-1);
				temp = temp.three;
			}
			else if(arr[i] == 4) {
				if(temp.four == null)
					temp.four = new Node(-1);
				temp = temp.four;
			}
		}
		if(arr[arr.length-1] == 1) {
			temp.one = new Node(data);
			setXY(temp.one,arr);
		}
		else if(arr[arr.length-1] == 2) {
			temp.two = new Node(data);
			setXY(temp.two,arr);
		}
		else if(arr[arr.length-1] == 3) {
			temp.three = new Node(data);
			setXY(temp.three,arr);
		}
		else if(arr[arr.length-1] == 4) {
			temp.four = new Node(data);
			setXY(temp.four,arr);
		}
	}
	public static void traverse(Node node) {
		if(node.data != -1) {System.out.println(node.data + " " + node.x + " " + node.y); return;}		
		if(node.one != null) traverse(node.one);
		if(node.two != null) traverse(node.two);
		if(node.three != null) traverse(node.three);
		if(node.four != null) traverse(node.four);
		double x = getx(node);
		double y = gety(node);
		System.out.println(node.data + " " + x + " " + y);
	}
	public static void main(String[]args) {
		
		Node root = new Node(-1);
		Node temp = root;
		int arr[] = {2,4,2,1};
		int arr1[] = {1,2,4};
		int arr2[] = {1,2};
		int arr3[] = {3};
		addChild(10,temp,arr);
		addChild(20,temp,arr1);
		addChild(30,temp,arr2);
		addChild(40,temp,arr3);
		traverse(root);
		
	}
	
	/*
	 * 
	 * 4^12 lik max UNIQUE input
	 * 
	 * */
	
	
}

class Node{
	int data;
	Node one;
	Node two;
    Node three;
	Node four;
	Node temp;
	double x;
	double y;
	
	public Node(int data) {
		this.data = data;
	}
	
	
	
}