from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field


# Load environment variables from .env file


load_dotenv()

if not os.getenv("HUGGINGFACEHUB_API_TOKEN"):
    raise ValueError(" ❌ CRITICAL: HUGGINGFACEHUB_API_TOKEN not found in environment variables")


app = FastAPI(
    title = "Chat with your PDF",
    description="An AI-powered PDF assistant that leverages Hugging Face models to answer questions based on the content of your PDF documents.",
    version="1.0.0",
)


class QuestionRequest(BaseModel):
    query : str = Field(
        ...,
        title = "User Query",
        description = "The question posed by the user regarding the PDF content.",
        min_length = 5,
        max_length = 1024,
        examples="What is the main topic of the document?"
    )
    

    class Config:
        schema_extra = {
            "example": {
                "query": "What is the main topic of the document?"
            }
        }




if __name__ == "__main__":
    print("Server is running....................................")
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000)