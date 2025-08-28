# tools.py
from crewai.tools import tool
import os
import requests
from typing import Optional

class FinancialDocumentTool:
    """Tool for reading and extracting data from financial documents."""
    
    @tool("Read Financial Document")
    def read_data_tool(file_path: str) -> str:
        """
        Reads a financial document (PDF or TXT) and returns its text content.
        
        Args:
            file_path: Path to the financial document file
            
        Returns:
            Extracted text content from the document
        """
        if not os.path.exists(file_path):
            return f"Error: File not found at path: {file_path}"

        try:
            if file_path.lower().endswith(".txt"):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    return content if content.strip() else "Warning: Document appears to be empty"

            elif file_path.lower().endswith(".pdf"):
                try:
                    import PyPDF2
                    with open(file_path, "rb") as f:
                        reader = PyPDF2.PdfReader(f)
                        text = ""
                        for page_num, page in enumerate(reader.pages):
                            page_text = page.extract_text()
                            if page_text:
                                text += f"\n--- Page {page_num + 1} ---\n"
                                text += page_text
                        
                        if not text.strip():
                            return "Warning: No text could be extracted from PDF"
                        return text

                except ImportError:
                    return "Error: PyPDF2 library not installed. Please install with: pip install PyPDF2"
                except Exception as pdf_error:
                    return f"Error reading PDF: {str(pdf_error)}"

            else:
                return f"Error: Unsupported file format. Please provide a .pdf or .txt file. Got: {file_path}"

        except Exception as e:
            return f"Error reading file {file_path}: {str(e)}"

@tool("Search Financial Information")
def search_tool(query: str) -> str:
    """
    Search for financial and market information related to the query.
    
    Args:
        query: Search query for financial information
        
    Returns:
        Search results or simulated financial data
    """
    try:
        # For demo purposes, return simulated search results
        # In production, this would connect to a real search API
        simulated_results = {
            "market trends": "Current market showing volatility due to inflation concerns and geopolitical tensions.",
            "investment": "Diversified portfolio recommended with focus on defensive stocks and bonds.",
            "risk": "Current risk factors include interest rate changes, supply chain disruptions, and regulatory changes.",
            "tesla": "TSLA showing strong fundamentals with growing EV market share but facing increased competition.",
            "financial ratios": "Key ratios to monitor include P/E ratio, debt-to-equity, current ratio, and ROE.",
        }
        
        # Simple keyword matching for demo
        query_lower = query.lower()
        for keyword, result in simulated_results.items():
            if keyword in query_lower:
                return f"Search results for '{query}': {result}"
        
        return f"Search completed for '{query}'. General market analysis suggests maintaining diversified portfolio with regular risk assessment."
        
    except Exception as e:
        return f"Search error for query '{query}': {str(e)}"