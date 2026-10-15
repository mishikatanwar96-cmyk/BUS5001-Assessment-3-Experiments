"""Simple deterministic baseline for BUS5001 Assessment 3 Q3.
It is intentionally transparent and less context-sensitive than the LLM.
"""

def classify(message: str):
    text = message.lower()
    out = {
        "issue_category": "OTHER",
        "urgency": "LOW",
        "sentiment": "NEUTRAL",
        "followup_required": "N",
        "recommended_team": "ESG Operations"
    }

    if any(k in text for k in ["water", "leak", "flood"]):
        out.update(issue_category="WATER_FACILITIES", urgency="HIGH", followup_required="Y", recommended_team="Facilities")
    if any(k in text for k in ["electrical", "fire", "chemical"]):
        out["urgency"] = "CRITICAL"
    if any(k in text for k in ["supplier", "procurement"]):
        out.update(issue_category="PROCUREMENT_GOVERNANCE", urgency="MEDIUM", followup_required="Y", recommended_team="Procurement")
    if any(k in text for k in ["accessible", "accessibility", "wheelchair"]):
        out.update(issue_category="ACCESSIBILITY_INCLUSION", urgency="MEDIUM", followup_required="Y", recommended_team="Accessibility/Facilities")
    if any(k in text for k in ["blocked", "leak", "spreading", "contaminated"]):
        out["sentiment"] = "NEGATIVE"

    return out

if __name__ == "__main__":
    tests = [
        "Water is spreading across the floor near electrical equipment in Building C, Level 2.",
        "I want to report that one of our suppliers may not meet our sustainability policy.",
        "The accessible entrance near the main building has been blocked for two days."
    ]
    for t in tests:
        print(t)
        print(classify(t))
        print()
