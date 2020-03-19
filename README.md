# Description
Rule-based insult classifier for the Russian language

# Requirements

Python 3.6+
Rule-based insult classifier stands on the shoulders of a giants:
- `pymorphy2`
- the assembled twitter-based dataset

# Installation
```
pip install git+https://github.com/kudep/rus_rule_based_insult_classifier
```


# Example
```
>>> from rus_rule_based_insult_classifier.core import insult_classifier
>>> text = "Ночь, улица, фонарь, аптека"
>>> insult_classifier(text)
False
>>> text = "Cука"
>>> insult_classifier(text)
True

```
