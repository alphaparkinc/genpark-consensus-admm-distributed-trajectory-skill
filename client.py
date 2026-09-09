class ConsensusADMMCoordinator:
    """Consensus ADMM for Multi-Agent Rendezvous and Coordination."""
    def __init__(self, agents, rho=1.0):
        self.agents = agents
        self.rho = rho
        self.local_trajs = {a: 0.0 for a in agents}
        self.dual_vars = {a: 0.0 for a in agents}
        self.global_consensus = 0.0

    def step(self, targets):
        for a in self.agents:
            t = targets.get(a, 0.0)
            u = self.dual_vars[a]
            z = self.global_consensus
            self.local_trajs[a] = (t + self.rho * z - u) / (1.0 + self.rho)

        self.global_consensus = sum(self.local_trajs[a] + self.dual_vars[a] / self.rho for a in self.agents) / len(self.agents)

        for a in self.agents:
            self.dual_vars[a] += self.rho * (self.local_trajs[a] - self.global_consensus)

        return {
            'consensus_val': round(self.global_consensus, 3),
            'local_trajs': {a: round(self.local_trajs[a], 3) for a in self.agents}
        }
