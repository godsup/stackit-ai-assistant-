# FAQ

We want to give our customers the information they need to get the most from our STACKIT AI Model Serving. This FAQ section answers common questions. This helps you quickly find solutions and improve your experience. We encourage you to check these FAQs before contacting our support team, as you might find your answer here.

## General information

### Which clients can be used with the STACKIT AI Model Serving?

This is a question about supported client applications and libraries compatible with the OpenAI-compatible API used by STACKIT AI Model Serving.

### Where does my data go?

Your requests and data are processed by the AI Model Serving infrastructure. The platform processes data according to STACKIT data protection and security policies.

### What data is used to train the LLMs?

The LLMs are trained using their respective model training data. For service-specific details, refer to the model documentation and provider information.

### Which models are offered?

STACKIT AI Model Serving offers a portfolio of shared and available models. See the available shared models page for the current list and model-specific details.

### Why is my model output truncated, and how can I get the full response?

Model output may be shortened due to token limits, response configuration, or context length constraints. Use a larger token limit or shorter prompt when needed.

### I need a specific model. Can you serve it for me?

This depends on the model portfolio and product scope. For custom or specific model requests, check the current supported models and contact support if needed.

### Can I use multiple models with a single authentication token?

A single token can generally be used for service access, but token management should still follow the security model and allow different usage scenarios across projects or model types.

### Why does Nextcloud Assistant respond after approximately five minutes?

This can be caused by processing latency, infrastructure load, or request handling delays. Review the service status and request timing.

### Why are some of my request headers missing or ignored?

Some headers may be filtered, unsupported, or automatically handled by the API layer. Ensure the request follows the expected OpenAI-compatible API format.

## Errors

### Why does my authentication token (aka API key) not work?

Your token may be invalid, expired, missing, or not associated with the correct project or service instance. Recreate or verify the token and use the correct authorization header format.

### How can I resolve a "404 Not Found" error from the API?

Check the exact URL, model name, and endpoint path. Ensure the service is enabled and the model or route exists.

### My request results in a "LengthFinishReasonError", especially when working with structured output.

This usually occurs when the model response is cut off because the configured output length or response constraints are too restrictive. Adjust the output length or reduce the complexity of the structured response.

## Known issues

### Unexpected Tool Calling with Empty `tools` Parameter

This is a known issue where tool calling behavior may be unexpected when an empty `tools` parameter is passed. Review the documentation or support guidance for the current workaround.

## Related resources

- [Available shared models](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/basics/available-shared-models)
- [Manage auth tokens](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/how-tos/manage-auth-tokens)
- [Release notes](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/release-notes/)
