# 协议总览

这里整理跨厂商或抽象层的模型协议与接口规范。

## 为什么单独维护协议页

- 同一家厂商可能同时支持多种协议。
- 不同厂商可能宣称兼容同一协议，但字段和行为并不完全一致。
- 做网关、代理层、SDK、适配器时，协议视角比厂商视角更重要。

## 协议清单

- [OpenAI Compatible API](openai-compatible/README.md)
- [Model Context Protocol (MCP)](mcp/README.md)
- [Agent2Agent (A2A)](a2a/README.md)
- [流式输出格式](streaming/README.md)
- [工具调用约定](tool-calling/README.md)
- [多模态消息结构](multimodal/README.md)
