import time


class RateLimiter:

    def __init__(self):

        self.request_logs = {}

        self.role_limits = {

            "employee": 5,

            "marketing": 10,

            "hr": 10,

            "finance": 10,

            "engineering": 10,

            "admin": 20
        }

        self.time_window = 60

        print(
            "✅ Rate limiter initialized"
        )

    # =====================================
    # Check Rate Limit
    # =====================================

    def is_allowed(

        self,

        role
    ):

        current_time = time.time()

        # =====================================
        # Initialize Role Logs
        # =====================================

        if role not in self.request_logs:

            self.request_logs[role] = []

        # =====================================
        # Remove Expired Requests
        # =====================================

        valid_requests = []

        for timestamp in self.request_logs[role]:

            if (

                current_time - timestamp

                < self.time_window
            ):

                valid_requests.append(
                    timestamp
                )

        self.request_logs[role] = (

            valid_requests
        )

        # =====================================
        # Get Role Limit
        # =====================================

        role_limit = (

            self.role_limits.get(

                role,

                5
            )
        )

        # =====================================
        # Limit Exceeded
        # =====================================

        if (

            len(
                self.request_logs[role]
            )

            >= role_limit
        ):

            return {

                "allowed": False,

                "reason":

                "Rate limit exceeded"
            }

        # =====================================
        # Record Request
        # =====================================

        self.request_logs[role].append(

            current_time
        )

        return {

            "allowed": True,

            "reason":

            "Request allowed"
        }