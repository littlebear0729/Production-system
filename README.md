# Production system

### Usage

1. Install dependency `pip install pick`

2. Add conditions in `db.txt`

3. Run program `python identify_system.py`

4. Select all conditions via `UP/DOWN arrow` and `space` key, you should select at least one condition

5. Hit `Enter` to see conclusion

### About db.txt

Number, Conditions and Conclusions should be added in `db.txt` in specified format like this: `<Number>: IF <Condition1> [& <Condition2>...] THEN <Conclusion>`

For example: `R12：IF 被子植物 & 蔷薇科 & 木本 & 可食用 & 结果实 -> 苹果树`

What's more, a line start with a single character "`#`" is a commented line, which will not be processed

### Conclusions

1. If no conclusion, an alert will give

2. If only one conclusion matched, the one will be printed out

3. If multiple conclusions matched, an alert will give and the first one will be printed

### Copyright

Haonan Xiong, 2022

MIT License
