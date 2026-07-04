# Volume III - Classical Analysis Proofs To Do

Proof-writing order is dependency-first among active TODO proof labels, with the generated knowledge graph order used as the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 465
Completed in this tracker: 6

1. () `prop:little-o-quotient-characterization` — **Little-o Quotient Characterisation**
   > **Statement.**
   > Let $a\in\mathbb{R}$, and let $f$ and $g$ be real-valued functions defined on a
   > punctured neighbourhood of $a$, with $g(x)\neq 0$ for $x$ sufficiently close to
   > $a$ and $x\neq a$. Then
   > \[
   >  f(x)=o(g(x))\ (x\to a)
   >  \quad\Longleftrightarrow\quad
   >  \frac{f(x)}{g(x)}\to 0\ (x\to a).
   > \]

2. () `prop:little-o-sum-rule` — **Sum Rule for Little-o**
   > **Statement.**
   > If $f_1(x)=o(g(x))$ and $f_2(x)=o(g(x))$ as $x\to a$, then
   > \[
   >  f_1(x)+f_2(x)=o(g(x))\qquad (x\to a).
   > \]

3. () `prop:little-o-bounded-factor-rule` — **Bounded Factor Rule for Little-o**
   > **Statement.**
   > If $f(x)=o(g(x))$ as $x\to a$ and $m$ is bounded near $a$, then
   > \[
   >  m(x)f(x)=o(g(x))\qquad (x\to a).
   > \]

4. () `thm:ineq-add-both-sides` — **Addition Preserves Strict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a < b \;\Rightarrow\; a + c < b + c.
   > \]

5. () `thm:ineq-nonstrict-add-both-sides` — **Addition Preserves Nonstrict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a \le b \;\Rightarrow\; a + c \le b + c.
   > \]

6. () `thm:ineq-transitivity-strict` — **Transitivity of Strict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a < b \;\land\; b < c \;\Rightarrow\; a < c.
   > \]

7. () `thm:ineq-add-inequalities` — **Addition of Strict Inequalities**
   > **Statement.**
   > For all $a, b, c, d \in \mathbb{R}$,
   > \[
   >  a < b \;\land\; c < d \;\Rightarrow\; a + c < b + d.
   > \]

8. () `thm:ineq-nonstrict-add-inequalities` — **Addition of Nonstrict Inequalities**
   > **Statement.**
   > For all $a, b, c, d \in \mathbb{R}$,
   > \[
   >  a \le b \;\land\; c \le d \;\Rightarrow\; a + c \le b + d.
   > \]

9. () `thm:ineq-transitivity-mixed` — **Mixed Transitivity**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a \le b \;\land\; b < c \;\Rightarrow\; a < c.
   > \]

10. () `thm:ineq-mixed-add` — **Mixed Addition of Inequalities**
   > **Statement.**
   > For all $a, b, c, d \in \mathbb{R}$,
   > \[
   >  a \le b \;\land\; c < d \;\Rightarrow\; a + c < b + d.
   > \]

11. () `thm:ineq-multiply-positive` — **Multiplication by a Positive Scalar Preserves Strict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a < b \;\land\; 0 < c \;\Rightarrow\; ac < bc.
   > \]

12. () `thm:ineq-multiply-negative` — **Multiplication by a Negative Scalar Reverses Strict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a < b \;\land\; c < 0 \;\Rightarrow\; ac > bc.
   > \]

13. () `thm:ineq-nonstrict-multiply-positive` — **Multiplication by a Positive Scalar Preserves Nonstrict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a \le b \;\land\; 0 < c \;\Rightarrow\; ac \le bc.
   > \]

14. () `thm:ineq-nonstrict-multiply-nonneg` — **Multiplication by a Nonneg Scalar Preserves Nonstrict Inequality**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a \le b \;\land\; 0 \le c \;\Rightarrow\; ac \le bc.
   > \]

15. () `thm:ineq-squeeze` — **Squeeze**
   > **Statement.**
   > For all $a, b, c \in \mathbb{R}$,
   > \[
   >  a \le b \le c \;\land\; a = c \;\Rightarrow\; b = a.
   > \]

16. () `thm:ineq-reciprocal-positive` — **Reciprocal Reverses Strict Inequality for Positives**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$,
   > \[
   >  0 < a < b \;\Rightarrow\; 0 < \frac{1}{b} < \frac{1}{a}.
   > \]

17. () `thm:ineq-reciprocal-flip` — **Reciprocal Equivalence for Positives**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$ with $a > 0$ and $b > 0$,
   > \[
   >  a < b \iff \frac{1}{b} < \frac{1}{a}.
   > \]

18. () `thm:ineq-square-monotone` — **Square Is Strictly Monotone on Nonneg Reals**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$,
   > \[
   >  0 \le a < b \;\Rightarrow\; a^2 < b^2.
   > \]

19. () `thm:ineq-square-root-monotone` — **Square Root Is Monotone on Nonneg Reals**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$,
   > \[
   >  0 \le a \le b \;\Rightarrow\; \sqrt{a} \le \sqrt{b}.
   > \]

20. () `thm:ineq-am-gm-two` — **AM-GM Inequality for Two Terms**
   > **Statement.**
   > For all $a, b \ge 0$,
   > \[
   >  \sqrt{ab} \le \frac{a + b}{2}.
   > \]

21. () `thm:ineq-bernoulli` — **Bernoulli's Inequality**
   > **Statement.**
   > For all $x \in \mathbb{R}$ with $x \ge -1$ and all $n \in \mathbb{N}$,
   > \[
   >  (1 + x)^n \ge 1 + nx.
   > \]

22. () `thm:absolute-value-nonneg` — **Absolute Value Is Nonnegative**
   > **Statement.**
   > For all $a \in \mathbb{R}$,
   > \[
   >  \lvert a \rvert \ge 0.
   > \]

23. () `thm:absolute-value-zero-iff-zero` — **Absolute Value Zero Iff Zero**
   > **Statement.**
   > For all $a \in \mathbb{R}$,
   > \[
   >  \lvert a \rvert = 0 \iff a = 0.
   > \]

24. () `thm:absolute-value-self-or-neg` — **Absolute Value Equals Self or Negation**
   > **Statement.**
   > For all $a \in \mathbb{R}$, either $\lvert a \rvert = a$ or
   > $\lvert a \rvert = -a$.

25. () `thm:absolute-value-symmetric` — **Absolute Value Is Symmetric**
   > **Statement.**
   > For all $a \in \mathbb{R}$,
   > \[
   >  \lvert -a \rvert = \lvert a \rvert.
   > \]

26. () `thm:absolute-value-product` — **Absolute Value of a Product**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$,
   > \[
   >  \lvert ab \rvert = \lvert a \rvert\,\lvert b \rvert.
   > \]

27. () `thm:absolute-value-quotient` — **Absolute Value of a Quotient**
   > **Statement.**
   > For all $a \in \mathbb{R}$ and $b \in \mathbb{R}$ with $b \ne 0$,
   > \[
   >  \left\lvert \frac{a}{b} \right\rvert
   >  = \frac{\lvert a \rvert}{\lvert b \rvert}.
   > \]

28. () `thm:absolute-value-bounds` — **Bound by Modulus**
   > **Statement.**
   > For all $a \in \mathbb{R}$,
   > \[
   >  -\lvert a \rvert \le a \le \lvert a \rvert.
   > \]

29. () `thm:absolute-value-le-iff` — **Nonstrict Modulus Inequality**
   > **Statement.**
   > For all $a \in \mathbb{R}$ and $r \ge 0$,
   > \[
   >  \lvert a \rvert \le r \iff -r \le a \le r.
   > \]

30. () `thm:absolute-value-lt-iff` — **Strict Modulus Inequality**
   > **Statement.**
   > For all $a \in \mathbb{R}$ and $r > 0$,
   > \[
   >  \lvert a \rvert < r \iff -r < a < r.
   > \]

31. () `thm:reverse-triangle-inequality` — **Reverse Triangle Inequality**
   > **Statement.**
   > For all $a, b \in \mathbb{R}$,
   > \[
   >  \lvert\, \lvert a \rvert - \lvert b \rvert \,\rvert
   >  \le \lvert a - b \rvert.
   > \]

32. () `thm:absolute-value-sum-bound` — **Generalised Triangle Inequality**
   > **Statement.**
   > For all $n \in \mathbb{N}$ and $a_1, \ldots, a_n \in \mathbb{R}$,
   > \[
   >  \left\lvert \sum_{k=1}^{n} a_k \right\rvert
   >  \le \sum_{k=1}^{n} \lvert a_k \rvert.
   > \]

33. () `prop:order-arithmetic` — **Order arithmetic**
   > **Statement.**
   > Let $a,b,c,d\in\mathbb{R}$.
   > - [label=(\roman*)]
   > - If $a\leq b$ and $c\leq d$, then $a+c\leq b+d$.
   > - If $a\leq b$ and $c>0$, then $ac\leq bc$.
   > - If $a\leq b$ and $c<0$, then $ac\geq bc$.
   > - $|x|\leq y$ (with $y\geq 0$) if and only if $-y\leq x\leq y$.

34. () `prop:convergent-bounded` — **Convergent sequences are bounded**
   > **Statement.**
   > If $(b_n)\to b$, then there exists $M>0$ such that $|b_n|\leq M$ for all
   > $n\in\mathbb{N}$.

35. () `prop:eps-char-sup` — **$\varepsilon$-characterisation of $\sup$**
   > **Statement.**
   > Let $S\subset\mathbb{R}$ be nonempty and bounded above, and let
   > $s=\sup S$. Then for every $\varepsilon>0$ there exists $x\in S$ with
   > $x>s-\varepsilon$.

36. () `prop:monotone-approx-bounds` — **Monotone Approximation of Bounds**
   > **Statement.**
   > Let $S\subset\mathbb{R}$ be nonempty and bounded. Then there exist
   > monotone sequences $(x_n),(y_n)\subset S$ with
   > $x_n\to\sup S$ and $y_n\to\inf S$.

37. () `prop:io-ev-dichotomy` — **The dichotomy**
   > **Statement.**
   > For any predicate $P$ on $\mathbb{N}$, exactly one of the following holds:
   > - [label=(\roman*)]
   > - $P$ holds infinitely often.
   > - $\neg P$ holds eventually.

38. () `prop:bw-bisection` — **Bolzano--Weierstrass via bisection**
   > **Statement.**
   > Every bounded sequence in $\mathbb{R}$ has a convergent subsequence.

39. () `prop:ivt-bisection` — **Intermediate Value Theorem**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous. If $L\in\mathbb{R}$ satisfies
   > $f(a)<L<f(b)$ or $f(a)>L>f(b)$, then there exists $c\in(a,b)$ with
   > $f(c)=L$.

40. () `prop:r-uncountable` — **R Uncountable**
   > **Statement.**
   > $\mathbb{R}$ is uncountable.

41. () `prop:residue-divergence` — **Residue divergence criterion**
   > **Statement.**
   > If there exist residues $r, s \in \{0,\ldots,k-1\}$ such that
   > $(a_{kn+r}) \to L$ and $(a_{kn+s}) \to M$ with $L \neq M$, then
   > $(a_n)$ diverges.

42. () `prop:abs-value-is-distance-to-zero` — **Absolute Value Is Distance to the Origin**
   > **Statement.**
   > For every $a\in\mathbb{R}$, $\;|a|=d(a,0)$.

43. () `thm:closed-iff-contains-limit-points` — **Closed Sets Contain Their Limit Points**
   > **Statement.**
   > A set $F\subseteq\mathbb{R}$ is closed if and only if it contains every one of its limit points.

44. () `thm:compact-implies-closed-bounded` — **Compact Subsets of $\mathbb{R}$ Are Closed and Bounded**
   > **Statement.**
   > If $K\subseteq\mathbb{R}$ is compact, then $K$ is closed and bounded.

45. () `thm:closed-bounded-interval-compact` — **Closed Bounded Intervals Are Compact**
   > **Statement.**
   > Every closed bounded interval $[a,b]\subseteq\mathbb{R}$ is compact.

46. () `thm:heine-borel` — **Heine--Borel Theorem for $\mathbb{R}$**
   > **Statement.**
   > A set $K\subseteq\mathbb{R}$ is compact if and only if $K$ is closed and bounded.

47. () `thm:open-interval-is-open` — **Open Intervals Are Open**
   > **Statement.**
   > Every open interval $(a,b)$, every open ray $(a,\infty)$ and $(-\infty,b)$, and $\mathbb{R}$ itself are open sets.

48. () `thm:open-set-closure-operations` — **Unions and Finite Intersections of Open Sets**
   > **Statement.**
   > An arbitrary union of open subsets of $\mathbb{R}$ is open, and a finite intersection of open subsets of $\mathbb{R}$ is open.

49. () `thm:distance-is-a-metric` — **The Distance Function Is a Metric**
   > **Statement.**
   > The map $d(x,y)=|x-y|$ satisfies, for all $x,y,z\in\mathbb{R}$: (i) $d(x,y)\ge 0$ with $d(x,y)=0$ iff $x=y$; (ii) $d(x,y)=d(y,x)$; and (iii) $d(x,z)\le d(x,y)+d(y,z)$. Hence $(\mathbb{R},d)$ is a metric space.

50. () `thm:closed-set-closure-operations` — **Closure Laws for Closed Sets**
   > **Statement.**
   > An arbitrary intersection of closed subsets of $\mathbb{R}$ is closed, and a finite union of closed subsets of $\mathbb{R}$ is closed.

51. () `thm:translation-invariance-supremum` — **Translation Invariance of the Supremum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $c\in\mathbb{R}$. Then
   > \[
   >  \sup(A+c)=\sup A+c,
   >  \qquad
   >  A+c=\{a+c:a\in A\}.
   > \]

52. () `thm:translation-invariance-infimum` — **Translation Invariance of the Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let
   > $c\in\mathbb{R}$. Then
   > \[
   >  \inf(A+c)=\inf A+c.
   > \]

53. (✅) `thm:scalar-mult-positive` — **Scalar Multiplication by a Positive Scalar**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $k>0$. Then
   > \[
   >  \sup(kA)=k\sup A,
   >  \qquad
   >  kA=\{ka:a\in A\}.
   > \]

54. () `thm:positive-scalar-mult-infimum` — **Positive Scalar Multiplication of the Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let $k>0$.
   > Then
   > \[
   >  \inf(kA)=k\inf A.
   > \]

55. (✅) `thm:scalar-mult-negative` — **Scalar Multiplication by a Negative Scalar**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let $k<0$. Then
   > \[
   >  \sup(kA)=k\inf A,
   >  \qquad
   >  kA=\{ka:a\in A\}.
   > \]

56. () `thm:negative-scalar-mult-infimum` — **Negative Scalar Multiplication of the Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $k<0$.
   > Then
   > \[
   >  \inf(kA)=k\sup A.
   > \]

57. (✅) `thm:negation-exchange-sup-inf` — **Negation Exchanges Supremum and Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below. Then $-A=\{-a:a\in A\}$ is bounded above and
   > \[
   >  \sup(-A)=-\inf A.
   > \]

58. () `thm:supremum-sum-set` — **Supremum of a Sum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. Then
   > \[
   >  \sup(A+B)=\sup A+\sup B,
   >  \qquad
   >  A+B=\{a+b:a\in A,\ b\in B\}.
   > \]

59. () `thm:infimum-sum-set` — **Infimum of a Sum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded below. Then
   > \[
   >  \inf(A+B)=\inf A+\inf B.
   > \]

60. () `thm:supremum-difference-set` — **Supremum of a Difference Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty, with $A$ bounded above and $B$ bounded below. Then
   > \[
   >  \sup(A-B)=\sup A-\inf B,
   >  \qquad
   >  A-B=\{a-b:a\in A,\ b\in B\}.
   > \]

61. () `thm:infimum-difference-set` — **Infimum of a Difference Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty, with $A$ bounded below and $B$
   > bounded above. Then
   > \[
   >  \inf(A-B)=\inf A-\sup B.
   > \]

62. () `thm:supremum-dilation` — **Supremum of a Dilation**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded, and let $\lambda\in\mathbb{R}$. Then
   > \[
   >  \sup(\lambda A)=\max\{\lambda\sup A,\lambda\inf A\},
   >  \qquad
   >  \lambda A=\{\lambda a:a\in A\}.
   > \]

63. (✅) `prop:every-element-lies-below-the-supremum` — **Every Element Lies Below the Supremum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let
   > $s=\sup A$. Then $x\leq s$ for every $x\in A$.

64. () `thm:supremum-absolute-value-image` — **Supremum of the Absolute-Value Image**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \sup |A|=\max\{|\sup A|,|\inf A|\},
   >  \qquad
   >  |A|=\{|a|:a\in A\}.
   > \]

65. () `thm:supremum-reciprocal-set` — **Supremum of a Reciprocal Set**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded, and suppose that
   > $0<\inf A$ or $\sup A<0$. Define
   > \[
   >  A^{-1}:=\{1/a:a\in A\}.
   > \]
   > Then
   > \[
   >  \sup(A^{-1})=\frac{1}{\inf A}.
   > \]

66. () `thm:infimum-reciprocal-set` — **Infimum of a Reciprocal Set**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded, and suppose that
   > $0<\inf A$ or $\sup A<0$. Define
   > \[
   >  A^{-1}:=\{1/a:a\in A\}.
   > \]
   > Then
   > \[
   >  \inf(A^{-1})=\frac{1}{\sup A}.
   > \]

67. () `thm:supremum-product-set` — **Supremum of a Product Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \sup(AB)=
   >  \max\{(\inf A)(\inf B),(\inf A)(\sup B),(\sup A)(\inf B),(\sup A)(\sup B)\}.
   > \]

68. () `thm:infimum-product-set` — **Infimum of a Product Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \inf(AB)=
   >  \min\{(\inf A)(\inf B),(\inf A)(\sup B),(\sup A)(\inf B),(\sup A)(\sup B)\}.
   > \]

69. () `thm:supremum-quotient-set` — **Supremum of a Quotient Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded, and suppose
   > $0<\inf B$ or $\sup B<0$. Then
   > \[
   >  \sup(A/B)=
   >  \max\left\{\frac{\inf A}{\inf B},\frac{\inf A}{\sup B},
   >  \frac{\sup A}{\inf B},\frac{\sup A}{\sup B}\right\}.
   > \]

70. () `thm:infimum-quotient-set` — **Infimum of a Quotient Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded, and suppose
   > $0<\inf B$ or $\sup B<0$. Then
   > \[
   >  \inf(A/B)=
   >  \min\left\{\frac{\inf A}{\inf B},\frac{\inf A}{\sup B},
   >  \frac{\sup A}{\inf B},\frac{\sup A}{\sup B}\right\}.
   > \]

71. () `prop:bounds-sum-set` — **Bounds for Suprema and Infima Under Set Addition**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \inf A+\inf B\le \inf(A+B)
   >  \qquad\text{and}\qquad
   >  \sup(A+B)\le \sup A+\sup B.
   > \]

72. () `prop:upper-bounds-ambient-order` — **Upper Bounds Depend on the Ambient Order**
   > **Statement.**
   > Let $(S,\le_S)$ and $(T,\le_T)$ be ordered sets, and let $A\subseteq S\cap T$. Whether $u$ is an upper bound of $A$ must be interpreted relative to the chosen ambient order.

73. () `prop:suprema-ambient-set` — **Suprema Depend on the Ambient Set**
   > **Statement.**
   > Let $A\subseteq S\subseteq S'$ be subsets of an ordered set. The supremum of $A$ relative to $S$, if it exists, need not agree with the supremum of $A$ relative to $S'$.

74. () `thm:ambient-existence-supremum` — **Ambient Existence of Supremum**
   > **Statement.**
   > There are ordered sets $S\subseteq S'$ and a subset $A\subseteq S$ such that $A$ has a supremum relative to $S'$ but has no supremum relative to $S$.

75. () `lem:rational-gap-suprema` — **Rational Gap Example for Suprema**
   > **Statement.**
   > Let
   > \[
   >  A=\{q\in\mathbb{Q}:q^2<2\}.
   > \]
   > Then $A$ is nonempty and bounded above in $\mathbb{Q}$, but $A$ has no supremum relative to $\mathbb{Q}$.

76. () `prop:translation-preserves-upper-bounds` — **Translation Preserves Upper Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty. If $u$ is an upper bound of $A$,
   > then $u+c$ is an upper bound of $A+c$.

77. () `prop:translation-preserves-lower-bounds` — **Translation Preserves Lower Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty. If $\ell$ is a lower bound of $A$,
   > then $\ell+c$ is a lower bound of $A+c$.

78. () `prop:positive-dilation-preserves-upper-bounds` — **Positive Dilation Preserves Upper Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and let $\lambda>0$. If $u$ is an
   > upper bound of $A$, then $\lambda u$ is an upper bound of $\lambda A$.

79. () `prop:positive-dilation-preserves-lower-bounds` — **Positive Dilation Preserves Lower Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and let $\lambda>0$. If $\ell$ is a
   > lower bound of $A$, then $\lambda\ell$ is a lower bound of $\lambda A$.

80. () `prop:negative-dilation-sends-lower-to-upper-bounds` — **Negative Dilation Sends Lower Bounds to Upper Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and let $\lambda<0$. If $\ell$ is a
   > lower bound of $A$, then $\lambda\ell$ is an upper bound of $\lambda A$.

81. () `prop:negative-dilation-sends-upper-to-lower-bounds` — **Negative Dilation Sends Upper Bounds to Lower Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and let $\lambda<0$. If $u$ is an
   > upper bound of $A$, then $\lambda u$ is a lower bound of $\lambda A$.

82. () `cor:reflection-swaps-upper-lower-bounds` — **Reflection Swaps Upper and Lower Bounds**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty. If $\ell$ is a lower bound of $A$,
   > then $-\ell$ is an upper bound of $-A$. If $u$ is an upper bound of $A$,
   > then $-u$ is a lower bound of $-A$.

83. () `thm:increasing-image-preserves-suprema` — **Increasing Image Preserves Suprema**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$, let $A\subseteq I$ be nonempty and bounded above,
   > and let $f:I\to\mathbb{R}$ be increasing. Suppose $s=\sup A$ belongs to $I$
   > and $f$ is continuous at $s$. Then
   > \[
   >  \sup f(A)=f(\sup A),
   >  \qquad
   >  f(A)=\{f(a):a\in A\}.
   > \]

84. () `thm:increasing-image-preserves-infima` — **Increasing Image Preserves Infima**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$, let $A\subseteq I$ be nonempty and bounded below,
   > and let $f:I\to\mathbb{R}$ be increasing. Suppose $t=\inf A$ belongs to $I$
   > and $f$ is continuous at $t$. Then
   > \[
   >  \inf f(A)=f(\inf A).
   > \]

85. () `thm:decreasing-image-infimum-to-supremum` — **Decreasing Image Sends Infimum to Supremum**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$, let $A\subseteq I$ be nonempty and bounded below,
   > and let $f:I\to\mathbb{R}$ be decreasing. Suppose $t=\inf A$ belongs to $I$
   > and $f$ is continuous at $t$. Then
   > \[
   >  \sup f(A)=f(\inf A).
   > \]

86. () `thm:decreasing-image-supremum-to-infimum` — **Decreasing Image Sends Supremum to Infimum**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$, let $A\subseteq I$ be nonempty and bounded above,
   > and let $f:I\to\mathbb{R}$ be decreasing. Suppose $s=\sup A$ belongs to $I$
   > and $f$ is continuous at $s$. Then
   > \[
   >  \inf f(A)=f(\sup A).
   > \]

87. () `thm:increasing-inverse-preserves-suprema` — **Increasing Inverse Preserves Suprema**
   > **Statement.**
   > Let $I,J\subseteq\mathbb{R}$, and let $f:I\to J$ be bijective. Suppose
   > $f^{-1}:J\to I$ is increasing and continuous. If $B\subseteq J$ is nonempty
   > and bounded above, and if $\sup B\in J$, then
   > \[
   >  \sup f^{-1}(B)=f^{-1}(\sup B).
   > \]

88. () `thm:increasing-inverse-preserves-infima` — **Increasing Inverse Preserves Infima**
   > **Statement.**
   > Let $I,J\subseteq\mathbb{R}$, and let $f:I\to J$ be bijective. Suppose
   > $f^{-1}:J\to I$ is increasing and continuous. If $B\subseteq J$ is nonempty
   > and bounded below, and if $\inf B\in J$, then
   > \[
   >  \inf f^{-1}(B)=f^{-1}(\inf B).
   > \]

89. () `thm:decreasing-inverse-infimum-to-supremum` — **Decreasing Inverse Sends Infimum to Supremum**
   > **Statement.**
   > Let $I,J\subseteq\mathbb{R}$, and let $f:I\to J$ be bijective. Suppose
   > $f^{-1}:J\to I$ is decreasing and continuous. If $B\subseteq J$ is nonempty
   > and bounded below, and if $\inf B\in J$, then
   > \[
   >  \sup f^{-1}(B)=f^{-1}(\inf B).
   > \]

90. () `thm:decreasing-inverse-supremum-to-infimum` — **Decreasing Inverse Sends Supremum to Infimum**
   > **Statement.**
   > Let $I,J\subseteq\mathbb{R}$, and let $f:I\to J$ be bijective. Suppose
   > $f^{-1}:J\to I$ is decreasing and continuous. If $B\subseteq J$ is nonempty
   > and bounded above, and if $\sup B\in J$, then
   > \[
   >  \inf f^{-1}(B)=f^{-1}(\sup B).
   > \]

91. () `thm:supremum-pointwise-maximum-set` — **Supremum of the Pointwise Maximum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. Then
   > \[
   >  \sup\max(A,B)=\max\{\sup A,\sup B\}.
   > \]

92. () `thm:infimum-pointwise-maximum-set` — **Infimum of the Pointwise Maximum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded below. Then
   > \[
   >  \inf\max(A,B)=\max\{\inf A,\inf B\}.
   > \]

93. () `thm:supremum-pointwise-minimum-set` — **Supremum of the Pointwise Minimum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. Then
   > \[
   >  \sup\min(A,B)=\min\{\sup A,\sup B\}.
   > \]

94. () `thm:infimum-pointwise-minimum-set` — **Infimum of the Pointwise Minimum Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded below. Then
   > \[
   >  \inf\min(A,B)=\min\{\inf A,\inf B\}.
   > \]

95. () `lem:union-preserves-upper-bounds` — **Union Preserves Upper Bounds**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$. If $u_A$ is an upper bound of $A$ and
   > $u_B$ is an upper bound of $B$, then $\max\{u_A,u_B\}$ is an upper bound
   > of $A\cup B$.

96. () `lem:union-preserves-lower-bounds` — **Union Preserves Lower Bounds**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$. If $\ell_A$ is a lower bound of $A$ and
   > $\ell_B$ is a lower bound of $B$, then $\min\{\ell_A,\ell_B\}$ is a lower
   > bound of $A\cup B$.

97. () `lem:subsets-preserve-upper-bounds` — **Subsets Preserve Upper Bounds**
   > **Statement.**
   > Let $C\subseteq A\subseteq\mathbb{R}$. If $u$ is an upper bound of $A$,
   > then $u$ is an upper bound of $C$.

98. () `prop:union-bounded-above-iff-pieces-bounded-above` — **Union Is Bounded Above Exactly When Both Pieces Are**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty. Then $A\cup B$ is bounded above
   > if and only if $A$ is bounded above and $B$ is bounded above.

99. () `lem:subsets-preserve-lower-bounds` — **Subsets Preserve Lower Bounds**
   > **Statement.**
   > Let $C\subseteq A\subseteq\mathbb{R}$. If $\ell$ is a lower bound of $A$,
   > then $\ell$ is a lower bound of $C$.

100. () `prop:union-bounded-below-iff-pieces-bounded-below` — **Union Is Bounded Below Exactly When Both Pieces Are**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty. Then $A\cup B$ is bounded below
   > if and only if $A$ is bounded below and $B$ is bounded below.

101. () `cor:union-bounded-iff-pieces-bounded` — **Union Is Bounded Exactly When Both Pieces Are**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty. Then $A\cup B$ is bounded if and
   > only if $A$ is bounded and $B$ is bounded.

102. () `cor:intersections-inherit-bounds` — **Intersections Inherit Bounds**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$. Every upper bound of $A$ is an upper bound
   > of $A\cap B$, and every lower bound of $A$ is a lower bound of $A\cap B$.

103. () `cor:differences-inherit-bounds` — **Differences Inherit Bounds**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$. Every upper bound of $A$ is an upper bound
   > of $A\setminus B$, and every lower bound of $A$ is a lower bound of
   > $A\setminus B$.

104. () `cor:complements-inherit-ambient-bounds` — **Complements Inherit Ambient Bounds**
   > **Statement.**
   > Let $A\subseteq E\subseteq\mathbb{R}$, and take complements relative to
   > $E$. Every upper bound of $E$ is an upper bound of $E\setminus A$, and
   > every lower bound of $E$ is a lower bound of $E\setminus A$.

105. () `prop:uniqueness-of-the-maximum` — **Uniqueness of the Maximum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $m,n\in S$ are both maxima of $A$, then $m=n$.

106. () `prop:uniqueness-of-the-minimum` — **Uniqueness of the Minimum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $m,n\in S$ are both minima of $A$, then $m=n$.

107. (✅) `prop:maximum-implies-supremum` — **Maximum Implies Supremum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $m=\max A$, then $m=\sup A$.

108. () `prop:minimum-implies-infimum` — **Minimum Implies Infimum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $m=\min A$, then $m=\inf A$.

109. () `prop:supremum-in-the-set-is-the-maximum` — **Supremum in the Set is the Maximum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $s=\sup A$ and $s\in A$, then $s=\max A$.

110. () `prop:infimum-in-the-set-is-the-minimum` — **Infimum in the Set is the Minimum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $i=\inf A$ and $i\in A$, then $i=\min A$.

111. () `prop:uniqueness-of-the-supremum` — **Uniqueness of the Supremum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $s,t\in S$ are both suprema of $A$, then $s=t$.

112. () `prop:uniqueness-of-the-infimum` — **Uniqueness of the Infimum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set and let $A\subseteq S$ be nonempty. If
   > $i,j\in S$ are both infima of $A$, then $i=j$.

113. () `prop:upper-bound-property-of-supremum` — **Upper Bound Property of the Supremum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set, let $A\subseteq S$ be nonempty, and
   > suppose that $s=\sup A$ exists in $S$. Then every element of $A$ lies
   > below $s$:
   > \[
   >  (\forall x\in A)(x\leq s).
   > \]

114. () `prop:lower-bound-property-of-infimum` — **Lower Bound Property of the Infimum**
   > **Statement.**
   > Let $(S,\leq)$ be an ordered set, let $A\subseteq S$ be nonempty, and
   > suppose that $i=\inf A$ exists in $S$. Then every element of $A$ lies
   > above $i$:
   > \[
   >  (\forall x\in A)(i\leq x).
   > \]

115. () `lem:subset-inclusion-preserves-upper-bounds` — **Subset Inclusion Preserves Upper Bounds**
   > **Statement.**
   > Let $A\subseteq B\subseteq S$ be nonempty subsets of an ordered set
   > $(S,\leq)$. If $u$ is an upper bound of $B$, then $u$ is an upper bound
   > of $A$.

116. () `lem:subset-inclusion-preserves-lower-bounds` — **Subset Inclusion Preserves Lower Bounds**
   > **Statement.**
   > Let $A\subseteq B\subseteq S$ be nonempty subsets of an ordered set
   > $(S,\leq)$. If $\ell$ is a lower bound of $B$, then $\ell$ is a lower
   > bound of $A$.

117. () `thm:supremum-is-monotone-under-inclusion` — **Supremum Is Monotone Under Inclusion**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. If
   > $A\subseteq B$, then $\sup A\leq\sup B$.

118. () `thm:infimum-is-monotone-under-inclusion` — **Infimum Is Monotone Under Inclusion**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded below. If
   > $A\subseteq B$, then $\inf B\leq\inf A$.

119. () `prop:upper-bound-comparison-with-the-supremum` — **Upper Bound Comparison with the Supremum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let
   > $s=\sup A$. For $u\in\mathbb{R}$, the number $u$ is an upper bound of
   > $A$ if and only if $s\leq u$.

120. () `prop:lower-bound-comparison-with-the-infimum` — **Lower Bound Comparison with the Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let
   > $i=\inf A$. For $\ell\in\mathbb{R}$, the number $\ell$ is a lower bound
   > of $A$ if and only if $\ell\leq i$.

121. () `prop:every-element-lies-above-the-infimum` — **Every Element Lies Above the Infimum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let
   > $i=\inf A$. Then $i\leq x$ for every $x\in A$.

122. (✅) `thm:infimum-less-than-supremum` — **Infimum Is Less Than or Equal to the Supremum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty, bounded below, and bounded above.
   > Then $\inf A\leq\sup A$.

123. () `prop:order-comparison-of-suprema` — **Order Comparison of Suprema**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. If every
   > $x\in A$ is below some $y\in B$, then $\sup A\leq\sup B$.

124. () `thm:lub-property-implies-existence-of-suprema` — **Least Upper Bound Property Implies Existence of Suprema**
   > **Statement.**
   > Let $S\subseteq\mathbb{R}$ be nonempty and bounded above. By the least
   > upper bound property of the real numbers, there exists a real number
   > $s$ such that $s=\sup S$.

125. () `thm:glb-property-implies-existence-of-infima` — **Greatest Lower Bound Property Implies Existence of Infima**
   > **Statement.**
   > Let $S\subseteq\mathbb{R}$ be nonempty and bounded below. Then there
   > exists a real number $i$ such that $i=\inf S$.

126. () `thm:archimedean-property` — **Archimedean Property**
   > **Statement.**
   > For every real number $x$, there exists a natural number $n$ such that $n>x$.

127. () `cor:archimedean-reciprocal-form` — **Archimedean Reciprocal Form**
   > **Statement.**
   > For every real number $\varepsilon>0$, there exists a natural number
   > $n\in\mathbb{N}$ such that
   > \[
   > 0<\frac{1}{n}<\varepsilon.
   > \]

128. () `cor:archimedean-reciprocal` — **Archimedean Scaling Form**
   > **Statement.**
   > For every $x>0$ and every $y\in\mathbb{R}$, there exists $n\in\mathbb{N}$ such that $nx>y$.

129. () `lem:integer-part-lemma` — **Integer Part Lemma**
   > **Statement.**
   > For every real number $x\in\mathbb{R}$, there exists an integer
   > $m\in\mathbb{Z}$ such that
   > \[
   > m\le x<m+1.
   > \]

130. () `lem:archimedean-integer-part-lemma` — **Archimedean Integer Part Lemma**
   > **Statement.**
   > For every $x\in\mathbb{R}$, there exists $m\in\mathbb{Z}$ such that
   > \[
   > m-1\le x<m.
   > \]

131. () `lem:integer-ceiling-lemma` — **Integer Ceiling Lemma**
   > **Statement.**
   > For every $x\in\mathbb{R}$, there exists $m\in\mathbb{Z}$ such that
   > \[
   > x<m\le x+1.
   > \]

132. () `lem:integer-above-lemma` — **Integer Above Lemma**
   > **Statement.**
   > For every $x\in\mathbb{R}$, there exists an integer $m\in\mathbb{Z}$ such
   > that
   > \[
   > x<m.
   > \]

133. () `lem:unit-length-interval-contains-integer` — **Unit-Length Interval Contains an Integer**
   > **Statement.**
   > If $\alpha,\beta\in\mathbb{R}$ and $\beta-\alpha>1$, then there exists
   > $m\in\mathbb{Z}$ such that
   > \[
   > \alpha<m<\beta.
   > \]

134. () `thm:density-of-rationals-in-reals` — **Density of the Rationals**
   > **Statement.**
   > For every $a,b\in\mathbb{R}$ with $a<b$, there exists $q\in\mathbb{Q}$ such that $a<q<b$.

135. () `lem:rational-translation-preserves-rationality` — **Rational Translation Preserves Rationality**
   > **Statement.**
   > If $r,q\in\mathbb{Q}$, then
   > \[
   > r+q\in\mathbb{Q}.
   > \]

136. () `lem:rational-difference-preserves-rationality` — **Rational Difference Preserves Rationality**
   > **Statement.**
   > If $r,q\in\mathbb{Q}$, then
   > \[
   > r-q\in\mathbb{Q}.
   > \]

137. () `lem:nonzero-rational-product-preserves-irrationality` — **Nonzero Rational Product Preserves Irrationality**
   > **Statement.**
   > If $q\in\mathbb{Q}\setminus\{0\}$ and
   > $x\in\mathbb{R}\setminus\mathbb{Q}$, then
   > \[
   > qx\in\mathbb{R}\setminus\mathbb{Q}.
   > \]

138. () `lem:rational-translation-preserves-irrationality` — **Rational Translation Preserves Irrationality**
   > **Statement.**
   > If $q\in\mathbb{Q}$ and $x\in\mathbb{R}\setminus\mathbb{Q}$, then
   > \[
   > q+x\in\mathbb{R}\setminus\mathbb{Q}.
   > \]

139. () `lem:irrational-minus-irrational-need-not-be-irrational` — **Irrational Minus Irrational Need Not Be Irrational**
   > **Statement.**
   > There exist irrational numbers $x,y\in\mathbb{R}\setminus\mathbb{Q}$ such
   > that
   > \[
   > x-y\in\mathbb{Q}.
   > \]

140. () `lem:rational-minus-irrational-is-irrational` — **Rational Minus Irrational Is Irrational**
   > **Statement.**
   > If $q\in\mathbb{Q}$ and $x\in\mathbb{R}\setminus\mathbb{Q}$, then
   > \[
   > q-x\in\mathbb{R}\setminus\mathbb{Q}.
   > \]

141. () `lem:irrational-plus-rational-is-irrational` — **Irrational Plus Rational Is Irrational**
   > **Statement.**
   > If $x\in\mathbb{R}\setminus\mathbb{Q}$ and $q\in\mathbb{Q}$, then
   > \[
   > x+q\in\mathbb{R}\setminus\mathbb{Q}.
   > \]

142. () `lem:irrational-minus-rational-is-irrational` — **Irrational Minus Rational Is Irrational**
   > **Statement.**
   > If $x\in\mathbb{R}\setminus\mathbb{Q}$ and $q\in\mathbb{Q}$, then
   > \[
   > x-q\in\mathbb{R}\setminus\mathbb{Q}.
   > \]

143. () `thm:density-of-irrationals-in-reals` — **Density of the Irrationals**
   > **Statement.**
   > For every $a,b\in\mathbb{R}$ with $a<b$, there exists $s\in\mathbb{R}\setminus\mathbb{Q}$ such that $a<s<b$.

144. () `thm:irrational-between-any-two-rationals` — **An Irrational Between Any Two Rationals**
   > **Statement.**
   > If $r,s\in\mathbb{Q}$ and $r<s$, then there exists
   > $x\in\mathbb{R}\setminus\mathbb{Q}$ such that
   > \[
   > r<x<s.
   > \]

145. () `thm:rational-between-any-two-irrationals` — **A Rational Between Any Two Irrationals**
   > **Statement.**
   > If $x,y\in\mathbb{R}\setminus\mathbb{Q}$ and $x<y$, then there exists
   > $q\in\mathbb{Q}$ such that
   > \[
   > x<q<y.
   > \]

146. () `lem:small-irrational-positive-number` — **Small Irrational Positive Number**
   > **Statement.**
   > For every $\varepsilon>0$, there exists
   > $\eta\in\mathbb{R}\setminus\mathbb{Q}$ such that
   > \[
   > 0<\eta<\varepsilon.
   > \]

147. () `cor:every-open-interval-contains-rational-and-irrational` — **Rational and Irrational Points in Every Open Interval**
   > **Statement.**
   > Every open interval in $\mathbb{R}$ contains both a rational number and an irrational number.

148. () `thm:nested-interval-theorem` — **Nested Interval Property**
   > **Statement.**
   > Let $(I_n)$ be a sequence of nonempty closed intervals in $\mathbb{R}$. If $I_{n+1}\subseteq I_n$ for every $n\in\mathbb{N}$, then
   > \[
   >  \bigcap_{n=1}^{\infty} I_n\neq\varnothing.
   > \]

149. () `prop:composition-injective` — **Composition of Injections Is Injective**
   > **Statement.**
   > Let $f:A\to B$ and let $g:B\to C$. If $f$ is injective and $g$ is
   > injective, then $g\circ f:A\to C$ is injective.

150. () `prop:composition-surjective` — **Composition of Surjections Is Surjective**
   > **Statement.**
   > $\operatorname{Surjective}(f)\wedge\operatorname{Surjective}(g)
   > \Rightarrow\operatorname{Surjective}(g\circ f)$.

151. () `cor:composition-bijective` — **Composition of Bijections Is Bijective**
   > **Statement.**
   > Let $f:A\to B$ and let $g:B\to C$. If $f$ is bijective and $g$ is
   > bijective, then $g\circ f:A\to C$ is bijective.

152. () `prop:inverse-bijection` — **Inverse of a Bijection Is a Bijection**
   > **Statement.**
   > $\operatorname{Bijective}(f)\Rightarrow\operatorname{Bijective}(f^{-1})$.

153. () `prop:preimage-union-intersection` — **Preimage Distributes over Union and Intersection**
   > **Statement.**
   > Let $f:A\to B$, $S,T\subseteq B$. Then:
   > - [label=(\roman*)]
   > - $f^{-1}(S\cup T)=f^{-1}(S)\cup f^{-1}(T)$.
   > - $f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T)$.
   > - $f^{-1}(S^c)=(f^{-1}(S))^c$.

154. () `thm:cluster-point-sequential` — **Sequential Characterization of Cluster Points**
   > **Statement.**
   > $c\text{ is a cluster point of }A$ if and only if there exists
   > $(a_n) \subseteq A \setminus \{c\}$ with $a_n \to c$.

155. () `lem:closure-elementary` — **Elementary Properties of Closures**
   > **Statement.**
   > Let $X, Y \subseteq \mathbb{R}$. Then: (i) $X \subseteq \overline{X}$;
   > (ii) $\overline{X \cup Y} = \overline{X} \cup \overline{Y}$;
   > (iii) $\overline{X \cap Y} \subseteq \overline{X} \cap \overline{Y}$;
   > (iv) $X \subseteq Y \Rightarrow \overline{X} \subseteq \overline{Y}$.

156. () `cor:closed-iff-seq-limits` — **Closed iff Sequentially Closed**
   > **Statement.**
   > $X\text{ is closed} \iff \forall (a_n)\subseteq X,\;
   > a_n \to x \Rightarrow x \in X$.

157. () `cor:interval-all-limit-points` — **Every Point of an Interval Is a Cluster Point**
   > **Statement.**
   > If $I$ is an interval, then every $x\in I$ is a cluster point of $I$.

158. () `thm:heine-borel-subsets-real-line` — **Heine--Borel Theorem for $\mathbb{R}$**
   > **Statement.**
   > $X\text{ is closed} \wedge X\text{ is bounded}$
   > $\iff$ every $(a_n)\subseteq X$ has a subsequence converging to
   > a limit in $X$.

159. () `prop:delta-linearity` — **Linearity of \(\Delta\)**
   > **Statement.**
   > For functions \(f,g : \mathbb{Z} \to \mathbb{R}\) and constants \(a,b \in \mathbb{R}\),
   > \[
   > \Delta (a f + b g)
   > =
   > a\,\Delta f + b\,\Delta g.
   > \]

160. () `prop:delta-constant` — **Constant rule**
   > **Statement.**
   > If \(c\) is a constant function, then \(\Delta c = 0\).

161. () `thm:delta-shift-minus-identity` — **\(\Delta = E - I\)**
   > **Statement.**
   > \[
   > \Delta = E - I.
   > \]

162. () `thm:polynomial-detection` — **Polynomial detection**
   > **Statement.**
   > Let \(f(n)\) be a sequence generated by a polynomial of degree \(d\). Then
   > \(\Delta^d f(n)\) is constant, and \(\Delta^{d+1} f(n) = 0\).

163. () `prop:constant-of-integration` — **Constant of integration**
   > **Statement.**
   > If \(F\) is a discrete antiderivative of \(f\), then so is \(F + C\)
   > for any constant \(C \in \mathbb{R}\).

164. () `thm:binomial-theorem` — **Binomial Theorem**
   > **Statement.**
   > For any integer \(n \ge 0\) and real numbers \(x,y\),
   > \[
   > (x+y)^n
   > =
   > \sum_{k=0}^{n} \binom{n}{k} x^{\,n-k} y^{\,k},
   > \]
   > where the \emph{binomial coefficients} are
   > \[
   > \binom{n}{k}
   > =
   > \frac{n!}{k!(n-k)!}.
   > \]

165. () `prop:higher-diff-formula` — **Higher difference formula**
   > **Statement.**
   > For any function \(f\),
   > \[
   > \Delta^n f(x)
   > =
   > \sum_{k=0}^{n} (-1)^{\,n-k}
   > \binom{n}{k}
   > f(x+k).
   > \]

166. () `prop:discrete-exponential-rule` — **Discrete exponential rule**
   > **Statement.**
   > \[
   > \Delta\,(1+a)^n = a\,(1+a)^n.
   > \]

167. () `prop:higher-diff-two-n` — **Higher differences of \(2^n\)**
   > **Statement.**
   > For all \(k \ge 0\),
   > \[
   > \Delta^k\, 2^n = 2^n.
   > \]

168. () `prop:discrete-ivp` — **Discrete IVP**
   > **Statement.**
   > The unique function \(F : \mathbb{N} \to \mathbb{R}\) satisfying
   > \[
   > F(n+1) = 2\,F(n), \qquad F(0) = 1
   > \]
   > is \(F(n) = 2^n\).

169. () `thm:nonzero-limit-eventually-nonzero` — **Nonzero Limit is Eventually Nonzero**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$ with $L\neq 0$.
   > If $x_n\to L$, then there exists $N\in\mathbb{N}$ such that $x_n\neq 0$
   > for every $n\ge N$.

170. () `thm:limit-of-a-product` — **Limit of a Product**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_ny_n\to LM$.

171. () `thm:limit-of-a-reciprocal` — **Limit of a Reciprocal**
   > **Statement.**
   > Let $(x_n)$ be a real sequence such that $x_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$ with $L\neq 0$. If $x_n\to L$,
   > then $1/x_n\to 1/L$.

172. () `thm:limit-of-a-quotient` — **Limit of a Quotient**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences such that $y_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L,M\in\mathbb{R}$ with $M\neq 0$. If
   > $x_n\to L$ and $y_n\to M$, then $x_n/y_n\to L/M$.

173. () `thm:limit-of-scalar-multiple` — **Limit of a Scalar Multiple**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $\alpha\in\mathbb{R}$. If $x_n\to L$, then $\alpha x_n\to \alpha L$.

174. () `thm:limit-of-a-sum` — **Limit of a Sum**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n+y_n\to L+M$.

175. () `thm:limit-of-a-square` — **Limit of a Square**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $x_n^2\to L^2$.

176. () `thm:polynomial-sequence-limit` — **Polynomial Sequence Limit**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p\in\mathbb{R}[t]$ be a polynomial. If $x_n\to L$, then
   > $p(x_n)\to p(L)$.

177. () `thm:rational-sequence-limit` — **Rational Sequence Limit**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p,q\in\mathbb{R}[t]$ be polynomials. Suppose $q(L)\neq 0$ and
   > $q(x_n)\neq 0$ for every $n\in\mathbb{N}$. If $x_n\to L$, then
   > \[
   > \frac{p(x_n)}{q(x_n)}\to \frac{p(L)}{q(L)}.
   > \]

178. () `thm:monotone-convergence-theorem` — **Monotone Convergence Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing and bounded above, then $(x_n)$ converges and
   >  \[
   >  \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   >  \]
   > - If $(x_n)$ is decreasing and bounded below, then $(x_n)$ converges and
   >  \[
   >  \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   >  \]

179. () `thm:newton-approximation-sqrt-two` — **Newton Approximation of $\sqrt{2}$**
   > **Statement.**
   > Let $(x_n)$ be the Newton sequence for $\sqrt{2}$. Then $(x_n)$ converges
   > and
   > \[
   >  \lim_{n\to\infty}x_n=\sqrt{2}.
   > \]

180. () `thm:convergent-sequences-are-cauchy` — **Convergent Sequences Are Cauchy**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ converges, then $(x_n)$ is
   > Cauchy.

181. () `thm:cauchy-sequences-are-bounded` — **Cauchy Sequences Are Bounded**
   > **Statement.**
   > Every Cauchy real sequence is bounded.

182. () `thm:cauchy-sequence-with-convergent-subsequence` — **Cauchy Sequence with a Convergent Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. If a subsequence of $(x_n)$
   > converges to $L\in\mathbb{R}$, then $(x_n)$ converges to $L$.

183. () `thm:bounded-monotone-sequence-equivalences` — **Bounded Monotone Sequence Equivalences**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded above.
   > - If $(x_n)$ is decreasing, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded below.
   > - If $(x_n)$ is monotone, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded.

184. () `thm:boundedness-passes-to-subsequences` — **Boundedness Passes to Subsequences**
   > **Statement.**
   > Every subsequence of a bounded real sequence is bounded.

185. () `thm:monotone-subsequence-theorem` — **Monotone Subsequence Theorem**
   > **Statement.**
   > Every real sequence has a monotone subsequence.

186. () `thm:bolzano-weierstrass-sequences` — **Bolzano-Weierstrass Theorem for Sequences**
   > **Statement.**
   > Every bounded real sequence has a convergent subsequence.

187. () `thm:cauchy-criterion-real-sequences` — **Cauchy Criterion for Real Sequences**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ converges if and only if
   > $(x_n)$ is Cauchy.

188. () `thm:factorial-partial-sums-approximate-e` — **Factorial Partial Sums Approximate $e$**
   > **Statement.**
   > Let $(s_n)$ be the factorial partial-sum sequence. Then $(s_n)$ converges
   > to the Euler number $e$:
   > \[
   >  \lim_{n\to\infty}s_n=e.
   > \]

189. () `thm:uniqueness-of-limits` — **Uniqueness of Limits**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$. If $x_n \to L$ and $x_n \to K$, then
   > $L = K$.

190. () `thm:limit-preserves-eventual-order` — **Limit Preserves Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > Suppose that $x_n\to L$ and $y_n\to M$. If there exists
   > $N_0\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N_0$, then
   > $L\le M$.

191. () `thm:sequence-squeeze-theorem` — **Sequence Squeeze Theorem**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences, and let
   > $L\in\mathbb{R}$. Suppose that $a_n\to L$ and $b_n\to L$. If there
   > exists $N_0\in\mathbb{N}$ such that $a_n\le x_n\le b_n$ for every
   > $n\ge N_0$, then $x_n\to L$.

192. () `thm:compound-interest-approximation-e` — **Compound-Interest Approximation of $e$**
   > **Statement.**
   > Let $(c_n)$ be the compound-interest sequence. Then
   > \[
   >  \lim_{n\to\infty}c_n=e.
   > \]

193. () `thm:decimal-truncations-converge` — **Decimal Truncations Converge**
   > **Statement.**
   > Let $\alpha\in\mathbb{R}$, and let $(d_n)$ be the decimal truncation
   > sequence of $\alpha$. Then
   > \[
   >  \lim_{n\to\infty}d_n=\alpha.
   > \]

194. () `thm:cauchy-criterion-via-tails` — **Cauchy Criterion via Tails**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that the
   > $N$-tail has pairwise term distances less than $\varepsilon$.

195. () `thm:cauchy-tail-diameter-criterion` — **Cauchy Tail Diameter Criterion**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > every sufficiently late tail has arbitrarily small pairwise diameter.

196. () `thm:cauchy-successive-differences-vanish` — **Cauchy Sequences Have Vanishing Successive Differences**
   > **Statement.**
   > If $(x_n)$ is a Cauchy real sequence, then
   > \[
   >  |x_{n+1}-x_n|\to 0.
   > \]

197. () `thm:scalar-multiple-cauchy-sequence` — **Scalar Multiples of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence, and let $\alpha\in\mathbb{R}$.
   > Then $(\alpha x_n)$ is Cauchy.

198. () `thm:sum-cauchy-sequences` — **Sums of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n+y_n)$ is
   > Cauchy.

199. () `thm:difference-cauchy-sequences` — **Differences of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n-y_n)$ is
   > Cauchy.

200. () `thm:linear-combination-cauchy-sequences` — **Linear Combinations of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences, and let
   > $\alpha,\beta\in\mathbb{R}$. Then $(\alpha x_n+\beta y_n)$ is Cauchy.

201. () `thm:product-cauchy-sequences` — **Products of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_ny_n)$ is
   > Cauchy.

202. () `thm:reciprocal-cauchy-sequence` — **Reciprocals of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. If there exist $c>0$ and
   > $N_0\in\mathbb{N}$ such that $|x_n|\ge c$ for every $n\ge N_0$, then
   > $(1/x_n)$ is Cauchy.

203. () `thm:quotient-cauchy-sequences` — **Quotients of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. If there exist $c>0$
   > and $N_0\in\mathbb{N}$ such that $|y_n|\ge c$ for every $n\ge N_0$,
   > then $(x_n/y_n)$ is Cauchy.

204. () `thm:absolute-value-cauchy-sequence` — **Absolute Values of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. Then $(|x_n|)$ is Cauchy.

205. () `thm:frequent-properties-yield-subsequences` — **Frequent Properties Yield Subsequences**
   > **Statement.**
   > Let $P(n)$ be a property of indices. If for every $N\in\mathbb{N}$ there
   > exists $n\ge N$ such that $P(n)$ holds, then there exists a strictly
   > increasing index map $\sigma:\mathbb{N}\to\mathbb{N}$ such that
   > $P(\sigma(k))$ holds for every $k\in\mathbb{N}$.

206. () `thm:cluster-values-are-subsequential-limits` — **Cluster Values Are Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. Then $L$ is a
   > cluster value of $(x_n)$ if and only if $L$ is a subsequential limit of
   > $(x_n)$.

207. () `thm:bounded-sequences-have-cluster-values` — **Bounded Sequences Have Cluster Values**
   > **Statement.**
   > Every bounded real sequence has at least one cluster value.

208. () `thm:limsup-largest-subsequential-limit` — **Limsup Is the Largest Subsequential Limit**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let
   > $S=\limsup_{n\to\infty}x_n$. Then $S$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is less than or equal
   > to $S$.

209. () `thm:liminf-smallest-subsequential-limit` — **Liminf Is the Smallest Subsequential Limit**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let
   > $I=\liminf_{n\to\infty}x_n$. Then $I$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is greater than or
   > equal to $I$.

210. () `thm:limsup-liminf-extremal-cluster-values` — **Limsup and Liminf Are Extremal Cluster Values**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > $\limsup_{n\to\infty}x_n$ is the largest cluster value of $(x_n)$, and
   > $\liminf_{n\to\infty}x_n$ is the smallest cluster value of $(x_n)$.

211. () `thm:limit-of-a-negation` — **Limit of a Negation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $-x_n\to -L$.

212. () `thm:limit-of-a-difference` — **Limit of a Difference**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n-y_n\to L-M$.

213. () `thm:limit-of-an-absolute-value` — **Limit of an Absolute Value**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $|x_n|\to |L|$.

214. () `thm:positive-limit-eventually-positive` — **Positive Limit is Eventually Positive**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L>0$. If $x_n\to L$, then there
   > exists $N\in\mathbb{N}$ such that $0<x_n$ for every $n\ge N$.

215. () `thm:limit-of-a-square-root` — **Limit of a Square Root**
   > **Statement.**
   > Let $(x_n)$ be a real sequence such that $0\le x_n$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$. If $x_n\to L$, then
   > $0\le L$ and $\sqrt{x_n}\to\sqrt{L}$.

216. () `thm:equivalence-of-convergence-formulations` — **Equivalence of Convergence Formulations**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. The following
   > statements are equivalent.
   > - [label=\textup{(\alph*)}]
   > - $x_n \to L$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(|x_n - L| < \varepsilon\bigr)$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(L - \varepsilon < x_n < L + \varepsilon\bigr)$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(x_n \in V_\varepsilon(L)\bigr)$.

217. () `thm:strict-limit-separation-gives-eventual-order` — **Strict Limit Separation Gives Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$. If $A<B$, then there exists
   > $N\in\mathbb{N}$ such that $x_n<y_n$ for every $n\ge N$.

218. () `thm:eventual-strict-comparison-preserves-weak-limit-order` — **Eventual Strict Comparison Preserves Weak Limit Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$.
   > - [label=(\alph*)]
   > - If there exists $N\in\mathbb{N}$ such that $x_n<y_n$ for every
   >  $n\ge N$, then $A\le B$.
   > - If there exists $N\in\mathbb{N}$ such that $x_n>y_n$ for every
   >  $n\ge N$, then $A\ge B$.

219. () `thm:constant-comparison-for-sequence-limits` — **Constant Comparison for Sequence Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $A,B\in\mathbb{R}$. Suppose
   > that $x_n\to A$.
   > - [label=(\alph*)]
   > - If there exists $N\in\mathbb{N}$ such that $x_n\le B$ for every
   >  $n\ge N$, then $A\le B$.
   > - If there exists $N\in\mathbb{N}$ such that $x_n<B$ for every
   >  $n\ge N$, then $A\le B$.
   > - If there exists $N\in\mathbb{N}$ such that $x_n\ge B$ for every
   >  $n\ge N$, then $A\ge B$.
   > - If there exists $N\in\mathbb{N}$ such that $x_n>B$ for every
   >  $n\ge N$, then $A\ge B$.

220. () `thm:constant-squeeze-theorem` — **Constant Squeeze Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If there
   > exists $N_0\in\mathbb{N}$ such that $L\le x_n\le L$ for every
   > $n\ge N_0$, then $x_n\to L$.

221. () `thm:absolute-value-squeeze-theorem` — **Absolute-Value Squeeze Theorem**
   > **Statement.**
   > Let $(x_n)$ and $(u_n)$ be real sequences, and let $L\in\mathbb{R}$.
   > Suppose that $u_n\to 0$. If there exists $N_0\in\mathbb{N}$ such that
   > $|x_n-L|\le u_n$ for every $n\ge N_0$, then $x_n\to L$.

222. () `thm:constant-sequence-convergence` — **Constant Sequence Convergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ converges to $c$.

223. () `thm:zero-sequence-is-null` — **Zero Sequence is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $x_n = 0$ for every $n \in \mathbb{N}$,
   > then $(x_n)$ is a null sequence.

224. () `thm:constant-null-sequence` — **Constant Null Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ is a null sequence if and only if
   > $c = 0$.

225. () `thm:difference-from-limit-is-null` — **Difference from the Limit is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L \in \mathbb{R}$. The sequence
   > $(x_n)$ converges to $L$ if and only if the sequence $(x_n - L)$ is a null
   > sequence.

226. () `thm:ultimately-constant-sequence-convergence` — **Ultimately Constant Sequence Convergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exist $N_0 \in \mathbb{N}$ and
   > $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$, then
   > $(x_n)$ converges to $c$.

227. () `thm:constant-implies-ultimately-constant` — **Constant Implies Ultimately Constant**
   > **Statement.**
   > Every constant real sequence is ultimately constant.

228. () `thm:ultimately-zero-sequence-is-null` — **Ultimately Zero Sequence is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exists $N_0 \in \mathbb{N}$ such
   > that $x_n = 0$ for every $n \ge N_0$, then $(x_n)$ is a null sequence.

229. () `thm:ultimately-constant-null-sequence` — **Ultimately Constant Null Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Suppose there exist $N_0 \in \mathbb{N}$
   > and $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$. Then
   > $(x_n)$ is a null sequence if and only if $c = 0$.

230. () `thm:tail-equality-preserves-convergence` — **Tail Equality Preserves Convergence**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences. If there exists
   > $N_0 \in \mathbb{N}$ such that $x_n = y_n$ for every $n \ge N_0$, then
   > for every $L \in \mathbb{R}$, $(x_n)$ converges to $L$ if and only if
   > $(y_n)$ converges to $L$.

231. () `thm:eventually-bounded-above-tail-formulation` — **Eventually Bounded Above Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded above if and
   > only if there exist $N_0 \in \mathbb{N}$ and $M \in \mathbb{R}$ such that
   > $x_n \le M$ for every $n \ge N_0$.

232. () `thm:eventually-bounded-below-tail-formulation` — **Eventually Bounded Below Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded below if and
   > only if there exist $N_0 \in \mathbb{N}$ and $m \in \mathbb{R}$ such that
   > $m \le x_n$ for every $n \ge N_0$.

233. () `thm:eventually-bounded-tail-formulation` — **Eventually Bounded Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if there exist $N_0 \in \mathbb{N}$ and $M > 0$ such that $|x_n| \le M$ for
   > every $n \ge N_0$.

234. () `thm:bounded-sequence-iff-bounded-above-and-below` — **Bounded Sequence If and Only If Bounded Above and Below**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if it is both bounded above and bounded below.

235. () `thm:absolute-bound-gives-upper-and-lower-bounds` — **Absolute Bound Gives Upper and Lower Bounds**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $K > 0$. If $|x_n| \le K$ for every
   > $n \in \mathbb{N}$, then $-K \le x_n \le K$ for every
   > $n \in \mathbb{N}$.

236. () `thm:upper-and-lower-bounds-give-absolute-bound` — **Upper and Lower Bounds Give an Absolute Bound**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exist $m,M \in \mathbb{R}$ such
   > that $m \le x_n \le M$ for every $n \in \mathbb{N}$, then there exists
   > $K > 0$ such that $|x_n| \le K$ for every $n \in \mathbb{N}$.

237. () `thm:divergence-to-infinity-implies-real-divergence` — **Divergence to Infinity Implies Real Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $x_n\to+\infty$ or $x_n\to-\infty$,
   > then $(x_n)$ is divergent.

238. () `thm:subsequence-indices-dominate-identity` — **Subsequence Indices Dominate the Identity**
   > **Statement.**
   > Let $\sigma:\mathbb{N}\to\mathbb{N}$ be a strictly increasing index map.
   > Then
   > \[
   >  k\le \sigma(k)
   >  \qquad
   >  \text{for every } k\in\mathbb{N}.
   > \]

239. () `thm:subsequences-preserve-limits` — **Subsequences Preserve Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then every subsequence of $(x_n)$ converges to $L$.

240. () `thm:subsequential-limit-of-convergent-sequence` — **Subsequential Limit of a Convergent Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $L$ is the only possible subsequential limit of $(x_n)$.

241. () `thm:divergence-by-two-subsequential-limits` — **Divergence by Two Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ has two distinct subsequential
   > limits, then $(x_n)$ does not converge.

242. () `thm:two-subsequential-limits-force-divergence` — **Two Subsequential Limits Force Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ has two subsequential limits
   > $L,K\in\mathbb{R}$ with $L\ne K$, then $(x_n)$ is divergent.

243. () `thm:unbounded-above-has-positive-infinity-subsequence` — **Unbounded Above Sequence Has a Positive-Infinity Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded above, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to+\infty$.

244. () `thm:unbounded-below-has-negative-infinity-subsequence` — **Unbounded Below Sequence Has a Negative-Infinity Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded below, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to-\infty$.

245. () `thm:bounded-divergence-produces-two-subsequential-limits` — **Bounded Divergence Produces Two Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. If $(x_n)$ is divergent, then
   > there exist $L,K\in\mathbb{R}$ with $L\ne K$ such that $L$ and $K$ are
   > subsequential limits of $(x_n)$.

246. () `thm:tail-suprema-are-decreasing` — **Tail Suprema Are Decreasing**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $(s_n)$ be its tail
   > supremum sequence. Then $(s_n)$ is decreasing.

247. () `thm:tail-infima-are-increasing` — **Tail Infima Are Increasing**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $(i_n)$ be its tail
   > infimum sequence. Then $(i_n)$ is increasing.

248. () `thm:liminf-below-limsup` — **Liminf Is Below Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >  \liminf_{n\to\infty}x_n\le \limsup_{n\to\infty}x_n.
   > \]

249. () `thm:convergence-iff-liminf-equals-limsup` — **Convergence iff Liminf Equals Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $L\in\mathbb{R}$. Then
   > $x_n\to L$ if and only if
   > \[
   >  \liminf_{n\to\infty}x_n
   >  =
   >  \limsup_{n\to\infty}x_n
   >  =
   >  L.
   > \]

250. () `thm:oscillation-criterion-via-liminf-limsup` — **Oscillation Criterion via Liminf and Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >  \liminf_{n\to\infty}x_n
   >  <
   >  \limsup_{n\to\infty}x_n
   > \]
   > if and only if $(x_n)$ has two distinct subsequential limits.

251. () `thm:limsup-comparison-under-eventual-order` — **Limsup Comparison Under Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >  \limsup_{n\to\infty}x_n
   >  \le
   >  \limsup_{n\to\infty}y_n.
   > \]

252. () `thm:liminf-comparison-under-eventual-order` — **Liminf Comparison Under Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >  \liminf_{n\to\infty}x_n
   >  \le
   >  \liminf_{n\to\infty}y_n.
   > \]

253. () `thm:limsup-squeeze-under-eventual-order` — **Limsup Squeeze Under Eventual Order**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
   > exists $N\in\mathbb{N}$ such that
   > \[
   >  a_n\le x_n\le b_n
   >  \qquad\text{for every }n\ge N,
   > \]
   > then
   > \[
   >  \limsup_{n\to\infty}a_n
   >  \le
   >  \limsup_{n\to\infty}x_n
   >  \le
   >  \limsup_{n\to\infty}b_n.
   > \]

254. () `thm:liminf-squeeze-under-eventual-order` — **Liminf Squeeze Under Eventual Order**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
   > exists $N\in\mathbb{N}$ such that
   > \[
   >  a_n\le x_n\le b_n
   >  \qquad\text{for every }n\ge N,
   > \]
   > then
   > \[
   >  \liminf_{n\to\infty}a_n
   >  \le
   >  \liminf_{n\to\infty}x_n
   >  \le
   >  \liminf_{n\to\infty}b_n.
   > \]

255. () `thm:strict-monotonicity-implies-monotonicity` — **Strict Monotonicity Implies Monotonicity**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is strictly increasing, then $(x_n)$ is increasing.
   > - If $(x_n)$ is strictly decreasing, then $(x_n)$ is decreasing.

256. () `thm:convergence-of-tail` — **Convergence of a Tail**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $m \in \mathbb{N}$. The
   > $m$-tail $(x_{m+n})_{n \in \mathbb{N}}$ converges if and only if
   > $(x_n)$ converges. Moreover, in this case,
   > \[
   >  \lim_{n \to \infty} x_{m+n} \;=\; \lim_{n \to \infty} x_n.
   > \]

257. () `thm:eventually-monotone-convergence-theorem` — **Eventually Monotone Convergence Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is eventually increasing and bounded above, then
   >  $(x_n)$ converges.
   > - If $(x_n)$ is eventually decreasing and bounded below, then
   >  $(x_n)$ converges.
   > - If $(x_n)$ is eventually monotone and bounded, then $(x_n)$ converges.

258. () `thm:unbounded-monotone-divergence` — **Unbounded Monotone Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing and is not bounded above, then
   >  $x_n\to+\infty$.
   > - If $(x_n)$ is decreasing and is not bounded below, then
   >  $x_n\to-\infty$.

259. () `thm:algebraic-transformations-preserve-monotonicity` — **Algebraic Transformations Preserve Monotonicity**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $c,\alpha\in\mathbb{R}$.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing, then $(x_n+c)$ is increasing.
   > - If $(x_n)$ is decreasing, then $(x_n+c)$ is decreasing.
   > - If $(x_n)$ is increasing and $\alpha>0$, then $(\alpha x_n)$ is increasing.
   > - If $(x_n)$ is increasing and $\alpha<0$, then $(\alpha x_n)$ is decreasing.
   > - If $(x_n)$ is increasing, then $(-x_n)$ is decreasing.
   > - If $(x_n)$ is decreasing, then $(-x_n)$ is increasing.

260. () `thm:increasing-sequence-limit-as-supremum` — **Increasing Sequence Limit as Supremum**
   > **Statement.**
   > Let $(x_n)$ be an increasing real sequence that is bounded above. Then
   > \[
   >  \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   > \]

261. () `thm:decreasing-sequence-limit-as-infimum` — **Decreasing Sequence Limit as Infimum**
   > **Statement.**
   > Let $(x_n)$ be a decreasing real sequence that is bounded below. Then
   > \[
   >  \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   > \]

262. () `thm:tail-suprema-and-infima-converge` — **Tail Suprema and Infima Converge**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Define
   > \[
   >  s_n=\sup\{x_k:k\ge n\},
   >  \qquad
   >  i_n=\inf\{x_k:k\ge n\}.
   > \]
   > Then $(s_n)$ and $(i_n)$ converge.

263. () `thm:bounded-sequence-has-limsup-and-liminf` — **Bounded Sequence Has Limsup and Liminf**
   > **Statement.**
   > Every bounded real sequence has a limit superior and a limit inferior.

264. () `thm:monotonicity-passes-to-subsequences` — **Monotonicity Passes to Subsequences**
   > **Statement.**
   > Every subsequence of an increasing real sequence is increasing, and every
   > subsequence of a decreasing real sequence is decreasing.

265. () `thm:subsequence-of-subsequence` — **Subsequence of a Subsequence**
   > **Statement.**
   > Every subsequence of a subsequence of $(x_n)$ is a subsequence of $(x_n)$.

266. () `thm:eventual-properties-pass-to-subsequences` — **Eventual Properties Pass to Subsequences**
   > **Statement.**
   > Let $P(n)$ be a property of indices. If there exists $N\in\mathbb{N}$ such
   > that $P(n)$ holds for every $n\ge N$, then for every strictly increasing
   > index map $\sigma$ there exists $K\in\mathbb{N}$ such that $P(\sigma(k))$
   > holds for every $k\ge K$.

267. () `thm:subsequential-limits-respect-bounds` — **Subsequential Limits Respect Bounds**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L$ be a subsequential limit of
   > $(x_n)$. If $m\le x_n\le M$ for every $n\in\mathbb{N}$, then
   > $m\le L\le M$.

268. () `thm:squeeze-passes-to-subsequences` — **Squeeze Passes to Subsequences**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences. If
   > $a_n\le x_n\le b_n$ eventually, then for every subsequence
   > $(x_{\sigma(k)})$ there exists $K\in\mathbb{N}$ such that
   > \[
   >  a_{\sigma(k)}\le x_{\sigma(k)}\le b_{\sigma(k)}
   >  \qquad
   >  \text{for every } k\ge K.
   > \]

269. () `thm:sequential-compactness-closed-bounded-interval` — **Sequential Compactness of Closed Bounded Intervals**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ with $a\le b$. Every sequence in $[a,b]$ has a
   > convergent subsequence whose limit belongs to $[a,b]$.

270. () `thm:convergence-by-domination` — **Convergence by Domination**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. Let
   > $(a_n)$ be a sequence of positive real numbers with
   > $\displaystyle\lim_{n \to \infty} a_n = 0$. If there exist a constant
   > $c > 0$ and an index $m \in \mathbb{N}$ such that
   > \[
   >  |x_n - L| \;\le\; c\, a_n \qquad \forall n \ge m,
   > \]
   > then $\displaystyle\lim_{n \to \infty} x_n = L$.

271. () `thm:ratio-limit-less-than-one-implies-null` — **Ratio Limit Less Than One Implies Null**
   > **Statement.**
   > Let $(x_n)$ be a sequence of positive real numbers. Suppose that the
   > limit
   > \[
   >  L := \lim_{n\to\infty}\frac{x_{n+1}}{x_n}
   > \]
   > exists. If $L<1$, then $(x_n)$ converges and
   > \[
   >  \lim_{n\to\infty} x_n = 0.
   > \]

272. () `lem:finite-sum-splitting` — **Splitting a Finite Sum**
   > **Statement.**
   > Let \(m \le n < p\) be integers, and let \(a_i\) be a real number
   > assigned to each integer \(i\) satisfying \(m \le i \le p\). Then
   > \[
   >  \sum_{i=m}^{n} a_i
   >  +
   >  \sum_{i=n+1}^{p} a_i
   >  =
   >  \sum_{i=m}^{p} a_i.
   > \]

273. () `prop:finite-summations-well-defined` — **Finite Summations Are Well-Defined**
   > **Statement.**
   > Let \(X\) be a finite set with \(n\) elements, where \(n \in \mathbb{N}\),
   > let \(f:X\to\mathbb{R}\), and let
   > \[
   >  g:\{i\in\mathbb{N}:1\le i\le n\}\to X
   >  \qquad\text{and}\qquad
   >  h:\{i\in\mathbb{N}:1\le i\le n\}\to X
   > \]
   > be bijections. Then
   > \[
   >  \sum_{i=1}^{n} f(g(i))
   >  =
   >  \sum_{i=1}^{n} f(h(i)).
   > \]

274. () `prop:empty-finite-set-summation` — **Empty Finite Set Summation**
   > **Statement.**
   > If \(X\) is empty, and \(f:X\to\mathbb{R}\) is a function, then
   > \[
   >  \sum_{x\in X} f(x)=0.
   > \]

275. () `prop:singleton-finite-set-summation` — **Singleton Finite Set Summation**
   > **Statement.**
   > If \(X\) consists of a single element, \(X=\{x_0\}\), and
   > \(f:X\to\mathbb{R}\) is a function, then
   > \[
   >  \sum_{x\in X} f(x)=f(x_0).
   > \]

276. () `prop:substitution-finite-set-summation` — **Substitution for Finite Set Summation**
   > **Statement.**
   > If \(X\) is a finite set, \(f:X\to\mathbb{R}\) is a function, and
   > \(g:Y\to X\) is a bijection, then
   > \[
   >  \sum_{x\in X} f(x)
   >  =
   >  \sum_{y\in Y} f(g(y)).
   > \]

277. () `prop:integer-interval-finite-set-summation` — **Integer Interval as a Finite Set**
   > **Statement.**
   > Let \(n \le m\) be integers, and let
   > \[
   >  X:=\{i\in\mathbb{Z}:n\le i\le m\}.
   > \]
   > If \(a_i\) is a real number assigned to each integer \(i\in X\), then
   > \[
   >  \sum_{i=n}^{m} a_i
   >  =
   >  \sum_{i\in X} a_i.
   > \]

278. () `prop:disjoint-union-finite-set-summation` — **Disjoint Union Finite Set Summation**
   > **Statement.**
   > Let \(X\) and \(Y\) be disjoint finite sets, so \(X\cap Y=\emptyset\),
   > and let \(f:X\cup Y\to\mathbb{R}\) be a function. Then
   > \[
   >  \sum_{z\in X\cup Y} f(z)
   >  =
   >  \left(\sum_{x\in X} f(x)\right)
   >  +
   >  \left(\sum_{y\in Y} f(y)\right).
   > \]

279. () `prop:addition-rule-finite-set-summation` — **Addition Rule for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) and
   > \(g:X\to\mathbb{R}\) be functions. Then
   > \[
   >  \sum_{x\in X} (f(x)+g(x))
   >  =
   >  \sum_{x\in X} f(x)
   >  +
   >  \sum_{x\in X} g(x).
   > \]

280. () `prop:scalar-multiplication-rule-finite-set-summation` — **Scalar Multiplication Rule for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, let \(f:X\to\mathbb{R}\) be a function, and
   > let \(c\) be a real number. Then
   > \[
   >  \sum_{x\in X} c f(x)
   >  =
   >  c \sum_{x\in X} f(x).
   > \]

281. () `prop:monotonicity-finite-set-summation` — **Monotonicity for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) and
   > \(g:X\to\mathbb{R}\) be functions such that \(f(x)\le g(x)\) for all
   > \(x\in X\). Then
   > \[
   >  \sum_{x\in X} f(x)
   >  \le
   >  \sum_{x\in X} g(x).
   > \]

282. () `prop:triangle-inequality-finite-set-summation` — **Triangle Inequality for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) be a function.
   > Then
   > \[
   >  \left\lvert \sum_{x\in X} f(x) \right\rvert
   >  \le
   >  \sum_{x\in X} \lvert f(x)\rvert.
   > \]

283. () `lem:iterated-summation-over-product` — **Iterated Summation over a Product**
   > **Statement.**
   > Let \(X\) and \(Y\) be finite sets, and let
   > \(f:X\times Y\to\mathbb{R}\) be a function. Then
   > \[
   >  \sum_{x\in X}
   >  \left(
   >  \sum_{y\in Y} f(x,y)
   >  \right)
   >  =
   >  \sum_{(x,y)\in X\times Y} f(x,y).
   > \]

284. () `cor:fubini-theorem-finite-series` — **Fubini's Theorem for Finite Series**
   > **Statement.**
   > Let \(X\) and \(Y\) be finite sets, and let
   > \(f:X\times Y\to\mathbb{R}\) be a function. Then
   > \[
   >  \sum_{x\in X}
   >  \left(
   >  \sum_{y\in Y} f(x,y)
   >  \right)
   >  =
   >  \sum_{(x,y)\in X\times Y} f(x,y)
   >  =
   >  \sum_{(y,x)\in Y\times X} f(x,y)
   >  =
   >  \sum_{y\in Y}
   >  \left(
   >  \sum_{x\in X} f(x,y)
   >  \right).
   > \]

285. () `lem:finite-sum-reindexing` — **Reindexing a Finite Sum**
   > **Statement.**
   > Let \(m \le n\) be integers, let \(k\) be an integer, and let \(a_i\)
   > be a real number assigned to each integer \(i\) satisfying \(m \le i
   > \le n\). Then
   > \[
   >  \sum_{i=m}^{n} a_i
   >  =
   >  \sum_{j=m+k}^{n+k} a_{j-k}.
   > \]

286. () `lem:finite-sum-of-sums` — **Finite Sum of Sums**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) and \(b_i\) be real
   > numbers assigned to each integer \(i\) satisfying \(m \le i \le n\).
   > Then
   > \[
   >  \sum_{i=m}^{n} (a_i+b_i)
   >  =
   >  \left(\sum_{i=m}^{n} a_i\right)
   >  +
   >  \left(\sum_{i=m}^{n} b_i\right).
   > \]

287. () `lem:finite-sum-scalar-multiple` — **Finite Sum of Scalar Multiples**
   > **Statement.**
   > Let \(m \le n\) be integers, let \(a_i\) be a real number assigned to
   > each integer \(i\) satisfying \(m \le i \le n\), and let
   > \(c \in \mathbb{R}\). Then
   > \[
   >  \sum_{i=m}^{n} (c a_i)
   >  =
   >  c\left(\sum_{i=m}^{n} a_i\right).
   > \]

288. () `lem:triangle-inequality-finite-series` — **Triangle Inequality for Finite Series**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) be a real number assigned
   > to each integer \(i\) satisfying \(m \le i \le n\). Then
   > \[
   >  \left\lvert \sum_{i=m}^{n} a_i \right\rvert
   >  \le
   >  \sum_{i=m}^{n} \lvert a_i\rvert.
   > \]

289. () `lem:comparison-test-finite-series` — **Comparison Test for Finite Series**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) and \(b_i\) be real
   > numbers assigned to each integer \(i\) satisfying \(m \le i \le n\).
   > Suppose that \(a_i \le b_i\) for all \(i\) satisfying \(m \le i \le n\).
   > Then
   > \[
   >  \sum_{i=m}^{n} a_i
   >  \le
   >  \sum_{i=m}^{n} b_i.
   > \]

290. () `prop:hyperbolic-pythagorean` — **Hyperbolic Pythagorean Identity**
   > **Statement.**
   > For all $x \in \mathbb{R}$:
   > \[
   >  \cosh^2 x - \sinh^2 x = 1.
   > \]

291. () `prop:hyperbolic-addition` — **Addition Formulas for Hyperbolic Functions**
   > **Statement.**
   > For all $x, y \in \mathbb{R}$:
   > \[
   >  \sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y,
   >  \qquad
   >  \cosh(x+y) = \cosh x \cosh y + \sinh x \sinh y.
   > \]

292. () `prop:tanh-limits` — **Limits of $\tanh$**
   > **Statement.**
   > \[
   >  \lim_{x \to +\infty} \tanh x = 1,
   >  \qquad
   >  \lim_{x \to -\infty} \tanh x = -1.
   > \]

293. () `prop:limit-logarithm-fundamental` — **Fundamental Logarithmic Limit**
   > **Statement.**
   > \[
   >  \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1.
   > \]

294. () `prop:limit-exponential-fundamental` — **Fundamental Exponential Limit**
   > **Statement.**
   > \[
   >  \lim_{x \to 0} \frac{e^x - 1}{x} = 1.
   > \]

295. () `prop:power-dominates-log` — **Every Power Dominates the Logarithm**
   > **Statement.**
   > For every $r > 0$:
   > \[
   >  \lim_{x \to \infty} \frac{\ln x}{x^r} = 0
   >  \qquad\text{and}\qquad
   >  \lim_{x \to 0^+} x^r \ln x = 0.
   > \]

296. () `prop:limit-compound-interest` — **Compound Interest Limit**
   > **Statement.**
   > \[
   >  \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e.
   > \]

297. () `prop:exponential-dominates-power` — **Exponential Dominates Every Power**
   > **Statement.**
   > For every $r > 0$:
   > \[
   >  \lim_{x \to \infty} \frac{x^r}{e^x} = 0.
   > \]

298. () `prop:pythagorean-identity` — **Pythagorean Identity**
   > **Statement.**
   > For all $x \in \mathbb{R}$:
   > \[
   >  \sin^2 x + \cos^2 x = 1.
   > \]

299. () `prop:trig-addition-formulas` — **Addition Formulas**
   > **Statement.**
   > For all $x, y \in \mathbb{R}$:
   > \[
   >  \sin(x+y) = \sin x \cos y + \cos x \sin y,
   >  \qquad
   >  \cos(x+y) = \cos x \cos y - \sin x \sin y.
   > \]

300. () `thm:fundamental-trig-limit` — **Fundamental Trigonometric Limit**
   > **Statement.**
   > \[
   >  \lim_{x \to 0} \frac{\sin x}{x} = 1.
   > \]

301. () `prop:limit-one-minus-cos` — **Second Fundamental Trigonometric Limit**
   > **Statement.**
   > \[
   >  \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}.
   > \]

302. () `thm:heine-cantor` — **Heine--Cantor Theorem**
   > **Statement.**
   > Let $a,b \in \mathbb{R}$ with $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then $f$ is uniformly continuous on $[a,b]$.

303. () `thm:step-function-approximation` — **Step Function Approximation**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous and let $\varepsilon>0$.
   > Then there exists a step function $s_\varepsilon:[a,b]\to\mathbb{R}$ such that
   > \[
   > \sup_{x\in[a,b]} |f(x)-s_\varepsilon(x)|<\varepsilon.
   > \]

304. () `thm:piecewise-linear-approximation` — **Piecewise Linear Approximation**
   > **Statement.**
   > Let $f\colon[a,b]\to\mathbb{R}$ be continuous and let $\varepsilon>0$. Then there exists a continuous piecewise linear function $\ell_\varepsilon\colon[a,b]\to\mathbb{R}$ such that $\sup_{x\in[a,b]}|f(x)-\ell_\varepsilon(x)|<\varepsilon$. \hyperref[prf:piecewise-linear-approximation]{Go to proof.}

305. () `thm:bernstein-approximation` — **Bernstein Approximation Theorem**
   > **Statement.**
   > Let $f:[0,1]\to\mathbb{R}$ be continuous, and for each $n\in\mathbb{N}$ let $B_n$ denote the $n$th Bernstein polynomial of $f$. Then for every $\varepsilon>0$ there exists $n_\varepsilon\in\mathbb{N}$ such that $\|f-B_n\|_\infty<\varepsilon$ for all $n\ge n_\varepsilon$. \hyperref[prf:bernstein-approximation]{Go to proof.}

306. () `thm:weierstrass-approximation` — **Weierstrass Approximation Theorem**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous. For every $\varepsilon>0$ there exists a polynomial $p_\varepsilon\in\mathbb{R}[x]$ such that $\|f-p_\varepsilon\|_{\infty,[a,b]}<\varepsilon$.

307. () `lem:every-point-covered-by-tag` — **Every Point Is Covered by a Tag**
   > **Statement.**
   > Let $\dot{\mathcal{P}}=\{([x_{i-1},x_i],t_i)\}_{i=1}^n$ be a tagged partition of $[a,b]$ that is $\delta$-fine on $[a,b]$, and let $x\in[a,b]$. Then there exists $i\in\{1,\ldots,n\}$ such that $|x-t_i|<\delta(t_i)$.

308. () `thm:cousins-theorem` — **Cousin's Theorem**
   > **Statement.**
   > Every gauge $\delta:[a,b]\to(0,\infty)$ on a closed interval $[a,b]$
   > admits a $\delta$-fine tagged partition of $[a,b]$.

309. () `thm:boundedness-theorem` — **Boundedness Theorem**
   > **Statement.**
   > Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then there exists $M>0$ such that $|f(x)|\le M$ for every $x\in[a,b]$.

310. () `thm:extreme-value-theorem` — **Extreme Value Theorem**
   > **Statement.**
   > Let $a,b \in \mathbb{R}$ with $a<b$, and let $f:[a,b] \to \mathbb{R}$ be continuous. There exist points $x_m,x_M \in [a,b]$ such that $f(x_m) \le f(x) \le f(x_M)$ for every $x \in [a,b]$. Equivalently, $f$ attains both an absolute maximum and an absolute minimum on $[a,b]$.

311. () `thm:bolzano-intermediate-value` — **Bolzano's Intermediate Value Theorem**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f \colon I \to \mathbb{R}$ be continuous on $I$, and choose $a,b \in I$ with $f(a) < k < f(b)$. Then there exists $c \in I$ such that $\min\{a,b\} < c < \max\{a,b\}$ and $f(c) = k$. \hyperref[prf:bolzano-intermediate-value]{Go to proof.}

312. () `thm:location-of-roots` — **Location of Roots**
   > **Statement.**
   > Let $a,b \in \mathbb{R}$ with $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous. If either $f(a)<0<f(b)$ or $f(a)>0>f(b)$, then there exists $c\in(a,b)$ such that $f(c)=0$.

313. () `thm:image-of-closed-bounded-interval` — **Image of Closed Bounded Interval Is Closed Bounded Interval**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous. Then $f([a,b])=[\min_{[a,b]} f,\max_{[a,b]} f]$.

314. () `thm:preservation-of-intervals` — **Preservation of Intervals**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval and let $f:I \to \mathbb{R}$ be continuous. Then $f(I)$ is an interval.

315. () `thm:darboux-property` — **Darboux Property**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ satisfy $a<b$, let $f:[a,b]\to\mathbb{R}$ be continuous, and fix $c\in\mathbb{R}$. If $f(x)\neq c$ for every $x\in[a,b]$, then either $f(x)>c$ for all $x\in[a,b]$ or $f(x)<c$ for all $x\in[a,b]$.

316. () `thm:limit-sum` — **Sum Rule for Function Limits**
   > **Statement.**
   > Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(f+g)(x)=L+M.
   > \]

317. () `thm:limit-difference` — **Difference Rule for Function Limits**
   > **Statement.**
   > Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(f-g)(x)=L-M.
   > \]

318. () `thm:limit-scalar-multiple` — **Scalar Multiple Rule for Function Limits**
   > **Statement.**
   > Let $f:A\to\mathbb{R}$, let $c$ be a cluster point of $A$, and let
   > $\alpha\in\mathbb{R}$. If $\lim_{x\to c}f(x)=L$, then
   > \[
   >  \lim_{x\to c}(\alpha f)(x)=\alpha L.
   > \]

319. () `thm:limit-product` — **Product Rule for Function Limits**
   > **Statement.**
   > Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(fg)(x)=LM.
   > \]

320. () `thm:limit-quotient` — **Quotient Rule for Function Limits**
   > **Statement.**
   > Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$, $\lim_{x\to c}g(x)=M$, and $M\neq 0$, then
   > there exists $\delta_0>0$ such that $g(x)\neq 0$ whenever $x\in A$ and
   > $0<|x-c|<\delta_0$, and
   > \[
   >  \lim_{x\to c}\frac{f(x)}{g(x)}=\frac{L}{M}.
   > \]

321. () `prop:limit-neighbourhood-equiv` — **Neighbourhood Form of the Limit**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every
   > $\varepsilon$-neighbourhood $V_\varepsilon(L)$ there exists a
   > $\delta$-neighbourhood $V_\delta(c)$ such that
   > $x\in V_\delta^*(c)\cap A$ implies $f(x)\in V_\varepsilon(L)$.

322. () `thm:limit-unique` — **Uniqueness of Limits of Functions**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $f$ has at most one limit at $c$.

323. () `prop:sequential-criterion-limits` — **Sequential Criterion for Function Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every sequence
   > $(x_n)\subseteq A\setminus\{c\}$ with $x_n\to c$, one has
   > $f(x_n)\to L$.

324. () `cor:limit-three-equiv` — **Three Equivalent Forms of the Function Limit**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > The $\varepsilon$-$\delta$ form of $\lim_{x\to c}f(x)=L$, the
   > neighbourhood form, and the sequential form are equivalent descriptions
   > of the same limit condition.

325. () `thm:limit-implies-local-bounding` — **Limit Implies Local Boundedness**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$ for some $L \in \mathbb{R}$,
   > then there exist $\delta, M > 0$ such that $|f(x)| \leq M$ for all
   > $x \in A$ with $0<|x-c|<\delta$.

326. () `thm:bounded-limits` — **Bounded Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$, let $c$ be a cluster point of $A$, and
   > let $a, b \in \mathbb{R}$. If $a \leq f(x) \leq b$ for all $x \in A$
   > with $x \neq c$, and $\lim_{x\to c}f(x)=L$, then
   > $a \leq L \leq b$.

327. () `thm:squeeze-function-limits` — **Squeeze Theorem for Function Limits**
   > **Statement.**
   > Let $f, g, h : A \to \mathbb{R}$ and let $c$ be a cluster point of
   > $A$. Suppose $\lim_{x\to c}f(x)=L =
   > \lim_{x\to c}g(x)=L$, and suppose there exists
   > $\delta_0 > 0$ such that
   > \[
   >  \forall x \in A,\;
   >  0 < |x - c| < \delta_0
   >  \;\Rightarrow\;
   >  f(x) \leq h(x) \leq g(x).
   > \]
   > Then $\lim_{x\to c}h(x)=L$.

328. () `thm:limits-are-local` — **Limits Are Local**
   > **Statement.**
   > Let $E \subseteq X \subseteq \mathbb{R}$, let $x_0$ be a cluster
   > point of $E$, let $f : X \to \mathbb{R}$, and let $\delta > 0$.
   > Then
   > \[
   >  \lim_{x\to x_0;\,x\in E}f(x)=L
   >  \;\iff\;
   >  \lim_{x\to x_0;\,x\in E\cap(x_0-\delta,x_0+\delta)}f(x)=L.
   > \]

329. () `prop:limit-absolute-value` — **Limit of Absolute Value**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$, then
   > $\lim_{x\to c}|f(x)|=|L|$.

330. () `thm:composition-of-limits` — **Composition of Limits**
   > **Statement.**
   > Let $f : A \to B$, let $g : B \to \mathbb{R}$, let $c_1$ be a
   > cluster point of $A$, and let $c_2 \in \mathbb{R}$ be a cluster
   > point of $B$. Suppose $\lim_{x\to c_1}f(x)=c_2$ and
   > $\lim_{y\to c_2}g(y)=L$. If $c_2 \in B$, assume also that
   > $g(c_2) = L$. Then $\lim_{x\to c_1}g(f(x))=L$.

331. () `thm:monotone-limit-theorem` — **Monotone Limit Theorem**
   > **Statement.**
   > Let $a < b$ and let $f : (a,b) \to \mathbb{R}$ be monotone and
   > bounded. Then both one-sided limits exist at every interior point.
   > For increasing $f$ and every $x_0 \in (a,b)$:
   > \[
   >  f(x_0^-) = \sup\{\,f(x) : a < x < x_0\,\},
   >  \qquad
   >  f(x_0^+) = \inf\{\,f(x) : x_0 < x < b\,\}.
   > \]

332. () `prop:cauchy-criterion-limits` — **Cauchy Criterion for Function Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ exists for some
   > $L \in \mathbb{R}$ if and only if
   > \[
   >  \ForallOT{\varepsilon},\;
   >  \ExistsIT{\delta},\;
   >  \forall x, y \in A :\;
   >  0<|x-c|<\delta
   >  \;\wedge\;
   >  0<|y-c|<\delta
   >  \;\Rightarrow\;
   >  |f(x)-f(y)|<\varepsilon.
   > \]

333. () `thm:sequential-criterion-right-hand-limit` — **Sequential Criterion for Right-Hand Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(c,\infty)$. Then $\lim_{x\to c^+}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(c,\infty)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.

334. () `cor:sequential-criterion-left-hand-limit` — **Sequential Criterion for Left-Hand Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(-\infty,c)$. Then $\lim_{x\to c^-}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(-\infty,c)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.

335. () `thm:two-sided-limit-iff-matching-one-sided-limits` — **Two-Sided Limit via One-Sided Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ and let $f:A\to\mathbb{R}$. If $c$ is a
   > cluster point of both $A\cap(c,\infty)$ and $A\cap(-\infty,c)$, then
   > $\lim_{x\to c}f(x)=L$ if and only if both $\lim_{x\to c^+}f(x)=L$ and
   > $\lim_{x\to c^-}f(x)=L$.

336. () `prop:limsup-geq-liminf-function` — **$\limsup\geq\liminf$**
   > **Statement.**
   > Let $A\subseteq \mathbb{R}$, let $x_0$ be a limit point of $A$, and let $f:A\to\mathbb{R}$. Then
   > \[
   > \limsup_{x\to x_0} f(x) \ge \liminf_{x\to x_0} f(x).
   > \]

337. () `prop:limsup-liminf-limit-criterion` — **Limit Exists iff $\limsup=\liminf$**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, let $x_0$ be a limit point of $A$ with $x_0 \in \mathbb{R}$, and let $L \in \mathbb{R}$. Then $\lim_{x \to x_0} f(x)$ exists and equals $L$ if and only if $\limsup_{x \to x_0} f(x) = \liminf_{x \to x_0} f(x) = L$.

338. () `thm:monotone-one-sided-limits` — **One-Sided Limits of Monotone Functions**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $c$ be interior to $I$, and let $f:I\to\mathbb{R}$ be increasing. Define
   > \[
   > L_- \coloneqq \sup\{f(x): x\in I,\; x<c\},
   > \qquad
   > L_+ \coloneqq \inf\{f(x): x\in I,\; c<x\}.
   > \]
   > Then both one-sided limits exist and satisfy
   > \[
   > \lim_{x\to c^-} f(x) = L_-,
   > \qquad
   > \lim_{x\to c^+} f(x) = L_+.
   > \]

339. () `cor:monotone-continuity-criterion` — **Continuity Criterion for Monotone Functions**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f:I \to \mathbb{R}$ be monotone increasing, and let $c$ be an interior point of $I$. Then $f$ is continuous at $c$ if and only if its one-sided limits satisfy $f(c^-)=f(c)=f(c^+)$, where $f(c^-)=\lim_{x\to c^-} f(x)$ and $f(c^+)=\lim_{x\to c^+} f(x)$.

340. () `prop:monotone-discontinuities-first-kind` — **Discontinuities of a Monotone Function Are of First Kind**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f:I \to \mathbb{R}$ be monotone, and let $a \in I$ be such that there exist points of $I$ strictly less and strictly greater than $a$. If $f$ is discontinuous at $a$, then both one-sided limits $\lim_{x\uparrow a} f(x)$ and $\lim_{x\downarrow a} f(x)$ exist in $\mathbb{R}$.

341. () `cor:jump-intervals-for-monotone-discontinuities` — **Jump Intervals Are Disjoint**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval and let $f:I \to \mathbb{R}$ be nondecreasing. If $a,b \in I$ are distinct points of discontinuity of $f$, then the open intervals $(f(a^-),f(a^+))$ and $(f(b^-),f(b^+))$ are disjoint.

342. () `thm:monotone-discontinuities-countable` — **Discontinuities of a Monotone Function Are Countable**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be monotone. Then the set $D_f \coloneqq \{c \in I : f \text{ is discontinuous at } c\}$ is at most countable. \hyperref[prf:monotone-discontinuities-countable]{Go to proof.}

343. () `cor:monotone-continuous-on-dense-set` — **Monotone Function Is Continuous on a Dense Set**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be monotone. Then the set $\{x\in[a,b]:f \text{ is continuous at } x\}$ is dense in $[a,b]$.

344. () `prop:continuous-injective-iff-strictly-monotone` — **Continuous Injective Is Strictly Monotone**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then $f$ is injective if and only if $f$ is strictly monotone on $[a,b]$.

345. () `thm:continuous-inverse-theorem` — **Continuous Inverse Theorem**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be strictly monotone and continuous on $I$. Then the inverse function $f^{-1}:f(I)\to I$ exists, is strictly monotone, and is continuous on $f(I)$.

346. () `lem:equivalent-discontinuity-at-a-point` — **Equivalent Formulations of Discontinuity at a Point**
   > **Statement.**
   > Let $A\subseteq \mathbb{R}$, let $f:A\to\mathbb{R}$, and let $c\in A$. The following are equivalent:
   > - $c$ is a point of discontinuity in the $\varepsilon$-$\delta$ sense.
   > - $c$ is a sequential point of discontinuity.
   > - $c$ is a neighbourhood point of discontinuity.

347. () `thm:continuity-iff-zero-oscillation` — **Continuity Characterised by Oscillation**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, and let $c \in A$. Then $f$ is continuous at $c$ if and only if $\omega(f;c)=0$.

348. () `prop:discontinuity-set-via-oscillation` — **Discontinuity Set via Oscillation**
   > **Statement.**
   > Let $f:E\to\mathbb{R}$. Then
   > \[
   > D(f):=\{x\in E: f \text{ is discontinuous at } x\}
   > =\{x\in E: \omega(f;x)>0\}
   > =\bigcup_{n=1}^{\infty} \{x\in E: \omega(f;x)\ge 1/n\}.
   > \]

349. () `thm:algebra-of-uniform-continuity-general` — **Algebra of Uniform Continuity on a General Domain**
   > **Statement.**
   > - [label=(\alph*)]
   > - For every set $A \subseteq \mathbb{R}$, every pair of functions $f,g : A \to \mathbb{R}$ that are uniformly continuous on $A$, and every scalar $c \in \mathbb{R}$, the functions $f+g$, $f-g$, and $cf$ are uniformly continuous on $A$.
   > - There exist a set $A \subseteq \mathbb{R}$ and uniformly continuous functions $f,g : A \to \mathbb{R}$ such that the product $fg$ is not uniformly continuous on $A$.

350. () `thm:algebra-of-uniform-continuity-bounded` — **Algebra of Uniform Continuity on a Bounded Domain**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ be bounded, and let $f,g:A \to \mathbb{R}$ be uniformly continuous on $A$.
   > - [label=(\alph*)]
   > - The product $x \mapsto f(x)g(x)$ is uniformly continuous on $A$.
   > - If there exists $k>0$ such that $|g(x)| \ge k$ for all $x \in A$, then the quotient $x \mapsto f(x)/g(x)$ is uniformly continuous on $A$.

351. () `prop:sequential-uniform-continuity` — **Sequential Characterization of Uniform Continuity**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ and let $f:A \to \mathbb{R}$. Then $f$ is uniformly continuous on $A$ if and only if for every pair of sequences $(x_n)$ and $(y_n)$ in $A$ with $\lim_{n \to \infty} (x_n - y_n) = 0$ we have $\lim_{n \to \infty} (f(x_n) - f(y_n)) = 0$.

352. () `prop:uniform-continuity-cauchy` — **Uniform Continuity Preserves Cauchy Sequences**
   > **Statement.**
   > Let $S \subseteq \mathbb{R}$, let $f:S \to \mathbb{R}$, and let $(x_n)$ be a sequence in $S$. If $f$ is uniformly continuous on $S$ and $(x_n)$ is a Cauchy sequence in $S$, then $(f(x_n))$ is a Cauchy sequence in $\mathbb{R}$.

353. () `prop:lipschitz-implies-uc` — **Lipschitz Implies Uniform Continuity**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ and $f:A \to \mathbb{R}$. If there exists $K \ge 0$ such that $|f(x)-f(y)| \le K |x-y|$ for all $x,y \in A$, then $f$ is uniformly continuous on $A$.

354. () `thm:algebra-of-lipschitz-functions` — **Algebra of Lipschitz Functions**
   > **Statement.**
   > Let $A\subseteq \mathbb{R}$ and let $f,g:A\to\mathbb{R}$ be Lipschitz with constants $K_f,K_g\ge 0$ respectively.
   > - [label=(\alph*)]
   > - For every $c\in\mathbb{R}$, the function $cf$ is Lipschitz on $A$ with constant $|c|K_f$.
   > - The functions $f+g$ and $f-g$ are Lipschitz on $A$ with constant $K_f+K_g$.
   > - If $B\subseteq\mathbb{R}$, $h:B\to\mathbb{R}$ is Lipschitz with constant $K_h\ge 0$, and $f(A)\subseteq B$, then $h\circ f$ is Lipschitz on $A$ with constant $K_hK_f$.
   > - If $|f(x)|\le M_f$ and $|g(x)|\le M_g$ for all $x\in A$, then $fg$ is Lipschitz on $A$ with constant $M_gK_f+M_fK_g$.
   > - If $|f(x)|\le M_f$ for all $x\in A$, if $|g(x)|\ge k>0$ for all $x\in A$, and if $g$ is Lipschitz on $A$ with constant $K_g$, then $f/g$ is Lipschitz on $A$ with constant $K_f/k + M_fK_g/k^2$.

355. () `thm:bilipschitz-inverse-is-lipschitz` — **Inverse of a Bi-Lipschitz Map Is Lipschitz**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f:A \to \mathbb{R}$, and suppose there exist constants $\alpha,K>0$ such that
   > $\alpha |x-y| \le |f(x)-f(y)| \le K |x-y|$ for all $x,y \in A$. Then $f$ is injective, the inverse mapping $f^{-1}:f(A) \to A$ is well defined, and
   > \[
   > \frac{1}{K}|u-v| \le |f^{-1}(u)-f^{-1}(v)| \le \frac{1}{\alpha}|u-v|
   > \quad\text{for all } u,v \in f(A).
   > \]

356. () `thm:constant-multiple-rule` — **Constant Multiple Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable at $c$, then $\alpha f$ is differentiable at $c$, and
   > \[
   > (\alpha f)'(c) = \alpha f'(c).
   > \]

357. () `thm:sum-rule` — **Sum Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If $f$ and $g$ are differentiable at $c$, then $f + g$ is differentiable at $c$, and
   > \[
   > (f+g)'(c) = f'(c) + g'(c).
   > \]

358. () `thm:differentiable-implies-continuous` — **Differentiable Implies Continuous**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and $c \in A$. If $f$ is differentiable at $c$, then $f$ is continuous at $c$.

359. () `thm:product-rule` — **Product Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If $f$ and $g$ are differentiable at $c$, then $fg$ is differentiable at $c$, and
   > \[
   > (fg)'(c) = f'(c)g(c) + f(c)g'(c).
   > \]

360. () `thm:quotient-rule` — **Quotient Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. Suppose that $f$ and $g$ are differentiable at $c$ and that $g(c) \neq 0$. Then $f/g$ is differentiable at $c$, and
   > \[
   > \left(\frac{f}{g}\right)'(c) = \frac{f'(c)g(c) - f(c)g'(c)}{(g(c))^2}.
   > \]

361. () `cor:finite-sum-rule` — **Finite Sum Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then $\sum_{i=1}^{n} \alpha_i f_i$ is differentiable at $c$, and
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(c) = \sum_{i=1}^{n} \alpha_i f_i'(c).
   > \]

362. () `cor:extended-product-rule` — **Extended Product Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then $\prod_{i=1}^{n} f_i$ is differentiable at $c$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(c)
   > =
   > \sum_{k=1}^{n}
   > f_k'(c) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(c).
   > \]

363. () `cor:power-rule-special-case` — **Power Rule for Integer Powers of a Function**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $n \in \mathbb{N}$. If $f$ is differentiable at $c$, then $f^n$ is differentiable at $c$, and
   > \[
   > (f^n)'(c) = n(f(c))^{n-1}f'(c).
   > \]

364. () `thm:finite-linear-combination-rule` — **Finite Linear Combination Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(c) = \sum_{i=1}^{n} \alpha_i f_i'(c).
   > \]

365. () `thm:constant-multiple-rule-interval` — **Constant Multiple Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable on $I$, then $\alpha f$ is differentiable on $I$, and
   > \[
   > (\alpha f)'(x) = \alpha f'(x) \qquad \text{for all } x \in I.
   > \]

366. () `thm:sum-rule-interval` — **Sum Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $f + g$ is differentiable on $I$, and
   > \[
   > (f+g)'(x) = f'(x) + g'(x) \qquad \text{for all } x \in I.
   > \]

367. () `thm:product-rule-interval` — **Product Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $fg$ is differentiable on $I$, and
   > \[
   > (fg)'(x) = f'(x)g(x) + f(x)g'(x) \qquad \text{for all } x \in I.
   > \]

368. () `thm:quotient-rule-interval` — **Quotient Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. Suppose that $f$ and $g$ are differentiable on $I$ and that $g(x) \neq 0$ for all $x \in I$. Then $f/g$ is differentiable on $I$, and
   > \[
   > \left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2} \qquad \text{for all } x \in I.
   > \]

369. () `cor:finite-sum-rule-interval` — **Finite Sum Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\sum_{i=1}^{n} \alpha_i f_i$ is differentiable on $I$, and
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

370. () `cor:extended-product-rule-interval` — **Extended Product Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f_1, \dots, f_n : I \to \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\prod_{i=1}^{n} f_i$ is differentiable on $I$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(x)
   > = \sum_{k=1}^{n} f_k'(x) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(x)
   > \qquad \text{for all } x \in I.
   > \]

371. () `cor:power-rule-special-case-interval` — **Power Rule for Integer Powers of a Function on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $n \in \mathbb{N}$. If $f$ is differentiable on $I$, then $f^n$ is differentiable on $I$, and
   > \[
   > (f^n)'(x) = n(f(x))^{n-1}f'(x) \qquad \text{for all } x \in I.
   > \]

372. () `thm:finite-linear-combination-rule-interval` — **Finite Linear Combination Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

373. () `thm:caratheodory-characterization-of-differentiability` — **Carath\'{e}odory Characterization of Differentiability**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $c \in I$. The following are equivalent:
   > - [label=(\roman*)]
   > - $f$ is differentiable at $c$.
   > - There exists a function $\phi : I \to \mathbb{R}$, continuous at $c$, such that
   > \[
   > f(x) = f(c) + (x-c)\,\phi(x) \qquad \text{for all } x \in I.
   > \]
   > In this case, $\phi(c) = f'(c)$.

374. () `thm:chain-rule` — **Chain Rule**
   > **Statement.**
   > Let $I, J \subseteq \mathbb{R}$ be intervals, let $f : I \to \mathbb{R}$ and $g : J \to \mathbb{R}$, and suppose that $f(I) \subseteq J$. Let $c \in I$. If $f$ is differentiable at $c$ and $g$ is differentiable at $f(c)$, then the composition $g \circ f$ is differentiable at $c$, and
   > \[
   > (g \circ f)'(c) = g'(f(c))\,f'(c).
   > \]

375. () `cor:inverse-function-derivative` — **Derivative of the Inverse Function**
   > **Statement.**
   > Under the hypotheses of \hyperref[thm:inverse-function-theorem-one-variable]{the one-variable Inverse Function Theorem}, the local inverse \(g\) satisfies
   > \[
   >  g'=\frac{1}{f'\circ g}
   > \]
   > on \(V\). More globally, if \(f:I\to J\) is a \(C^1\) bijection with \(f'(x)\neq 0\) for every \(x\in I\), then \(f^{-1}:J\to I\) is \(C^1\) and
   > \[
   >  (f^{-1})'(y)=\frac{1}{f'(f^{-1}(y))}
   >  \qquad\text{for every }y\in J.
   > \]

376. () `thm:differentiability-and-one-sided-derivatives` — **Differentiability and One-Sided Derivatives**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval and let $f : I \to \mathbb{R}$. Then $f$ is differentiable at $c \in I$ if and only if both one-sided derivatives $f'_-(c)$ and $f'_+(c)$ exist and are equal. In that case,
   > \[
   > f'(c) = f'_-(c) = f'_+(c).
   > \]

377. () `thm:interior-extremum-theorem` — **Interior Extremum Theorem**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$.
   > If $f$ has a relative extremum at $c$ and $f$ is differentiable at $c$, then
   > \[
   > f'(c) = 0.
   > \]

378. () `thm:rolles-theorem` — **Rolle's Theorem**
   > **Statement.**
   > Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $f(a) = f(b)$. Then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = 0.
   > \]

379. () `thm:mean-value-theorem` — **Mean Value Theorem**
   > **Statement.**
   > Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = \frac{f(b) - f(a)}{b - a}.
   > \]

380. () `thm:nondecreasing-iff-nonneg-derivative` — **Nondecreasing Iff Nonnegative Derivative**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nondecreasing on $I$ if and only if
   > \[
   > f'(x) \geq 0 \qquad \text{for all } x \in I.
   > \]

381. () `thm:inverse-function-theorem-one-variable` — **Inverse Function Theorem, One Variable**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an open interval, let \(f:I\to\mathbb{R}\) be of class \(C^1\), and let \(c\in I\) satisfy \(f'(c)\neq 0\). Then there exist open intervals \(U\subseteq I\) and \(V\subseteq\mathbb{R}\), with \(c\in U\) and \(f(c)\in V\), such that:
   > - \(f|_U:U\to V\) is a bijection;
   > - the inverse \(g=(f|_U)^{-1}:V\to U\) is of class \(C^1\);
   > - for every \(y\in V\),
   >  \[
   >  g'(y)=\frac{1}{f'(g(y))}.
   >  \]

382. () `thm:cauchy-mean-value-theorem` — **Cauchy Mean Value Theorem**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ with $a<b$. Suppose that $f,g:[a,b]\to\mathbb{R}$ are continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists $c\in(a,b)$ such that
   > \[
   >  \bigl(f(b)-f(a)\bigr)g'(c)
   >  =
   >  \bigl(g(b)-g(a)\bigr)f'(c).
   > \]
   > If, in addition, $g'(x)\neq 0$ for every $x\in(a,b)$, then $g(b)\neq g(a)$ and
   > \[
   >  \frac{f'(c)}{g'(c)}
   >  =
   >  \frac{f(b)-f(a)}{g(b)-g(a)}.
   > \]

383. () `thm:lhopital-zero-over-zero` — **L'H\^{o}pital's Rule, \(0/0\) Form**
   > **Statement.**
   > Let \(a<b\), and let \(f,g:(a,b)\to\mathbb{R}\) be differentiable with \(g'(x)\neq 0\) for every \(x\in(a,b)\). Suppose
   > \[
   >  \lim_{x\to a^+}f(x)=\lim_{x\to a^+}g(x)=0
   >  \qquad\text{and}\qquad
   >  \lim_{x\to a^+}\frac{f'(x)}{g'(x)}=L
   > \]
   > for \(L\in\mathbb{R}\cup\{-\infty,+\infty\}\). Then
   > \[
   >  \lim_{x\to a^+}\frac{f(x)}{g(x)}=L.
   > \]
   > The analogous statements at left-hand endpoints, at two-sided interior points, and at infinity follow by the same reductions.

384. () `thm:lhopital-infinity-over-infinity` — **L'H\^{o}pital's Rule, \(\infty/\infty\) Form**
   > **Statement.**
   > Let \(a<b\), and let \(f,g:(a,b)\to\mathbb{R}\) be differentiable with \(g'(x)\neq 0\) for every \(x\in(a,b)\). Suppose
   > \[
   >  \lim_{x\to a^+}|g(x)|=+\infty
   >  \qquad\text{and}\qquad
   >  \lim_{x\to a^+}\frac{f'(x)}{g'(x)}=L
   > \]
   > for \(L\in\mathbb{R}\cup\{-\infty,+\infty\}\). Then
   > \[
   >  \lim_{x\to a^+}\frac{f(x)}{g(x)}=L.
   > \]
   > No separate hypothesis on \(\lim_{x\to a^+}f(x)\) is required.

385. () `thm:leibniz-rule` — **Leibniz Rule**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval, let \(x\in I\), and suppose
   > that \(f,g:I\to\mathbb{R}\) are \(n\)-times differentiable on a
   > neighbourhood of \(x\). Then \(fg\) is \(n\)-times differentiable at \(x\),
   > and
   > \[
   >  (fg)^{(n)}(x)
   >  =
   >  \sum_{k=0}^{n}\binom{n}{k}f^{(k)}(x)g^{(n-k)}(x).
   > \]

386. () `thm:faa-di-bruno` — **Faa di Bruno's Formula**
   > **Statement.**
   > Let \(I,J\subseteq\mathbb{R}\) be intervals, let \(x\in I\), suppose
   > \(g:I\to J\) is \(n\)-times differentiable on a neighbourhood of \(x\), and
   > suppose \(f:J\to\mathbb{R}\) is \(n\)-times differentiable on a neighbourhood
   > of \(g(x)\). Then \(f\circ g\) is \(n\)-times differentiable at \(x\), and
   > \[
   >  \frac{d^n}{dx^n}f(g(x))
   >  =
   >  \sum_{\sum_{m=1}^{n}mk_m=n}
   >  \frac{n!}{\prod_{m=1}^{n}k_m!\,(m!)^{k_m}}\,
   >  f^{(k)}(g(x))
   >  \prod_{m=1}^{n}\bigl(g^{(m)}(x)\bigr)^{k_m},
   > \]
   > where \(k_m\geq0\) and \(k=\sum_{m=1}^{n}k_m\).

387. () `thm:derivative-equivalence` — **Equivalence of Definitions of the Derivative at a Point**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and $c \in A$ be a limit point of $A$. The following are equivalent:
   > - $f$ is differentiable at $c$ in the $\varepsilon$-$\delta$ sense with derivative $L$.
   > - $f$ is differentiable at $c$ in the topological sense with derivative $L$.
   > - $f$ is differentiable at $c$ in the sequential sense with derivative $L$.

388. () `prop:derivative-h-form-equivalence` — **Derivative: $h$-Form Equivalence**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and $c \in \operatorname{int}(A)$. Then $f$ is differentiable at $c$ with derivative $L$ if and only if
   > \[
   > \lim_{h \to 0} \frac{f(c+h) - f(c)}{h} = L.
   > \]

389. () `thm:uniqueness-of-the-derivative` — **Uniqueness of the Derivative**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and $c \in A$. If $f$ is differentiable at $c$, its derivative is unique.

390. () `prop:derivative-of-the-identity` — **Derivative of the Identity**
   > **Statement.**
   > Let $f(x) = x$ for all $x \in \mathbb{R}$. Then $f'(c) = 1$ for every $c \in \mathbb{R}$.

391. () `prop:derivative-of-a-constant` — **Derivative of a Constant**
   > **Statement.**
   > Let $k\in\mathbb{R}$ and let $f(x)=k$ for all $x\in\mathbb{R}$. Then $f'(c)=0$ for every $c\in\mathbb{R}$.

392. () `thm:necessary-condition-extremum` — **Necessary Condition for an Interior Extremum**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then either $f'(c)$ does not exist, or
   > \[
   > f'(c) = 0.
   > \]

393. () `cor:relative-extremum-necessary-condition` — **Necessary Condition for an Extremum**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then
   > \[
   > f'(c) = 0 \quad \text{or} \quad f'(c) \text{ does not exist.}
   > \]

394. () `thm:darboux` — **Darboux's Theorem**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$ and let $f : I \to \mathbb{R}$ be differentiable on $I$. If $k$ is a real number strictly between $f'(a)$ and $f'(b)$, then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = k.
   > \]

395. () `thm:second-derivative-convexity-test` — **Second-Derivative Convexity Test**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be twice differentiable on $I$. If
   > \[
   >  f''(x)\geq 0 \qquad \text{for all } x\in I,
   > \]
   > then $f$ is convex on $I$.

396. () `thm:second-derivative-concavity-test` — **Second-Derivative Concavity Test**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be twice differentiable on $I$. If
   > \[
   >  f''(x)\leq 0 \qquad \text{for all } x\in I,
   > \]
   > then $f$ is concave on $I$.

397. () `thm:second-derivative-test` — **Second Derivative Test**
   > **Statement.**
   > Let $f$ be twice differentiable in a neighbourhood of $c$, and suppose $f'(c)=0$.
   > - If $f''(c)>0$, then $f$ has a strict relative minimum at $c$.
   > - If $f''(c)<0$, then $f$ has a strict relative maximum at $c$.

398. () `prop:inflection-point-necessary-condition` — **Inflection Point Necessary Condition**
   > **Statement.**
   > Let $f$ have an inflection point at $c$. If $f''$ exists on a neighbourhood of $c$ and is continuous at $c$, then
   > \[
   >  f''(c)=0.
   > \]

399. () `thm:smoothness-tower` — **The Smoothness Tower**
   > **Statement.**
   > For every nondegenerate interval \(I\), the inclusions
   > \[
   >  C^0(I)\supseteq C^1(I)\supseteq C^2(I)\supseteq \cdots
   >  \supseteq C^\infty(I)\supseteq C^\omega(I)
   > \]
   > hold, and each displayed inclusion is strict.

400. () `cor:derivative-bound-implies-lipschitz` — **Derivative Bound Implies Lipschitz**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval and let \(f:I\to\mathbb{R}\) be differentiable on \(I\). If there exists \(M\geq 0\) such that
   > \[
   >  |f'(x)|\leq M
   >  \qquad\text{for every }x\in I,
   > \]
   > then \(f\) is Lipschitz on \(I\) with constant \(M\):
   > \[
   >  |f(x)-f(y)|\leq M|x-y|
   >  \qquad\text{for every }x,y\in I.
   > \]

401. () `thm:c11-placement` — **Placement of \(C^{1,1}\)**
   > **Statement.**
   > For every nondegenerate interval \(I\),
   > \[
   >  C^{1,1}(I)\subsetneq C^1(I),
   > \]
   > and \(C^{1,1}(I)\) is not contained in \(C^2(I)\). If \(K\) is a compact
   > interval, then
   > \[
   >  C^2(K)\subseteq C^{1,1}(K)\subsetneq C^1(K),
   > \]
   > and the first inclusion is strict.

402. () `cor:bounded-second-derivative-implies-c11` — **Bounded Second Derivative Implies \(C^{1,1}\)**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval and let \(f\in C^2(I)\). If
   > \(|f''(x)|\leq M\) for all \(x\in I\), then \(f\in C^{1,1}(I)\), and \(f'\)
   > is Lipschitz with constant \(M\).

403. () `thm:zero-derivative-implies-constant` — **Zero Derivative Implies Constant**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$ be a closed interval, and let $f : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If
   > \[
   > f'(x) = 0 \qquad \text{for all } x \in (a,b),
   > \]
   > then $f$ is constant on $I$.

404. () `cor:equal-derivatives-constant-difference` — **Equal Derivatives Imply Difference Is Constant**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$, and let $f, g : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If
   > \[
   > f'(x) = g'(x) \qquad \text{for all } x \in (a,b),
   > \]
   > then there exists $C \in \mathbb{R}$ such that $f(x) = g(x) + C$ for all $x \in I$.

405. () `thm:nonincreasing-iff-nonpos-derivative` — **Nonincreasing Iff Nonpositive Derivative**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nonincreasing on $I$ if and only if
   > \[
   > f'(x) \leq 0 \qquad \text{for all } x \in I.
   > \]

406. () `lem:positive-derivative-implies-locally-increasing` — **Positive Derivative Implies Locally Increasing**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose that $f$ is differentiable at $c$. If $f'(c) > 0$, then there exists $\delta > 0$ such that
   > \[
   > f(x) < f(c) \quad \text{for all } x \in I \text{ with } c - \delta < x < c,
   > \]
   > and
   > \[
   > f(x) > f(c) \quad \text{for all } x \in I \text{ with } c < x < c + \delta.
   > \]

407. () `lem:negative-derivative-implies-locally-decreasing` — **Negative Derivative Implies Locally Decreasing**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose that $f$ is differentiable at $c$. If $f'(c) < 0$, then there exists $\delta > 0$ such that
   > \[
   > f(x) > f(c) \quad \text{for all } x \in I \text{ with } c - \delta < x < c,
   > \]
   > and
   > \[
   > f(x) < f(c) \quad \text{for all } x \in I \text{ with } c < x < c + \delta.
   > \]

408. () `thm:first-derivative-test-maximum` — **First Derivative Test: Relative Maximum**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$. Suppose $f$ is differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ such that $(c-\delta,c+\delta) \subseteq I$ and
   > \[
   > f'(x) \geq 0 \quad \text{for all } x \in (c-\delta,c),
   > \qquad
   > f'(x) \leq 0 \quad \text{for all } x \in (c,c+\delta),
   > \]
   > then $f$ has a relative maximum at $c$.

409. () `thm:first-derivative-test-minimum` — **First Derivative Test: Relative Minimum**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$. Suppose $f$ is differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ such that $(c-\delta,c+\delta) \subseteq I$ and
   > \[
   > f'(x) \leq 0 \quad \text{for all } x \in (c-\delta,c),
   > \qquad
   > f'(x) \geq 0 \quad \text{for all } x \in (c,c+\delta),
   > \]
   > then $f$ has a relative minimum at $c$.

410. () `thm:differential-and-derivative-agree` — **Differential and Derivative Agree**
   > **Statement.**
   > Let $f$ be defined on a neighbourhood of $c\in\mathbb{R}$. Then $f$ is differentiable at $c$ in the ordinary derivative sense if and only if it is differentiable at $c$ in the differential sense. When this holds,
   > \[
   >  df_c(h)=f'(c)h.
   > \]

411. () `thm:uniqueness-of-the-differential` — **Uniqueness of the Differential**
   > **Statement.**
   > If $L_1,L_2:\mathbb{R}\to\mathbb{R}$ are linear maps and
   > \[
   >  f(c+h)-f(c)=L_1(h)+o(h)=L_2(h)+o(h)
   >  \qquad\text{as } h\to 0,
   > \]
   > then $L_1=L_2$.

412. () `thm:differential-continuity-criterion` — **Differential Continuity Criterion**
   > **Statement.**
   > If $f$ is differentiable at $c$ in the differential sense, then $f$ is continuous at $c$.

413. () `thm:chain-rule-for-differentials` — **Chain Rule for Differentials**
   > **Statement.**
   > If $f$ is differentiable at $c$ and $g$ is differentiable at $f(c)$, then
   > \[
   >  d(g\circ f)_c=dg_{f(c)}\circ df_c.
   > \]

414. () `thm:linearity-of-the-differential` — **Linearity of the Differential**
   > **Statement.**
   > If $f$ and $g$ are differentiable at $c$ and $\alpha,\beta\in\mathbb{R}$, then
   > \[
   >  d(\alpha f+\beta g)_c=\alpha\,df_c+\beta\,dg_c.
   > \]

415. () `thm:taylor-theorem-lagrange-remainder` — **Taylor's Theorem with Lagrange Remainder**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ with $a<b$, let $n\in\mathbb{N}$, and let
   > $f:[a,b]\to\mathbb{R}$. Suppose that $f,f',\ldots,f^{(n)}$ are continuous
   > on $[a,b]$ and that $f^{(n+1)}$ exists on $(a,b)$. Then, for every
   > $x\in(a,b)$, there exists $c$ strictly between $a$ and $x$ such that
   > \[
   >  f(x)
   >  =
   >  \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
   >  +
   >  \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
   > \]

416. () `cor:taylor-expansion-peano-remainder` — **Taylor Expansion with Peano Remainder**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval, let $a\in I$, let
   > $n\in\mathbb{N}$, and let $f:I\to\mathbb{R}$ have derivatives up to order
   > $n$ in a neighbourhood of $a$. If $f^{(n)}$ is continuous at $a$, then
   > \[
   >  f(x)
   >  =
   >  \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
   >  +
   >  o\bigl((x-a)^n\bigr)
   >  \qquad\text{as }x\to a.
   > \]

417. () `cor:first-order-peano-remainder` — **First-Order Peano Remainder**
   > **Statement.**
   > Let $f$ be differentiable at $c$. Then, as $h\to 0$,
   > \[
   >  f(c+h)=f(c)+f'(c)h+o(h).
   > \]

418. () `prop:flat-function` — **The Flat Function: Smooth but Not Analytic**
   > **Statement.**
   > Define \(f:\mathbb{R}\to\mathbb{R}\) by
   > \[
   >  f(x)=
   >  \begin{cases}
   >  e^{-1/x^2}, & x\neq 0,\\
   >  0, & x=0.
   >  \end{cases}
   > \]
   > Then:
   > - \(f\in C^\infty(\mathbb{R})\);
   > - \(f^{(n)}(0)=0\) for every \(n\geq 0\);
   > - the Maclaurin series of \(f\) is identically \(0\), so \(f\notin C^\omega\) on any neighbourhood of \(0\).
   > In particular, \(C^\infty(\mathbb{R})\setminus C^\omega(\mathbb{R})\neq\varnothing\).

419. () `prop:cauchy-integral-constant` — **Cauchy Integral of a Constant**
   > **Statement.**
   > If \(f(x)=c\) on \([a,b]\), then \(\int_a^b c\,dx=c(b-a)\).

420. () `thm:cauchy-integral-linearity` — **Linearity of the Cauchy Integral**
   > **Statement.**
   > If \(f\) and \(g\) are Cauchy-integrable on \([a,b]\), then
   > \[
   >  \int_a^b(\alpha f+\beta g)\,dx
   >  =
   >  \alpha\int_a^b f\,dx+\beta\int_a^b g\,dx.
   > \]

421. () `thm:cauchy-integral-monotonicity` — **Monotonicity of the Cauchy Integral**
   > **Statement.**
   > If \(f\) and \(g\) are Cauchy-integrable on \([a,b]\) and \(f(x)\le g(x)\)
   > for every \(x\in[a,b]\), then
   > \[
   >  \int_a^b f\,dx\le \int_a^b g\,dx .
   > \]

422. () `cor:cauchy-integral-bounds` — **Bounds for the Cauchy Integral**
   > **Statement.**
   > If \(f\) is continuous on \([a,b]\), \(m=\min_{[a,b]}f\), and
   > \(M=\max_{[a,b]}f\), then
   > \[
   >  m(b-a)\le \int_a^b f\,dx\le M(b-a).
   > \]

423. () `thm:cauchy-integral-triangle-inequality` — **Triangle Inequality for the Cauchy Integral**
   > **Statement.**
   > If \(f\) and \(|f|\) are Cauchy-integrable on \([a,b]\), then
   > \[
   >  \left|\int_a^b f\,dx\right|\le \int_a^b |f|\,dx .
   > \]

424. () `thm:cauchy-integral-interval-additivity` — **Interval Additivity for the Cauchy Integral**
   > **Statement.**
   > If \(c\in[a,b]\) and \(f\) is Cauchy-integrable on the relevant intervals,
   > then
   > \[
   >  \int_a^b f\,dx=\int_a^c f\,dx+\int_c^b f\,dx .
   > \]

425. () `thm:continuous-cauchy-integrable` — **Continuous Functions Are Cauchy-Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb R\) is Cauchy-integrable.

426. () `thm:cauchy-tag-independence` — **Tag Independence for Continuous Functions**
   > **Statement.**
   > If \(f\) is continuous on \([a,b]\), then every choice of tags gives the same
   > limit as the left-endpoint sums as \(\|P\|\to 0\).

427. () `lem:darboux-refinement-squeeze` — **Darboux Sums Under Refinement**
   > **Statement.**
   > If \(P'\) refines \(P\), then
   > \[
   >  L(f,P)\le L(f,P')\le U(f,P')\le U(f,P).
   > \]

428. () `thm:darboux-criterion` — **Darboux Criterion**
   > **Statement.**
   > A bounded function \(f\) is Darboux-integrable if and only if for every
   > \(\varepsilon>0\) there exists a partition \(P\) such that
   > \[
   >  U(f,P)-L(f,P)<\varepsilon.
   > \]

429. () `thm:riemann-darboux-equivalence` — **Equivalence of Riemann and Darboux Integrability**
   > **Statement.**
   > For bounded functions on \([a,b]\), Riemann integrability and Darboux
   > integrability are equivalent, and the integral values agree.

430. () `thm:continuous-darboux-integrable` — **Continuous Functions Are Darboux-Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb R\) is Darboux-integrable.

431. () `thm:monotone-darboux-integrable` — **Monotone Functions Are Darboux-Integrable**
   > **Statement.**
   > Every monotone function \(f:[a,b]\to\mathbb R\) is Darboux-integrable.

432. () `thm:finite-discontinuities-darboux-integrable` — **Bounded Functions with Finitely Many Discontinuities Are Darboux-Integrable**
   > **Statement.**
   > If \(f:[a,b]\to\mathbb R\) is bounded and has only finitely many
   > discontinuities, then \(f\) is Darboux-integrable.

433. () `thm:darboux-integrable-linear-combinations` — **Sums and Scalar Multiples of Darboux-Integrable Functions**
   > **Statement.**
   > If \(f\) and \(g\) are Darboux-integrable on \([a,b]\), then
   > \(\alpha f+\beta g\) is Darboux-integrable for all
   > \(\alpha,\beta\in\mathbb R\).

434. () `thm:darboux-integrable-products` — **Products of Darboux-Integrable Functions**
   > **Statement.**
   > If \(f\) and \(g\) are Darboux-integrable on \([a,b]\), then \(fg\) is
   > Darboux-integrable on \([a,b]\).

435. () `thm:darboux-integrable-absolute-value` — **Absolute Values of Darboux-Integrable Functions**
   > **Statement.**
   > If \(f\) is Darboux-integrable on \([a,b]\), then \(|f|\) is
   > Darboux-integrable on \([a,b]\).

436. () `thm:darboux-integrable-continuous-composition` — **Continuous Images of Darboux-Integrable Functions**
   > **Statement.**
   > If \(f\) is Darboux-integrable on \([a,b]\), \(\varphi\) is continuous on an
   > interval containing \(f([a,b])\), and \(f\) is bounded, then
   > \(\varphi\circ f\) is Darboux-integrable on \([a,b]\).

437. () `lem:cousin` — **Cousin's Lemma**
   > **Statement.**
   > For every gauge \(\delta\) on \([a,b]\), there exists a \(\delta\)-fine tagged
   > partition of \([a,b]\).

438. () `thm:riemann-integrable-implies-hk-integrable` — **Riemann Integrable Implies Henstock--Kurzweil Integrable**
   > **Statement.**
   > If \(f\) is Riemann-integrable on \([a,b]\), then \(f\) is
   > Henstock--Kurzweil integrable on \([a,b]\), and the two integrals have the
   > same value.

439. () `lem:hk-straddle` — **Straddle Lemma**
   > **Statement.**
   > If \(F\) is differentiable at \(\xi\) with \(F'(\xi)=f(\xi)\), then for every
   > \(\varepsilon>0\) there is \(\delta(\xi)>0\) such that whenever
   > \(u\le \xi\le v\), \(u,v\in(\xi-\delta(\xi),\xi+\delta(\xi))\),
   > \[
   >  |F(v)-F(u)-f(\xi)(v-u)|\le \varepsilon(v-u).
   > \]

440. () `thm:hk-fundamental-theorem` — **Fundamental Theorem for the Henstock--Kurzweil Integral**
   > **Statement.**
   > If \(F:[a,b]\to\mathbb R\) is differentiable at every point and \(F'=f\), then
   > \(f\) is Henstock--Kurzweil integrable and
   > \[
   >  (\mathrm{HK})\int_a^b f=F(b)-F(a).
   > \]

441. () `thm:continuous-hk-integrable` — **Continuous Functions Are Henstock--Kurzweil Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb R\) is Henstock--Kurzweil
   > integrable.

442. () `thm:riemann-mcshane-hk-inclusions` — **Riemann Integrable Implies McShane Integrable Implies Henstock--Kurzweil Integrable**
   > **Statement.**
   > On a compact interval,
   > \[
   >  \mathcal R[a,b]\subseteq \mathcal M[a,b]\subseteq \mathcal{HK}[a,b],
   > \]
   > and the integral values agree whenever a function belongs to the smaller
   > class.

443. () `thm:mcshane-equals-lebesgue` — **McShane Integrability Equals Lebesgue Integrability**
   > **Statement.**
   > For real-valued functions on a compact interval,
   > \[
   >  \mathcal{McShane}[a,b]=\mathcal L[a,b],
   > \]
   > and the McShane and Lebesgue integral values agree.

444. () `thm:lebesgue-criterion-riemann-integrability` — **Lebesgue Criterion for Riemann Integrability**
   > **Statement.**
   > A bounded function \(f:[a,b]\to\mathbb R\) is Riemann-integrable if and only
   > if its discontinuity set
   > \[
   >  D=\{x\in[a,b]:\omega_f(x)>0\}
   > \]
   > has measure zero.

445. () `lem:common-refinement-partitions` — **Common Refinement of Two Partitions**
   > **Statement.**
   > Any two partitions \(P\) and \(P'\) of \([a,b]\) have a common refinement:
   > order the finite set \(P\cup P'\) increasingly.

446. () `thm:continuous-riemann-integrable` — **Continuous Functions Are Riemann-Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb R\) is Riemann-integrable.

447. () `thm:riemann-integral-linearity` — **Linearity of the Riemann Integral**
   > **Statement.**
   > If \(f\) and \(g\) are Riemann-integrable on \([a,b]\), then
   > \[
   >  \int_a^b(\alpha f+\beta g)\,dx
   >  =
   >  \alpha\int_a^b f\,dx+\beta\int_a^b g\,dx .
   > \]

448. () `thm:riemann-integral-monotonicity` — **Monotonicity of the Riemann Integral**
   > **Statement.**
   > If \(f\) and \(g\) are Riemann-integrable on \([a,b]\) and \(f(x)\le g(x)\)
   > for every \(x\in[a,b]\), then
   > \[
   >  \int_a^b f\,dx\le \int_a^b g\,dx .
   > \]

449. () `thm:riemann-integral-triangle-inequality` — **Triangle Inequality for the Riemann Integral**
   > **Statement.**
   > If \(f\) is Riemann-integrable on \([a,b]\), then \(|f|\) is
   > Riemann-integrable and
   > \[
   >  \left|\int_a^b f\,dx\right|\le \int_a^b |f|\,dx .
   > \]

450. () `thm:riemann-integral-interval-additivity` — **Interval Additivity for the Riemann Integral**
   > **Statement.**
   > If \(c\in[a,b]\), then \(f\) is Riemann-integrable on \([a,b]\) if and only if
   > it is Riemann-integrable on \([a,c]\) and \([c,b]\), and in that case
   > \[
   >  \int_a^b f\,dx=\int_a^c f\,dx+\int_c^b f\,dx .
   > \]

451. () `thm:riemann-cauchy-criterion` — **Cauchy Criterion for Riemann Integrability**
   > **Statement.**
   > A bounded function is Riemann-integrable if and only if for every
   > \(\varepsilon>0\) there is \(\delta>0\) such that any two tagged partitions
   > \((P,\xi)\) and \((Q,\eta)\) with \(\|P\|,\|Q\|<\delta\) have
   > \[
   >  |S(f,P,\xi)-S(f,Q,\eta)|<\varepsilon.
   > \]

452. () `prop:monotone-bounded-variation` — **Monotone Functions Have Bounded Variation**
   > **Statement.**
   > If \(\alpha\) is monotone on \([a,b]\), then \(\alpha\) has bounded variation.

453. () `thm:rs-continuous-bv-existence` — **Continuous Integrand and BV Integrator**
   > **Statement.**
   > If \(f\) is continuous on \([a,b]\) and \(\alpha\) has bounded variation, then
   > \(\int_a^b f\,d\alpha\) exists.

454. () `thm:rs-bilinearity` — **Bilinearity of the Riemann--Stieltjes Integral**
   > **Statement.**
   > Whenever the displayed integrals exist,
   > \[
   >  \int_a^b (\lambda f+\mu g)\,d\alpha
   >  =
   >  \lambda\int_a^b f\,d\alpha+\mu\int_a^b g\,d\alpha
   > \]
   > and
   > \[
   >  \int_a^b f\,d(\lambda\alpha+\mu\beta)
   >  =
   >  \lambda\int_a^b f\,d\alpha+\mu\int_a^b f\,d\beta .
   > \]

455. () `thm:rs-interval-additivity` — **Interval Additivity for the Riemann--Stieltjes Integral**
   > **Statement.**
   > If \(c\in[a,b]\) and the relevant Riemann--Stieltjes integrals exist, then
   > \[
   >  \int_a^b f\,d\alpha
   >  =
   >  \int_a^c f\,d\alpha+\int_c^b f\,d\alpha .
   > \]

456. () `thm:rs-integration-by-parts` — **Riemann--Stieltjes Integration by Parts**
   > **Statement.**
   > If \(f\) and \(\alpha\) are such that one of
   > \(\int_a^b f\,d\alpha\) and \(\int_a^b \alpha\,df\) exists, then the other
   > exists under the same Riemann--Stieltjes convention, and
   > \[
   >  \int_a^b f\,d\alpha+\int_a^b \alpha\,df
   >  =
   >  f(b)\alpha(b)-f(a)\alpha(a).
   > \]

457. () `thm:rs-c1-reduction` — **Reduction to Riemann Integration for a \(C^1\) Integrator**
   > **Statement.**
   > If \(\alpha\in C^1([a,b])\) and \(f\) is Riemann-integrable on \([a,b]\), then
   > \[
   >  \int_a^b f\,d\alpha=\int_a^b f(x)\alpha'(x)\,dx .
   > \]

458. () `thm:rs-step-integrator-finite-sum` — **Step Integrators Give Finite Sums**
   > **Statement.**
   > If \(\alpha\) is constant except for finitely many jumps at points \(c_k\) and
   > \(f\) is continuous at each \(c_k\), then
   > \[
   >  \int_a^b f\,d\alpha=\sum_k f(c_k)\,\Delta\alpha(c_k).
   > \]

459. () `lem:positive-product` — **Positive Product**
   > **Statement.**
   > If \(a,b\in\mathbb{R}\), \(a>0\), and \(b>0\), then \(ab>0\).

460. () `lem:negative-times-negative-is-positive` — **Negative Times Negative Is Positive**
   > **Statement.**
   > If \(a,b\in\mathbb{R}\), \(a<0\), and \(b<0\), then \(ab>0\).

461. () `lem:positive-times-negative-is-negative` — **Positive Times Negative Is Negative**
   > **Statement.**
   > If \(a,b\in\mathbb{R}\), \(a>0\), and \(b<0\), then \(ab<0\).

462. () `lem:negative-times-positive-is-negative` — **Negative Times Positive Is Negative**
   > **Statement.**
   > If \(a,b\in\mathbb{R}\), \(a<0\), and \(b>0\), then \(ab<0\).

463. () `lem:order-and-subtraction` — **Order and Subtraction**
   > **Statement.**
   > For \(a,b\in\mathbb{R}\), \(a<b \Longleftrightarrow b-a>0\).

464. () `lem:non-strict-order-and-subtraction` — **Non-Strict Order and Subtraction**
   > **Statement.**
   > For \(a,b\in\mathbb{R}\), \(a\le b \Longleftrightarrow b-a\ge 0\).

465. () `lem:division-by-positive-preserves-order` — **Division by Positive Preserves Order**
   > **Statement.**
   > If \(a,b,c\in\mathbb{R}\), \(a<b\), and \(c>0\), then \(\frac ac<\frac bc\).

466. () `lem:division-by-negative-reverses-order` — **Division by Negative Reverses Order**
   > **Statement.**
   > If \(a,b,c\in\mathbb{R}\), \(a<b\), and \(c<0\), then \(\frac bc<\frac ac\).

467. () `prop:supremum-need-not-belong-to-the-set` — **Supremum Need Not Belong to the Set**
   > **Statement.**
   > There exists a nonempty bounded above set \(A\subseteq\mathbb{R}\) such that
   > \[
   >  \sup A\notin A.
   > \]

468. () `prop:infimum-need-not-belong-to-the-set` — **Infimum Need Not Belong to the Set**
   > **Statement.**
   > There exists a nonempty bounded below set \(A\subseteq\mathbb{R}\) such that
   > \[
   >  \inf A\notin A.
   > \]

469. () `thm:no-immediate-successors-in-r` — **No Immediate Successors in \(\mathbb{R}\)**
   > **Statement.**
   > For every \(a\in\mathbb{R}\), there is no least real number greater than \(a\).

470. () `thm:no-immediate-predecessors-in-r` — **No Immediate Predecessors in \(\mathbb{R}\)**
   > **Statement.**
   > For every \(a\in\mathbb{R}\), there is no greatest real number less than \(a\).

471. () `thm:real-line-structural-order-facts` — **Real Line Structural Order Facts**
   > **Statement.**
   > The real numbers are linearly ordered, form an ordered field, and satisfy the
   > least upper bound property.
