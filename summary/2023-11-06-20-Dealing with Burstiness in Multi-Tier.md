## 文献总结




### 基本信息
1. Title: Dealing with Burstiness in Multi-Tier (应对多层次中的突发性)
2. Authors: Giuliano Casale, Ningfang Mi, Lucy Cherkasova, Evgenia Smirni
3. Affiliation: Giuliano Casale (帝国理工学院), Ningfang Mi (东北大学), Lucy Cherkasova (惠普实验室), Evgenia Smirni (威廉玛丽学院)
4. Keywords: Capacity planning, multi-tier applications, bursty workload, bottleneck switch, index of dispersion.
5. Urls: [Paper](https://link.springer.com/chapter/10.1007%2F978-3-642-00644-6_14), [No Github available]

### 简要总结
6. Summary:
- (1): 这篇文章的研究背景是企业应用中的工作负载和资源使用模式经常表现出突发性，导致用户感知的性能大幅下降。
- (2): 过去的方法存在一些问题，该方法在回溯性方面很有动机。
- (3): 本文提出了一种检测多层次应用程序中突发性症状的方法，并将这些信息纳入性能预测模型中。该建模方法是基于服务器上服务过程的离散度指数，通过观察该服务器的concatenated busy times内的完成次数进行推断。离散度指数用于推导出一个Markov调制过程，很好地捕捉资源的突发性和可变性，从而允许我们定义用于性能预测的排队网络模型。
- (4): 该方法在突发性和非突发性负载下，实验结果和性能模型预测一致，并且说明了该方法的有效性。此外，我们还展示了该方法可扩展到建模引起应用程序请求流中的突发性的闪光人群。





### 详细总结

8. Conclusion:

- (1):重要性：这篇文章的重要性在于针对企业应用中常见的突发性工作负载和资源使用模式进行建模和预测，从而帮助应对突发性对用户性能的负面影响。

- (2):创新点：本文的创新点在于提出了一种基于离散度指数的建模方法，通过推断服务器服务过程的信息来捕捉和纳入性能预测模型中，有效应对突发性。

- (3):性能：实验结果验证了该方法在突发性和非突发性负载情况下的性能预测一致性，证明了该方法的有效性，并且针对存在瓶颈交换机的系统也能有效预测性能。

- (4):工作量：本文采用了TPC-W基准进行了详细的实验，验证了提出的方法在突发性、瓶颈交换条件和闪光人群等情况下的稳健性。






