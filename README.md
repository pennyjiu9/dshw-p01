# P01：金融数据获取、管理与初步分析

## 股票列表

| 代码   | 名称     | 行业   | 选股理由                                   |
| ------ | -------- | ------ | ------------------------------------------ |
| 002142 | 宁波银行 | 银行   | 优质城商行代表，成长性好，资产质量优异     |
| 600036 | 招商银行 | 银行   | 零售银行龙头，ROE 长期领先同业             |
| 002594 | 比亚迪   | 汽车   | 新能源汽车龙头，技术壁垒高，成长性强       |
| 600048 | 保利发展 | 房地产 | 央企地产龙头，财务稳健，市占率持续提升     |
| 000063 | 中兴通讯 | 通讯   | 5G 设备龙头，受益于通信基础设施建设        |
| 600487 | 亨通光电 | 通讯   | 光纤光缆及通信网络龙头，受益于数字经济发展 |
| 600519 | 贵州茅台 | 白酒   | A 股股王，品牌护城河极深，盈利能力强       |
| 300750 | 宁德时代 | 能源   | 全球动力电池龙头，新能源赛道核心标的       |
| 600900 | 长江电力 | 能源   | 水电龙头，现金流稳定，防御属性强           |
| 002352 | 顺丰控股 | 物流   | 快递行业龙头，高端物流服务差异化竞争优势   |

**行业覆盖**：银行、汽车、房地产、通讯、白酒、能源、物流（共 7 个行业，满足至少 5 个行业的要求，每个行业至多 2 只）

## 数据来源

- **股票行情**：`akshare`（`ak.stock_zh_a_hist()`），后复权（`adjust='hfq'`），日度数据，时间范围 2020-01-01 至今
- **市场指数**：
  - 沪深 300（000300）：CAPM 市场基准
  - 上证指数（000001）：A 股综合市场参考，覆盖面更广
- **宏观指标**：
  - CPI 同比增速：`akshare`（`ak.macro_china_cpi_monthly()`），月度数据
  - **选择 CPI 的理由**：CPI 反映通货膨胀水平，影响央行货币政策取向，进而影响股市整体估值水平和资金成本
  - M2 同比增速：`akshare`（`ak.macro_china_money_supply()`），月度数据
  - **选择 M2 的理由**：M2 反映市场流动性宽裕程度，与股市资金面密切相关，M2 增速变化往往领先于市场走势
- **财务数据**：`akshare`（`ak.stock_financial_abstract()`），获取 ROE 和净利润率

## 存储方式

- **基础（方式 A）**：CSV 格式存储所有原始数据及清洗后的综合数据
  - **CSV 的优点**：通用性强，任何文本编辑器均可打开，与 Pandas 兼容性好，可读性强
  - **CSV 的不足**：无 Schema 约束（类型信息丢失），不支持列式读取，大文件时读取速度慢，不支持嵌套数据
- **进阶（方式 B）**：Parquet 格式
  - **选择 Parquet 的理由**：列式存储格式，支持高效的压缩和编码，可选择性读取所需列，自带 Schema 信息，适合大规模数据的存储和分析

## Quarto 电子书

本项目已整理为在线电子书，可通过以下链接访问：

**https://pennyjiu9.github.io/dshw-p01/**

电子书包含目录导航、各章节标题、图表和分析文字，排版整洁。

## GitHub 仓库

https://github.com/pennyjiu9/dshw-p01

## 如何运行

1. **安装依赖**：

   ```bash
   pip install -r requirements.txt
   ```

   或在已创建好的虚拟环境中安装：

   ```bash
   conda activate dsfin_py311
   pip install -r requirements.txt
   ```
2. **运行 `01_download.ipynb`**：下载原始数据（个股行情、指数、宏观指标、财务数据）

   - 所有原始数据保存至 `data/` 目录下的对应子目录
   - 下载日志记录于 `download_log.txt`
3. **运行 `02_clean.ipynb`**：清洗数据并存储

   - 完成缺失值处理、日期格式化、类型检查、重复值处理、离群值标注
   - 宽表/长表转换演示
   - 多表合并（股票 + 指数 + 宏观数据）
   - 保存为 CSV（`data/combined/combined_data.csv`）和 Parquet（`data/clean/stock_clean.parquet`）
   - 对比 CSV 与 Parquet 的读取速度和文件体积
4. **运行 `03_analysis.ipynb`**：描述性统计与回归分析

   - 计算 10 只股票日收益率的描述性统计量
   - 生成 4 张必做图形（归一化走势、收益率分布、相关系数热力图、宏观-市场关系）
   - CAPM 模型估计与讨论
   - 所有图形保存至 `output/` 目录
5. **导出报告**：

   ```bash
   jupyter nbconvert --to html 03_analysis.ipynb --output report.html
   ```

   打开 `report.html` 阅读完整分析报告

## 目录结构

```
dshw-p01/
├── README.md                    # 项目说明
├── report.html                  # 分析报告（由 03_analysis.ipynb 导出）
├── requirements.txt             # 依赖库列表
├── .gitignore
├── 01_download.ipynb            # 数据下载
├── 02_clean.ipynb               # 数据清洗
├── 03_analysis.ipynb            # 描述统计与回归分析
├── download_log.txt             # 下载日志
├── data/
│   ├── stock/                   # 个股行情原始数据（CSV）
│   ├── index/                   # 指数数据（CSV）
│   ├── macro/                   # 宏观数据（CSV）
│   ├── finance/                 # 财务数据（CSV）
│   ├── clean/                   # 清洗后数据（CSV + Parquet）
│   └── combined/                # 合并后综合数据
└── output/                      # 图形输出（PNG）
```

## 项目说明

- 本项目使用 Python 代码自动创建目录结构（`os.makedirs`），无需手动新建文件夹
- 数据清洗后的综合数据（`data/combined/combined_data.csv` 和 `data/clean/` 下的文件）已上传至仓库，方便直接查看分析结果
- 原始行情数据（`data/stock/`、`data/index/`、`data/macro/`、`data/finance/`）体积较大，可通过运行 `01_download.ipynb` 重新下载
- Parquet 格式的进阶存储演示位于 `02_clean.ipynb` 末尾

## 提交清单

- [X] 项目根目录名称为 `dshw-p01`，目录结构由 Python 代码自动创建
- [X] `README.md` 完整，含股票列表、数据来源、存储方式说明、GitHub 仓库链接、运行步骤
- [X] `download_log.txt` 存在，记录所有数据的下载状态
- [X] 3 个 Notebook 均可从头到尾完整运行
- [X] 方式 A（CSV）已完成；方式 B（Parquet）已完成并有对比说明
- [X] 数据清洗 6 个步骤均完成，每步有文字说明
- [X] 图 1-4 均已完成，保存至 `output/`，每图有文字解读
- [X] CAPM 回归表格存在，三个讨论问题均有文字回答
- [X] `report.html` 存在于根目录，可独立阅读
- [X] `.gitignore` 配置正确
