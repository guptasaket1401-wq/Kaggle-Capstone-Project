from agents.research_agent import ResearchAgent
from agents.analysis_agent import AnalysisAgent
from agents.summary_agent import SummaryAgent

class Coordinator:
    def __init__(self, session_memory, memory_bank, tools):
        self.session_memory = session_memory
        self.memory_bank = memory_bank

        self.research = ResearchAgent(
            google_search=tools["google"],
            file_loader=tools["file_loader"]
        )

        self.analysis = AnalysisAgent(
            code_execution=tools["code_exec"]
        )

        self.summary = SummaryAgent(memory_bank)

    async def run(self, user_query: list[str]):
        # store user query in session state
        self.session_memory.set("last_query", user_query)

        research_output = await self.research.run(user_query)
        analysis_output = await self.analysis.run(research_output)
        final_output = await self.summary.run(analysis_output)

        return final_output
