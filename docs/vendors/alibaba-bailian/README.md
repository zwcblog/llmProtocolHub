# 阿里云百炼

## 一句话判断

百炼并不是一个单纯的模型 API 文档入口，而是阿里云体系下的模型与 Agent 能力平台；理解它的关键，在于分清“百炼平台能力”与 `DashScope` 等 API 接入面的关系，而不是把它看成一个单层接口站点。

## 官方入口

- 官网 / 产品页：<https://www.aliyun.com/product/bailian>
- 百炼控制台：<https://bailian.console.aliyun.com/>
- 官方文档：<https://help.aliyun.com/zh/model-studio/>
- API Reference：<https://help.aliyun.com/zh/model-studio/developer-reference/>
- DashScope：<https://dashscope.aliyun.com/>
- SDK / 示例：以阿里云官方文档与仓库链接为准

## 接口形态

- 主平台形态：百炼更像平台与能力集合，不只是单一推理 API
- API 接入面：开发者常通过 DashScope 或相关 API 入口接入模型能力
- 工具调用：支持情况需以具体模型与平台能力文档为准
- 流式输出：支持情况以最新官方文档为准
- 多模态输入：平台支持多种模型能力，但应按模型与服务文档分别确认
- Agent 能力：百炼在 Agent 与工作流方向具备平台化特征

## 平台边界

- 产品线划分：最容易混淆的是百炼平台、DashScope 接口、模型市场与阿里云其他 AI 产品之间的边界
- 官方推荐入口：先从产品概览与开发者文档总览进入，再按具体接入面定位 API 文档
- 常见误区：把百炼理解成“一个 endpoint”；实际上，它更接近平台入口，而 API 只是其中一层
- 迁移注意事项：从 OpenAI 风格平台迁移时，要重点确认认证方式、endpoint 组织、模型命名、区域与阿里云账号体系约束

## 能力范围

- Text / Chat：支持
- Embeddings / 多模态：支持情况取决于模型与服务类别
- 工具调用 / Agent：具备平台化能力，需查看对应专题文档
- 流式输出：支持情况以具体 API 文档为准
- 企业化能力：与阿里云控制台、权限、区域、配额等体系紧密相关

## 备注

理解百炼时，先建立“平台层”和“接口层”两层视角；很多接入问题并不是字段问题，而是站错了入口。
