# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:39:17 2022

@author: asus
"""

import tkinter as tk
import tkinter.filedialog
import os
from PIL import Image,ImageTk 
#import subprocess
import time
import shutil



class Test():
    def __init__(self):
        self.newname=""
        self.window = tk.Tk()
        self.window.focus_force()    # 主窗口获得焦点
        self.window.title('AniName')   # 窗口标题
        self.window.geometry('1400x800')

        
        self.text1 = tk.StringVar()
        self.text1.set("未选择文件夹")
        
        self.text2 = tk.StringVar()
        self.text2.set("未选择文件夹")
        
        self.text3 = tk.StringVar()
        self.text3.set("另存为文件名：待定")
        
        self.text4 = tk.StringVar()
        self.text4.set("")
        
        self.text5 = tk.StringVar()
        self.text5.set("/")

        
        self.b1 = tk.Button(self.window, text="选择文件夹", font=('宋体','12'), command=self.func1)
        self.b1.place(x = 50, y = 50)
        
        self.l1 = tk.Label(self.window, textvariable = self.text1, font=('宋体','12'), width = 40)
        self.l1.place(x = 170, y = 68, anchor="w")
        
        self.b2 = tk.Button(self.window, text="另存文件夹", font=('宋体','12'), command=self.func2)
        self.b2.place(x = 600, y = 50)
        
        self.l2 = tk.Label(self.window, textvariable = self.text2, font=('宋体','12'), width = 40)
        self.l2.place(x = 720, y = 68, anchor="w")
        
        frame1 = tk.Frame(self.window, borderwidth=1, width=1000, height = 560, 
                      relief='ridge')
        frame1.place(x=50,y=100,anchor = 'nw')
        
        self.photo_label = tk.Label(frame1,  width=1000, height=560)
        self.photo_label.pack(padx = 0, pady = 0)
        
        self.mp4_label = tk.Label(self.window, textvariable = self.text4, font=('宋体','16'))
        self.mp4_label.pack(pady = 250)

        
        self.b3 = tk.Button(self.window, text="上一张图片", font=('宋体','12'), command=self.func3)
        self.b3.place(x = 1110, y = 150)

        self.b4 = tk.Button(self.window, text="下一张图片", font=('宋体','12'), command=self.func4)
        self.b4.place(x = 1110, y = 200)
        
        self.l2 = tk.Label(self.window, text="位置：", font=('宋体','12'))
        self.l2.place(x = 1100, y = 270, anchor="w")
        
        self.e1 = tk.Entry(self.window, font=('宋体','12'), width=15)
        self.e1.place(x = 1100, y = 300)
        
        self.l3 = tk.Label(self.window, text="其他：", font=('宋体','12'))
        self.l3.place(x = 1100, y = 350, anchor="w")
        
        self.e2 = tk.Entry(self.window, font=('宋体','12'), width=15)
        self.e2.place(x = 1100, y = 380)    
        
        self.b5 = tk.Button(self.window, text="珠颈斑鸠", font=('宋体','12'), width=10,command=self.func5)
        self.b5.place(x = 1050, y = 420)
        
        self.b6 = tk.Button(self.window, text="乌鸫", font=('宋体','12'), width=10, command=self.func6)
        self.b6.place(x = 1050, y = 480)   
        
        self.b7 = tk.Button(self.window, text="白头鹎", font=('宋体','12'), width=10, command=self.func7)
        self.b7.place(x = 1050, y = 540)    
        
        self.b8 = tk.Button(self.window, text="预览", font=('宋体','12'), width=10, command=self.func8)
        self.b8.place(x = 1110, y = 600)  
        
        self.b9 = tk.Button(self.window, text="重命名", font=('宋体','14'), width=15, height=3, command=self.func9)
        self.b9.place(x = 1070, y = 670)  
        
        self.l4 = tk.Label(self.window, textvariable = self.text3, font=('宋体','16'))
        self.l4.place(x = 100, y = 720, anchor="w")
        
        self.l5 = tk.Label(self.window, textvariable = self.text5, font=('宋体','16'))
        self.l5.place(x = 850, y = 720, anchor="w")
        
        self.b10 = tk.Button(self.window, text="远东山雀", font=('宋体','12'), width=10,command=self.func10)
        self.b10.place(x = 1200, y = 420)
        
        self.b11 = tk.Button(self.window, text="鹊鸲", font=('宋体','12'), width=10, command=self.func11)
        self.b11.place(x = 1200, y = 480)   
        
        self.b12 = tk.Button(self.window, text="黄鼬", font=('宋体','12'), width=10, command=self.func12)
        self.b12.place(x = 1200, y = 540)  

        self.b13 = tk.Button(self.window, text="生成excel", font=('宋体','12'), command=self.func13)
        self.b13.place(x = 1200, y = 50)
        
        self.window.mainloop()
        
    def func1(self,):
        self.foldpath1 = tkinter.filedialog.askdirectory() #获得选择好的文件夹
        self.text1.set(self.foldpath1)
        self.filelist = os.listdir(self.foldpath1)
        self.filenum = len(self.filelist)
        self.fileid = 1
        self.file_key = None
        file = self.filelist[self.fileid-1]
        self.text5.set(str(self.fileid)+'/'+str(self.filenum))
        self.filetimeList = []
        self.figid = 0
        if (file[-3:] == "jpg" or file[-3:] == "JPG"):
            image = Image.open(self.foldpath1+'/'+self.filelist[self.fileid-1])
            self.image = image
            fig = ImageTk.PhotoImage(image.resize((1000,560)))
            self.photo_label.config(image=fig)
            self.photo_label.image = fig 
            
            exif_data = image._getexif()
            ImageDate = exif_data[36867]
            ImageDate = ImageDate.replace(":","")
            ImageDate = ImageDate.replace(" ","")
            self.time = ImageDate
            self.file_key = 1
            self.filetimeList.append(self.time)
            self.figid += 1
        else:
            self.text4.set(file)
            #subprocess.call(r'C:/Program Files/Windows Media Player/wmplayer.exe '+self.foldpath1+"/" +file)
            os.startfile(self.foldpath1+"/" +file)
            time1 = os.path.getmtime(self.foldpath1+"/" +file)
            timeStruce = time.localtime(time1)
            times = time.strftime('%Y:%m:%d %H:%M:%S', timeStruce)
            times = times.replace(":","")
            times = times.replace(" ","")
            self.time = times
            self.file_key = 2
            
        
        
        
    def func2(self):
        self.foldpath2 = tkinter.filedialog.askdirectory() #获得选择好的文件夹
        self.text2.set(self.foldpath2)
        
    def func3(self):
        self.fileid -= 1
        if self.fileid == 0:
            self.fileid = self.filenum
            tkinter.messagebox.showinfo('提示','已经是第一张图片，将切到最后一张！')
        file = self.filelist[self.fileid-1]
        self.text5.set(str(self.fileid)+'/'+str(self.filenum))
        if (file[-3:] == "jpg" or file[-3:] == "JPG"):
            self.mp4_label.pack_forget()
            self.photo_label.pack()
            image = Image.open(self.foldpath1+'/'+self.filelist[self.fileid-1])
            self.image = image
            fig = ImageTk.PhotoImage(image.resize((1000,560)))
            self.photo_label.config(image=fig)
            self.photo_label.image = fig 
            
            self.figid -= 1
            self.time = self.filetimeList[self.figid-1]
            
            # exif_data = image._getexif()
            # ImageDate = exif_data[36867]
            # ImageDate = ImageDate.replace(":","")
            # ImageDate = ImageDate.replace(" ","")
            # self.time = ImageDate
            self.file_key = 1


        else:
            self.photo_label.pack_forget()
            self.mp4_label.pack(pady = 250)
            self.text4.set(file)
            #subprocess.call(r'C:/Program Files/Windows Media Player/wmplayer.exe '+self.foldpath1+"/" +file)
            os.startfile(self.foldpath1+"/" +file)
            time1 = os.path.getmtime(self.foldpath1+"/" +file)
            timeStruce = time.localtime(time1)
            times = time.strftime('%Y:%m:%d %H:%M:%S', timeStruce)
            times = times.replace(":","")
            times = times.replace(" ","")
            self.time = times    
            self.file_key = 2

            
    def func4(self):
        self.fileid += 1
        if self.fileid > self.filenum:
            self.fileid = 1
            tkinter.messagebox.showinfo('提示','已经是最后一张图片，将切到第一张！')
            
        file = self.filelist[self.fileid-1]
        self.text5.set(str(self.fileid)+'/'+str(self.filenum))
        
        if (file[-3:] == "jpg" or file[-3:] == "JPG"):      
            self.mp4_label.pack_forget()
            self.photo_label.pack()
            image = Image.open(self.foldpath1+'/'+self.filelist[self.fileid-1])
            self.image = image
            fig = ImageTk.PhotoImage(image.resize((1000,560)))
            self.photo_label.config(image=fig)
            self.photo_label.image = fig 
            
            self.figid += 1
            if (self.figid <= len(self.filetimeList)):
                self.time = self.filetimeList[self.figid-1]
            else:
                exif_data = image._getexif()
                ImageDate = exif_data[36867]
                ImageDate = ImageDate.replace(":","")
                ImageDate = ImageDate.replace(" ","")
                self.time = ImageDate 
                if self.time in self.filetimeList:
                    temp = 1
                    while (self.time + "(" + str(temp) + ")" in self.filetimeList):
                        temp += 1
                    self.time = self.time + "(" + str(temp) + ")"
                    self.filetimeList.append(self.time)
                else:
                    self.filetimeList.append(self.time)
            self.file_key = 1
            
        else:
            self.photo_label.pack_forget()
            self.mp4_label.pack(pady = 250)
            self.text4.set(file)           
            #subprocess.call(r'C:/Program Files/Windows Media Player/wmplayer.exe '+self.foldpath1+"/" +file)
            os.startfile(self.foldpath1+"/" +file)
            time1 = os.path.getmtime(self.foldpath1+"/" +file)
            timeStruce = time.localtime(time1)
            times = time.strftime('%Y:%m:%d %H:%M:%S', timeStruce)
            times = times.replace(":","")
            times = times.replace(" ","")
            self.time = times  
            self.file_key = 2
                    
    def func5(self):
        self.newname = "珠颈斑鸠"
        self.func8()
        self.func9()
    
    def func6(self):
        self.newname = "乌鸫"
        self.func8()
        self.func9()
        
    def func7(self):
        self.newname = "白头鹎"    
        self.func8()
        self.func9()
        
    def func10(self):
        self.newname = "远东山雀"
        self.func8()
        self.func9()
    
    def func11(self):
        self.newname = "鹊鸲"
        self.func8()
        self.func9()
        
    def func12(self):
        self.newname = "黄鼬"    
        self.func8()
        self.func9()   
    
    def func13(self):
        
        import os
        import xlwt #操作excel模块
        import sys
         
        file_path =self.foldpath2+'/enamelist.xls'#sys.path[0]为要获取当前路径，filenamelist为要写入的文件
        f = xlwt.Workbook(encoding='utf-8', style_compression=0) #新建一个excel
        sheet = f.add_sheet('sheet1') #新建一个sheet
        pathDir = os.listdir(self.foldpath2)#文件放置在当前文件夹中，用来获取当前文件夹内所有文件目录
         
        i = 0 #将文件列表写入test.xls
        for s in pathDir:
            sheet.write(i, 0, s) #参数i,0,s分别代表行，列，写入值
            i = i+1
        f.save(file_path)
        
    def func8(self):
        if self.e2.get() != "":
            self.newname = self.e2.get()
        self.filename =  self.e1.get() +" " +self.time+ " " + self.newname
        if self.file_key == 1:
            self.filename = self.filename + '.jpg'
        else:
            self.filename = self.filename + '.mp4'   
        self.text3.set("新文件名：" + self.filename)
        #self.func9()
    
    def func9(self):
        if self.foldpath2 == "未选择文件夹":
            print("未选择目标文件夹")
        if self.file_key == 1:
            self.image.save(self.foldpath2 + '/' + self.filename)
        else:
            shutil.copy(self.foldpath1 + '/'+self.filelist[self.fileid-1],self.foldpath2 + '/' + self.filename)
    
if __name__ == "__main__":
    window1 = Test()
    
        
        
        