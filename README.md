# Paper Reading Assistant

这是一个使用Moonshot的[KimiChat](https://kimi.moonshot.cn/)模型创建的论文阅读助手，它可以帮助你阅读和理解科研论文，并根据你提供的指引/问题列表生成论文的总结。代码参考了[Moonshot AI使用手册](https://platform.moonshot.cn/docs/intro)。

## 功能

- 读取论文文件
- 根据提供的问题列表，生成论文的总结
- 将论文总结保存为文本文件

## 使用方法

1. 安装必要的Python库：

```bash
pip install openai
```

2. 将你的[Moonshot API密钥](https://platform.moonshot.cn/console/api-keys)添加到代码中：

```bash
client = OpenAI(
    api_key = "$MOONSHOT_API_KEY",
    base_url= "https://api.moonshot.cn/v1",
)
```

3. 运行脚本，并提供论文文件、问题列表文件和输出文件的路径：

```bash
python paper_reading_assistant.py --paper your_paper.pdf --questions your_questions.txt --output your_summary.md
```

## 脚本参数

- `--paper` 或 `-p`：待阅读的论文文件路径
- `--questions` 或 `-q`：问题列表文件的路径
- `--output` 或 `-o`：论文总结输出的路径

## 注意事项

- 问题列表文件应为文本文件，每个问题之间用 `---`分隔，问题支持单行/多行表达。你可以仿造我提供的例子，创造自己研究领域的问题模板，以快速且格式化地从论文中提取你需要的信息。
  ```
  请你作为一名专业的科研文献阅读助手，为我提供一篇科研文献的详细总结。总结应包括以下部分：
  文献基本信息：列出文献的作者、发表年份、标题及研究领域。
  章节内容：依照文献的章节顺序，详细描述每个章节的内容。请确保语言准确专业，信息无遗漏，且忠实于原文内容。
  重点与创新点：明确指出文献的关键发现、理论贡献或技术创新。
  一段话总结：用一段通俗易懂的中文总结整篇文献，并提供你的个人评论，以便于我快速把握文献的精髓。
  ---
  根据文章的内容，依次填入以下信息。需要标注"根据 x.x 节"给出信息来源，需要给出判断依据。如果文章没有明确提及某一部分，请填入None，不要推测。
  数据预处理：对数据进行的预处理步骤。
  模型类型：使用的模型类型，如 "MLP"、"CNN"、"Transformer"。
  模型结构：使用的模型结构。
  参数量：模型的参数量。
  ```
- 推荐以Markdown格式保存输出文件。

## 开源许可

本项目采用MIT许可证，你可以自由地使用、修改和分发本项目的源代码，但必须保留原作者的版权声明。
