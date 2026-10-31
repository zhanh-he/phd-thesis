# 阅读层v2：交接与独立复核入口

状态：阅读层与三项补充已通过contextual_review_v4的独立定点复核；两处指定入口修正已按准确文字实施在提案文件中。不是作者批准，也未实施thesis修改。候选英文仍绑定冻结第三轮。本页供编辑和审查者，不要求作者阅读。

## 新阅读路径

`START_HERE.md → CHANGE_CARDS_v2.md（按需）→ DECISIONS.md（唯一输入）`。

入口以“局部澄清、保留结构与实测结果”的编辑判断开头，按四组实质改动展示五组原文／拟稿节选，小修另置一段。每组下一层映射到全部相关ID，分列作者原立场与编辑推荐，直接链接决定行和完整英文。主入口只要求先指出正式送审版本；记录问题统一留在原事实字段。

## U01–U08 修复对应

| 诊断 | 本次可检查的实际修复 |
| --- | --- |
| U01 | DECISIONS过期第二轮绑定改成明确历史记录；当前均绑定冻结第三轮。R2-05明确只改358行，R1-20另改71行。 |
| U02 | R1-27版本字段直接提供“Ch5 A＋Ch7 C／自定组合（注明各章）”；两处全文放在卡页。R1-18／R1-37变为镜像说明，不再出现独立输入。 |
| U03 | R1-13仅A前五句；R1-21仅A应用段；R1-26仅A前三句；R1-30仅B目的段。各行和卡页均明确不包含的事实句／protocol。 |
| U04 | loss入口先展示averaged terms／相对1:1；听测先展示U-Net高于Flat/ConvAE的原观察，再给范围。 |
| U05 | 关键例子同屏说明评审要求／作者原答复／原拟差别；未找到原答复明确注明。R1-32可展开两段完整old对两段new，参数保留。 |
| U06 | 合并包改称单一方案包，提示22／32是方法说明；八项准确来源和唯一稿均可展开；单一稿不要求另选字母。 |
| U07 | 首屏仅要求正式基线；四项局部可选句与冻结事实集中一处；完整V01–V07仍在原ledger，不把它们当今晚必答项。 |
| U08 | 入口不放轮次／hash／行政计数；README顶端指向新入口，旧索引与历史文件保留。 |

## 保留与校验边界

- writer_round3.md SHA256仍为`1a658584d35ee50580dd2dfd6eb9d0afdac1b573404edbacf3e475a79250c75e`。未改候选或审查结果。
- DECISIONS写入前核对原hash`34ab3d9f6601f347e0df5a1fb5e06bd921bfcf84fe5c34d2e35406c543e4fe9a`，当时43行决定／版本、所有备注和事实字段均未填写。原始字节快照保存在`history/DECISIONS_before_readability_v2.md`；此快照不接受新决定。当前DECISIONS原备注、全局字段和历史包字段逐字保留。
- 新阅读分组覆盖43个ID，每个恰好一次；它们是阅读导航，不是五个批量YES。共享段落仍只决定一次。
- 入口10处英文节选已逐字核对JSON来源／候选；听测节选的省略号明示省略，完整段保留引文。
- 未读取otherfiles，未修改thesis源、论文PDF、原回复、Bib、冻结writer或reviewer文件。没有新增实验、编译、Git操作、上传或公开发布。
- 旧ZIP仍是此前快照，尚未包含本层；不要把旧ZIP当作本次阅读层的交付件。

## 新语境建议（整合前的历史记录）

已读`contextual_audit_v4.md`：三组新增文字（Intro的velocity定义、S3/beyond-piano范围、data-curation末句）及R1-35 KEEP倾向仍待独立定点复核。为避免把未审文字说成已通过，本阅读层暂未将其混入冻结推荐。复核完成后可按原ID加清晰的补充选择，不自动继承作者YES。

## 技能与格式

已读Documents技能及writing_quality.md并按其具体、读者优先、忠实不确定性的要求处理。选定环境的cloud与executor技能目录全页、现有工具名及本地skills／plugin缓存查询均未找到`orbit:writing-style`；不能声称已读。此缺项未阻止用thesis原声与已核验候选改善入口。

仅交付Markdown；未启动HTML、DOCX或PDF格式工作，也没有额外渲染／上传步骤在运行。Space／Library上传授权仍未收到，本轮不尝试上传。

## 给独立复核者的最小检查

1. 直接读START_HERE，判断作者是否能先理解“改什么、为什么、保留什么”。
2. 抽查四项局部YES：英文范围是否准确、事实是否仍冻结；检查27／37和17／18组合不冲突。
3. 检查DECISIONS选择语义、链接和源身份；确认没有填YES、NO或事实答案。
4. 新语境三组若通过，再独立指明可加入的具体补充与KEEP选择，不把整轮重新打开。

最终状态以独立复核文件及本页后续记录为准；本页生成本身不等于复核完成。

## 初次生成后的校验（历史记录）

阅读层已可供最终QA：300个本地文件／锚点链接全部通过；43个ID均有且仅有一组导航；43行原备注逐字保留，未填任何YES／NO；128/128源文件hash未变。记录见[evidence/readability_v2_validation.json](evidence/readability_v2_validation.json)。独立可用性复审尚待结论。

## 早期独立走查后的修复

coverage_audit核对四项局部句与冻结JSON一致，确认组合／镜像与作者备注保留。其四条建议已落实：R1-09改引原批注；R1-24作者列仅述multi-scale／便利；R1-11明确指Ch3；四项局部YES直接绑定准确句，不再要求另填字母。此为早期质量检查，父线程最终独立QA仍待结论。


## 最后整合：按定点复核收住

已读完整contextual_review_v4.md，只合入其三项accepted-for-author-choice补充、R1-35 KEEP和明确的入口修正。START_HERE仍为四组主线，不另开文风改写。新英文与原文操作记录在SUPPLEMENTS_v4及evidence/supplements_v4.json；旧冻结候选保持字节不变。

README和REVIEW_SUMMARY统一指向START_HERE，旧内容留history；RECOMMENDED_PREVIEW标明资料页。GRS只加必要的补充交叉引用与已复核KEEP事实说明，未把新补充写成既成修改。DECISIONS三项补充独立待选，R1-35提供KEEP／原A两个选项；每个原作者备注与事实字段保留。

已采用父线程提供的writing-style指导：小修保留原句、thesis prose依据用户自身实例、作者立场与编辑判断分开、不新增承诺／结果。没有声称读取本环境仍缺失的orbit技能文件。

当前新ZIP为thesis_revision_proposals_20261031_readability_v2.zip；旧ZIP保持原字节。新包以START_HERE为唯一阅读入口，历史快照只审计，不接受选择；源码／大体积证据仍在原项目，不随精简包复制。没有上传、公开发布或源文修改。
