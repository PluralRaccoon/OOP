"""
Handling Unpredictable Scanners

Scenario:
You are expanding your VulnerabilityFinding model. Sometimes, the cybersecurity scanner detects a vulnerability but hasn't finished calculating the CVSS score yet, so it drops the field entirely. Furthermore, you want every finding to automatically be tagged with a status of "OPEN" unless the API explicitly says otherwise.

Your Task:
Rewrite the VulnerabilityFinding model with these two new constraints:

    Make cvss_score optional (it should accept a float, but default to None if the scanner omits it).

    Add a new field called status that must be a string, and defaults to "OPEN".

Test Data:
Python

api_response_incomplete = {
    "cve_id": "CVE-2026-0001",
    "patched": False
    # Notice cvss_score is completely missing!
    # Notice status is completely missing!
}

Task: Show me the updated model and how you would process this incomplete payload.
"""
from pydantic import BaseModel
from typing import Any

class VulnerabilityFinding(BaseModel):
    cve_id: str
    cvss_score: float | None = None
    patched: bool
    status: str = "OPEN"

api_response: dict[str, Any] = {
    "cve_id": "CVE-2026-9999",
    "cvss_score": "8.5",  
    "patched": "False"   
}

api_response_incomplete: dict[str, Any] = {
    "cve_id": "CVE-2026-0001",
    "patched": False
    # Notice cvss_score is completely missing!
    # Notice status is completely missing!
}

log = VulnerabilityFinding(**api_response) 
log2 = VulnerabilityFinding(**api_response_incomplete)

print(log)
print(log2)