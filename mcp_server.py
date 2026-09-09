import sys
import json
from client import ConsensusADMMCoordinator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "consensus_step":
        coord = ConsensusADMMCoordinator(params.get("agents", []))
        return coord.step(params.get("targets", {}))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
