import streamlit as st
import pandas as pd
import random

st.title("班表生成應用")

# 定義班表生成邏輯
def assign_shifts_based_on_month_preferences(employees, shift_needs, months):
    final_df = pd.DataFrame(index=employees.keys(), columns=months)
    while True:
        final_df[:] = None
        for i, month in enumerate(months):
            candidates_for_A = [emp for emp, choices in employees.items() if choices[i] == "A"]
            candidates_for_E = [emp for emp, choices in employees.items() if choices[i] == "E"]
            candidates_for_N = [emp for emp, choices in employees.items() if choices[i] == "N"]

            selected_A = random.sample(candidates_for_A, min(len(candidates_for_A), shift_needs["A"]))
            selected_E = random.sample(candidates_for_E, min(len(candidates_for_E), shift_needs["E"]))
            selected_N = random.sample(candidates_for_N, min(len(candidates_for_N), shift_needs["N"]))

            final_df.loc[selected_A, month] = 'A'
            final_df.loc[selected_E, month] = 'E'
            final_df.loc[selected_N, month] = 'N'
        
        # 假設我們有一個檢查班別需求的函數
        if check_shift_needs(final_df, shift_needs, months):
            break

    return final_df

# 定義上傳文件的選項
uploaded_file = st.file_uploader("上傳員工選擇文件 (CSV)", type="csv")

# 設定班別需求
a_count = st.slider("A 班人數", 1, 50, 5)
e_count = st.slider("E 班人數", 1, 50, 3)
n_count = st.slider("N 班人數", 1, 50, 2)

if uploaded_file:
    employees_df = pd.read_csv(uploaded_file)
    employees = employees_df.set_index('name').T.to_dict('list')

    # 生成班表
    shift_needs = {"A": a_count, "E": e_count, "N": n_count}
    months = ["January", "February", "March", "April", "May", "June"]
    schedule_df = assign_shifts_based_on_month_preferences(employees, shift_needs, months)

    # 顯示生成的班表
    st.write("生成的班表：")
    st.dataframe(schedule_df)

    # 提供下載選項
    csv = schedule_df.to_csv(index=False)
    st.download_button("下載班表 (CSV)", csv, "schedule.csv", "text/csv")


