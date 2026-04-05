# 🤖 How LLMs Work — Complete Learning Notes
> **Source Video:** [How LLMs Work — YouTube](https://youtu.be/K45s2PgywvI?si=ZCpQRVhQftrQgYrx)  
> **Topic:** GPT — Generative Pre-Trained Transformer & Transformer Architecture  
> **Last Updated:** April 2026

---

## 🗺️ Overview — The Big Picture

A **Large Language Model (LLM)** like GPT is a deep learning model trained on massive text data to understand and generate human language. It's built on an architecture called the **Transformer**, introduced in the landmark 2017 paper *"Attention Is All You Need"* by Vaswani et al. at Google.

### 🧠 Real-Life Analogy
Think of an LLM like a **very well-read person** who has read billions of pages — books, articles, code, conversations. When you ask them a question, they don't look anything up. They answer purely from memory and pattern recognition. The Transformer is the *brain architecture* that makes this possible.

### The Pipeline at a Glance

```
Raw Text → [Tokenization] → [Embeddings] → [Positional Encoding]
       → [Multi-Head Attention] → [Feed Forward] → [Output Probabilities] → Generated Text
```

---

## Step 1 — Encoding: Tokenization

### 📖 What Is It?
**Tokenization** is the process of breaking raw text into smaller units called **tokens** — which can be words, subwords, punctuation, or characters. These tokens are then converted into numbers so the model can process them mathematically.

### 🍕 Real-Life Analogy
Imagine you're teaching a child to read. You first break a sentence into individual **words** (or even syllables). Similarly, before an LLM can "read" text, it must chop it up into digestible pieces.

### 📌 Example
```
Input:  "Hey There"
Tokens: ["Hey", "There"]
Token IDs: [10, 36]
```

The word **"Hey"** gets assigned the number `10`, and **"There"** gets assigned `36`. These IDs come from the model's **vocabulary** — a fixed dictionary (GPT-4 has ~100,000 tokens).

### 🔍 Subword Tokenization (BPE)
Modern LLMs use **Byte Pair Encoding (BPE)**. Rare words get split into subword pieces:
```
"unbelievable" → ["un", "believ", "able"]
```
This lets the model handle words it has never seen before.

### 💡 Key Facts
- GPT models use the **tiktoken** tokenizer
- 1 token ≈ 4 characters or ¾ of a word in English
- "ChatGPT is great!" = approximately 6 tokens

### 🔗 Tools to Explore
- **[OpenAI Tokenizer](https://platform.openai.com/tokenizer)** — Visualize how text gets tokenized in real time

---

## Step 2 — Vector Embeddings

### 📖 What Is It?
Once tokens are assigned IDs (numbers), they must carry **meaning**. A **vector embedding** is a list of numbers (a vector) that represents the *semantic meaning* of a token in high-dimensional space.

Instead of a single number, each token becomes a **vector of hundreds or thousands of numbers**:
```
CAT = [0.2, -0.5, 0.8, 0.1, ...]   (hundreds of dimensions)
DOG = [0.3, -0.4, 0.7, 0.2, ...]
```

### 📐 Why Vectors?
Vectors allow us to **measure similarity** between words using math. Words with similar meanings are *close together* in vector space.

### 🗺️ Real-Life Analogy
Think of a **city map**. Every building (word) has coordinates (x, y). Buildings close together are related — a bakery and a café are near each other. A hospital is far away. Vector embeddings work the same way, but in 1000+ dimensional space.

### 📌 Famous Example: Word2Vec Relationships
```
King - Man + Woman ≈ Queen
Paris - France + Italy ≈ Rome
```
The model *learns* that "King is to Man as Queen is to Woman" purely from patterns in text!

### 🖼️ Visualizing Embeddings
In the diagram from the video:
- **CAT = 20**, **DOG = 80** (simplified 1D example)
- In reality, embeddings are 768 to 12,288 dimensional (GPT-4)
- Related words like `cat`, `dog`, `milk`, `pedigree` cluster near each other

### 💡 Key Facts
- Embeddings are **learned during training**, not hand-crafted
- GPT-3 uses **12,288-dimensional** embeddings
- The embedding layer is the first neural network layer in a Transformer

---

## Step 3 — Positional Encoding

### 📖 What Is It?
Transformers process ALL tokens **simultaneously** (in parallel), unlike older RNNs that read one word at a time. This is fast, but it means the model loses track of **word order** by default.

**Positional Encoding** adds a special vector to each token's embedding that encodes its *position* in the sequence.

### 🚂 Real-Life Analogy
Imagine receiving a shuffled set of train carriages with no numbers. You know what each carriage contains, but not the order. Positional encoding is like **stamping a sequence number** on each carriage: Carriage 1, Carriage 2, etc.

### 📌 Why It Matters
```
"Dog eats food"  ≠  "Food eats dog"
```
Both sentences have the same words — only the order changes the meaning. Positional encoding ensures the model knows *who* is doing *what*.

### 🔢 How It Works (Simplified)
The original Transformer uses **sine and cosine functions** of different frequencies to generate unique positional vectors:
```
PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
```
These are added to the token embeddings before attention is computed.

### 💡 Modern Variants
- **RoPE** (Rotary Positional Encoding) — used in LLaMA, Mistral
- **ALiBi** — used in some models for better long-context handling

---

## Step 4 — Self-Attention

### 📖 What Is It?
**Self-attention** is the *core mechanism* of the Transformer. It allows each token to "look at" every other token in the sequence and decide how much attention to pay to each one.

### 📌 Example
Sentence: *"The animal didn't cross the street because **it** was too tired."*

What does **"it"** refer to? The animal? The street?

Self-attention lets the model figure this out by attending to relevant tokens:
```
"it" → attends most strongly to "animal" (not "street")
```

### 🎬 Real-Life Analogy
Imagine a **group discussion** in a meeting. When someone says "it", everyone in the room mentally figures out what "it" refers to based on context. Self-attention is the model doing exactly this — but mathematically, for every word, simultaneously.

### ⚙️ The QKV Mechanism
Each token is transformed into **three vectors**:

| Vector | Name | Role |
|--------|------|------|
| **Q** | Query | "What am I looking for?" |
| **K** | Key | "What do I contain?" |
| **V** | Value | "What information do I pass on?" |

**Attention Score** = softmax(Q · Kᵀ / √d_k)

Then: **Output** = Attention Score × V

### 💡 Intuition for QKV
Think of a **library search**:
- Your **Query** = the search term you type
- The **Keys** = the titles of all books on the shelf
- The **Values** = the actual content of those books
- The search finds the books most relevant to your query and returns their content

---

## Step 5 — Multi-Head Attention

### 📖 What Is It?
Instead of running one self-attention operation, the Transformer runs **multiple attention heads in parallel** — each looking at the sentence from a different "perspective."

### 🔍 Why Multiple Heads?
Each head can capture a different type of relationship:
- **Head 1** → focuses on grammatical structure (subject-verb)
- **Head 2** → focuses on coreference ("it" → "animal")
- **Head 3** → focuses on semantic similarity

### 🎭 Real-Life Analogy
Think of a **panel of expert reviewers** analyzing a movie:
- Critic 1 focuses on cinematography
- Critic 2 focuses on acting
- Critic 3 focuses on the soundtrack

Each critic gives their own score, and the final rating combines all perspectives. Multi-head attention works the same way.

### 📌 Architecture Detail
If you have **12 attention heads** and embedding size **768**:
- Each head works on a dimension of 768/12 = **64**
- All heads run **in parallel**
- Outputs are **concatenated** and projected back to 768 dimensions

---

## Step 6 — Feed-Forward Network (FFN)

### 📖 What Is It?
After the attention layers, each token's representation passes through a **Feed-Forward Network** — two linear layers with a non-linear activation (usually ReLU or GELU) in between.

```
FFN(x) = max(0, x·W₁ + b₁) · W₂ + b₂
```

### 🧠 What Does It Do?
If attention is about **relationships between tokens**, the FFN is about **processing each token's own information** — it adds depth and non-linearity to the model's understanding.

### 🍳 Real-Life Analogy
Attention is like **gathering ingredients** from across a kitchen. The Feed-Forward Network is the **actual cooking** — transforming those gathered ingredients into a finished dish.

---

## Step 7 — Decoder & Output

### 📖 What Is It?
In a **generative** model (like GPT), the Transformer uses only the **Decoder** stack. The output of the final layer is a vector that gets projected through a **linear layer** and then **softmax** to produce a probability distribution over all tokens in the vocabulary.

```
Output: [0.001, 0.003, 0.412, 0.0002, ...]
                              ↑
                    Highest prob = next predicted token
```

### 🎲 Sampling
The model doesn't always pick the single highest-probability token. Techniques like:
- **Temperature** — controls randomness (higher = more creative)
- **Top-k sampling** — picks from top k most likely tokens
- **Top-p (nucleus) sampling** — picks from tokens covering top p% of probability

---

## Step 8 — Pre-Training

### 📖 What Is It?
GPT stands for **Generative Pre-Trained Transformer**. The "Pre-Trained" part means the model is trained on a massive corpus of text with a simple objective:

> **Predict the next token** given all previous tokens.

This is called **Causal Language Modeling**.

```
Input:  "The cat sat on the"
Target: "mat"
```

The model sees billions of such examples and adjusts its weights to get better at prediction.

### 💡 Scale of Training
| Model | Parameters | Training Tokens |
|-------|-----------|-----------------|
| GPT-2 | 1.5B | 40 GB text |
| GPT-3 | 175B | 300B tokens |
| GPT-4 | ~1T (est.) | Trillions |

---

## Step 9 — Fine-Tuning & RLHF

### 📖 What Is It?
After pre-training, a raw GPT model can predict text but isn't very helpful as a **chatbot**. Fine-tuning adapts it:

1. **Supervised Fine-Tuning (SFT)** — Train on examples of good human responses
2. **RLHF** (Reinforcement Learning from Human Feedback) — Humans rank outputs; a reward model is trained; the LLM is updated to maximize reward

### 🎯 Real-Life Analogy
Pre-training is like a student **reading every textbook ever written**. Fine-tuning + RLHF is like that student going through a **coaching program** to learn how to communicate clearly, be helpful, and avoid harmful responses.

---

## 🔁 Complete Flow — End to End

```
You type: "What is the capital of France?"
        ↓
[Tokenization]  →  ["What", "is", "the", "capital", "of", "France", "?"]
        ↓
[Embeddings]    →  Each token → 12288-dim vector
        ↓
[Pos. Encoding] →  Add position info to each vector
        ↓
[96× Transformer Blocks]
   → Multi-Head Self-Attention
   → Feed-Forward Network
   → Layer Normalization + Residual Connections
        ↓
[Linear + Softmax] → Probability over 100k vocabulary
        ↓
Output token: "Paris"  →  Repeat for next token → "." → Stop
```

---

## 📊 Quick Reference Table

| Concept | What It Does | Real-Life Analogy |
|---------|-------------|-------------------|
| Tokenization | Breaks text into tokens | Chopping vegetables |
| Embeddings | Converts tokens to meaning-vectors | GPS coordinates for words |
| Positional Encoding | Adds order information | Numbering train carriages |
| Self-Attention | Weighs token relationships | Group discussion |
| Multi-Head Attention | Multiple parallel attention views | Panel of expert reviewers |
| Feed-Forward Network | Processes each token's info | The actual cooking |
| Softmax Output | Picks next token | Voting on most likely word |

---

## 📚 References & Further Learning

### 📄 Must-Read Papers
1. **Attention Is All You Need** (2017) — Vaswani et al. — [arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
2. **BERT** — Bidirectional Encoder Representations from Transformers — [arxiv.org/abs/1810.04805](https://arxiv.org/abs/1810.04805)
3. **GPT-3** — Language Models are Few-Shot Learners — [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165)
4. **InstructGPT / RLHF** — [arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155)

### 🎥 Videos & Courses
- **3Blue1Brown — Neural Networks Series** — [youtube.com/3blue1brown](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — Best visual intuition
- **Andrej Karpathy — Let's build GPT** — [youtube.com/watch?v=kCc8FmEb1nY](https://www.youtube.com/watch?v=kCc8FmEb1nY) — Build GPT from scratch in Python
- **Original Source Video** — [youtu.be/K45s2PgywvI](https://youtu.be/K45s2PgywvI?si=ZCpQRVhQftrQgYrx)

### 🌐 Interactive Tools
- **OpenAI Tokenizer** — [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)
- **Tensorflow Embedding Projector** — [projector.tensorflow.org](https://projector.tensorflow.org) — Visualize word vectors in 3D
- **BertViz** — Visualize attention heads — [github.com/jessevig/bertviz](https://github.com/jessevig/bertviz)

### 📘 Books
- **"The Hundred-Page Machine Learning Book"** — Andriy Burkov (free PDF available)
- **"Deep Learning"** — Goodfellow, Bengio, Courville — [deeplearningbook.org](https://www.deeplearningbook.org) (free)

---

## 🧩 Glossary

| Term | Definition |
|------|-----------|
| **Token** | The smallest unit of text processed by an LLM |
| **Embedding** | A dense vector representation of a token capturing semantic meaning |
| **Attention** | Mechanism to weigh relevance between tokens |
| **Transformer** | Architecture using attention layers to process sequences in parallel |
| **LLM** | Large Language Model — a Transformer trained on massive text data |
| **BPE** | Byte Pair Encoding — subword tokenization algorithm |
| **RLHF** | Reinforcement Learning from Human Feedback — fine-tuning technique |
| **Temperature** | Controls randomness in token sampling |
| **Parameter** | A learnable weight in the neural network |
| **Context Window** | Maximum number of tokens the model can "see" at once |

