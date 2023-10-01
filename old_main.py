if __name__ == "__main__":

    # feature map. Position of 2 point features in the world frame.
    M2D = [np.array([[-40, 5]]).T,
           np.array([[-5, 40]]).T,
           np.array([[-5, 25]]).T,
           np.array([[-3, 50]]).T,
           np.array([[-20, 3]]).T,
           np.array([[40,-40]]).T]
    xs0 = np.zeros((6,1))   # initial simulated robot pose

    robot = DifferentialDriveSimulatedRobot(xs0, M2D) # instantiate the simulated robot object

    kSteps = 5000 # number of simulation steps
    xsk_1 = xs0 = np.zeros((6, 1))  # initial simulated robot pose
    index = [IndexStruct("x", 0, None), IndexStruct("y", 1, None), IndexStruct("yaw", 2, 1)] # index of the state vector used for plotting
    usk = np.array([[0.5, 0.03]]).T  # initial input to the simulator

    for i in range(kSteps):
        xsk = robot.fs(xsk_1, usk)
        xsk_1 = xsk
        print("xsk=", xsk.T)

    exit(0)