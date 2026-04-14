from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import router

app = FastAPI(
    title="Structured Data Extraction with Vision LLMs and Pydantic",
    description="Extract structured data from invoices using vision LLMs with Pydantic validation",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
async def root():
    return {"service": "vision-llm-extraction", "docs": "/docs"}
