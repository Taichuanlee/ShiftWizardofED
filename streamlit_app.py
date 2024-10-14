import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMCvREsO3b45DunQnb3J/cA",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Taichuanlee/ShiftWizard/blob/main/%E6%8A%BD%E7%8F%AD%E5%88%A5_ver_%E5%AF%A6%E9%A9%97.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install gspread oauth2client"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "agXT96Qfj7j5",
        "outputId": "00e97d18-8707-49f6-d653-59858a3ebf22"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: gspread in /usr/local/lib/python3.10/dist-packages (6.0.2)\n",
            "Requirement already satisfied: oauth2client in /usr/local/lib/python3.10/dist-packages (4.1.3)\n",
            "Requirement already satisfied: google-auth>=1.12.0 in /usr/local/lib/python3.10/dist-packages (from gspread) (2.27.0)\n",
            "Requirement already satisfied: google-auth-oauthlib>=0.4.1 in /usr/local/lib/python3.10/dist-packages (from gspread) (1.2.1)\n",
            "Requirement already satisfied: StrEnum==0.4.15 in /usr/local/lib/python3.10/dist-packages (from gspread) (0.4.15)\n",
            "Requirement already satisfied: httplib2>=0.9.1 in /usr/local/lib/python3.10/dist-packages (from oauth2client) (0.22.0)\n",
            "Requirement already satisfied: pyasn1>=0.1.7 in /usr/local/lib/python3.10/dist-packages (from oauth2client) (0.6.1)\n",
            "Requirement already satisfied: pyasn1-modules>=0.0.5 in /usr/local/lib/python3.10/dist-packages (from oauth2client) (0.4.1)\n",
            "Requirement already satisfied: rsa>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from oauth2client) (4.9)\n",
            "Requirement already satisfied: six>=1.6.1 in /usr/local/lib/python3.10/dist-packages (from oauth2client) (1.16.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth>=1.12.0->gspread) (5.5.0)\n",
            "Requirement already satisfied: requests-oauthlib>=0.7.0 in /usr/local/lib/python3.10/dist-packages (from google-auth-oauthlib>=0.4.1->gspread) (1.3.1)\n",
            "Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /usr/local/lib/python3.10/dist-packages (from httplib2>=0.9.1->oauth2client) (3.1.4)\n",
            "Requirement already satisfied: oauthlib>=3.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (3.2.2)\n",
            "Requirement already satisfied: requests>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (2.32.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.0.0->requests-oauthlib>=0.7.0->google-auth-oauthlib>=0.4.1->gspread) (2024.8.30)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "這邊是上傳檔案的部分\n",
        "\n",
        "用 csv檔\n",
        "\n",
        "**注意事項:**\n",
        "\n",
        "刪除時間戳記 (原編/班別)\n",
        "\n",
        "第一行單純就是name 月份"
      ],
      "metadata": {
        "id": "YIdXYVtm75Aw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "# 上傳文件\n",
        "uploaded = files.upload()\n",
        "\n",
        "# 檢查上傳的文件名稱\n",
        "for file_name in uploaded.keys():\n",
        "    print(f\"Uploaded file: {file_name}\")\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 86
        },
        "collapsed": true,
        "id": "MbnQAgSD38hg",
        "outputId": "a747577b-6a35-4ba9-ce98-8fde8eeaf75c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-f73c1e73-a127-4be2-abe9-baa649744faa\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-f73c1e73-a127-4be2-abe9-baa649744faa\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving 班表測試 (姓名版).csv to 班表測試 (姓名版).csv\n",
            "Uploaded file: 班表測試 (姓名版).csv\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "這個是測試用的，記得修改檔案位置\n",
        "\n",
        "file_path = '/content/這個示範例.csv'"
      ],
      "metadata": {
        "id": "Nmgp2NeC8KZB"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# 讀取 CSV 文件，這裡忽略第一列（Time）\n",
        "file_path = '/content/班表測試 (姓名版).csv'\n",
        "df = pd.read_csv(file_path)\n",
        "\n",
        "\n",
        "# 將 DataFrame 轉換為字典，鍵為員工名稱，值為 1 月到 6 月的班別選擇\n",
        "employees = df.set_index('name').T.to_dict('list')\n",
        "\n",
        "# 將選擇的班別列表轉換為連接的字符串（例如 'NEEANN'）\n",
        "employees = {k: ''.join(v) for k, v in employees.items()}\n",
        "\n",
        "# 檢查轉換後的 employees 字典\n",
        "print(employees)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-3-BhovFrnbP",
        "outputId": "4f592328-bfc9-4ca9-9d8f-33c42ebb15ae"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{'李岱川': 'NANNEE', '郭峰辭': 'NANNEE', '晨翔': 'EANNEE', '許銘偉': 'AANNNE', '度聖哲': 'AAAAAE', '陳雅婷': 'ENAEEE', '閎宴會': 'ANEENA', '陳冠宇': 'NEENNN', '陳懿文': 'NNAENN', '王翊傑': 'EAEAEE'}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "開始運行\n",
        "**更改班別需求 shift_needs = {\"A\": 5, \"E\": 4, \"N\": 2}"
      ],
      "metadata": {
        "id": "cWGsXnYp0Gct"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import random\n",
        "\n",
        "# 每月班別需求\n",
        "shift_needs = {\"A\": 5, \"E\": 3, \"N\": 2}\n",
        "months = [\"January\", \"February\", \"March\", \"April\", \"May\", \"June\"]\n",
        "\n",
        "# 定義檢查邏輯，確保班別需求滿足\n",
        "def check_shift_needs(final_df, shift_needs, months):\n",
        "    for month in months:\n",
        "        count_A = (final_df[month] == 'A').sum()\n",
        "        count_E = (final_df[month] == 'E').sum()\n",
        "        count_N = (final_df[month] == 'N').sum()\n",
        "        if count_A != shift_needs[\"A\"] or count_E != shift_needs[\"E\"] or count_N != shift_needs[\"N\"]:\n",
        "            return False\n",
        "    return True\n",
        "\n",
        "# 定義分配邏輯，新增確保每個員工至少有一個 A 班的檢查\n",
        "def assign_shifts_based_on_month_preferences(employees, shift_needs, months):\n",
        "    final_schedule = {month: {\"A\": [], \"E\": [], \"N\": []} for month in months}\n",
        "    final_df = pd.DataFrame(index=employees.keys(), columns=months)\n",
        "\n",
        "    while True:  # 不斷嘗試直到滿足兩個條件\n",
        "        # 清空分配\n",
        "        final_df[:] = None\n",
        "\n",
        "        # 優先分配每個月的需求\n",
        "        for i, month in enumerate(months):\n",
        "            # Step 1: 根據每個員工當月的選擇進行分配\n",
        "            candidates_for_A = [emp for emp, choices in employees.items() if choices[i] == \"A\"]\n",
        "            candidates_for_E = [emp for emp, choices in employees.items() if choices[i] == \"E\"]\n",
        "            candidates_for_N = [emp for emp, choices in employees.items() if choices[i] == \"N\"]\n",
        "\n",
        "            # Step 2: 如果候選人數超過需求，抽籤決定\n",
        "            selected_A = random.sample(candidates_for_A, min(len(candidates_for_A), shift_needs[\"A\"]))\n",
        "            selected_E = random.sample(candidates_for_E, min(len(candidates_for_E), shift_needs[\"E\"]))\n",
        "            selected_N = random.sample(candidates_for_N, min(len(candidates_for_N), shift_needs[\"N\"]))\n",
        "\n",
        "            # Step 3: 如果班別需求未滿，從未分配的人員中補齊\n",
        "            remaining_A = shift_needs[\"A\"] - len(selected_A)\n",
        "            remaining_E = shift_needs[\"E\"] - len(selected_E)\n",
        "            remaining_N = shift_needs[\"N\"] - len(selected_N)\n",
        "\n",
        "            not_selected = set(employees.keys()) - set(selected_A) - set(selected_E) - set(selected_N)\n",
        "\n",
        "            if remaining_A > 0:\n",
        "                selected_A += random.sample(list(not_selected), remaining_A)  # Convert set to list\n",
        "                not_selected = not_selected - set(selected_A)\n",
        "\n",
        "            if remaining_E > 0:\n",
        "                selected_E += random.sample(list(not_selected), remaining_E)  # Convert set to list\n",
        "                not_selected = not_selected - set(selected_E)\n",
        "\n",
        "            if remaining_N > 0:\n",
        "                selected_N += random.sample(list(not_selected), remaining_N)  # Convert set to list\n",
        "\n",
        "            # Step 4: 更新當月的班別分配至 DataFrame\n",
        "            for emp in selected_A:\n",
        "                final_df.at[emp, month] = 'A'\n",
        "            for emp in selected_E:\n",
        "                final_df.at[emp, month] = 'E'\n",
        "            for emp in selected_N:\n",
        "                final_df.at[emp, month] = 'N'\n",
        "\n",
        "        # Step 5: 確保每個員工至少有一個 A 班\n",
        "        for emp in employees.keys():\n",
        "            if 'A' not in final_df.loc[emp].values:\n",
        "                # 隨機選擇一個月份來分配 A 班\n",
        "                available_months = [month for month in months if final_df.at[emp, month] != 'A']\n",
        "                if available_months:\n",
        "                    chosen_month = random.choice(available_months)\n",
        "                    final_df.at[emp, chosen_month] = 'A'\n",
        "\n",
        "        # Step 6: 檢查是否滿足班別需求\n",
        "        if check_shift_needs(final_df, shift_needs, months):\n",
        "            break  # 如果滿足需求，跳出 while 循環，完成分配\n",
        "\n",
        "    return final_df\n",
        "\n",
        "\n",
        "\n",
        "# 執行班表分配\n",
        "schedule_df = assign_shifts_based_on_month_preferences(employees, shift_needs, months)\n",
        "\n",
        "# 顯示分配結果\n",
        "print(schedule_df)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "E2gzZCwP0KCF",
        "outputId": "8bbb6e3d-c8a8-473e-ab53-088d774cb21b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    January February March April May June\n",
            "李岱川       A        A     N     N   E    E\n",
            "郭峰辭       N        A     A     A   E    A\n",
            "晨翔        E        E     A     N   E    E\n",
            "許銘偉       A        A     N     A   N    A\n",
            "度聖哲       A        A     A     A   A    A\n",
            "陳雅婷       E        N     A     E   A    A\n",
            "閎宴會       A        E     E     E   A    A\n",
            "陳冠宇       N        E     E     A   A    N\n",
            "陳懿文       A        N     A     E   N    N\n",
            "王翊傑       E        A     E     A   A    E\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**測試 保底機制**\n",
        "\n",
        "min_matches=2\n",
        "\n",
        "這邊要修改(實測下來，保底兩個是極限，三個容易爆炸)"
      ],
      "metadata": {
        "id": "iHmT2XN4DSKN"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def ensure_minimum_matches_with_swap(schedule, original_preferences, months, min_matches=2):\n",
        "    \"\"\"\n",
        "    確保每個員工在初步班表中有至少 min_matches 個班別與原始班表選擇相同，並進行交換班表。\n",
        "    每次交換後會重新檢查衰鬼。\n",
        "    \"\"\"\n",
        "    def calculate_matches(employee, original, schedule):\n",
        "        \"\"\"\n",
        "        計算某員工的中標次數\n",
        "        \"\"\"\n",
        "        matches = 0\n",
        "        for i, month in enumerate(months):\n",
        "            if schedule.at[employee, month] == original[i]:\n",
        "                matches += 1\n",
        "        return matches\n",
        "\n",
        "    # 一個用來記錄尚未達到保底標準的衰鬼員工\n",
        "    has_suai_ghosts = True\n",
        "\n",
        "    while has_suai_ghosts:\n",
        "        has_suai_ghosts = False  # 假設沒有衰鬼\n",
        "\n",
        "        for employee, original in original_preferences.items():\n",
        "            matches = calculate_matches(employee, original, schedule)\n",
        "\n",
        "            # 若中標數低於保底標準，則為衰鬼，進行調整\n",
        "            if matches < min_matches:\n",
        "                print(f\"{employee} is a 衰鬼 with {matches} matches.\")\n",
        "                has_suai_ghosts = True  # 設定有衰鬼\n",
        "\n",
        "                # 找中標最多的員工（從中標數高的開始）\n",
        "                for top_employee, top_original in original_preferences.items():\n",
        "                    if top_employee == employee:  # 跳過自己\n",
        "                        continue\n",
        "\n",
        "                    # 找到中標次數最多的員工\n",
        "                    top_matches = calculate_matches(top_employee, top_original, schedule)\n",
        "\n",
        "                    # 優先選擇中標最多的員工進行交換\n",
        "                    if top_matches > matches:\n",
        "                        for i, month in enumerate(months):\n",
        "                            # 確認中標最多員工的初步班表是否符合衰鬼的原始班表\n",
        "                            if (schedule.at[top_employee, month] == original[i] and  # 中標最多員工的初步班表符合衰鬼的原始班表\n",
        "                                schedule.at[employee, month] != original[i]):  # 衰鬼的初步班表不同於原始班表\n",
        "\n",
        "                                # 進行交換\n",
        "                                print(f\"Swapping {employee} and {top_employee} in {month}.\")\n",
        "                                temp = schedule.at[employee, month]\n",
        "                                schedule.at[employee, month] = schedule.at[top_employee, month]\n",
        "                                schedule.at[top_employee, month] = temp\n",
        "\n",
        "                                # 每次交換後重新檢查衰鬼的中標次數\n",
        "                                matches = calculate_matches(employee, original, schedule)\n",
        "                                if matches >= min_matches:\n",
        "                                    print(f\"{employee} has reached {matches} matches after adjustment.\")\n",
        "                                    break  # 停止交換，該衰鬼已達到保底標準\n",
        "\n",
        "                                # 若沒有達到保底標準，繼續嘗試交換\n",
        "                            else:\n",
        "                                continue\n",
        "\n",
        "                        # 若某個交換完成後，停止當前衰鬼的處理\n",
        "                        if matches >= min_matches:\n",
        "                            break\n",
        "\n",
        "    return schedule\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "# 創建初步班表的副本，確保不改動原始的 schedule_df\n",
        "initial_schedule_df = schedule_df.copy()\n",
        "\n",
        "# 執行班別互換的保底機制\n",
        "second_schedule_df = ensure_minimum_matches_with_swap(initial_schedule_df, employees, months)\n",
        "\n",
        "# 顯示更新後的分配結果\n",
        "print(second_schedule_df)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "-8ckmA5bDRGx",
        "outputId": "f5ccad67-2462-458c-d567-5d806d9427d2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    January February March April May June\n",
            "李岱川       A        A     N     N   E    E\n",
            "郭峰辭       N        A     A     A   E    A\n",
            "晨翔        E        E     A     N   E    E\n",
            "許銘偉       A        A     N     A   N    A\n",
            "度聖哲       A        A     A     A   A    A\n",
            "陳雅婷       E        N     A     E   A    A\n",
            "閎宴會       A        E     E     E   A    A\n",
            "陳冠宇       N        E     E     A   A    N\n",
            "陳懿文       A        N     A     E   N    N\n",
            "王翊傑       E        A     E     A   A    E\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Step 3: 新功能：依據生成的班表隨機抽取員工並替換班別\n",
        "def assign_special_shifts(schedule_df, months):\n",
        "    # 複製班表來進行修改\n",
        "    updated_schedule = schedule_df.copy()\n",
        "\n",
        "    # 追蹤已經被抽選過的員工，避免重複\n",
        "    selected_employees = set()\n",
        "\n",
        "    # Step 1: 處理 N 班，逐月隨機選取一位員工替換成 N1\n",
        "    for month in months:\n",
        "        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'N' and emp not in selected_employees]\n",
        "        if available_employees:\n",
        "            selected_N = random.choice(available_employees)\n",
        "            updated_schedule.at[selected_N, month] = 'N1'\n",
        "            selected_employees.add(selected_N)\n",
        "\n",
        "    # Step 2: 處理 E 班，逐月隨機選取一位員工替換成 E1\n",
        "    for month in months:\n",
        "        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'E' and emp not in selected_employees]\n",
        "        if available_employees:\n",
        "            selected_E = random.choice(available_employees)\n",
        "            updated_schedule.at[selected_E, month] = 'E1'\n",
        "            selected_employees.add(selected_E)\n",
        "\n",
        "    # Step 3: 處理 A 班，逐月隨機選取兩位員工替換成 A1 和 A2\n",
        "    for month in months:\n",
        "        available_employees = [emp for emp in schedule_df.index if schedule_df.at[emp, month] == 'A' and emp not in selected_employees]\n",
        "        if len(available_employees) >= 2:\n",
        "            selected_A1, selected_A2 = random.sample(available_employees, 2)\n",
        "            updated_schedule.at[selected_A1, month] = 'A1'\n",
        "            updated_schedule.at[selected_A2, month] = 'A2'\n",
        "            selected_employees.add(selected_A1)\n",
        "            selected_employees.add(selected_A2)\n",
        "\n",
        "    return updated_schedule\n",
        "\n",
        "# Step 4: 應用特殊抽籤邏輯，基於保底機制後的結果進行更新\n",
        "final_schedule_df = assign_special_shifts(second_schedule_df, months)\n",
        "\n",
        "# 顯示最終分配結果\n",
        "print(final_schedule_df)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 211
        },
        "id": "mng75qXxdHOp",
        "outputId": "f4a89fc2-3525-444c-b867-c86140202bf5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'second_schedule_df' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-3-9a4977f4c6dd>\u001b[0m in \u001b[0;36m<cell line: 38>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     36\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     37\u001b[0m \u001b[0;31m# Step 4: 應用特殊抽籤邏輯，基於保底機制後的結果進行更新\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 38\u001b[0;31m \u001b[0mfinal_schedule_df\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0massign_special_shifts\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msecond_schedule_df\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmonths\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     39\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     40\u001b[0m \u001b[0;31m# 顯示最終分配結果\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'second_schedule_df' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "**最後輸出檔案**"
      ],
      "metadata": {
        "id": "DRv2ylUgM7dh"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 保存結果為 CSV 文件\n",
        "schedule_df.to_csv('initial_schedule.csv', index=True)  # 保存初次班表分配結果\n",
        "second_schedule_df.to_csv('second_schedule.csv', index=True)  # 保存保底機制分配結果\n",
        "final_schedule_df.to_csv('final_schedule.csv', index=True)  # 保存最終分配結果\n",
        "\n",
        "# 如果需要，可以保存為 Excel 文件\n",
        "schedule_df.to_excel('initial_schedule.xlsx', index=True)  # 保存初次班表分配結果為 Excel\n",
        "second_schedule_df.to_excel('second_schedule.xlsx', index=True)  # 保存保底機制分配結果為 Excel\n",
        "final_schedule_df.to_excel('final_schedule.xlsx', index=True)  # 保存最終分配結果為 Excel"
      ],
      "metadata": {
        "id": "qoweVYmWKr6y"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# 顯示 CSV 文件路徑，以便在 Colab 上進行下載\n",
        "from google.colab import files\n",
        "files.download('team_shift_schedule.xlsx')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 17
        },
        "id": "cjZFh3TjMqPJ",
        "outputId": "9047a35b-8527-42fc-cb2e-57af00e73f1f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "\n",
              "    async function download(id, filename, size) {\n",
              "      if (!google.colab.kernel.accessAllowed) {\n",
              "        return;\n",
              "      }\n",
              "      const div = document.createElement('div');\n",
              "      const label = document.createElement('label');\n",
              "      label.textContent = `Downloading \"${filename}\": `;\n",
              "      div.appendChild(label);\n",
              "      const progress = document.createElement('progress');\n",
              "      progress.max = size;\n",
              "      div.appendChild(progress);\n",
              "      document.body.appendChild(div);\n",
              "\n",
              "      const buffers = [];\n",
              "      let downloaded = 0;\n",
              "\n",
              "      const channel = await google.colab.kernel.comms.open(id);\n",
              "      // Send a message to notify the kernel that we're ready.\n",
              "      channel.send({})\n",
              "\n",
              "      for await (const message of channel.messages) {\n",
              "        // Send a message to notify the kernel that we're ready.\n",
              "        channel.send({})\n",
              "        if (message.buffers) {\n",
              "          for (const buffer of message.buffers) {\n",
              "            buffers.push(buffer);\n",
              "            downloaded += buffer.byteLength;\n",
              "            progress.value = downloaded;\n",
              "          }\n",
              "        }\n",
              "      }\n",
              "      const blob = new Blob(buffers, {type: 'application/binary'});\n",
              "      const a = document.createElement('a');\n",
              "      a.href = window.URL.createObjectURL(blob);\n",
              "      a.download = filename;\n",
              "      div.appendChild(a);\n",
              "      a.click();\n",
              "      div.remove();\n",
              "    }\n",
              "  "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "download(\"download_b52bba36-809a-4712-915b-7776649599b8\", \"team_shift_schedule.xlsx\", 9652)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "以下為保底機制的test"
      ],
      "metadata": {
        "id": "OCDC_-uhhLcz"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 安裝 Streamlit\n",
        "pip install streamlit\n"
      ],
      "metadata": {
        "id": "iXnT1mFwLMJZ",
        "outputId": "a44a1ec0-1244-4ccd-dd8b-b8182738dd1b",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 106
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "SyntaxError",
          "evalue": "invalid syntax (<ipython-input-10-f7d3930f599d>, line 2)",
          "traceback": [
            "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-f7d3930f599d>\"\u001b[0;36m, line \u001b[0;32m2\u001b[0m\n\u001b[0;31m    pip install streamlit\u001b[0m\n\u001b[0m        ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
          ]
        }
      ]
    }
  ]
}
