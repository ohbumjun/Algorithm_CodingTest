// https://exercism.io/my/solutions/d86e5027f9524132a82920b7dc9eccb5

export default class Clock{
    public Hour : number ;
    public Minute : number ;
    constructor(Hour : number, Minute : number = 0 ){
        
        const MINUTES_IN_HOUR = 60;
        const HOURS_IN_DAY = 24

        /*
        Math.floor : 내림
        also applies to '-' 

        ex. Math.floor(-1.1) = -2 
        ex. Math.floor ( -160 // 60) 
        = Math.floor ( -2.666666) 
        = -3 ! ( it's not -2 )
        */
        let _hours   = ( Hour + Math.floor( Minute / 60 ) ) % 24 // 시간이 나온다. 
        let _minutes = Minute % 60

        this.Hour   = _hours < 0 ? _hours + 24 : _hours  ;
        this.Minute = _minutes < 0 ? _minutes + 60 : _minutes;

    }

    toString() : string {
        
        let strMin;
        let strHour;

        if( this.Hour < 10){
            strHour = `0${this.Hour}`
        }else{
            strHour = `${this.Hour}`
        }

        if( this.Minute < 10 ){
            strMin = `0${this.Minute}`
        }else{
            strMin = `${this.Minute}`
        }
        return strHour + ':' + strMin
    }

    plus(minuteToAdd : number) : Clock{
        return new Clock(this.Hour , this.Minute + minuteToAdd)
    }

    minus(minuteToSub : number): Clock{
        return new Clock(this.Hour , this.Minute - minuteToSub)
    }

    /*
    Don't forget return type 'boolean' !
    for 'toBeTruthy()' in test case to happen
    */
    equals(newClock : Clock) : boolean{
        return this.Hour == newClock.Hour && this.Minute == newClock.Minute;
    }

}