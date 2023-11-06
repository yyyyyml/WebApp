## 文献总结




1. Title: BURN: Enabling Workload Burstiness (使工作负载突发性) 

2. Authors: G. Casale, A. Kalbasi, D. Krishnamurthy, and J. Rolia 

3. Affiliation: G. Casale is affiliated with IMDEA Networks Institute, Madrid, Spain 

4. Keywords: Benchmarking, performance, burstiness, bottleneck migration, overdemand 

5. Urls: [Paper Link](xxx), [Github Code Link](None) 

6. Summary: 

- (1): 这篇论文的研究背景是测试多层应用程序在变化的资源使用条件下的自定义基准。 

- (2): 过去的方法存在问题，该方法有很好的动机。 

- (3): 论文提出了一种基于模型的技术，使用马尔可夫模型描述每个测试工作负载的资源消耗模式，并生成一个策略来设置不同资源上的目标请求混合和用户指定的突发程度。 

- (4): 该方法在多层应用程序测试平台上进行了案例研究，能够对会话服务需求的突发程度进行精细控制和预测。实验表明，对于任何给定的请求混合，该方法可以暴露出与非突发性的工作负载相比具有相同请求混合的延迟和吞吐量下降。
7. Methods:

- (1): The paper proposes the BURN methodology for generating a benchmark with controlled burstiness in service demands. It takes as input a test suite mix vector provided by the user, which describes the percentage of sessions to be drawn from each test suite, and test suite demand models.

- (2): The session submission policy (P) is a discrete-time Markov chain that determines the sequence of sessions submitted to the system. The probabilities in P are defined to match the desired test suite mix vector (γ) and target burstiness.

- (3): The composition step of BURN predicts the service demand burstiness created at different resources by a benchmark. It utilizes Markovian arrival processes (MAPs) to describe the burstiness and temporal dependence in the workload. The MAPs are derived from the test suite demand models and the session submission policy.

- (4): By analyzing the bursts and bottleneck migrations, BURN enables the generation of benchmarks that exhibit dynamic bottleneck switches and controlled burstiness in service demands.

- (5): The moments and burstiness in the service demands for each resource can be estimated using closed-form analytical expressions based on the benchmark burstiness model (Di0, Di1).

- (6): BURN allows the estimation of the average service demand and maximum session arrival rate that do not saturate any resource, facilitating performance evaluation of systems under bursty workloads.

- (7): The proposed methodology is evaluated through case studies on a multi-tier application testing platform, demonstrating fine-grained control and prediction of workload burstiness.

- (8): The BURN methodology provides a novel approach for generating customizable benchmarks that capture burstiness properties and enable realistic performance testing scenarios in multi-layer applications.





8. Conclusion:

- (1): The significance of this work lies in its ability to generate customizable benchmarks with controlled burstiness in service demands. This allows for realistic performance testing scenarios in multi-layer applications, providing valuable insights into system behavior under varying workload conditions.

- (2): 
- 创新点 (Innovation point): The BURN methodology proposes a novel approach for generating benchmarks with customizable burstiness, utilizing Markovian arrival processes (MAPs) to describe burstiness and temporal dependence in the workload. This innovation enables the fine-grained control and prediction of workload burstiness, providing a valuable tool for performance evaluation.
- 性能 (Performance): The experimental results on a multi-tier application testing platform demonstrate the accuracy and effectiveness of the proposed models in predicting service demands and their burstiness. The methodology allows for the estimation of average service demand and maximum session arrival rate without resource saturation, making it an efficient approach for evaluating system performance.
- 工作量 (Workload): The BURN methodology addresses the challenge of creating benchmarks that capture burstiness properties in service demands. It enables the generation of benchmarks with controlled burstiness, facilitating the evaluation of system performance under realistic workload conditions and stress scenarios.

Please note that the above conclusions are based on the information provided in the given summary and may not fully reflect the actual content and findings of the article.




