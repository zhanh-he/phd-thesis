# Writer/evaluator 对指定提案文字的一致记录

**可供作者选择；不是作者批准、正文实施或run/GT认证。** 最终reader输入的文字及范围已完成协调，UI／交互验收仍由reader整合者完成；不沿用旧五卡测试结果。

第一次外部评阅后的七处R2选文已获第二次外部评阅接受。本次只采用已评阅的两项精确整合修正，无第三轮风格改写。20项选文的英文hash与外部C2 verdict逐一相同。

## 两项明确采用的修正

1. `V4-R2-04-sync-3`：扩大原文范围，包含`Supported by listening tests, `；新句首用`It`。保留positive result和objective/listening证据，删同句重复。没有新增第45个重叠补丁。
2. `N07`：采用外部提供的准确corrected table副本，去掉GT−Flat行共用向上箭头。表内58个numeric tokens顺序不变；0.193仍是报告值，不重算。

## 最终组合与绑定

- `READER_PACKET_REVIEWED_v5.json` SHA-256：`9496ad5ece7f51e5de642c59fe0d547503e6eb7c77eb2376e34b8bad2f3c4c17`。

- `FINAL_SELECTION_REVIEWED_v5.json`：20个选文，只有`reinserted_context_final`作为当前上下文，移除会误导adapter的旧context字段。
- `DEPENDENCIES_REVIEWED_v5.json`：23项既有依赖，其中roadmap一项采用上述完整源范围修正；均仍未获作者批准。
- `N07_TABLE_MARKUP_REVIEWED_v5.tex`：与外部C2准确表格副本字节相同。
- `evidence/FINAL_OPERATION_MANIFEST_v5.json`：44项源操作，和R2相比恰好只有上述两项操作变化，无重叠。
- 八个内存组合文档的SHA-256与外部C2的corrected virtual overlay全部一致。没有保存或修改thesis源文件。

根`FINAL_DELIVERY_MANIFEST_v5.json`另绑定最终交付文件及其hash。Writer确认采用已评阅精确修正，外部历史verdict中的writer-pending字段作为历史保留，不被回填。

## Reader必须保留的边界

- 六卡只是精选只读入口，不能充当44项执行manifest。
- N01卡是N01/N02/N03＋N07＋N04五范围一致性组，完整文本同源。
- N05b/c是独立可选项；最终export不再将它们挂作N05a自动followthrough。
- 其余v4依赖是明确的组合预览假设，不继承旧YES。
- `jointly-reviewed-v5`只表示指定提案文本达成writer/evaluator一致，不表示author approval。
- reader来源必须是本次`FINAL_SELECTION_REVIEWED_v5.json`和`reinserted_context_final`，不能读冻结的早期FINAL_SELECTION或R2旧字段。

## 核验依据

外部报告：`evaluator_cycle1.md`、`evaluator_cycle2.md`及`evaluator_cycle2_verdict.json`。两项修正依据：`evaluator_cycle2_two_repairs.diff`、`evaluator_cycle2_dependencies_corrected_proposal.json`、`evaluator_cycle2_N07_corrected_proposal.tex`。Writer有界核验在`evidence/FINAL_WRITER_VERIFICATION_v5.json`；独立最终完整性报告随后作为单独证据保存。

此前内部C1/C2与父级报告的bounded GPT-6.1-sol excerpt review继续各自归属，不冒充外部完整审查轮次或全文认证。

正式送审基线、R1-13/21/26/30、run/checkpoint/table provenance、guitar GT、最终ICASSP版本继续开放。没有编译、实验、外传、commit/push、publication或正文实施。
