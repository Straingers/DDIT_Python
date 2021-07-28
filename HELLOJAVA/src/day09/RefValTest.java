package day09;

public class RefValTest {
	
	public static void changeArr(int[] arr) {
		arr[0] = 3;
	}
	
	public static void changeA(int a) {
		a = 4;
	}
	
	public static void main(String[] args) {
		int[] arr = {1};
		int a = 2;
		
		System.out.println(arr[0]);
		System.out.println(a);
		
		changeArr(arr);
		changeA(a);
		
		System.out.println(arr[0]);
		System.out.println(a);
	}
}
