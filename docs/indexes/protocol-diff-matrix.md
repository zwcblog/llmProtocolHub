# 主流厂商模型协议差异对比（参数 / 返回值 / 请求头 / 流式）

> 目的：给接入方提供一张**协议层面对比表**，帮助快速理解不同厂商在请求头、请求结构、返回结构、流式事件、工具调用、多模态输入等方面的差异。
>
> 范围：本页聚焦**文本 / 对话主协议**，优先覆盖最常见的接口族：
>
> - OpenAI Chat Completions / Responses
> - Anthropic Messages
> - Google Gemini GenerateContent / streamGenerateContent
> - xAI（Grok API，通常采用 OpenAI-compatible 风格）
> - 兼容层厂商（DeepSeek / 阿里云百炼 / 百度千帆 / 腾讯混元 / 火山引擎 / 智谱等）
>
> 注意：
>
> 1. 本页是**协议差异导航与归纳**，不是官方文档替代品。
> 2. 不同平台版本演进非常快，字段与能力细节请始终以各自官方文档为准。
> 3. 很多国内平台同时提供“自有协议 + OpenAI Compatible 接口”，接入前要先确认你使用的是哪一层。

---

## 一、先看结论

如果只抓最关键的协议差异，可以先记这几条：

1. **OpenAI / OpenAI-compatible** 最像“行业事实标准”  
   - `Authorization: Bearer ...`  
   - JSON body 里带 `model`、`messages`、`stream`  
   - 返回 `choices[]` / SSE `data:` 事件  

2. **Anthropic Messages** 明显不是 OpenAI 同构  
   - 关键请求头多一个 `anthropic-version`  
   - 输入通常是 `messages` + 可选 `system`  
   - 返回结构不是 `choices[]`，而是 `content[]` 语义  
   - 流式事件类型更细，事件语义更明确  

3. **Google Gemini** 更像“内容生成协议”而不是 chat completions clone  
   - 常见鉴权是 query `?key=` 或特定 header  
   - 主体结构常见 `contents[]`、`parts[]`、`generationConfig`、`tools`  
   - 返回常见 `candidates[]`  
   - 多模态与 function calling 结构和 OpenAI 差异明显  

4. **xAI / DeepSeek / 国内兼容层厂商** 往往优先支持 OpenAI-compatible 入口  
   - 接入成本低  
   - 但流式细节、工具调用、结构化输出、额外 header/endpoint 可能并不完全等价  

5. **真正难兼容的不是字段名，而是语义**  
   尤其体现在：
   - tool calling 回填方式
   - stream 事件颗粒度
   - usage 何时返回
   - 多模态输入结构
   - system prompt 放置位置
   - structured output / schema 约束方式

---

## 二、主协议族对比总表

| 维度 | OpenAI Chat / Responses | Anthropic Messages | Google Gemini GenerateContent | xAI / Grok API | OpenAI-compatible 厂商层 |
|---|---|---|---|---|---|
| 主入口风格 | Chat Completions / Responses | Messages API | GenerateContent / streamGenerateContent | 多数场景接近 OpenAI 风格 | 通常宣称兼容 OpenAI |
| 常见路径 | `/v1/chat/completions`、`/v1/responses` | `/v1/messages` | `/v1beta/models/{model}:generateContent` | 通常为 `/v1/chat/completions` 等 | 多为 `/v1/chat/completions` |
| 认证头 | `Authorization: Bearer <api_key>` | `x-api-key: <api_key>` + `anthropic-version` | 常见为 `?key=` 或 `x-goog-api-key` | 多数为 `Authorization: Bearer` | 多数为 `Authorization: Bearer` |
| 模型字段 | `model` | `model` | 路径模型名或 body 内模型上下文 | 多数为 `model` | 多数为 `model` |
| 输入主字段 | `messages` 或 `input` | `messages` + `system` | `contents[]` | 多数为 `messages` | 多数为 `messages` |
| system 提示 | 常放在 `messages[role=system]`；Responses 也可做更丰富输入 | 通常独立 `system` 字段/语义 | 常通过 `systemInstruction` 或内容结构表达 | 多数随 OpenAI 风格 | 通常兼容 OpenAI `system` message |
| 返回主字段 | `choices[]` 或 Responses 事件对象 | `content[]` + stop reason / usage | `candidates[]` | 多数接近 `choices[]` | 多数接近 `choices[]` |
| usage 字段 | 常见 `usage` | 常见 `usage`，位置和时机不同 | 常见 token 统计但结构不完全一致 | 大多兼容 OpenAI | 可能兼容，也可能简化/缺失 |
| 工具调用 | function / tool calls | tool use / tool result | tools / function declarations | 若兼容 OpenAI，则多为 tool calls | 常见兼容 OpenAI，但语义可能不完全一致 |
| 流式 | SSE，`data:` 事件，通常最终 `[DONE]` | SSE，事件类型更细，如 message start/delta/stop | 流式接口独立，返回 chunk/candidates | 多数兼容 OpenAI SSE | 多宣称兼容，但 done/usage/tool delta 可能不同 |
| 多模态输入 | 逐步统一，但不同 API family 差异存在 | content blocks 结构明确 | `parts[]` 多模态能力较自然 | 视具体 API 而定 | 常常只兼容文本子集 |
| 结构化输出 | OpenAI Responses / JSON schema 能力相对成熟 | 有结构化约束能力，但表达方式不同 | 依赖 Gemini 工具/模式与 schema 能力 | 视平台而定 | 常见仅部分兼容 |

---

## 三、请求头差异对比

### 3.1 典型请求头总览

| 厂商 / 协议 | 必要认证头 | 常见版本头 / 特殊头 | 备注 |
|---|---|---|---|
| OpenAI | `Authorization: Bearer <key>` | `OpenAI-Beta`（部分新能力可能涉及） | 最典型的 Bearer 模式 |
| Anthropic Messages | `x-api-key: <key>` | `anthropic-version: <date>`，某些 beta 能力可能还需 beta header | 版本头基本是协议关键组成 |
| Google Gemini | `x-goog-api-key: <key>` 或 URL query `key=<key>` | 某些 Google 平台场景还会带项目/区域语义 | REST 形态与 OpenAI 不同 |
| xAI | 多数为 `Authorization: Bearer <key>` | 取决于具体 API family | 常见对外风格接近 OpenAI |
| OpenAI-compatible 厂商 | 多数为 `Authorization: Bearer <key>` | 可能额外要求厂商自定义 header | “兼容”通常先从 header 开始对齐 |

### 3.2 头部层面最值得注意的差异

1. **Anthropic 的 `anthropic-version` 不是装饰字段**  
   很多接入失败不是 body 问题，而是没带版本头。

2. **Google Gemini 常见 query key 模式**  
   对很多通用网关来说，这意味着签名、缓存、日志脱敏处理都和 Bearer 头不完全一样。

3. **兼容平台可能表面兼容 Bearer，实际还有厂商私有 header 要求**  
   比如组织 ID、区域、路由策略、beta 功能、推理地域等。

---

## 四、请求体主结构差异

### 4.1 文本对话请求结构对比

| 维度 | OpenAI Chat Completions | OpenAI Responses | Anthropic Messages | Google Gemini | OpenAI-compatible |
|---|---|---|---|---|---|
| 顶层输入核心 | `messages[]` | `input` | `messages[]` | `contents[]` | 多数 `messages[]` |
| 消息角色 | `system/user/assistant/tool` | 更偏统一输入事件/内容结构 | `user/assistant` + 独立 system 语义 | role + parts | 通常跟 OpenAI 对齐 |
| 文本内容表达 | message.content 可是字符串/结构块 | 更丰富的输入项 | content blocks | `parts[]` | 多为字符串或 OpenAI 风格数组 |
| 生成参数 | `temperature`、`top_p`、`max_tokens` 等 | `max_output_tokens` 等 API family 差异 | `max_tokens`、sampling 参数 | `generationConfig` 中配置 | 常宣称兼容 OpenAI 参数 |
| 工具定义 | `tools[]` | `tools[]` | tools 定义结构不同 | functionDeclarations / tools | 可能兼容 OpenAI tools |
| 流式开关 | `stream` | `stream` 或流式 endpoint 语义 | `stream: true` | 独立 stream 接口更常见 | 多数兼容 `stream` |

### 4.2 system prompt 的放置方式差异

| 协议 | 常见方式 | 兼容风险 |
|---|---|---|
| OpenAI Chat | `messages` 里的 `role=system` | 最容易被兼容层支持 |
| OpenAI Responses | 仍可表达 system 语义，但输入模型更灵活 | 转换到兼容层时可能丢语义 |
| Anthropic | 常独立 `system` 语义，而不是普通 message 完全等价 | 简单映射到 OpenAI 容易失真 |
| Gemini | 常通过 `systemInstruction` / 内容结构表达 | 和 messages 模型差别较大 |

### 4.3 参数层面最常见的不一致

| 参数主题 | 差异点 |
|---|---|
| 最大输出 token | 字段名可能是 `max_tokens`、`max_output_tokens` 或在配置对象中 |
| 随机性参数 | `temperature`、`top_p`、`top_k` 并非各家都同名同义 |
| 停止词 | `stop`、`stop_sequences` 等命名不一致 |
| 候选数 | `n` 并非每家都支持，或仅部分模型支持 |
| 用户标识 | `user`、`metadata`、安全审计标识等表达方式不同 |
| service tier / store / safety / geo | 有些是厂商私有参数，不应假设跨平台可移植 |

---

## 五、返回值结构差异

### 5.1 非流式返回主结构对比

| 维度 | OpenAI Chat | OpenAI Responses | Anthropic Messages | Google Gemini | OpenAI-compatible |
|---|---|---|---|---|---|
| 主要结果容器 | `choices[]` | response object / output items | `content[]` | `candidates[]` | 多数 `choices[]` |
| 文本提取位置 | `choices[0].message.content` | 需从 output item 中提取 | `content[]` 的 text blocks | `candidates[0].content.parts[]` | 多数与 OpenAI 类似 |
| finish reason | `finish_reason` | 有独立完成语义 | `stop_reason` / stop sequence 语义 | `finishReason` | 多数尝试兼容 OpenAI |
| usage | `usage.prompt_tokens` 等 | usage 结构更细 | usage 位置和字段不同 | token usage 结构不同 | 可能有，也可能不完整 |
| tool call 返回 | assistant message 中 tool calls | output item 里工具相关对象 | tool_use blocks | candidates/parts 中工具语义 | 通常尝试贴近 OpenAI |

### 5.2 返回结构上最容易踩坑的地方

1. **OpenAI 的 `choices[]` 不能当成行业统一结构**  
   Anthropic 与 Gemini 都不是这个主结构。

2. **文本不一定总是一个字符串字段**  
   可能是：
   - content blocks
   - parts[]
   - output item list
   - tool use + text 混合

3. **usage 并不一定总在最终根对象里稳定返回**  
   流式场景尤甚。

---

## 六、流式协议差异

### 6.1 流式总体差异表

| 维度 | OpenAI SSE | Anthropic SSE | Gemini 流式 | OpenAI-compatible |
|---|---|---|---|---|
| 传输方式 | SSE 为主 | SSE 为主 | 常有独立 stream endpoint | 多数宣称 SSE 兼容 |
| 数据载体 | `data: {...}` | `event:` + `data:` 更强调事件类型 | 返回 chunk / candidates 语义 | 大多模仿 OpenAI |
| 结束标识 | 常见 `[DONE]` | 通常通过 stop 事件语义 | 依赖流结束或特定完成语义 | 可能兼容 `[DONE]` |
| usage 返回时机 | 有时仅最后返回 | 事件粒度更细 | 依赖实现 | 经常不完全一致 |
| tool delta | 支持但不同 API family 有差异 | 事件拆分更细 | function call delta 结构不同 | 常见兼容不完整 |

### 6.2 流式兼容最难的不是 `stream=true`

真正困难的是：

- 是否有明确 `event` 类型
- 是否有 final done token
- usage 在中途还是结尾返回
- tool call 参数是增量拼接还是整块返回
- 错误是通过断流还是 error event 表达
- 是否允许中间 heartbeat / ping

### 6.3 对网关实现的建议

如果你要做统一 Gateway，不要直接把各家流式原样透传给前端。更合理的是先抽象统一事件模型，例如：

- `delta`
- `tool_call_delta`
- `usage`
- `error`
- `done`

这样比假设所有上游都长得像 OpenAI SSE 稳得多。

---

## 七、工具调用（Tool Calling / Function Calling）差异

### 7.1 主差异对比

| 维度 | OpenAI | Anthropic | Gemini | OpenAI-compatible |
|---|---|---|---|---|
| 工具定义字段 | `tools` | tools（结构不同） | `tools` / `functionDeclarations` | 多数兼容 `tools` |
| 触发结果位置 | assistant message / output item | `tool_use` block | candidate/part/function call 结构 | 多数贴近 OpenAI |
| 工具结果回填 | tool message / structured input | `tool_result` block | function response part | 常常只兼容最简单文本回填 |
| 流式工具调用 | 支持增量，但格式细节复杂 | 增量事件粒度明确 | 增量结构不同 | 很多兼容层只做部分支持 |

### 7.2 为什么工具调用最容易“不兼容”

因为它不仅是字段映射，还涉及：

1. 工具声明 schema 怎么表达  
2. 模型调用工具时返回什么中间对象  
3. 工具执行结果如何回填  
4. 多轮调用如何持续  
5. 流式场景如何增量拼 tool arguments  

也就是说，**tool calling 的差异往往是“协议语义差异”，不是简单 JSON rename。**

---

## 八、多模态消息结构差异

### 8.1 多模态输入的典型差异

| 协议 | 常见表达方式 | 特点 |
|---|---|---|
| OpenAI | message content blocks（text / image 等） | 在新旧 API family 间仍有差异 |
| Anthropic | content blocks | 结构较清晰，文本/图片等块式表达 |
| Gemini | `parts[]` | 天然偏内容块结构，多模态相对自然 |
| OpenAI-compatible | 往往先兼容文本，再逐步补图片/音频 | 兼容层经常只覆盖部分多模态能力 |

### 8.2 接入方最常见误区

误区是把“文本兼容”误认为“多模态兼容”。

实际上很多平台：

- 文本对话兼容 OpenAI
- 图片输入字段只部分兼容
- 视频/音频输入完全是私有协议

所以协议兼容评估必须把多模态单独拿出来看。

---

## 九、国内 / 兼容层厂商怎么理解

下面这些厂商，很多场景都优先提供 OpenAI-compatible 接口，降低接入门槛：

- DeepSeek
- 阿里云百炼
- 百度千帆
- 腾讯混元
- 火山引擎
- 智谱 AI（部分接口）
- xAI（很多接入场景也会被当作 OpenAI-compatible 来理解）

### 9.1 它们的共同点

- 通常支持 `Authorization: Bearer`
- 通常支持 `/v1/chat/completions`
- 通常支持 `model` + `messages`
- 通常支持 `stream=true`

### 9.2 它们的真实差异常出现在

- 模型命名与 model mapping
- 工具调用细节
- 流式 done 语义
- usage 返回稳定性
- 私有参数（安全、地域、服务等级等）
- 多模态与结构化输出能力
- embedding / image / audio 是否真的同构

### 9.3 最实用的接入建议

对于兼容层厂商，可以分三层判断：

1. **能不能跑起来**：看 OpenAI-compatible 文本接口  
2. **能不能稳定生产用**：看 stream / usage / error / timeout / tool calling  
3. **能不能无损迁移**：看多模态、structured output、schema、私有 header 与参数

---

## 十、字段级协议差异矩阵

本节把常见接入字段拆成更细粒度的对照表，便于：

- 做多厂商网关抽象
- 做 OpenAI-compatible 兼容评估
- 做 SDK / Adapter 设计
- 做请求转换和返回归一化

### 10.1 顶层请求字段矩阵

| 字段主题 | OpenAI Chat Completions | OpenAI Responses | Anthropic Messages | Google Gemini | OpenAI-compatible 厂商 |
|---|---|---|---|---|---|
| 模型标识 | `model` | `model` | `model` | 常在 URL path 中体现模型，或以平台风格表达 | 多数 `model` |
| 主输入字段 | `messages` | `input` | `messages` | `contents` | 多数 `messages` |
| system 指令 | `messages[role=system]` | 可通过 input/system 语义表达 | 常为独立 `system` 语义 | 常为 `systemInstruction` 或内容块表达 | 通常兼容 OpenAI `system` |
| 流式开关 | `stream` | `stream` / 对应流式响应 | `stream` | 常通过 stream 方法/endpoint | 多数兼容 `stream` |
| 候选数量 | `n` | 通常不完全同构 | 通常不是 OpenAI 风格的 `n` | 常以 candidate 语义建模 | 有些兼容，有些不支持 |
| 最大输出 | `max_tokens` | `max_output_tokens` 等 | `max_tokens` | 多在 `generationConfig.maxOutputTokens` | 多尝试兼容 OpenAI |
| 随机性控制 | `temperature`, `top_p` | 类似但不完全同构 | `temperature`, `top_p/top_k` 风格差异 | 常在 `generationConfig` 中 | 多数兼容常用子集 |
| 停止词 | `stop` | 相关停止控制但接口语义不同 | `stop_sequences` | 通常有停止生成配置但不完全同名 | 常常仅兼容 `stop` 子集 |
| 元数据 | `user`, `metadata` 等 | 有更丰富元数据空间 | metadata / 其他审计字段 | 平台风格元数据 | 经常存在私有扩展 |
| 工具定义 | `tools` | `tools` | tools（结构不同） | `tools` / `functionDeclarations` | 多数尝试兼容 OpenAI tools |
| 结构化输出 | JSON schema / response format 等 | 原生能力更强 | 有自己的受控输出方式 | 依赖 schema / tool 模式 | 常常只兼容最简单形式 |

### 10.2 消息结构字段矩阵

| 维度 | OpenAI Chat | OpenAI Responses | Anthropic Messages | Gemini | OpenAI-compatible |
|---|---|---|---|---|---|
| 角色集合 | `system/user/assistant/tool` | 更偏事件/输入项语义 | 主要是 `user/assistant`，system 单独处理 | role + parts | 多数跟 OpenAI 对齐 |
| 文本内容 | `content` 可为字符串或结构块 | input item / content item | block-based content | `parts[].text` | 多数支持字符串，部分支持内容块 |
| 图片输入 | 常通过内容块表达 | 支持但结构与 chat 不完全同构 | content blocks | `parts` 中天然支持 | 兼容层常常不完整 |
| 工具回填消息 | `role=tool` 或相关输入项 | 更偏 output/input item 模型 | `tool_result` block | function response part | 常见只兼容简单文本回填 |
| reasoning / 思维链相关 | 视 API family 与模型而定 | 更容易承载复杂 output item | 有自己的思维/内容块语义 | 平台特定 | 兼容层经常不暴露 |

### 10.3 返回字段矩阵

| 字段主题 | OpenAI Chat | OpenAI Responses | Anthropic Messages | Gemini | OpenAI-compatible |
|---|---|---|---|---|---|
| 结果容器 | `choices[]` | `output` / response object | `content[]` | `candidates[]` | 多数 `choices[]` |
| 文本主路径 | `choices[0].message.content` | 需遍历 output items | `content[]` text block | `candidates[0].content.parts[]` | 多数兼容 OpenAI |
| 完成原因 | `finish_reason` | completion/response status 语义 | `stop_reason` | `finishReason` | 多数尝试映射成 `finish_reason` |
| usage | `usage.prompt_tokens` 等 | usage 可能更细 | usage 结构与字段名不同 | token 统计结构不同 | 可能缺失或语义不稳 |
| 工具调用结果 | tool calls 在 message 或 item 中 | output item 中更自然 | `tool_use` block | candidate / part 中 | 常尝试映射到 OpenAI tool call |
| 安全 / 过滤信息 | 视 API family | 可更细化 | 平台特有 | 常见 safety ratings | 兼容层通常弱化或忽略 |

### 10.4 流式事件字段矩阵

| 维度 | OpenAI SSE | Anthropic SSE | Gemini 流式 | OpenAI-compatible |
|---|---|---|---|---|
| 事件包装 | 常以 `data: {json}` 为主 | 常见 `event:` + `data:` | 依赖平台流式返回结构 | 多数模仿 OpenAI |
| 文本增量字段 | delta / output text delta | message/content delta 事件 | candidate / part delta | 大多兼容 OpenAI delta |
| 工具增量字段 | tool call delta | tool use delta 事件更细 | function call delta | 常见不完整 |
| usage 事件 | 常在末尾或最终对象 | 事件类型更细 | 平台依赖 | 经常不稳定 |
| done 信号 | `[DONE]` 常见 | stop 事件语义 | 流结束或完成字段 | 可能兼容 `[DONE]` |
| 错误表达 | SSE 中断或错误对象 | 事件化更明确 | 平台依赖 | 不完全一致 |

### 10.5 请求头字段矩阵

| 请求头 / 鉴权方式 | OpenAI | Anthropic | Gemini | xAI | OpenAI-compatible |
|---|---|---|---|---|---|
| `Authorization: Bearer` | 是 | 否 | 一般不是主模式 | 通常是 | 通常是 |
| `x-api-key` | 否 | 是 | 不是典型主模式 | 视实现 | 少数平台可能支持 |
| `anthropic-version` | 否 | 是 | 否 | 否 | 否 |
| `x-goog-api-key` | 否 | 否 | 常见 | 否 | 否 |
| URL query `key=` | 否 | 否 | 常见 | 否 | 少见 |
| Beta / 特性头 | 部分场景 | 常见 beta header 场景 | 平台特有 | 平台特有 | 厂商私有 |

### 10.6 兼容迁移风险矩阵

| 能力主题 | 从 OpenAI 迁移到 Anthropic | 从 OpenAI 迁移到 Gemini | 从 OpenAI 迁移到兼容层厂商 |
|---|---|---|---|
| 文本对话 | 中等风险：messages 近似，但返回结构不同 | 中高风险：contents/parts 模型不同 | 低到中风险：通常先能跑 |
| system prompt | 中风险：独立 system 语义 | 中高风险：systemInstruction 表达不同 | 低风险：多数兼容 |
| tool calling | 高风险：语义与回填方式差异明显 | 高风险：声明和响应结构差异明显 | 中风险：常见只兼容子集 |
| streaming | 中高风险：事件模型不同 | 高风险：流式结构差异大 | 中风险：done/usage/tool delta 经常不稳 |
| structured output | 中风险：表达方式不同 | 中高风险：依赖平台 schema 能力 | 中高风险：很多平台只做部分兼容 |
| multimodal | 中风险 | 高风险 | 中高风险 |

### 10.7 字段级矩阵的使用建议

如果你要做一层统一抽象，最稳的方式不是“假装所有厂商都等于 OpenAI”，而是：

1. **内部定义统一请求模型**
   - `model`
   - `messages / contents / input` 统一抽象
   - `systemInstruction`
   - `tools`
   - `generationConfig`

2. **内部定义统一响应事件模型**
   - `textDelta`
   - `toolCallDelta`
   - `usage`
   - `finishReason`
   - `error`

3. **在 Adapter 层处理厂商差异**
   - header 映射
   - path / query 组装
   - 请求体转换
   - 返回值抽取
   - 流式事件归一化

---

## 十一、面向网关实现的协议抽象建议

如果你要建设统一 AI Gateway，建议按以下维度建模，而不是直接绑定某一家协议：

### 10.1 请求头抽象

- auth header/query
- version header
- beta header
- vendor-specific headers

### 10.2 统一请求模型抽象

- model
- messages / contents / input
- system instruction
- tools
- generation params
- multimodal parts
- stream flag

### 10.3 统一返回模型抽象

- text delta / full text
- tool calls
- usage
- finish reason
- vendor metadata

### 10.4 统一流式事件抽象

- `delta`
- `tool_call_delta`
- `usage`
- `error`
- `done`

这比直接拿 OpenAI JSON 作为系统内部模型更稳。

---

## 十一、如何使用这张表

### 如果你是“直接接模型 API”的开发者
优先看：

1. 请求头差异  
2. 请求体主结构  
3. 返回值主结构  
4. 流式 done / usage 语义  

### 如果你是“做网关/兼容层”的开发者
优先看：

1. system prompt 放置方式  
2. tool calling 回填模型  
3. 流式事件抽象  
4. 多模态输入结构  
5. 私有参数透传策略  

### 如果你是“做迁移”的开发者
优先确认：

1. 只是文本兼容，还是工具/流式也兼容  
2. 是 header/query 差异，还是 body 语义差异  
3. 是字段重命名问题，还是交互轮次模型不一样  

---

## 十二、相关阅读

### 厂商入口

- [OpenAI](../vendors/openai/README.md)
- [Anthropic](../vendors/anthropic/README.md)
- [Google Gemini](../vendors/google-gemini/README.md)
- [xAI](../vendors/xai/README.md)
- [DeepSeek](../vendors/deepseek/README.md)
- [智谱 AI](../vendors/zhipu/README.md)
- [阿里云百炼](../vendors/alibaba-bailian/README.md)
- [百度千帆](../vendors/baidu-qianfan/README.md)
- [腾讯混元](../vendors/tencent-hunyuan/README.md)
- [火山引擎](../vendors/volcengine/README.md)

### 协议专题

- [OpenAI Compatible API](../protocols/openai-compatible/README.md)
- [流式输出格式](../protocols/streaming/README.md)
- [工具调用约定](../protocols/tool-calling/README.md)
- [多模态消息结构](../protocols/multimodal/README.md)

---

## 十三、最后的判断原则

> 不同厂商“看起来很像”，往往只是因为它们都在向同一个事实标准靠近。  
> 真正决定接入成本的，不是顶层 URL 或几个公共参数，而是：
>
> - 请求头要求
> - 消息结构
> - 工具调用语义
> - 流式事件模型
> - usage / finish / error 的返回方式

如果你只想记一句话：

> **OpenAI-compatible 解决的是“先接入”，不是“完全等价”。**
