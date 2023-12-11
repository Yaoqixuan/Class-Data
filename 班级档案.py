import tkinter as tk
import tkinter.messagebox

# 学生类
class Student:
	def __init__(self):
		self.name = "" # 姓名
		self.number = 0 # 学号

# 窗口类
class Window(tk.Tk):
	width, height = 400, 400 # 大小
	number = 0 # 人数
	students = []
	# 全局控件
	entry, label, button = None, None, None
	# 初始化
	def __init__(self):
		super().__init__()
		self.title("班级档案") # 设置窗口标题
		self.geometry("%sx%s" % (self.width, self.height)) # 设置窗口长宽
		self.create_class()

	# 创建班级
	def create_class(self):
		# "创建班级"文字
		self.label = tk.Label(self, text="创建班级", font=("宋体", 20))
		self.label.pack(expand=True)
		# 人数输入框
		self.entry = tk.Entry(self, font=("宋体", 15), fg="black")
		self.entry.insert(0, "输入人数...(<100)")
		self.entry.pack(expand=True)
		# 确定按钮
		self.button = tk.Button(self, text="确定", font=("宋体", 15), command=self.home_page)
		self.button.pack(expand=True)

	# 主页
	def home_page(self):
		self.number = self.entry.get() # 获取输入框内容
		# 判断输入内容是否为数字
		if (self.number.isdigit()):
			self.number = int(self.number)
			if (self.number >= 100):
				tk.messagebox.showerror("错误", "请输入小于100的数字！") # 弹窗
			else:
				# 清空窗口
				self.label.pack_forget()
				self.entry.pack_forget()
				self.button.pack_forget()
				# "班级主页"文字
				self.label = tk.Label(self, text="班级主页", font=("宋体", 20))
				self.label.pack()
				# # 滚动栏
				# self.bar = tk.Scrollbar(self)
				# self.bar.pack(side="right", fill="y")
				# 创建学生信息
				for i in range(self.number):
					# 创建一个学生
					self.student = Student()
					self.student.name = ""
					self.student.number = i + 1
					self.students.append(self.student) # 加入列表
				# 显示学生信息
				self.list = tk.Listbox(self, height=40)
				self.list.pack(fill="both")
				for self.student in self.students:
					self.list.insert("end", str(self.student.number)+self.student.name)
				# self.bar.config(command=self.list.yview) # 绑定滚动栏与列表
				# self.bar.set(0, 1)

		else:
			tk.messagebox.showerror("错误", "请输入数字！") # 弹窗


# 运行
if __name__ == "__main__":
	win = Window()
	win.mainloop()