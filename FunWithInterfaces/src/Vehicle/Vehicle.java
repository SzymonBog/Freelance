package Vehicle;

public class Vehicle implements VehicleInterface{
    private boolean state;
    private int velocity;
    private int gear;

    public Vehicle(){
        this.state = false;
        this.velocity = 0;
        this.gear = 1;
    }
    public boolean getState() {
        return state;
    }
    public int getVelocity() {
        return velocity;
    }
    public int getGear() {
        return gear;
    }

    public void setState(boolean state) {
        this.state = state;
    }

    public void setVelocity(int velocity) {
        this.velocity = velocity;
    }

    public void setGear(int gear) {
        this.gear = gear;
    }

    @Override
    public void showStats() {
        System.out.println("Vehicle is turned on: " + getState());
        System.out.println("Current velocity: " + getVelocity());
        System.out.println("current gear: " + getGear());
    }
}
