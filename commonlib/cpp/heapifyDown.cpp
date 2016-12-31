/******Heapify Down******/
template <typename K>
void heapifyDown(int pos, K* arr, int length){
  if(!hasChild(pos,length))
    return;
  int left = leftChild(pos);
  int right = rightChild(pos, length);

  if(arr[left]>=arr[right] || right < 0){
    if(arr[left]>arr[pos]){
      K temp = arr[left];
      arr[left]=arr[pos];
      arr[pos]=temp;
      heapifyDown(left, arr, length);
    }
  }
  else{
    if(arr[right]>arr[pos]){
      K temp = arr[right];
      arr[right]=arr[pos];
      arr[pos]=temp;
      heapifyDown(right, arr, length);
    }
  }
}
