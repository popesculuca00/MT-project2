# Project Title: Direct Preference Optimization on FLAN T5 for English to Romanian Translation

## Authors
- Popescu Luca Alexandru 
- Vasilescu Andreea
## Abstract
This project explores the application of Direct Preference Optimization (DPO) on the Text-to-Text Transfer Transformer (FLAN T5) model for English-to-Romanian translation without diacritics. Leveraging the Transformer Reinforcement Learning library, we aim to fine-tune an open-source model from Hugging Face and evaluate the effectiveness of DPO in aligning the model with human preferences.

## Keywords
Machine Translation, T5, Direct Preference Optimization (DPO), Transformer, Reinforcement Learning, English-to-Romanian Translation

## 1. Introduction

## 2. State of the ART
### 2.1 Different Approaches of Machine Translation

### 2.2 Transformers

### 2.3 Direct Preference Optimization (DPO)

### 2.4 How Does DPO Work?

## 3. Experiment

## 4. Conclusions
The project provides a pipeline for applying DPO to language translation tasks. However, challenges with smaller models and hardware limitations prevented achieving satisfactory results. 
### Issues Encountered
1. Lack of resources and information for applying DPO on smaller models.
2. Difficulty fitting a Mistral 7B model into limited VRAM.
3. VRAM requirements even with quantization pose challenges.
4. Scarcity of details in online discussions on similar T5 model issues.

## 5. Future Work
Future work involves running the pipeline on larger models to potentially yield better results. 
