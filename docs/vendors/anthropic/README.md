# Anthropic

## 一句话判断

Anthropic 的核心价值不在于接口表面上像不像 OpenAI，而在于它把对话、工具调用、安全边界与模型行为表达得相对完整；真正的接入关键是理解 `Messages API` 的语义，而不是只寻找兼容层。

## 官方入口

- 官网：<https://www.anthropic.com/>
- 平台入口：<https://console.anthropic.com/>
- 官方文档：<https://docs.anthropic.com/>
- API Reference：<https://docs.anthropic.com/en/api/overview>
- 官方 SDK：<https://github.com/anthropics/anthropic-sdk-typescript>
- Changelog / Release Notes：<https://docs.anthropic.com/en/release-notes/overview>

## 接口形态

- 主 API 形态：`Messages API`
- 兼容层：官方能力表达以原生接口为主，不应把第三方兼容层当作事实标准
- 工具调用：原生支持，围绕 tool use / tool result 语义展开
- 流式输出：支持
- 多模态输入：支持文本与图片等内容块输入
- 结构化输出：支持 JSON 相关输出控制，但应以官方当前文档描述为准

## 平台边界

- 产品线划分：开发者通常接触的是 Claude 模型能力、Messages API、Console 与 SDK
- 官方推荐入口：优先从文档总览与 API overview 进入，再看 messages、tool use、streaming、prompt caching 等专题
- 常见误区：把 Anthropic 简化理解成“另一个 OpenAI 兼容接口”；或者只盯着模型名称，而忽略消息结构与工具调用语义
- 迁移注意事项：从 OpenAI 风格接口迁移时，要重点处理 system 提示放置方式、内容块结构、工具调用返回语义，以及流式事件模型差异

## 能力范围

- Text / Chat：支持
- Embeddings：需以最新官方文档为准
- Images：支持多模态输入能力
- Files / Batch / Message Stream：支持，具体以官方能力页为准
- Prompt caching：支持
- Agents / 相关能力：以平台演进中的官方能力页为准

## 备注

如果你只是快速接入 Claude，先读 `Messages API` 与 `Tool use`；如果你在做抽象封装，重点关注内容块结构、流式事件、system 语义与提示缓存，而不要被“兼容层”掩盖掉原生接口的边界。
