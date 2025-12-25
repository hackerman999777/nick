#!/usr/bin/env python3
import time

def main():
    print("[Agent] Started. Awaiting commands... (Press Ctrl+C to exit)")
    try:
        while True:
            cmd = input("Agent> ")
            if cmd.lower() in ("exit", "quit"):
                print("Bye!")
                break
            elif cmd:
                print(f"Command received: {cmd}")
            else:
                continue
    except KeyboardInterrupt:
        print("\n[Agent] Shutting down.")

if __name__ == "__main__":
    main()
