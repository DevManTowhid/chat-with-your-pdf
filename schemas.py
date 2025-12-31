from pydantic import Field, BaseModel

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

