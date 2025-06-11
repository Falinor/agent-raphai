import logging
import traceback
from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, ValidationError

from service import OriChatServiceAgent
from message import ClientMessage

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="ZLV AI Assistant API",
    description="AI Assistant API for ZLV with SQL capabilities and data visualization",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request models
class ChatRequest(BaseModel):
    messages: List[ClientMessage]

class HealthResponse(BaseModel):
    status: str
    message: str

# Initialize the chat service
chat_service = OriChatServiceAgent()

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(status="healthy", message="ZLV AI Assistant API is running")

@app.post("/chat")
async def chat_endpoint(request: ChatRequest) -> StreamingResponse:
    """
    Chat endpoint that handles conversations with the ZLV AI Assistant
    
    Args:
        request: ChatRequest containing messages
        
    Returns:
        StreamingResponse with chat data
    """
    try:
        logger.debug(f"Messages count: {len(request.messages)}")
        
        # Validate that we have at least one message
        if not request.messages:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one message is required"
            )
        
        # Handle the chat request using the service
        response = await chat_service.handle_chat_request(
            messages=request.messages,
        )
        
        return response
        
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid request data: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error processing chat request: {e}")
        logger.error(f"Traceback: {traceback.format_exc()}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error occurred while processing the chat request"
        )

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to ZLV AI Assistant API",
        "version": "1.0.0",
        "docs": "/docs",
        "health": "/health"
    }

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 