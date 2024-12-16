import tkinter as tk
from tkinter import scrolledtext
import subprocess
import shlex

def paste_command():
  """将剪贴板内容粘贴到文本窗口"""
  try:
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, root.clipboard_get())
  except tk.TclError:
    text_area.insert(tk.END, "剪切板为空或无法访问")

def run_command():
  """读取文本窗口中的 curl 命令，并执行"""
  command = text_area.get("1.0", tk.END).strip()
  if not command:
    output_area.insert(tk.END, "请输入 curl 命令\n")
    return
  # 替换续行符
  command = command.replace("\\\n", "")
  command = command.replace("\\\r\n","")
  # 使用 shlex.split 分割命令，处理空格和引号
  try:
    command_list = shlex.split(command)
    process = subprocess.Popen(
        command_list,
        shell=False, # 禁止 shell=True, 防止安全漏洞
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True, # 使用文本模式
        encoding='utf-8' # 指定编码
    )
    output, error = process.communicate() # 获取输出和错误信息

    output_area.insert(tk.END, output)  # 显示输出
    if error:
        output_area.insert(tk.END, f"Error:\n{error}\n")  # 显示错误信息
    else:
         output_area.insert(tk.END, "Command execution finished.\n")
  except FileNotFoundError:
       output_area.insert(tk.END, "Error: curl 命令没有找到，请确保 curl 命令在你的系统环境变量中.\n")
  except Exception as e:
        output_area.insert(tk.END, f"执行命令时发生错误:\n{e}\n")

# 创建主窗口
root = tk.Tk()
root.title("curl 命令执行器")
root.geometry("800x600") # 设置初始窗口大小

# 创建文本输入框
text_area = scrolledtext.ScrolledText(root, height=15, width=100, wrap=tk.WORD)
text_area.pack(pady=10)

# 创建粘贴按钮
paste_button = tk.Button(root, text="粘贴命令", command=paste_command)
paste_button.pack(pady=5)

# 创建运行按钮
run_button = tk.Button(root, text="运行命令", command=run_command)
run_button.pack(pady=5)

# 创建输出显示区
output_area = scrolledtext.ScrolledText(root, height=15, width=100, wrap=tk.WORD, state='disabled')
output_area.pack(pady=10)

# 循环使用
root.mainloop()