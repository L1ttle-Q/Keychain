# Keychain

Python 交互式本地账号记录练习，使用 C++ 辅助程序对文件内容做自定义可逆变换。提供终端显示版和可选剪贴板版。

**当前实现不适合保存真实密码。** `Lock.cpp` 使用自定义伪随机数和 XOR，恢复所需信息也保存在本地，没有主密码或经过审计的加密方案；界面还会显示账号和密码。请使用虚构数据体验。

## 环境与启动

需要 Git、Python 3 和可运行的 `g++`。终端版只使用 Python 标准库。

Windows PowerShell，从仓库根目录执行：

```powershell
git clone https://github.com/L1ttle-Q/Keychain.git
cd Keychain
g++ -std=c++11 Lock.cpp -o Lock.exe
python main.py
```

脚本启动时会尝试自动编译缺失的 `Lock.exe`，但不会可靠检查编译结果，因此建议先执行上述编译命令。必须在仓库目录启动：辅助程序与数据路径都基于**当前工作目录**。

Linux/macOS 的现有脚本同样写死辅助程序名 `Lock.exe`；使用 `g++ -std=c++11 Lock.cpp -o Lock.exe` 后再 `python3 main.py`。本轮仅实测 Windows；不同平台的文本模式与非 ASCII 数据兼容性未保证。

## 操作流程

首次启动提示无法读取已有记录是正常的：此时尚未生成有效的本地数据。按 Enter 后进入菜单：

| 输入 | 行为 |
| --- | --- |
| `i` | 依次输入网站、账号和密码；已有账号会询问是否覆盖 |
| `r` | 输入网站，查看该网站的记录 |
| `a` | 查看全部记录 |
| `q` | 正常退出，并调用辅助程序保存 |

可用 `example.test`、`sample`、`example-only` 作为一组演示数据。正常输入 `q` 退出后重新启动，用 `r` 查询 `example.test`，应能看到刚才的记录。新增内容先保存在内存中，直接关闭进程可能丢失。

## 剪贴板版本（可选）

此版本额外使用 Pyperclip 与 PyAutoGUI。可在独立虚拟环境中安装：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-clipboard.txt
.\.venv\Scripts\python.exe main_clipboard.py
```

查询后按编号选择网站或账号，再通过确认框复制账号、密码。需要可用的图形桌面与系统剪贴板；其他平台可能还需要对应的系统后端。本轮未验证图形确认框和剪贴板流程。

## 文件与限制

- `main.py`：终端版；`main_clipboard.py`：剪贴板版；`Lock.cpp`：本地存取辅助程序。
- `key.txt` 与 `sec.txt`：保存在工作目录中的一对数据文件，恢复记录需要二者；不要单独修改或丢失其中一个。
- `.gitignore` 排除生成的辅助程序、数据文件和虚拟环境；已有被 Git 跟踪的数据不受此规则自动保护。
- 数据损坏、非 ASCII 密码、命令行参数长度和异常退出的处理仍不完善。它不是系统钥匙串，也没有自动填充或云同步功能。
- 本次将清屏等待改为 Python `time.sleep` 和按系统选择的 `cls` / `clear`，避免 Windows 缺少 `sleep` / `clear` 命令。
- 辅助程序需要脚本提供正确参数；不要不带参数直接运行 `Lock.exe`。

## 验证记录与许可证

2026-10-26：Windows、MinGW-w64 GCC 8.1、Python 3.14 下，辅助程序构建、虚构记录插入和文件恢复检查通过。当前没有自动测试套件，剪贴板和完整异常输入流程未验收。

使用 [Apache License 2.0](LICENSE)。
