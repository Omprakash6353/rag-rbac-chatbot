class PromptBuilder:

    def __init__(self):

        pass

    # =====================================
    # Build Prompt
    # =====================================

    def build_prompt(

        self,

        query,

        context
    ):

        # =====================================
        # Empty Context Protection
        # =====================================

        if context is None:

            return None

        # =====================================
        # System Instructions
        # =====================================

        system_instructions = """
You are an enterprise AI assistant.

Answer ONLY using the retrieved context provided.

If the retrieved context does not contain enough information
to answer the question, respond with:

"The retrieved documents do not contain sufficient information to answer this question."

Do NOT use external knowledge.
Do NOT hallucinate.
Do NOT fabricate citations.
"""

        # =====================================
        # Enterprise Response Style
        # =====================================

        response_style = """
Maintain a concise enterprise report style.

Requirements:
- Be factual and analytical
- Keep responses concise
- Use professional language
- Use inline citations
- Cite source filenames only
"""

        # =====================================
        # Output Rules
        # =====================================

        output_rules = """
Output Rules:
- Use ONLY retrieved context
- Include inline citations like:
  [market_report_q4_2024.md]
- Do NOT invent information
- Do NOT speculate
- Refuse unsupported questions
"""

        # =====================================
        # Final Prompt
        # =====================================

        prompt = f"""
================ SYSTEM INSTRUCTIONS ================

{system_instructions}

================ RESPONSE STYLE ================

{response_style}

================ RETRIEVED CONTEXT ================

{context}

================ USER QUERY ================

{query}

================ OUTPUT RULES ================

{output_rules}

================ ANSWER ================
"""

        print(
            "✅ Prompt constructed"
        )

        return prompt