## Paper:1




1. Title: Ekya: Continuous Learning of Video Analytics Models on Edge Compute Servers

2. Authors: Romil Bhardwaj, Zhengxu Xia, Ganesh Ananthanarayanan, Junchen Jiang, Yuanchao Shu, Nikolaos Karianakis, Kevin Hsieh, Paramvir Bahl, Ion Stoica

3. Affiliation: Bhardwaj is affiliated with Microsoft and UC Berkeley.

4. Keywords: video analytics, edge compute servers, continuous learning, data drift, inference accuracy

5. URLs: Paper - [Link](https://www.usenix.org/conference/nsdi22/presentation/bhardwaj), Github: None

6. Summary:
- (1): The research background of this paper is video analytics applications using edge compute servers for processing videos. These applications face the challenge of data drift, where live video data diverges from the training data.
- (2): Past methods for addressing data drift in video analytics models on edge compute servers have not effectively balanced the tradeoff between retrained model accuracy and inference accuracy. The approach presented in this paper, Ekya, aims to address this challenge.
- (3): The research methodology proposed in this paper is the development of Ekya, which balances the tradeoff between retraining models and inference accuracy on edge compute servers. Ekya uses a micro-profiler to identify models in need of retraining and achieves higher accuracy compared to a baseline scheduler.
- (4): The methods in this paper improve the accuracy of video analytics models deployed on edge compute servers. Ekya achieves a 29% higher accuracy compared to the baseline scheduler and requires 4× fewer GPU resources to achieve the same accuracy. The performance supports the goal of addressing data drift and improving inference accuracy in video analytics applications on edge compute servers.





8. Conclusion:

- (1): 本研究的意义在于提出了一种在边缘计算服务器上持续学习视频分析模型的方法。这是为了应对数据漂移的挑战，因为视频数据可能会与训练数据不一致。

- (2): 创新点: 这篇文章的创新之处在于提出了Ekya这一方法，该方法可以在边缘计算服务器上平衡模型的重新训练和推理准确性之间的权衡。通过使用微调模型以及基于MicroProfiler的调度器，Ekya相比基准调度器实现了更高的准确性。

性能: 该方法在边缘计算服务器上部署的视频分析模型的准确性得到了显著改进。与基准调度器相比，Ekya的准确性提高了29％，而且实现相同准确性所需的GPU资源减少了4倍。这表明Ekya能够在解决数据漂移并提高视频分析应用的推理准确性方面具有良好的性能。

工作量: 本文中的方法可以在边缘计算服务器上实现视频分析模型的持续学习，而无需频繁地重新训练整个模型。Ekya利用MicroProfiler来确定需要重新训练的模型，从而减少了工作量。因此，这种方法可以节省时间和计算资源，并提高系统的效率。

根据以上综述，本文提出的Ekya方法在解决数据漂移和改善边缘计算服务器上视频分析应用的推理准确性方面具有重要的意义。它在创新点、性能和工作量方面都有突出特点，为边缘计算环境下的视频分析任务提供了一种有效的解决方案。




