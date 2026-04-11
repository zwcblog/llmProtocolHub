# Mistral

## 一句话判断

Mistral 的价值不只是“又一家通用模型 API”，而在于它同时覆盖云端 API、开源模型与企业部署语境；理解它时，关键是分清平台服务、模型家族与部署形态，而不是只看单一路径的聊天接口。

## 官方入口

- 官网：<https://mistral.ai/>
- 平台入口：<https://console.mistral.ai/>
- 官方文档：<https://docs.mistral.ai/>
- API Reference：<https://docs.mistral.ai/api/>
- 官方 SDK：<https://github.com/mistralai/client-js>
- Changelog / Release Notes：以官方文档与平台更新说明为准

## 接口形态

- 主 API 形态：以官方平台 API 为主
- 部署形态：同时存在云服务、开源模型与企业部署语境
- 工具调用：支持情况应以最新官方文档为准
- 流式输出：支持
- 多模态输入：支持范围取决于具体模型与能力开放情况
- Embeddings / OCR / Agents：需按官方能力页分别确认

## 平台边界

- 产品线划分：最容易混淆的是“平台 API 能力”“开源模型能力”与“企业部署方案”之间的边界
- 官方推荐入口：先看文档总览与 API Reference，再按聊天、Embedding、OCR 或 Agents 等主题深入
- 常见误区：把开源模型能力与云平台 API 默认视为完全等价；或只按模型名字判断平台能力
- 迁移注意事项：从其他国际平台迁移时，要重点确认模型命名、流式语义、工具调用支持、部署方式与鉴权差异

## 能力范围

- Text / Chat：支持
- Embeddings：支持情况以最新官方文档为准
- OCR / 多模态：支持情况按能力页确认
- Agents / 高级能力：应以官方文档描述为准
- 流式输出：支持

## 备注

Mistral 适合放在“平台 API + 模型部署形态”双重视角下理解；如果你只把它当成一个聊天 endpoint，会错过它真正的产品边界。
