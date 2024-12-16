# pycurlcmd
To convert a multi-line curl command from Linux to Windows

## 用户界面

从提供的截图可以看到，这是一个 Windows 命令行界面，用于执行 curl 命令。界面包含以下主要元素:

1. **命令输入区域**: 用于输入 curl 命令。可以看到这里显示了一个多行的 curl 命令。
2. **功能按钮区域**: 包含了4个按钮 - "粘贴转换"、"运行命令"、"复制命令"和"清除"。这些按钮可以帮助用户执行相应的操作。

## 使用说明

1. **输入 curl 命令**: 用户可以在命令输入区域直接输入多行的 Linux 格式 curl 命令。
2. **转换命令格式**: 点击"粘贴转换"按钮，系统会自动将 Linux 格式的 curl 命令转换为 Windows 兼容格式。
3. **执行命令**: 点击"运行命令"按钮，系统会执行转换后的 curl 命令。
4. **复制命令**: 点击"复制命令"按钮，可以将转换后的 curl 命令复制到剪贴板。
5. **清除命令**: 点击"清除"按钮，可以清空命令输入区域。

总的来说，该工具提供了一个简单直观的界面,帮助用户轻松地在 Windows 环境下执行从其他来源获得的 curl 命令。通过自动转换命令格式,大大降低了在不同操作系统间迁移 curl 命令的难度。

要将网站上提供的多行 `curl` 命令从 Linux 转换为 Windows 格式，可以按照以下步骤进行。下面是一个示例和转换的详细说明。

### 示例 Linux `curl` 命令

假设您在网站上看到的 `curl` 命令如下：

```bash
curl -X POST \
  https://api.example.com/v1/resource \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}'
```

### 转换为 Windows `curl` 命令

您可以将其转换为 Windows 格式，如下所示：

```cmd
curl -X POST ^
  https://api.example.com/v1/resource ^
  -H "Content-Type: application/json" ^
  -d "{\"key\":\"value\"}"
```

### 转换步骤

1. **换行符**：在 Windows 中，使用 `^` 作为换行符。
2. **引号转义**：在 JSON 数据中，双引号需要使用 `\"` 进行转义。
3. **保持其他参数不变**：大部分参数在 Windows 和 Linux 中是相同的。

### 完整示例

```cmd
curl -X POST ^
  https://api.example.com/v1/resource ^
  -H "Content-Type: application/json" ^
  -d "{\"key\":\"value\"}"
```

### 其他注意事项

- 确保在 Windows 命令提示符中运行此命令。
- 如果使用 PowerShell，可能需要稍微调整引号的使用。

如果您有特定的 `curl` 命令需要转换，请提供，我可以为您进行更具体的转换。

pycurlcmd 使用说明书
概述
pycurlcmd 是一个工具，用于将多行的 Linux curl 命令转换为 Windows 格式。这对于在不同操作系统之间迁移命令非常有用，特别是当您需要在 Windows 环境中执行从网站或其他来源获得的 curl 命令时。

功能
将 Linux 风格的 curl 命令自动转换为 Windows 兼容格式。
处理多行命令和 JSON 数据的引号转义。
使用方法
输入格式
您需要提供一个多行的 Linux curl 命令，格式如下：

复制
curl -X <HTTP_METHOD> \
  <URL> \
  -H "<HEADER>" \
  -d '<DATA>'
输出格式
转换后的 Windows curl 命令将如下所示：

复制
curl -X <HTTP_METHOD> ^
  <URL> ^
  -H "<HEADER>" ^
  -d "<DATA>"
示例
输入示例
复制
curl -X POST \
  https://api.example.com/v1/resource \
  -H "Content-Type: application/json" \
  -d '{"key":"value"}'
输出示例
复制
curl -X POST ^
  https://api.example.com/v1/resource ^
  -H "Content-Type: application/json" ^
  -d "{\"key\":\"value\"}"
转换步骤
换行符替换：将每行末尾的 \ 替换为 Windows 的换行符 ^。
引号转义：在 JSON 数据中，双引号 " 需要使用 \" 进行转义。
保持其他参数不变：大部分参数在 Windows 和 Linux 中是相同的。
注意事项
确保在 Windows 命令提示符或 PowerShell 中运行转换后的命令。
如果您在 PowerShell 中使用，可能需要根据情况调整引号的使用。
结论
pycurlcmd 使得在不同操作系统之间迁移 curl 命令变得简单高效。只需输入 Linux 格式的命令，即可获得适用于 Windows 的版本。

