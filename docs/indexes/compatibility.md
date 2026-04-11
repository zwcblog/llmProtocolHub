# 兼容性索引

这不是一份承诺“完全等价”的兼容性矩阵，而是一份帮助你快速定位兼容入口与分歧边界的导航页。

## OpenAI Compatible API

- [OpenAI Compatible API](../protocols/openai-compatible/README.md)
- [DeepSeek](../vendors/deepseek/README.md)
- [阿里云百炼](../vendors/alibaba-bailian/README.md)
- [百度千帆](../vendors/baidu-qianfan/README.md)
- [腾讯混元](../vendors/tencent-hunyuan/README.md)
- [火山引擎](../vendors/volcengine/README.md)
- [xAI](../vendors/xai/README.md)

> 兼容接口通常足以让应用先跑起来，但真正的差异常常暴露在工具调用、流式、结构化输出与多模态输入层。

## Tool Calling

- [OpenAI](../vendors/openai/README.md)
- [Anthropic](../vendors/anthropic/README.md)
- [Google Gemini](../vendors/google-gemini/README.md)
- [智谱 AI](../vendors/zhipu/README.md)
- [阿里云百炼](../vendors/alibaba-bailian/README.md)
- [xAI](../vendors/xai/README.md)
- [工具调用约定](../protocols/tool-calling/README.md)

> 字段名相似并不代表调用语义等价；执行轮次、结果回填与流式事件往往更容易出现不兼容。

## Streaming

- [OpenAI](../vendors/openai/README.md)
- [Anthropic](../vendors/anthropic/README.md)
- [Google Gemini](../vendors/google-gemini/README.md)
- [DeepSeek](../vendors/deepseek/README.md)
- [智谱 AI](../vendors/zhipu/README.md)
- [阿里云百炼](../vendors/alibaba-bailian/README.md)
- [xAI](../vendors/xai/README.md)
- [流式输出格式](../protocols/streaming/README.md)

> 真正难兼容的往往不是 `stream=true` 这个参数，而是事件粒度、结束语义与异常处理。

## Multimodal

- [OpenAI](../vendors/openai/README.md)
- [Anthropic](../vendors/anthropic/README.md)
- [Google Gemini](../vendors/google-gemini/README.md)
- [MiniMax](../vendors/minimax/README.md)
- [多模态消息结构](../protocols/multimodal/README.md)

> 纯文本接口的相似性，常常会在多模态输入结构这里被迅速打破。

## Protocol / Runtime Layer

- [Model Context Protocol (MCP)](../protocols/mcp/README.md)
- [Agent2Agent (A2A)](../protocols/a2a/README.md)
- [OpenAI Compatible API](../protocols/openai-compatible/README.md)

> 不同协议解决的是不同层次的问题：模型推理接口、工具接入层与 Agent 协作层，并不应被混成同一张表。
