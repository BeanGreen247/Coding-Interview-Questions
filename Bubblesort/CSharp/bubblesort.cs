using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace bubblesort
{
class Program
    {
        static void Main(string[] args)
        {
		int[] arr =new int[] {28, 86, 33, 7, 17, 21, 145, 221, 60};

		int temp = 0;

		Console.WriteLine("unsorted");
		for (int i = 0; i < arr.Length; i++)
    		Console.Write(arr[i] + " ");

		for (int write = 0; write < arr.Length; write++) {
    			for (int sort = 0; sort < arr.Length - 1; sort++) {
        			if (arr[sort] > arr[sort + 1]) {
            			temp = arr[sort + 1];
            			arr[sort + 1] = arr[sort];
            			arr[sort] = temp;
        			}
    			}
		}

		Console.WriteLine("\n"+"sorted");
		for (int i = 0; i < arr.Length; i++)
    		Console.Write(arr[i] + " ");

		Console.ReadKey();
        }
    }
}
