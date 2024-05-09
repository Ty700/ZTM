function boooo(n){
    for(let i = 0; i < n.length; i++){
        console.log('booooooooo')
    }
}


boooo('Hello');

/*
    What is the space complexity?
        - When counting this, we don't count the size of the function

        - We are not adding space in the function, just let i = 0, so O(n)
*/


// But what if we had


function arrayOfHiNTimes(n){
    let hiArray = [];

    for(let i = 0; i < n.length; i++){
        hiArray[i] = 'hi';
    }
    return hiArray;
}

/* What is the space completity? */

// My guess: O(n) since we would append 'hi' n amount of times and returning that array
// Really O(1 + 1 + n) the first 1 is the function call, and the other 1 is for the let i = 0

arrayOfHiNTimes(6);

