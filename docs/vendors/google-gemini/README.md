# Google Gemini

## 一句话判断

Gemini 最容易让人困惑的地方，不是模型本身，而是入口分裂：Gemini Developer API 与 Vertex AI 同时存在，语义相近但产品边界、文档组织与适用场景并不完全相同。

## 官方入口

- 官网：<https://deepmind.google/technologies/gemini/>
- Gemini Developer API：<https://ai.google.dev/>
- Vertex AI Gemini：<https://cloud.google.com/vertex-ai/generative-ai/docs>
- API Reference：<https://ai.google.dev/gemini-api/docs>
- 官方 SDK：<https://github.com/googleapis/js-genai>
- Changelog / Release Notes：<https://ai.google.dev/gemini-api/docs/changelog>

## 接口形态

- 主 API 形态：`generateContent` / `streamGenerateContent` 及相关能力接口
- 平台分叉：Gemini Developer API 面向开发者快速接入；Vertex AI 面向 Google Cloud 体系内的企业化接入
- 工具调用：支持 function calling
- 流式输出：支持
- 多模态输入：原生支持文本、图片、音频、视频等内容部件
- 实时能力：Live API 等能力应以最新官方文档为准

## 平台边界

- 产品线划分：最常见的误判是把 Gemini Developer API 与 Vertex AI 文档混为一谈
- 官方推荐入口：如无 GCP 强依赖，先从 Gemini Developer API 文档进入；若涉及企业权限、区域、合规或云上集成，再看 Vertex AI
- 常见误区：只按模型名搜索而不区分 API 所属平台；或者把 Vertex AI 的接入要求套到 Developer API 上
- 迁移注意事项：从 OpenAI 或 Anthropic 风格迁移时，要重点处理内容部件结构、函数调用定义方式、多模态输入组织方式，以及不同平台下的认证与 endpoint 差异

## 能力范围

- Text / Chat：支持
- Embeddings：支持，具体入口以官方文档为准
- Images / Audio / Video：支持多模态输入与部分相关生成能力
- Files / Batch：支持，能力分布需区分 Developer API 与 Vertex AI
- Live / Realtime：支持相关实时交互能力
- Fine-tuning / 企业能力：更多见于 Vertex AI 体系

## 备注

理解 Gemini 的第一步，不是先背接口名，而是先确认你到底要用的是 Developer API 还是 Vertex AI；很多“文档找不到”或“字段对不上”的问题，根源都在这里。
