
load_dotenv()

if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    raise ValueError("HUGGINGFACEHUB_API_TOKEN not found in environment variables")


if __name__ == "__main__":
    print("Server is running....................................")
