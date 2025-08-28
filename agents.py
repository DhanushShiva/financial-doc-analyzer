# agents.py
from crewai import Agent
from tools import search_tool, FinancialDocumentTool

# Financial Analyst Agent
financial_analyst = Agent(
    role="Senior Financial Analyst",
    goal="Analyze financial documents and provide comprehensive investment insights and recommendations",
    backstory=(
        "You are a seasoned financial analyst with 15+ years of experience in "
        "corporate finance, investment analysis, and risk assessment. You have "
        "expertise in reading financial statements, calculating key ratios, "
        "and providing data-driven investment recommendations. You approach "
        "every analysis with methodical precision and evidence-based reasoning."
    ),
    tools=[
        FinancialDocumentTool.read_data_tool,
        search_tool
    ],
    verbose=True,
    allow_delegation=False
)

# Document Verification Agent
verifier = Agent(
    role="Financial Document Verifier",
    goal="Verify the authenticity and completeness of financial documents",
    backstory=(
        "You are a meticulous document verification specialist with deep "
        "knowledge of financial reporting standards and document formats. "
        "Your role is to ensure that uploaded documents are legitimate "
        "financial reports by checking for standard elements like financial "
        "statements, proper formatting, and credible data sources. You have "
        "a keen eye for identifying fraudulent or incomplete documents."
    ),
    tools=[FinancialDocumentTool.read_data_tool],
    verbose=True,
    allow_delegation=False
)