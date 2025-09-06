# Nyay AI ⚖️ - A Personal AI Law Advisor for India

![Python Version](https://img.shields.io/badge/Python-3.10%20(64--bit)-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)
![Framework](https://img.shields.io/badge/Framework-Flask-black)
![Model](https://img.shields.io/badge/Model-LLaMA%203.1%20(8B)-orange)

An advanced, context-aware conversational AI assistant designed to make Indian law accessible to everyone. This project, developed by **Yugesh** for [ProjectWorlds.com](https://projectworlds.com/), is not just a Q&A bot; it's a true legal advisor with a persistent memory, capable of having in-depth, stateful conversations.

This was developed as a final year academic project to showcase the power of modern Large Language Models when fine-tuned for specialized domains.

---

## 📸 Project Showcase

Here is Nyay AI in action, demonstrating its sleek, modern UI and its ability to remember the user's name throughout a conversation.

![Nyay AI Showcase](https://raw.githubusercontent.com/projectworldsofficial/Nyay-AI/main/screenshots/1.png)

## 🎬 Watch the Live Demo on YouTube!

Click the thumbnail below to watch a full showcase of Nyay AI in action, including a demonstration of its conversational memory and deep legal knowledge.

[[Nyay AI - Personal AI Law Advisor for India (Project Showcase)](https://youtu.be/KvXmbnJ5wco)]

---

## ✨ Core Features

- **🧠 Conversational Memory:** Nyay AI remembers the context of your entire conversation, allowing for natural follow-up questions and a truly interactive experience.
- **📚 Deep Legal Knowledge:** Expertly trained on a vast corpus of Indian legal texts, including the Constitution, the Indian Penal Code (IPC), and more.
- **⚖️ Landmark Case Summarization:** Instantly get concise and accurate summaries of complex and lengthy Supreme Court of India judgments.
- **🚀 GPU Accelerated:** Leverages NVIDIA CUDA through `llama-cpp-python` to run the 8-billion parameter model efficiently on consumer hardware, ensuring responses are generated in a timely manner.
- **💻 Modern & Responsive UI:** A clean, professional, and user-friendly interface built with modern CSS and JavaScript.

---

## 🛠️ Tech Stack

- **Foundation Model:** [varma007ut/Indian_Legal_Assitant](https://huggingface.co/varma007ut/Indian_Legal_Assitant) (LLaMA 3.1 8B GGUF)
- **Backend:** Python, Flask
- **AI Engine:** `llama-cpp-python`
- **GPU Acceleration:** NVIDIA CUDA
- **Frontend:** HTML, CSS, JavaScript

---

## 🖥️ System Requirements (Strict)

This is a resource-intensive project. The following are the **minimum requirements** to run it successfully.

| Component         | Minimum Required Specification                                  |
|-------------------|-----------------------------------------------------------------|
| **OS**            | Windows 10/11 **(64-bit)**                                      |
| **Python**        | Python 3.10 **(64-bit)**                                        |
| **GPU (NVIDIA)**  | **4 GB VRAM** (e.g., RTX 3050) & CUDA Compute Capability 8.0+    |
| **RAM**           | **16 GB**                                                       |
| **CPU**           | Modern 6-core processor (e.g., Ryzen 5 5600X, Intel i5-12400)   |
| **Storage**       | **20 GB free space** on an SSD                                  |

---

## 🚀 Installation & Setup Guide

Follow these steps carefully to set up and run the project locally.

### 1. Prerequisites
- **NVIDIA GPU:** You must have a compatible NVIDIA graphics card.
- **Git:** Ensure [Git](https://git-scm.com/downloads) is installed.
- **Python 3.10 (64-bit):** Crucially, you must have a **64-bit** version of Python 3.10. You can download it [here](https://www.python.org/downloads/release/python-31011/). **Remember to check "Add Python 3.10 to PATH" during installation.**

### 2. Clone the Repository
Open your terminal and clone this repository:
```bash
git clone https://github.com/projectworldsofficial/Nyay-AI.git
cd Nyay-AI