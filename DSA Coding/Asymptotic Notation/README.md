# Asymptotic notations

## ASYMPTOTIC NOTATION :
- Efficiency of algorithm depends on amount of time ,storage and other resources required to execute an algorithm.
- Efficiency is measured with help of asymptotic notations.
- Asymptotic notations are mathematical notations used to decribe execution time of an algorithm when input tends towards a particular value or limiting value.

## **THREE ASYMPTOTIC NOTATIONS :**
1. Big-O notation : used to measure the worst case scenerio of an algorithm .
   - It generally gives an upper bound. in simple words we can say that (O) notation is used to measure the maximum time that an algorithm can take to execute.
2. Omega notations : used to measure the best case scenerio of an algorithm .It generally gives lower bound.
   - In simple words we can say that theta notation is used to measure the minimum time that an alogrithm can take to execute.
3. Theta notations : used to measure the average case scenerio of an alogrithm .It generally gives the average bound. 
   - In simple words we can say that omega notation is used to measure the average time that an algorithm can take to execute.

How to find the time complexity of an algorithm with aymptotic notation?
`let 'n' -> size of input`
then , f(n) will represent the number of instruction executed for input value 'n'.
## Lets try to find the time complexities with asymptotic notation with help of example:

<br>

Ex 1. :
we have a main function which will execute a for loop to print hello world 'n' times.

```python
  main(){
    int n = 10;
    for(int i = 0 ;i < n ;i++){ |
    printf("hello-world"); |
    }
    return 0;
  }
```
lets break the code
```python
  int n = 10; -> This instruction with execute 1-time : 1
  for(int i = 0 ;i < n ;i++){
  printf("hello-world"); -> This instruction will execute n-times : n
  }
  return 0; -> This instruct will also execute 1-time : 1
  f(n) = 1 + n + 1;
  f(n) = n + 2;
```

> the complexity of an algorithm is generally not dependent on the constants so we can ignore the '2' and therefore
> the worst case complexity will be f(n) = n ***i.e O(n)***,for the above code.

<br>

Ex 2. :
Lets check another example ,this time with multiple for-loop
```python
  void search(int arr[] ,int size){
    for(int i = 0 ;i <= size ;i++){
      for(int j = i+1 ;j <= size - i - 1 ;j++){
        if(arr[j] > arr[j + 1]){
          swap(arr[j] ,arr[j+1]);
        }
      }
    }
  }
```

lets break the code
```python
for(int i = 0 ;i <= size ;i++){ -> This instruction will execute for n times
for(int j = i+1 ;j <= size - i - 1 ;j++){ ->This loop will execute for n times
if(arr[j] > arr[j + 1]){ ->This instruction will execute for 1 time
swap(arr[j] ,arr[j+1]); -> This instruction will execute for 1 time
f(n) = n * n + 1 + 1;
f(n) = n^2 + 2;
```
> we can ignore the constant value '2' ,therefore
> the worst case complexity will be** *O(n^2)***

<br>

Ex 3. :
Note : in case of worst if-else statements as well ,we will compute the complexity from if-else ,which ever block has larger complexity
```python
  if(val == 1){ 
    printf("hello world"); 
  } 
  else{ 
    for(int i = 0 ;i < n ;i++){ 
      printf("hello world");
    }
  }
```

> in this we can see that else part has worst case complexity O(n) whereas if block will have O(1) worst case complexity
> therefore we will consider the worst case complexity as O(n) for the above example
