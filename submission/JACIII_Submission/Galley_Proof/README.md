# 校样阶段（Galley Proof）记录

**论文**：Jc26-0016, JACIII Vol.30 No.6（预定 2026-11-20 出版）
**阶段结果**：校样修改全部被编辑部采纳，2026-10-23 确认无进一步修改，等待定稿出版。

## 时间线

| 日期 | 事件 |
|---|---|
| 2026-06-22 | 英文润色稿返回编辑部（correction0.zip） |
| 2026-10-14 | 收到第一版校样 gal0（截止 10-21），编辑部提问：作者简介 `????` 年份、Visual Abstract |
| 2026-10-14 前后 | 编辑部回复单位问题：标题下单位保持研究期间单位，现单位可加入作者简介 |
| 2026-10-21 | 提交 Author Feedback + 3 个文件（图 6、图 7、修订版作者简介） |
| 2026-10-22 | 收到第二版校样 gal1，编辑部确认全部按要求修改 |
| 2026-10-23 | 严格核对 gal1（17 页逐页文字、坐标、位图哈希、像素对比）后回复无进一步修改 |

## 提交给编辑部的修改（见 `author_feedback_round1_2026-10-21.txt`）

1. **作者简介年份**（编辑部问题 1）：Amena 2012 / 2020 / 2025- / 2026-；Takaoka 2015- / 2019-
2. **Visual Abstract**（编辑部问题 2）：图 1，说明 "Dual-stream fusion of text and MeSH"（35 字符）
3. **替换图 6、图 7**：
   - 图 6：绿柱原为 Best TC + Best TD 相加（1.3630 / 1.3371 / 1.3219 / 1.2826，两者出现在不同 (α, β)，
     不对应任何实际配置），改为表 2 的 Best TC+TD（1.3443 / 1.3247 / 1.3005 / 1.2331）。
     旧图使 Dual BioBERT 看似高于基线，与正文 −1.6% 矛盾。
   - 图 7：旧图含 `generate_pdf_figures.py` 中未替换的**占位数据**（A3 0.50/0.60、A4 0.55/0.68，
     脚本注释 "Update these numbers once the actual ablation results are confirmed"）及与表 4 不符的配置标签，
     改为完全按表 4 绘制。
   - 两张图**只改数据**，版式、配色、图例位置保持原样；正文、表格、图注无需任何修改，未引入新结果。
4. **修订版作者简介**：补年份；Amena 简历加入 E-JUST（编辑部实际只加在简历行，Affiliation 栏未加，判断可接受）
5. **Amena 代表作年份**：IEEE Access Vol.12, pp. 1865-1879 由 2023 改为 2024（Crossref 核实，
   DOI 10.1109/ACCESS.2023.3334641 中的 2023 是在线年份）

## 刻意未提的问题（作者决定"尽量不改"）

- 5.2 节首句 "significant improvements … across all evaluated metrics" 与 Dual BioBERT −1.6% 不完全一致
- 排版把 "per-topic coherence" 缩写成 "Per-TC"
- 3.3 节引用 [19]（图嵌入主题模型）不能支撑"句向量模型可处理未预处理文本"
- Qwen 模型名三处不统一；Data Availability 前后矛盾（"按需索取" vs "已在 GitHub 公开"）

## 本目录文件

- `Fig6_fig_model_comparison_bar.pdf`、`Fig7_fig_ablation_comparison.pdf`：提交的修正图（已被采用）
- `regen_fig6_fig7.py`：生成上述两图的脚本（基于 `experiment/generate_pdf_figures.py`，只改数据）
- `author_feedback_round1_2026-10-21.txt`：第一轮 Author Feedback 全文
- `author_feedback_round2_2026-10-23.txt`：第二轮确认回复

`experiment/generate_pdf_figures.py` 已同步修正，`fig/` 下两张图也已替换为修正版；
`Final_Submission/` 与 `Submission_Revised/` 保留当时提交的原样作为历史记录。

校样 PDF（publisher proof）与含合著者照片和履历的作者简介 docx 未放入本公开仓库。
