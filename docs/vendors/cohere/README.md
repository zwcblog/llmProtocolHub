# Cohere

## 一句话判断

Cohere 的辨识度并不只是聊天模型，而在于它长期在文本理解、Embedding 与 Rerank 这些检索增强能力上具有稳定存在感；理解它时，不能只用“LLM 聊天接口”这一种视角去观察。

## 官方入口

- 官网：<https://cohere.com/>
- 平台入口：<https://dashboard.cohere.com/>
- 官方文档：<https://docs.cohere.com/>
- API Reference：<https://docs.cohere.com/reference/about>
- 官方 SDK：<https://github.com/cohere-ai/cohere-typescript>
- Changelog / Release Notes：以官方文档与平台说明为准

## 接口形态

- 主 API 形态：围绕文本生成、Embedding、Rerank 等能力提供平台 API
- 兼容层：如存在兼容接入，也应以 Cohere 原生能力组织为准
- 工具调用：支持情况应以最新官方文档确认
- 流式输出：支持情况需按 API 文档核对
- 多模态输入：支持范围取决于平台当前能力开放情况
- Rerank：其长期具有代表性的能力方向之一

## 平台边界

- 产品线划分：最值得区分的是聊天生成能力与检索增强能力，不应只把 Cohere 理解成“另一家聊天模型平台”
- 官方推荐入口：先从文档总览进入，再按 Chat、Embed、Rerank 等能力分类深入
- 常见误区：只比较大模型聊天效果，而忽略 Cohere 在检索链路中的位置
- 迁移注意事项：从通用聊天平台迁移或对接时，要重点确认模型命名、Rerank 接口、Embedding 维度与平台鉴权方式

## 能力范围

- Text / Chat：支持
- Embeddings：重点能力方向之一
- Rerank：重点能力方向之一
- 工具调用 / 多模态：支持情况以官方说明为准
- 流式输出：支持情况以最新 API 文档为准

## 备注

如果你的系统涉及检索增强生成（RAG）、排序优化或向量检索链路，Cohere 往往比只看通用聊天能力更值得纳入对照。
