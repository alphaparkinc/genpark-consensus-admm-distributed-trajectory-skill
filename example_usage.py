from client import ConsensusADMMCoordinator

def main():
    print("=== Testing Consensus ADMM Coordinator ===")
    coordinator = ConsensusADMMCoordinator(agents=["ugv_1", "ugv_2", "ugv_3"], rho=1.0)
    desired_speeds = {"ugv_1": 15.0, "ugv_2": 18.0, "ugv_3": 12.0}

    last_res = None
    for _ in range(20):
        last_res = coordinator.step(desired_speeds)

    print("Final Consensus Output after 20 iterations:", last_res)
    assert 14.5 <= last_res['consensus_val'] <= 15.5

    print("Consensus ADMM Coordinator verified successfully!")

if __name__ == '__main__':
    main()
