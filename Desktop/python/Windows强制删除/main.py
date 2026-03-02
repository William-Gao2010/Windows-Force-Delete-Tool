import os
import shutil
import ctypes
import sys

def is_admin():
    """检查是否拥有管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def force_delete_folder(path):
    if not os.path.exists(path):
        print(f"❌ 路径不存在: {path}")
        return

    try:
        # shutil.rmtree 可以删除整个目录树
        shutil.rmtree(path)
        print(f"✅ 成功强制删除文件夹: {path}")
    except Exception as e:
        print(f"❌ 删除失败。原因: {e}")
        print("💡 提示：如果文件被其他程序占用，请先关闭相关程序。")

if __name__ == "__main__":
    if not is_admin():
        # 强制请求管理员权限，这对删除受保护的文件夹至关重要
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:
        print("="*40)
        print("      Python 文件夹强制删除工具")
        print("      作者: William-Gao2010")
        print("="*40)
        
        target = input("\n请输入或拖入要删除的文件夹路径: ").strip().strip('"')
        
        confirm = input(f"⚠️ 确定要永久删除 {target} 吗？(y/n): ")
        if confirm.lower() == 'y':
            force_delete_folder(target)
        else:
            print("操作已取消。")
        
        input("\n按回车键退出...")