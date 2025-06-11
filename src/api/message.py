from pydantic import BaseModel
from typing import Optional, List, Union, Dict, Any

class ToolInvocation(BaseModel):
    toolCallId: str
    toolName: str
    args: dict
    result: Union[Dict[str, Any], str]
    state: Optional[str] = None
    step: Optional[int] = None


class ClientMessage(BaseModel):
    role: Optional[str] = None
    content: Optional[str] = None
    #toolInvocations: Optional[List[ToolInvocation]] = None


def convert_to_openai_messages(
    messages: List[ClientMessage],
) -> List[Dict[str, Any]]:
    """Convert client messages to OpenAI format with proper system prompts."""
    openai_messages = []

    for message in messages:
        # Check the message type and format accordingly
        if message.role == "user":
            openai_messages.append({"role": message.role, "content": message.content})
        if message.role == "assistant":
            openai_messages.append({"role": message.role, "content": message.content})
    return openai_messages
