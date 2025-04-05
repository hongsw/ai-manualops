# MCP Integration in an Elixir Environment

Is it possible to integrate MCP communication in an Elixir-based system? Absolutely – thanks to MCP's open spec and simple wire format, an Elixir application can act as an MCP host or even implement servers, even though official SDKs for Elixir don't exist (yet).

## Using JSON-RPC from Elixir

Elixir can leverage existing JSON-RPC libraries or write a thin client to speak MCP:
- MCP's spec is language-agnostic (SDKs are provided for Python, TS, Java, etc., but not required)
- Every MCP message is just JSON; for instance a tool call might be: `{"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": { ... }}`
- Elixir's `Jason` library could encode/decode these easily

The two main transports (stdio and SSE) are also straightforward in Elixir:

### Stdio Transport
Elixir can start the MCP server program as a separate OS process and pipe data to its stdin, read from its stdout:
- Using `:os.cmd` or Port to manage the external process
- The Elixir process can send a JSON request line to the server and receive the JSON reply
- Libraries like `Porcelain` or OTP Ports can manage these external processes

### SSE/HTTP Transport
Elixir has HTTP client libraries that could post JSON to a server's `/messages` endpoint and listen to an SSE stream:
- `Mint` or `Finch` could be used for HTTP communications
- However, SSE is one-way from server to client; an easier approach might be to run a small Plug/Cowboy server in Elixir that the MCP server can connect to
- For local deployments, the stdio approach is likely simpler

## Elixir as MCP Client or Server

### As MCP Client
One could implement an **MCP client in Elixir** (the host side) to connect to existing servers:
- An Elixir agent could spawn the official Python *"fetch"* server and communicate via JSON-RPC to use it
- Since the spec is open, an Elixir developer could hand-roll this or possibly generate code from the MCP schema

### As MCP Server
One could implement an **MCP server in Elixir**:
- Imagine wrapping an Elixir function (like an Ecto database query or some Erlang library call) as a tool
- The server would need to accept JSON-RPC requests and dispatch to the appropriate function
- The MCP specification defines standard methods and JSON schemas for requests; adhering to those would be key for compatibility

## Integration with Elixir Agent Frameworks

Projects like Jido or Axon could incorporate MCP fairly naturally:
- An Axon agent (which might already communicate with Python via HTTP) could also launch an MCP server process and handle JSON messaging
- Elixir's concurrency means you can maintain a separate **GenServer process for each MCP server connection**, keeping the communication asynchronous and non-blocking
- This GenServer could manage the lifecycle (start the external process, handle reconnections, etc.) similar to how `mcp-agent` does in Python
- The agent logic (perhaps another process representing the AI's brain) would then call into these GenServers when it needs a tool
- This separation fits well with OTP design principles

## Feasibility and Prior Art

While there isn't an official Elixir MCP SDK yet, the existence of a C# SDK and others shows that implementing the protocol in new languages is feasible.

The core tasks are:
- Parsing JSON
- Managing IDs for requests
- Handling asynchronous messages

All of which Elixir can do very well.

One challenge could be that many MCP servers today are written in Python/TS and might not run on the BEAM. But since MCP encourages a decoupled architecture, an Elixir host can still interact with those external processes.

In short, **Elixir can serve as an MCP orchestrator**, coordinating between the LLM and MCP servers. This might even be beneficial:
- Elixir could supervise the MCP servers (restarting them if they crash)
- Throttle calls if needed
- Concurrently handle multiple tool results

## Example Approach

Imagine an Elixir Phoenix application that serves as an AI assistant backend:
- It could have a process that on startup runs `fetch_server` and `filesystem_server` (from the MCP repo) as child processes
- The app then has routes or LiveView events that trigger an LLM call
- When the LLM (maybe via OpenAI API) returns a function-call to "fetch", the Elixir code would send the JSON RPC to the fetch server, get the result, then pass it back to the LLM
- This is quite achievable with existing Elixir primitives

Over time, the Elixir community might wrap this up in a friendly library to reduce boilerplate.
