# 工具调用约定

## 一句话定义

工具调用并不是某一家厂商独有的新能力，而是当前主流模型 API 逐渐形成的一类事实标准：让模型在生成文本之外，能够显式表达“我想调用某个外部函数或工具”，再由宿主环境决定是否执行与如何回填结果。

## 官方来源

- OpenAI 参考：<https://platform.openai.com/docs/guides/function-calling>
- Anthropic 参考：<https://docs.anthropic.com/en/docs/agents-and-tools/tool-use/overview>
- Gemini 参考：<https://ai.google.dev/gemini-api/docs/function-calling>
- 相关兼容背景：可结合 [OpenAI Compatible API](../openai-compatible/README.md) 一起理解

## 核心对象

- 参与角色：模型、宿主应用、外部工具 / 函数执行器
- 关键对象：tool / function 定义、参数 schema、tool call 请求、tool result 回填消息
- 核心能力：让模型在对话过程中结构化地请求外部能力，而不是把调用意图藏在自然语言里

## 关键流程

- 工具声明：宿主应用在请求中向模型声明可用工具及其参数模式
- 调用决策：模型根据上下文决定是否发起工具调用，以及调用哪个工具
- 参数生成：模型生成结构化参数，通常要求满足 JSON Schema 或等价约束
- 宿主执行：真正执行工具的是宿主系统，而不是模型本身
- 结果回填：工具执行结果再次进入对话上下文，供模型继续完成回答

## 与相邻概念的边界

- 与 Structured Output：Structured Output 更强调输出格式受约束；工具调用强调的是“请求外部动作”的语义
- 与 Agent：Agent 往往把工具调用作为能力基础之一，但 Agent 还涉及规划、状态管理、多轮决策等更高层语义
- 与 MCP：MCP 解决的是工具与上下文源如何被统一接入；工具调用约定解决的是模型如何在推理过程中表达调用请求
- 与 OpenAI Compatible API：很多兼容接口会复用类似字段，但字段名相似并不代表调用语义完全一致

## 厂商差异

- 工具声明字段命名不同：`tools`、`functions`、`functionDeclarations` 等
- 参数模式支持程度不同：有的偏宽松，有的更接近严格 JSON Schema
- 调用结果回填结构不同：不同平台在 message role、content block、tool result 表示上差异明显
- 流式事件差异明显：部分平台会在 stream 中增量输出 tool call 信息，部分平台则以更高层事件表达

## 实践中的意义

- 适用场景：查询数据库、调用业务 API、执行检索、接入外部工作流、构建 Agent 能力
- 不适用场景：只需要固定格式文本输出、没有外部动作需求的简单生成任务
- 最容易误判的地方：把“模型提出调用请求”误认为“模型已经完成调用”；真正的执行控制权始终在宿主系统手里

## 备注

理解工具调用时，最重要的不是记字段名，而是记住边界：模型负责提出结构化调用意图，宿主负责决定是否执行、如何执行，以及是否信任结果。
