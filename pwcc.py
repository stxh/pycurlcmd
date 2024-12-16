import tkinter as tk
from tkinter import scrolledtext, filedialog
import subprocess
import shlex
import re
import os
import configparser

config = configparser.ConfigParser()

config_file = 'curl.ini'
curl_path = 'curl'

# 检查配置文件是否存在
if os.path.exists(config_file):
    config.read(config_file)
  
    # 检查配置文件中是否存在 curl 配置
    if 'settings' in config and 'curl' in config['settings']:
        curl_path = config['settings']['curl']

else:
    with open(config_file, 'w') as configfile:
      config['settings'] = {'curl': curl_path}
      config.write(configfile)

def transform_string(input_str):
    # 定义正则表达式，匹配一对单引号中的内容
    pattern = re.compile(r"'([^']*)'", re.DOTALL) # 使用re.DOTALL可以匹配多行字符串
    
    # 替换匹配的内容
    def replace(match):
        inner_str = match.group(1)
        # 替换双引号为 \"
        inner_str = inner_str.replace('"', '\\"')
        # 返回新的字符串，单引号替换为双引号
        return f'"{inner_str}"'
    
    result = pattern.sub(replace, input_str)
    return result

def paste_command():
  """将剪贴板内容粘贴到文本窗口"""
  text_area.delete("1.0", tk.END)
  try:
    clip = root.clipboard_get().strip()
    if clip.find("curl") == 0:
      modified_string = re.sub(r'\\$', '^', clip, flags=re.MULTILINE)

      modified_string = transform_string(modified_string)

      text_area.insert(tk.END, modified_string)

      run_button.config(state=tk.NORMAL)
      copy_button.config(state=tk.NORMAL)
      
    else:
      text_area.insert(tk.END, f"剪切板内容不是 curl 命令\n===\n{clip}\n===\n请粘贴 curl 命令\n")
      
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

  output_area.delete("1.0", tk.END)
  output_area.insert(tk.END, f"Running command: {command}\n")

  curl_test = [curl_path, "--version"]
  try:
    process = subprocess.Popen(
        curl_test,
        shell=False, # 禁止 shell=True, 防止安全漏洞
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True, # 使用文本模式
        encoding='utf-8' # 指定编码
    )
    output, _error = process.communicate()
    # output_area.insert(tk.END, f"curl 命令版本信息:\n{output}\n")

  except FileNotFoundError:
    output_area.insert(tk.END, "Error: curl 命令没有找到，请确保 curl 命令在你的系统环境变量中.\n")

    # 打开文件对话框
    file_path = filedialog.askopenfilename(
      title="指定curl 命令文件", 
      filetypes=[("curl 命令文件", "curl.exe")],
      initialdir="C:\\Program Files (x86)\\curl"
    )

    # 打印选择的文件路径
    if os.path.exists(file_path): 
      curl_test[0] = file_path
      with open(config_file, 'w') as configfile:
        config['settings'] = {'curl': file_path}
        config.write(configfile)
    else: 
      output_area.insert(tk.END, f"执行命令时发生错误:\n{e}\n")
      run_button.config(state=tk.DISABLED)
      
  except Exception as e:
    output_area.insert(tk.END, f"执行命令时发生错误:\n{e}\n")

    # 使用 shlex.split 分割命令，处理空格和引号
  try:
    command_list = shlex.split(command)
    command_list[0] = curl_test[0]

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


def copy_command():
  """将文本窗口内容复制到剪贴板"""
  try:
    root.clipboard_put(text_area.get("1.0", tk.END).strip())
  except tk.TclError:
    output_area.insert(tk.END, "剪切板为空或无法访问")

####

root = tk.Tk()
root.title("Windows command line curl 多行命令执行器")
root.geometry("800x600")  # 设置初始窗口大小

# 创建文本输入框
text_area = scrolledtext.ScrolledText(root, height=15, width=120, wrap=tk.WORD)
text_area.pack(pady=10)

# 创建按钮框架
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# 创建粘贴按钮
paste_button = tk.Button(button_frame, text="粘贴并转换", command=paste_command)
paste_button.pack(side=tk.LEFT, padx=5)

# 创建运行按钮
run_button = tk.Button(button_frame, text="运行命令", command=run_command, state=tk.DISABLED)
run_button.pack(side=tk.LEFT, padx=5)

# 创建复制按钮
copy_button = tk.Button(button_frame, text="复制命令", command=copy_command, state=tk.DISABLED)
copy_button.pack(side=tk.LEFT, padx=5)

# 创建输出显示区
output_area = scrolledtext.ScrolledText(root, height=30, width=120, wrap=tk.WORD)
output_area.pack(pady=10)

# 循环使用
root.mainloop()