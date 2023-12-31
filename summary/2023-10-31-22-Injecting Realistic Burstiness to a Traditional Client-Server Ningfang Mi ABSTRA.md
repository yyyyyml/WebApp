## 文献总结




1. Title: Injecting Realistic Burstiness to a Traditional Client-Server (通过向传统客户端-服务器系统注入真实的突发性)

2. Authors: Ningfang Mi

3. Affiliation: None

4. Keywords: deep learning, autonomic systems, burstiness, client-server benchmarks

5. Urls: None, Github: None

6. Summary:
- (1): 该论文的研究背景是自主系统设计中的基准测试，该测试需要考虑真实的突发性负载对系统性能的影响。
- (2): 过去的方法中存在的问题是现有的客户端-服务器基准测试无法注入突发性负载。本文的方法启发性良好，旨在提供一种可控制的方法，能够模拟突发性工作负载并用于评估系统性能。
- (3): 本文提出了一种新的研究方法，通过使用离散指数参数来注入突发性负载，实现对客户端到服务器到到达过程的控制。作者还修改了TPC-W基准测试，并实现了新模块用于注入突发性负载。
- (4): 该方法在真实系统上进行了详细的实验，证明了该方法的有效性和健壮性。通过该方法，可以模拟不同程度的突发性负载，从而对自主系统的容量规划提供有用的依据。
7. Methods:

- (1): 本文的方法思路是通过修改TPC-W基准测试中的思考时间生成方式，以实现对进入流量的突发性注入。作者使用了Markovian Arrival Processes（MAPs）作为流量模型来生成网络流量的思考时间。MAPs可以提供不同级别的变化以及时序关系，以模拟流量的突发性特征。

- (2): 在MAP模型中，作者使用了两个状态的MAP，一个状态生成“短”思考时间，表示用户产生紧密连续的到达，可能导致突发；另一个状态生成“长”思考时间，表示正常流量的到达。通过调节这两个状态的到达速率和状态转换概率，实现了流量突发和持续时间的控制。

- (3): 进一步地，为了调节流量突发程度，作者提出使用离散指数参数作为调节器。这个指数参数反映了流量的突发性程度，可以通过调节它的值来控制不同程度的流量突发。

- (4): 本文还通过实验证明了该方法的有效性和健壮性，并且指出该方法可以应用于其他具有闭环结构和思考时间的基准测试。





8. Conclusion:

- (1): 重要性：本研究的重要性在于提供一种可控制的方法来模拟真实的突发性工作负载，并用于评估自主系统的性能。当前的基准测试方法无法注入突发性负载，而该研究提出的方法填补了这一空白，对自主系统设计和容量规划有着重要的指导意义。

- (2): 创新点：
    - 本文提出了使用离散指数参数来控制流量的突发性负载，这是一种新的思路。通过调节离散指数参数的值，可以控制突发性负载的程度，使得测试更精细和实用。
    - 文中修改了TPC-W基准测试，并实现了新模块用于注入突发性负载。这个修改能够生成具有突发性特征的网络流量，使得评估系统性能更加准确和可靠。

- (3): 性能：
    - 通过实验证明了该方法在真实系统上的有效性和健壮性。作者使用真实环境进行了详细的实验，并展示了该方法能够准确模拟不同程度的突发性负载。这表明该方法在自主系统性能评估中具有较高的可行性和适用性。

- (4): 工作量：
    - 本研究修改了TPC-W基准测试，并增加了新模块用于注入突发性负载。这需要对基准测试进行深入理解和改造，并且需要在真实系统上进行详细的实验和验证。因此，在实施该方法时需要一定的工作量和技术投入。

该研究对于提高自主系统性能评估的准确性和实用性具有重要的意义。通过注入真实的突发性工作负载，可以更加全面地评估系统的容量规划和并发处理能力，进一步推动自主系统领域的发展。不过，该研究的具体实施需要一定的工作量，并且需要更多的实验和验证来进一步证明其适用性和可行性。总体而言，该研究是在自主系统设计中基准测试领域的一次有益的探索。




