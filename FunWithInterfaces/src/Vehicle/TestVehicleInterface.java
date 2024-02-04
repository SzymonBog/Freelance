package Vehicle;

public class TestVehicleInterface {
    public static void main(String[] args) {
        Vehicle v = new Vehicle();
        v.showStats();

        v.setState(v.turnOnOff(v.getState()));
        v.showStats();

        v.setVelocity(v.changeVelocity(v.getVelocity(), 40, v.getState()));
        v.setGear(v.changeGear(v.getGear(), v.getVelocity()));
        v.showStats();

        v.setVelocity(v.changeVelocity(v.getVelocity(), 70, v.getState()));
        v.setGear(v.changeGear(v.getGear(), v.getVelocity()));
        v.showStats();

        v.setVelocity(v.changeVelocity(v.getVelocity(), -50, v.getState()));
        v.setGear(v.changeGear(v.getGear(), v.getVelocity()));
        v.showStats();

        v.setState(v.turnOnOff(v.getState()));
        v.setVelocity(v.changeVelocity(v.getVelocity(), 0, v.getState()));
        v.setGear(v.changeGear(v.getGear(), v.getVelocity()));
        v.showStats();
    }
}
