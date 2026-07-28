from client import QuantizationCheckerClient

def main():
    client = QuantizationCheckerClient()
    res = client.check_quantization(model_size_b=7)
    print(f"Result for ram_required_gb: {res['ram_required_gb']}")

if __name__ == "__main__":
    main()
