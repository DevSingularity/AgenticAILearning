from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import phi
import os
from phi.playground import Playground, serve_playground_app

load_dotenv()

phi.api=os.getenv("PHIDATA_API_KEY")

# This is for accessing the agent through Phidata
# Use a valid Groq chat model
model = Groq(id="llama-3.1-8b-instant")

financial_intelligence_agent = Agent(
    name="Financial Intelligence Agent",
    role="Provide financial analysis, analyst recommendations, and latest stock news with sources.",
    model=model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=False,   # reduce token load
            company_news=True
        ),
        DuckDuckGo()
    ],
    instructions=[
        "Use tables to display analyst recommendations clearly.",
        "Summarize news in bullet points.",
        "Always include source links for news.",
        "Keep responses concise and structured."
    ],
    show_tool_calls=False,   # reduce token usage
    markdown=True,
)

app=Playground(agents=[financial_intelligence_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)