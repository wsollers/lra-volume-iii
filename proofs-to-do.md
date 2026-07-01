# Volume III - Classical Analysis Proofs To Do

Proof-writing order is dependency-first among active proof labels. Dependency edges come from resolved statement and proof dependency blocks; original source order is the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 394
Completed in this tracker: 6
Unresolved dependency edges skipped for ordering: 4

1. () `thm:decreasing-image-infimum-to-supremum` — **Decreasing Image Sends Infimum to Supremum**
   > **Statement.**
   > If $f$ is decreasing and continuous at $\inf A$, then
   > $\sup f(A)=f(\inf A)$.

2. () `thm:decreasing-image-supremum-to-infimum` — **Decreasing Image Sends Supremum to Infimum**
   > **Statement.**
   > If $f$ is decreasing and continuous at $\sup A$, then
   > $\inf f(A)=f(\sup A)$.

3. () `thm:decreasing-inverse-infimum-to-supremum` — **Decreasing Inverse Sends Infimum to Supremum**
   > **Statement.**
   > If $f^{-1}$ is decreasing and continuous at $\inf B$, then
   > $\sup f^{-1}(B)=f^{-1}(\inf B)$.

4. () `thm:decreasing-inverse-supremum-to-infimum` — **Decreasing Inverse Sends Supremum to Infimum**
   > **Statement.**
   > If $f^{-1}$ is decreasing and continuous at $\sup B$, then
   > $\inf f^{-1}(B)=f^{-1}(\sup B)$.

5. (✅) `prop:every-element-lies-below-the-supremum` — **Every Element Lies Below the Supremum**
   > **Statement.**
   > If $s = \sup A$, then for every $x \in A$, $x \le s$.

6. () `thm:increasing-image-preserves-infima` — **Increasing Image Preserves Infima**
   > **Statement.**
   > If $f$ is increasing and continuous at $\inf A$, then
   > $\inf f(A)=f(\inf A)$.

7. () `thm:increasing-image-preserves-suprema` — **Increasing Image Preserves Suprema**
   > **Statement.**
   > If $f$ is increasing and continuous at $\sup A$, then
   > $\sup f(A)=f(\sup A)$.

8. () `thm:increasing-inverse-preserves-infima` — **Increasing Inverse Preserves Infima**
   > **Statement.**
   > If $f^{-1}$ is increasing and continuous at $\inf B$, then
   > $\inf f^{-1}(B)=f^{-1}(\inf B)$.

9. () `thm:increasing-inverse-preserves-suprema` — **Increasing Inverse Preserves Suprema**
   > **Statement.**
   > If $f^{-1}$ is increasing and continuous at $\sup B$, then
   > $\sup f^{-1}(B)=f^{-1}(\sup B)$.

10. (✅) `thm:infimum-less-than-supremum` — **Infimum-Supremum Comparison**
   > **Statement.**
   > For any non-empty bounded set $A \subseteq \mathbb{R}$, the infimum of $A$ is less than or equal to the supremum of $A$.

11. () `thm:infimum-pointwise-maximum-set` — **Infimum of the Pointwise Maximum Set**
   > **Statement.**
   > For nonempty bounded-below $A,B\subseteq\mathbb{R}$,
   > $\inf\max(A,B)=\max\{\inf A,\inf B\}$.

12. () `thm:infimum-pointwise-minimum-set` — **Infimum of the Pointwise Minimum Set**
   > **Statement.**
   > For nonempty bounded-below $A,B\subseteq\mathbb{R}$,
   > $\inf\min(A,B)=\min\{\inf A,\inf B\}$.

13. () `thm:infimum-sum-set` — **Infimum of a Sum Set**
   > **Statement.**
   > For nonempty bounded-below sets $A,B$, $\inf(A+B)=\inf A+\inf B$.

14. (✅) `prop:maximum-implies-supremum` — **Maximum Implies Supremum**
   > **Statement.**
   > If a set $A \subseteq \mathbb{R}$ has a maximum $m$, then $m$ is also the supremum of $A$.

15. (✅) `thm:negation-exchange-sup-inf` — **Negation Exchanges Supremum and Infimum**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ be a non-empty set. If $A$ is bounded below, then $\sup(-A) = -\inf A$.

16. () `prop:negative-dilation-sends-lower-to-upper-bounds` — **Negative Dilation Sends Lower Bounds to Upper Bounds**
   > **Statement.**
   > If $\lambda<0$ and $\ell$ is a lower bound of $A$, then $\lambda\ell$ is an
   > upper bound of $\lambda A$.

17. () `prop:negative-dilation-sends-upper-to-lower-bounds` — **Negative Dilation Sends Upper Bounds to Lower Bounds**
   > **Statement.**
   > If $\lambda<0$ and $u$ is an upper bound of $A$, then $\lambda u$ is a lower
   > bound of $\lambda A$.

18. () `thm:negative-scalar-mult-infimum` — **Negative Scalar Multiplication of the Infimum**
   > **Statement.**
   > If $k<0$ and $A$ is nonempty and bounded above, then $\inf(kA)=k\sup A$.

19. () `thm:infimum-difference-set` — **Infimum of a Difference Set**
   > **Statement.**
   > For nonempty $A,B$, with $A$ bounded below and $B$ bounded above,
   > $\inf(A-B)=\inf A-\sup B$.

20. () `prop:order-comparison-of-suprema` — **Order Comparison of Supremum**
   > **Statement.**
   > Let $A, B \subseteq \mathbb{R}$ be non-empty sets that are bounded above. If for every $x \in A$, there exists $y \in B$ such that $x \le y$, then $\sup A \le \sup B$.

21. () `prop:positive-dilation-preserves-lower-bounds` — **Positive Dilation Preserves Lower Bounds**
   > **Statement.**
   > If $\lambda>0$ and $\ell$ is a lower bound of $A$, then $\lambda\ell$ is a
   > lower bound of $\lambda A$.

22. () `prop:positive-dilation-preserves-upper-bounds` — **Positive Dilation Preserves Upper Bounds**
   > **Statement.**
   > If $\lambda>0$ and $u$ is an upper bound of $A$, then $\lambda u$ is an
   > upper bound of $\lambda A$.

23. () `thm:positive-scalar-mult-infimum` — **Positive Scalar Multiplication of the Infimum**
   > **Statement.**
   > If $k>0$ and $A$ is nonempty and bounded below, then $\inf(kA)=k\inf A$.

24. () `cor:reflection-swaps-upper-lower-bounds` — **Reflection Swaps Upper and Lower Bounds**
   > **Statement.**
   > If $\ell$ is a lower bound of $A$, then $-\ell$ is an upper bound of $-A$.
   > If $u$ is an upper bound of $A$, then $-u$ is a lower bound of $-A$.

25. () `lem:subset-inclusion-preserves-upper-bounds` — **Subset Inclusion Preserves Upper Bounds**
   > **Statement.**
   > Let $A \subseteq B \subseteq \mathbb{R}$. If $u$ is an upper bound of $B$, then $u$ is an upper bound of $A$.

26. () `lem:subsets-preserve-lower-bounds` — **Subsets Preserve Lower Bounds**
   > **Statement.**
   > If $C\subseteq A\subseteq\mathbb{R}$ and $\ell$ is a lower bound of $A$,
   > then $\ell$ is a lower bound of $C$.

27. () `lem:subsets-preserve-upper-bounds` — **Subsets Preserve Upper Bounds**
   > **Statement.**
   > If $C\subseteq A\subseteq\mathbb{R}$ and $u$ is an upper bound of $A$, then
   > $u$ is an upper bound of $C$.

28. () `cor:complements-inherit-ambient-bounds` — **Complements Inherit Ambient Bounds**
   > **Statement.**
   > For $A\subseteq E\subseteq\mathbb{R}$, every upper bound of $E$ is an upper
   > bound of $E\setminus A$, and every lower bound of $E$ is a lower bound of
   > $E\setminus A$.

29. () `cor:differences-inherit-bounds` — **Differences Inherit Bounds**
   > **Statement.**
   > Every upper bound of $A$ is an upper bound of $A\setminus B$, and every lower
   > bound of $A$ is a lower bound of $A\setminus B$.

30. () `cor:intersections-inherit-bounds` — **Intersections Inherit Bounds**
   > **Statement.**
   > Every upper bound of $A$ is an upper bound of $A\cap B$, and every lower
   > bound of $A$ is a lower bound of $A\cap B$.

31. () `prop:suprema-ambient-set` — **Suprema Depend on the Ambient Set**
   > **Statement.**
   > Let $A\subseteq S\subseteq S'$ be subsets of an ordered set. The supremum of $A$ relative to $S$, if it exists, need not agree with the supremum of $A$ relative to $S'$.

32. () `thm:ambient-existence-supremum` — **Ambient Existence of Supremum**
   > **Statement.**
   > There are ordered sets $S\subseteq S'$ and a subset $A\subseteq S$ such that $A$ has a supremum relative to $S'$ but has no supremum relative to $S$.

33. () `lem:rational-gap-suprema` — **Rational Gap Example for Suprema**
   > **Statement.**
   > Let
   > \[
   >   A=\{q\in\mathbb{Q}:q^2<2\}.
   > \]
   > Then $A$ is nonempty and bounded above in $\mathbb{Q}$, but $A$ has no supremum relative to $\mathbb{Q}$.

34. () `thm:supremum-absolute-value-image` — **Supremum of the Absolute-Value Image**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >   \sup |A|=\max\{|\sup A|,|\inf A|\},
   >   \qquad
   >   |A|=\{|a|:a\in A\}.
   > \]

35. () `prop:supremum-in-the-set-is-the-maximum` — **Supremum in the Set Is the Maximum**
   > **Statement.**
   > Let $s = \sup A$. If $s \in A$, then $s$ is the maximum of $A$.

36. () `thm:supremum-is-monotone-under-inclusion` — **Supremum Is Monotone Under Inclusion**
   > **Statement.**
   > Let $A$ and $B$ be non-empty subsets of $\mathbb{R}$ that are bounded above. If $A \subseteq B$, then $\sup A \le \sup B$.

37. () `thm:supremum-pointwise-maximum-set` — **Supremum of the Pointwise Maximum Set**
   > **Statement.**
   > For nonempty bounded-above $A,B\subseteq\mathbb{R}$,
   > $\sup\max(A,B)=\max\{\sup A,\sup B\}$.

38. () `thm:supremum-pointwise-minimum-set` — **Supremum of the Pointwise Minimum Set**
   > **Statement.**
   > For nonempty bounded-above $A,B\subseteq\mathbb{R}$,
   > $\sup\min(A,B)=\min\{\sup A,\sup B\}$.

39. () `thm:supremum-product-set` — **Supremum of a Product Set**
   > **Statement.**
   > For nonempty bounded $A,B$, $\sup(AB)$ is the maximum of the four endpoint
   > products.

40. () `thm:infimum-product-set` — **Infimum of a Product Set**
   > **Statement.**
   > For nonempty bounded $A,B$, $\inf(AB)$ is the minimum of the four endpoint
   > products.

41. () `thm:supremum-reciprocal-set` — **Supremum of a Reciprocal Set**
   > **Statement.**
   > For a nonempty bounded set separated from zero,
   > \[
   >   \sup(A^{-1})=(\inf A)^{-1}.
   > \]

42. () `thm:infimum-reciprocal-set` — **Infimum of a Reciprocal Set**
   > **Statement.**
   > For a nonempty bounded set separated from zero,
   > \[
   >   \inf(A^{-1})=(\sup A)^{-1}.
   > \]

43. () `thm:infimum-quotient-set` — **Infimum of a Quotient Set**
   > **Statement.**
   > If $A,B$ are nonempty and bounded and $B$ is separated from zero, then
   > $\inf(A/B)$ is the minimum of the four endpoint quotients.

44. () `thm:supremum-quotient-set` — **Supremum of a Quotient Set**
   > **Statement.**
   > If $A,B$ are nonempty and bounded and $B$ is separated from zero, then
   > $\sup(A/B)$ is the maximum of the four endpoint quotients.

45. () `thm:supremum-sum-set` — **Supremum of a Sum Set**
   > **Statement.**
   > Let $A, B \subseteq \mathbb{R}$ be non-empty sets bounded above. Define $A + B = \{a + b : a \in A, b \in B\}$. Then $\sup(A + B) = \sup A + \sup B$.

46. () `prop:bounds-sum-set` — **Bounds for Suprema and Infima Under Set Addition**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >   \inf A+\inf B\le \inf(A+B)
   >   \qquad\text{and}\qquad
   >   \sup(A+B)\le \sup A+\sup B.
   > \]

47. () `thm:supremum-difference-set` — **Supremum of a Difference Set**
   > **Statement.**
   > Let $A,B\subseteq\mathbb{R}$ be nonempty, with $A$ bounded above and $B$ bounded below. Then
   > \[
   >   \sup(A-B)=\sup A-\inf B,
   >   \qquad
   >   A-B=\{a-b:a\in A,\ b\in B\}.
   > \]

48. () `thm:translation-invariance-infimum` — **Translation Invariance of the Infimum**
   > **Statement.**
   > For nonempty $A$ bounded below, $\inf(A+c)=\inf A+c$.

49. () `thm:translation-invariance-supremum` — **Translation Invariance of the Supremum**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $c\in\mathbb{R}$. Then
   > \[
   >   \sup(A+c)=\sup A+c,
   >   \qquad
   >   A+c=\{a+c:a\in A\}.
   > \]

50. () `prop:translation-preserves-lower-bounds` — **Translation Preserves Lower Bounds**
   > **Statement.**
   > If $\ell$ is a lower bound of $A$, then $\ell+c$ is a lower bound of $A+c$.

51. () `prop:translation-preserves-upper-bounds` — **Translation Preserves Upper Bounds**
   > **Statement.**
   > If $u$ is an upper bound of $A$, then $u+c$ is an upper bound of $A+c$.

52. () `lem:union-preserves-lower-bounds` — **Union Preserves Lower Bounds**
   > **Statement.**
   > If $\ell_A$ is a lower bound of $A$ and $\ell_B$ is a lower bound of $B$,
   > then $\min\{\ell_A,\ell_B\}$ is a lower bound of $A\cup B$.

53. () `prop:union-bounded-below-iff-pieces-bounded-below` — **Union Is Bounded Below Exactly When Both Pieces Are**
   > **Statement.**
   > For nonempty $A,B\subseteq\mathbb{R}$, $A\cup B$ is bounded below if and only
   > if $A$ and $B$ are bounded below.

54. () `lem:union-preserves-upper-bounds` — **Union Preserves Upper Bounds**
   > **Statement.**
   > If $u_A$ is an upper bound of $A$ and $u_B$ is an upper bound of $B$, then
   > $\max\{u_A,u_B\}$ is an upper bound of $A\cup B$.

55. () `prop:union-bounded-above-iff-pieces-bounded-above` — **Union Is Bounded Above Exactly When Both Pieces Are**
   > **Statement.**
   > For nonempty $A,B\subseteq\mathbb{R}$, $A\cup B$ is bounded above if and only
   > if $A$ and $B$ are bounded above.

56. () `cor:union-bounded-iff-pieces-bounded` — **Union Is Bounded Exactly When Both Pieces Are**
   > **Statement.**
   > For nonempty $A,B\subseteq\mathbb{R}$, $A\cup B$ is bounded if and only if
   > $A$ and $B$ are bounded.

57. () `prop:uniqueness-of-the-maximum` — **Uniqueness of the Maximum**
   > **Statement.**
   > If a set $A \subseteq \mathbb{R}$ has a maximum, then that maximum is unique.

58. () `prop:uniqueness-of-the-supremum` — **Uniqueness of the Supremum**
   > **Statement.**
   > If a set $A \subseteq \mathbb{R}$ has a supremum, then that supremum is unique.

59. () `prop:upper-bound-comparison-with-the-supremum` — **Upper Bound Comparison with the Supremum**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ be non-empty and bounded above, and let $s = \sup A$. For any $u \in \mathbb{R}$, $u$ is an upper bound of $A$ if and only if $s \le u$.

60. (✅) `thm:scalar-mult-positive` — **Scalar Multiplication by a Positive Scalar**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $k>0$. Then
   > \[
   >   \sup(kA)=k\sup A,
   >   \qquad
   >   kA=\{ka:a\in A\}.
   > \]

61. (✅) `thm:scalar-mult-negative` — **Scalar Multiplication by a Negative Scalar**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let $k<0$. Then
   > \[
   >   \sup(kA)=k\inf A,
   >   \qquad
   >   kA=\{ka:a\in A\}.
   > \]

62. () `thm:supremum-dilation` — **Supremum of a Dilation**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ be nonempty and bounded, and let $\lambda\in\mathbb{R}$. Then
   > \[
   >   \sup(\lambda A)=\max\{\lambda\sup A,\lambda\inf A\},
   >   \qquad
   >   \lambda A=\{\lambda a:a\in A\}.
   > \]

63. () `prop:upper-bounds-ambient-order` — **Upper Bounds Depend on the Ambient Order**
   > **Statement.**
   > Let $(S,\le_S)$ and $(T,\le_T)$ be ordered sets, and let $A\subseteq S\cap T$. Whether $u$ is an upper bound of $A$ must be interpreted relative to the chosen ambient order.

64. () `prop:every-element-lies-above-the-infimum` — **Every Element Lies Above the Infimum**
   > **Statement.**
   > If i is the infimum of A, then every element of A lies above i.

65. () `thm:glb-property-implies-existence-of-infima` — **Greatest Lower Bound Property Implies Existence of Infima**
   > **Statement.**
   > Every nonempty subset of R that is bounded below has an infimum in R.

66. () `prop:infimum-in-the-set-is-the-minimum` — **Infimum in the Set is the Minimum**
   > **Statement.**
   > If the infimum of a nonempty set belongs to the set, then it is the minimum.

67. () `thm:infimum-is-monotone-under-inclusion` — **Infimum Is Monotone Under Inclusion**
   > **Statement.**
   > If A is a subset of B and both infima exist, then inf B is less than or equal to inf A.

68. () `prop:lower-bound-comparison-with-the-infimum` — **Lower Bound Comparison with the Infimum**
   > **Statement.**
   > For a nonempty set with infimum i, lower bounds are exactly the numbers less than or equal to i.

69. () `prop:lower-bound-property-of-infimum` — **Lower Bound Property of the Infimum**
   > **Statement.**
   > If i is the infimum of A, then i is a lower bound of A.

70. () `thm:lub-property-implies-existence-of-suprema` — **Least Upper Bound Property Implies Existence of Suprema**
   > **Statement.**
   > Let $S$ be a partially ordered set. If $S$ has the Least Upper Bound Property, then every nonempty subset of $S$ that is bounded above in $S$ has a supremum in $S$.

71. () `prop:minimum-implies-infimum` — **Minimum Implies Infimum**
   > **Statement.**
   > If a nonempty ordered set has a minimum, then that minimum is its infimum.

72. () `lem:subset-inclusion-preserves-lower-bounds` — **Subset Inclusion Preserves Lower Bounds**
   > **Statement.**
   > If A is a subset of B and ell is a lower bound of B, then ell is a lower bound of A.

73. () `prop:uniqueness-of-the-infimum` — **Uniqueness of the Infimum**
   > **Statement.**
   > If a set has an infimum, then that infimum is unique.

74. () `prop:uniqueness-of-the-minimum` — **Uniqueness of the Minimum**
   > **Statement.**
   > If a set has a minimum, then that minimum is unique.

75. () `prop:upper-bound-property-of-supremum` — **Upper Bound Property of Supremum**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ and let $s \in \mathbb{R}$. If $s=\sup A$, then
   > \[
   > x \le s
   > \qquad \text{for every } x \in A.
   > \]

76. () `thm:archimedean-property` — **Archimedean Property**
   > **Statement.**
   > For every $x \in \mathbb{R}$, there exists $n \in \mathbb{N}$ such that $n > x$.

77. () `cor:archimedean-reciprocal` — **Archimedean Corollary**
   > **Statement.**
   > For every $\varepsilon \in \mathbb{R}$ such that $\varepsilon > 0$, there exists $n \in \mathbb{N}$ such that $\frac{1}{n} < \varepsilon$.

78. () `thm:density-of-rationals-in-reals` — **Density of the Rational Numbers in $R$**
   > **Statement.**
   > For every $a,b\in\mathbb{R}$ with $a<b$, there exists $q\in\mathbb{Q}$ such that $a<q<b$.

79. () `thm:density-of-irrationals-in-reals` — **Density of the Irrational Numbers in $R$**
   > **Statement.**
   > For every $a,b\in\mathbb{R}$ with $a<b$, there exists $s\in\mathbb{R}\setminus\mathbb{Q}$ such that $a<s<b$.

80. () `cor:every-open-interval-contains-rational-and-irrational` — **Rational and Irrational Points in Every Open Interval**
   > **Statement.**
   > Every open interval in $\mathbb{R}$ contains both a rational number and an irrational number.

81. () `thm:nested-interval-theorem` — **Nested Interval Theorem**
   > **Statement.**
   > Let $I_n = [a_n, b_n]$ be a sequence of non-empty closed bounded intervals such that $I_{n+1} \subseteq I_n$. Then $\bigcap_{n=1}^\infty I_n \neq \varnothing$.

82. () `prop:delta-constant` — **Constant rule**
   > **Statement.**
   > The forward difference of a constant sequence is zero.

83. () `prop:delta-linearity` — **Linearity of \(\Delta\)**
   > **Statement.**
   > The forward difference operator is linear.

84. () `thm:delta-shift-minus-identity` — **\(\Delta = E-I\)**
   > **Statement.**
   > The forward difference operator is the shift operator minus the identity
   > operator.

85. () `prop:constant-of-integration` — **Constant of integration**
   > **Statement.**
   > Discrete antiderivatives are unique up to an additive constant.

86. () `thm:binomial-theorem` — **Binomial Theorem**
   > **Statement.**
   > For any integer \(n \ge 0\) and real numbers \(x,y\),
   > \[
   > (x+y)^n
   > =
   > \sum_{k=0}^{n} \binom{n}{k} x^{\,n-k} y^{\,k}.
   > \]

87. () `thm:polynomial-detection` — **Polynomial detection**
   > **Statement.**
   > Finite differences detect polynomial degree.

88. () `prop:higher-diff-formula` — **Higher difference formula**
   > **Statement.**
   > For any function \(f\),
   > \[
   > \Delta^n f(x)
   > =
   > \sum_{k=0}^{n} (-1)^{\,n-k}
   > \binom{n}{k}
   > f(x+k).
   > \]

89. () `prop:discrete-exponential-rule` — **Discrete exponential rule**
   > **Statement.**
   > The discrete exponential has geometric forward differences.

90. () `prop:discrete-ivp` — **Discrete IVP**
   > **Statement.**
   > A first-order discrete initial value problem has the stated solution.

91. () `prop:higher-diff-two-n` — **Higher differences of \(2^n\)**
   > **Statement.**
   > All higher forward differences of \(2^n\) are again \(2^n\).

92. () `cor:composition-bijective` — **Composition of Bijections Is Bijective**
   > **Statement.**
   > Let $f:A\to B$ and let $g:B\to C$. If $f$ is bijective and $g$ is
   > bijective, then $g\circ f:A\to C$ is bijective.
   >
   > \smallskip\noindent

93. () `prop:composition-injective` — **Composition of Injections Is Injective**
   > **Statement.**
   > Let $f:A\to B$ and let $g:B\to C$. If $f$ is injective and $g$ is
   > injective, then $g\circ f:A\to C$ is injective.
   >
   > \smallskip\noindent

94. () `prop:composition-surjective` — **Composition of Surjections Is Surjective**
   > **Statement.**
   > $\operatorname{Surjective}(f)\wedge\operatorname{Surjective}(g)
   > \Rightarrow\operatorname{Surjective}(g\circ f)$.
   >
   > \smallskip\noindent

95. () `prop:inverse-bijection` — **Inverse of a Bijection Is a Bijection**
   > **Statement.**
   > $\operatorname{Bijective}(f)\Rightarrow\operatorname{Bijective}(f^{-1})$.
   >
   > \smallskip\noindent

96. () `prop:preimage-union-intersection` — **Preimage Distributes over Union and Intersection**
   > **Statement.**
   > Let $f:A\to B$, $S,T\subseteq B$. Then:
   > \begin{enumerate}[label=(\roman*)]
   >   \item $f^{-1}(S\cup T)=f^{-1}(S)\cup f^{-1}(T)$.
   >   \item $f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T)$.
   >   \item $f^{-1}(S^c)=(f^{-1}(S))^c$.
   > \end{enumerate}
   >
   > \smallskip\noindent

97. () `lem:closure-elementary` — **Elementary Properties of Closures**
   > **Statement.**
   > Let $X, Y \subseteq \mathbb{R}$. Then: (i) $X \subseteq \overline{X}$;
   > (ii) $\overline{X \cup Y} = \overline{X} \cup \overline{Y}$;
   > (iii) $\overline{X \cap Y} \subseteq \overline{X} \cap \overline{Y}$;
   > (iv) $X \subseteq Y \Rightarrow \overline{X} \subseteq \overline{Y}$.
   >
   > \smallskip\noindent

98. () `thm:cluster-point-sequential` — **Sequential Characterization of Cluster Points**
   > **Statement.**
   > $c\text{ is a cluster point of }A$ if and only if there exists
   > $(a_n) \subseteq A \setminus \{c\}$ with $a_n \to c$.
   >
   > \smallskip\noindent

99. () `cor:closed-iff-seq-limits` — **Closed iff Sequentially Closed**
   > **Statement.**
   > $X\text{ is closed} \iff \forall (a_n)\subseteq X,\;
   > a_n \to x \Rightarrow x \in X$.
   >
   > \smallskip\noindent

100. () `thm:heine-borel-subsets-real-line` — **Heine--Borel Theorem for $R$**
   > **Statement.**
   > $X\text{ is closed} \wedge X\text{ is bounded}$
   > $\iff$ every $(a_n)\subseteq X$ has a subsequence converging to
   > a limit in $X$.
   >
   > \smallskip\noindent

101. () `cor:interval-all-limit-points` — **Every Point of an Interval Is a Cluster Point**
   > **Statement.**
   > If $I$ is an interval, then every $x\in I$ is a cluster point of $I$.
   >
   > \smallskip\noindent

102. () `thm:absolute-value-cauchy-sequence` — **Absolute Values of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. Then $(|x_n|)$ is Cauchy.
   >
   > \smallskip
   > \noindent

103. () `thm:cauchy-criterion-via-tails` — **Cauchy Criterion via Tails**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that the
   > $N$-tail has pairwise term distances less than $\varepsilon$.
   >
   > \smallskip
   > \noindent

104. () `thm:cauchy-sequence-with-convergent-subsequence` — **Cauchy Sequence with a Convergent Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. If a subsequence of $(x_n)$
   > converges to $L\in\mathbb{R}$, then $(x_n)$ converges to $L$.
   >
   > \smallskip
   > \noindent

105. () `thm:cauchy-sequences-are-bounded` — **Cauchy Sequences Are Bounded**
   > **Statement.**
   > Every Cauchy real sequence is bounded.
   >
   > \smallskip
   > \noindent

106. () `thm:cauchy-successive-differences-vanish` — **Cauchy Sequences Have Vanishing Successive Differences**
   > **Statement.**
   > If $(x_n)$ is a Cauchy real sequence, then
   > \[
   >   |x_{n+1}-x_n|\to 0.
   > \]
   >
   > \smallskip
   > \noindent

107. () `thm:cauchy-tail-diameter-criterion` — **Cauchy Tail Diameter Criterion**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > every sufficiently late tail has arbitrarily small pairwise diameter.
   >
   > \smallskip
   > \noindent

108. () `thm:convergent-sequences-are-cauchy` — **Convergent Sequences Are Cauchy**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ converges, then $(x_n)$ is
   > Cauchy.
   >
   > \smallskip
   > \noindent

109. () `thm:product-cauchy-sequences` — **Products of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_ny_n)$ is
   > Cauchy.
   >
   > \smallskip
   > \noindent

110. () `thm:reciprocal-cauchy-sequence` — **Reciprocals of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence. If there exist $c>0$ and
   > $N_0\in\mathbb{N}$ such that $|x_n|\ge c$ for every $n\ge N_0$, then
   > $(1/x_n)$ is Cauchy.
   >
   > \smallskip
   > \noindent

111. () `thm:quotient-cauchy-sequences` — **Quotients of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. If there exist $c>0$
   > and $N_0\in\mathbb{N}$ such that $|y_n|\ge c$ for every $n\ge N_0$,
   > then $(x_n/y_n)$ is Cauchy.
   >
   > \smallskip
   > \noindent

112. () `thm:scalar-multiple-cauchy-sequence` — **Scalar Multiples of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ be a Cauchy real sequence, and let $\alpha\in\mathbb{R}$.
   > Then $(\alpha x_n)$ is Cauchy.
   >
   > \smallskip
   > \noindent

113. () `thm:sum-cauchy-sequences` — **Sums of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n+y_n)$ is
   > Cauchy.
   >
   > \smallskip
   > \noindent

114. () `thm:difference-cauchy-sequences` — **Differences of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n-y_n)$ is
   > Cauchy.
   >
   > \smallskip
   > \noindent

115. () `thm:linear-combination-cauchy-sequences` — **Linear Combinations of Cauchy Sequences**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be Cauchy real sequences, and let
   > $\alpha,\beta\in\mathbb{R}$. Then $(\alpha x_n+\beta y_n)$ is Cauchy.
   >
   > \smallskip
   > \noindent

116. () `thm:constant-squeeze-theorem` — **Constant Squeeze Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If there
   > exists $N_0\in\mathbb{N}$ such that $L\le x_n\le L$ for every
   > $n\ge N_0$, then $x_n\to L$.
   >
   > \smallskip
   > \noindent

117. () `thm:equivalence-of-convergence-formulations` — **Equivalence of Convergence Formulations**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. The following
   > statements are equivalent.
   > \begin{enumerate}[label=\textup{(\alph*)}]
   >     \item $x_n \to L$.
   >     \item $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >           \;\bigl(|x_n - L| < \varepsilon\bigr)$.
   >     \item $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >           \;\bigl(L - \varepsilon < x_n < L + \varepsilon\bigr)$.
   >     \item $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >           \;\bigl(x_n \in V_\varepsilon(L)\bigr)$.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

118. () `thm:limit-of-a-product` — **Limit of a Product**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_ny_n\to LM$.
   >
   > \smallskip
   > \noindent

119. () `thm:limit-of-a-square-root` — **Limit of a Square Root**
   > **Statement.**
   > Let $(x_n)$ be a real sequence such that $0\le x_n$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$. If $x_n\to L$, then
   > $0\le L$ and $\sqrt{x_n}\to\sqrt{L}$.
   >
   > \smallskip
   > \noindent

120. () `thm:limit-of-a-square` — **Limit of a Square**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $x_n^2\to L^2$.
   >
   > \smallskip
   > \noindent

121. () `thm:limit-of-a-sum` — **Limit of a Sum**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n+y_n\to L+M$.
   >
   > \smallskip
   > \noindent

122. () `thm:limit-of-an-absolute-value` — **Limit of an Absolute Value**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $|x_n|\to |L|$.
   >
   > \smallskip
   > \noindent

123. () `thm:limit-of-scalar-multiple` — **Limit of a Scalar Multiple**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $\alpha\in\mathbb{R}$. If $x_n\to L$, then $\alpha x_n\to \alpha L$.
   >
   > \smallskip
   > \noindent

124. () `thm:limit-of-a-negation` — **Limit of a Negation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $-x_n\to -L$.
   >
   > \smallskip
   > \noindent

125. () `thm:limit-of-a-difference` — **Limit of a Difference**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n-y_n\to L-M$.
   >
   > \smallskip
   > \noindent

126. () `thm:nonzero-limit-eventually-nonzero` — **Nonzero Limit is Eventually Nonzero**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$ with $L\neq 0$.
   > If $x_n\to L$, then there exists $N\in\mathbb{N}$ such that $x_n\neq 0$
   > for every $n\ge N$.
   >
   > \smallskip
   > \noindent

127. () `thm:limit-of-a-reciprocal` — **Limit of a Reciprocal**
   > **Statement.**
   > Let $(x_n)$ be a real sequence such that $x_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$ with $L\neq 0$. If $x_n\to L$,
   > then $1/x_n\to 1/L$.
   >
   > \smallskip
   > \noindent

128. () `thm:limit-of-a-quotient` — **Limit of a Quotient**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences such that $y_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L,M\in\mathbb{R}$ with $M\neq 0$. If
   > $x_n\to L$ and $y_n\to M$, then $x_n/y_n\to L/M$.
   >
   > \smallskip
   > \noindent

129. () `thm:polynomial-sequence-limit` — **Polynomial Sequence Limit**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p\in\mathbb{R}[t]$ be a polynomial. If $x_n\to L$, then
   > $p(x_n)\to p(L)$.
   >
   > \smallskip
   > \noindent

130. () `thm:positive-limit-eventually-positive` — **Positive Limit is Eventually Positive**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L>0$. If $x_n\to L$, then there
   > exists $N\in\mathbb{N}$ such that $0<x_n$ for every $n\ge N$.
   >
   > \smallskip
   > \noindent

131. () `thm:rational-sequence-limit` — **Rational Sequence Limit**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p,q\in\mathbb{R}[t]$ be polynomials. Suppose $q(L)\neq 0$ and
   > $q(x_n)\neq 0$ for every $n\in\mathbb{N}$. If $x_n\to L$, then
   > \[
   > \frac{p(x_n)}{q(x_n)}\to \frac{p(L)}{q(L)}.
   > \]
   >
   > \smallskip
   > \noindent

132. () `thm:uniqueness-of-limits` — **Uniqueness of Limits**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$. If $x_n \to L$ and $x_n \to K$, then
   > $L = K$.
   >
   > \smallskip
   > \noindent

133. () `thm:limit-preserves-eventual-order` — **Limit Preserves Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > Suppose that $x_n\to L$ and $y_n\to M$. If there exists
   > $N_0\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N_0$, then
   > $L\le M$.
   >
   > \smallskip
   > \noindent

134. () `thm:eventual-strict-comparison-preserves-weak-limit-order` — **Eventual Strict Comparison Preserves Weak Limit Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n<y_n$ for every
   >   $n\ge N$, then $A\le B$.
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n>y_n$ for every
   >   $n\ge N$, then $A\ge B$.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

135. () `thm:constant-comparison-for-sequence-limits` — **Constant Comparison for Sequence Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $A,B\in\mathbb{R}$. Suppose
   > that $x_n\to A$.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n\le B$ for every
   >   $n\ge N$, then $A\le B$.
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n<B$ for every
   >   $n\ge N$, then $A\le B$.
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n\ge B$ for every
   >   $n\ge N$, then $A\ge B$.
   >   \item If there exists $N\in\mathbb{N}$ such that $x_n>B$ for every
   >   $n\ge N$, then $A\ge B$.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

136. () `thm:sequence-squeeze-theorem` — **Sequence Squeeze Theorem**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences, and let
   > $L\in\mathbb{R}$. Suppose that $a_n\to L$ and $b_n\to L$. If there
   > exists $N_0\in\mathbb{N}$ such that $a_n\le x_n\le b_n$ for every
   > $n\ge N_0$, then $x_n\to L$.
   >
   > \smallskip
   > \noindent

137. () `thm:compound-interest-approximation-e` — **Compound-Interest Approximation of $e$**
   > **Statement.**
   > Let $(c_n)$ be the compound-interest sequence. Then
   > \[
   >   \lim_{n\to\infty}c_n=e.
   > \]
   >
   > \smallskip
   > \noindent

138. () `thm:decimal-truncations-converge` — **Decimal Truncations Converge**
   > **Statement.**
   > Let $\alpha\in\mathbb{R}$, and let $(d_n)$ be the decimal truncation
   > sequence of $\alpha$. Then
   > \[
   >   \lim_{n\to\infty}d_n=\alpha.
   > \]
   >
   > \smallskip
   > \noindent

139. () `thm:absolute-value-squeeze-theorem` — **Absolute-Value Squeeze Theorem**
   > **Statement.**
   > Let $(x_n)$ and $(u_n)$ be real sequences, and let $L\in\mathbb{R}$.
   > Suppose that $u_n\to 0$. If there exists $N_0\in\mathbb{N}$ such that
   > $|x_n-L|\le u_n$ for every $n\ge N_0$, then $x_n\to L$.
   >
   > \smallskip
   > \noindent

140. () `thm:strict-limit-separation-gives-eventual-order` — **Strict Limit Separation Gives Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$. If $A<B$, then there exists
   > $N\in\mathbb{N}$ such that $x_n<y_n$ for every $n\ge N$.
   >
   > \smallskip
   > \noindent

141. () `thm:absolute-bound-gives-upper-and-lower-bounds` — **Absolute Bound Gives Upper and Lower Bounds**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $K > 0$. If $|x_n| \le K$ for every
   > $n \in \mathbb{N}$, then $-K \le x_n \le K$ for every
   > $n \in \mathbb{N}$.
   >
   > \smallskip
   > \noindent

142. () `thm:bounded-sequence-iff-bounded-above-and-below` — **Bounded Sequence If and Only If Bounded Above and Below**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if it is both bounded above and bounded below.
   >
   > \smallskip
   > \noindent

143. () `thm:constant-implies-ultimately-constant` — **Constant Implies Ultimately Constant**
   > **Statement.**
   > Every constant real sequence is ultimately constant.
   >
   > \smallskip
   > \noindent

144. () `thm:constant-null-sequence` — **Constant Null Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ is a null sequence if and only if
   > $c = 0$.
   >
   > \smallskip
   > \noindent

145. () `thm:constant-sequence-convergence` — **Constant Sequence Convergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ converges to $c$.
   >
   > \smallskip
   > \noindent

146. () `thm:difference-from-limit-is-null` — **Difference from the Limit is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L \in \mathbb{R}$. The sequence
   > $(x_n)$ converges to $L$ if and only if the sequence $(x_n - L)$ is a null
   > sequence.
   >
   > \smallskip
   > \noindent

147. () `thm:eventually-bounded-above-tail-formulation` — **Eventually Bounded Above Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded above if and
   > only if there exist $N_0 \in \mathbb{N}$ and $M \in \mathbb{R}$ such that
   > $x_n \le M$ for every $n \ge N_0$.
   >
   > \smallskip
   > \noindent

148. () `thm:eventually-bounded-below-tail-formulation` — **Eventually Bounded Below Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded below if and
   > only if there exist $N_0 \in \mathbb{N}$ and $m \in \mathbb{R}$ such that
   > $m \le x_n$ for every $n \ge N_0$.
   >
   > \smallskip
   > \noindent

149. () `thm:eventually-bounded-tail-formulation` — **Eventually Bounded Tail Formulation**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if there exist $N_0 \in \mathbb{N}$ and $M > 0$ such that $|x_n| \le M$ for
   > every $n \ge N_0$.
   >
   > \smallskip
   > \noindent

150. () `thm:tail-equality-preserves-convergence` — **Tail Equality Preserves Convergence**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be real sequences. If there exists
   > $N_0 \in \mathbb{N}$ such that $x_n = y_n$ for every $n \ge N_0$, then
   > for every $L \in \mathbb{R}$, $(x_n)$ converges to $L$ if and only if
   > $(y_n)$ converges to $L$.
   >
   > \smallskip
   > \noindent

151. () `thm:ultimately-constant-null-sequence` — **Ultimately Constant Null Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Suppose there exist $N_0 \in \mathbb{N}$
   > and $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$. Then
   > $(x_n)$ is a null sequence if and only if $c = 0$.
   >
   > \smallskip
   > \noindent

152. () `thm:ultimately-constant-sequence-convergence` — **Ultimately Constant Sequence Convergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exist $N_0 \in \mathbb{N}$ and
   > $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$, then
   > $(x_n)$ converges to $c$.
   >
   > \smallskip
   > \noindent

153. () `thm:ultimately-zero-sequence-is-null` — **Ultimately Zero Sequence is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exists $N_0 \in \mathbb{N}$ such
   > that $x_n = 0$ for every $n \ge N_0$, then $(x_n)$ is a null sequence.
   >
   > \smallskip
   > \noindent

154. () `thm:upper-and-lower-bounds-give-absolute-bound` — **Upper and Lower Bounds Give an Absolute Bound**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If there exist $m,M \in \mathbb{R}$ such
   > that $m \le x_n \le M$ for every $n \in \mathbb{N}$, then there exists
   > $K > 0$ such that $|x_n| \le K$ for every $n \in \mathbb{N}$.
   >
   > \smallskip
   > \noindent

155. () `thm:zero-sequence-is-null` — **Zero Sequence is Null**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $x_n = 0$ for every $n \in \mathbb{N}$,
   > then $(x_n)$ is a null sequence.
   >
   > \smallskip
   > \noindent

156. () `thm:divergence-to-infinity-implies-real-divergence` — **Divergence to Infinity Implies Real Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $x_n\to+\infty$ or $x_n\to-\infty$,
   > then $(x_n)$ is divergent.
   >
   > \smallskip
   > \noindent

157. () `thm:unbounded-above-has-positive-infinity-subsequence` — **Unbounded Above Sequence Has a Positive-Infinity Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded above, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to+\infty$.
   >
   > \smallskip
   > \noindent

158. () `thm:unbounded-below-has-negative-infinity-subsequence` — **Unbounded Below Sequence Has a Negative-Infinity Subsequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded below, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to-\infty$.
   >
   > \smallskip
   > \noindent

159. () `thm:convergence-iff-liminf-equals-limsup` — **Convergence iff Liminf Equals Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $L\in\mathbb{R}$. Then
   > $x_n\to L$ if and only if
   > \[
   >   \liminf_{n\to\infty}x_n
   >   =
   >   \limsup_{n\to\infty}x_n
   >   =
   >   L.
   > \]
   >
   > \smallskip
   > \noindent

160. () `thm:liminf-below-limsup` — **Liminf Is Below Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >   \liminf_{n\to\infty}x_n\le \limsup_{n\to\infty}x_n.
   > \]
   >
   > \smallskip
   > \noindent

161. () `thm:liminf-comparison-under-eventual-order` — **Liminf Comparison Under Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >   \liminf_{n\to\infty}x_n
   >   \le
   >   \liminf_{n\to\infty}y_n.
   > \]
   >
   > \smallskip
   > \noindent

162. () `thm:liminf-squeeze-under-eventual-order` — **Liminf Squeeze Under Eventual Order**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
   > exists $N\in\mathbb{N}$ such that
   > \[
   >   a_n\le x_n\le b_n
   >   \qquad\text{for every }n\ge N,
   > \]
   > then
   > \[
   >   \liminf_{n\to\infty}a_n
   >   \le
   >   \liminf_{n\to\infty}x_n
   >   \le
   >   \liminf_{n\to\infty}b_n.
   > \]
   >
   > \smallskip
   > \noindent

163. () `thm:limsup-comparison-under-eventual-order` — **Limsup Comparison Under Eventual Order**
   > **Statement.**
   > Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >   \limsup_{n\to\infty}x_n
   >   \le
   >   \limsup_{n\to\infty}y_n.
   > \]
   >
   > \smallskip
   > \noindent

164. () `thm:limsup-squeeze-under-eventual-order` — **Limsup Squeeze Under Eventual Order**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
   > exists $N\in\mathbb{N}$ such that
   > \[
   >   a_n\le x_n\le b_n
   >   \qquad\text{for every }n\ge N,
   > \]
   > then
   > \[
   >   \limsup_{n\to\infty}a_n
   >   \le
   >   \limsup_{n\to\infty}x_n
   >   \le
   >   \limsup_{n\to\infty}b_n.
   > \]
   >
   > \smallskip
   > \noindent

165. () `thm:tail-infima-are-increasing` — **Tail Infima Are Increasing**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $(i_n)$ be its tail
   > infimum sequence. Then $(i_n)$ is increasing.
   >
   > \smallskip
   > \noindent

166. () `thm:tail-suprema-are-decreasing` — **Tail Suprema Are Decreasing**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let $(s_n)$ be its tail
   > supremum sequence. Then $(s_n)$ is decreasing.
   >
   > \smallskip
   > \noindent

167. () `thm:algebraic-transformations-preserve-monotonicity` — **Algebraic Transformations Preserve Monotonicity**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $c,\alpha\in\mathbb{R}$.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is increasing, then $(x_n+c)$ is increasing.
   >   \item If $(x_n)$ is decreasing, then $(x_n+c)$ is decreasing.
   >   \item If $(x_n)$ is increasing and $\alpha>0$, then $(\alpha x_n)$ is increasing.
   >   \item If $(x_n)$ is increasing and $\alpha<0$, then $(\alpha x_n)$ is decreasing.
   >   \item If $(x_n)$ is increasing, then $(-x_n)$ is decreasing.
   >   \item If $(x_n)$ is decreasing, then $(-x_n)$ is increasing.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

168. () `thm:monotone-convergence-theorem` — **Monotone Convergence Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is increasing and bounded above, then $(x_n)$ converges and
   >   \[
   >     \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   >   \]
   >   \item If $(x_n)$ is decreasing and bounded below, then $(x_n)$ converges and
   >   \[
   >     \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   >   \]
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

169. () `thm:newton-approximation-sqrt-two` — **Newton Approximation of $2$**
   > **Statement.**
   > Let $(x_n)$ be the Newton sequence for $\sqrt{2}$. Then $(x_n)$ converges
   > and
   > \[
   >   \lim_{n\to\infty}x_n=\sqrt{2}.
   > \]
   >
   > \smallskip
   > \noindent

170. () `thm:bounded-monotone-sequence-equivalences` — **Bounded Monotone Sequence Equivalences**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is increasing, then $(x_n)$ converges if and only if
   >   $(x_n)$ is bounded above.
   >   \item If $(x_n)$ is decreasing, then $(x_n)$ converges if and only if
   >   $(x_n)$ is bounded below.
   >   \item If $(x_n)$ is monotone, then $(x_n)$ converges if and only if
   >   $(x_n)$ is bounded.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

171. () `thm:strict-monotonicity-implies-monotonicity` — **Strict Monotonicity Implies Monotonicity**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is strictly increasing, then $(x_n)$ is increasing.
   >   \item If $(x_n)$ is strictly decreasing, then $(x_n)$ is decreasing.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

172. () `thm:unbounded-monotone-divergence` — **Unbounded Monotone Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is increasing and is not bounded above, then
   >   $x_n\to+\infty$.
   >   \item If $(x_n)$ is decreasing and is not bounded below, then
   >   $x_n\to-\infty$.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

173. () `thm:decreasing-sequence-limit-as-infimum` — **Decreasing Sequence Limit as Infimum**
   > **Statement.**
   > Let $(x_n)$ be a decreasing real sequence that is bounded below. Then
   > \[
   >   \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   > \]
   >
   > \smallskip
   > \noindent

174. () `thm:increasing-sequence-limit-as-supremum` — **Increasing Sequence Limit as Supremum**
   > **Statement.**
   > Let $(x_n)$ be an increasing real sequence that is bounded above. Then
   > \[
   >   \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   > \]
   >
   > \smallskip
   > \noindent

175. () `thm:tail-suprema-and-infima-converge` — **Tail Suprema and Infima Converge**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Define
   > \[
   >   s_n=\sup\{x_k:k\ge n\},
   >   \qquad
   >   i_n=\inf\{x_k:k\ge n\}.
   > \]
   > Then $(s_n)$ and $(i_n)$ converge.
   >
   > \smallskip
   > \noindent

176. () `thm:bounded-sequence-has-limsup-and-liminf` — **Bounded Sequence Has Limsup and Liminf**
   > **Statement.**
   > Every bounded real sequence has a limit superior and a limit inferior.
   >
   > \smallskip
   > \noindent

177. () `thm:boundedness-passes-to-subsequences` — **Boundedness Passes to Subsequences**
   > **Statement.**
   > Every subsequence of a bounded real sequence is bounded.
   >
   > \smallskip
   > \noindent

178. () `thm:frequent-properties-yield-subsequences` — **Frequent Properties Yield Subsequences**
   > **Statement.**
   > Let $P(n)$ be a property of indices. If for every $N\in\mathbb{N}$ there
   > exists $n\ge N$ such that $P(n)$ holds, then there exists a strictly
   > increasing index map $\sigma:\mathbb{N}\to\mathbb{N}$ such that
   > $P(\sigma(k))$ holds for every $k\in\mathbb{N}$.
   >
   > \smallskip
   > \noindent

179. () `thm:cluster-values-are-subsequential-limits` — **Cluster Values Are Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. Then $L$ is a
   > cluster value of $(x_n)$ if and only if $L$ is a subsequential limit of
   > $(x_n)$.
   >
   > \smallskip
   > \noindent

180. () `thm:monotone-subsequence-theorem` — **Monotone Subsequence Theorem**
   > **Statement.**
   > Every real sequence has a monotone subsequence.
   >
   > \smallskip
   > \noindent

181. () `thm:bolzano-weierstrass-sequences` — **Bolzano-Weierstrass Theorem for Sequences**
   > **Statement.**
   > Every bounded real sequence has a convergent subsequence.
   >
   > \smallskip
   > \noindent

182. () `thm:cauchy-criterion-real-sequences` — **Cauchy Criterion for Real Sequences**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. Then $(x_n)$ converges if and only if
   > $(x_n)$ is Cauchy.
   >
   > \smallskip
   > \noindent

183. () `thm:factorial-partial-sums-approximate-e` — **Factorial Partial Sums Approximate $e$**
   > **Statement.**
   > Let $(s_n)$ be the factorial partial-sum sequence. Then $(s_n)$ converges
   > to the Euler number $e$:
   > \[
   >   \lim_{n\to\infty}s_n=e.
   > \]
   >
   > \smallskip
   > \noindent

184. () `thm:bounded-sequences-have-cluster-values` — **Bounded Sequences Have Cluster Values**
   > **Statement.**
   > Every bounded real sequence has at least one cluster value.
   >
   > \smallskip
   > \noindent

185. () `thm:liminf-smallest-subsequential-limit` — **Liminf Is the Smallest Subsequential Limit**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let
   > $I=\liminf_{n\to\infty}x_n$. Then $I$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is greater than or
   > equal to $I$.
   >
   > \smallskip
   > \noindent

186. () `thm:limsup-largest-subsequential-limit` — **Limsup Is the Largest Subsequential Limit**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence, and let
   > $S=\limsup_{n\to\infty}x_n$. Then $S$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is less than or equal
   > to $S$.
   >
   > \smallskip
   > \noindent

187. () `thm:limsup-liminf-extremal-cluster-values` — **Limsup and Liminf Are Extremal Cluster Values**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > $\limsup_{n\to\infty}x_n$ is the largest cluster value of $(x_n)$, and
   > $\liminf_{n\to\infty}x_n$ is the smallest cluster value of $(x_n)$.
   >
   > \smallskip
   > \noindent

188. () `thm:monotonicity-passes-to-subsequences` — **Monotonicity Passes to Subsequences**
   > **Statement.**
   > Every subsequence of an increasing real sequence is increasing, and every
   > subsequence of a decreasing real sequence is decreasing.
   >
   > \smallskip
   > \noindent

189. () `thm:subsequence-indices-dominate-identity` — **Subsequence Indices Dominate the Identity**
   > **Statement.**
   > Let $\sigma:\mathbb{N}\to\mathbb{N}$ be a strictly increasing index map.
   > Then
   > \[
   >   k\le \sigma(k)
   >   \qquad
   >   \text{for every } k\in\mathbb{N}.
   > \]
   >
   > \smallskip
   > \noindent

190. () `thm:eventual-properties-pass-to-subsequences` — **Eventual Properties Pass to Subsequences**
   > **Statement.**
   > Let $P(n)$ be a property of indices. If there exists $N\in\mathbb{N}$ such
   > that $P(n)$ holds for every $n\ge N$, then for every strictly increasing
   > index map $\sigma$ there exists $K\in\mathbb{N}$ such that $P(\sigma(k))$
   > holds for every $k\ge K$.
   >
   > \smallskip
   > \noindent

191. () `thm:squeeze-passes-to-subsequences` — **Squeeze Passes to Subsequences**
   > **Statement.**
   > Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences. If
   > $a_n\le x_n\le b_n$ eventually, then for every subsequence
   > $(x_{\sigma(k)})$ there exists $K\in\mathbb{N}$ such that
   > \[
   >   a_{\sigma(k)}\le x_{\sigma(k)}\le b_{\sigma(k)}
   >   \qquad
   >   \text{for every } k\ge K.
   > \]
   >
   > \smallskip
   > \noindent

192. () `thm:subsequence-of-subsequence` — **Subsequence of a Subsequence**
   > **Statement.**
   > Every subsequence of a subsequence of $(x_n)$ is a subsequence of $(x_n)$.
   >
   > \smallskip
   > \noindent

193. () `thm:subsequences-preserve-limits` — **Subsequences Preserve Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then every subsequence of $(x_n)$ converges to $L$.
   >
   > \smallskip
   > \noindent

194. () `thm:bounded-divergence-produces-two-subsequential-limits` — **Bounded Divergence Produces Two Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. If $(x_n)$ is divergent, then
   > there exist $L,K\in\mathbb{R}$ with $L\ne K$ such that $L$ and $K$ are
   > subsequential limits of $(x_n)$.
   >
   > \smallskip
   > \noindent

195. () `thm:subsequential-limit-of-convergent-sequence` — **Subsequential Limit of a Convergent Sequence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $L$ is the only possible subsequential limit of $(x_n)$.
   >
   > \smallskip
   > \noindent

196. () `thm:divergence-by-two-subsequential-limits` — **Divergence by Two Subsequential Limits**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ has two distinct subsequential
   > limits, then $(x_n)$ does not converge.
   >
   > \smallskip
   > \noindent

197. () `thm:two-subsequential-limits-force-divergence` — **Two Subsequential Limits Force Divergence**
   > **Statement.**
   > Let $(x_n)$ be a real sequence. If $(x_n)$ has two subsequential limits
   > $L,K\in\mathbb{R}$ with $L\ne K$, then $(x_n)$ is divergent.
   >
   > \smallskip
   > \noindent

198. () `thm:oscillation-criterion-via-liminf-limsup` — **Oscillation Criterion via Liminf and Limsup**
   > **Statement.**
   > Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >   \liminf_{n\to\infty}x_n
   >   <
   >   \limsup_{n\to\infty}x_n
   > \]
   > if and only if $(x_n)$ has two distinct subsequential limits.
   >
   > \smallskip
   > \noindent

199. () `thm:subsequential-limits-respect-bounds` — **Subsequential Limits Respect Bounds**
   > **Statement.**
   > Let $(x_n)$ be a real sequence and let $L$ be a subsequential limit of
   > $(x_n)$. If $m\le x_n\le M$ for every $n\in\mathbb{N}$, then
   > $m\le L\le M$.
   >
   > \smallskip
   > \noindent

200. () `thm:sequential-compactness-closed-bounded-interval` — **Sequential Compactness of Closed Bounded Intervals**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ with $a\le b$. Every sequence in $[a,b]$ has a
   > convergent subsequence whose limit belongs to $[a,b]$.
   >
   > \smallskip
   > \noindent

201. () `thm:convergence-by-domination` — **Convergence by Domination**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. Let
   > $(a_n)$ be a sequence of positive real numbers with
   > $\displaystyle\lim_{n \to \infty} a_n = 0$. If there exist a constant
   > $c > 0$ and an index $m \in \mathbb{N}$ such that
   > \[
   >     |x_n - L| \;\le\; c\, a_n \qquad \forall n \ge m,
   > \]
   > then $\displaystyle\lim_{n \to \infty} x_n = L$.
   >
   > \smallskip
   > \noindent

202. () `thm:convergence-of-tail` — **Convergence of a Tail**
   > **Statement.**
   > Let $(x_n) \subseteq \mathbb{R}$ and let $m \in \mathbb{N}$. The
   > $m$-tail $(x_{m+n})_{n \in \mathbb{N}}$ converges if and only if
   > $(x_n)$ converges. Moreover, in this case,
   > \[
   >     \lim_{n \to \infty} x_{m+n} \;=\; \lim_{n \to \infty} x_n.
   > \]
   >
   > \smallskip
   > \noindent

203. () `thm:eventually-monotone-convergence-theorem` — **Eventually Monotone Convergence Theorem**
   > **Statement.**
   > Let $(x_n)$ be a real sequence.
   > \begin{enumerate}[label=(\alph*)]
   >   \item If $(x_n)$ is eventually increasing and bounded above, then
   >   $(x_n)$ converges.
   >   \item If $(x_n)$ is eventually decreasing and bounded below, then
   >   $(x_n)$ converges.
   >   \item If $(x_n)$ is eventually monotone and bounded, then $(x_n)$ converges.
   > \end{enumerate}
   >
   > \smallskip
   > \noindent

204. () `thm:ratio-limit-less-than-one-implies-null` — **Ratio Limit Less Than One Implies Null**
   > **Statement.**
   > Let $(x_n)$ be a sequence of positive real numbers. Suppose that the
   > limit
   > \[
   >     L := \lim_{n\to\infty}\frac{x_{n+1}}{x_n}
   > \]
   > exists. If $L<1$, then $(x_n)$ converges and
   > \[
   >     \lim_{n\to\infty} x_n = 0.
   > \]
   >
   > \smallskip
   > \noindent

205. () `prop:addition-rule-finite-set-summation` — **Addition Rule for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) and
   > \(g:X\to\mathbb{R}\) be functions. Then
   > \[
   >   \sum_{x\in X} (f(x)+g(x))
   >   =
   >   \sum_{x\in X} f(x)
   >   +
   >   \sum_{x\in X} g(x).
   > \]

206. () `lem:comparison-test-finite-series` — **Comparison Test for Finite Series**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) and \(b_i\) be real
   > numbers assigned to each integer \(i\) satisfying \(m \le i \le n\).
   > Suppose that \(a_i \le b_i\) for all \(i\) satisfying \(m \le i \le n\).
   > Then
   > \[
   >   \sum_{i=m}^{n} a_i
   >   \le
   >   \sum_{i=m}^{n} b_i.
   > \]

207. () `prop:disjoint-union-finite-set-summation` — **Disjoint Union Finite Set Summation**
   > **Statement.**
   > Let \(X\) and \(Y\) be disjoint finite sets, so \(X\cap Y=\emptyset\),
   > and let \(f:X\cup Y\to\mathbb{R}\) be a function. Then
   > \[
   >   \sum_{z\in X\cup Y} f(z)
   >   =
   >   \left(\sum_{x\in X} f(x)\right)
   >   +
   >   \left(\sum_{y\in Y} f(y)\right).
   > \]

208. () `prop:empty-finite-set-summation` — **Empty Finite Set Summation**
   > **Statement.**
   > If \(X\) is empty, and \(f:X\to\mathbb{R}\) is a function, then
   > \[
   >   \sum_{x\in X} f(x)=0.
   > \]

209. () `lem:finite-sum-of-sums` — **Finite Sum of Sums**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) and \(b_i\) be real
   > numbers assigned to each integer \(i\) satisfying \(m \le i \le n\).
   > Then
   > \[
   >   \sum_{i=m}^{n} (a_i+b_i)
   >   =
   >   \left(\sum_{i=m}^{n} a_i\right)
   >   +
   >   \left(\sum_{i=m}^{n} b_i\right).
   > \]

210. () `lem:finite-sum-reindexing` — **Reindexing a Finite Sum**
   > **Statement.**
   > Let \(m \le n\) be integers, let \(k\) be an integer, and let \(a_i\)
   > be a real number assigned to each integer \(i\) satisfying \(m \le i
   > \le n\). Then
   > \[
   >   \sum_{i=m}^{n} a_i
   >   =
   >   \sum_{j=m+k}^{n+k} a_{j-k}.
   > \]

211. () `lem:finite-sum-scalar-multiple` — **Finite Sum of Scalar Multiples**
   > **Statement.**
   > Let \(m \le n\) be integers, let \(a_i\) be a real number assigned to
   > each integer \(i\) satisfying \(m \le i \le n\), and let
   > \(c \in \mathbb{R}\). Then
   > \[
   >   \sum_{i=m}^{n} (c a_i)
   >   =
   >   c\left(\sum_{i=m}^{n} a_i\right).
   > \]

212. () `lem:finite-sum-splitting` — **Splitting a Finite Sum**
   > **Statement.**
   > Let \(m \le n < p\) be integers, and let \(a_i\) be a real number
   > assigned to each integer \(i\) satisfying \(m \le i \le p\). Then
   > \[
   >   \sum_{i=m}^{n} a_i
   >   +
   >   \sum_{i=n+1}^{p} a_i
   >   =
   >   \sum_{i=m}^{p} a_i.
   > \]

213. () `prop:finite-summations-well-defined` — **Finite Summations Are Well-Defined**
   > **Statement.**
   > Let \(X\) be a finite set with \(n\) elements, where \(n \in \mathbb{N}\),
   > let \(f:X\to\mathbb{R}\), and let
   > \[
   >   g:\{i\in\mathbb{N}:1\le i\le n\}\to X
   >   \qquad\text{and}\qquad
   >   h:\{i\in\mathbb{N}:1\le i\le n\}\to X
   > \]
   > be bijections. Then
   > \[
   >   \sum_{i=1}^{n} f(g(i))
   >   =
   >   \sum_{i=1}^{n} f(h(i)).
   > \]

214. () `prop:integer-interval-finite-set-summation` — **Integer Interval as a Finite Set**
   > **Statement.**
   > Let \(n \le m\) be integers, and let
   > \[
   >   X:=\{i\in\mathbb{Z}:n\le i\le m\}.
   > \]
   > If \(a_i\) is a real number assigned to each integer \(i\in X\), then
   > \[
   >   \sum_{i=n}^{m} a_i
   >   =
   >   \sum_{i\in X} a_i.
   > \]

215. () `lem:iterated-summation-over-product` — **Iterated Summation over a Product**
   > **Statement.**
   > Let \(X\) and \(Y\) be finite sets, and let
   > \(f:X\times Y\to\mathbb{R}\) be a function. Then
   > \[
   >   \sum_{x\in X}
   >   \left(
   >     \sum_{y\in Y} f(x,y)
   >   \right)
   >   =
   >   \sum_{(x,y)\in X\times Y} f(x,y).
   > \]

216. () `cor:fubini-theorem-finite-series` — **Fubini's Theorem for Finite Series**
   > **Statement.**
   > Let \(X\) and \(Y\) be finite sets, and let
   > \(f:X\times Y\to\mathbb{R}\) be a function. Then
   > \[
   >   \sum_{x\in X}
   >   \left(
   >     \sum_{y\in Y} f(x,y)
   >   \right)
   >   =
   >   \sum_{(x,y)\in X\times Y} f(x,y)
   >   =
   >   \sum_{(y,x)\in Y\times X} f(x,y)
   >   =
   >   \sum_{y\in Y}
   >   \left(
   >     \sum_{x\in X} f(x,y)
   >   \right).
   > \]

217. () `prop:monotonicity-finite-set-summation` — **Monotonicity for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) and
   > \(g:X\to\mathbb{R}\) be functions such that \(f(x)\le g(x)\) for all
   > \(x\in X\). Then
   > \[
   >   \sum_{x\in X} f(x)
   >   \le
   >   \sum_{x\in X} g(x).
   > \]

218. () `prop:scalar-multiplication-rule-finite-set-summation` — **Scalar Multiplication Rule for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, let \(f:X\to\mathbb{R}\) be a function, and
   > let \(c\) be a real number. Then
   > \[
   >   \sum_{x\in X} c f(x)
   >   =
   >   c \sum_{x\in X} f(x).
   > \]

219. () `prop:singleton-finite-set-summation` — **Singleton Finite Set Summation**
   > **Statement.**
   > If \(X\) consists of a single element, \(X=\{x_0\}\), and
   > \(f:X\to\mathbb{R}\) is a function, then
   > \[
   >   \sum_{x\in X} f(x)=f(x_0).
   > \]

220. () `prop:substitution-finite-set-summation` — **Substitution for Finite Set Summation**
   > **Statement.**
   > If \(X\) is a finite set, \(f:X\to\mathbb{R}\) is a function, and
   > \(g:Y\to X\) is a bijection, then
   > \[
   >   \sum_{x\in X} f(x)
   >   =
   >   \sum_{y\in Y} f(g(y)).
   > \]

221. () `lem:triangle-inequality-finite-series` — **Triangle Inequality for Finite Series**
   > **Statement.**
   > Let \(m \le n\) be integers, and let \(a_i\) be a real number assigned
   > to each integer \(i\) satisfying \(m \le i \le n\). Then
   > \[
   >   \left\lvert \sum_{i=m}^{n} a_i \right\rvert
   >   \le
   >   \sum_{i=m}^{n} \lvert a_i\rvert.
   > \]

222. () `prop:triangle-inequality-finite-set-summation` — **Triangle Inequality for Finite Set Summation**
   > **Statement.**
   > Let \(X\) be a finite set, and let \(f:X\to\mathbb{R}\) be a function.
   > Then
   > \[
   >   \left\lvert \sum_{x\in X} f(x) \right\rvert
   >   \le
   >   \sum_{x\in X} \lvert f(x)\rvert.
   > \]

223. () `prop:abs-value-is-distance-to-zero` — **Absolute Value Is Distance to the Origin**
   > **Statement.**
   > For every $a\in\mathbb{R}$, $\;|a|=d(a,0)$.

224. () `thm:closed-iff-contains-limit-points` — **Closed Sets Contain Their Limit Points**
   > **Statement.**
   > A set $F\subseteq\mathbb{R}$ is closed if and only if it contains every one of its limit points.

225. () `thm:compact-implies-closed-bounded` — **Compact Subsets of $R$ Are Closed and Bounded**
   > **Statement.**
   > If $K\subseteq\mathbb{R}$ is compact, then $K$ is closed and bounded.

226. () `thm:closed-bounded-interval-compact` — **Closed Bounded Intervals Are Compact**
   > **Statement.**
   > Every closed bounded interval $[a,b]\subseteq\mathbb{R}$ is compact.

227. () `thm:heine-borel` — **Heine--Borel Theorem for $R$**
   > **Statement.**
   > A set $K\subseteq\mathbb{R}$ is compact if and only if $K$ is closed and bounded.

228. () `thm:open-interval-is-open` — **Open Intervals Are Open**
   > **Statement.**
   > Every open interval $(a,b)$, every open ray $(a,\infty)$ and $(-\infty,b)$, and $\mathbb{R}$ itself are open sets.

229. () `thm:open-set-closure-operations` — **Unions and Finite Intersections of Open Sets**
   > **Statement.**
   > An arbitrary union of open subsets of $\mathbb{R}$ is open, and a finite intersection of open subsets of $\mathbb{R}$ is open.

230. () `thm:distance-is-a-metric` — **The Distance Function Is a Metric**
   > **Statement.**
   > The map $d(x,y)=|x-y|$ satisfies, for all $x,y,z\in\mathbb{R}$: (i) $d(x,y)\ge 0$ with $d(x,y)=0$ iff $x=y$; (ii) $d(x,y)=d(y,x)$; and (iii) $d(x,z)\le d(x,y)+d(y,z)$. Hence $(\mathbb{R},d)$ is a metric space.

231. () `thm:closed-set-closure-operations` — **Closure Laws for Closed Sets**
   > **Statement.**
   > An arbitrary intersection of closed subsets of $\mathbb{R}$ is closed, and a finite union of closed subsets of $\mathbb{R}$ is closed.

232. () `thm:bernstein-approximation` — **Bernstein Approximation Theorem**
   > **Statement.**
   > TODO: restate the theorem.

233. () `thm:weierstrass-approximation` — **Weierstrass Approximation Theorem**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous. For every $\varepsilon>0$ there exists a polynomial $p_\varepsilon\in\mathbb{R}[x]$ such that $\|f-p_\varepsilon\|_{\infty,[a,b]}<\varepsilon$.

234. () `thm:cousins-theorem` — **Cousin's Theorem**
   > **Statement.**
   > Every gauge $\delta:[a,b]\to(0,\infty)$ on a closed interval $[a,b]$
   > admits a $\delta$-fine tagged partition of $[a,b]$.

235. () `lem:every-point-covered-by-tag` — **Every Point Is Covered by a Tag**
   > **Statement.**
   > Let $\dot{\mathcal{P}}=\{([x_{i-1},x_i],t_i)\}_{i=1}^n$ be a tagged partition of $[a,b]$ that is $\delta$-fine on $[a,b]$, and let $x\in[a,b]$. Then there exists $i\in\{1,\ldots,n\}$ such that $|x-t_i|<\delta(t_i)$.

236. () `thm:bolzano-intermediate-value` — **Bolzano's Intermediate Value Theorem**
   > **Statement.**
   > Let $I$ be an interval, let $f : I \to \mathbb{R}$ be continuous on $I$, let $a, b \in I$, and let $k \in \mathbb{R}$. If $f(a) < k < f(b)$ or $f(a) > k > f(b)$, then there exists $c$ between $a$ and $b$ such that $f(c) = k$.

237. () `thm:boundedness-theorem` — **Boundedness Theorem**
   > **Statement.**
   > Every function continuous on a closed bounded interval $[a,b]$ is bounded on $[a,b]$.

238. () `thm:darboux-property` — **Darboux Property**
   > **Statement.**
   > Let $f : [a, b] \to \mathbb{R}$ be continuous on the closed interval $[a, b]$. For any $c \in \mathbb{R}$, if $f(x) \neq c$ for all $x \in [a, b]$, then either $f(x) > c$ for all $x \in [a, b]$, or $f(x) < c$ for all $x \in [a, b]$.

239. () `thm:extreme-value-theorem` — **Extreme Value Theorem**
   > **Statement.**
   > Let $a,b \in \mathbb{R}$ with $a<b$, and let $f:[a,b] \to \mathbb{R}$ be continuous. There exist points $x_m,x_M \in [a,b]$ such that $f(x_m) \le f(x) \le f(x_M)$ for every $x \in [a,b]$. Equivalently, $f$ attains both an absolute maximum and an absolute minimum on $[a,b]$.

240. () `thm:image-of-closed-bounded-interval` — **Image of a Closed Bounded Interval Is a Closed Bounded Interval**
   > **Statement.**
   > Let $f : [a,b] \to \mathbb{R}$ be continuous on the closed bounded interval $[a,b]$. Then $f([a,b]) = [m, M]$, where $m = \inf f([a,b])$ and $M = \sup f([a,b])$.

241. () `thm:location-of-roots` — **Location of Roots Theorem**
   > **Statement.**
   > Let $f : [a,b] \to \mathbb{R}$ be continuous on $[a,b]$. If $f(a) < 0 < f(b)$ or $f(a) > 0 > f(b)$, then there exists $c \in (a,b)$ such that $f(c) = 0$.

242. () `thm:preservation-of-intervals` — **Preservation of Intervals**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval and let $f : I \to \mathbb{R}$ be continuous on $I$. Then $f(I)$ is an interval.

243. () `thm:bounded-limits` — **Bounded Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$, let $c$ be a cluster point of $A$, and
   > let $a, b \in \mathbb{R}$. If $a \leq f(x) \leq b$ for all $x \in A$
   > with $x \neq c$, and $\lim_{x\to c}f(x)=L$, then
   > $a \leq L \leq b$.
   >
   > \smallskip\noindent

244. () `prop:cauchy-criterion-limits` — **Cauchy Criterion for Function Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ exists for some
   > $L \in \mathbb{R}$ if and only if
   > \[
   >   \ForallOT{\varepsilon},\;
   >   \ExistsIT{\delta},\;
   >   \forall x, y \in A :\;
   >   0<|x-c|<\delta
   >   \;\wedge\;
   >   0<|y-c|<\delta
   >   \;\Rightarrow\;
   >   |f(x)-f(y)|<\varepsilon.
   > \]
   >
   > \smallskip\noindent

245. () `thm:composition-of-limits` — **Composition of Limits**
   > **Statement.**
   > Let $f : A \to B$, let $g : B \to \mathbb{R}$, let $c_1$ be a
   > cluster point of $A$, and let $c_2 \in \mathbb{R}$ be a cluster
   > point of $B$. Suppose $\lim_{x\to c_1}f(x)=c_2$ and
   > $\lim_{y\to c_2}g(y)=L$. If $c_2 \in B$, assume also that
   > $g(c_2) = L$. Then $\lim_{x\to c_1}g(f(x))=L$.
   >
   > \smallskip\noindent

246. () `prop:limit-absolute-value` — **Limit of Absolute Value**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$, then
   > $\lim_{x\to c}|f(x)|=|L|$.
   >
   > \smallskip\noindent

247. () `thm:limit-difference` — **Difference Rule for Function Limits**
   > **Statement.**
   > Let $f, g : A \to \mathbb{R}$, let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > $\lim_{x\to c}(f-g)(x) = L-M$.

248. () `thm:limit-implies-local-bounding` — **Limit Implies Local Boundedness**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$ for some $L \in \mathbb{R}$,
   > then there exist $\delta, M > 0$ such that $|f(x)| \leq M$ for all
   > $x \in A$ with $0<|x-c|<\delta$.
   >
   > \smallskip\noindent

249. () `prop:limit-neighbourhood-equiv` — **Neighbourhood Form of the Limit**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every
   > $\varepsilon$-neighbourhood $V_\varepsilon(L)$ there exists a
   > $\delta$-neighbourhood $V_\delta(c)$ such that
   > $x\in V_\delta^*(c)\cap A$ implies $f(x)\in V_\varepsilon(L)$.
   >
   > \smallskip\noindent

250. () `thm:limit-product` — **Product Rule for Function Limits**
   > **Statement.**
   > Let $f, g : A \to \mathbb{R}$, let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > $\lim_{x\to c}(fg)(x) = LM$.

251. () `thm:limit-quotient` — **Quotient Rule for Function Limits**
   > **Statement.**
   > Let $f, g : A \to \mathbb{R}$, let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$, $\lim_{x\to c}g(x)=M$, and $M \neq 0$, then there
   > exists $\delta_0 > 0$ such that $g(x) \neq 0$ whenever $x \in A$ and
   > $0 < |x-c| < \delta_0$, and $\lim_{x\to c}(f/g)(x) = L/M$.

252. () `thm:limit-scalar-multiple` — **Scalar Multiple Rule for Function Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$, let $c$ be a cluster point of $A$, and let
   > $\alpha \in \mathbb{R}$. If $\lim_{x\to c}f(x)=L$, then
   > $\lim_{x\to c}(\alpha f)(x) = \alpha L$.

253. () `thm:limit-sum` — **Sum Rule for Function Limits**
   > **Statement.**
   > Let $f, g : A \to \mathbb{R}$, let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > $\lim_{x\to c}(f+g)(x) = L+M$.

254. () `thm:limit-unique` — **Uniqueness of Limits of Functions**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $f$ has at most one limit at $c$.
   >
   > \smallskip\noindent

255. () `thm:limits-are-local` — **Limits Are Local**
   > **Statement.**
   > Let $E \subseteq X \subseteq \mathbb{R}$, let $x_0$ be a cluster
   > point of $E$, let $f : X \to \mathbb{R}$, and let $\delta > 0$.
   > Then
   > \[
   >   \lim_{x\to x_0;\,x\in E}f(x)=L
   >   \;\iff\;
   >   \lim_{x\to x_0;\,x\in E\cap(x_0-\delta,x_0+\delta)}f(x)=L.
   > \]
   >
   > \smallskip\noindent

256. () `thm:monotone-limit-theorem` — **Monotone Limit Theorem**
   > **Statement.**
   > Let $a < b$ and let $f : (a,b) \to \mathbb{R}$ be monotone and
   > bounded. Then both one-sided limits exist at every interior point.
   > For increasing $f$ and every $x_0 \in (a,b)$:
   > \[
   >   f(x_0^-) = \sup\{\,f(x) : a < x < x_0\,\},
   >   \qquad
   >   f(x_0^+) = \inf\{\,f(x) : x_0 < x < b\,\}.
   > \]
   >
   > \smallskip\noindent

257. () `cor:sequential-criterion-left-hand-limit` — **Sequential Criterion for Left-Hand Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(-\infty,c)$. Then $\lim_{x\to c^-}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(-\infty,c)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.
   >
   > \smallskip\noindent

258. () `prop:sequential-criterion-limits` — **Sequential Criterion for Function Limits**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every sequence
   > $(x_n)\subseteq A\setminus\{c\}$ with $x_n\to c$, one has
   > $f(x_n)\to L$.
   >
   > \smallskip\noindent

259. () `cor:limit-three-equiv` — **Three Equivalent Forms of the Function Limit**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > The $\varepsilon$-$\delta$ form of $\lim_{x\to c}f(x)=L$, the
   > neighbourhood form, and the sequential form are equivalent descriptions
   > of the same limit condition.
   >
   > \smallskip\noindent

260. () `thm:sequential-criterion-right-hand-limit` — **Sequential Criterion for Right-Hand Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(c,\infty)$. Then $\lim_{x\to c^+}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(c,\infty)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.
   >
   > \smallskip\noindent

261. () `thm:squeeze-function-limits` — **Squeeze Theorem for Function Limits**
   > **Statement.**
   > Let $f, g, h : A \to \mathbb{R}$ and let $c$ be a cluster point of
   > $A$. Suppose $\lim_{x\to c}f(x)=L =
   > \lim_{x\to c}g(x)=L$, and suppose there exists
   > $\delta_0 > 0$ such that
   > \[
   >   \forall x \in A,\;
   >   0 < |x - c| < \delta_0
   >   \;\Rightarrow\;
   >   f(x) \leq h(x) \leq g(x).
   > \]
   > Then $\lim_{x\to c}h(x)=L$.
   >
   > \smallskip\noindent

262. () `thm:two-sided-limit-iff-matching-one-sided-limits` — **Two-Sided Limit via One-Sided Limits**
   > **Statement.**
   > Let $A\subseteq\mathbb{R}$ and let $f:A\to\mathbb{R}$. If $c$ is a
   > cluster point of both $A\cap(c,\infty)$ and $A\cap(-\infty,c)$, then
   > $\lim_{x\to c}f(x)=L$ if and only if both $\lim_{x\to c^+}f(x)=L$ and
   > $\lim_{x\to c^-}f(x)=L$.
   >
   > \smallskip\noindent

263. () `prop:continuous-injective-iff-strictly-monotone` — **Continuous Injective Is Strictly Monotone**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then $f$ is injective if and only if $f$ is strictly monotone on $[a,b]$.

264. () `thm:continuous-inverse-theorem` — **Continuous Inverse Theorem**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be strictly monotone and continuous on $I$. Then the inverse function $f^{-1}:f(I)\to I$ exists, is strictly monotone, and is continuous on $f(I)$.

265. () `prop:limsup-geq-liminf-function` — **$$**
   > **Statement.**
   > Let $A\subseteq \mathbb{R}$, let $x_0$ be a limit point of $A$, and let $f:A\to\mathbb{R}$. Then
   > \[
   > \limsup_{x\to x_0} f(x) \ge \liminf_{x\to x_0} f(x).
   > \]

266. () `prop:limsup-liminf-limit-criterion` — **Limit Exists iff $=$**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, let $x_0$ be a limit point of $A$ with $x_0 \in \mathbb{R}$, and let $L \in \mathbb{R}$. Then $\lim_{x \to x_0} f(x)$ exists and equals $L$ if and only if $\limsup_{x \to x_0} f(x) = \liminf_{x \to x_0} f(x) = L$.

267. () `prop:monotone-discontinuities-first-kind` — **Discontinuities of a Monotone Function Are of First Kind**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f:I \to \mathbb{R}$ be monotone, and let $a \in I$ be such that there exist points of $I$ strictly less and strictly greater than $a$. If $f$ is discontinuous at $a$, then both one-sided limits $\lim_{x\uparrow a} f(x)$ and $\lim_{x\downarrow a} f(x)$ exist in $\mathbb{R}$.

268. () `cor:jump-intervals-for-monotone-discontinuities` — **Jump Intervals of a Monotone Function Are Disjoint**
   > **Statement.**
   > Let $f : I \to \mathbb{R}$ be a monotone function on an interval $I$, and let $D \subseteq I$ be the set of all discontinuities of $f$. For each $c \in D$, the jump interval at $c$ is $J_c(f) \coloneqq (f(c^{-}), f(c^{+}))$. If $c, d \in D$ with $c \neq d$, then $J_c(f) \cap J_d(f) = \emptyset$.

269. () `thm:monotone-one-sided-limits` — **One-Sided Limits of Monotone Functions**
   > **Statement.**
   > Let $f : I \to \mathbb{R}$ be monotone increasing on the interval $I$, and let $c \in I$ be an interior point. Then both one-sided limits of $f$ at $c$ exist and are given by
   > \[
   >   \lim_{x \to c^{-}} f(x) = \sup\{f(x) : x < c,\, x \in I\}
   >   \qquad \text{and} \qquad
   >   \lim_{x \to c^{+}} f(x) = \inf\{f(x) : x > c,\, x \in I\}.
   > \]
   > Moreover, $f(c^{-}) \leq f(c) \leq f(c^{+})$.

270. () `cor:monotone-continuity-criterion` — **Continuity Criterion for Monotone Functions**
   > **Statement.**
   > Let $f : I \to \mathbb{R}$ be monotone increasing and let $c \in I$ be an interior point. Then $f$ is continuous at $c$ if and only if $f(c^{-}) = f(c^{+})$.

271. () `thm:monotone-discontinuities-countable` — **Discontinuities of a Monotone Function Are Countable**
   > **Statement.**
   > Let $f : I \to \mathbb{R}$ be a monotone function on an interval $I$. Then the set of discontinuities of $f$ is at most countable.

272. () `cor:monotone-continuous-on-dense-set` — **Monotone Function Is Continuous on a Dense Set**
   > **Statement.**
   > Let $f : I \to \mathbb{R}$ be a monotone function on an interval $I$. Then the set of points of continuity of $f$ is dense in $I$.

273. () `thm:continuity-iff-zero-oscillation` — **Continuity Characterised by Oscillation**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, and let $c \in A$. Then $f$ is continuous at $c$ if and only if $\omega(f;c)=0$.

274. () `prop:discontinuity-set-via-oscillation` — **Discontinuity Set via Oscillation**
   > **Statement.**
   > Let $f:E\to\mathbb{R}$. Then
   > \[
   > D(f):=\{x\in E: f \text{ is discontinuous at } x\}
   > =\{x\in E: \omega(f;x)>0\}
   > =\bigcup_{n=1}^{\infty} \{x\in E: \omega(f;x)\ge 1/n\}.
   > \]

275. () `lem:equivalent-discontinuity-at-a-point` — **Equivalent Formulations of Discontinuity at a Point**
   > **Statement.**
   > Let $E \subseteq \mathbb{R}$, $f : E \to \mathbb{R}$, $x_0 \in E$. The $\varepsilon$-$\delta$, sequential, and neighbourhood formulations of discontinuity at $x_0$ are mutually equivalent.

276. () `thm:algebra-of-lipschitz-functions` — **Algebra of Lipschitz Functions**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$ be Lipschitz on $A$ with constants $K_f$ and $K_g$ respectively, and let $c \in \mathbb{R}$. Then:
   > \begin{enumerate}
   > \item[(a)] $cf$ is Lipschitz with constant $|c|K_f$
   > \item[(b)] $f + g$ and $f - g$ are Lipschitz with constant $K_f + K_g$
   > \item[(c)] If $h : B \to \mathbb{R}$ is Lipschitz on $B$ with constant $K_h$ and $f(A) \subseteq B$, then $h \circ f$ is Lipschitz on $A$ with constant $K_h K_f$
   > \item[(d)] If $|f| \leq M_f$ and $|g| \leq M_g$ on $A$, then $fg$ is Lipschitz with constant $M_g K_f + M_f K_g$
   > \item[(e)] If $|f| \leq M_f$ and $|g(x)| \geq k > 0$ for all $x \in A$, then $f/g$ is Lipschitz with constant $K_f/k + M_f K_g/k^2$
   > \end{enumerate}

277. () `thm:algebra-of-uniform-continuity-bounded` — **Algebra of Uniform Continuity on a Bounded Domain**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ be bounded, and let $f,g:A \to \mathbb{R}$ be uniformly continuous on $A$.
   > \begin{enumerate}[label=(\alph*)]
   > \item The product $x \mapsto f(x)g(x)$ is uniformly continuous on $A$.
   > \item If there exists $k>0$ such that $|g(x)| \ge k$ for all $x \in A$, then the quotient $x \mapsto f(x)/g(x)$ is uniformly continuous on $A$.
   > \end{enumerate}

278. () `thm:algebra-of-uniform-continuity-general` — **Algebra of Uniform Continuity on a General Domain**
   > **Statement.**
   > \begin{enumerate}[label=(\alph*)]
   >   \item For every set $A \subseteq \mathbb{R}$, every pair of functions $f,g : A \to \mathbb{R}$ that are uniformly continuous on $A$, and every scalar $c \in \mathbb{R}$, the functions $f+g$, $f-g$, and $cf$ are uniformly continuous on $A$.
   >   \item There exist a set $A \subseteq \mathbb{R}$ and uniformly continuous functions $f,g : A \to \mathbb{R}$ such that the product $fg$ is not uniformly continuous on $A$.
   > \end{enumerate}

279. () `thm:bilipschitz-inverse-is-lipschitz` — **Inverse of a Bi-Lipschitz Map Is Lipschitz**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ and let $f : A \to f(A)$ be bi-Lipschitz with bounds $\alpha$ and $K$, meaning
   > \[
   >   \alpha|x - u| \leq |f(x) - f(u)| \leq K|x - u|
   >   \quad \text{for all } x, u \in A.
   > \]
   > Then (a)~$f$ is injective, so $f^{-1} : f(A) \to A$ exists; (b)~$f^{-1}$ is Lipschitz with constant $1/\alpha$; (c)~$f^{-1}$ is bi-Lipschitz with bounds $1/K$ and $1/\alpha$.

280. () `thm:heine-cantor` — **Heine-Cantor Theorem**
   > **Statement.**
   > Every function continuous on a closed bounded interval $[a,b]$ is uniformly continuous on $[a,b]$.

281. () `thm:piecewise-linear-approximation` — **Piecewise Linear Approximation**
   > **Statement.**
   > TODO: restate the theorem.

282. () `thm:step-function-approximation` — **Step Function Approximation**
   > **Statement.**
   > Let $f:[a,b]\to\mathbb{R}$ be continuous and let $\varepsilon>0$.
   > Then there exists a step function $s_\varepsilon:[a,b]\to\mathbb{R}$ such that
   > \[
   > \sup_{x\in[a,b]} |f(x)-s_\varepsilon(x)|<\varepsilon.
   > \]

283. () `prop:lipschitz-implies-uc` — **Lipschitz Implies Uniform Continuity**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$ and $f:A \to \mathbb{R}$. If there exists $K \ge 0$ such that $|f(x)-f(y)| \le K |x-y|$ for all $x,y \in A$, then $f$ is uniformly continuous on $A$.

284. () `prop:sequential-uniform-continuity` — **Sequential Characterization of Uniform Continuity**
   > **Statement.**
   > Let $X \subseteq \mathbb{R}$ and $f : X \to \mathbb{R}$.
   > Then $f$ is uniformly continuous on $X$ if and only if
   > for every pair of sequences $(x_n)$, $(y_n)$ in $X$ with
   > $|x_n - y_n| \to 0$, we have $|f(x_n) - f(y_n)| \to 0$.

285. () `prop:uniform-continuity-cauchy` — **Uniform Continuity Preserves Cauchy Sequences**
   > **Statement.**
   > If $f \colon S \to \mathbb{R}$ is uniformly continuous and $(x_{n})$ is a Cauchy sequence in $S$, then $(f(x_{n}))$ is a Cauchy sequence in $\mathbb{R}$.

286. () `thm:constant-multiple-rule` — **Constant Multiple Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable at $c$, then $\alpha f$ is differentiable at $c$, and
   > \[
   > (\alpha f)'(c) = \alpha f'(c).
   > \]

287. () `thm:constant-multiple-rule-interval` — **Constant Multiple Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable on $I$, then $\alpha f$ is differentiable on $I$, and
   > \[
   > (\alpha f)'(x) = \alpha f'(x) \qquad \text{for all } x \in I.
   > \]

288. () `thm:sum-rule` — **Sum Rule**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $c \in I$, and let $f, g : I \to \mathbb{R}$ be differentiable at $c$. Then $f + g$ is differentiable at $c$ and $(f + g)'(c) = f'(c) + g'(c)$.

289. () `thm:finite-linear-combination-rule` — **Finite Linear Combination Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(c) = \sum_{i=1}^{n} \alpha_i f_i'(c).
   > \]

290. () `thm:finite-linear-combination-rule-interval` — **Finite Linear Combination Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

291. () `cor:finite-sum-rule` — **Finite Sum Rule**
   > **Statement.**
   > If $f_1, f_2, \dots, f_n$ are functions on an interval $I$ to $\mathbb{R}$ that are differentiable at $c \in I$, then:
   > \[ \left( \sum_{i=1}^{n} f_i \right)'(c) = \sum_{i=1}^{n} f_i'(c) \]

292. () `cor:finite-sum-rule-interval` — **Finite Sum Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\sum_{i=1}^{n} \alpha_i f_i$ is differentiable on $I$, and
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

293. () `thm:sum-rule-interval` — **Sum Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $f + g$ is differentiable on $I$, and
   > \[
   > (f+g)'(x) = f'(x) + g'(x) \qquad \text{for all } x \in I.
   > \]

294. () `thm:caratheodory-characterization-of-differentiability` — **Carath\'{e}odory Characterization of Differentiability**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $c \in I$. The following are equivalent:
   > \begin{enumerate}[label=(\roman*)]
   > \item $f$ is differentiable at $c$.
   > \item There exists a function $\phi : I \to \mathbb{R}$, continuous at $c$, such that
   > \[
   > f(x) = f(c) + (x-c)\,\phi(x) \qquad \text{for all } x \in I.
   > \]
   > \end{enumerate}
   > In this case, $\phi(c) = f'(c)$.

295. () `thm:derivative-equivalence` — **Equivalence of Definitions of the Derivative at a Point**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. Let $L \in \mathbb{R}$. The following are equivalent:
   > \begin{enumerate}[label=(\roman*)]
   > \item \textbf{(Epsilon--Delta)} $\forall \varepsilon > 0\;\exists \delta > 0\;\forall x \in A\;\bigl(0 < |x-c| < \delta \Rightarrow \left|\tfrac{f(x)-f(c)}{x-c} - L\right| < \varepsilon\bigr)$.
   > \item \textbf{(Neighbourhood)} For every $\varepsilon > 0$, there exists a neighbourhood $V$ of $c$ such that $x \in (A \cap V) \setminus \{c\} \Rightarrow \left|\tfrac{f(x)-f(c)}{x-c} - L\right| < \varepsilon$.
   > \item \textbf{(Sequential)} $\forall (x_n) \subseteq A \setminus \{c\}\;\bigl(x_n \to c \Rightarrow \tfrac{f(x_n)-f(c)}{x_n-c} \to L\bigr)$.
   > \end{enumerate}

296. () `prop:derivative-h-form-equivalence` — **Derivative: $h$-Form Equivalence**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. The following are equivalent:
   > \begin{enumerate}
   > \item $f$ is differentiable at $c$.
   > \item The limit $\displaystyle\lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$ exists.
   > \end{enumerate}
   > In this case, $\displaystyle f'(c) = \lim_{h \to 0} \frac{f(c + h) - f(c)}{h}$.

297. () `prop:derivative-of-a-constant` — **Derivative of a Constant**
   > **Statement.**
   > Let $k\in\mathbb{R}$ and let $f(x)=k$ for all $x\in\mathbb{R}$. Then $f'(c)=0$ for every $c\in\mathbb{R}$.

298. () `prop:derivative-of-the-identity` — **Derivative of the Identity**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, and let $\operatorname{id}_I : I \to \mathbb{R}$ be the identity function defined by $\operatorname{id}_I(x) := x$. Then $\operatorname{id}_I$ is differentiable at every $c \in I$, and $\operatorname{id}_I'(c) = 1$.

299. () `thm:differentiable-implies-continuous` — **Differentiability Implies Continuity**
   > **Statement.**
   > Let $f$ be defined on an open interval $I$ containing $c$. If $f$ is differentiable at $c$, then $f$ is continuous at $c$.

300. () `thm:product-rule` — **Product Rule**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $c \in I$, and let $f, g : I \to \mathbb{R}$ be differentiable at $c$. Then $fg$ is differentiable at $c$ and $(fg)'(c) = f'(c)g(c) + f(c)g'(c)$.

301. () `cor:extended-product-rule` — **Extended Product Rule**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then $\prod_{i=1}^{n} f_i$ is differentiable at $c$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(c)
   > =
   > \sum_{k=1}^{n}
   > f_k'(c) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(c).
   > \]

302. () `cor:extended-product-rule-interval` — **Extended Product Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f_1, \dots, f_n : I \to \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\prod_{i=1}^{n} f_i$ is differentiable on $I$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(x)
   > = \sum_{k=1}^{n} f_k'(x) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(x)
   > \qquad \text{for all } x \in I.
   > \]

303. () `cor:power-rule-special-case` — **Power Rule for Integer Powers of a Function**
   > **Statement.**
   > Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $n \in \mathbb{N}$. If $f$ is differentiable at $c$, then $f^n$ is differentiable at $c$, and
   > \[
   > (f^n)'(c) = n(f(c))^{n-1}f'(c).
   > \]

304. () `cor:power-rule-special-case-interval` — **Power Rule for Integer Powers of a Function on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $n \in \mathbb{N}$. If $f$ is differentiable on $I$, then $f^n$ is differentiable on $I$, and
   > \[
   > (f^n)'(x) = n(f(x))^{n-1}f'(x) \qquad \text{for all } x \in I.
   > \]

305. () `thm:product-rule-interval` — **Product Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $fg$ is differentiable on $I$, and
   > \[
   > (fg)'(x) = f'(x)g(x) + f(x)g'(x) \qquad \text{for all } x \in I.
   > \]

306. () `thm:quotient-rule` — **Quotient Rule**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $c \in I$, and let
   > $f, g : I \to \mathbb{R}$ be differentiable at $c$ with $g(c) \neq 0$. Then
   > $f/g$ is differentiable at $c$ and
   > \[
   >   \left(\frac{f}{g}\right)'(c) = \frac{f'(c)g(c) - f(c)g'(c)}{(g(c))^2}.
   > \]

307. () `thm:quotient-rule-interval` — **Quotient Rule on an Interval**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. Suppose that $f$ and $g$ are differentiable on $I$ and that $g(x) \neq 0$ for all $x \in I$. Then $f/g$ is differentiable on $I$, and
   > \[
   > \left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2} \qquad \text{for all } x \in I.
   > \]

308. () `thm:chain-rule` — **Chain Rule**
   > **Statement.**
   > Let $J, I \subseteq \mathbb{R}$ be open intervals, let $f : J \to \mathbb{R}$ and $g : I \to \mathbb{R}$ be functions with $f(J) \subseteq I$, and let $c \in J$. If $f$ is differentiable at $c$ and $g$ is differentiable at $f(c)$, then $g \circ f$ is differentiable at $c$ and $(g \circ f)'(c) = g'(f(c)) \cdot f'(c)$.

309. () `thm:leibniz-rule` — **Leibniz Rule**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval, let \(x\in I\), and suppose
   > that \(f,g:I\to\mathbb{R}\) are \(n\)-times differentiable on a
   > neighbourhood of \(x\). Then
   > \[
   >   (fg)^{(n)}(x)
   >   =
   >   \sum_{k=0}^{n}\binom{n}{k}f^{(k)}(x)g^{(n-k)}(x).
   > \]

310. () `thm:faa-di-bruno` — **Faa di Bruno's Formula**
   > **Statement.**
   > Under the hypotheses of \hyperref[thm:faa-di-bruno]{Faa di Bruno's Formula},
   > \[
   >   \frac{d^n}{dx^n}f(g(x))
   >   =
   >   \sum_{\sum_{m=1}^{n}mk_m=n}
   >   \frac{n!}{\prod_{m=1}^{n}k_m!\,(m!)^{k_m}}\,
   >   f^{(k)}(g(x))
   >   \prod_{m=1}^{n}\bigl(g^{(m)}(x)\bigr)^{k_m},
   > \]
   > where \(k=\sum_{m=1}^{n}k_m\).

311. () `thm:uniqueness-of-the-derivative` — **Uniqueness of the Derivative**
   > **Statement.**
   > Let $f : A \to \mathbb{R}$ and $c \in A$. If $f$ is differentiable at $c$, its derivative is unique.
   >
   > \smallskip\noindent

312. () `prop:inflection-point-necessary-condition` — **Inflection Point Necessary Condition**
   > **Statement.**
   > Let $f$ have an inflection point at $c$. If $f''$ exists on a neighbourhood of $c$ and is continuous at $c$, then $f''(c)=0$.

313. () `lem:positive-derivative-implies-locally-increasing` — **Positive Derivative Implies Locally Increasing**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose $f$ is differentiable at $c$. If $f'(c) > 0$, then there exists $\delta > 0$ such that $f(x) < f(c)$ for all $x \in I$ with $c - \delta < x < c$, and $f(x) > f(c)$ for all $x \in I$ with $c < x < c + \delta$.

314. () `lem:negative-derivative-implies-locally-decreasing` — **Negative Derivative Implies Locally Decreasing**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose $f$ is differentiable at $c$. If $f'(c) < 0$, then there exists $\delta > 0$ such that $f(x) > f(c)$ for all $x \in I$ with $c - \delta < x < c$, and $f(x) < f(c)$ for all $x \in I$ with $c < x < c + \delta$.

315. () `thm:second-derivative-concavity-test` — **Second-Derivative Concavity Test**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be twice differentiable on $I$. If $f''(x)\leq 0$ for all $x\in I$, then $f$ is concave on $I$.

316. () `thm:second-derivative-convexity-test` — **Second-Derivative Convexity Test**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be twice differentiable on $I$. If $f''(x)\geq 0$ for all $x\in I$, then $f$ is convex on $I$.

317. () `thm:second-derivative-test` — **Second Derivative Test**
   > **Statement.**
   > Let $f$ be twice differentiable in a neighbourhood of $c$, and suppose $f'(c)=0$. If $f''(c)>0$, then $f$ has a strict relative minimum at $c$. If $f''(c)<0$, then $f$ has a strict relative maximum at $c$.

318. () `thm:differentiability-and-one-sided-derivatives` — **Differentiability and One-Sided Derivatives**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval and let $f : I \to \mathbb{R}$. Fix $c \in I$. Then $f$ is differentiable at $c$ if and only if both one-sided derivatives $f'_-(c)$ and $f'_+(c)$ exist and are equal, in which case $f'(c) = f'_-(c) = f'_+(c)$.

319. () `thm:interior-extremum-theorem` — **Interior Extremum Theorem**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$ and is differentiable at $c$, then $f'(c) = 0$.

320. () `thm:necessary-condition-extremum` — **Necessary Condition for an Interior Extremum**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then either $f'(c)$ does not exist, or
   > \[
   > f'(c) = 0.
   > \]

321. () `cor:relative-extremum-necessary-condition` — **Necessary Condition for an Extremum**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then either $f'(c)$ does not exist, or $f'(c) = 0$.

322. () `thm:darboux` — **Darboux's Theorem**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$ and let $f : I \to \mathbb{R}$ be differentiable on $I$. If $k$ is a real number strictly between $f'(a)$ and $f'(b)$, then there exists $c \in (a,b)$ such that $f'(c) = k$.

323. () `thm:smoothness-tower` — **The Smoothness Tower**
   > **Statement.**
   > For every nondegenerate interval \(I\), the inclusions
   > \[
   >   C^0(I)\supseteq C^1(I)\supseteq C^2(I)\supseteq \cdots
   >   \supseteq C^\infty(I)\supseteq C^\omega(I)
   > \]
   > hold, and each displayed inclusion is strict.

324. () `thm:rolles-theorem` — **Rolle's Theorem**
   > **Statement.**
   > Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $f(a) = f(b)$. Then there exists $c \in (a,b)$ such that $f'(c) = 0$.

325. () `thm:cauchy-mean-value-theorem` — **Cauchy Mean Value Theorem**
   > **Statement.**
   > Let \(a,b\in\mathbb{R}\) with \(a<b\). Suppose that \(f,g:[a,b]\to\mathbb{R}\) are continuous on \([a,b]\) and differentiable on \((a,b)\). Then there exists \(c\in(a,b)\) such that
   > \[
   >   (f(b)-f(a))g'(c)=(g(b)-g(a))f'(c).
   > \]
   > If \(g'(x)\neq 0\) for every \(x\in(a,b)\), then \(g(b)\neq g(a)\) and the corresponding quotient identity holds.

326. () `thm:lhopital-infinity-over-infinity` — **L'H\^{o}pital's Rule, \(\infty/\infty\) Form**
   > **Statement.**
   > If \(g(x)\) diverges in magnitude near \(a^+\), \(g'\neq 0\), and \(f'(x)/g'(x)\to L\), then \(f(x)/g(x)\to L\).

327. () `thm:lhopital-zero-over-zero` — **L'H\^{o}pital's Rule, \(0/0\) Form**
   > **Statement.**
   > If \(f,g\) are differentiable near \(a^+\), \(g'\neq 0\), \(f(x)\to 0\), \(g(x)\to 0\), and \(f'(x)/g'(x)\to L\), then \(f(x)/g(x)\to L\).

328. () `thm:mean-value-theorem` — **Mean Value Theorem**
   > **Statement.**
   > Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists $c \in (a,b)$ such that $f'(c) = \dfrac{f(b)-f(a)}{b-a}$.

329. () `thm:nondecreasing-iff-nonneg-derivative` — **Nondecreasing Iff Nonnegative Derivative**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nondecreasing on $I$ if and only if $f'(x) \geq 0$ for all $x \in I$.

330. () `thm:inverse-function-theorem-one-variable` — **Inverse Function Theorem, One Variable**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be open, let \(f:I\to\mathbb{R}\) be \(C^1\), and suppose \(f'(c)\neq 0\). Then \(f\) has a \(C^1\) local inverse near \(c\), and the inverse satisfies \(g'(y)=1/f'(g(y))\).

331. () `cor:inverse-function-derivative` — **Derivative of the Inverse Function**
   > **Statement.**
   > Under the hypotheses of the one-variable Inverse Function Theorem, the local inverse \(g\) satisfies \(g'=1/(f'\circ g)\).

332. () `thm:nonincreasing-iff-nonpos-derivative` — **Nonincreasing Iff Nonpositive Derivative**
   > **Statement.**
   > Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nonincreasing on $I$ if and only if $f'(x) \leq 0$ for all $x \in I$.

333. () `thm:first-derivative-test-maximum` — **First Derivative Test: Relative Maximum**
   > **Statement.**
   > Let $I := [a,b]$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$ with $f$ differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ with $(c-\delta,c+\delta) \subseteq I$ and $f'(x) \geq 0$ for $x \in (c-\delta,c)$ and $f'(x) \leq 0$ for $x \in (c,c+\delta)$, then $f$ has a relative maximum at $c$.

334. () `thm:first-derivative-test-minimum` — **First Derivative Test: Relative Minimum**
   > **Statement.**
   > Let $I := [a,b]$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$ with $f$ differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ with $(c-\delta,c+\delta) \subseteq I$ and $f'(x) \leq 0$ for $x \in (c-\delta,c)$ and $f'(x) \geq 0$ for $x \in (c,c+\delta)$, then $f$ has a relative minimum at $c$.

335. () `thm:zero-derivative-implies-constant` — **Zero Derivative Implies Constant**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$ be a closed interval, and let $f : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If $f'(x) = 0$ for all $x \in (a,b)$, then $f$ is constant on $I$.

336. () `cor:equal-derivatives-constant-difference` — **Equal Derivatives Imply Difference Is Constant**
   > **Statement.**
   > Let $I := [a,b] \subseteq \mathbb{R}$, and let $f, g : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If $f'(x) = g'(x)$ for all $x \in (a,b)$, then there exists $C \in \mathbb{R}$ such that $f(x) = g(x) + C$ for all $x \in I$.

337. () `cor:derivative-bound-implies-lipschitz` — **Derivative Bound Implies Lipschitz**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval and let \(f:I\to\mathbb{R}\) be differentiable on \(I\). If \(|f'(x)|\leq M\) for every \(x\in I\), then
   > \[
   >   |f(x)-f(y)|\leq M|x-y|
   >   \qquad\text{for every }x,y\in I.
   > \]

338. () `cor:bounded-second-derivative-implies-c11` — **Bounded Second Derivative Implies \(C^{1,1}\)**
   > **Statement.**
   > Let \(I\subseteq\mathbb{R}\) be an interval and let \(f\in C^2(I)\). If
   > \(|f''(x)|\leq M\) for all \(x\in I\), then \(f\in C^{1,1}(I)\), and \(f'\)
   > is Lipschitz with constant \(M\).

339. () `thm:c11-placement` — **Placement of \(C^{1,1}\)**
   > **Statement.**
   > For every nondegenerate interval \(I\),
   > \[
   >   C^{1,1}(I)\subsetneq C^1(I),
   > \]
   > and \(C^{1,1}(I)\) is not contained in \(C^2(I)\). If \(K\) is a compact
   > interval, then
   > \[
   >   C^2(K)\subseteq C^{1,1}(K)\subsetneq C^1(K),
   > \]
   > and the first inclusion is strict.

340. () `thm:differential-continuity-criterion` — **Differential Continuity Criterion**
   > **Statement.**
   > If $f$ is differentiable at $c$ in the differential sense, then $f$ is continuous at $c$.

341. () `cor:first-order-peano-remainder` — **First-Order Peano Remainder**
   > **Statement.**
   > Let $f$ be differentiable at $c$. Then $f(c+h)=f(c)+f'(c)h+o(h)$ as $h\to 0$.

342. () `thm:differential-and-derivative-agree` — **Differential and Derivative Agree**
   > **Statement.**
   > The ordinary derivative at $c$ exists if and only if the differential exists at $c$, and then $df_c(h)=f'(c)h$.

343. () `thm:chain-rule-for-differentials` — **Chain Rule for Differentials**
   > **Statement.**
   > If $f$ is differentiable at $c$ and $g$ is differentiable at $f(c)$, then $d(g\circ f)_c=dg_{f(c)}\circ df_c$.

344. () `prop:flat-function` — **The Flat Function: Smooth but Not Analytic**
   > **Statement.**
   > The function \(f(x)=e^{-1/x^2}\) for \(x\neq 0\), with \(f(0)=0\), is smooth on \(\mathbb{R}\), has \(f^{(n)}(0)=0\) for every \(n\), and is not analytic at \(0\).

345. () `thm:linearity-of-the-differential` — **Linearity of the Differential**
   > **Statement.**
   > If $f$ and $g$ are differentiable at $c$ and $\alpha,\beta\in\mathbb{R}$, then $d(\alpha f+\beta g)_c=\alpha\,df_c+\beta\,dg_c$.

346. () `cor:taylor-expansion-peano-remainder` — **Taylor Expansion with Peano Remainder**
   > **Statement.**
   > Let $I\subseteq\mathbb{R}$ be an interval, let $a\in I$, let
   > $n\in\mathbb{N}$, and let $f:I\to\mathbb{R}$ have derivatives up to order
   > $n$ in a neighbourhood of $a$. If $f^{(n)}$ is continuous at $a$, then
   > \[
   >   f(x)
   >   =
   >   \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
   >   +
   >   o\bigl((x-a)^n\bigr)
   >   \qquad\text{as }x\to a.
   > \]
   >
   > \smallskip
   > \noindent

347. () `thm:taylor-theorem-lagrange-remainder` — **Taylor's Theorem with Lagrange Remainder**
   > **Statement.**
   > Let $a,b\in\mathbb{R}$ with $a<b$, let $n\in\mathbb{N}$, and let
   > $f:[a,b]\to\mathbb{R}$. Suppose that $f,f',\ldots,f^{(n)}$ are continuous
   > on $[a,b]$ and that $f^{(n+1)}$ exists on $(a,b)$. Then, for every
   > $x\in(a,b)$, there exists $c$ strictly between $a$ and $x$ such that
   > \[
   >   f(x)
   >   =
   >   \sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k
   >   +
   >   \frac{f^{(n+1)}(c)}{(n+1)!}(x-a)^{n+1}.
   > \]
   >
   > \smallskip
   > \noindent

348. () `thm:uniqueness-of-the-differential` — **Uniqueness of the Differential**
   > **Statement.**
   > If two linear maps give the same first-order expansion up to $o(h)$, then they are equal.

349. () `prop:hyperbolic-addition` — **Addition Formulas for Hyperbolic Functions**
   > **Statement.**
   > For all $x, y \in \mathbb{R}$:
   > \[
   >   \sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y,
   >   \qquad
   >   \cosh(x+y) = \cosh x \cosh y + \sinh x \sinh y.
   > \]
   >
   > \smallskip\noindent

350. () `prop:hyperbolic-pythagorean` — **Hyperbolic Pythagorean Identity**
   > **Statement.**
   > For all $x \in \mathbb{R}$:
   > \[
   >   \cosh^2 x - \sinh^2 x = 1.
   > \]
   >
   > \smallskip\noindent

351. () `prop:tanh-limits` — **Limits of $$**
   > **Statement.**
   > \[
   >   \lim_{x \to +\infty} \tanh x = 1,
   >   \qquad
   >   \lim_{x \to -\infty} \tanh x = -1.
   > \]
   >
   > \smallskip\noindent

352. () `prop:limit-logarithm-fundamental` — **Fundamental Logarithmic Limit**
   > **Statement.**
   > \[
   >   \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1.
   > \]
   >
   > \smallskip\noindent

353. () `prop:exponential-dominates-power` — **Exponential Dominates Every Power**
   > **Statement.**
   > For every $r > 0$:
   > \[
   >   \lim_{x \to \infty} \frac{x^r}{e^x} = 0.
   > \]
   >
   > \smallskip\noindent

354. () `prop:power-dominates-log` — **Every Power Dominates the Logarithm**
   > **Statement.**
   > For every $r > 0$:
   > \[
   >   \lim_{x \to \infty} \frac{\ln x}{x^r} = 0
   >   \qquad\text{and}\qquad
   >   \lim_{x \to 0^+} x^r \ln x = 0.
   > \]
   >
   > \smallskip\noindent

355. () `prop:limit-compound-interest` — **Compound Interest Limit**
   > **Statement.**
   > \[
   >   \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e.
   > \]
   >
   > \smallskip\noindent

356. () `prop:limit-exponential-fundamental` — **Fundamental Exponential Limit**
   > **Statement.**
   > \[
   >   \lim_{x \to 0} \frac{e^x - 1}{x} = 1.
   > \]
   >
   > \smallskip\noindent

357. () `thm:fundamental-trig-limit` — **Fundamental Trigonometric Limit**
   > **Statement.**
   > \[
   >   \lim_{x \to 0} \frac{\sin x}{x} = 1.
   > \]
   >
   > \smallskip\noindent

358. () `prop:pythagorean-identity` — **Pythagorean Identity**
   > **Statement.**
   > For all $x \in \mathbb{R}$:
   > \[
   >   \sin^2 x + \cos^2 x = 1.
   > \]
   >
   > \smallskip\noindent

359. () `prop:trig-addition-formulas` — **Addition Formulas**
   > **Statement.**
   > For all $x, y \in \mathbb{R}$:
   > \[
   >   \sin(x+y) = \sin x \cos y + \cos x \sin y,
   >   \qquad
   >   \cos(x+y) = \cos x \cos y - \sin x \sin y.
   > \]
   >
   > \smallskip\noindent

360. () `prop:limit-one-minus-cos` — **Second Fundamental Trigonometric Limit**
   > **Statement.**
   > \[
   >   \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}.
   > \]
   >
   > \smallskip\noindent

361. () `prop:cauchy-integral-constant` — **Cauchy Integral of a Constant**
   > **Statement.**
   > If \(f(x)=c\) on \([a,b]\), then \(\int_a^b c\,dx=c(b-a)\).

362. () `thm:cauchy-integral-interval-additivity` — **Interval Additivity for the Cauchy Integral**
   > **Statement.**
   > When the relevant Cauchy integrals exist, the integral over \([a,b]\) splits
   > across an intermediate point \(c\).

363. () `thm:cauchy-integral-linearity` — **Linearity of the Cauchy Integral**
   > **Statement.**
   > If \(f\) and \(g\) are Cauchy-integrable, then the integral is linear.

364. () `thm:cauchy-integral-monotonicity` — **Monotonicity of the Cauchy Integral**
   > **Statement.**
   > If \(f\le g\) pointwise and both functions are Cauchy-integrable, then the
   > integral of \(f\) is no larger than the integral of \(g\).

365. () `cor:cauchy-integral-bounds` — **Bounds for the Cauchy Integral**
   > **Statement.**
   > A continuous function whose values lie between \(m\) and \(M\) has integral
   > between \(m(b-a)\) and \(M(b-a)\).

366. () `thm:cauchy-integral-triangle-inequality` — **Triangle Inequality for the Cauchy Integral**
   > **Statement.**
   > If \(f\) and \(|f|\) are Cauchy-integrable, the absolute value of the integral
   > is bounded by the integral of the absolute value.

367. () `thm:cauchy-tag-independence` — **Tag Independence for Continuous Functions**
   > **Statement.**
   > If \(f\) is continuous, all tagged sums have the same limit as the left sums.

368. () `thm:continuous-cauchy-integrable` — **Continuous Functions Are Cauchy-Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb{R}\) is Cauchy-integrable.

369. () `thm:darboux-criterion` — **Darboux Criterion**
   > **Statement.**
   > Darboux integrability is equivalent to making \(U(f,P)-L(f,P)\) arbitrarily
   > small.

370. () `thm:continuous-darboux-integrable` — **Continuous Functions Are Darboux-Integrable**
   > **Statement.**
   > Every continuous function on a compact interval is Darboux-integrable.

371. () `thm:darboux-integrable-absolute-value` — **Absolute Values of Darboux-Integrable Functions**
   > **Statement.**
   > The absolute value of a Darboux-integrable function is Darboux-integrable.

372. () `thm:darboux-integrable-continuous-composition` — **Continuous Images of Darboux-Integrable Functions**
   > **Statement.**
   > Continuous functions preserve Darboux integrability under composition with a
   > bounded Darboux-integrable function.

373. () `thm:darboux-integrable-linear-combinations` — **Sums and Scalar Multiples of Darboux-Integrable Functions**
   > **Statement.**
   > Linear combinations of Darboux-integrable functions are Darboux-integrable.

374. () `thm:darboux-integrable-products` — **Products of Darboux-Integrable Functions**
   > **Statement.**
   > Products of Darboux-integrable functions are Darboux-integrable.

375. () `lem:darboux-refinement-squeeze` — **Darboux Sums Under Refinement**
   > **Statement.**
   > Refinement raises lower sums and lowers upper sums.

376. () `thm:finite-discontinuities-darboux-integrable` — **Bounded Functions with Finitely Many Discontinuities Are Darboux-Integrable**
   > **Statement.**
   > If \(f:[a,b]\to\mathbb R\) is bounded and has only finitely many
   > discontinuities, then \(f\) is Darboux-integrable.

377. () `thm:monotone-darboux-integrable` — **Monotone Functions Are Darboux-Integrable**
   > **Statement.**
   > Every monotone function \(f:[a,b]\to\mathbb R\) is Darboux-integrable.

378. () `thm:riemann-darboux-equivalence` — **Equivalence of Riemann and Darboux Integrability**
   > **Statement.**
   > For bounded functions, Riemann and Darboux integrability are equivalent.

379. () `thm:continuous-hk-integrable` — **Continuous Functions Are Henstock--Kurzweil Integrable**
   > **Statement.**
   > Every continuous function \(f:[a,b]\to\mathbb{R}\) is Henstock--Kurzweil
   > integrable.

380. () `lem:cousin` — **Cousin's Lemma**
   > **Statement.**
   > For every gauge \(\delta\) on \([a,b]\), there exists a \(\delta\)-fine tagged
   > partition of \([a,b]\).

381. () `thm:hk-fundamental-theorem` — **Fundamental Theorem for the Henstock--Kurzweil Integral**
   > **Statement.**
   > If \(F\) is differentiable on \([a,b]\) and \(F'=f\), then
   > \[
   >   (\mathrm{HK})\int_a^b f=F(b)-F(a).
   > \]

382. () `lem:hk-straddle` — **Straddle Lemma**
   > **Statement.**
   > If \(F\) is differentiable at \(\xi\) with \(F'(\xi)=f(\xi)\), then the
   > one-slab linearization error across any sufficiently small interval straddling
   > \(\xi\) is bounded by \(\varepsilon\) times its length.

383. () `thm:riemann-integrable-implies-hk-integrable` — **Riemann Integrable Implies Henstock--Kurzweil Integrable**
   > **Statement.**
   > If \(f\) is Riemann-integrable on \([a,b]\), then \(f\) is
   > Henstock--Kurzweil integrable on \([a,b]\), with the same value.

384. () `thm:mcshane-equals-lebesgue` — **McShane Integrability Equals Lebesgue Integrability**
   > **Statement.**
   > For real-valued functions on a compact interval,
   > \[
   >   \mathcal{McShane}[a,b]=\mathcal L[a,b],
   > \]
   > with agreement of integral values.

385. () `thm:riemann-mcshane-hk-inclusions` — **Riemann Integrable Implies McShane Integrable Implies Henstock--Kurzweil Integrable**
   > **Statement.**
   > On a compact interval,
   > \[
   >   \mathcal R[a,b]\subseteq \mathcal M[a,b]\subseteq \mathcal{HK}[a,b],
   > \]
   > with agreement of integral values.

386. () `thm:lebesgue-criterion-riemann-integrability` — **Lebesgue Criterion for Riemann Integrability**
   > **Statement.**
   > A bounded function \(f:[a,b]\to\mathbb R\) is Riemann-integrable if and only
   > if its discontinuity set has measure zero.

387. () `lem:common-refinement-partitions` — **Common Refinement of Two Partitions**
   > **Statement.**
   > If \(P\) and \(P'\) are partitions of \([a,b]\), then \(P\cup P'\), ordered
   > in increasing order, is a partition of \([a,b]\) that refines both.

388. () `thm:continuous-riemann-integrable` — **Continuous Functions Are Riemann-Integrable**
   > **Statement.**
   > Every continuous function on a compact interval is Riemann-integrable.

389. () `thm:riemann-cauchy-criterion` — **Cauchy Criterion for Riemann Integrability**
   > **Statement.**
   > A bounded function is Riemann-integrable if and only if sufficiently fine
   > tagged sums are mutually close.

390. () `thm:riemann-integral-interval-additivity` — **Interval Additivity for the Riemann Integral**
   > **Statement.**
   > Riemann integrability and the integral value split across an intermediate
   > point.

391. () `thm:riemann-integral-linearity` — **Linearity of the Riemann Integral**
   > **Statement.**
   > The Riemann integral is linear on its domain of integrable functions.

392. () `thm:riemann-integral-monotonicity` — **Monotonicity of the Riemann Integral**
   > **Statement.**
   > If \(f\le g\) pointwise and both functions are Riemann-integrable, then the
   > integral of \(f\) is no larger than the integral of \(g\).

393. () `thm:riemann-integral-triangle-inequality` — **Triangle Inequality for the Riemann Integral**
   > **Statement.**
   > The Riemann integral satisfies the usual absolute-value bound.

394. () `prop:monotone-bounded-variation` — **Monotone Functions Have Bounded Variation**
   > **Statement.**
   > Every monotone function on \([a,b]\) has bounded variation.

395. () `thm:rs-bilinearity` — **Bilinearity of the Riemann--Stieltjes Integral**
   > **Statement.**
   > Whenever the displayed integrals exist, the Riemann--Stieltjes integral is
   > linear in the integrand and in the integrator.

396. () `thm:rs-c1-reduction` — **Reduction to Riemann Integration for a \(C^1\) Integrator**
   > **Statement.**
   > If the integrator is \(C^1\), then the Riemann--Stieltjes integral reduces to
   > an ordinary Riemann integral against \(\alpha'\).

397. () `thm:rs-continuous-bv-existence` — **Continuous Integrand and BV Integrator**
   > **Statement.**
   > If \(f\) is continuous and \(\alpha\) has bounded variation, then \(\int f\,d\alpha\) exists.

398. () `thm:rs-integration-by-parts` — **Riemann--Stieltjes Integration by Parts**
   > **Statement.**
   > Under the Riemann--Stieltjes convention, existence of one integral implies
   > existence of the paired integral and their sum is the endpoint product
   > difference.

399. () `thm:rs-interval-additivity` — **Interval Additivity for the Riemann--Stieltjes Integral**
   > **Statement.**
   > When the relevant integrals exist, the Riemann--Stieltjes integral over
   > \([a,b]\) splits across an intermediate point \(c\).

400. () `thm:rs-step-integrator-finite-sum` — **Step Integrators Give Finite Sums**
   > **Statement.**
   > A Riemann--Stieltjes integral against a finite-step integrator is a finite
   > weighted sum over the jump points, provided the integrand is continuous there.
