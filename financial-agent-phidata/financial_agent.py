from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

web_search_agent=Agent(
    name="Web search agent",
    role="Search the web for information about the stock",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,   
)

financial_agent=Agent(
    name="Finance AI agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=False),
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=False,
    markdown=True,
)

mutli_ai_agent=Agent(
    team=[web_search_agent, financial_agent],
    model=Groq(id="llama-3.1-8b-instant"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=False,
    markdown=True
)

mutli_ai_agent.print_response("Summarize analyst recommendation and share latest news for NVIDIA", stream=False)