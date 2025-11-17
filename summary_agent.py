import asyncio
from observability.logger import logger
from observability.metrics import metrics

class ResearchAgent:
    def __init__(self, google_search, file_loader):
        self.google_search = google_search
        self.file_loader = file_loader

    async def run(self, query_list, min_results=5):
        logger.info("ResearchAgent starting", queries=query_list)

        results = []

        async def search_one(q):
            return await self.google_search.search(q)

        # LOOP + PARALLEL BEHAVIOR
        while len(results) < min_results:
            parallel_output = await asyncio.gather(
                *[search_one(q) for q in query_list]
            )
            for batch in parallel_output:
                results.extend(batch)

        metrics.increment("research.documents_processed", len(results))
        logger.info("ResearchAgent completed", count=len(results))

        return results[:min_results]
