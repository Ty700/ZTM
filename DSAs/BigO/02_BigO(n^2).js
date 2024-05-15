// Log all pairs of arrays

const boxes = [1,2,3,4,5];

/*
Logging all pairs of an array means:
    (1,2), (1,3), (1,4), (1,5), (2,1), (2,3), (2,4) ...
*/

// We'd have to do a nested loop

const pairs = [];

for(let i = 0; i < boxes.length; i++){
    for(let j = 0; j < boxes.length; j++){
        if(i == j){
            continue;
        }

        pairs.push([boxes[i],boxes[j]]);
    }
}

/* 
    Nested for loops = * of n

    Thus:
        O(n * n) = O(n^2)
*/

/* Not counting printing in the Big O cal */
for(let i = 0; i < pairs.length; i++){
    console.log(pairs[i]);
}

