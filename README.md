## Django-CRUD
CRUD stands for Create, Read, Update & Delete. These are the four basic operations which are executed on Database Models. We are developing a web app which is capable of performing these operations.

<img src="https://drive.google.com/file/d/1wxyIs3ZM7VuGqbL2879u8yZHR8MGIc1k/view?usp=sharing" alt="photo">

###Code

#### DELETE operation
```python
 def delete(request, Employees_id):
    Employees_id = int(Employees_id)
    print("id Employees" + Employees_id)
    print("id Employees" + Employees_id)
    print("id Employees" + Employees_id)
    try:
        Employees_sel = Employees.objects.get(id = Employees_id)
    except Employees.DoesNotExist:
        return redirect('index.html')
    Employees_sel.delete()
    return render(request,'index.html')
```
