// https://exercism.io/tracks/typescript/exercises/grade-school/solutions/cbb9165daa8d47c59f8d7f167de6aa1d

export default class GradeSchool {
    
    private roster = new Map<string, string[]>();
  
    public studentRoster(): Map<string, string[]> {
        // the reason why we don't just return this.roster is because, 
        // 1) we have to sort by key as below
        // 2) prevent modification outside the module by returning new Map, rather than existing map
        // that is, we have to return copy of map, not a reference to original map
        // returning a reference to original is what allow that entry in the roaster to be modified
        // 3) then why is e[1].slice() needed in the end ??
        // because, e[1] is the array, which is reference type, which means ,
        // even if we copy existing Map, it is shallow copy, ef we just return e[1], it means ,
        // copied Map > e[1] ( which is value array ) can still access the original Map > e[1] ( value array ) because
        // shallow copy just copies pointer of 'reference type variable( value ) in the reference type( Map ) '
        // in order to copy the data of array and allocate in into new Map , we need to use " .slice() "
      return new Map([...this.roster.entries()].map(e => [e[0], e[1].slice()]));
    }
  
    public studentsInGrade(grade: number): string[] {
        // the reason why we conver 'grade' in to 'string' type is because, there is certain case in test case in which they are trying to reach throught string key
        // ex. const result = this.roster.get('2')
        const students = this.roster.get(''+grade)
        // students within a grade should be sorted alphabetically by name
      return this.getStudents(grade);
    }
  
    public addStudent(name: string, grade: number): void {
      // to prevent same student exiting in different grades, remove student in existing grades
      this.removeStudent(name);
      // you have to still add 'sort()' !
      this.roster.set(''+grade, [...this.getStudents(grade), name].sort());
    }
  
    private getStudents(grade: number): string[] {
      return this.roster.get(''+grade)?.slice() || [];
    }
  
    private removeStudent(name: string): void {
      /*
      ex. const map = new Map<string, string>();
      map.set('name' ,'Mommoo')
      map.forEach((value,key,mapObject) => console.log(key + ',', + value))
      결과 : name, Mommoo
      */
      this.roster.forEach((value) =>
        value.includes(name) && value.splice(value.indexOf(name))
      );
  
      /* < 혹은 >
          this.roster.forEach((value, key, mapObject) =>
          mapObject.get(key)?.includes(name) && value.splice(value.indexOf(name))
          );
  
          -- the reason why '?' needed is because, mapObject.get(key) might not exist ( undefined )
      */
    }
    
  }