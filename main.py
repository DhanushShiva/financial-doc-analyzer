# main.py
import os
from crewai import Crew, Process
from tasks import analyze_financial_document, investment_analysis, risk_assessment, verification
from agents import financial_analyst, verifier

def main():
    """
    Main entry point for the Financial Document Analyzer.
    Processes a sample Tesla financial report through verification and analysis.
    """
    
    print("=" * 60)
    print("Financial Document Analyzer - CrewAI")
    print("=" * 60)
    
    # Path to sample document
    sample_doc = os.path.join("data", "TSLA-Q2-2025-Update.pdf")
    
    if not os.path.exists(sample_doc):
        print(f"Error: Sample document not found at {sample_doc}")
        print("Please ensure the data directory contains the Tesla report.")
        return
    
    print(f"Processing document: {sample_doc}")
    print("-" * 60)
    
    try:
        # Step 1: Document Verification
        print("\nStep 1: Document Verification")
        print("-" * 30)
        
        verification_crew = Crew(
            agents=[verifier],
            tasks=[verification],
            process=Process.sequential,
            verbose=True
        )
        
        verification_result = verification_crew.kickoff(
            inputs={"file_path": sample_doc}
        )
        
        print("Verification Result:")
        print(verification_result)
        
        # Step 2: Financial Analysis
        print("\n" + "=" * 60)
        print("Step 2: Financial Document Analysis")
        print("-" * 30)
        
        analysis_crew = Crew(
            agents=[financial_analyst],
            tasks=[analyze_financial_document],
            process=Process.sequential,
            verbose=True
        )
        
        analysis_result = analysis_crew.kickoff(
            inputs={"file_path": sample_doc, "query": "Analyze Tesla Q2 2025 financial performance"}
        )
        
        print("Financial Analysis Result:")
        print(analysis_result)
        
        # Step 3: Investment Analysis
        print("\n" + "=" * 60)
        print("Step 3: Investment Recommendation")
        print("-" * 30)
        
        investment_crew = Crew(
            agents=[financial_analyst],
            tasks=[investment_analysis],
            process=Process.sequential,
            verbose=True
        )
        
        investment_result = investment_crew.kickoff(
            inputs={"file_path": sample_doc, "query": "Provide investment recommendation for Tesla"}
        )
        
        print("Investment Analysis Result:")
        print(investment_result)
        
        # Step 4: Risk Assessment
        print("\n" + "=" * 60)
        print("Step 4: Risk Assessment")
        print("-" * 30)
        
        risk_crew = Crew(
            agents=[financial_analyst],
            tasks=[risk_assessment],
            process=Process.sequential,
            verbose=True
        )
        
        risk_result = risk_crew.kickoff(
            inputs={"file_path": sample_doc, "query": "Assess financial risks for Tesla investment"}
        )
        
        print("Risk Assessment Result:")
        print(risk_result)
        
        print("\n" + "=" * 60)
        print("Analysis Complete!")
        print("=" * 60)
        
    except Exception as e:
        print(f"Error during analysis: {str(e)}")
        print("Please check your dependencies and file paths.")

def analyze_custom_document(file_path: str, query: str = "Analyze this financial document"):
    """
    Analyze a custom financial document.
    
    Args:
        file_path: Path to the financial document
        query: Specific query for analysis
    """
    if not os.path.exists(file_path):
        print(f"Error: Document not found at {file_path}")
        return
    
    print(f"Analyzing custom document: {file_path}")
    
    # Run full analysis pipeline
    crew = Crew(
        agents=[verifier, financial_analyst],
        tasks=[verification, analyze_financial_document, investment_analysis, risk_assessment],
        process=Process.sequential,
        verbose=True
    )
    
    result = crew.kickoff(
        inputs={"file_path": file_path, "query": query}
    )
    
    return result

if __name__ == "__main__":
    main()