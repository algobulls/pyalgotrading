# Prerequisites

You will need the following to start with Pyalgotrading:

1. ### **[AlgoBulls Account](https://www.algobulls.com/){target=_blank}**
    To upload and test your strategies, you will need this account. You can create your account for FREE on the [Algobulls website](https://app.algobulls.com/user/register){target=_blank}.

2. ### Developer Key
To access the features, you will need a developer key. The key can be obtained as follows:
    - **Step 1**: Activate the [Advanced Developer Plan](https://app.algobulls.com/pricing?section=Developers){target=_blank} from the **Pricing** menu.
    [![purchase plan](imgs/purchase_plan.png)](imgs/purchase_plan.png)
    - **Step 2**: Get the [Developer Key](https://app.algobulls.com/settings?query=eyJpc0xpdmUiOiJ0cnVlIn0%3D&section=developerOptions){target=_blank} from the **Settings** section.
    [![developer key](imgs/developer_key.png)](imgs/developer_key.png)
    !!! Note "Please Note"
         For security reasons, the **developer key** will get reset every time you log out from your AlgoBulls account.
    Once you have the developer key, you can access the AlgoBulls platform using `pyalgotrading` functions.   

3. ### **[Python 3.10+](https://www.python.org/downloads/){target=_blank}**
  The Pyalgotrading platform can run all strategies that conform to Python 3.8 or higher. However, we recommend Python 3.10 or higher. 

    !!! Tip "Python Tips"
        * It is a good idea to set up a virtual environment first while installing Python 3.10.
        * Once Python is installed, most packages are easily installed in your venv using `pip install` command
    
4. ### **[Pyalgotrading Package](https://pypi.org/project/pyalgotrading/){target=_blank}**  
  To create and execute your fully automated trading strategies, you only need to install `pyalgotrading`. You can install the `pyalgotrading` package using the following command:
    ```shell
    pip install pyalgotrading
    ``` 

5. ### **[Jupyter Notebook](https://jupyter.org/install){target=_blank}**
  You will use a Jupyter Notebook to connect to the AlgoBulls platform. Using the notebook, you can upload the strategy, test your strategy (Backtesting, Paper Trading, or Real Trading), and fetch logs.  
       Install Jupyter Notebook using the following command:  
       ```
       pip install jupyter
       ```

    !!! Tip "Pro Tip"
           If you are an experienced Pyalgotrading user, Jupyter Notebook might not be necessary. You can directly integrate it into your application.

6. ### Enhancing Productivity
For enhancing your productivity while building and executing strategies using Pyalgotrading, you can make use of Python IDEs of your choice, such as:
    - **[PyCharm](https://www.jetbrains.com/pycharm/download/){target=_blank}**
    - **[VS Code](https://code.visualstudio.com/){target=_blank}**
    
