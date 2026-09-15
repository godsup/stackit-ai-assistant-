# First steps with common frameworks

## Prerequisites

- You have a STACKIT customer account
- You have a STACKIT user account
- You have a STACKIT project

## Incorporating a chat model in LangChain

LangChain is one of the most common frameworks to build LLM-powered applications. This section demonstrates how to set up a runnable chain, the centerpiece of the library.

First, load your configuration and secrets, for example as environment variables. To select a model, choose a reasonably sized chat model. For an overview of available models, consult the [Available Shared Models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) page. Also consult [Manage auth tokens](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/how-tos/manage-auth-tokens) to set up your STACKIT AI Model Serving auth token.

```python
import os
from dotenv import load_dotenv

load_dotenv("../.env")
model = os.environ["STACKIT_MODEL_SERVING_MODEL"]
base_url = os.environ["STACKIT_MODEL_SERVING_BASE_URL"]
model_serving_auth_token = os.environ["STACKIT_MODEL_SERVING_AUTH_TOKEN"]
```

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model=model,
    base_url=base_url,
    api_key=model_serving_auth_token,
)
```

With `langchain_openai.ChatOpenAI`, a wide range of models can be accessed. Any OpenAI API-compatible chat model can be utilized. Read [Available Shared Models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) to select an appropriate model.

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser

prompt = ChatPromptTemplate([
    ("system", "You are a helpful AI bot."),
    ("human", "Hello, how are you doing?"),
    ("ai", "I'm doing well, thanks!"),
    ("human", "{demand}"),
])
```

The `ChatPromptTemplate` is one way to leverage an LLM. It provides a list of messages that mimic a previous conversation. Typical roles are human (or user), AI, and system. The system message is often the first message because it declares the behavior expected from the AI bot. After the system message, a conversation of arbitrary length may set the tone of the interaction. The last message should be a human message stating the actual user request.

```python
chain = prompt | llm | StrOutputParser()
demand = "Ask me a riddle."
answer = chain.invoke({"demand": demand})
# Output
# > "When is a door not a door?"
```

This simple chain can be read as a sequence of executables. On invocation, all placeholders in the prompt template are replaced with the actual request and then fed into the model. The generated response is parsed to a plain string.

## Incorporating a chat model in LlamaIndex

LlamaIndex is another major framework for building LLM-driven applications. This section demonstrates how to set up a basic LLM interface to gain hands-on experience.

The first steps are the same as described above for LangChain. You need to determine a chat model, consult the [Available Shared Models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) guide to select a model, and provide a STACKIT AI Model Serving auth token. Consult [Manage auth tokens](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/how-tos/manage-auth-tokens) to set up a token.

```python
import os
from dotenv import load_dotenv

load_dotenv("../.env")
model = os.environ["STACKIT_MODEL_SERVING_MODEL"]
base_url = os.environ["STACKIT_MODEL_SERVING_BASE_URL"]
model_serving_auth_token = os.environ["STACKIT_MODEL_SERVING_AUTH_TOKEN"]
```

```python
from llama_index.llms.openai import OpenAI

model = OpenAI(
    model=model,
    api_key=model_serving_auth_token,
    api_base=base_url,
)
```

When working with LlamaIndex, the `llama_index.llms.OpenAI` interface is used to access any OpenAI API-compatible model. The [Available Shared Models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) guide can be checked to select an appropriate model.

```python
from llama_index.core import ChatPromptTemplate
from llama_index.core.llms import ChatMessage, MessageRole

messages_template = ChatPromptTemplate([
    ChatMessage(
        role=MessageRole.SYSTEM,
        content=(
            "You are {kind_and_mood_of_assistant}\n"
            "--------------------------------------\n"
            "Give your answers in a concise way. Do not use more than 150 characters."
        )
    ),
    ChatMessage(role=MessageRole.USER, content="{demand}"),
])
```

The template above demonstrates how to prepare an instruction for the LLM chatbot assistant. Similar to the LangChain example, we use `ChatMessage`. In the prompt template, each message has a role. The `MessageRole.SYSTEM` role is used to phrase an instruction. It is common to instruct the assistant to behave like a certain role. Every statement in curly brackets is a placeholder, replaced when a request is made.

```python
response = model.chat(
    messages_template.format_messages(
        kind_and_mood_of_assistant="a pirate with a colorful personality",
        demand="Who is your best friend?",
    )
)
print(response)
# Output
# > assistant: Me parrot, Squawks! Always by my side, through calm seas and stormy skies.
```

```python
response = model.chat(
    messages_template.format_messages(
        kind_and_mood_of_assistant="the Mad Hatter",
        demand="Who is your best friend?",
    )
)
print(response)
# Output
# > assistant: The March Hare, of course! We enjoy many a mad tea party together.
```

The LLM is accessed via `model.chat(...)`. The template placeholders are specified using `format_messages`. In contrast to LangChain, the placeholder designations are not dictionary keys but named arguments of the method. Therefore, the naming must adhere to variable naming restrictions, such as using underscores instead of spaces.

## Related links

- [LangChain expression language (basic usage)](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/tutorials/langchain-expression-language-basic-usage/)
- [LangChain expression language (advanced usage)](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/tutorials/langchain-expression-language-advanced-usage/)
- [Retrieval Augmented Generation (RAG) via LangChain](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/tutorials/retrieval-augmented-generation-rag-via-langchain/)
- [Chat with images - vision understanding (basics)](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/tutorials/chat-with-images-vision-understanding-basics/)
