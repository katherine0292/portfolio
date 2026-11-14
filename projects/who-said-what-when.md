[← Portfolio](../README.md) · [中文总览](../README.zh-CN.md)

# Who Said What When

**Evaluate who spoke, what they meant and when the evidence occurs.**

![Conversational audio and supporting evidence](../assets/previews/who-said-what-when-benchmark.png)

| | |
| --- | --- |
| Focus | Speaker-attributed, temporally grounded question answering for conversational audio |
| Work represented | Task framing, two-round annotation workflow, data formats, validation and scoring tooling |
| Tools | Python standard library, JSONL, JSON Schema |
| Delivery | 0.1.0 pilot with 25 items from 5 source videos; 178 annotated turns |

## Problem and direction

An answer can sound plausible while assigning a guest's claim to a host, dropping a qualification or pointing to the wrong audio passage. This benchmark keeps the speaker, meaning and evidence relationship explicit.

Given conversational audio and a question, a system returns a clip-local speaker ID, an answer and supporting intervals. Evidence may occupy several separated passages.

## Design and implementation

- **Structure the annotation in two rounds.** First record speakers and turns; then write questions and connect key points to supporting passages.
- **Separate inputs from evaluator material.** References, source identities and audit records remain outside model-facing inputs.
- **Score actual interval sets.** Temporal IoU uses the union of supporting intervals, so an unsupported gap reduces the score.
- **Keep meaning evaluation explicit.** A separate judgments file grades key points and contradictions. Joint Pass requires correct speaker, sufficient time overlap and full meaning credit.
- **Make the workflow reproducible.** Validation, diagnostic baselines and scoring run with the Python standard library, without downloading media or calling a model.

## Evidence and current scope

The default evaluation covers **18 text-aligned items**. Another **7 need priority media review**. All 25 await independent listening review, and the release has **0 gold items** and no held-out test set.

Bundled duration-only baselines provide reproducibility checks. They do not establish a model leaderboard. Meaning and joint scores need their grading coverage reported. Original media and verbatim transcripts are not bundled; the source repository documents access and permission limits.

The pilot demonstrates the evaluation workflow and error analysis. Expansion, independent review and frozen splits remain future work.

## Explore

- [Interactive walkthrough](https://katherine0292.github.io/who-said-what-when-benchmark/)
- [Project repository](https://github.com/katherine0292/who-said-what-when-benchmark)
- [Data card](https://github.com/katherine0292/who-said-what-when-benchmark/blob/main/docs/DATA_CARD.md)
- [Annotation guide](https://github.com/katherine0292/who-said-what-when-benchmark/blob/main/docs/ANNOTATION_GUIDE.md)
- [Benchmark protocol](https://github.com/katherine0292/who-said-what-when-benchmark/blob/main/docs/BENCHMARK_PROTOCOL.md)
- [Scorer](https://github.com/katherine0292/who-said-what-when-benchmark/blob/main/wsw/score.py)

**中文摘要：** 对话音频问答评估 pilot，将说话人、含义与时间证据分别测量后再联合评估。当前共 25 条，默认使用 18 条文本对齐数据；全部仍待独立听审，不用于可靠的模型排名。

[Source snapshot and preview provenance](../docs/SOURCES.md#who-said-what-when-benchmark)
