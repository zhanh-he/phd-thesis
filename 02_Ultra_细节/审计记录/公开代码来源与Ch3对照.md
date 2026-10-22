# 公开代码来源与 Ch.3 对照

2026-10-22，只读核查，未执行所取源码。公开源码用于补充实现证据，不能静默替代指定的主论文版本。仅通过官方 GitHub API/raw 读取相关小文件；未 clone、未安装依赖、未下载 checkpoint、未登录 WandB、未运行训练或推理。

## 固定来源

仓库 [zhanh-he/midi-velocity-colorizer](https://github.com/zhanh-he/midi-velocity-colorizer)，本次 main 固定到 `53e1b950a89fc5915f07703a228986ff00b64a83`。相关源文件与 API tree/commit 元数据已留在[本地快照](公开源码_Ch3_53e1b950/本地快照清单.json)，每个文件有 SHA256。以下行号均为该 commit 的源文件行号；不把今天的 main 自动当作 thesis 表格的运行版本。

## 1. attention 参数的空间含义有了源码证据，表格映射仍未确认

**已由代码/数据确认（这份公开实现）。** [main/models.py:270–340](https://github.com/zhanh-he/midi-velocity-colorizer/blob/53e1b950a89fc5915f07703a228986ff00b64a83/main/models.py#L270) 将 `window_size` 用于高度/宽度整除、padding 和 `window_size²` 局部 attention 计算；它是空间尺寸，不是沿两轴的 partition 数。数值1对应每个空间区域只有1个位置，不能直接称跨空间的 global attention。这一判断限于代码结构，不验证 forward 的全部数学正确性。

**已由原文确认。** 主论文 `Zhanhong_He_PhD_Thesis_v0.pdf` §3.5.1，印刷 p.42／PDF p.69 以 n×n 窗口描述；§3.8，印刷 p.46／PDF p.73 又称1×1为 global，Table3.4，印刷 p.48／PDF p.75 报若干标签。

**待作者确认。** Table3.4 各行究竟对应哪份 run/config/commit，尤其表中1×1、2×2、4×4、8×8是否与这份类同义。不能直接把表的1×1数字重新归入某个未验证模型；正式稿先采用条件说明。无需为确认标签而重训。

## 2. input 和 loss 的公开默认配置与 v0 不完全一致

**已由代码/数据确认（这份配置的分支）。** `conf/config.yaml:28` 为 `onset_mask=True`；[main/models.py:35–49](https://github.com/zhanh-he/midi-velocity-colorizer/blob/53e1b950a89fc5915f07703a228986ff00b64a83/main/models.py#L35) 由此选择 `gt_onset` 作 U-Net 输入。v0 §3.4.1，印刷 p.41／PDF p.68 则明确写 F 为 network input。配置可以被覆盖，因此不能断言论文实验实际用了 onset 而不是 frame；需要保存的 resolved config。

**已由代码/数据确认（这份配置的 loss 分支）。** `conf/config.yaml:37–41` 选择 `element_wise` mask、u_shape weighting、cosim=0.2；[main/loss.py:8–58](https://github.com/zhanh-he/midi-velocity-colorizer/blob/53e1b950a89fc5915f07703a228986ff00b64a83/main/loss.py#L8) 在 element-wise 分支先把选中元素展开，再对 BCE 取 mean，并在当前张量最后一维计算 cosine。v0 Eqs.3.3–3.5，印刷 p.43／PDF p.70 写 pitch-wise CosSim 平均和 TP 分母。两者不是仅靠换术语就可视为相同公式；也不应未经 run 映射直接用公开默认配置改论文公式。

**合理解释但未验证。** 这些差异可能来自公开版本演化、运行覆盖参数、论文公式简化或写作误差。当前不选择其一作事实，也未推断它们改变了已报告指标多少。

**最小解决办法。** 为 Ch.3 提供论文对应 run ID、代码 commit、resolved config 与表3.4行的对应清单；至少包含 input=onset/frame、attention 参数语义、mask/reduction/cosine维度。记录在关键核查的同一“实现/协议资料包”，不增加训练要求。

## 出版状态：独立核对的范围

- CMMR：作者 [arXiv v2](https://arxiv.org/abs/2508.07751v2) 列 CMMR2025 pp.949–960 与相关 DOI；[UWA 研究记录](https://research-repository.uwa.edu.au/en/persons/zhanh-he/) 也列为 peer-reviewed conference paper。与主论文 Authorship Declaration，印刷 p.v／PDF p.8 相符。
- SMC：截至2026-10-22，[官方 programme](https://smc26.mbz.hr/index.php?act=mlist&id=8&opt=item) 列于11月6日 Session4 item7。可写 accepted/scheduled；不能因它列入programme就说已在未来会期报告或正式出版。作者较早的 arXiv comment 仍为 submitted，不优先于更新的正式programme和论文声明；最终 proceedings 元数据另核。
- ICASSP：[官方 paper 5161](https://www.cmsworkshops.com/ICASSP2026/view_paper.php?PaperNum=5161&bare=1) 列5月7日报告；[UWA 已发表条目](https://research-repository.uwa.edu.au/en/publications/joint-estimation-of-piano-dynamics-and-metrical-structure-with-a--2/) 列 published、DOI `10.1109/ICASSP55912.2026.11460839`。日期/页码以最终条目为准，不混用 preprint record。
- ISMIR：作者 [arXiv v1](https://arxiv.org/abs/2608.08985v1) Comments 明确 Accepted to ISMIR2026；报告1 p.2也确认可改 accepted。这支持更正 under review，但本轮未取得正式 proceedings 页码/DOI，不把预印本当正式出版记录。

以上为 **已由原文确认（公开一手来源）**。paper-to-thesis 每个新增实验/段落的归属仍需版本逐项对照，不由出版状态自动推得。公开资料内容的核对没有把评审细节上传到任何网站。
