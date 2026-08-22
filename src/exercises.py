"""
Exercise 1: Building your first Model

Scenario:
You are building an ingestion script for a vulnerability scanner. 
The scanner outputs a flat dictionary for each finding. You need to model this data.

Your Task:
Write a Pydantic BaseModel named VulnerabilityFinding that includes the following fields:

    cve_id: A string representing the vulnerability ID (e.g., "CVE-2026-1234").

    cvss_score: A float representing the severity score.

    patched: A boolean indicating if a patch has been applied.

Test Data:
Imagine your pipeline receives this messy dictionary from the scanner API:
Python

api_response = {
    "cve_id": "CVE-2026-9999",
    "cvss_score": "8.5",  # Note: It's a string!
    "patched": "False"    # Note: It's a string!
}

Task: Show me the class definition, and show me how you would instantiate it using the api_response dictionary.
"""
from pydantic import BaseModel

class VulnerabilityFinding(BaseModel):
    cve_id: str
    cvss_score: float
    patched: bool

api_response: dict[str, str | float | bool] = {
    "cve_id": "CVE-2026-9999",
    "cvss_score": "8.5",  
    "patched": "False"   
}

log = VulnerabilityFinding(**api_response) # type: ignore

print(log)