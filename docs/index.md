
# Phoenix

## AlgoBulls

Welcome to AlgoBulls, the AI-powered trading platform that unlocks new dimensions in algorithmic trading. Our mission is to boost your expertise in designing and executing personalised trading strategies using our cutting-edge product - **Phoenix**. 

---

## Introducing **Phoenix**: Your Gateway to Algorithmic Trading

**Phoenix** is your ultimate companion for crafting and executing trading strategies with the precision of a seasoned professional. Designed for both experienced traders and newcomers, this platform offers a range of powerful tools that empower you to make well-informed decisions and trade confidently in dynamic financial markets.

When it comes to strategy development, **Phoenix** lets you dive into coding, backtesting, and deploying your trading strategies with remarkable ease. With an intuitive interface, you gain the ability to precisely set entry and exit points, handle multiple instruments, and take actions based on informed insights.

![algo trading basic image](imgs/python_build_basic_a.png)

What sets **Phoenix** apart is its adaptable strategy format, suitable for various trading styles. Whether you're into backtesting, paper trading, or live trading, the same strategy code works for all three, making the experience straightforward.

The library covers all scenarios (**backtesting**, **paper trading**, and **live trading**) during strategy execution or generating analytics. This unified approach ensures seamless transitions between these modes, eliminating the need for complex adjustments. Additionally, it simplifies the creation of progress logs, helping you track your journey and anticipate completion times. For real-time updates, live logs are available too, offering transparency and control over your trading endeavours.

![algo trading basic image](imgs/algotrading_basic_4.png)

**Phoenix**'s strength lies in its seamless integration with real-time market data sources, historical data, and trading platforms. Its adaptable nature enables connection with various data providers and broker APIs, ensuring access to the information you need for well-informed trading decisions.

---

## Powerful Stats & Visual Analytics
<p align="center">
  <img src="imgs/analytics_mascot.svg" alt="algo trading basic image"/>
</p>

In the pursuit of successful trading, **Phoenix** equips you with advanced visual tools for strategy analytics. These tools provide a deeper understanding of your strategies' performance, helping you manage risks and fine-tune your plans for optimal success. Visualisations facilitate data-driven decision-making, giving you clearer insights into the intricacies of your trading activities.

---
## Multiple Platforms to use Phoenix

To support our diverse community of users, we have the options of two dynamic platforms for our users to use Phoenix - **pyalgotrading** and **Phoenix Web**

[Explore our Python Package: Pyalgotrading](pyalgotrad/introduction.md){ .md-button }

[Dive into the amazing Features of our Web-App: Phoenix Web](python_build/python-build-introduction.md){ .md-button }

---

## Join the Community

AlgoBulls is more than just a platform; it's a community. Connect, learn, and collaborate with traders and developers. Code your strategies or explore ours – AlgoBulls is where innovation meets trading expertise.

By becoming part of the **Phoenix** community, you tap into a rich network of traders and developers. This community serves as a platform for collaboration, offering guidance, valuable insights, and collective refinement of trading strategies. Diverse perspectives help you approach trading challenges from multiple angles, fostering growth and improvement.

Join us in this journey as AlgoBulls revolutionizes algorithmic trading!

In essence, **Phoenix** is more than a product; it's your comprehensive guide to mastering algorithmic trading. With its user-friendly interface, diverse functionalities, and seamless integration, it's a valuable asset for traders of all levels. By simplifying strategy crafting, integration, execution, and analysis, **Phoenix** empowers you to navigate the trading world with confidence and precision.

## Open Source Strategy Library

We maintain an open source GitHub repository, [pyalgostrategypool](https://github.com/algobulls/pyalgostrategypool){target=_blank} containing fully functional algorithmic trading strategies. These strategies can be used for Backtesting, Paper Trading, or Live Trading across various brokers and exchanges. The same code works in all trading modes.

!!!tip "Keep an eye on our GitHub repo"
    Our team periodically updates the library to add more strategy Python codes

For those new to algorithmic trading or **Phoenix**, exploring included example strategies is an excellent starting point. These strategies are pre-built scenarios showcasing different trading strategies and concepts. By studying and experimenting with these examples, you'll gain a deeper grasp of how **Phoenix** operates and how strategies are constructed.


Here's what you can do with the example strategies:

- **Analyze Structure**: Study code structure, including strategy definition, condition setting, and action execution.
- **Modify and Experiment**: Once comfortable with examples, customise them to your preferences. Adjust parameters, conditions, and actions to observe their impact on trading outcomes.

- **Learn Strategies**: Each example represents a different trading approach, like trend-following or mean-reversion. Studying these examples introduces you to various trading strategies and their underlying principles.

Remember, these example strategies lay the foundation for your learning journey. As you grow more familiar with the library, you can create and customise your own strategies based on your insights and preferences.

To conclude, the installation process readies you to use **Phoenix**, while the documentation and example strategies empower you to explore the library's capabilities and apply them to real trading situations. Whether you're a beginner or a seasoned trader...

---
## Limitations of **Phoenix**

In the exciting world of algorithmic trading, **Phoenix** offers numerous benefits and considerations for traders and developers. Let's also acknowledge its limitations to help you make an informed decision.
<p align="center">
  <img src="imgs/pros_n_cons.svg" alt="algo trading basic image", width="400px"/>
</p>

1. **Python Speed Limitations:**  While versatile, Python isn't the fastest language for computation. This may pose challenges for complex strategies requiring extensive calculations. Our team is actively transitioning a major part of the codebase to Cython to enhance speed while retaining Python's simplicity. We're also exploring options like GPUs for the future.

2. **Cloud Cold-Start Speed Limitations:** Each strategy runs on a dedicated virtual server in the cloud. While this ensures secure execution with dedicated resources, there's a short delay as the cloud fetches the resource before strategy execution begins. This minor delay is part of our ongoing optimization efforts.


!!! tip "Note"
    Our team is working round the clock to make these limitations a thing of the past.

---
## References

To unleash **Phoenix**'s full potential, dive into its comprehensive documentation. This roadmap offers detailed insights into the product's features, functionalities, and capabilities. It's your go-to resource for harnessing the power of **Phoenix** effectively. The documentation includes:


- **[Code Examples](https://github.com/algobulls/pyalgostrategypool){target=_blank}**: Real code snippets showcasing how to implement specific strategies, functions, and techniques using **Phoenix**.
- **[Python Cookbook for Algorithmic Trading](https://www.amazon.in/Python-Algorithmic-Trading-Cookbook-algorithmic/dp/1838989358){target=_blank}**: A Python Cookbook for Algorithmic Trading, explaining in-depth about strategy creation and execution from scratch using Python. Explore the technical content of the book on [GitHub](https://github.com/PacktPublishing/Python-Algorithmic-Trading-Cookbook){target=_blank}.

