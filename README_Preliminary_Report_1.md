<!-- 本文完整保留 PDF 的全部评审文字与 25 条回复批注。只调整 Markdown 排版、合并印刷换行；无回复处统一标为 zhanhong not response yet。学校徽标和手写签名为图像，不在此作文字转写。 -->

# Report on the PhD thesis of Zhanhong He entitled:

## “Recovering Musical Dynamics for Expressive Automatic Music Transcription”

*24 September 2026*

Dr Emmanouil Benetos  
Reader in Machine Listening  
School of Electronic Engineering and Computer Science  
Queen Mary University of London  
Mile End Road, London E1 4NS  
Tel: +44(0)20 7882 6206  
Email: emmanouil.benetos@qmul.ac.uk  

## Introduction

Zhanhong He has provided a PhD thesis which consists of 154 pages, 127 of which make up the main body of the text which consists of seven chapters. The core methodological chapters are chapters 3-6, with the first two providing an introduction and background and the last chapter being the thesis conclusions. Overall the document is well written and clearly organised, with no comments on the overall chapter structure. In terms of citation style, I would suggest to use an author-year format which improves readability given a lack of space constraints. The use of language and the overall presentation of the text is excellent. In general the thesis is of high quality and was a pleasure to read.

**Zhanhong’s response:**

> zhanhong not response yet

Three works carried out by the candidate have been published as peer-reviewed papers at the CMMR 2025, SMC 2026, and IEEE ICASSP 2026 conferences respectively, and one work has been accepted for publication at the ISMIR 2026 conference. This shows good research productivity and consistency on publishing the outputs of Zhanhong’s PhD research to the music computing and MIR communities. All associated publications were carried out by Zhanhong as lead author with supervisors as co-authors.

**Zhanhong’s response:**

> zhanhong not response yet

## Thesis Evaluation

According to the six merit criteria set by the University of Western Australia:

### Criterion 1

The thesis of Zhanhong He as a whole is a substantial and original contribution to knowledge in the fields of music information retrieval and music signal processing (the latter particularly for the contribution in chapter 6).

**Zhanhong’s response:**

> zhanhong not response yet

### Criterion 2

As demonstrated by Chapter 2 of the thesis, but also throughout the thesis document, the candidate shows familiarity with, and understanding of, the relevant literature particularly on topics related to automatic music transcription and velocity prediction, and more broadly on topics related to music information retrieval and music signal processing (such as DDSP).

**Zhanhong’s response:**

> zhanhong not response yet

### Criterion 3

The thesis provides a comprehensive study of the topic of automatically recovering musical dynamics from music audio and machine-readable symbolic music representations, perhaps at a level not achieved before in the field.

**Zhanhong’s response:**

> zhanhong not response yet

### Criterion 4

The techniques adopted and proposed (primarily computational, related to machine learning and signal processing) are all appropriate to the subject matter of the thesis and are properly applied. In certain cases, as with most engineering works, there could be alternative techniques or minor suggestions on certain experimental settings; these will be detailed in the comments below.

**Zhanhong’s response:**

> zhanhong not response yet

### Criterion 5

For each of the core methodological chapters (3-6), there are well-designed experiments and evaluations using appropriate existing or newly proposed evaluation metrics; results are suitably set out in tables and figures, and there is a good level of discussion of experimental results. As with most PhD theses including a computational evaluation component, there can be minor suggestions for presentation of results or choice of experimental setup; these are detailed in the comments below.

**Zhanhong’s response:**

> zhanhong not response yet

### Criterion 6

The quality of English and general presentation are of a standard for doctoral thesis publication. The narrative in particular flows very well across and within chapters.

**Zhanhong’s response:**

> zhanhong not response yet

---

*Patron: Her Majesty The Late Queen Elizabeth II*

*Incorporated by Royal Charter as Queen Mary University of London*

<!-- Original PDF page 2 -->

## Specific comments and questions

Below are specific comments on the thesis manuscript, as well as topics to be discussed during the viva.

Preamble: Submitted ISMIR 2026 paper can now be marked as accepted for publication.

**Zhanhong’s response:**

> zhanhong not response yet

### Chapter 1:

#### 1.1

Figure 1.1 is captioned as a “general architecture of an AMT system”, however step 2 of the figure only takes into account dynamics and velocity estimation, and not other aspects of music performance (e.g. instrument identities, expressive playing techniques).

**Zhanhong’s response:**

> Yes, that’s a fair point. I forgot instrument identities and other expressive aspects from this figure. Final thesis, in this figure I will add them.

#### 1.2

Section 1.1, final paragraph: the term “recollecting” is ambiguous, perhaps “collecting” is more appropriate?

**Zhanhong’s response:**

> Yes, collecting

#### 1.3

Section 1.5: how do you define weakly expressive and weakly supervised music data?

**Zhanhong’s response:**

> Oops, Thanks, indeed I should add definition on that part.
>
> Weakly expressive is like "音符和时间信息已经存在，但目标力度层被简化，例如 MIDI velocity 全部设为默认值，无法保留逐音力度变化 (set to 64, or 8-labels scale quantization.)"
>
> Weak supervise is the missing of groundtruth labels, or low quality groundtruth.

#### 1.4

Table 1.2: would a scenario of converting performance audio to MIDI velocity also apply, particularly for the work done in chapter 6?

**Zhanhong’s response:**

> At current, I am success in Senario 2. We use a score-informed MIDI velocity estimation model because it performs better and provides a stronger pre-train model for adaptation.
>
> Normal MIDI velocity estimation, those without music score as prior, for example the hFT Transformer by Toyama ISMIR2023 is about 3 times MAE than our baseline system. So adapt these audio-only (S3) model with DDSP or DIff-SFProxy is good problem to explore, but we have not yet established.
>
> Current method is useful, As we demonstrated in Chapter 4, the audio–score misalignments won't affect much. So it works well.
>
> So it's good to explore border application. I believe.

### Chapter 2:

#### 2.1

Figure 2.1: does there need to be always a correspondence between the Perceptual level and the MIDI velocity level? Could there be a direct link between the Perceptual level to the Score Dynamics level?

**Zhanhong’s response:**

> Ture, but and False. This correspondence is about the instrument-specific tones, and Performer style. Like two different piano will give different sound with the same finger force. And, about the skill, this could said the piano pedal, and many other factor influence it. So it's false, because too many uncertainty.
>
> I would the Katerina Kosta's work, a "piano symbol" performance guidance resulted in sound is not always a soft. Her journal article also analyze this problem, and her ML model is better learn about the performer style instead of some kind of audio-to-loudness correspondence.
>
> Same finding in Kim’s work utilizing LLMs for midi-velocity-to-dynamic  translation

#### 2.2

Table 2.3 could benefit from inserting vertical lines to separate triplets of columns (1-3 vs 4-6 vs 7-9).

**Zhanhong’s response:**

> zhanhong not response yet

#### 2.3

Section 2.3.2: “MIDI [...] is attached to a note onset”. Does that always hold true for the MIDI protocol?

**Zhanhong’s response:**

> Yes a true

#### 2.4

Figure 2.3: In subfigures (e) and (f), it is not clear what do the different colours signify.

**Zhanhong’s response:**

> zhanhong not response yet

#### 2.5

Section 2.5: The term “humanisation” is unclear – I would suggest to either define or replace it.

**Zhanhong’s response:**

> zhanhong not response yet

#### 2.6

Section 2.6.1 could also discuss other score dynamics symbols, including crescendo and diminuendo.

**Zhanhong’s response:**

> zhanhong not response yet

#### 2.7

Table 2.7: should an “audio” column be included for those datasets which include audio recordings? The upper triangular symbol is unclear. Does the MIDI column include both performance (unquantised) MIDI and reference (quantised) MIDI? What does the “43%” refer to? Many of the above can be clarified in the table caption.

**Zhanhong’s response:**

> In my table, MIDI is unquantised real-performance data, and the score is quantised (somehow we call it score-MIDI). So 43% means the ATEPP only have 43% of recording provided the score, but all of them can use a AMT system to obtain MIDI.

#### 2.8

Section 2.8.3: It might benefit the background section if commonly used evaluation metrics for dynamics prediction are defined here.

**Zhanhong’s response:**

> zhanhong not response yet

### Chapter 3:

#### 3.1

Section 3.1: This work is mentioned as the “most controlled” in the thesis; however predicting dynamics from a score in the absence of any dynamics markings or velocity info is a more unconstrained problem than dynamics prediction given input audio (where dynamics are present).

**Zhanhong’s response:**

> Yes my mistake, my intend is to say "less input signal compared to others", but indeed less constrained. I will change my term.

#### 3.2

Section 3.1 and beyond: to what extent should MIDI Velocity completion be style-specific or composer-specific?

**Zhanhong’s response:**

> That's a great question, During my Dolby internship, we explored using style as a control parameter in a generative system. Composer could also be used as a coarse style label, for example “Chopin style” or “Beethoven style.”
>
> However, we were facing the data limitation, we don't have enough training data for composer/style control. So we changed our idea from " style control", to make a model can generalize to more data in different style. 
>
> You can see our human listening test analyse the "most-seen composer / unseen composer style" in train data, it exist a gap, but work well across those scenario.s.

#### 3.3

Section 3.2 and beyond considers the proposed work as “image-based”. Although there are some related figures with varying colours included in this chapter, I do not see any strong argument for using this term – the methodology does not treat dynamics as a colour channel or similar.

**Zhanhong’s response:**

> Good question. The idea originally came from image-processing papers, especially the use of U-Net and window attention. We use “image-based” because both the input and output are two-dimensional pitch–time matrices, processed with two-dimensional convolutions.
>
> The input is a binary piano roll, and the output is a single-channel velocity roll. We do not predict RGB colours. “Colourisation” is an analogy for adding velocity values to the existing note structure, it's good for general audiance understand, but I agree that the wording needs clarification.
>
> I would say the “image-like” is more proper. I will make revision.

#### 3.4

Section 3.3: The text and candidate could perhaps better justify the use of piano-roll as representation, as opposed to other MIDI-like representations (with lists of notes).

**Zhanhong’s response:**

> zhanhong not response yet

#### 3.5

Section 3.3: is this task about velocity recovery? Or velocity estimation?

**Zhanhong’s response:**

> At first is recovery, because it's how we make the training data. We delete those midi velocity from the given MIDI files. But the final task is the estimation, so shown our MAESTRO dataset trained model can perform well in SMD dataset.

#### 3.6

Section 3.4.1: could the input representation be in musical time as opposed to physical time? One might expect that velocity prediction in symbolic music might be more accurate using a beat-aligned representation.

**Zhanhong’s response:**

> Could be, but I guess it will be less expressive, as we know about the problem of quantization. We are not always input this model with the "real music score", sometimes, it could be AMT model result,. For example the  guitar-AMT model will not provide the velocity. Using our model in Physcical time, will be a great help.

#### 3.7

Section 3.6: The data used for experiments is performance MIDI, as opposed to reference (quantised) MIDI. Would that conflict with the main envisaged usecase which is on music composition?

**Zhanhong’s response:**

> I don't think so. We tried the model inference, and it actually works well in quantised MIDI scores we download from the internet. And our MOS test is based on the score-MIDI, which is quantised, double confirm it can work.
>
> Be honestly I understand this can make a further experiment, which make discussion deeper. 
>
> The true problem is Dolby will not happy for my "internship finished project" have further development" haha. So we keep it as current.

#### 3.8

Section 3.7: Baseline models could be presented in a separate subsection with more detail.

**Zhanhong’s response:**

> zhanhong not response yet

---

*Patron: Her Majesty The Late Queen Elizabeth II*

*Incorporated by Royal Charter as Queen Mary University of London*

<!-- Original PDF page 3 -->

### Chapter 4:

#### 4.1

Section 4.4: As part of the motivation for this work, it is stated that the proposed system isolates dynamics refinement from note transcription. Although practical, is this ecologically valid? Also, there is evidence that good velocity prediction can improve on note transcription performance, which would motivate linking both tasks and not isolating them.

**Zhanhong’s response:**

> zhanhong not response yet

#### 4.2

Section 4.5 and Figure 4.2: The use of piano-rolls for the proposed work could be further motivated; why not use event-based representations which are closer to MIDI?

**Zhanhong’s response:**

> because we want to use the multi-scale network. Event-based token transformer might have better methodologies, but piano-roll based is easier to build. Actually we tried a "multi-scale transformer" in time series research, which is failed, so I did not goes further.

#### 4.3

Section 4.5.3: Are both loss components balanced? Is there a need to weigh loss components?

**Zhanhong’s response:**

> This is the following work of a ISMIR2024 paper by Hyon Kim, he found this is the best ratio, and I verfied it. 
>
> I will directly cite his work to further explain this.

#### 4.4

The different experimental setups as presented in Table 4.1 are not clearly defined in the main text of the thesis.

**Zhanhong’s response:**

> zhanhong not response yet

### Chapter 5:

#### 5.1

Section 5.3: beyond the dynamics-related predictions made by the proposed system, did you attempt to combine these outputs with the outputs of a note-based AMT system as to have a complete AMT system?

**Zhanhong’s response:**

> zhanhong not response yet

#### 5.2

Section 5.3: It is not clear why there is a need to explictly model changepoints, and not predict dynamics markings at beat/downbeat levels.

**Zhanhong’s response:**

> dynamic markings is decode to beat levels,

#### 5.3

Figure 5.2: Are the beat and downbeat components not connected? The same applies to the loss function of equation 5.2.

**Zhanhong’s response:**

*Response 1*

> connected them might have benefit, a good point, but our idea is the simply MMoE module, so hard development might damage its performance.

*Response 2*

> only the decoding progress has the connection, but thanks for rasing it, this is a good point if we want a further performance improvement.

#### 5.4

Section 5.6.1: is cross-dataset evaluation crucial for this specific work? Given that dynamics prediction can be to a large extent composer- and performer-dependent.

**Zhanhong’s response:**

> That's the reason. So we want to check whether this model can generalised across the composer and performer.
>
> Unfortunaly we cannot make a dataset that has specific balance to discuss this topic, but least we verfied it has a good generalization.

### Chapter 6:

#### 6.1

Section 6.2: The author argues that this chapter is taking a “simpler route”. However I would doubt that treating the problem using analysis-by-synthesis methods and DDSP is simpler than a supervised labelling effort. One might argue that the former is more appropriate and accurate, and the latter is less valid and time-consuming, however modelling simplicity might be difficult to argue for the proposed work.

**Zhanhong’s response:**

> yes, great point. Protential problem is design a ddsp model is hard, it need a new data/methodology develpment. But as you said, it's more straightforward.
>
> I will modify this term "simpler route" to "more efficient route".

#### 6.2

Section 6.4.1: What is the difference between V^{(0)} and \hat{V} ?

**Zhanhong’s response:**

> zhanhong not response yet

#### 6.3

Section 6.4.2: Can you comment on the faithfulness of the DDSP-Piano and DDSP-Guitar-Synth synthesizers?

**Zhanhong’s response:**

> We use these synthesizers as differentiable approximations, and their fidelity to the target recordings, especially their velocity-to-sound response, is a limitation. The degradation after Diff-Synth adaptation is consistent with acoustic mismatch, although we have not separately measured reconstruction fidelity and velocity-gradient accuracy on our target data.

#### 6.4

Section 6.4.3: Can you justify the use of a Huber distance as opposed to a more straightforward MAE loss?

**Zhanhong’s response:**

> We chose Huber because it provides smoother gradients for small PHE/OSF errors while retaining an L1-like penalty for large errors. We use β = 1, but we have not established that it performs better than MAE through a dedicated comparison.
>
> We will add more details about this in the thesis, thanks for rasing it.

#### 6.5

Figure 6.2: is the data in the right part of the figure rendered audio? If yes, this is not shown in the figure.

**Zhanhong’s response:**

> zhanhong not response yet

#### 6.6

Section 6.9.4: Could the SoundFont selection not be selected by ear but be automated instead?

**Zhanhong’s response:**

> could be, but it is a big field about the instrument similarity, we agree it's future work but hard to do it well at the current.

### Chapter 7:

#### 7.1

Would it be possible to integrate the developed models into AMT models for complete AMT? Would these improve on transcription performance?

**Zhanhong’s response:**

> Possible, but I can image this is taken the longer time. 
>
> I think it will make the model output more "human-prefer", for example in my case, we used the Bark-scale loudness so definatly it sounds more like the real performance. 
>
> But sometimes, it will return lower objective evaluation metrics, which is a deeper issues need to be address.

#### 7.2

Section 7.3: A possible limitation of this work is that not all possible dynamics markings (e.g. crescendo) are invetigated; these could be mentioned as future work.

**Zhanhong’s response:**

> Yes I agree, I will make this more detail.

## Overall recommendation

As demonstrated by this thesis, the research carried out by the candidate contributed new knowledge to the field of music information retrieval in terms of proposing new models for predicting or recovering musical dynamics in the context of automatic music transcription. This is a systematic and thorough work into the topic, with significant contributions to knowledge, and the proposed work was carried out in a systematic and rigorous manner. As can be seen from the comments above, I have certain minor queries or comments that can be further discussed during the viva. I therefore approve the PhD thesis of Zhanhong He to proceed to viva, and consider the written work to be excellent, at the level of top 25% PhD theses I have examined.

**Zhanhong’s response:**

> zhanhong not response yet

---

*Patron: Her Majesty The Late Queen Elizabeth II*

*Incorporated by Royal Charter as Queen Mary University of London*

<!-- Original PDF page 4 -->

Yours faithfully,  
Dr Emmanouil Benetos  
emmanouil.benetos@qmul.ac.uk  

---

*Patron: Her Majesty The Late Queen Elizabeth II*

*Incorporated by Royal Charter as Queen Mary University of London*
