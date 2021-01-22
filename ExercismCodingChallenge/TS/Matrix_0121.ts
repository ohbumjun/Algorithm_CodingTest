class Matrix {

    public rows : Array<number>[] = []
    public columns : Array<number>[] = []
  
    constructor(InputString : string) {
  
      let stringSplit = InputString.split('\n')
  
      for(let row of stringSplit){
          let tmpRow : Array<number> = row.split(' ').map(e => Number(e))
          
          // check if it is an Array
          if(!Array.isArray(tmpRow)){
            throw new Error("InValid Input")
          }else{
              this.rows.push(tmpRow)
              tmpRow.forEach((number, idx) => {
                  if(this.columns[idx]){
                    this.columns[idx].push(number)
                  }else{
                    this.columns.push([number])
                  }
              })
          }
      }
    }
  }
  
  export default Matrix
  