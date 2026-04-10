# 文档总索引

这份手册按两条主线组织：

- 厂商：站在接入方视角，看不同平台的 API 能力与差异。
- 协议：站在抽象层视角，看 MCP、A2A、OpenAI Compatible 这类接口规范。

## 厂商索引

- [厂商总览](vendors/README.md)
- [OpenAI](vendors/openai/README.md)
- [Anthropic](vendors/anthropic/README.md)
- [Google Gemini](vendors/google-gemini/README.md)
- [xAI](vendors/xai/README.md)
- [Mistral](vendors/mistral/README.md)
- [Cohere](vendors/cohere/README.md)
- [DeepSeek](vendors/deepseek/README.md)
- [智谱 AI](vendors/zhipu/README.md)
- [MiniMax](vendors/minimax/README.md)
- [阿里云百炼](vendors/alibaba-bailian/README.md)
- [百度千帆](vendors/baidu-qianfan/README.md)
- [腾讯混元](vendors/tencent-hunyuan/README.md)
- [火山引擎](vendors/volcengine/README.md)

## 协议索引

- [协议总览](protocols/README.md)
- [OpenAI Compatible API](protocols/openai-compatible/README.md)
- [Model Context Protocol (MCP)](protocols/mcp/README.md)
- [Agent2Agent (A2A)](protocols/a2a/README.md)
- [流式输出格式](protocols/streaming/README.md)
- [工具调用约定](protocols/tool-calling/README.md)
- [多模态消息结构](protocols/multimodal/README.md)

## 建议维护顺序

1. 先补齐每个厂商页的官方文档入口、基础地址、鉴权方式、核心接口。
2. 再补协议页中的字段对照与兼容差异。
3. 最后追加模型能力矩阵、迁移说明和常见坑位。

## 维护规范

- [维护规范](MAINTENANCE.md)
- [厂商页模板](templates/vendor-doc-template.md)
- [协议页模板](templates/protocol-doc-template.md)
