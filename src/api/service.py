import json
import logging
from typing import AsyncGenerator, List
from uuid import UUID
import base64
from agents import RawResponsesStreamEvent, Runner, trace, Agent, ToolCallOutputItem
from openai.types.responses import (
    ResponseTextDeltaEvent,
    ResponseCompletedEvent,
)
from fastapi.responses import StreamingResponse
from agent import build_zlv_agent
from message import ClientMessage, convert_to_openai_messages
from visualizations import BaseVisualization

logger = logging.getLogger(__name__)


# Integrate logfire logging into the OriChatService class
class OriChatServiceAgent:

    async def handle_chat_request(
        self,
        messages: List[ClientMessage],
    ) -> StreamingResponse:


        ori_agent = await build_zlv_agent()

        # Generate the streaming response
        stream_generator = self._stream_chat_response(
            messages=messages, ori_agent=ori_agent,
        )

        # Create the streaming response with appropriate headers
        response = StreamingResponse(stream_generator)

        # Set header required by Vercel AI SDK for data streams
        response.headers["x-vercel-ai-data-stream"] = "v1"

        return response

    async def _stream_chat_response(
        self,
        ori_agent: Agent,
        messages: List[ClientMessage],
    ) -> AsyncGenerator[str, None]:
        """
        Stream chat response in the requested protocol format.

        Args:
            messages: List of chat messages
            protocol: Stream protocol to use ('data' or 'text')

        Yields:
            String chunks in the appropriate format for the selected protocol
        """
        # try:
        # Format messages for OpenAI

        formatted_inputs = convert_to_openai_messages(
            messages=messages
        )

        run_streaming = Runner.run_streamed(
            ori_agent, input=formatted_inputs,
        )
        # Process the streaming response
        async for event in run_streaming.stream_events():
            if not isinstance(event, RawResponsesStreamEvent):
                continue
            data = event.data
            if isinstance(data, ResponseTextDeltaEvent):
                yield f"0:{json.dumps(data.delta)}\n"
            elif isinstance(data, ResponseCompletedEvent):
                prompt_tokens = 0
                completion_tokens = 0
                finish_reason = "done"
                yield f'd:{{"finishReason":"{finish_reason}","usage":{{"promptTokens":{prompt_tokens},"completionTokens":{completion_tokens}}}}}\n'

        for item in run_streaming.new_items:
            if isinstance(item, ToolCallOutputItem):
                output = item.output
                if isinstance(output, str):
                    continue
                if isinstance(output, BaseVisualization):
                    data = output.model_dump_json()
                    base64_json = base64.b64encode(data.encode()).decode()
                    string_to_yield = f'k:{{"data":"{base64_json}","mimeType":"application/json+visualization"}}\n'
                    yield string_to_yield
                    # Donne moi la répartition par usage de mes équipements
