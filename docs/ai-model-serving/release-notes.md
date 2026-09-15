# Release notes

## Sep 2026

### STACKIT AI Model Serving: New Model Release Qwen3.8 27B (Replacement for Qwen3.6 27B)

We are excited to announce that we are upgrading our model lineup by introducing `Qwen/Qwen3.8-27B`, which will serve as the successor to our current Qwen offerings.

As the successor of Qwen3.6 27B, the newer Qwen3.8 27B generally improves quality across all fields of application, while maintaining the focus on coding tasks. It was trained on a broad mix of publicly available data and post-trained for code generation, debugging, and technical reasoning, while also supporting general assistant tasks. With a context window of 262K tokens, it can handle large codebases and complex multi-step workflows.

As part of this transition, we are officially deprecating the following model:

- `Qwen/Qwen3.6-27B`

We kindly ask all customers to migrate their workloads to the new model `Qwen/Qwen3.8-27B` before December 08, 2026.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## Jul 2026

### STACKIT AI Model Serving: New Model Release Google Gemma 4 (Replacement for Google Gemma 3)

We are excited to announce that we are upgrading our model lineup by introducing `google/gemma-4-31B-it`, which will serve as the successor to our current Google-Gemma offerings.

Gemma 4 models are multimodal, handling text and image input and generating text output. Gemma 4 features a context window of up to 256K tokens and maintains multilingual support in over 140 languages. Gemma 4 models are well-suited for a variety of text generation and image understanding tasks, including question answering, summarization, and reasoning. The large context window of 256K and the improved reasoning capabilities make this model particularly well-suited to agent-based workflows.

As part of this transition, we are officially deprecating the following model:

- `google/gemma-3-27b-it`

We kindly ask all customers to migrate their workloads to the new model `google/gemma-4-31B-it` before 14 October 2026.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## May 2026

### STACKIT AI Model Serving: Model release Qwen3.6 27B

We are excited to announce the release of Qwen3.6 27B, a coding-focused language model from the Qwen team, to our shared LLM model portfolio.

Qwen3.6 27B is post-trained for code generation, debugging, and technical reasoning, while also supporting general assistant tasks. With a context window of 262K tokens, it can handle large codebases and complex multi-step agentic workflows.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## Mar 2026

### STACKIT AI Model Serving: New Model Release GPT-OSS 20B (Replacement for Llama-8B and Nemo)

We are excited to announce that we are upgrading our model lineup by introducing `openai/gpt-oss-20b`, which will serve as the successor to our current Mistral-Nemo and Llama 3.1 8B offerings.

By leveraging 4-bit (MXFP4) quantization, this new 20-billion parameter model provides a significant boost in reasoning capabilities while maintaining the low-latency performance our customers expect. Applications such as real-time chatbots, retrieval-augmented generation (RAG), and agentic workflows will benefit from improved tool-calling and higher throughput.

#### Deprecation Notice

As part of this transition, we are officially deprecating the following models:

- `neuralmagic/Mistral-Nemo-Instruct-2407-FP8`
- `neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8`

We kindly ask all customers to migrate their workloads to the new model `openai/gpt-oss-20b` before 4 June 2026.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## Feb 2026

### STACKIT AI Model Serving: New Model Release Qwen3-VL-Embedding-8B as Multi-Modal Embedding

We are excited to announce the addition of Qwen3-VL-Embedding-8B to our shared LLM model portfolio. This is a state-of-the-art multimodal embedding model designed to bridge the gap between visual and textual data.

Unlike traditional text-only models, Qwen3-VL-Embedding-8B projects both text and images into a unified semantic vector space. This release unlocks powerful cross-modal retrieval capabilities for your applications, allowing you to perform text-to-image search, image-to-text search, and complex multimodal RAG workflows.

#### Key Upgrades

This generation delivers comprehensive improvements in vector representation and retrieval accuracy:

- Unified multimodality: computes semantic embedding vectors from chat messages containing both text and images.
- High-fidelity embeddings: features an output dimension of 4096 and 8 billion parameters for deep semantic nuance.
- Extended context: supports a maximum input of 32,000 tokens.
- Multi-language reach: optimized support for over 30 languages.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## Jan 2026

### STACKIT AI Model Serving: New Model Release Qwen3-VL-235B-A22B

We’re excited to announce the release of Qwen3-VL-235B-A22B, the most powerful vision-language model in the Qwen series to date, to our shared LLM model portfolio. This model brings a major leap in reasoning, tool calling capabilities, long-context reliability, and visual capabilities.

This generation delivers comprehensive upgrades across the board: superior text understanding and generation, deeper visual perception and reasoning, extended context length, enhanced spatial and video dynamics comprehension, and stronger agent interaction capabilities.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/getting-started/getting-started-with-shared-models). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## Dec 2025

### STACKIT AI Model Serving: New Model Release GPT-OSS-120B

We’re excited to announce the release of GPT-OSS-120B, the most capable model in the GPT-OSS family to date, to our shared LLM model portfolio. This model brings a major leap in reasoning, tool calling capabilities, and long-context reliability.

GPT-OSS-120B is designed to be used within agentic workflows with strong instruction following and reasoning capabilities. The model provides full chain-of-thought (CoT) and supports structured outputs.

Explore our full model portfolio, and access detailed examples and tutorials in our [documentation](https://docs.stackit.cloud/products/data-and-ai/ai-model-serving/). Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.

## May 2025

### STACKIT AI Model Serving is now available

From 6 May 2025, we can offer you the new STACKIT AI Model Serving service.

STACKIT AI Model Serving offers you easy pay-as-you-go access to proven GenAI models, such as Llama 3.3 or Gemma, in a secure environment on the data-sovereign STACKIT Cloud. As a building block of our Data & AI Platform, STACKIT AI Model Serving enables you to use various Large Language Models (LLMs) with maximum data sovereignty. Your data and your queries are neither stored nor used to train models. You choose the LLM that is right for you and receive a seamless user experience when integrating it into your applications thanks to our API.

Our [Help Center](https://support.stackit.cloud/servicedesk/customer/portal/3) is always at your disposal if you have any questions.
