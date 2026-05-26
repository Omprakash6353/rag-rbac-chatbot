import json

from datetime import datetime


class AuditLogger:

    def __init__(self):

        self.log_file = (

            "audit_logs.jsonl"
        )

        print(
            "✅ Audit logger initialized"
        )

    # =====================================
    # Write Audit Event
    # =====================================

    def log_event(

        self,

        role,

        query,

        status,

        details=None
    ):

        log_entry = {

            "timestamp":

            datetime.utcnow().isoformat(),

            "role":
            role,

            "query":
            query,

            "status":
            status,

            "details":
            details
        }

        with open(

            self.log_file,

            "a"
        ) as file:

            file.write(

                json.dumps(log_entry)

                + "\n"
            )

        print(
            "✅ Audit event logged"
        )