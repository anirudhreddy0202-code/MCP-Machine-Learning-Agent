# my_client.py
import asyncio

from agents.mcp import MCPServerStdio
from mcp_client_demo import params, call


async def main():
    async with MCPServerStdio(
        params=params,
        client_session_timeout_seconds=120
    ) as server:

        # Discover available tools
        tools = await server.list_tools()

        print(f"The server offers {len(tools)} tools:")
        for tool in tools:
            print("  -", tool.name)

        # Train both models
        await call(server, "train_models", {"request_id": "hw-train"})

        # Test all 114 patients
        disagreements = []

        for i in range(114):
            sample = await call(
                server,
                "get_sample_input",
                {"index": i, "request_id": f"hw-sample-{i}"}
            )

            result = await call(
                server,
                "predict_both",
                {
                    "input_data": sample["input_data"],
                    "request_id": f"hw-both-{i}",
                }
            )

            if not result["models_agree"]:
                disagreements.append(i)
                print(
                    f"Patient {i}: true = {sample['true_class']}, "
                    f"logistic regression = {result['logistic_regression']}, "
                    f"knn = {result['knn']}"
                )

        print(
            f"\nThe models disagree on "
            f"{len(disagreements)} of 114 test patients."
        )


asyncio.run(main())