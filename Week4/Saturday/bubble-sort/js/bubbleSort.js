var sequence = [4, 3, 5, 0, 1]


function bubbleSort(arr) {
    let index = 1;
    let swaps = 0;
    while (index < arr.length) {
        let previous = arr[index-1]   
        let current = arr[index]
        if (previous > current) {
            let hold = previous
            arr[index-1] = current 
            arr[index] = hold
            index = 1
            swaps++ 
        } else {
            index++
        }
    }
    console.log("Final result: " + arr)
    console.log("Swaps: " + swaps)
    return arr
}


console.log(bubbleSort(sequence))