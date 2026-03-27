def compliance_agent(text):
    if "guaranteed" in text.lower():
        return "FAIL: Risky claim detected"
    return "PASS"
