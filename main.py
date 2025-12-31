
load_dotenv()

if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    raise ValueError(" ❌ CRITICAL: HUGGINGFACEHUB_API_TOKEN not found in environment variables")


app = FastAPI(
    name : "Chat with your PDF",
    description="An AI-powered PDF assistant that leverages Hugging Face models to answer questions based on the content of your PDF documents.",
    version="1.0.0",
)


if __name__ == "__main__":
    print("Server is running....................................")
