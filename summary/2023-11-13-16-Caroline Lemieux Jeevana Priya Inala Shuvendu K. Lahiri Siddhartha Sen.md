## 文献总结




### 基本信息
Title: CODAMOSA: Escaping Coverage Plateaus in Test Generation with Pre-trained Large Language Models (通过预训练的大语言模型在测试生成中跳出覆盖停滞期)

Authors: Caroline Lemieux, Jeevana Priya Inala, Shuvendu K. Lahiri, Siddhartha Sen

Affiliation: University of British Columbia, Canada (卡罗琳·勒米厄，温哥华大学，加拿大)

Keywords: search-based software testing, large language models (LLMs), test case generation, coverage plateaus (搜索型软件测试，大语言模型，测试用例生成，覆盖停滞期)

Urls: [Paper](xxxx) or [Github Code](None)

### 简要总结
Summary: 
 - (1): 本文研究背景是搜索型软件测试在生成能覆盖程序核心逻辑的测试用例时的困境。
 - (2): 过去的方法通常依赖于随机生成和变异测试用例，但在生成覆盖程序关键部分的测试用例方面遇到困难，导致性能停滞。本文提出的方法通过使用预训练的大语言模型来生成有效的测试用例，从而有望解决这一问题。
 - (3): 本文提出的方法是CODAMOSA，它在搜索型软件测试过程中监测覆盖率进展并使用大语言模型生成测试用例以帮助搜索更有用的区域。CODAMOSA通过将大语言模型生成的代码转化为符合SBST要求的测试用例表示形式，进而利用SBST的变异操作和适应度函数来评估和优化生成的测试用例。
 - (4): 本文在486个Python模块上进行了实证评估，结果表明CODAMOSA在大多数评测案例上实现了更高的覆盖率，证明了方法的有效性。





### 详细总结
Conclusion: 

- (1):重要性：这项工作的重要性在于提出一种新的方法，即使用预训练的大语言模型来解决搜索型软件测试中的覆盖停滞问题。过去的方法在生成有效的测试用例方面遇到困难，导致性能停滞。本文提出的方法通过利用大语言模型生成测试用例，有望解决这一问题。

- (2):创新点: 本文的创新点在于将大语言模型引入搜索型软件测试，用于生成能覆盖程序核心逻辑的测试用例。通过将大语言模型生成的代码转化为适合搜索型软件测试的测试用例形式，并利用变异操作和适应度函数评估和优化测试用例，从而提高覆盖率。

- (3):性能: 实证评估结果显示，本文提出的方法在486个Python模块上实现了更高的覆盖率。这表明该方法在性能上具有优势，能够帮助函数覆盖停滞的搜索型软件测试。

- (4):工作量: 本文的工作量主要在于实施CODAMOSA方法并进行大规模实证评估。实验中涉及了486个Python模块的评估，计算覆盖率等指标。然而，具体的工作量细节并未明确提及，我们无法对其进行进一步评估。

Please note that the provided English translations of the proper nouns may not be accurate.




