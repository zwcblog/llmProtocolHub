# AI 厂商模型协议官方文档汇总参考手册

这个仓库用于整理各家 AI 厂商与模型协议的官方文档，目标是做成一份可检索、可对比、可持续维护的参考手册。

## 目标

- 汇总主流 AI 厂商的模型 API、Agent 协议、工具调用、流式输出、多模态、向量接口等官方资料。
- 只记录官方来源，降低二手教程、社区博客带来的信息偏差。
- 用统一结构沉淀不同厂商之间的共性与差异，方便选型、对接、迁移和兼容层开发。

## 收录范围

### 厂商维度

- OpenAI
- Anthropic
- Google Gemini
- xAI
- Mistral
- Cohere
- DeepSeek
- 智谱 AI
- MiniMax
- 阿里云百炼
- 百度千帆
- 腾讯混元
- 火山引擎

### 协议维度

- OpenAI Compatible API
- Model Context Protocol (MCP)
- Agent2Agent (A2A)
- 厂商自定义工具调用协议
- 多模态输入输出约定
- 流式响应格式

## 仓库结构

```text
.
├── README.md
└── docs
    ├── INDEX.md
    ├── vendors
    │   ├── README.md
    │   └── <vendor>/README.md
    ├── protocols
    │   ├── README.md
    │   └── <protocol>/README.md
    └── templates
        ├── vendor-doc-template.md
        └── protocol-doc-template.md
```

## 单页推荐字段

每个厂商或协议页建议至少覆盖以下信息：

- 官方主页
- 官方文档入口
- API 基础地址
- 鉴权方式
- 模型命名规则
- Chat / Responses / Messages 接口
- Embeddings / Rerank / Batch / Files 能力
- 函数调用 / 工具调用格式
- 流式返回格式
- 多模态能力
- 错误码与限流说明
- SDK 与示例链接
- 变更日志或版本说明
- 与其他协议的兼容关系

## 维护原则

- 只引用官方文档、官方 SDK、官方博客、官方 Changelog。
- 每一条关键信息尽量附原始链接。
- 不大段复制官方内容，优先做结构化摘要和差异说明。
- 对不确定或待验证的内容明确标注状态。
- 新增条目前，优先复用 `docs/templates` 下的模板。

## 快速开始

1. 先看 [docs/INDEX.md](docs/INDEX.md)。
2. 按厂商查询时进入 `docs/vendors/`。
3. 按协议查询时进入 `docs/protocols/`。
4. 新增资料时先看 [docs/MAINTENANCE.md](docs/MAINTENANCE.md)。
5. 复制对应模板并补齐官方链接与摘要。

## 在线查看

这个项目已经适配 GitHub Pages 文档站，推荐后续直接通过网页访问。

- 仓库地址：<https://github.com/zwcblog/llmProtocolHub>
- 预期站点地址：<https://zwcblog.github.io/llmProtocolHub/>

如果 GitHub Pages 尚未生效，请在仓库设置里确认：

- `Settings` → `Pages`
- Source 使用 **GitHub Actions**

站点构建配置文件：

- `mkdocs.yml`
- `.github/workflows/deploy-docs.yml`
- `requirements.txt`

## 当前状态

当前仓库已完成第一版文档骨架，并已补齐 GitHub Pages 文档站所需配置，适合作为后续持续填充官方资料的基础结构。
