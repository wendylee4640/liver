import tkinter as tk
from tkinter import messagebox

def submit():
    # 獲取使用者輸入的 GOP、GDP 和性別
    gop = float(gop_entry.get())
    gpt = float(gpt_entry.get())
    gender = gender_var.get()

    # 根據使用者輸入的 GOP、GDP 和性別進行判斷，並顯示相應的健康建議
    if gender == "男":
        if gop < 37 and gpt < 41:
            messagebox.showinfo("健康建議", "你的肝是健康寶寶!!")
        elif gop >= 37 and gpt < 41:
            response = messagebox.askquestion("健康建議", "你的肝好像有點嚴重ㄟ....可能是喝酒或非肝臟的器官細胞受傷所導致肝指數升高，也有可能是肝硬化所導致!\n你想要救救你的肝嗎?")
            if response == "yes":
                messagebox.showinfo("健康建議", "酒杯收掉 !!! 換成一杯無糖豆漿吧~去醫院檢查一下吧～看看有沒有肝硬化^_^如果是工作應酬所需，那男性每日請不要超過20g，女性請不要超過10g ! !多吃豆類、生薑、益生元來降降你的肝指數吧!")
            else:
                messagebox.showinfo("健康建議", "你的肝要哭哭惹....")
        elif gop >= 37 and gpt >= 41:
            response = messagebox.askquestion("健康建議", "你的肝好像有點嚴重ㄟ....你可能是肝臟發炎導致肝指數升高\n你想要救救你的肝嗎?")
            if response == "yes":
                messagebox.showinfo("健康建議", "少吃辛辣、刺激、添加過多人工香料及熏烤的食物，也不要因為節儉而吃快過期的海產類，在這期間你的消化能力比較弱，記得少量多餐，吃點新鮮魚肉、瘦肉、紅蘿蔔、綠色青菜、番茄、牛奶!")
            else:
                messagebox.showinfo("健康建議", "你的肝要哭哭惹....")
        elif gop >= 37 and gpt >= 41 and gop > gpt:
            response = messagebox.askquestion("健康建議", "你的肝好像有點嚴重ㄟ....你可能是慢性B、C肝炎 、脂肪性肝炎，或者是因另外藥物性及自體免疫性導致的肝炎\n你想要救救你的肝嗎?")
            if response == "yes":
                messagebox.showinfo("健康建議", "先去找醫生確定自己得到哪類型肝炎，並給予相對應治療，如為慢性B肝 ：不要吸菸、嚼檳榔、喝酒，不要食用人工添加劑、醃製、或可能本黃麴毒素所污染的食物（ex：花生醬、豆瓣醬…….）；如為慢性C肝：請多休息、維持規律生活、運動，均衡飲食，避免不必要的打針、刺青、穿耳洞，避免服用成分不明的藥物偏方、草藥；如為脂肪肝：🈲酒🈲油，多攝取蛋白質、食物纖維，還有要多運動!!慢性B肝!")
            else:
                messagebox.showinfo("健康建議", "你的肝要哭哭惹....")
    elif gender == "女":
        if gop < 31 and gpt < 31:
            messagebox.showinfo("健康建議", "你的肝是健康寶寶!!")
        elif gop >= 31 and gpt < 31:
            response = messagebox.askquestion("健康建議", "你的肝好像有點嚴重ㄟ....可能是喝酒或非肝臟的器官細胞受傷所導致肝指數升高，也有可能是肝硬化所導致!\n你想要救救你的肝嗎?")
            if response == "yes":
                messagebox.showinfo("健康建議", "酒杯收掉 !!! 換成一杯無糖豆漿吧~去醫院檢查一下吧～看看有沒有肝硬化^_^如果是工作應酬所需，那男性每日請不要超過20g，女性請不要超過10g ! !多吃豆類、生薑、益生元來降降你的肝指數吧!")
            else:
                messagebox.showinfo("健康建議", "你的肝要哭哭惹....")
        elif gop >= 31 and gpt >= 31:
            response = messagebox.askquestion("健康建議", "你的肝好像有點嚴重ㄟ....你可能是肝臟發炎導致肝指數升高\n你想要救救你的肝嗎?")
            if response == "yes":
                messagebox.showinfo("健康建議", "少吃辛辣、刺激、添加過多人工香料及熏烤的食物，也不要因為節儉而吃快過期的海產類，在這期間你的消化能力比較弱，記得少量多餐，吃點新鮮魚肉、瘦肉、紅蘿蔔、綠色青菜、番茄、牛奶!")
            else:
                messagebox.showinfo("健康建議", "你的肝要哭哭惹....")

# 創建主視窗
root = tk.Tk()
root.title("肝健康評估系統")

# 創建 GOP 輸入欄位
gop_label = tk.Label(root, text="請輸入 GOP：")
gop_label.grid(row=0, column=0, padx=10, pady=5)
gop_entry = tk.Entry(root)
gop_entry.grid(row=0, column=1, padx=10, pady=5)

# 創建 GPT 輸入欄位
gpt_label = tk.Label(root, text="請輸入 GPT：")
gpt_label.grid(row=1, column=0, padx=10, pady=5)
gpt_entry = tk.Entry(root)
gpt_entry.grid(row=1, column=1, padx=10, pady=5)

# 創建性別選項
gender_label = tk.Label(root, text="請選擇性別：")
gender_label.grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("男")  # 預設值為男性
gender_male = tk.Radiobutton(root, text="男", variable=gender_var, value="男")
gender_male.grid(row=2, column=1, padx=10, pady=5, sticky="w")
gender_female = tk.Radiobutton(root, text="女", variable=gender_var, value="女")
gender_female.grid(row=2, column=1, padx=10, pady=5, sticky="e")

# 創建提交按鈕
submit_button = tk.Button(root, text="提交", command=submit)
submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# 啟動主迴圈
root.mainloop()
