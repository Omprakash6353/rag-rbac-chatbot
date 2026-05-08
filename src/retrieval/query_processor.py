import re


class QueryProcessor:

    def __init__(self):

        # =====================================
        # Quarter Normalization Mapping
        # =====================================

        self.quarter_mappings = {

            "quarter one": "Q1",
            "first quarter": "Q1",
            "quarter 1": "Q1",

            "quarter two": "Q2",
            "second quarter": "Q2",
            "quarter 2": "Q2",

            "quarter three": "Q3",
            "third quarter": "Q3",
            "quarter 3": "Q3",

            "quarter four": "Q4",
            "fourth quarter": "Q4",
            "quarter 4": "Q4"
        }

    # =====================================
    # Query Normalization
    # =====================================

    def normalize_query(
        self,
        query
    ):

        normalized_query = (
            query.lower()
        )

        for phrase, replacement in (
            self.quarter_mappings.items()
        ):

            normalized_query = (
                normalized_query.replace(
                    phrase,
                    replacement
                )
            )

        return normalized_query

    # =====================================
    # Query Processing
    # =====================================

    def process_query(
        self,
        query
    ):

        # =====================================
        # Normalize Query
        # =====================================

        normalized_query = (
            self.normalize_query(query)
        )

        filters = {}

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

                filters["department"] = (
                    department
                )

        # =====================================
        # Quarter Detection
        # =====================================

        quarter_match = re.search(

            r"\b(Q[1-4])\b",

            normalized_query,

            re.IGNORECASE
        )

        if quarter_match:

            filters["quarter"] = (
                quarter_match.group(1)
                .upper()
            )

        # =====================================
        # Year Detection
        # =====================================

        year_match = re.search(

            r"\b(20\d{2})\b",

            normalized_query
        )

        if year_match:

            filters["year"] = (
                year_match.group(1)
            )

        # =====================================
        # Chroma Filter Formatting
        # =====================================

        formatted_filters = None

        if len(filters) == 1:

            key = list(filters.keys())[0]

            formatted_filters = {
                key: filters[key]
            }

        elif len(filters) > 1:

            formatted_filters = {

                "$and": [

                    {key: value}

                    for key, value
                    in filters.items()
                ]
            }

        return {

            "query": normalized_query,

            "filters": formatted_filters
        }