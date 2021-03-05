let array = [1,2,3,4]

array.forEach((element, index, origin) => {
    console.log("origin", [ ...origin.slice(0,index), ...origin.slice(index+1)])
})