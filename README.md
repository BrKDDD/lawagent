# SpoonOS 法律公正助手

基于 LlamaIndex + DeepSeek 的智能法律助手，支持法律条文检索与区块链存证。

## 功能特性

- **法律检索**：基于 RAG（检索增强生成），在民法典等法律知识库中检索相关条文并回答问题
- **区块链存证**：对指定文本计算 SHA256 哈希并上链存证至 Sepolia 测试网
- **ReAct 智能体**：采用 ReAct 工作流，自动选择工具完成检索、回答与存证任务

## 项目结构

```
.
├── main.py              # 主程序入口，终端对话循环
├── build_knowledge.py   # 知识库构建脚本，从 PDF 构建向量索引
├── test_connection.py   # DeepSeek API 连接测试
├── requirements.txt     # 项目依赖
├── skills/              # 技能模块
│   ├── legal_skill.py   # 法律检索工具 search_laws
│   └── notary_skill.py  # 区块链存证工具 notarize_on_chain
├── data/                # 法律文档（PDF）
│   └── civil_code.pdf   # 民法典
└── storage/             # 向量索引持久化目录（运行 build_knowledge.py 后生成）
```

## 技术栈

- **LLM**：DeepSeek（通过 OpenAILike 兼容接口）
- **RAG 框架**：LlamaIndex
- **嵌入模型**：HuggingFace BGE-small-zh-v1.5
- **区块链**：Web3.py（Sepolia 测试网）

## 快速开始

### 1. 环境准备

- Python 3.10+
- 创建虚拟环境（推荐）：

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate  # Linux/macOS
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量

在项目根目录创建 `.env` 文件，配置以下变量：

```env
# DeepSeek API（或兼容 OpenAI 格式的 API）
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.deepseek.com
MODEL_NAME=deepseek-chat

# 区块链存证（可选，仅在使用存证功能时需要）
WEB3_RPC_URL=https://sepolia.infura.io/v3/your_project_id
WALLET_PRIVATE_KEY=your_private_key
```

> ⚠️ **安全提示**：切勿将 `.env` 提交到版本库，其中包含 API Key 和私钥等敏感信息。

### 4. 构建知识库

首次使用前，需要从 `data/` 目录下的 PDF 构建向量索引：

```bash
python build_knowledge.py
```

### 5. 测试连接（可选）

```bash
python test_connection.py
```

### 6. 启动助手

```bash
python main.py
```

启动后可在终端输入问题进行对话，输入 `q` 退出。

## 使用示例

```
您: 婚姻无效的情形有哪些？

助手: [先调用 search_laws 检索相关条文，再基于检索结果回答]

您: 请对「本合同于 2025 年 1 月 1 日签订」这段内容进行存证

助手: [调用 notarize_on_chain，返回上链交易哈希链接]
```

## 配置说明

| 环境变量 | 说明 | 是否必填 |
|---------|------|----------|
| OPENAI_API_KEY | DeepSeek 或兼容 API 的密钥 | 必填 |
| OPENAI_BASE_URL | API 地址，默认 `https://api.deepseek.com` | 可选 |
| MODEL_NAME | 模型名称，默认 `deepseek-chat` | 可选 |
| WEB3_RPC_URL | Sepolia 测试网 RPC 地址 | 存证时必填 |
| WALLET_PRIVATE_KEY | 用于发起存证交易的钱包私钥 | 存证时必填 |

## 扩展知识库

1. 将新的法律 PDF 放入 `data/` 目录
2. 重新运行 `python build_knowledge.py` 重建索引

## License

请根据项目实际情况添加开源协议。
