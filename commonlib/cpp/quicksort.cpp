/*******QUICKSORT********/
template<typename K>
void quickSort(K* myArray, int startIdx, int endIdx){
  if(endIdx-startIdx<=1)
    return;
  int flip = endIdx-1;
  int wall = startIdx;
  for(int i = startIdx; i<endIdx; i++){
    if(myArray[i]<myArray[flip]){
      K temp = myArray[i];
      myArray[i] = myArray[wall];
      myArray[wall] = temp;
      wall++;
    }
  }
  K temp = myArray[flip];
  myArray[flip] = myArray[wall];
  myArray[wall] = temp;

  printf("\n");
  mySort(myArray, wall+1, endIdx);
  mySort(myArray, startIdx, wall); //Negative gets tested in base case
}
