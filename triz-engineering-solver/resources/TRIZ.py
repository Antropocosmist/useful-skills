import json

class TRIZSkillEngine:
    def __init__(self):
        # Sparse mapping dictionary: (improving_id, worsening_id) -> list of principles
        self.matrix_edges = {
            (1, 2): [15, 8, 29, 34], (1, 3): [29, 17, 38, 34], (2, 1): [35, 10, 4, 26],
            (9, 10): [13, 15, 19, 35], (9, 22): [13, 28, 15, 19], (14, 1): [8, 40, 15, 35],
            (31, 36): [2, 24, 35, 1], (35, 36): [1, 15, 16, 26]
        }
        self.principles = {
            1: "Segmentation", 2: "Taking out", 8: "Anti-weight", 10: "Preliminary action",
            13: "The other way round", 15: "Dynamization", 16: "Partial or excessive actions",
            17: "Another dimension", 19: "Periodic action", 22: "Blessing in disguise",
            24: "Intermediary", 26: "Copying", 28: "Mechanics substitution",
            29: "Pneumatics and hydraulics", 34: "Discarding and recovering", 
            35: "Parameter changes", 36: "Phase transitions", 38: "Strong oxidants", 
            40: "Composite materials"
        }

    def resolve_contradiction(self, improve_id: int, worsen_id: int) -> dict:
        key = (improve_id, worsen_id)
        if key not in self.matrix_edges:
            return {"status": "error", "message": "No direct map. Try broad-matching properties."}
        
        resolved_principles = [
            f"Principle {pid}: {self.principles.get(pid, 'Unknown')}" 
            for pid in self.matrix_edges[key]
        ]
        return {
            "status": "success",
            "improving_parameter": improve_id,
            "worsening_parameter": worsen_id,
            "recommended_strategies": resolved_principles
        }

# Agent Execution Example: 
# Target: Increase Speed (9) but it causes high Energy Loss (22)
engine = TRIZSkillEngine()
print(json.dumps(engine.resolve_contradiction(9, 22), indent=2))
