# Weibo

## Fan attention

```python
'select * from animals where user_id=%s'
```

- Source: animal_inventory.py
- Description:
  - I select all the animals because I need their information to count them when I do the inventory.
- Data:
  - user_id: str - the id of the user that owns the animal


```python
'insert into fans_attention values(%s,%s,%s,%s,%s,%s,%s)'
```

- Source: save_person_information.py
- Description: 
  - insert bla bla bla. Then I update it every bla bla bla. I do this because bla bla.
- Data:
  - name: str - the name of the user
  - age: int - the age of the user (sometimes NULL)
  - blabla
  - ...
- Update frequency:
  - The data inserted here is updated every 5 minutes when I check for bla bla.

