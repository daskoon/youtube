import json
import subprocess
import time

p = subprocess.Popen(
    ["python", "-m", "uv", "--project", "C:\\Users\\transmacsual\\.gemini\\extensions\\youtube-to-docs", "run", "--all-extras", "python", "-m", "youtube_to_docs.mcp_server"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

init_req = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {
            "name": "test-client",
            "version": "1.0.0"
        }
    }
}
p.stdin.write(json.dumps(init_req) + '\n')
p.stdin.flush()

print("Sent init. Waiting for response...")
print(p.stdout.readline())

call_req = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "process_video",
        "arguments": {
            "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        }
    }
}
p.stdin.write(json.dumps(call_req) + '\n')
p.stdin.flush()

print("Sent call. Waiting for response...")
print(p.stdout.readline())
