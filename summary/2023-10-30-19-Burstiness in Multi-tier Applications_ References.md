## Paper:1




1. Title: Burstiness in Multi-tier Applications: Symptoms, Causes, and New Models (多层应用程序中的突发性：症状、原因和新模型)

2. Authors: G. Casale, N. Mi, E. Smirni

3. Affiliation: None

4. Keywords: Capacity planning, multi-tier systems, transactions, sessions, bursty workload, bottleneck switch, index of dispersion (容量规划，多层系统，事务，会话，突发工作负载，瓶颈开关，离散度指标)

5. Urls: https://link.springer.com/chapter/10.1007/978-3-642-23960-1_38 or Github: None

6. Summary:

- (1): 这篇论文研究了多层应用程序中的突发性现象，即时间相关性的一种形式。突发性经常导致用户感知性能的显著降低，而现有的容量规划模型很难捕捉到这种现象。

- (2): 过去的方法存在一些问题。传统模型无法准确捕捉复杂的工作负载和系统之间的相互作用，导致其对用户感知性能的预测不准确。本文提出的方法旨在通过检测多层系统中的突发性症状，而无需确定突发性的精确原因。这种方法的动机合理且有效。

- (3): 本文提出了一种简单有效的方法来检测多层系统中的突发性症状，并将这些信息纳入到建模方法中。该方法基于服务器上服务过程的离散度指标，并利用其他反映服务时间“估计”均值和95th百分位数的测量数据来构建马尔可夫调制过程，以捕捉真实服务过程的突发性和变异性。

- (4): 通过在TPC-W测试平台上的实验和模型预测结果验证，本文提出的方法在突发和非突发工作负载下的性能表现良好。实验结果与模型预测结果非常吻合，强烈支持所提方法的有效性。这些方法在容量规划和性能建模任务中表现出色，并能支持实际生产环境中的应用。





8. Conclusion:

- (1): The significance of this research lies in addressing the burstiness phenomenon in multi-tier applications, which is a form of temporal correlation. Burstiness often leads to a significant degradation in user-perceived performance, and existing capacity planning models struggle to capture this phenomenon accurately. This work provides a novel approach to detect burstiness symptoms and incorporates them into modeling techniques, improving performance predictions in multi-tier systems.

- (2): Innovation point: This article introduces a simple yet effective method to detect burstiness symptoms in multi-tier systems, utilizing the index of dispersion (IOD) of service processes on servers. By incorporating measurements reflecting estimates of mean and 95th percentiles of service times, the proposed Markov-modulated process captures the burstiness and variability of real service processes. This approach improves the accuracy of performance modeling and capacity planning in multi-tier applications.

Performance: The experimental results and model predictions on the TPC-W benchmark platform validate the effectiveness of the proposed method under bursty and non-bursty workloads. The strong correlation between the experimental results and model predictions supports the accuracy and reliability of the proposed approach. These methods exhibit excellent performance in capacity planning and performance modeling tasks, providing valuable support for real-world applications.

Workload: The article focuses on bursty workloads commonly found in multi-tier systems and effectively detects burstiness symptoms without requiring precise identification of the underlying causes. By addressing burstiness, this research contributes to better understanding and handling of performance issues in multi-tier applications.

Innovation point: The proposed method introduces a novel way to incorporate burstiness symptoms into modeling techniques by capturing the IOD of service processes. This approach offers a practical and effective solution to address burstiness and improve the accuracy of performance predictions in multi-tier systems.

Performance: The experimental validation and model predictions support the effectiveness of the proposed method in dealing with bursty workloads. The close correspondence between the experimental results and predicted outcomes demonstrates the reliability of the approach and its ability to accurately estimate performance under different workloads.

Workload: The focus on bursty workloads in multi-tier applications highlights the importance of understanding and managing burstiness symptoms for better performance. By providing a method to detect and model burstiness in multi-tier systems, this work contributes to improved capacity planning and performance modeling in real-world scenarios.




