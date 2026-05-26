import re


class ContextLeakGuard:

    def __init__(self):

        self.blocked_patterns = [

            r'aws_secret_access_key',

            r'api[_\-]?key',

            r'password',

            r'secret',

            r'token',

            r'private[_\-]?key',

            r'BEGIN RSA PRIVATE KEY',

            r'confidential',

            r'internal[_\-]?only',

            r'admin[_\-]?endpoint'
        ]

        print(
            "✅ Context leak guard initialized"
        )

    # =====================================
    # Scan Retrieved Context
    # =====================================

    def validate_context(

        self,

        context
    ):

        lowered_context = (

            context.lower()
        )

        for pattern in self.blocked_patterns:

            if re.search(

                pattern,

                lowered_context
            ):

                return {

                    "allowed": False,

                    "reason":

                    f"Sensitive context detected: {pattern}"
                }

        return {

            "allowed": True,

            "reason":

            "Context approved"
        }