# Getting started with shared models

The term “Shared Model” refers to models that are used communally by all clients. Through the shared hosting of our LLMs, we enable a large number of users to cost-effectively access these powerful models and utilize them for their specific applications.

Further information about the licenses and endpoints of the provided models can be found on the [Available shared models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) page.

To start with shared models you need to enable AI Model Serving and create an auth token. Upon completing this step you are ready to use the inference API. In this guide, you choose a model and start with inference.

## Prerequisites

- You have a STACKIT customer account
- You have a STACKIT user account
- You have a STACKIT project

## Enable AI Model Serving and create an auth token

To enable AI Model Serving, log in to the Customer portal and click AI Model Serving in the sidebar on the left. If it is not enabled yet, enable the feature and confirm the activation.

After AI Model Serving is enabled, create an authentication token:

1. In the top bar, click Create token.
2. In the new pane, enter a token name and optionally a lifetime in days.
3. To confirm, click Order fee-based.
4. Save the generated token to a safe location.
5. Click Close.

You cannot retrieve the token again after closing the pane.

After you created and saved your authentication token, decide which model you want to use. Read the [Available Shared Models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models) page to get information about all available models. In this guide we use Llama 3.3 70B. Now you are ready to use the model.

## Write a first message and receive the answer

To write the first message to your chat model, you need to use the API. There is no chat window yet, because this product is designed for API-first use.

Run the following command to write your first message to the chat model. Use the following parameters:

- auth-token: The AI Model Serving auth token
- Additional parameters such as system prompt and temperature are available, but for this tutorial they are left unchanged.

Example command:

```bash
curl -X POST "https://api.openai-compat.model-serving.eu01.onstackit.cloud/v1/chat/completions" \
  --header "Authorization: Bearer [auth-token]" \
  --header "Content-Type: application/json" \
  --data '{
    "model": "cortecs/Llama-3.3-70B-Instruct-FP8-Dynamic",
    "messages": [
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": "Why is this documentation great?"}
    ],
    "max_completion_tokens": 250,
    "temperature": 0.1
  }'
```

The model responds with JSON output containing the generated answer. You can then parse the application/json response in your client application.

After you exchanged your first message with the chat model, you can continue with the relevant how-tos or tutorials for deeper integration.

## Related information

- [Available shared models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models)
- [Manage auth tokens](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/how-tos/manage-auth-tokens)
- [First steps with common frameworks](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/tutorials/first-steps-with-common-frameworks)
