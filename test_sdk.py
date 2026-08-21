import asyncio
import sys
import time
from google.antigravity import Agent, LocalAgentConfig

async def main():
    print("Booting Antigravity Engine...")
    start_time = time.time()
    
    # We configure a read-only agent since it just needs to GM
    config = LocalAgentConfig(
        system_instructions="You are a helpful assistant testing latency."
    )
    
    async with Agent(config) as agent:
        boot_time = time.time() - start_time
        print(f"[OK] Engine Booted in {boot_time:.2f} seconds.")
        print("-" * 40)
        
        # Test 1
        print("SYS_OP> What is 2+2?")
        req1_start = time.time()
        response = await agent.chat("What is 2+2? Keep it brief.")
        
        # We can stream it or just print the final response
        full_text = ""
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
            full_text += token
        
        req1_time = time.time() - req1_start
        print(f"\n[Response Time: {req1_time:.2f}s]")
        print("-" * 40)
        
        # Test 2 - Proving the second call is instant since it's already running
        print("SYS_OP> And what is 4+4?")
        req2_start = time.time()
        response = await agent.chat("And what is 4+4? Keep it brief.")
        
        full_text = ""
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
            full_text += token
            
        req2_time = time.time() - req2_start
        print(f"\n[Response Time: {req2_time:.2f}s]")

if __name__ == "__main__":
    asyncio.run(main())
