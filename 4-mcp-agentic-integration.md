# Communication Patterns Between MCP and Agentic AI Systems

When integrating MCP with an agent framework, the communication between the **LLM (agent reasoning)** and the **MCP servers (tools)** follows a structured pattern. At a high level, the agent (acting as an MCP host) will **discover available tools** and then **invoke tools on demand**, all through MCP's JSON-based protocol.

## JSON-RPC Messaging

MCP uses JSON-RPC 2.0 as the message format for client-server communication:
- Every action is encoded as a JSON request (with a method name and parameters)
- Tools respond with JSON results or errors
- The MCP transport layer handles serializing the protocol-specific messages into JSON-RPC objects and back

In practice, an MCP client in the agent might call methods like `tools/list` or `tools/call` which the server understands.

Transport options include:
- **Stdio transport**: For local servers, sends JSON-RPC messages over the process's stdin/stdout pipes (simple for local tool processes)
- **SSE (Server-Sent Events) transport**: For remote or networked servers, where the client makes HTTP POSTs for requests and the server streams responses over an HTTP stream

Both achieve the same logical pattern – a **bidirectional channel** where the agent can request tool execution and the server can send back results (or even push notifications if needed).

## Tool Discovery

Once the agent's MCP client connects to a server, it typically performs a *capability exchange*:
- The client can query the server for what "tools" (operations) it offers using the standardized method `tools/list`
- The server responds with a list of tool names, each with an interface (expected parameters, description, etc.)
- The agent framework will use this to register those functions in the agent's context

For example, AutoGen's MCP adapter calls `tools/list` and then dynamically creates corresponding tool functions in the agent's tool registry (using AutoGen's `McpToolAdapter` which maps MCP tools to AutoGen's `BaseTool` interface). This makes the MCP tools seamlessly available for the LLM to call, just like any built-in tool.

## Invoking a Tool

When the LLM agent decides to use a tool, how is that expressed and executed?
- Typically, the agent framework either uses the LLM's **function calling** feature or parses the LLM's output to detect a tool usage
- For instance, OpenAI's GPT-4 might return a `{"function": "fetch", "arguments": {...}}` call, or an agent using chain-of-thought might output a special token indicating a tool action
- The agent runtime catches that and triggers the MCP client to perform `tools/call` with the specified tool name and arguments
- This is a JSON-RPC request that goes to the appropriate MCP server, which then runs the actual tool code and returns a result (or error) in the response
- The agent then provides that result back to the LLM (often feeding it into the prompt as observation) to continue the reasoning

This loop continues until the task is done. For example, when a user asks an agent to *"Summarize the content of [a URL]"*, the agent's LLM might respond with a FunctionCall to `fetch` the URL, which the framework executes via MCP. The fetched content comes back as a result and the LLM then produces the summary.

## Parallel and Multi-step Interactions

MCP is request-response, but agent frameworks can interleave multiple tool calls in one overall session:
- An agent might call `tools/list` on startup for each server, then decide among multiple servers which tool to use at a given step
- The **MCP client maintains separate sessions per server** (1:1 client-server connection) to isolate their state
- So an agent connected to a "filesystem" server and a "database" server will have two channels
- This ensures, for example, that the filesystem server's state (like working directory or open file handles) is kept separate from the database server's state
- The agent can route requests to the correct server's client
- All these communications use the JSON-RPC id to track responses so the agent knows which call corresponds to which request

## MCP vs Direct Integration

The benefit of using MCP for tools is that the agent doesn't need bespoke code for each integration – any software made MCP-compatible can be plugged in.

The pattern encourages a **separation of concerns**:
- Tool builders focus on the tool logic in the MCP server
- Agent builders focus on the prompting and decision logic in the host
- Communication is standardized (method calls like `tools/call`)
- Secure boundaries can be enforced (the server only exposes certain actions)

This does add an extra hop (calls go through JSON-RPC rather than direct function calls), but it makes the system more modular. As noted in one analysis, the *key advantage* is offloading complexity – you avoid hard-coding tool use in the agent, and instead "connect to existing MCP servers that handle the complex interactions" for you.

The trade-off is some added latency and setup complexity, which we'll discuss in the scalability section.
