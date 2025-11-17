class CodeExecutionTool:
    async def run(self, script: str, docs: list[str]):
        # mock secure isolated execution for student project
        local_vars = {"docs": docs}
        exec(script, {}, local_vars)
        return local_vars.get("result", {})
