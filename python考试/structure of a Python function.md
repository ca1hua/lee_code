Python 中的函数是代码组织的基本单元，它允许你封装一段可以重复使用的代码。了解函数的结构和如何定义它们对学习 Python 非常重要。下面我会介绍 Python 函数的基本结构和一些常用概念。

### 1. 函数的基本结构

在 Python 中，函数的定义使用 `def` 关键字，后跟函数名称、括号和参数列表。函数体部分缩进，表示函数内部的代码。

#### 语法结构：

```python
def 函数名(参数1, 参数2, ...):
    # 函数体
    # 执行一些操作
    return 返回值  # 可选
```

- **def**：用于定义函数。
- **函数名**：为你的函数取一个名字。
- **括号**：用于括住函数的参数。如果没有参数，可以省略括号。
- **函数体**：包含函数内部要执行的代码。
- **return**：用于返回一个值给函数的调用者。如果没有返回值，可以省略 `return`。

### 2. 示例：定义一个简单的函数

例如，定义一个计算两个数字和的函数：

```python
def add(a, b):
    result = a + b
    return result
```

在这个例子中：

- `add` 是函数名。
- `a` 和 `b` 是参数。
- `result` 存储计算结果，`return result` 返回结果给函数调用者。

#### 调用函数：

```python
print(add(3, 5))  # 输出：8
```

### 3. 参数和返回值

- **参数**：函数可以接受零个或多个参数，参数是传递给函数的信息。你可以在函数体内使用这些参数。
- **返回值**：使用 `return` 语句返回一个值。没有 `return` 时，函数默认返回 `None`。

### 4. 默认参数值

函数的参数可以有默认值，这意味着如果调用函数时没有传递这些参数，它们会使用默认值。

```python
def greet(name="World"):
    print(f"Hello, {name}!")
```

#### 调用方式：

```python
greet()  # 输出：Hello, World!
greet("Alice")  # 输出：Hello, Alice!
```

### 5. 可变数量的参数

有时你可能不确定函数会接收多少个参数。Python 提供了几种方式来处理这种情况。

- **`\*args`**：用于接受多个位置参数（非关键字参数）。
- **`\**kwargs`**：用于接受多个关键字参数。

#### 示例：

```python
def print_args(*args):
    for arg in args:
        print(arg)

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_args(1, 2, 3)  # 输出 1 2 3
print_kwargs(a=1, b=2)  # 输出 a: 1 b: 2
```

### 6. 函数的作用域

在函数内部定义的变量仅在函数体内有效，这称为**局部变量**。如果在函数外部定义一个变量，函数无法访问它，这称为**全局变量**。不过，可以通过 `global` 关键字来修改全局变量。

```python
x = 10  # 全局变量

def change_global():
    global x
    x = 20

change_global()
print(x)  # 输出：20
```

### 7. 高阶函数

Python 允许函数作为参数传递给其他函数，或者返回函数作为结果。这样做的函数被称为**高阶函数**。

#### 示例：函数作为参数

```python
def apply_function(func, value):
    return func(value)

def square(x):
    return x * x

print(apply_function(square, 5))  # 输出：25
```

### 总结

Python 中的函数是代码重用的基础，它们有助于将复杂的问题分解为更小、更易于管理的部分。了解函数的基本结构、参数传递、返回值及其作用域，会帮助你编写更加高效和模块化的代码。

如果有更具体的方面你想了解，或者有示例问题，随时告诉我！