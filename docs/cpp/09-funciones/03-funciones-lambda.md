title: Funciones Lambda (anónimas) | Apuntes lenguaje C++ | Hektor Profe
description: Funciones Lambda (anónimas) | Apuntes lenguaje C++

# Funciones Lambda (anónimas) en C++

Una función **Lambda o anónima** es una función sin nombre, definida y utilizada in-situ. Su estructura es muy interesante:

```cpp
// Definición básica y uso
auto hola = []() { std::cout << "Hola mundo!" };
hola(); // Hola mundo!
```

Puedes aceptar parámetros, pudiendo enviarse explícitamente después de la definición a forma de llamada:

```cpp
// Uso directo con parámetros
std::cout << [](double a, double b) { return (a + b); }(5, 4);  // 9
```

También permiten la captura de valores enlistados justo al principio de la definición:

```cpp
// Captura por valor en lista
double a{10}, b{15};
auto suma = [a, b]() { std::cout << "a+b: " << a + b; };
suma(); // a+b: 25
```

También se puede capturar los valores por referencia:

```cpp
// Captura por referencia en lista
int c{25};
std::cout << "&c ex: " << &c;
auto imprimir = [&c]() { std::cout << "&c in: " << &c; }; // 0x3e6ddffb9c
imprimir(); // 0x3e6ddffb9c
```

Podemos enviar a la función **Lambda** todo el contexto de variables definidas por valor con el operador `=`:

```cpp
// Captura de todo el contexto por valor
auto imprimir_contexto_valor = [=](){
    std::cout << "&a in: " << &a << ", &b in: " << &b << ", &c in: " << &c;
};
std::cout << "&a ex: " << &a << ", &b ex: " << &b << ", &c ex: " << &c;
imprimir_contexto_valor();
```
 
```
&a ex: 0x3e6ddffbc0, &b ex: 0x3e6ddffbb8, &c ex: 0x3e6ddffb9c
&a in: 0x3e6ddffb70, &b in: 0x3e6ddffb78, &c in: 0x3e6ddffb80
```

O por referencia mediante el operador `&`:

```cpp
// Captura de todo el contexto por referencia
auto imprimir_contexto_referencia = [&]() {
    std::cout << "&a in: " << &a << ", &b in: " << &b << ", &c in: " << &c;
};
std::cout << "&a ex: " << &a << ", &b ex: " << &b << ", &c ex: " << &c;
imprimir_contexto_referencia();
```
 
```
&a ex: 0xac75bff670, &b ex: 0xac75bff668, &c ex: 0xac75bff64c
&a in: 0xac75bff670, &b in: 0xac75bff668, &c in: 0xac75bff64c
```

___
<small class="edited"><i>Última edición: 09 de Mayo de 2022</i></small>