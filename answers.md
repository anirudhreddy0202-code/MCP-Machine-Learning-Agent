# MCP Machine Learning Agent — Assignment Answers

## 1. How many tools did the server list in Part 1, and how many in Part 3? What did you have to change in the client to make the new tool appear?

In Part 1, the server listed 8 tools. After adding the new `predict_both` tool in Part 2, the server listed 9 tools in Part 3. I did not have to change the client code to register the new tool. The client automatically discovered it using `server.list_tools()`. This demonstrates how MCP allows clients to discover tools directly from the server.

## 2. On how many of the 114 test patients do the two models disagree? For each of those patients, which model was right?

The two models disagreed on 8 out of 114 test patients.

- Patient 3: Logistic Regression was correct.
- Patient 25: Logistic Regression was correct.
- Patient 48: Logistic Regression was correct.
- Patient 53: KNN was correct.
- Patient 76: Logistic Regression was correct.
- Patient 80: Logistic Regression was correct.
- Patient 99: Logistic Regression was correct.
- Patient 102: Logistic Regression was correct.

## 3. Overall, which model was right more often when they disagreed?

Logistic Regression was right more often. It correctly predicted 7 out of the 8 disagreements, while KNN correctly predicted only 1. Therefore, Logistic Regression performed better when the two models disagreed on these test patients.

## 4. In your own words: why does the description in triple quotes matter when an AI app uses this tool?

The description in triple quotes explains what the tool does. An AI application reads this description to understand when the tool should be used and what task it performs. A clear description helps the AI select the correct tool and use it appropriately.

## 5. Why is it useful for the server to log every tool call?

Logging every tool call helps track which tools were used, when they were called, and whether they succeeded or failed. It is useful for debugging errors, monitoring the system, reviewing past activity, and maintaining accountability. In this project, the audit log also helps verify that the `predict_both` tool was successfully called for all 114 test patients.