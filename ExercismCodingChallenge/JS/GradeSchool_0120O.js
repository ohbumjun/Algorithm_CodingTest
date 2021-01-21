// https://exercism.io/my/solutions/c26349a5f80946b0af63aee14071fad1

export class GradeSchool {
  constructor(){
    this.school = {}
  }
  roster() {
    // one of way of deep copy of reference type
    return JSON.parse(JSON.stringify(this.school))
  }

  add(name , grade ) {
    // 이미 기존에 존재했다면
    if(this.school[grade]){
      this.school[grade].push(name)
      this.school[grade].sort()
    }else{
      this.school[grade] = []
      this.school[grade].push(name)
    }

  }

  grade(grade) {
    return this.school[grade] != null ? this.school[grade] : {}
  }
}
