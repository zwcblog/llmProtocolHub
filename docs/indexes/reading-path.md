# 阅读路径

如果你第一次来到这个项目，不必从头到尾顺序阅读。更高效的方式，是按你的问题类型进入。

## 1. 我只想尽快找到某个平台的官方入口

从这里开始：

- [厂商卷](../vendors/README.md)
- [总索引](../INDEX.md)

适合场景：

- 记不起官网、文档、控制台分别在哪里
- 想快速回到某个厂商的权威入口
- 只需要先找对资料，不急着做能力比较

## 2. 我在多个厂商之间做接入或迁移

从这里开始：

- [兼容性索引](compatibility.md)
- [OpenAI Compatible API](../protocols/openai-compatible/README.md)
- [工具调用约定](../protocols/tool-calling/README.md)
- [流式输出格式](../protocols/streaming/README.md)
- [多模态消息结构](../protocols/multimodal/README.md)

适合场景：

- 想知道“看起来兼容”到底兼容到什么程度
- 正在做统一 SDK、网关或封装层
- 需要先识别高风险分歧，而不是盲目平铺抽象

## 3. 我在理解协议边界

从这里开始：

- [协议卷](../protocols/README.md)
- [Model Context Protocol (MCP)](../protocols/mcp/README.md)
- [Agent2Agent (A2A)](../protocols/a2a/README.md)
- [工具调用约定](../protocols/tool-calling/README.md)

适合场景：

- 想弄清楚 MCP、A2A、Tool Calling 分别解决什么问题
- 不确定某个问题属于模型推理层、工具接入层还是 Agent 协作层
- 在设计 Agent 系统或多工具运行时

## 4. 我关心某类能力，而不是某个厂商

从这里开始：

- [能力索引](capabilities.md)

适合场景：

- 想看谁支持 Embeddings / Tool Calling / Streaming / Multimodal
- 在做方案选型，而不是厂商定向接入
- 需要按能力横向比较入口

## 5. 我是第一次接触这个项目，想先理解它的边界

从这里开始：

- [首页](../home.md)
- [总索引](../INDEX.md)
- [维护规范](../MAINTENANCE.md)

适合场景：

- 想确认这个站点是否值得长期收藏
- 想理解它为什么不写成长篇教程
- 想知道它解决的到底是什么问题

## 一个简单建议

如果你没有特别明确的目标，不要先看单页正文，先看：

1. [首页](../home.md)
2. [能力索引](capabilities.md)
3. [兼容性索引](compatibility.md)
4. 再进入具体厂商页或协议页

这样会比直接在正文里来回跳转更省时间。
