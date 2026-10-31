# 先看这些真正变好的地方

解释更具体，少重复、少替论文辩护，也不把尚未证实的比较写成实验事实。原本清楚的图注、听测稿和技术细节保留。**正文未改；这里是供你选择的提案。**

下面六处可先看。完整准确原文、英文与连读语境在[最终段落对照](FINAL_PASSAGES_REVIEWED_v5.md)。

## 把piano roll的理由说具体

先说regular grid保留什么音乐关系，再解释它怎样对应卷积；没有声称所有event models都不如它。

<details><summary>当前论文原段 → 推荐英文</summary>

修改前：
```latex
This motivates the image-based view adopted in the present chapter. By treating symbolic MIDI as a sparse image and velocity as a colourisation target, the model can exploit local polyphonic structure more directly. U-Net and attention mechanisms are already successful in related music and audio tasks, but the present setting is distinct because it is purely symbolic and does not rely on acoustic input \cite{he2025filling,kim2024method}. This makes the chapter a natural starting point for the broader thesis.
```

推荐：
```latex
We use a piano roll to place simultaneous notes and local pitch--time neighbourhoods on a regular grid for the convolutional U-Net. The input is binary; the single-channel output supplies velocity values, so colourisation is an analogy for adding dynamics to existing notes. A note-list representation would require a different model interface \cite{he2025filling,kim2024method}.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#t03)。

## 不替作者添加实验历史

保留使用Huber的数学理由；尚未证实优势，不等于从未做过比较。

<details><summary>v4提案末句，不是作者原话 → 推荐英文</summary>

修改前：
```latex
We did not conduct a dedicated comparison with MAE.
```

推荐：
```latex
We chose Huber for its smooth gradients near zero and L1-like penalty for large residuals. We have not established an advantage over MAE.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#t11)。

## 保留结果，收准指标推理

两种similarity都把GT排在flat之上；gap本身不能确立哪个更敏感。

<details><summary>当前论文原段 → 推荐英文</summary>

修改前：
```latex
To test dynamics sensitivity, $\Delta(\mathrm{GT} - \mathrm{Flat\,64})$ asks whether a metric can distinguish expressive resynthesis from a flat one. Among the similarity metrics, Pearson $r$ produces the larger separation on both BSSL ($+0.118$) and BSTL ($+0.263$). Cosine similarity also orders GT above flat, but it severely compresses the margin ($+0.052$ on BSSL and $+0.047$ on BSTL), proving \emph{insensitive} to fine dynamics differences.
```

推荐：
```latex
Both similarity metrics score GT above flat velocity in this diagnostic. Their numerical GT--flat gaps do not by themselves establish which metric is more sensitive to dynamics.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#n01)。

## 换SoundFont不等于只改gain

写清保持notes和velocities、改变rendered sound；数字留在表里，不重复抄写或重算。

<details><summary>当前论文原段 → 推荐英文</summary>

修改前：
```latex
To evaluate renderer robustness, $\Delta\lvert\mathrm{Sal.} - \mathrm{YDP}\rvert$ asks whether a metric is stable when the rendering SoundFont is swapped while the underlying note velocities are kept the same. Here, MAE proves \emph{over-sensitive} to absolute gain: it drifts by $0.193$ on BSSL and $1.723$ on BSTL, substantially more than the corresponding drift on $r$ ($0.034$ and $0.011$). On real recordings, this drift would conflate dynamics differences with renderer choice and make the evaluation unreliable.
```

推荐：
```latex
Changing from Salamander to YDP retains the GT notes and velocities but changes their rendered sound. This comparison tests the renderer change as a whole, rather than gain alone.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#n02)。

## 保留范围，删除自我辩护

boundaries原首句胜出；不把scope重新分类成缺陷。

<details><summary>当前论文原段 → 推荐英文</summary>

修改前：
```latex
The thesis has several boundaries. These boundaries are not artefacts of unfinished implementation; they follow from the problem definition and from the representational choices made throughout the dissertation.
```

推荐：
```latex
The thesis has several boundaries.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#n05a)。

## 两个术语，一次讲清楚

明确note content and timing；把数据状态与学习监督分开，仍允许重叠。

<details><summary>v4解释稿 → 推荐英文</summary>

修改前：
```latex
In this thesis, incomplete data lack the dynamics layer of interest, whereas weakly expressive data contain that layer only in a simplified form, such as constant or coarsely quantised MIDI velocities. Weakly supervised settings lack reliable target labels for direct training; Chapter 6 instead uses real audio and a renderer-based comparison to supervise the velocity estimator indirectly. These terms describe the available information rather than the quality of the musical performance. These conditions can overlap in the same dataset.
```

推荐：
```latex
Here, weakly expressive data retain note content and timing but have simplified dynamics, such as constant or coarsely quantised velocities. Weak supervision refers to learning without reliable direct dynamics labels, using indirect evidence such as the renderer-based supervision in Chapter~\ref{ch:beyondpiano}. These conditions can overlap.
```

</details>

[看准确范围和上下文](FINAL_PASSAGES_REVIEWED_v5.md#t01)。

<a id="keep-list"></a>

## 这些继续保留

- Fig6.2原图／图注：已经写明SoundFont-rendered targets。
- v4听测结果稿：具体比较对象、mean similarity和11位听者／8段／一个renderer范围清楚。
- 现有技术章节结构、O/F/V分工、公式、参数和实测数字。
- 结论中的boundaries原首句。

## 最后两处整合也已修好

Chapter3 roadmap不再出现“Supported…supported”重复；指标表GT−Flat行不再共用向上箭头，因为相关系数的有利差为正、MAE的有利差为负。所有数字保持原样。

## 仍需事实确认

正式送审PDF、听测timing处理、实际run／checkpoint／表源、guitar Fig6.3 GT和最终ICASSP版本仍待确认。R1-13/21/26/30没有因文字更顺而结案。旧YES不自动批准新稿；只读浏览也不会写入决定。

[完整段落](FINAL_PASSAGES_REVIEWED_v5.md) · [具体范围与依赖](DEPENDENCIES_REVIEWED_v5.json) · [复核和来源证据](FINAL_WRITER_EVALUATOR_AGREEMENT_v5.md)
