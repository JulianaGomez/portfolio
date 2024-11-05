# Improving ASR Output Using a Transformer-based Grammatical Error Correction Approach

Project developed for the Natural Language Processing with Deep Learning Final Project, as part of my Masters in Information and Data Science at UC Berkeley. In this work, we introduce a transformer-based encoder-only grammatical error correction approach for improving automatic speech recognition by utilizing both a grammatical acceptability classifier (GAC) and a grammatical error correction model (GEC). We investigate different strategies for optimizing the models and show that using raw data to train our GAC model generates better outputs than using cleaned and augmented data. We also find that the model which punctuates and proper-cases the input data by means of Named Entity Recognition (NER) yields better results than other GEC models, leading to reduced over-correction. Considering phonetics also improved model performance, and the performance differs between gender and emotions. 


*Authors*: Rachel Gao, Juliana Gómez Consuegra, Erica Nakabayashi  


## My role 

I was responsible for coming up with the research idea, research design (along with the rest of the team), gathering some of the data, doing EDA on the Grammatical Error Corrector, experimenting with Parts-of-speech tagging and spellchecking for the model, running RoBERTa models and hyperparameter tuning. I also wrote the final report, which can be found in the deliverables section.


|Folder|Notebook|Contents|
|---|---|---|
|grammatical_acceptability_clasifier|RoBERTa_base_max_len_128_pooler.ipynb|Train RoBERTa base as a grammatical acceptability classifier on CoLA dataset, with max token length = 128|
||RoBERTa_base_pooler.ipynb|Train RoBERTa base as a grammatical acceptability classifier on CoLA dataset, with max token length = 256|
||RoBERTa_large_cls.ipynb|Train RoBERTa large as a grammatical acceptability classifier on CoLA dataset, with cls token|
||RoBERTa_large_pooler.ipynb|Train RoBERTa large as a grammatical acceptability classifier on CoLA dataset, with pooling|
|grammatical_error_corrector|confusion_sets.ipynb|Selecting optimal confusion sets to aid model in correcting grammar where the POS doesn't change according to context|
||confusion_sets_large.ipynb|Create a confusion set, to aid model in correcting grammar|
||GEC_metrics_comparison.ipynb|Evaluation metrics for GEC model|
||GECM_comp_emotion.ipynb|Evaluation metrics for GEC model, with emotion added to the model|
||JG_POS_tagging.ipynb|Use parts of speech tagging to improve performance of grammatical error correction model|
||tokenizers.ipynb|Comparing how three types of tokenizers (BPE, Wordpiece and Moses) handle numbers|
||try_spellcheck_pipeline.ipynb|Try to include a spellcheck in the pipeline, to improve the performance of the grammatical error corrector model|




