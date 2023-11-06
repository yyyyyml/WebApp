## 文献总结




1. Title: Burstiness in Multi-tier Applications: Symptoms, Causes, and New Models (多层应用中的突发性：症状、原因和新模型)

2. Authors: G. Casale, N. Mi, E. Smirni

3. Affiliation: 无 (None)

4. Keywords: Capacity planning, multi-tier systems, transactions, sessions, bursty workload, bottleneck switch, index of dispersion.

5. Urls: [Paper](https://link.springer.com/chapter/10.1007%2F978-3-642-11623-0_5) [Github: None]

6. Summary: 
- (1): 本文研究的背景是企业系统中多层应用程序的工作负载经常表现为突发性，即存在一种时间相关性的形式。突发性往往导致用户感知性能大幅下降，而现有的容量规划模型很难捕捉到这种现象。
- (2): 过去的方法存在问题，无法准确捕捉突发性。本文提出了一种简单有效的方法来检测多层系统中的突发性症状，而无需确定突发性的低级精确原因。这种方法基于服务器的服务过程的离散指数，通过观察该服务器连接的繁忙周期内的完成数而得出。该离散指数以及其他反映“估计”的服务时间均值和第95个百分位的测量结果，用于推导出一个能够很好地捕捉真实服务过程的突发性和变化性的马尔可夫调制过程，尽管由于不准确和有限的测量而存在不可避免的误差。对通过HP（Mercury）Diagnostics获取的粗略测量结果的TPC-W测试平台进行了详细的实验，结果表明，所提出的技术在突发性和非突发性工作负载下都可以简单而有效地推断出服务时间过程的准确描述。实验和模型预测结果非常一致，充分证明了所提出方法的有效性。
- (3): 本文提出的研究方法是基于现有商业监控工具可以常规获得的测量结果。所得到的参数化模型在生产环境中适用于各种容量规划和性能建模任务，具有实用性和鲁棒性。
- (4): 该方法在容量规划和性能建模任务中取得了令人满意的性能，并能够支持研究目标。





8. Conclusion:

- (1): The significance of this work lies in addressing the challenge of burstiness in multi-tier applications, which often leads to a significant decrease in user-perceived performance. The existing capacity planning models struggle to capture this phenomenon accurately. This article proposes a novel approach to detect burstiness symptoms in multi-tier systems without the need to identify the precise underlying causes. This method leverages the discrete index of server service processes based on the observed completion count within busy periods of these connections. By utilizing this index, along with other measurements reflecting estimated service time mean and the 95th percentile, a Markov modulation process is derived to effectively capture the burstiness and variability of real service processes, despite the unavoidable errors due to inaccuracies and limited measurements. The experimental results obtained from detailed experiments on the TPC-W test platform using rough measurements obtained through HP (Mercury) Diagnostics demonstrate the effectiveness of the proposed technique in accurately describing the service time process under bursty and non-bursty workloads. The consistency between the experiments and model predictions confirms the validity of the proposed method.

- (2): 
    - Innovation point: This article introduces a simple yet effective method to detect burstiness symptoms in multi-tier systems by leveraging the discrete index of server service processes. This approach is innovative as it does not require precise identification of the low-level causes of burstiness, making it easier to apply in practical scenarios.

    - Performance: The proposed method achieves satisfactory performance in capacity planning and performance modeling tasks. By accurately capturing burstiness and variability in service time processes, it provides valuable insights for optimizing system performance and resource allocation.

    - Workload: This article focuses on bursty workloads in multi-tier applications and effectively addresses the challenge of capturing burstiness symptoms. However, the proposed method relies on rough measurements obtained through commercial monitoring tools, which may introduce errors and limitations. Further research could explore techniques to enhance the accuracy and robustness of the measurements.

In summary, this work is significant in addressing burstiness in multi-tier applications and introduces a novel approach to detect burstiness symptoms. The innovation lies in the use of the discreet index of server service processes, which simplifies the problem of identifying underlying causes. The proposed method demonstrates satisfactory performance in capacity planning and performance modeling tasks and can be applied in various production environments. However, reliance on rough measurements may introduce errors, which could be a potential limitation.




