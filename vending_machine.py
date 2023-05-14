import tkinter as tk
from tkinter import messagebox

class VendingMachine:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("E동 5층 자판기")

        #음료수 초기 개수
        self.cola_count = 10
        self.cider_count = 10
        self.water_count = 10
        self.lemonwater_count = 10
        self.trevi_count = 10
        self.coldbrew_count = 10
        self.mango_count = 10
        self.libton_count = 10
        self.tropicana_count = 10
        self.sikhye_count = 10
        self.cocopodo_count = 10
        self.milkiss_count = 10
        self.hot6_count = 10
        self.mountaindew_count = 10
        self.ghana_count = 10
        self.coffee_count = 10          

        # 음료수 개수 표시 라벨
        self.drink_counts_label = tk.Label(self.window, text = self.get_drink_counts(), font = ("Arial", 12))
        
        # 음료 가격
        self.cola_price = 900
        self.cider_price = 1100
        self.water_price = 700
        self.lemonwater_price = 1600        
        self.trevi_price = 1100
        self.coldbrew_price = 2100
        self.mango_price = 1100
        self.libton_price = 1100
        self.tropicana_price = 1100
        self.sikhye_price = 900
        self.cocopodo_price = 900
        self.milkiss_price = 900
        self.hot6_price = 1100
        self.mountaindew_price = 900
        self.ghana_price = 700
        self.coffee_price = 700
                                            
        # 현재 금액
        self.current_money = 0

        # 지폐 및 동전 추가 버튼
        self.insert_money_btns = []
        for money in [1000, 500, 100]:
            btn = tk.Button(self.window, text=f"{money}원 추가", width=15, command=lambda money=money: self.insert_money(money))
            self.insert_money_btns.append(btn)

        # 음료 선택 버튼
        self.select_drink_btns = []
        for name, price in [("콜라", self.cola_price), ("사이다", self.cider_price), ("물", self.water_price),("레몬워터", self.lemonwater_price), 
                            ("트레비", self.trevi_price), ("콜드브루", self.coldbrew_price), ("망고", self.mango_price), ("립톤", self.libton_price), 
                            ("트로피카나", self.tropicana_price), ("잔치집식혜", self.sikhye_price), ("코코포도", self.cocopodo_price), ("밀키스", self.milkiss_price),
                            ("핫식스", self.hot6_price), ("마운틴듀", self.mountaindew_price), ("가나초콜릿", self.ghana_price), ("레쓰비", self.coffee_price)]:
            btn = tk.Button(self.window, text=f"{name} - {price}원", width=15, command=lambda price=price: self.select_drink(price))
            self.select_drink_btns.append(btn)

        # 현재 금액 표시 라벨
        self.current_money_label = tk.Label(self.window, text="현재 금액: 0원", font=("HY헤드라인M", 20))

        # 거스름돈 반환 버튼
        self.return_money_btn = tk.Button(self.window, text="거스름돈 반환", width=25, command=self.return_money)
        
        # 음료 재고 표시 라벨
        self.current_balance_label = tk.Label(self.window, text="<음료 재고표>", font=("HY헤드라인M", 20))

        # 위젯 배치
        tk.Label(self.window, text="금액 추가").grid(row=0, column=0)
        for i, btn in enumerate(self.insert_money_btns):
            btn.grid(row=1, column=i)
        tk.Label(self.window, text="음료 선택").grid(row=2, column=0)
        for i, btn in enumerate(self.select_drink_btns[0:7]):
            btn.grid(row=3, column=i)
        for i, btn in enumerate(self.select_drink_btns[7:14]):    
            btn.grid(row=4, column=i)
        self.current_money_label.grid(row=5, column=0, columnspan= 6)
        self.return_money_btn.grid(row=6, column=0, columnspan= 6)
        self.current_balance_label.grid(row=7,column=0, columnspan= 6)            
        self.drink_counts_label.grid(row = 8, column = 0, columnspan = 6)     
    


    # 음료수 개수 반환 메소드
    def get_drink_counts(self):
        return f"""콜라: {self.cola_count}캔, 사이다: {self.cider_count}캔, 물: {self.water_count}병, 레몬워터: {self.lemonwater_count}병, 트레비: {self.trevi_count}병, 
        콜드브루: {self.coldbrew_count}병, 망고: {self.mango_count}캔, 립톤: {self.libton_count}캔, 트로피카나: {self.tropicana_count}캔, 잔치집식혜: {self.sikhye_count}캔, 
        코코포도: {self.cocopodo_count}캔, 밀키스: {self.milkiss_count}캔, 핫식스: {self.hot6_count}캔, 마운틴듀: {self.mountaindew_count}캔"""
    
    def run(self):
        self.window.mainloop()

    def return_money(self):
        messagebox.showinfo("거스름돈 반환", f"{self.current_money}원이 반환되었습니다.")
        self.current_money = 0
        self.current_money_label.config(text=f"현재 금액: {self.current_money}원")
    
    def insert_money(self, money):
        self.current_money += money
        self.current_money_label.config(text=f"현재 금액: {self.current_money}원")

    def select_drink(self, price):
        if self.current_money >= price:
            if price == self.cola_price:
                if self.cola_count <= 0:
                    messagebox.showerror("품절", "콜라가 품절입니다.")
                    return
                self.cola_count -= 1
            elif price == self.cider_price:
                if self.cider_count <= 0:
                    messagebox.showerror("품절", "사이다가 품절입니다.")
                    return
                self.cider_count -= 1
            elif price == self.water_price:
                if self.water_count <= 0:
                    messagebox.showerror("품절", "물이 품절입니다.")
                    return
                self.water_count -= 1
            elif price == self.lemonwater_price:
                if self.lemonwater_count <= 0:
                    messagebox.showerror("품절", "레몬워터가 품절입니다.")
                    return
                self.lemonwater_count -= 1    
            elif price == self.trevi_price:
                if self.trevi_count <= 0:
                    messagebox.showerror("품절", "트레비가 품절입니다.")
                    return
                self.trevi_count -= 1
            elif price == self.coldbrew_price:
                if self.coldbrew_count <= 0:
                    messagebox.showerror("품절", "콜드브루가 품절입니다.")
                    return
                self.coldbrew_count -= 1
            elif price == self.mango_price:
                if self.mango_count <= 0:
                    messagebox.showerror("품절", "망고가 품절입니다.")
                    return
                self.mango_count -= 1
            elif price == self.libton_price:
                if self.libton_count <= 0:
                    messagebox.showerror("품절", "립톤이 품절입니다.")
                    return
                self.libton_count -= 1
            elif price == self.tropicana_price:
                if self.tropicana_count <= 0:
                    messagebox.showerror("품절", "트로피카나가 품절입니다.")
                    return
                self.tropicana_count -= 1
            elif price == self.sikhye_price:
                if self.sikhye_count <= 0:
                    messagebox.showerror("품절", "잔치집식혜가 품절입니다.")
                    return
                self.sikhye_count -= 1
            elif price == self.cocopodo_price:
                if self.cocopodo_count <= 0:
                    messagebox.showerror("품절", "코코포도가 품절입니다.")
                    return
                self.cocopodo_count -= 1
            elif price == self.milkiss_price:
                if self.milkiss_count <= 0:
                    messagebox.showerror("품절", "밀키스가 품절입니다.")
                    return
                self.milkiss_count -= 1
            elif price == self.hot6_price:
                if self.hot6_count <= 0:
                    messagebox.showerror("품절", "핫식스가 품절입니다.")
                    return
                self.hot6_count -= 1
            elif price == self.mountaindew_price:
                if self.mountaindew_count <= 0:
                    messagebox.showerror("품절", "마운틴듀가 품절입니다.")
                    return
                self.mountaindew_count -= 1                                
            
            
            self.current_money -= price
            self.current_money_label.config(text=f"현재 금액: {self.current_money}원")
            messagebox.showinfo("구매 완료", "음료가 나왔습니다. 맛있게 드세요!")
            self.drink_counts_label.config(text=self.get_drink_counts())
        else:
            messagebox.showerror("잔액 부족", "금액이 부족합니다. 금액을 추가해주세요.")

vm = VendingMachine()
vm.run() 