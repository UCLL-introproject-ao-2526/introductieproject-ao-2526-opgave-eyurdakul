// Write your code here
function myFirstFunction(bike) {
    forward(bike);
}
function twiceForward(bike) {
    forward(bike);
    forward(bike);
}
function thriceForward(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
}
function forward4(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}
function forward5(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}
function forward10(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}
function right(bike) {
    turnRight(bike);
    forward(bike);
}
function ellShape(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    turnRight(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}
function uTurn(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    turnRight(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    turnRight(bike);
    forward(bike);
    forward(bike);
}
function crookedUTurn(bike) {
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    turnRight(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    forward(bike);
    turnRight(bike);
    forward(bike);
    forward(bike);
    forward(bike);
}
function forwardUntilWall(bike) {
    while (!sensor(bike)) {
        forward(bike);
    }
}
function smartEllShape(bike) {
    while (!sensor(bike)) {
        forward(bike);
    }
    turnRight(bike);
    while (!sensor(bike)) {
        forward(bike);
    }
}
function spiral(car) {
    const turnCount = 18;
    let start = 0;
    while(start < turnCount) {
        if(!sensor(car)) {
            forward(car);
        } else {
             turnRight(car);
             start++;
        }
    }
}
function turnLeft(car) {
    turnRight(car);
    turnRight(car);
    turnRight(car);
}
function left(car) {
    turnLeft(car);
    forward(car);
}
function slalom(car) {
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
}
function leftOrRight(car) {
    turnLeft(car);
    forwardUntilWall(car);
    turnRight(car);
    forwardUntilWall(car);
    turnRight(car);
    if(!sensor(car)) {
        forwardUntilWall(car);
        turnLeft(car);
        forward(car);
    }
}
function incompleteU(car) {
    if(!sensor(car)) {
        forwardUntilWall(car);
        turnRight(car);
        forwardUntilWall(car);
        turnRight(car);
        forwardUntilWall(car);
    } else {
        turnRight(car);
        forwardUntilWall(car);
        turnRight(car);
        forwardUntilWall(car);
    }
}
function whichDirection(car) {
    while(sensor(car)) {
        turnRight(car);
    }
    forwardUntilWall(car);
}
function firstRight(car) {
    turnRight(car);
    if(!sensor(car)) {
        while(!sensor(car)) {
            forward(car);
        }
    } else {
        turnLeft(car);
        forward(car);
        firstRight(car);
    }
}
function firstLeft(car) {
    turnLeft(car);
    if(!sensor(car)) {
        while(!sensor(car)) {
            forward(car);
        }
    } else {
        turnRight(car);
        forward(car);
        firstLeft(car);
    }
}
function zigZag(car) {
    firstRight(car);
    firstLeft(car);
    turnRight(car);
    turnRight(car);
    firstRight(car);
}
function forwardUntilNthLeft(car, nth) {
    var i = nth;
    while(i > 0) {
        forward(car);
        if(!sensorRight(car)) {
            i--;
        }
    }
}
function forwardUntilNthRight(car, nth) {
    var i = nth;
    while(i > 0) {
        forward(car);
        if(!sensorLeft(car)) {
            i--;
        }
    }
}
function findWayByNumber(car, times, directionCallBack, oppositeCallback) {
    passed = 0;
    while(passed <= times) {
        directionCallBack(car);
        if(!sensor(car)) {
            passed++;
        }
        if(passed < times) {
            oppositeCallback(car);
            forward(car);
        } else {
            break;
        }
    }
}
function secondRight(car) {
    findWayByNumber(car, 2, turnRight, turnLeft);
    forwardUntilWall(car);
}
function thirdRight(car) {
    findWayByNumber(car, 3, turnRight, turnLeft);
    forwardUntilWall(car);
}
function fourthRight(car) {
    findWayByNumber(car, 4, turnRight, turnLeft);
    forwardUntilWall(car);
}
function fifthLeft(car) {
    findWayByNumber(car, 5, turnLeft, turnRight);
    forwardUntilWall(car);
}
function maze(car) {
    right(2);
    left(1);
    left(2);
    left(2);
    right(4);
    right(1);
    left(3);
    forwardUntilWall(car);

    function left(n) {
        forwardUntilNthLeft(car, n);
        turnLeft(car);
    }

    function right(n) {
        forwardUntilNthRight(car, n);
        turnRight(car);
    }
}
function turnAround(car) {
    turnRight(car);
    turnRight(car);
}
function backward(car) {
    turnAround(car);
    forward(car);
    turnAround(car);
}
function isDeadEnd(car){
    if(!sensor(car)) {
        return false;
    }
    if(!sensorRight(car)) {
        return false;
    }
    if(!sensorLeft(car)) {
        return false;
    }
    return true;
}
function findDeadEnd(car) {
    while(true) {
        forward(car);
        if (sensor(car)) {
            return;
        }
        backward(car);
        turnRight(car);
    }
}
function sensorRight(car) {
    var isWall = false;
    turnRight(car);
    isWall = sensor(car);
    turnLeft(car);
    return isWall;
}
function sensorLeft(car) {
    var isWall = false;
    turnLeft(car);
    isWall = sensor(car);
    turnRight(car);
    return isWall;
}
function follow(car) {
    while(true) {
        forwardUntilWall(car);
        if(!sensorRight(car)) {
            turnRight(car);
        }else if (!sensorLeft(car)) {
            turnLeft(car);
        } else {
            return;
        }
    }
}
function rightHand(car) {
    while (!isDeadEnd(car)) {
        if (!sensorRight(car)) {
            turnRight(car);
            forward(car);
        } else if (!sensor(car)) {
            forward(car);
        } else if (!sensorLeft(car)) {
            turnLeft(car);
            forward(car);
        } else {
            turnAround(car);
        }
    }
}
function forwardUntilDestination(car) {
    while(!destinationReached(car)) {
        forward(car);
    }
}
function roomba(car) {
    var isRight = false;
    forward(car);
    turnRight(car);
    while(!destinationReached(car)) {
        forward(car);
        if(isRight) {
            turnRight(car);
            forward(car);
            turnRight(car);
        } else {
            turnLeft(car);
            forward(car);
            turnLeft(car);
        }
        isRight = !isRight;
    }
}
