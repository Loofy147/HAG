import argparse
import torch
from src.agents import NativelyRecursiveAgent, ResilientHAGModel, GeneralDataLoader

def main():
    parser = argparse.ArgumentParser(description="HAG Build 2.1 - Sovereign Intelligence Entry Point")
    parser.add_argument("--domain", type=str, default="physics", choices=["physics", "finance", "legal"], help="Data domain to analyze")
    parser.add_argument("--query", type=str, default="Analyze current patterns", help="Query for the agent")
    parser.add_argument("--device", type=str, default="auto", help="Device to use (cuda/cpu/auto)")

    args = parser.parse_args()

    if args.device == "auto":
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    else:
        device = torch.device(args.device)

    print(f"--- HAG Build 2.1 Initialized on {device} ---")

    loader = GeneralDataLoader(input_dim=16)
    x, y = loader.load_domain_data(domain=args.domain)

    if x is None:
        print(f"Error: Data for domain '{args.domain}' not found.")
        return

    model = ResilientHAGModel(input_dim=16)
    agent = NativelyRecursiveAgent(base_model=model)

    print(f"Processing query: '{args.query}' on {len(x)} samples...")
    result = agent.solve_complex_task(args.query, f"Domain: {args.domain}, Samples: {len(x)}")

    print(f"\nResult: {result}")
    print("\n--- Process Complete ---")

if __name__ == "__main__":
    main()
