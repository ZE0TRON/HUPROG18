package huprog;

public class hup {
	public static void addChild(int data,Node temp,int[]arr,Double x,Double y) {
		
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
		}
		else if(arr[arr.length-1] == 2) {
			temp.two = new Node(data);
		}
		else if(arr[arr.length-1] == 3) {
			temp.three = new Node(data);
		}
		else if(arr[arr.length-1] == 4) {
			temp.four = new Node(data);
		}
	}
	public static void main(String[]args) {
		
		Node root = new Node(-1);
		Node temp = root;
		int arr[] = {1,1,2};
		int arr1[] = {1,3,1,1};
		int arr2[] = {1,3,4};
		int arr3[] = {3};
		int arr4[] = {2,2,4};
		int arr5[] = {4,4,2};
		addChild(10,temp,arr,1.0,1.0);
		addChild(10,temp,arr1,1.0,1.0);
		addChild(10,temp,arr2,1.0,1.0);
		addChild(10,temp,arr3,1.0,1.0);
		addChild(10,temp,arr4,1.0,1.0);
		addChild(10,temp,arr5,1.0,1.0);
		
		
		System.out.println(root.one.one.two.data);
		
		
	}
	
	/*
	 * xyleri iþleyen func?
	 * inputu al?
	 * tree build?
	 * bottom-top dyn [10][2^20] arr?
	 * print arr?
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