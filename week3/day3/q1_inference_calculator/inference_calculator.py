# inference_calculator.py

# ✅ Step 1: Import required module
import argparse  # Used to handle command-line arguments

# ✅ Step 2: Define model profiles (sample values)
model_profiles = {
    "7B": {
        "vram": 16,           # in GB
        "token_speed": 100,   # tokens/sec
        "base_latency": 0.2,  # seconds
        "cost_per_1k": 0.0    # Free (local)
    },
    "13B": {
        "vram": 26,
        "token_speed": 60,
        "base_latency": 0.4,
        "cost_per_1k": 0.0
    },
    "GPT-4": {
        "vram": 50,
        "token_speed": 20,
        "base_latency": 1.0,
        "cost_per_1k": 0.06  # $0.06 per 1K tokens (est.)
    }
}

# ✅ Step 3: Main calculation function
def calculate_inference(model_size, tokens, batch_size, hardware_type, deployment_mode):
    profile = model_profiles.get(model_size)
    if not profile:
        raise ValueError("Model profile not found")

    # 🔹 Latency = base + (tokens / speed)
    latency = profile["base_latency"] + (tokens / profile["token_speed"])

    # 🔹 Memory usage = model VRAM + 0.5 * tokens * batch_factor
    batch_factor = 0.1 if hardware_type == "GPU" else 0.2  # GPUs are more efficient
    memory_usage = profile["vram"] + (tokens * batch_size * batch_factor / 1000)

    # 🔹 Cost = (tokens / 1000) * cost_per_1k
    cost = (tokens / 1000) * profile["cost_per_1k"]

    # 🔹 Compatibility (simple check)
    compatible = "Yes" if (hardware_type == "GPU" and memory_usage <= 40) else "Check Hardware"

    return {
        "latency_sec": round(latency, 2),
        "memory_usage_gb": round(memory_usage, 2),
        "cost_usd": round(cost, 4),
        "hardware_ok": compatible
    }

# ✅ Step 4: CLI Interface
def main():
    parser = argparse.ArgumentParser(description="LLM Inference Calculator")
    parser.add_argument("--model_size", choices=["7B", "13B", "GPT-4"])
    parser.add_argument("--tokens", type=int)
    parser.add_argument("--batch_size", type=int, default=1)
    parser.add_argument("--hardware_type", choices=["GPU", "CPU"])
    parser.add_argument("--deployment_mode", choices=["cloud", "local"])

    args = parser.parse_args()

    result = calculate_inference(
        args.model_size,
        args.tokens,
        args.batch_size,
        args.hardware_type,
        args.deployment_mode
    )

    print("\n📊 Inference Estimate")
    print(f"Model: {args.model_size}")
    print(f"Latency: {result['latency_sec']} sec")
    print(f"Memory Usage: {result['memory_usage_gb']} GB")
    print(f"Cost: ${result['cost_usd']}")
    print(f"Hardware Compatibility: {result['hardware_ok']}")

# ✅ Step 5: Entry point
if __name__ == "__main__":
    main()
