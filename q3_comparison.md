# Q3 Comparison Notes

The rule baseline and LLM agree on the main issue category and follow-up requirement for all three test messages. They also both detect the electrical-water scenario as CRITICAL. The main discrepancy is the blocked accessible entrance: the deterministic baseline assigns MEDIUM because it only recognises the accessibility keyword, whereas the LLM assigns HIGH by combining the two-day duration with the operational impact on equitable access.

This illustrates both the benefit and risk of an LLM. It can interpret context and severity that a rigid keyword rule misses, but its reasoning is probabilistic and may over- or under-escalate. A production design should therefore retain deterministic safety rules for explicit critical hazards, validate the JSON schema, log model/rule disagreements, and require human review for HIGH/CRITICAL cases or ambiguous sensitive matters.
