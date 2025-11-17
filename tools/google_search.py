import asyncio

class GoogleSearchTool:
    async def search(self, query: str):
        # mock implementation for academic submission
        await asyncio.sleep(0.1)
        return [f"Result for '{query}'"]
