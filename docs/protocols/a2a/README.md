# Agent2Agent (A2A)

## 一句话定义

A2A 关注的不是模型如何生成文本，也不是工具如何接入模型，而是一个 Agent 如何向另一个 Agent 描述能力、交换任务、传递状态，并在协作过程中维持可理解的交互语义。

## 官方来源

- 官方主页：<https://a2a-protocol.org/>
- 官方规范：<https://a2a-protocol.org/latest/specification/>
- 官方文档：<https://a2a-protocol.org/latest/topics/what-is-a2a/>
- 官方仓库：<https://github.com/a2aproject/A2A>
- 参考实现：以官方仓库与生态项目为准

## 核心对象

- 参与角色：Agent Client、Remote Agent、User / Calling System
- 关键对象：Agent Card、Task、Message、Artifact、State
- 核心能力：能力发现、任务创建、状态跟踪、结果返回、Agent 间协作语义约定

## 关键流程

- 能力发现：通过 Agent Card 或等价机制理解远端 Agent 提供什么能力
- 任务发起：调用方创建 task，请求远端 Agent 执行某项工作
- 状态流转：任务在提交、执行、等待输入、完成或失败等状态之间推进
- 结果回传：远端 Agent 通过 message、artifact 或状态更新返回阶段性或最终结果
- 协作延续：在需要时继续多轮交互，而不是把整个过程压扁成一次模型调用

## 与其他协议的边界

- 与 MCP：MCP 关注的是工具、资源与上下文如何接入运行时；A2A 关注的是 Agent 与 Agent 之间如何协作
- 与 OpenAI Compatible API：后者解决模型推理接口的兼容问题，A2A 不属于模型推理 API 范畴
- 与工具调用：工具调用通常发生在单个 Agent 或宿主内部；A2A 关注的是跨 Agent 的任务交换与能力协商
- 与厂商私有 Agent API：很多厂商会有各自的 Agent 协作机制，而 A2A 的价值在于提供相对中立的协作抽象

## 实践中的意义

- 适用场景：多 Agent 系统、任务分发、跨团队 Agent 能力复用、需要显式状态与结果工件的协作型场景
- 不适用场景：只调用单一模型接口、没有多 Agent 协作需求的简单应用
- 最容易误判的地方：把 A2A 当成“另一个工具调用格式”或“另一个模型 API”；实际上，它更接近 Agent 协作层协议

## 备注

理解 A2A 时，最重要的是先把协作层和推理层拆开：模型负责生成，工具负责执行，A2A 负责让多个 Agent 之间的任务与能力协作变得可交换、可追踪、可继续。
