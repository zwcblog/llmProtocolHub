# 多模态消息结构

## 一句话定义

多模态消息结构解决的不是“模型是否支持图片或音频”这种能力层问题，而是“不同类型输入怎样以统一、可解析、可扩展的方式进入同一次交互”。它看似只是请求体结构，实际上直接决定了跨厂商迁移与统一抽象的难度。

## 官方来源

- OpenAI 参考：<https://platform.openai.com/docs/guides/images>
- Anthropic 参考：<https://docs.anthropic.com/en/docs/build-with-claude/vision>
- Gemini 参考：<https://ai.google.dev/gemini-api/docs/image-understanding>
- 相关兼容背景：可结合 [OpenAI Compatible API](../openai-compatible/README.md) 一起理解

## 核心对象

- 参与角色：客户端、模型服务端、可选的文件存储或媒体托管服务
- 关键对象：message、content block / part、image、audio、video、file reference、URL、Base64 数据
- 核心能力：在同一轮请求中，把文本与图片、音频、视频等内容组织成模型可理解的统一输入

## 常见表达方式

- 内容数组：以 `content` 数组或 `parts` 数组承载不同类型的输入块
- 媒体引用：通过 URL、File ID、平台文件句柄或上传后的引用标识传递媒体对象
- 内联数据：通过 Base64 或等价方式直接嵌入媒体内容
- 类型标记：通过 `type`、`mime_type`、`media_type` 等字段标识具体内容类别

## 厂商差异

- 容器结构不同：有的平台使用 message + content block，有的平台使用 role + parts
- 媒体传参方式不同：URL、Base64、file upload、平台托管引用等支持程度不同
- 音频 / 视频支持深度不同：有的平台只支持图片理解，有的平台支持更丰富的原生多模态输入
- System 与多模态的组合方式不同：system prompt 是否能与媒体块并列、是否单独成段，各家差异明显

## 与相邻概念的边界

- 与工具调用：多模态消息结构解决“输入怎么表示”，工具调用解决“模型如何请求外部动作”
- 与流式输出：一个处理输入组织，一个处理输出传输；两者常同时出现，但不是一回事
- 与 OpenAI Compatible API：很多兼容接口在纯文本场景看起来接近，但在多模态结构上最容易出现分叉

## 实践中的意义

- 适用场景：图片理解、音频输入、视频分析、多模态问答、视觉 Agent、内容审核等
- 不适用场景：纯文本单轮生成、无需外部媒体输入的简单调用
- 最容易误判的地方：把“支持图片输入”误认为“多模态消息结构兼容”；真正的迁移成本往往藏在内容块组织、文件引用方式与媒体类型约束里

## 备注

如果你在做多厂商抽象，多模态结构通常比纯文本接口更早暴露分歧；先把消息容器、媒体引用和类型标记三层抽象分开，会比直接抹平成一个统一字段更稳。
