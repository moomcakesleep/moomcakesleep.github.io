# 实数r的n次方根近似公式及推导过程

## 公式

$x_{n+1}=\frac{1}{a}\left[(a-1) x_{n} +\frac{r}{x_{n}^{a-1}}\right]$

## 推导过程
设 $f\left ( x \right ) = x^{n} - r$ ，根据牛顿迭代公式$x_{n+1} = x_{n} - \frac{f\left ( x_{n} \right ) }{f'\left ( x_{n} \right )   }$，则有
$x_{n+1}=x_{n} - \frac{x_{n}^{a}-r}{ax_{n}^{a-1}}
等式右边进行通分，得
$x_{n+1}=\frac{ax_{n}^{a}-x_{n}^{a}+r}{ax_{n}^{a-1}}$
等式右边上下同时约去$ax_{n}^{a-1}$，得
$x_{n+1}=\frac{ax_{n}-x_{n}+\frac{r}{x_{n}^{a-1}}}{a}$
变形，得
$x_{n+1}=\frac{1}{a} \left [\left ( a-1 \right )x_{n}+\frac{r}{x_{n}^{a-1}} \right ]$
