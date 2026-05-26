import re


class PIIGuard:

    def __init__(self):

        print(
            "✅ PII guard initialized"
        )

    # =====================================
    # Mask Sensitive Data
    # =====================================

    def mask_pii(

        self,

        text
    ):

        # =====================================
        # Email Masking
        # =====================================

        email_pattern = (

            r'([a-zA-Z0-9._%+-]{2})'
            r'[a-zA-Z0-9._%+-]*'
            r'(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
        )

        text = re.sub(

            email_pattern,

            r'\1***\2',

            text
        )

        # =====================================
        # Salary Masking
        # =====================================

        salary_pattern = (

            r'(?i)(salary\s*[:\-]?\s*)'
            r'([0-9,.]+)'
        )

        text = re.sub(

            salary_pattern,

            r'\1[REDACTED SALARY]',

            text
        )

        # =====================================
        # DOB Masking
        # =====================================

        dob_pattern = (

            r'(?i)(date_of_birth\s*[:\-]?\s*)'
            r'([0-9]{4}-[0-9]{2}-[0-9]{2})'
        )

        text = re.sub(

            dob_pattern,

            r'\1[REDACTED DOB]',

            text
        )

        # =====================================
        # Employee ID Masking
        # =====================================

        employee_pattern = (

            r'FINEMP[0-9]{4}'
        )

        text = re.sub(

            employee_pattern,

            'FIN****',

            text
        )

        return text