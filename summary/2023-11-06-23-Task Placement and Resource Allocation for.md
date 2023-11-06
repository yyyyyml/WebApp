## 文献总结




### 基本信息
1. Title: Task Placement and Resource Allocation for Edge Machine Learning: A GNN-based Multi-Agent Reinforcement Learning Paradigm (为边缘机器学习任务分配和资源分配提供了一个基于GNN的多智能体强化学习范例)
2. Authors: Yihong Li, Xiaoxi Zhang, Tianyu Zeng, Jingpu Duan, Chuan Wu, Di Wu, Xu Chen
3. Affiliation: School of Computer Science and Engineering, Sun Yat-sen University (中山大学计算机科学与工程学院)
4. Keywords: Task placement, resource allocation, edge machine learning, multi-agent reinforcement learning, graph neural networks

5. Urls: [Paper](https://arxiv.org/abs/2302.00571v2), [Github: None]

### 简要总结
6. Summary:
- (1): 本文研究的背景是边缘计算网络中的机器学习任务，边缘设备资源有限，为了更好地利用这些资源，需要对任务进行合理的分配和资源分配。
- (2): 过去的方法采用了预设规则进行资源分配，但是对于机器学习任务的资源需求通常是不确定和弹性的，无法进行准确估计，因此需要新的方法来解决资源分配问题。本文提出了一种基于多智能体强化学习的分布式任务调度器TapFinger，通过优化任务分配和多维资源分配来最小化机器学习任务的总完成时间。
- (3): 本文采用了多智能体强化学习方法，并提出了一些技术来提高其效率，包括使用异构图注意力网络作为强化学习的支撑，在演员网络中引入了定制的任务选择阶段，以及运用贝叶斯定理和掩码方案进行集成。首先实现了单任务调度版本，然后推广到多任务调度情况，设计能够降低决策空间扩展的算法，并快速收敛到最优调度解。
- (4): 本文实验采用了合成和测试平台的机器学习任务痕迹，结果显示TapFinger相比于现有的调度器，可以减少平均任务完成时间，提高资源利用效率，最高可达到54.9%的减少。实验结果支持了他们的目标。





### 详细总结
8. Conclusion: 

- (1):重要性：本文提出的TapFinger框架在边缘计算网络中的机器学习任务分配和资源分配方面具有重要意义。通过多智能体强化学习和图神经网络的结合，实现了对边缘设备资源的高效利用，最小化机器学习任务的总完成时间。

- (2):创新点: 本文的创新点在于采用了多智能体强化学习方法，通过引入异构图注意力网络和定制任务选择阶段，实现了对边缘计算网络中机器学习任务的优化调度。此外，还应用贝叶斯定理和掩码方案解决了决策冲突问题，提高了调度算法的效率和有效性。

- (3):性能: 实验结果显示，与现有调度算法相比，TapFinger能够显著减少机器学习任务的平均完成时间。在合成和测试平台的机器学习任务痕迹上，TapFinger相对于现有调度器可以将平均任务完成时间降低高达28.6%和14.5%，使用扩展的多任务TapFinger可以达到最高54.9%的减少。

- (4):工作量: 本文在实验阶段使用了合成和测试平台的机器学习任务痕迹，通过对比实验结果，验证了TapFinger框架在减少任务完成时间和提高资源利用效率方面的效果。作者还提供了单任务和多任务版本的TapFinger，适用于不同的场景。通过充分验证和实验分析，本文工作量合理且结论可信。




