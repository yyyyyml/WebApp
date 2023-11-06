## 文献总结




### 基本信息
1. Title: Quantifying Cloud Workload Burstiness: New Measures and Models (量化云工作负载的突发性：新的度量和模型)
2. Authors: Abiola Adegboyega
3. Affiliation: 电气与计算机工程, 卡尔加里大学
4. Keywords: burstiness, variance, workloads, score
5. Urls: [Paper](链接), Github: None

### 简要总结      
6. Summary: 

- (1): 本文研究了云工作负载突发性的统计度量方法。云应用的多样性和按需部署导致了工作负载的突发性。突发性可以通过各种方差度量进行统计度量。
 
- (2): 过去的方法大多采用基于正态分布假设的工作负载模型来度量突发性，这对许多云使用场景来说是合理的。然而最近的研究发现了不能由正态性假设解释或捕捉的新观察结果。本文提出了一种新的突发性度量方法（即归一化得分指数），基于最近的计量经济模型，并根据不同的工作负载特征进行了改进。这一方法的动机充分。

- (3): 本文使用不同的工作负载，确定了一些独特捕捉工作负载特定突发性的统计模型。然后，它使用最近描述为自回归条件分数（ACS）的计量经济模型，它们能够更准确地捕捉突发性的时变参数。此外，与现有的方法相比，本文提出了一种新的突发性度量指标NSI，它能够捕捉特定于每个工作负载统计特征的突发性。NSI适用于传统的方差特征时，恢复到传统的突发性度量方法；对于非标准特征，它会相应地对其进行建模。NSI已应用于多样的工作负载集，并提供了静态指标和跟踪工作负载生命周期内突发性的手段。

- (4): 本文的方法在多样化的云工作负载集合上进行评估，在不同的使用案例中取得了良好的结果。该方法的性能既支持了他们的目标，也可以应用于云计算场景中的解决方案。





### 详细总结
8. Conclusion: 

- (1):重要性：本文的重要性在于提出了一种新的方法来量化云工作负载的突发性。传统的基于正态分布的方法无法准确捕捉到突发性的特征，而本文提出的新方法通过归一化得分指数（NSI）能够更好地描述和度量不同工作负载的突发性，对于理解和管理云计算场景中的工作负载非常重要。

- (2):创新点: 本文的创新点主要体现在以下几个方面：
   - 针对云工作负载突发性的统计度量，提出了一种新的方法——归一化得分指数（NSI），相比传统方法能更准确地捕捉工作负载的特征。
   - 使用计量经济模型自回归条件分数（ACS）来描述突发性的时变参数，进一步提高了突发性度量的准确性。
   - NSI指标能够适应不同工作负载的统计特征，既可用于传统的方差特征，又可以对非标准特征进行建模，具有更广泛的应用性。

- (3):性能: 本文的方法在多样化的云工作负载集合上进行了评估，并在不同的使用案例中取得了良好的结果。该方法能够准确度量工作负载的突发性，并提供了静态指标和跟踪工作负载生命周期内突发性的手段，对于云计算场景中的解决方案具有良好的性能。

- (4):工作量: 本文的工作量主要围绕量化云工作负载的突发性展开。通过研究不同工作负载的特点，提出了归一化得分指数（NSI）作为度量突发性的新方法，并应用于多样的工作负载集合中进行评估。同时，利用计量经济模型自回归条件分数（ACS）对突发性的时变参数进行建模，减少了工作负载度量的误差。通过量化工作负载突发性的新方法和模型，对云计算领域提供了有益的参考。

  This paper proposes a new method to quantify cloud workload burstiness. The method introduces the Normalized Score Index (NSI) as a measure of burstiness, based on recent econometric models and improved based on different workload characteristics. The NSI is able to capture burstiness specific to each workload statistical characteristic, making it applicable to both traditional variance features and non-standard features. The proposed method achieves good results on diverse sets of cloud workloads and can be applied in various use cases. The innovation lies in the introduction of the NSI measure and the application of the econometric model called Autoregressive Conditional Score (ACS) to capture burstiness' time-varying parameters. The performance of the method supports its objectives and provides a solution for burstiness measurement in cloud computing scenarios.




