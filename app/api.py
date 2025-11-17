from fastapi import APIRouter
from agents.coordinator import Coordinator
from tools.google_search import GoogleSearchTool
from tools.file_loader import FileLoaderTool
from tools.code_exec import CodeExecutionTool
from memory.session_memory import InMemorySessionService
from memory.memory_bank import MemoryBank

router = APIRouter()

session_mem = InMemorySessionService()
memory_bank = MemoryBank()

tools = {
    "google": GoogleSearchTool(),
    "file_loader": FileLoaderTool(),
    "code_exec": CodeExecutionTool()
}

coordinator = Coordinator(session_mem, memory_bank, tools)

@router.post("/run")
async def run_system(query: list[str]):
    return await coordinator.run(query)
