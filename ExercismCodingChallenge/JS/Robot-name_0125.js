// # https://exercism.io/my/solutions/404b6c31407448abb8a32bfb7879f71b

// This is only a SKELETON file for the 'Robot Name' exercise. It's been
// provided as a convenience to get your started writing code faster.
export class Robot {
    
    /*
    >> Static Varaible ----------------------------------------------
    정적 변수는, 함수를 벗어나더라도 사라지지 않고
    계속 유지된다. 
    정적 변수는, 프로그램이 시작될 때, 생성되고 초기화된다. 
    즉, static으로 선언된 변수는, 해당 클래스 로 생긴 instance 사이에서 공유된다
    
    ex void increaseNum(){
        int num = 0;
        num += 1
        print(num)
    }

    increaseNum() // 1
    increaseNum() // 1
    increaseNum() // 1

    모두 1로 출력된다.
    왜냐하면 int num은 increaseNum이 종료되는 순간, 사라지고
    increaseNum()이 호출되면 다시 생성되어 작동하기 때문이다. 


    이번에는 static 변수로 선언해보자
    ex void increaseNum(){
        static int num = 0;
        num += 1
        print(num)
    }

    increaseNum() // 1
    increaseNum() // 2
    increaseNum() // 3

    왜 ???

    void increaseNum(){
        static int num = 0;
        num += 1
        print(num)
    }

    void increaseNum(){
        static int num = 0; /// 여기서 0이라는 초기화 무시하고, 위에서 저장된 num이 사용되는 것이다. 
        num += 1
        print(num)
    }

    그렇다면 정적변수와 전역변수 간의 차이가 무엇이냐 !
    전역변수는 다른 파일에서도 사용할 수 있지만
    정적변수는 다른 파일에서 사용할 수 없다. 


    >> Static Method -------------------------------------------------
    
    What is Static Method in JS Classes ?
    
    - it's a method we define on a class
    but it's not part of the instantiated object
    
    it does not require an instance of Clas
    to be created,
    in order to be used.

    usually, static methods are used as
    helper function
    
    ex. 
    class Square(
        constructor(...width){
            this.width = _width;
            this.height= _width
        }

        static equals( a, b ){
            // a, b : two different two square instances
            return a.width == b.width
        }
    )

    let square1 = new Square(8)
    let square2 = new Square(5)

    // we approach to Class itself, not the class instance    ex. Square.equal
    console.log(Square.equals(square1, square2))

    */
    static usedNames = new Set()

    constructor(){
        this._name = this.generateName()
        Robot.usedNames.add(this._name)
    }

    generateName(){
        let name = "";
        // by below expression, we can divide each alphabet elements
        const LETTERS = [..."ABCDEFGHIJKLMNOPQRSTUVWXYZ"];
    
        const randomLetter = () => LETTERS[Math.floor(Math.random() * 25)]
        const randomDigits = () => Math.floor(Math.random() * 10)
        
        // make random alpha
        for( let i = 0 ; i < 5; i++ ){
            if( i < 2 ){
                name += randomLetter()
            }else{
                name += randomDigits()
            }
        }

        return name
    }

    /*
    Getter and Setter -------------------------------------------------------------------------
    
    we need to use get name(){ }

    to statisfy test case " internal name cannot be modified"
    

    this means that, we don't want the name property in the Class to be modified 
    directly,

    in other words, we only want 'read-only' property

    here is where getter, setter comes in

    so, what is getter and setter  ?? ---------

    when you are working with a object, there are 2 kinds of property
    1) data property
    2) accessor property 
    
    for data property , 
    key ~ value pair , in which case we mostly see

    for accessor propery ,
    it' is a function written as get, set function
    where we retrieve some type of info 
    or we set some type of info .

    ex.
    class Square(){
        constructor(_width){
            this.width  = _width;
            this.height = _height; 
        }

        get area(){
            return this.width + this.height
        }

        set area(area){
            this.width  = Math.sqrt(area)
            this.height = this.width 
        }
    }

    let square1 = new Square(9);
    square1.area = 25 // set method
    console.log(square1.width) // 9
    

    we use 'get' method to get the data in the form we want
    and
    we use 'set' method to set, modify the data in the form we want
    
    ------------------------------------------------------------------------
    To prevent, modifiying the specific 'data-proerty' directly,
    we can make usage of 'get' method , using 'get' method only
    and not using 'set' method .

    That is, we can use _ coding convention
    and simply avoid setters
    
    ex.
    Class Person{
        constructor(firstname, lastname){
            this._firstname = firstname;
            this._lastname  = lastname;
        }

        get firstname(){
            return this._firstname
        }

        get lastname(){
            return this._lastname
        }
    }

    let person = new Person('John', 'Doe')

    // this is ignored
    person.firstname = 'Foo'
    person.lastname  = 'Bar'

    console.log(person.firstname, person.lastname) // still 'John', 'Doe'
    

    so this is why we use
    this._name 
    and 
    get name()
    */

    get name(){
        return this._name 
    }

    reset(){
        let name ;
        do name = this.generateName();
        while(Robot.usedNames.has(name))

        Robot.usedNames.add(name);

        return ( this._name = name)
    }
}

// ' Every once in a while we need to reset a robot to its factory settings, which means that its name gets wiped '
Robot.releaseNames = () => Robot.usedNames.clear()

