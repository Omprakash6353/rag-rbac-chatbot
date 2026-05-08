import re


class QueryProcessor:

    def __init__(self):

        # =====================================
        # Quarter Normalization
        # =====================================

        self.quarter_mapping = {

            "quarter one": "Q1",
            "first quarter": "Q1",

            "quarter two": "Q2",
            "second quarter": "Q2",

            "quarter three": "Q3",
            "third quarter": "Q3",

            "quarter four": "Q4",
            "fourth quarter": "Q4"
        }

    # =====================================
    # Normalize Query
    # =====================================

    def normalize_query(

        self,

        query
    ):

        normalized_query = (
            query.lower()
        )

        for phrase, quarter in (

            self.quarter_mapping.items()
        ):

            normalized_query = (

                normalized_query.replace(
                    phrase,
                    quarter
                )
            )

        return normalized_query

    # =====================================
    # Extract Filters
    # =====================================

    def extract_filters(

        self,

        query
    ):

        normalized_query = (
            self.normalize_query(query)
        )

        filters = []

        # =====================================
        # Department Detection
        # =====================================

        departments = [

            "marketing",
            "finance",
            "hr",
            "engineering",
            "general"
        ]

        for department in departments:

            if department in normalized_query:

                filters.append({

                    "department": department
                })

        # =====================================
        # Quarter Detection
        # =====================================

        quarter_match = re.search(

            r"\bQ[1-4]\b",

            normalized_query,

            re.IGNORECASE
        )

        if quarter_match:

            filters.append({

                "quarter": (
                    quarter_match.group()
                    .upper()
                )
            })

        # =====================================
        # Year Detection
        # =====================================

        year_match = re.search(

            r"\b(20\d{2})\b",

            normalized_query
        )

        if year_match:

            filters.append({

                "year": (
                    year_match.group()
                )
            })

        # =====================================
        # Final Filter Construction
        # =====================================

        if len(filters) == 0:

            return None

        if len(filters) == 1:

            return filters[0]

        return {

            "$and": filters
        }