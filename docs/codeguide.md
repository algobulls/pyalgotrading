
!!! Note
    This will be a frequently updated page. Keep visiting to know what's new!
    
This page helps you to understand the best practices to create a good strategy.

## List of Guidelines
---
1. The following Python packages/modules are available to you:

    | Package / Module | Version |
    |------------------|---------|
    | [**TA-Lib**](https://mrjbq7.github.io/ta-lib/install.html)       | 0.4.17  |
    | [**pandas**](https://pypi.org/project/pandas/)       | 1.1.1   |
    | [**numpy**](https://pypi.org/project/numpy/)        | 1.16.3  |

2. The strategy class should not import any packages/modules.
3. The entire strategy should be a single Python class.
---

!!! Note
    * Pandas is available with limited functionality. Direct printing of dataframes is disabled.
    * It is a good idea to include the version number while installing a package using `pip`.
    * Example - `pip install numpy==1.16.3` 

You may get the following message if the strategy fails to adhere to the guidelines.

```
Strategy breached code of conduct. Please adjust your strategy to follow guidelines and run again. Halting strategy...
```
