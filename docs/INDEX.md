# LLM Protocol Hub

AI 厂商模型协议官方文档汇总参考手册。

这个站点按两条主线组织：

- **厂商视角**：看不同平台的 API 能力、字段设计和接入差异
- **协议视角**：看 OpenAI Compatible API、MCP、A2A、流式输出、工具调用、多模态等抽象规范

## 从哪里开始

- 新读者：先看 [总索引](INDEX.md)
- 想补内容：先看 [维护规范](MAINTENANCE.md)
- 按厂商查：进入 [厂商总览](vendors/README.md)
- 按协议查：进入 [协议总览](protocols/README.md)

## 当前覆盖范围

### 厂商

- OpenAI
- Anthropic
- Google Gemini
- xAI
- Mistral
- Cohere
- DeepSeek
- 智谱 AI
- MiniMax
- 阿里云百炼
- 百度千帆
- 腾讯混元
- 火山引擎

### 协议

- OpenAI Compatible API
- Model Context Protocol (MCP)
- Agent2Agent (A2A)
- 流式输出格式
- 工具调用约定
- 多模态消息结构

## 维护原则

- 只引用官方文档、官方 SDK、官方博客、官方 Changelog
- 优先做结构化摘要，不直接堆砌原文
- 对“兼容”保持谨慎，明确是字段兼容、路径兼容还是行为兼容
- 每条关键信息尽量附原始链接

## 仓库地址

- GitHub: [zwcblog/llmProtocolHub](https://github.com/zwcblog/llmProtocolHub)
