# NLP-Sentiment

# How to use

1. Clone This repo
2. `cd web-app`
3. `pip install requirements.txt`
4. `python3 run.py`

# Routes

`/recommend`

```
    {
    "user_input": [0, 0, 0, 1, 1, 1, 0, 1],
    "N": 10
    }
```

output(indexed recommend):
```
{
    "top_N_indices": [
        402,
        488,
        316,
        96,
        480,
        2,
        492,
        40,
        490,
        430
    ]
}
```