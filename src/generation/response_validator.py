import re


class ResponseValidator:

    def __init__(self):

        # =====================================
        # Suspicious Hallucination Phrases
        # =====================================

        self.suspicious_phrases = [

            "i believe",

            "probably",

            "possibly",

            "might be",

            "may indicate",

            "it seems",

            "likely",

            "could suggest"
        ]

        # =====================================
        # Approved Refusal Responses
        # =====================================

        self.refusal_phrases = [

            "the retrieved documents do not contain sufficient information",

            "insufficient information",

            "the provided context does not contain"
        ]

        print(
            "✅ Response validator initialized"
        )

    # =====================================
    # Validate Response
    # =====================================

    def validate(

        self,

        response
    ):

        # =====================================
        # Empty Response Check
        # =====================================

        if (

            response is None

            or

            len(response.strip()) == 0
        ):

            return {

                "valid": False,

                "reason":
                "Empty response"
            }

        # =====================================
        # API Failure Detection
        # =====================================

        lowercase_response = (
            response.lower()
        )

        if (

            "generation error" in lowercase_response

            or

            "429" in lowercase_response

            or

            "too many requests" in lowercase_response
        ):

            return {

                "valid": False,

                "reason":
                "Generation API failure"
            }

        # =====================================
        # Approved Refusal Detection
        # =====================================

        for refusal_phrase in (

            self.refusal_phrases
        ):

            if refusal_phrase in lowercase_response:

                return {

                    "valid": True,

                    "reason":
                    "Approved grounded refusal"
                }

        # =====================================
        # Citation Validation
        # =====================================

        citation_pattern = r"\[.*?\.md\]|\[.*?\.csv\]"

        citations = re.findall(

            citation_pattern,

            response
        )

        if len(citations) == 0:

            return {

                "valid": False,

                "reason":
                "Missing citations"
            }

        # =====================================
        # Hallucination Phrase Detection
        # =====================================

        for phrase in (

            self.suspicious_phrases
        ):

            if phrase in lowercase_response:

                return {

                    "valid": False,

                    "reason":
                    f"Suspicious phrase detected: {phrase}"
                }

        # =====================================
        # Validation Success
        # =====================================

        return {

            "valid": True,

            "reason":
            "Response validated successfully"
        }