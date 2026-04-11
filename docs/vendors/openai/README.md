# OpenAI

## 一句话判断

OpenAI 依然是当前通用模型 API 生态最重要的基准面，但它自己的平台能力与接口形态也变化最快，因此“看哪份官方文档”本身就是接入成本的一部分。

## 官方入口

- 官网：<https://openai.com/>
- 平台入口：<https://platform.openai.com/>
- 官方文档：<https://platform.openai.com/docs/overview>
- API Reference：<https://platform.openai.com/docs/api-reference>
- 官方 SDK：<https://github.com/openai/openai-node>
- Changelog / Release Notes：<https://platform.openai.com/docs/changelog>

## 接口形态

- 主 API 形态：`Responses API` 正在成为新的统一入口
- 兼容旧接口：`Chat Completions API` 仍被广泛使用
- 工具调用：原生支持
- 流式输出：支持
- 多模态输入：支持文本、图片、音频等多种输入形态
- 结构化输出：支持 JSON Schema / Structured Outputs

## 平台边界

- 产品线划分：开发者最常接触的是 Platform API、模型能力页、SDK 与 Playground
- 官方推荐入口：如无特殊原因，应优先从平台文档概览进入，再按能力跳转到具体 API
- 常见误区：把旧版 Chat Completions 视为唯一主接口；或只看 SDK README 而忽略平台文档
- 迁移注意事项：接入新能力时，应优先确认 Responses、Realtime、Audio、Images 等能力是否已归入统一接口语义，而不要只凭历史经验套用旧模型调用方式

## 能力范围

- Text / Chat：支持
- Embeddings：支持
- Images / Audio：支持
- Realtime / Batch / Files：支持
- Fine-tuning：支持
- Agents / 相关能力：平台能力持续演化中，应以最新文档为准

## 备注

如果你只是想快速开始，先看平台文档概览与 API Reference；如果你在做迁移或兼容层封装，重点看 Responses、Structured Outputs、Tool Calling 与 Changelog。
