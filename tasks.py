# tasks.py
from crewai import Task
from agents import financial_analyst, verifier
from tools import search_tool, FinancialDocumentTool

# Task: Analyze Financial Document
analyze_financial_document = Task(
    description=(
        "Analyze the provided financial document to extract key insights including "
        "revenue trends, profitability metrics, cash flow analysis, debt levels, "
        "and market risks. Provide a comprehensive financial health assessment "
        "based on the document content. Focus on quantitative data and factual analysis."
    ),
    expected_output="""A structured financial analysis containing:
- Revenue and profit trend analysis
- Key financial ratios (P/E, debt-to-equity, ROA, ROE, current ratio)
- Cash flow assessment
- Identified risks and opportunities
- Overall financial health summary with specific recommendations""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# Task: Investment Analysis
investment_analysis = Task(
    description=(
        "Based on the financial data extracted from the document, provide detailed "
        "investment recommendations. Analyze financial ratios, growth potential, "
        "competitive position, and industry trends. Use search capabilities to "
        "gather current market context when necessary."
    ),
    expected_output="""Investment recommendation report including:
- Clear Buy/Hold/Sell recommendation with reasoning
- Supporting financial metrics and ratios
- Risk-adjusted return potential
- Market position analysis
- At least 3 specific investment considerations
- Timeline for investment thesis""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool, search_tool],
    async_execution=False,
)

# Task: Risk Assessment
risk_assessment = Task(
    description=(
        "Conduct a comprehensive risk assessment based on the financial document. "
        "Evaluate liquidity risks, credit risks, market volatility exposure, "
        "operational risks, and regulatory concerns. Provide actionable risk "
        "mitigation strategies."
    ),
    expected_output="""Detailed risk assessment including:
- Liquidity risk analysis
- Credit risk evaluation
- Market and volatility risk exposure
- Operational risk factors
- Regulatory and compliance risks
- Specific mitigation strategies for each risk category
- Risk score or rating with justification""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False,
)

# Task: Document Verification
verification = Task(
    description=(
        "Verify whether the uploaded document is a legitimate financial document. "
        "Check for standard financial reporting elements including financial "
        "statements, accounting data, financial ratios, and proper document "
        "structure. Identify document type and credibility."
    ),
    expected_output="""Document verification report containing:
- Document type identification (10-K, 10-Q, earnings report, etc.)
- Verification status (Valid/Invalid financial document)
- Key financial elements found (balance sheet, income statement, cash flow)
- Document completeness assessment
- Confidence level in document authenticity""",
    agent=verifier,  # Fixed: was using financial_analyst
    tools=[FinancialDocumentTool.read_data_tool],
    async_execution=False
)