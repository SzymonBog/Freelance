package Vehicle;

public interface VehicleInterface {
    default boolean turnOnOff(boolean currentState){
        if(!currentState) {
            return true;
        } else {
            return false;
        }
    }
    default int changeGear(int curGear, int velocity){
        if(velocity>=0 && velocity<25){
            curGear = 1;
        } else if (velocity>=25 && velocity<40) {
            curGear = 2;
        } else if (velocity>=40 && velocity<60) {
            curGear = 3;
        } else if (velocity>=60 && velocity<80) {
            curGear = 4;
        } else if (velocity>=80 && velocity<100) {
            curGear = 5;
        } else {
            curGear = 6;
        }
        return curGear;
    }
    default int changeVelocity(int curVel, int velChange, boolean curState){
        if(!curState) {
            curVel = 0;
        } else {
            curVel = curVel + velChange;
        }
        return curVel;
    }
    public abstract void showStats();
}
