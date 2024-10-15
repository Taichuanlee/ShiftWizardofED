import streamlit as st
import pandas as pd
import random
from io import StringIO

st.title("班表生成應用")

# Step 1: 定義分配邏輯（包含基礎的班別分配）
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
        
        # 確保班別需求
        if check_shift_needs(final_df, shift_needs, months):
            break

    return final_df

# Step 2: 定義保底機制
def ensure_minimum_matches_with_swap(schedule, original_preferences, months, min_matches=2):
    def calculate_matches(employee, original, schedule):
        matches = 0
        for i, month in enumerate(months):
            if schedule.at[employee, month] == original[i]:
                matches += 1
        return matches

    has_suai_ghosts = True
    while has_suai_ghosts:
        has_suai_ghosts = False
        for employee, original in original_preferences.items():
            matches = calculate_matches(employee, original, schedule)
            if matches < min_matches:
                has_suai_ghosts = True
                for top_employee, top_original in original_preferences.items():
                    if top_employee == employee:
                        continue
                    top_matches = calculate_matches(top_employee, top_original, schedule)
                    if top_matches > matches:
                        for i, month in enumerate(months):
                            if schedule.at[top_employee, month] == original[i] and schedule.at[employee, month] != original[i]:
                                schedule.at[employee, month], schedule.at[top_employee, month] = schedule.at[top_employee, month], schedule.at[employee, month]
                                matches = calculate_matches(employee, original, schedule)
                                if matches >= min_matches:
                                    break
                        if matches >= min_matches:
                            break
    return schedule

# Step 3: 定義特殊班別分配
def assign_special_shifts(schedule_df, months):
    updated_schedule = schedule_df.copy()
    selected_employees = set()

    for month in months:
        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'N' and emp not in selected_employees]
        if available_employees:
            selected_N = random.choice(available_employees)
            updated_schedule.at[selected_N, month] = 'N1'
            selected_employees.add(selected_N)

    for month in months:
        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'E' and emp not in selected_employees]
        if available_employees:
            selected_E = random.choice(available_employees)
            updated_schedule.at[selected_E, month] = 'E1'
            selected_employees.add(selected_E)

    for month in months:
        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'A' and emp not in selected_employees]
        if len(available_employees) >= 2:
            selected_A1, selected_A2 = random.sample(available_employees, 2)
            updated_schedule.at[selected_A1, month] = 'A1'
            updated_schedule.at[selected_A2, month] = 'A2'
            selected_employees.add(selected_A1)
            selected_employees.add(selected_A2)

    return updated_schedule

# 檢查班別需求的輔助函數
def check_shift_needs(final_df, shift_needs, months):
    for month in months:
        count_A = (final_df[month] == 'A').sum()
        count_E = (final_df[month] == 'E').sum()
        count_N = (final_df[month] == 'N').sum()
        if count_A != shift_needs["A"] or count_E != shift_needs["E"] or count_N != shift_needs["N"]:
            return False
    return True

# Step 4: Streamlit界面與用戶交互
uploaded_file = st.file_uploader("上傳員工選擇文件 (CSV)", type="csv")

# 設定班別需求
a_count = st.slider("A 班人數", 1, 50, 5)
e_count = st.slider("E 班人數", 1, 50, 3)
n_count = st.slider("N 班人數", 1, 50, 2)
min_matches = st.slider("每人最少的班別匹配數", 1, 6, 2)

if uploaded_file is not None:
    try:
        # 將上傳的文件轉換為可以被 pd.read_csv 處理的格式
        stringio = StringIO(uploaded_file.getvalue().decode("ISO-8859-1"))
        employees_df = pd.read_csv(stringio, encoding='ISO-8859-1')
        st.write(employees_df)
    except Exception as e:
        st.error(f"Error reading file: {str(e)}")

# 添加執行按鈕
if uploaded_file and st.button("執行班表生成"):
    try:
        employees = employees_df.set_index('name').T.to_dict('list')

        # 生成初步班表
        shift_needs = {"A": a_count, "E": e_count, "N": n_count}
        months = ["January", "February", "March", "April", "May", "June"]
        schedule_df = assign_shifts_based_on_month_preferences(employees, shift_needs, months)

        # 執行保底機制
        second_schedule_df = ensure_minimum_matches_with_swap(schedule_df.copy(), employees, months, min_matches=min_matches)

        # 特殊班別分配
        final_schedule_df = assign_special_shifts(second_schedule_df, months)

        # 顯示生成的班表
        st.write("生成的最終班表：")
        st.dataframe(final_schedule_df)

        # 提供下載選項
        csv = final_schedule_df.to_csv(index=False)
        st.download_button("下載班表 (CSV)", csv, "schedule.csv", "text/csv")

    except Exception as e:
        st.error(f"Error during schedule generation: {str(e)}")
