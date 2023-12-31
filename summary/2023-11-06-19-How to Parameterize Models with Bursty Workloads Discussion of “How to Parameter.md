## 文献总结




### 基本信息
1. Title: How to Parameterize Models with Bursty Workloads（如何为突发工作负载参数化模型）

2. Authors: Guiliano Casale, Ningfang Mi, Ludmila Cherkasova, Evgenia Smirni

3. Affiliation: College of William and Mary (威廉玛丽学院)

4. Keywords: parameterization, bursty workloads, analytic models, index of dispersion, Markovian Arrival Process (MAP), capacity planning (参数化，突发工作负载，分析模型，离散度指数，马尔科夫到达过程，容量规划)

5. URLs: [Paper](link), [Github](None)

### 简要总结
6. Summary:
   - (1): 本文研究背景是关于如何为突发工作负载参数化模型。
   - (2): 过去的方法往往只使用基本的工作负载统计信息来参数化模型，忽略了真实负载的突发性和高度变异性，导致系统性能下降。本文的方法旨在解决这一问题，使用离散度指数来参数化模型，同时解决了测量粒度对突发性的影响。
   - (3): 本文提出一种基于离散度指数的参数化方法，并将其应用于两阶段Markov到达过程（MAP(2)）的评估中。
   - (4): 本文的方法在TPCW负载生成器的服务需求建模中提高了模型预测的准确性，相较于忽略突发性的参数化方法，准确性提高了30%。这个性能可以支持他们的目标。





### 详细总结
8. Conclusion: 

- (1):重要性：本研究对于如何为突发工作负载参数化模型具有重要的意义。过去的方法没有考虑到真实负载的突发性和高度变异性，导致系统性能下降。而本文提出的基于离散度指数的参数化方法可以更准确地描述和预测突发工作负载，从而提高系统性能和容量规划的准确性。

- (2):创新点: 本文的主要创新点在于使用离散度指数来参数化模型。通过考虑负载的突发性和高度变异性，离散度指数能够更准确地描述负载的特征，从而提高模型预测的准确性。另外，本文还解决了测量粒度对突发性的影响，确保模型的稳定性和可靠性。

- (3):性能: 本文的方法在TPCW负载生成器的服务需求建模中取得了良好的性能。相较于忽略突发性的参数化方法，本文的方法提高了模型预测的准确性，准确性的提升达到了30%。这说明本文的方法能够在实际应用中有效地改善系统性能。

- (4):工作量: 本文的工作量主要集中在提出基于离散度指数的参数化方法，并将其应用于两阶段Markov到达过程（MAP(2)）的评估中。通过实验和分析，作者验证了该方法在模型预测准确性方面的优势，并证明了其在实际应用中的可行性和有效性。然而，鉴于本文的方法主要针对TPCW负载生成器进行了评估，对于其他类型的突发工作负载的适用性还需要进一步研究和验证。




