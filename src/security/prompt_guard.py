class PromptGuard:

    def __init__(self):

        # =====================================
        # Injection / Jailbreak Patterns
        # =====================================

        self.blocked_patterns = [

            "ignore previous instructions",

            "ignore all instructions",

            "forget previous instructions",

            "pretend you are admin",

            "act as admin",

            "bypass security",

            "disable guardrails",

            "reveal confidential",

            "show all salaries",

            "dump database",

            "system prompt",

            "developer instructions",

            "you are no longer restricted",

            "jailbreak",

            "override policy"
        ]

        print(
            "✅ Prompt guard initialized"
        )

    # =====================================
    # Validate Query
    # =====================================

    def validate_query(

        self,

        query
    ):

        lowercase_query = (

            query.lower()
        )

        # =====================================
        # Pattern Detection
        # =====================================

        for pattern in (

            self.blocked_patterns
        ):

            if pattern in lowercase_query:

                return {

                    "allowed": False,

                    "reason":
                    f"Blocked prompt pattern detected: {pattern}"
                }

        # =====================================
        # Query Approved
        # =====================================

        return {

            "allowed": True,

            "reason":
            "Query approved"
        }