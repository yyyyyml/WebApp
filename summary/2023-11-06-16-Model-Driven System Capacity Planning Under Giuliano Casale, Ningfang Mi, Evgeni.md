## 文献总结




### 基本信息
1. Title: Model-Driven System Capacity Planning Under Workload Burstiness (基于工作负载突发性的模型驱动系统容量规划)
2. Authors: Giuliano Casale, Ningfang Mi, Evgenia Smirni
3. Affiliation: College of William and Mary (威廉与玛丽学院)
4. Keywords: capacity planning, MAP queueing networks, bursty workloads, performance prediction (容量规划，MAP队列网络，突发性工作负载，性能预测)
5. Urls: [Paper](链接), Github:None


### 简要总结
6. Summary: 
- (1): 本文研究了一种名为MAP队列网络的容量规划模型，用于描述和准确预测在突发性工作负载（如多层架构或存储阵列）下运行的复杂系统的性能。突发性工作负载是一种明显影响系统性能但不能被既有容量规划模型明确捕捉的特征。
- (2): 过去的方法主要基于产品形式队列网络进行容量规划，但这些模型无法准确预测非续订工作负载中的性能。为了解决这个问题，本文引入了使用Markovian Arrival Processes (MAPs) 建模服务时间的MAP队列网络。这种新方法旨在解决非续订工作负载下容量规划模型的局限性。
- (3): 本文提出了通过两种状态空间转换（Linear Reduction和Quadratic Reduction）解决MAP队列网络的方法。这些转换大大减少了队列网络模型中底层Markov链的状态数。从这些减少的状态空间中，我们得到了关于各种性能指标（如吞吐量、响应时间、利用率）的两类界限。数值实验表明，线性约简和二次约简的界限具有良好的准确性。
- (4): 本文的方法在对具有突发性TPC-W工作负载的实际多层架构性能分析中表现出很高的效果。通过所提出的MAP队列网络容量规划模型，可以提供可靠的性能预测，以支持系统容量规划的目标。





### 详细总结
8. Conclusion:

- (1): 重要性：这项工作的重要性在于提出了一种新的模型-驱动的系统容量规划方法，用于准确预测在突发性工作负载下运行的复杂系统的性能。这种突发性工作负载特征在过去的容量规划模型中难以捕捉，因此这项研究为解决这一问题提供了一种创新的解决方案。

- (2): 创新点：本文的创新点主要体现在以下几个方面：
    - 引入MAP队列网络：通过引入使用Markovian Arrival Processes（MAPs）建模服务时间的MAP队列网络，提出了一种新的容量规划模型。相比过去基于产品形式队列网络的方法，这种新方法可以更准确地预测非续订工作负载下的性能。
    - 状态空间转换方法：本文提出了两种状态空间转换方法（线性约简和二次约简），通过减少底层Markov链的状态数，从而降低了模型的复杂度。这些转换方法不仅提高了计算效率，还为性能指标的界限提供了准确的结果。
    - 关注实际应用：通过对具有突发性TPC-W工作负载的实际多层架构性能分析，验证了本文提出方法的有效性和可靠性。这对于实际系统容量规划和性能预测具有重要意义。

- (3): 性能：本文的性能表现在以下几个方面：
    - 准确性：通过对不同性能指标（如吞吐量、响应时间、利用率）的两类界限，该方法在预测性能方面表现出很高的准确性。数值实验验证了线性约简和二次约简的界限的准确性。
    - 效率：通过状态空间转换方法的应用，本文能够大大减少模型中底层Markov链的状态数，提高了计算效率和模型的可操作性。

- (4): 工作量：本文关注并解决了突发性工作负载下的系统容量规划问题，这是一个现实中普遍存在且具有挑战性的问题。通过提出的MAP队列网络容量规划模型，该研究为实际系统的容量规划提供了可靠的性能预测支持。



