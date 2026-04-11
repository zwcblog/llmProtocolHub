# Model Context Protocol (MCP)

## 一句话定义

MCP 试图解决的不是“如何调用模型”，而是“模型运行时如何以统一方式接入外部工具、资源与提示上下文”。它关心的是上下文协作层，不是厂商推理 API 本身。

## 官方来源

- 官方主页：<https://modelcontextprotocol.io/>
- 官方规范：<https://modelcontextprotocol.io/specification/2025-03-26>
- 官方文档：<https://modelcontextprotocol.io/docs/getting-started/intro>
- 官方仓库：<https://github.com/modelcontextprotocol>
- 参考实现：<https://github.com/modelcontextprotocol/typescript-sdk>

## 核心对象

- 参与角色：MCP Host、MCP Client、MCP Server
- 关键对象：Tools、Resources、Prompts、Sampling、Roots
- 核心能力：能力声明、上下文暴露、工具调用、资源读取、提示共享

## 关键流程

- 初始化：客户端与服务端建立连接并交换协议版本与能力声明
- 能力发现：客户端根据服务端暴露的 tools、resources、prompts 等能力决定可用交互面
- 请求 / 响应：围绕 JSON-RPC 风格消息进行调用与返回
- 流式交互：可根据 transport 与实现能力支持增量通信或事件通知
- 错误处理：依赖协议层错误返回与能力协商，不应把厂商模型错误语义直接等同于 MCP 错误语义

## 与其他协议的边界

- 与 OpenAI Compatible API：后者主要解决模型推理接口兼容，MCP 解决的是模型运行时与外部能力之间的接入协议
- 与 A2A：A2A 更偏向 Agent 之间的协作与任务交换，MCP 更偏向 Agent 或主机如何接入工具与上下文源
- 与厂商私有协议：不少厂商都有自己的工具调用或插件机制，而 MCP 的价值在于给这些能力提供一个相对中立的统一接入面

## 实践中的意义

- 适用场景：桌面 Agent、IDE 助手、需要统一接入多种工具与知识源的运行时环境
- 不适用场景：只想直接调用模型文本生成接口、没有外部上下文接入需求的简单 API 封装
- 最容易误判的地方：把 MCP 当成“另一个模型 API 标准”；实际上，它更接近模型外部能力的适配层协议

## 备注

理解 MCP 时，最重要的不是先背字段，而是先分清它与模型推理接口、Agent 协作协议、厂商工具调用格式之间的边界。
