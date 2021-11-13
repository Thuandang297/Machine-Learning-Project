import tkinter as tk
from tkinter import *
#Thêm các thư viện để xử lí 
#tkinter for GUI
import tkinter as tk
from tkinter import messagebox
#numpy để tính toán giá trị cho ma trận và mảng
import numpy as np
#matplotlib để vẽ các sơ đồ cho tập dữ liệu
import matplotlib.pyplot as plt

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from scipy.sparse import coo_matrix # for sparse matrix
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.metrics import accuracy_score #Tính xác suất sai số
from sklearn import linear_model 
import scipy.io as sio


#Khai báo các thư viện dùng để tạo giao diện cho ứng dụng ở đây tôi dùng Tkinter
#Thiết lập các giá trị mặc định cho giao diện như title hay kích thước của form hiện ra
master=tk.Tk()
master.title("Dự đoán khả năng nhiễm covid")
master.geometry("750x750")
#Các biến chứa giá trị mà người dùng đã nhập vào,Tương ứng với 1 nếu là có và 0 nếu là không
go_th=IntVar()
contact=IntVar()
forgein=IntVar()
sex=IntVar()
fever=IntVar()
cough=IntVar()
short_breath=IntVar()
headaches=IntVar()
myalgia=IntVar()
smoke=IntVar()
age=IntVar()
name=StringVar()
#Tạo các thành phần cơ bản cho giao diện bao gồm label,textbox để người dùng nhập dữ liệu
#Radio button để chọn giá trị 
tk.Label(master, text="Nhập các thông tin dưới đây").grid (column=0, row=0)

tk.Label(master, text="Họ và tên:").grid (column=0, row=1)
txt = Entry(master,textvariable = name,width=50)
txt.grid(column=1, row=1)

tk.Label (master, text="Tuổi:").grid (column=0, row=2)
age = Entry(master,width=50).grid(column=1, row=2)
age=tk.IntVar()

#####################SEX###################
tk.Label(master, text="Giới tính:").grid (column=0, row=3)

rad1 = Radiobutton(master, text="Nam",variable=sex, value=1)
rad2 = Radiobutton(master, text="Nữ",variable=sex, value=0)

rad1.grid(column=0, row=4)
rad2.grid(column=0, row=5)




#############################CONTACT#################
tk.Label(master, text="Có tiếp xúc với người nghi nhiễm trong vòng 14 ngày qua không?").grid(row=6,column=0)
rad3 = Radiobutton(master, text="Có",variable=contact ,value=1)
rad4 = Radiobutton(master, text="Không",variable=contact, value=0)

rad3.grid(column=0, row=7)
rad4.grid(column=0, row=8)

##########################FORGEIN#####################
tk.Label(master, text="Có về từ nước ngoài trong vòng 14 ngày qua không?",anchor=W).grid(row=9,column=0)
rad5 = Radiobutton(master, text="Có",variable=forgein, value=1)
rad6 = Radiobutton(master, text="Không",variable=forgein, value=0)

rad5.grid(column=0, row=10)
rad6.grid(column=0, row=11)
##########################GO THOURGH THE DISEASES#####################
tk.Label(master, text="Có đi qua vùng dịch trong vòng 14 ngày qua không?",anchor=W).grid(row=12,column=0)
rad7 = Radiobutton(master, text="Có",variable=go_th, value=1)
rad8 = Radiobutton(master, text="Không",variable=go_th, value=0)

rad7.grid(column=0, row=13)
rad8.grid(column=0, row=14)
##########################SMOKE#####################
tk.Label(master, text="Có hút thuốc không?",anchor=W).grid(row=15,column=0)
rad9 = Radiobutton(master, text="Có",variable=smoke, value=1)
rad10 = Radiobutton(master, text="Không",variable=smoke, value=0)

rad9.grid(column=0, row=16)
rad10.grid(column=0, row=17)

##########################HEADACHES#####################
tk.Label(master, text="Các triệu chứng(nếu có)",anchor=W).grid(row=18,column=0)
tk.Label(master, text="Đau đầu").grid(row=19,column=0)
rad11 = Radiobutton(master, text="Có",variable=headaches, value=1)
rad12 = Radiobutton(master, text="Không",variable=headaches, value=0)

rad11.grid(column=0, row=20)
rad12.grid(column=0, row=21)
##########################COUGH#####################
tk.Label(master, text="Ho").grid(row=19,column=1)
rad13 = Radiobutton(master, text="Có",variable=cough, value=1)
rad14 = Radiobutton(master, text="Không",variable=cough, value=0)

rad13.grid(column=1, row=20)
rad14.grid(column=1, row=21)
##########################SHORT OF BREATH#####################
tk.Label(master, text="Khó thở").grid(row=22,column=0)
rad15 = Radiobutton(master, text="Có",variable=short_breath, value=1)
rad16 = Radiobutton(master, text="Không",variable=short_breath, value=0)

rad15.grid(column=0, row=23)
rad16.grid(column=0, row=24)
##########################FEVER#####################
tk.Label(master, text="Sốt").grid(row=22,column=1)
rad17 = Radiobutton(master, text="Có",variable=fever, value=1)
rad18 = Radiobutton(master, text="Không",variable=fever, value=0)

rad17.grid(column=1, row=23)
rad18.grid(column=1, row=24)
########################## MYALGIAL #####################
tk.Label(master, text="Đau cơ").grid(row=25,column=0)
rad19 = Radiobutton(master, text="Có",variable=myalgia, value=1)
rad20 = Radiobutton(master, text="Không",variable=myalgia, value=0)

rad19.grid(column=0, row=26)
rad20.grid(column=0, row=27)


#Tạo button Quit để thoát khỏi form
tk.Button(master, 
          text='Quit', 
          command=master.quit).grid(row=30, 
                                    column=0, 
                                    sticky=tk.W,
                                    pady=4)

#Thêm data vào từ 2 tập dữ liệu với input là Data.txt và nhãn cho tập dữ liệu trong Data_y.txt
file_x='Train_x.txt'
data=pd.read_csv(file_x,sep='\t')
#Chuyển data vừa đưa vào về dạng numpy.array
X = data.values
file_y="Train_y.txt"
data=pd.read_csv(file_y,sep='\t')
y=data.values
y=y.reshape(100)
print(y)

file_x='Test_x.txt'
data=pd.read_csv(file_x,sep='\t')
#Chuyển data vừa đưa vào về dạng numpy.array
test_x = data.values
file_y="Test_y.txt"
data=pd.read_csv(file_y,sep='\t')
test_y=data.values

file_x='Logistic_train_y.txt'
data=pd.read_csv(file_x,sep='\t')
#Chuyển data vừa đưa vào về dạng numpy.array
Logistic_train_y = data.values
Logistic_train_y=Logistic_train_y.reshape(100)

file_y="Logistic_test_y.txt"
data=pd.read_csv(file_y,sep='\t')
Logistic_test_y=data.values
Logistic_test_y.reshape(31)



#Sử dụng Bootstrapping để tăng độ chính xác cho thuật toán
X1=X
X2=X
X3=X
#Sử dụng bootstrapping để tách y thành 3 nhóm 
y1=y
y2=y
y3=y


# Lấy random 3 ma trận mỗi ma trận 50 tập ví dụ huấn luyện
i=np.random.randint(100,size=50)
X1=X1[i]
X2=X2[i]
X3=X3[i]
y1=y1[i]
y2=y2[i]
y3=y3[i]
#Sử dụng thư viện trong sklearn để training cho tập ví dụ huấn luyện

clf1 = make_pipeline(StandardScaler(), SVC(gamma='auto'))
clf2= linear_model.LogisticRegression(C=1e5) 
clf3 = BernoulliNB(binarize = .5)
clf1.fit(X1,y1)
clf2.fit(X2,y2)
clf3.fit(X3,y3)
def getvalue():
	name=txt.get()
# Hàm predict để đưa dữ liệu vào và tính trung bình nhãn cho 3 tập dữ liệu bootstrapping vừa có được
def predict():
   bien1 =  float(go_th.get())
   bien2 =  float(contact.get()) 
   bien3 =  float(forgein.get())
   bien4 =  float(sex.get()) 
   bien5 =  float(fever.get())
   bien6 =  float(age.get()) 
   bien7 =  float(cough.get())
   bien8 =  float(short_breath.get()) 
   bien9 =  float(headaches.get()) 
   bien10 =  float(myalgia.get())
   bien11 =  float(smoke.get()) 
   #Hàm clf.predict để đưa ra nhãn cho tập dữ liệu,giá trị trả về sẽ là -1 hoặc 1
   i1= clf1.predict([[bien1,bien2,bien3,bien4,bien5,bien6,bien7,bien8,bien9,bien10,bien11]])
   i2 = clf2.predict([[bien1,bien2,bien3,bien4,bien5,bien6,bien7,bien8,bien9,bien10,bien11]])
   i3= clf3.predict([[bien1,bien2,bien3,bien4,bien5,bien6,bien7,bien8,bien9,bien10,bien11]])
   xac_xuat= clf2.predict_proba([[bien1,bien2,bien3,bien4,bien5,bien6,bien7,bien8,bien9,bien10,bien11]])
   xs=xac_xuat[0][1]
   xs=round(xs,4)
   print("khả năng nhiễm bệnh",xac_xuat[0][1])
#    i=(i1+i2+i3)/3
   i=i2;
   if i>0:
    i=1
    messagebox.showinfo( "Dự đoán ", " Bạn có khả năng nhiễm covid! \n Vui lòng đến ngay cơ sở y tế gần nhất để kiểm tra!")
    messagebox.showinfo("Khả năng nhiễm bệnh của bạn là ", xs*100 )
   else:
    i=-1
    messagebox.showinfo( "Dự đoán"," Chúc mừng!Bạn không nhiễm covid")
   

tk.Button(master,  text='Show Label', command=predict).grid(row=30, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
# model = SVC(kernel='linear', probability=True)
# model.fit(X, y)                                       
# w = model.coef_

# print('w = ', w)
# print(getvalue())


#Tính toán độ chính xác của thuật toán


# y.ravel(100)
# print(test_y)



#Test độ chính xác cho thuật toán bằng SVM
clf = SVC(kernel='poly', degree = 1, gamma=1, C = 100)
clf.fit(X, y)
y_pred = clf.predict(test_x)
print("Độ chính xác của thuật toán SVM là: %.2f %%" %(100*accuracy_score(test_y, y_pred)))
master.mainloop()


#Sử dụng Navie Bayes trong phân
clf = MultinomialNB()
clf.fit(X, y)
# test
#Phân lớp với Navie Bayes và đưa ra độ chính xác
d6=[[1,1,1,1,1,26,1,1,1,1,1]]
print('Predicting class of d5:', str(clf.predict(d6)))
print('Probability of d6 in each class:', clf.predict_proba(d6))
#Sử dụng MultinomialNB 
y_pred = clf.predict(test_x)
print('Training size = %d, accuracy of MultinomialNB = %.2f%%' % \
      (X.shape[0],accuracy_score(test_y, y_pred)*100))
#Sử dụng BernoulliB
clf = BernoulliNB(binarize = .5)
clf.fit(X, y)
y_pred1 = clf.predict(d6)
y_pred = clf.predict(test_x)

print('Training size = %d, accuracy of BernoulliNB = %.2f%%' % \
      (X.shape[0],accuracy_score(test_y, y_pred)*100))
# print("predict",y_pred1)
# print("predict",str(clf.predict(X)[0]))
          # for logistic regression
from sklearn.metrics import accuracy_score # for evaluation
from scipy import misc
clf4= linear_model.LogisticRegression(C=1e5) # just a big number 
clf4.fit(X, Logistic_train_y)

y_pred = clf4.predict(test_x)
print ("Accuracy of logistic: %.2f %%" %(100*accuracy_score(Logistic_test_y, y_pred)))
#Khả năng nhiễm bệnh



