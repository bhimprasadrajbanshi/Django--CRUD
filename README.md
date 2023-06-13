## Django-CRUD
CRUD stands for Create, Read, Update & Delete. These are the four basic operations which are executed on Database Models. We are developing a web app which is capable of performing these operations.

<img src="https://drive.google.com/file/d/1wxyIs3ZM7VuGqbL2879u8yZHR8MGIc1k/view?usp=sharing" alt="photo">

### Code
#### Model
```python
 class Employees(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.IntegerField() 
    
    def __str__(self):
        return self.name
 ```

#### ADD operation
```python
def add(request):
    if request.method == "POST": 
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        
        emp.save()
        return redirect('index')
        
    return render(request,'index.html')

```

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
