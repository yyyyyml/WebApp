## Paper:1




1. Title: "Good Robot!"：高效转化强化学习用于多步骤视觉任务的Sim to Real

2. Authors: Andrew Hundt, Benjamin Killeen, Nicholas Greene, Hongtao Wu, Heeyeon Kwon, Chris Paxton, and Gregory D. Hager

3. Affiliation: 华盛顿附近约翰·霍普金斯大学 (The Johns Hopkins University, Baltimore, MD 21218, USA)

4. Keywords: Computer vision for other robotic applications, deep learning in grasping and manipulation, reinforcement learning

5. Urls: Paper: [link](https://ieeexplore.ieee.org/document/9176844), Github: [link](https://github.com/jhulcsr/good_robot)

6. Summary: 

- (1): 本文的研究背景是针对长期多步骤任务，当前的强化学习算法在其中面临浪费时间在错误的探索和任务进度容易逆转的挑战。

- (2): 过去的方法在长期多步骤任务中经常出现问题，因为它们无法有效地解决探索阶段的时间浪费和进度逆转问题。本文提出了一种有动机的方法来解决这些问题。

- (3): 本文提出了Schedule for Positive Task (SPOT)框架，该框架在行动安全区域内进行探索，学习有关不安全区域的信息而无需真正探索它们，并优先考虑逆转先前进展的经验，从而实现了学习效率的显著提高。

- (4): 该方法在模拟环境中成功完成了各种任务的试验，如堆叠4个方块的成功率从13%提高到100%，创建4个方块行的成功率从13%提高到99%，以及清除陷阱布局的玩具的成功率从84%提高到95%。平均每次试验中的行动效率通常提高了30%以上，而训练所需的行动次数为1-20k，具体取决于任务的复杂程度。此外，本文还展示了直接的模拟到真实世界的转移，通过直接加载模拟训练的模型到真实机器人，无需额外的真实世界微调，实现了在真实环境中构建立方体堆叠和行创建的100%成功率。综上，本文是首个成功应用于长期多步骤任务（如块状堆叠和行创建）的强化学习与模拟到真实世界转移，并且在任务上实现了较好的性能，能够支持其目标的实现。
7. Methods: 

  - (1): 本文采用Schedule for Positive Task（SPOT）框架来解决长期多步骤任务中的问题。SPOT框架通过在安全区域内进行探索，学习有关不安全区域的信息，并优先考虑逆转先前进展的经验来提高学习效率。

  - (2): 在问题建模方面，本文将任务定义为马尔可夫决策过程（Markov Decision Process，MDP）并使用Q-learning算法来估计动作的质量，选择具有最大预期奖励值的动作。

  - (3): 本文还引入了奖励塑造（Reward Shaping）技术，通过优化奖励函数来训练神经网络，以提高策略的学习效率。其中，引入了基于子任务权重的基准奖励函数和稀疏近似任务进度函数来指示任务的整体进展。

  - (4): 为了加速训练和减少无效尝试，本文利用动态动作空间的概念，通过先验知识中的"预测失败"指示器对可能失败的动作进行预测，从而优化训练过程中的动作选择。

  - (5): 为了解决动作失败对训练的影响，本文提出了Situation Removal（SR）的概念，通过将失败动作的奖励设置为零，阻止奖励通过失败动作传播，从而聚焦于能够完成任务的短暂和成功序列。

  - (6): 本文提出的SPOT-Q Learning算法结合了SPOT框架、奖励塑造和动态动作空间的思想，通过使用已知的环境信息来选择最优动作，并进行目标值函数的更新和





8. Conclusion: 

    - (1): The significance of this piece of work lies in its successful application of reinforcement learning with sim to real transfer in long-term multi-step tasks, such as block-stacking and creating rows. It addresses the challenges of wasteful exploration and progress reversal, improving learning efficiency and supporting the achievement of the desired goals.

    - (2): Innovation point: The authors propose the Schedule for Positive Task (SPOT) framework, which combines exploration within safe areas, learning about unsafe areas without actual exploration, and prioritizing the reversal of previous progress. This approach significantly improves learning efficiency in long-term multi-step tasks.

    Performance: The SPOT framework achieves impressive results in various tasks, with success rates for stacked blocks increasing from 13% to 100%, success rates for creating rows of blocks increasing from 13% to 99%, and success rates for clearing trap layouts of toys increasing from 84% to 95%. The action efficiency in each trial is improved by over 30%, and the training requires only 1-20k actions, depending on the task complexity. Moreover, successful sim to real transfer is demonstrated, achieving 100% success rates in real-world tasks without additional fine-tuning.

    Workload: The proposed SPOT-Q Learning algorithm incorporates the SPOT framework, reward shaping, and dynamic action space optimization. While the methods are effective, future research can explore ways to incorporate task structures and learn action space masks to further optimize the workload. Investigation into the differences in sim to real transfer for different types of tasks (such as pushing and grasping) can also be pursued.

Please note that proper nouns in English have been marked as required.




