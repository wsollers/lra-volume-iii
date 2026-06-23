# Volume III Proofs To Do

Proof-writing order is dependency-first among active TODO proof labels, with the generated proof/status report order used as the stable tie-breaker.
Use `✅` to record completion after the canonical proof file has both proof bodies populated and validated.

Open proofs to do: 247
Completed in this tracker: 4

1. (✅) `prop:every-element-lies-below-the-supremum` — **Every Element Lies Below the Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $s=\sup A$. Then $x\le s$ for every $x\in A$.

2. (✅) `thm:infimum-less-than-supremum` — **Infimum Is Less Than or Equal to the Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty, bounded below, and bounded above. Then $\inf A\le \sup A$.

3. (✅) `prop:maximum-implies-supremum` — **Maximum Implies Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ and let $m\in A$. If $m$ is a maximum of $A$, then $m=\sup A$.

4. (✅) `thm:negation-exchange-sup-inf` — **Negation Exchanges Supremum and Infimum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded below. Then $-A=\{-a:a\in A\}$ is bounded above and
   > \[
   >  \sup(-A)=-\inf A.
   > \]

5. () `thm:scalar-mult-negative` — **Scalar Multiplication by a Negative Scalar**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded below, and let $k<0$. Then
   > \[
   >  \sup(kA)=k\inf A,
   >  \qquad
   >  kA=\{ka:a\in A\}.
   > \]

6. () `thm:scalar-mult-positive` — **Scalar Multiplication by a Positive Scalar**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $k>0$. Then
   > \[
   >  \sup(kA)=k\sup A,
   >  \qquad
   >  kA=\{ka:a\in A\}.
   > \]

7. () `lem:subset-inclusion-preserves-upper-bounds` — **Subset Inclusion Preserves Upper Bounds**
   > **Statement.** Let $A\subseteq B\subseteq\mathbb{R}$. If $u$ is an upper bound of $B$, then $u$ is an upper bound of $A$.

8. () `prop:suprema-ambient-set` — **Suprema Depend on the Ambient Set**
   > **Statement.** Let $A\subseteq S\subseteq S'$ be subsets of an ordered set. The supremum of $A$ relative to $S$, if it exists, need not agree with the supremum of $A$ relative to $S'$.

9. () `thm:ambient-existence-supremum` — **Ambient Existence of Supremum**
   > **Statement.** There are ordered sets $S\subseteq S'$ and a subset $A\subseteq S$ such that $A$ has a supremum relative to $S'$ but has no supremum relative to $S$.

10. () `lem:rational-gap-suprema` — **Rational Gap Example for Suprema**
   > **Statement.** Let
   > \[
   >  A=\{q\in\mathbb{Q}:q^2<2\}.
   > \]
   > Then $A$ is nonempty and bounded above in $\mathbb{Q}$, but $A$ has no supremum relative to $\mathbb{Q}$.

11. () `thm:supremum-absolute-value-image` — **Supremum of the Absolute-Value Image**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \sup |A|=\max\{|\sup A|,|\inf A|\},
   >  \qquad
   >  |A|=\{|a|:a\in A\}.
   > \]

12. () `thm:supremum-dilation` — **Supremum of a Dilation**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded, and let $\lambda\in\mathbb{R}$. Then
   > \[
   >  \sup(\lambda A)=\max\{\lambda\sup A,\lambda\inf A\},
   >  \qquad
   >  \lambda A=\{\lambda a:a\in A\}.
   > \]

13. () `prop:supremum-in-the-set-is-the-maximum` — **Supremum in the Set Is the Maximum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ and let $s=\sup A$. If $s\in A$, then $s$ is a maximum of $A$.

14. () `thm:supremum-is-monotone-under-inclusion` — **Supremum Is Monotone Under Inclusion**
   > **Statement.** Let $A,B\subseteq\mathbb{R}$ be nonempty sets that are bounded above. If $A\subseteq B$, then $\sup A\le \sup B$.

15. () `thm:supremum-sum-set` — **Supremum of a Sum Set**
   > **Statement.** Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. Then
   > \[
   >  \sup(A+B)=\sup A+\sup B,
   >  \qquad
   >  A+B=\{a+b:a\in A,\ b\in B\}.
   > \]

16. () `prop:bounds-sum-set` — **Bounds for Suprema and Infima Under Set Addition**
   > **Statement.** Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded. Then
   > \[
   >  \inf A+\inf B\le \inf(A+B)
   >  \qquad\text{and}\qquad
   >  \sup(A+B)\le \sup A+\sup B.
   > \]

17. () `thm:supremum-difference-set` — **Supremum of a Difference Set**
   > **Statement.** Let $A,B\subseteq\mathbb{R}$ be nonempty, with $A$ bounded above and $B$ bounded below. Then
   > \[
   >  \sup(A-B)=\sup A-\inf B,
   >  \qquad
   >  A-B=\{a-b:a\in A,\ b\in B\}.
   > \]

18. () `thm:translation-invariance-supremum` — **Translation Invariance of the Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $c\in\mathbb{R}$. Then
   > \[
   >  \sup(A+c)=\sup A+c,
   >  \qquad
   >  A+c=\{a+c:a\in A\}.
   > \]

19. () `prop:uniqueness-of-the-maximum` — **Uniqueness of the Maximum**
   > **Statement.** Let $A\subseteq\mathbb{R}$. If $m_1$ and $m_2$ are both maximum elements of $A$, then $m_1=m_2$.

20. () `prop:uniqueness-of-the-supremum` — **Uniqueness of the Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$. If $s_1$ and $s_2$ are both suprema of $A$, then $s_1=s_2$.

21. () `prop:upper-bound-comparison-with-the-supremum` — **Upper Bound Comparison with the Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ be nonempty and bounded above, and let $s=\sup A$. For $u\in\mathbb{R}$, the number $u$ is an upper bound of $A$ if and only if $s\le u$.

22. () `prop:order-comparison-of-suprema` — **Order Comparison of Suprema**
   > **Statement.** Let $A,B\subseteq\mathbb{R}$ be nonempty and bounded above. If for every $x\in A$ there exists $y\in B$ such that $x\le y$, then $\sup A\le \sup B$.

23. () `prop:upper-bounds-ambient-order` — **Upper Bounds Depend on the Ambient Order**
   > **Statement.** Let $(S,\le_S)$ and $(T,\le_T)$ be ordered sets, and let $A\subseteq S\cap T$. Whether $u$ is an upper bound of $A$ must be interpreted relative to the chosen ambient order.

24. () `thm:lub-property-implies-existence-of-suprema` — **Least Upper Bound Property Implies Existence of Suprema**
   > **Statement.** Let $S$ be an ordered set with the least upper bound property. If $A\subseteq S$ is nonempty and bounded above in $S$, then $A$ has a supremum in $S$.

25. () `prop:upper-bound-property-of-supremum` — **Upper Bound Property of Supremum**
   > **Statement.** Let $A\subseteq\mathbb{R}$ and let $s=\sup A$. Then $x\le s$ for every $x\in A$.

26. () `thm:archimedean-property` — **Archimedean Property**
   > **Statement.** For every real number $x$, there exists a natural number $n$ such that $n>x$.

27. () `cor:archimedean-reciprocal` — **Archimedean Reciprocal Corollary**
   > **Statement.** For every $x>0$ and every $y\in\mathbb{R}$, there exists $n\in\mathbb{N}$ such that $nx>y$.

28. () `thm:density-of-rationals-in-reals` — **Density of the Rational Numbers in $ $**
   > **Statement.** For every $a,b\in\mathbb{R}$ with $a<b$, there exists $q\in\mathbb{Q}$ such that $a<q<b$.

29. () `thm:density-of-irrationals-in-reals` — **Density of the Irrational Numbers in $ $**
   > **Statement.** For every $a,b\in\mathbb{R}$ with $a<b$, there exists $s\in\mathbb{R}\setminus\mathbb{Q}$ such that $a<s<b$.

30. () `cor:every-open-interval-contains-rational-and-irrational` — **Rational and Irrational Points in Every Open Interval**
   > **Statement.** Every open interval in $\mathbb{R}$ contains both a rational number and an irrational number.

31. () `thm:nested-interval-theorem` — **Nested Interval Property**
   > **Statement.** Let $(I_n)$ be a sequence of nonempty closed intervals in $\mathbb{R}$. If $I_{n+1}\subseteq I_n$ for every $n\in\mathbb{N}$, then
   > \[
   >  \bigcap_{n=1}^{\infty} I_n\neq\varnothing.
   > \]

32. () `thm:bernstein-approximation` — **Bernstein Approximation Theorem**
   > **Statement.** Let $f:[0,1]\to\mathbb{R}$ be continuous, and for each $n\in\mathbb{N}$ let $B_n$ denote the $n$th Bernstein polynomial of $f$. Then for every $\varepsilon>0$ there exists $n_\varepsilon\in\mathbb{N}$ such that $\|f-B_n\|_\infty<\varepsilon$ for all $n\ge n_\varepsilon$. \hyperref[prf:bernstein-approximation]{Go to proof.}

33. () `thm:weierstrass-approximation` — **Weierstrass Approximation Theorem**
   > **Statement.** Let $f:[a,b]\to\mathbb{R}$ be continuous. For every $\varepsilon>0$ there exists a polynomial $p_\varepsilon\in\mathbb{R}[x]$ such that $\|f-p_\varepsilon\|_{\infty,[a,b]}<\varepsilon$.

34. () `thm:cousins-theorem` — **Cousin's Theorem**
   > **Statement.** Every gauge $\delta:[a,b]\to(0,\infty)$ on a closed interval $[a,b]$
   > admits a $\delta$-fine tagged partition of $[a,b]$.

35. () `lem:every-point-covered-by-tag` — **Every Point Is Covered by a Tag**
   > **Statement.** Let $\dot{\mathcal{P}}=\{([x_{i-1},x_i],t_i)\}_{i=1}^n$ be a tagged partition of $[a,b]$ that is $\delta$-fine on $[a,b]$, and let $x\in[a,b]$. Then there exists $i\in\{1,\ldots,n\}$ such that $|x-t_i|<\delta(t_i)$.

36. () `thm:bolzano-intermediate-value` — **Bolzano's Intermediate Value Theorem**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f \colon I \to \mathbb{R}$ be continuous on $I$, and choose $a,b \in I$ with $f(a) < k < f(b)$. Then there exists $c \in I$ such that $\min\{a,b\} < c < \max\{a,b\}$ and $f(c) = k$. \hyperref[prf:bolzano-intermediate-value]{Go to proof.}

37. () `thm:boundedness-theorem` — **Boundedness Theorem**
   > **Statement.** Let $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then there exists $M>0$ such that $|f(x)|\le M$ for every $x\in[a,b]$.

38. () `thm:darboux-property` — **Darboux Property**
   > **Statement.** Let $a,b\in\mathbb{R}$ satisfy $a<b$, let $f:[a,b]\to\mathbb{R}$ be continuous, and fix $c\in\mathbb{R}$. If $f(x)\neq c$ for every $x\in[a,b]$, then either $f(x)>c$ for all $x\in[a,b]$ or $f(x)<c$ for all $x\in[a,b]$.

39. () `thm:extreme-value-theorem` — **Extreme Value Theorem**
   > **Statement.** Let $a,b \in \mathbb{R}$ with $a<b$, and let $f:[a,b] \to \mathbb{R}$ be continuous. There exist points $x_m,x_M \in [a,b]$ such that $f(x_m) \le f(x) \le f(x_M)$ for every $x \in [a,b]$. Equivalently, $f$ attains both an absolute maximum and an absolute minimum on $[a,b]$.

40. () `thm:image-of-closed-bounded-interval` — **Image of Closed Bounded Interval Is Closed Bounded Interval**
   > **Statement.** Let $f:[a,b]\to\mathbb{R}$ be continuous. Then $f([a,b])=[\min_{[a,b]} f,\max_{[a,b]} f]$.

41. () `thm:location-of-roots` — **Location of Roots**
   > **Statement.** Let $a,b \in \mathbb{R}$ with $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous. If either $f(a)<0<f(b)$ or $f(a)>0>f(b)$, then there exists $c\in(a,b)$ such that $f(c)=0$.

42. () `thm:preservation-of-intervals` — **Preservation of Intervals**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval and let $f:I \to \mathbb{R}$ be continuous. Then $f(I)$ is an interval.

43. () `prop:continuous-injective-iff-strictly-monotone` — **Continuous Injective Is Strictly Monotone**
   > **Statement.** Let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then $f$ is injective if and only if $f$ is strictly monotone on $[a,b]$.

44. () `thm:continuous-inverse-theorem` — **Continuous Inverse Theorem**
   > **Statement.** Let $I\subseteq\mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be strictly monotone and continuous on $I$. Then the inverse function $f^{-1}:f(I)\to I$ exists, is strictly monotone, and is continuous on $f(I)$.

45. () `prop:limsup-geq-liminf-function` — **$ $**
   > **Statement.** Let $A\subseteq \mathbb{R}$, let $x_0$ be a limit point of $A$, and let $f:A\to\mathbb{R}$. Then
   > \[
   > \limsup_{x\to x_0} f(x) \ge \liminf_{x\to x_0} f(x).
   > \]

46. () `prop:limsup-liminf-limit-criterion` — **Limit Exists iff $ = $**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, let $x_0$ be a limit point of $A$ with $x_0 \in \mathbb{R}$, and let $L \in \mathbb{R}$. Then $\lim_{x \to x_0} f(x)$ exists and equals $L$ if and only if $\limsup_{x \to x_0} f(x) = \liminf_{x \to x_0} f(x) = L$.

47. () `prop:monotone-discontinuities-first-kind` — **Discontinuities of a Monotone Function Are of First Kind**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f:I \to \mathbb{R}$ be monotone, and let $a \in I$ be such that there exist points of $I$ strictly less and strictly greater than $a$. If $f$ is discontinuous at $a$, then both one-sided limits $\lim_{x\uparrow a} f(x)$ and $\lim_{x\downarrow a} f(x)$ exist in $\mathbb{R}$.

48. () `cor:jump-intervals-for-monotone-discontinuities` — **Jump Intervals Are Disjoint**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval and let $f:I \to \mathbb{R}$ be nondecreasing. If $a,b \in I$ are distinct points of discontinuity of $f$, then the open intervals $(f(a^-),f(a^+))$ and $(f(b^-),f(b^+))$ are disjoint.

49. () `thm:monotone-one-sided-limits` — **One-Sided Limits of Monotone Functions**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $c$ be interior to $I$, and let $f:I\to\mathbb{R}$ be increasing. Define
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

50. () `cor:monotone-continuity-criterion` — **Continuity Criterion for Monotone Functions**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f:I \to \mathbb{R}$ be monotone increasing, and let $c$ be an interior point of $I$. Then $f$ is continuous at $c$ if and only if its one-sided limits satisfy $f(c^-)=f(c)=f(c^+)$, where $f(c^-)=\lim_{x\to c^-} f(x)$ and $f(c^+)=\lim_{x\to c^+} f(x)$.

51. () `thm:monotone-discontinuities-countable` — **Discontinuities of a Monotone Function Are Countable**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval and let $f:I\to\mathbb{R}$ be monotone. Then the set $D_f \coloneqq \{c \in I : f \text{ is discontinuous at } c\}$ is at most countable. \hyperref[prf:monotone-discontinuities-countable]{Go to proof.}

52. () `cor:monotone-continuous-on-dense-set` — **Monotone Function Is Continuous on a Dense Set**
   > **Statement.** Let $f:[a,b]\to\mathbb{R}$ be monotone. Then the set $\{x\in[a,b]:f \text{ is continuous at } x\}$ is dense in $[a,b]$.

53. () `thm:continuity-iff-zero-oscillation` — **Continuity Characterised by Oscillation**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f \colon A \to \mathbb{R}$, and let $c \in A$. Then $f$ is continuous at $c$ if and only if $\omega(f;c)=0$.

54. () `prop:discontinuity-set-via-oscillation` — **Discontinuity Set via Oscillation**
   > **Statement.** Let $f:E\to\mathbb{R}$. Then
   > \[
   > D(f):=\{x\in E: f \text{ is discontinuous at } x\}
   > =\{x\in E: \omega(f;x)>0\}
   > =\bigcup_{n=1}^{\infty} \{x\in E: \omega(f;x)\ge 1/n\}.
   > \]

55. () `lem:equivalent-discontinuity-at-a-point` — **Equivalent Formulations of Discontinuity at a Point**
   > **Statement.** Let $A\subseteq \mathbb{R}$, let $f:A\to\mathbb{R}$, and let $c\in A$. The following are equivalent:
   > - $c$ is a point of discontinuity in the $\varepsilon$-$\delta$ sense.
   > - $c$ is a sequential point of discontinuity.
   > - $c$ is a neighbourhood point of discontinuity.

56. () `thm:algebra-of-lipschitz-functions` — **Algebra of Lipschitz Functions**
   > **Statement.** Let $A\subseteq \mathbb{R}$ and let $f,g:A\to\mathbb{R}$ be Lipschitz with constants $K_f,K_g\ge 0$ respectively.
   > - [label=(\alph*)]
   > - For every $c\in\mathbb{R}$, the function $cf$ is Lipschitz on $A$ with constant $|c|K_f$.
   > - The functions $f+g$ and $f-g$ are Lipschitz on $A$ with constant $K_f+K_g$.
   > - If $B\subseteq\mathbb{R}$, $h:B\to\mathbb{R}$ is Lipschitz with constant $K_h\ge 0$, and $f(A)\subseteq B$, then $h\circ f$ is Lipschitz on $A$ with constant $K_hK_f$.
   > - If $|f(x)|\le M_f$ and $|g(x)|\le M_g$ for all $x\in A$, then $fg$ is Lipschitz on $A$ with constant $M_gK_f+M_fK_g$.
   > - If $|f(x)|\le M_f$ for all $x\in A$, if $|g(x)|\ge k>0$ for all $x\in A$, and if $g$ is Lipschitz on $A$ with constant $K_g$, then $f/g$ is Lipschitz on $A$ with constant $K_f/k + M_fK_g/k^2$.

57. () `thm:algebra-of-uniform-continuity-bounded` — **Algebra of Uniform Continuity on a Bounded Domain**
   > **Statement.** Let $A \subseteq \mathbb{R}$ be bounded, and let $f,g:A \to \mathbb{R}$ be uniformly continuous on $A$.
   > - [label=(\alph*)]
   > - The product $x \mapsto f(x)g(x)$ is uniformly continuous on $A$.
   > - If there exists $k>0$ such that $|g(x)| \ge k$ for all $x \in A$, then the quotient $x \mapsto f(x)/g(x)$ is uniformly continuous on $A$.

58. () `thm:algebra-of-uniform-continuity-general` — **Algebra of Uniform Continuity on a General Domain**
   > **Statement.** - [label=(\alph*)]
   > - For every set $A \subseteq \mathbb{R}$, every pair of functions $f,g : A \to \mathbb{R}$ that are uniformly continuous on $A$, and every scalar $c \in \mathbb{R}$, the functions $f+g$, $f-g$, and $cf$ are uniformly continuous on $A$.
   > - There exist a set $A \subseteq \mathbb{R}$ and uniformly continuous functions $f,g : A \to \mathbb{R}$ such that the product $fg$ is not uniformly continuous on $A$.

59. () `thm:bilipschitz-inverse-is-lipschitz` — **Inverse of a Bi-Lipschitz Map Is Lipschitz**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f:A \to \mathbb{R}$, and suppose there exist constants $\alpha,K>0$ such that
   > $\alpha |x-y| \le |f(x)-f(y)| \le K |x-y|$ for all $x,y \in A$. Then $f$ is injective, the inverse mapping $f^{-1}:f(A) \to A$ is well defined, and
   > \[
   > \frac{1}{K}|u-v| \le |f^{-1}(u)-f^{-1}(v)| \le \frac{1}{\alpha}|u-v|
   > \quad\text{for all } u,v \in f(A).
   > \]

60. () `thm:heine-cantor` — **Heine--Cantor Theorem**
   > **Statement.** Let $a,b \in \mathbb{R}$ with $a<b$ and let $f:[a,b]\to\mathbb{R}$ be continuous on $[a,b]$. Then $f$ is uniformly continuous on $[a,b]$.

61. () `thm:piecewise-linear-approximation` — **Piecewise Linear Approximation**
   > **Statement.** Let $f\colon[a,b]\to\mathbb{R}$ be continuous and let $\varepsilon>0$. Then there exists a continuous piecewise linear function $\ell_\varepsilon\colon[a,b]\to\mathbb{R}$ such that $\sup_{x\in[a,b]}|f(x)-\ell_\varepsilon(x)|<\varepsilon$. \hyperref[prf:piecewise-linear-approximation]{Go to proof.}

62. () `thm:step-function-approximation` — **Step Function Approximation**
   > **Statement.** Let $f:[a,b]\to\mathbb{R}$ be continuous and let $\varepsilon>0$.
   > Then there exists a step function $s_\varepsilon:[a,b]\to\mathbb{R}$ such that
   > \[
   > \sup_{x\in[a,b]} |f(x)-s_\varepsilon(x)|<\varepsilon.
   > \]

63. () `prop:lipschitz-implies-uc` — **Lipschitz Implies Uniform Continuity**
   > **Statement.** Let $A \subseteq \mathbb{R}$ and $f:A \to \mathbb{R}$. If there exists $K \ge 0$ such that $|f(x)-f(y)| \le K |x-y|$ for all $x,y \in A$, then $f$ is uniformly continuous on $A$.

64. () `prop:sequential-uniform-continuity` — **Sequential Characterization of Uniform Continuity**
   > **Statement.** Let $A \subseteq \mathbb{R}$ and let $f:A \to \mathbb{R}$. Then $f$ is uniformly continuous on $A$ if and only if for every pair of sequences $(x_n)$ and $(y_n)$ in $A$ with $\lim_{n \to \infty} (x_n - y_n) = 0$ we have $\lim_{n \to \infty} (f(x_n) - f(y_n)) = 0$.

65. () `prop:uniform-continuity-cauchy` — **Uniform Continuity Preserves Cauchy Sequences**
   > **Statement.** Let $S \subseteq \mathbb{R}$, let $f:S \to \mathbb{R}$, and let $(x_n)$ be a sequence in $S$. If $f$ is uniformly continuous on $S$ and $(x_n)$ is a Cauchy sequence in $S$, then $(f(x_n))$ is a Cauchy sequence in $\mathbb{R}$.

66. () `thm:constant-multiple-rule` — **Constant Multiple Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable at $c$, then $\alpha f$ is differentiable at $c$, and
   > \[
   > (\alpha f)'(c) = \alpha f'(c).
   > \]

67. () `thm:constant-multiple-rule-interval` — **Constant Multiple Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $\alpha \in \mathbb{R}$. If $f$ is differentiable on $I$, then $\alpha f$ is differentiable on $I$, and
   > \[
   > (\alpha f)'(x) = \alpha f'(x) \qquad \text{for all } x \in I.
   > \]

68. () `thm:sum-rule` — **Sum Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If $f$ and $g$ are differentiable at $c$, then $f + g$ is differentiable at $c$, and
   > \[
   > (f+g)'(c) = f'(c) + g'(c).
   > \]

69. () `thm:finite-linear-combination-rule` — **Finite Linear Combination Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(c) = \sum_{i=1}^{n} \alpha_i f_i'(c).
   > \]

70. () `thm:finite-linear-combination-rule-interval` — **Finite Linear Combination Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

71. () `cor:finite-sum-rule` — **Finite Sum Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then $\sum_{i=1}^{n} \alpha_i f_i$ is differentiable at $c$, and
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(c) = \sum_{i=1}^{n} \alpha_i f_i'(c).
   > \]

72. () `cor:finite-sum-rule-interval` — **Finite Sum Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f_1, \dots, f_n : I \to \mathbb{R}$, and let $\alpha_1, \dots, \alpha_n \in \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\sum_{i=1}^{n} \alpha_i f_i$ is differentiable on $I$, and
   > \[
   > \left(\sum_{i=1}^{n} \alpha_i f_i\right)'(x) = \sum_{i=1}^{n} \alpha_i f_i'(x) \qquad \text{for all } x \in I.
   > \]

73. () `thm:sum-rule-interval` — **Sum Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $f + g$ is differentiable on $I$, and
   > \[
   > (f+g)'(x) = f'(x) + g'(x) \qquad \text{for all } x \in I.
   > \]

74. () `thm:caratheodory-characterization-of-differentiability` — **Carath\' e odory Characterization of Differentiability**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $c \in I$. The following are equivalent:
   > - [label=(\roman*)]
   > - $f$ is differentiable at $c$.
   > - There exists a function $\phi : I \to \mathbb{R}$, continuous at $c$, such that
   > \[
   > f(x) = f(c) + (x-c)\,\phi(x) \qquad \text{for all } x \in I.
   > \]
   > In this case, $\phi(c) = f'(c)$.

75. () `thm:derivative-equivalence` — **Equivalence of Definitions of the Derivative at a Point**
   > **Statement.** Let $f : A \to \mathbb{R}$ and $c \in A$ be a limit point of $A$. The following are equivalent:
   > - $f$ is differentiable at $c$ in the $\varepsilon$-$\delta$ sense with derivative $L$.
   > - $f$ is differentiable at $c$ in the topological sense with derivative $L$.
   > - $f$ is differentiable at $c$ in the sequential sense with derivative $L$.

76. () `prop:derivative-h-form-equivalence` — **Derivative: $h$-Form Equivalence**
   > **Statement.** Let $f : A \to \mathbb{R}$ and $c \in \operatorname{int}(A)$. Then $f$ is differentiable at $c$ with derivative $L$ if and only if
   > \[
   > \lim_{h \to 0} \frac{f(c+h) - f(c)}{h} = L.
   > \]

77. () `prop:derivative-of-the-identity` — **Derivative of the Identity**
   > **Statement.** Let $f(x) = x$ for all $x \in \mathbb{R}$. Then $f'(c) = 1$ for every $c \in \mathbb{R}$.

78. () `thm:differentiable-implies-continuous` — **Differentiable Implies Continuous**
   > **Statement.** Let $f : A \to \mathbb{R}$ and $c \in A$. If $f$ is differentiable at $c$, then $f$ is continuous at $c$.

79. () `thm:product-rule` — **Product Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If $f$ and $g$ are differentiable at $c$, then $fg$ is differentiable at $c$, and
   > \[
   > (fg)'(c) = f'(c)g(c) + f(c)g'(c).
   > \]

80. () `cor:extended-product-rule` — **Extended Product Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f_1, \dots, f_n : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. If each $f_i$ is differentiable at $c$, then $\prod_{i=1}^{n} f_i$ is differentiable at $c$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(c)
   > =
   > \sum_{k=1}^{n}
   > f_k'(c) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(c).
   > \]

81. () `cor:extended-product-rule-interval` — **Extended Product Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f_1, \dots, f_n : I \to \mathbb{R}$. If each $f_i$ is differentiable on $I$, then $\prod_{i=1}^{n} f_i$ is differentiable on $I$, and
   > \[
   > \left(\prod_{i=1}^{n} f_i\right)'(x)
   > = \sum_{k=1}^{n} f_k'(x) \prod_{\substack{i=1\\i\neq k}}^{n} f_i(x)
   > \qquad \text{for all } x \in I.
   > \]

82. () `cor:power-rule-special-case` — **Power Rule for Integer Powers of a Function**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f : A \to \mathbb{R}$, let $c \in A$ be a limit point of $A$, and let $n \in \mathbb{N}$. If $f$ is differentiable at $c$, then $f^n$ is differentiable at $c$, and
   > \[
   > (f^n)'(c) = n(f(c))^{n-1}f'(c).
   > \]

83. () `cor:power-rule-special-case-interval` — **Power Rule for Integer Powers of a Function on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, and let $n \in \mathbb{N}$. If $f$ is differentiable on $I$, then $f^n$ is differentiable on $I$, and
   > \[
   > (f^n)'(x) = n(f(x))^{n-1}f'(x) \qquad \text{for all } x \in I.
   > \]

84. () `thm:product-rule-interval` — **Product Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. If $f$ and $g$ are differentiable on $I$, then $fg$ is differentiable on $I$, and
   > \[
   > (fg)'(x) = f'(x)g(x) + f(x)g'(x) \qquad \text{for all } x \in I.
   > \]

85. () `thm:quotient-rule` — **Quotient Rule**
   > **Statement.** Let $A \subseteq \mathbb{R}$, let $f, g : A \to \mathbb{R}$, and let $c \in A$ be a limit point of $A$. Suppose that $f$ and $g$ are differentiable at $c$ and that $g(c) \neq 0$. Then $f/g$ is differentiable at $c$, and
   > \[
   > \left(\frac{f}{g}\right)'(c) = \frac{f'(c)g(c) - f(c)g'(c)}{(g(c))^2}.
   > \]

86. () `thm:quotient-rule-interval` — **Quotient Rule on an Interval**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f, g : I \to \mathbb{R}$. Suppose that $f$ and $g$ are differentiable on $I$ and that $g(x) \neq 0$ for all $x \in I$. Then $f/g$ is differentiable on $I$, and
   > \[
   > \left(\frac{f}{g}\right)'(x) = \frac{f'(x)g(x) - f(x)g'(x)}{(g(x))^2} \qquad \text{for all } x \in I.
   > \]

87. () `thm:chain-rule` — **Chain Rule**
   > **Statement.** Let $I, J \subseteq \mathbb{R}$ be intervals, let $f : I \to \mathbb{R}$ and $g : J \to \mathbb{R}$, and suppose that $f(I) \subseteq J$. Let $c \in I$. If $f$ is differentiable at $c$ and $g$ is differentiable at $f(c)$, then the composition $g \circ f$ is differentiable at $c$, and
   > \[
   > (g \circ f)'(c) = g'(f(c))\,f'(c).
   > \]

88. () `thm:uniqueness-of-the-derivative` — **Uniqueness of the Derivative**
   > **Statement.** Let $f : A \to \mathbb{R}$ and $c \in A$. If $f$ is differentiable at $c$, its derivative is unique.

89. () `lem:positive-derivative-implies-locally-increasing` — **Positive Derivative Implies Locally Increasing**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose that $f$ is differentiable at $c$. If $f'(c) > 0$, then there exists $\delta > 0$ such that
   > \[
   > f(x) < f(c) \quad \text{for all } x \in I \text{ with } c - \delta < x < c,
   > \]
   > and
   > \[
   > f(x) > f(c) \quad \text{for all } x \in I \text{ with } c < x < c + \delta.
   > \]

90. () `lem:negative-derivative-implies-locally-decreasing` — **Negative Derivative Implies Locally Decreasing**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, let $f : I \to \mathbb{R}$, let $c \in I$, and suppose that $f$ is differentiable at $c$. If $f'(c) < 0$, then there exists $\delta > 0$ such that
   > \[
   > f(x) > f(c) \quad \text{for all } x \in I \text{ with } c - \delta < x < c,
   > \]
   > and
   > \[
   > f(x) < f(c) \quad \text{for all } x \in I \text{ with } c < x < c + \delta.
   > \]

91. () `thm:differentiability-and-one-sided-derivatives` — **Differentiability and One-Sided Derivatives**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an open interval and let $f : I \to \mathbb{R}$. Then $f$ is differentiable at $c \in I$ if and only if both one-sided derivatives $f'_-(c)$ and $f'_+(c)$ exist and are equal. In that case,
   > \[
   > f'(c) = f'_-(c) = f'_+(c).
   > \]

92. () `thm:interior-extremum-theorem` — **Interior Extremum Theorem**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$.
   > If $f$ has a relative extremum at $c$ and $f$ is differentiable at $c$, then
   > \[
   > f'(c) = 0.
   > \]

93. () `thm:darboux` — **Darboux's Theorem**
   > **Statement.** Let $I := [a,b] \subseteq \mathbb{R}$ and let $f : I \to \mathbb{R}$ be differentiable on $I$. If $k$ is a real number strictly between $f'(a)$ and $f'(b)$, then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = k.
   > \]

94. () `thm:necessary-condition-extremum` — **Necessary Condition for an Interior Extremum**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then either $f'(c)$ does not exist, or
   > \[
   > f'(c) = 0.
   > \]

95. () `cor:necessary-condition-extremum` — **Necessary Condition for an Extremum**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an open interval, let $f : I \to \mathbb{R}$, and let $c \in I$. If $f$ has a relative extremum at $c$, then
   > \[
   > f'(c) = 0 \quad \text{or} \quad f'(c) \text{ does not exist.}
   > \]

96. () `thm:rolles-theorem` — **Rolle's Theorem**
   > **Statement.** Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$, differentiable on $(a,b)$, and satisfies $f(a) = f(b)$. Then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = 0.
   > \]

97. () `thm:mean-value-theorem` — **Mean Value Theorem**
   > **Statement.** Let $a, b \in \mathbb{R}$ with $a < b$. Suppose that $f : [a,b] \to \mathbb{R}$ is continuous on $[a,b]$ and differentiable on $(a,b)$. Then there exists $c \in (a,b)$ such that
   > \[
   > f'(c) = \frac{f(b) - f(a)}{b - a}.
   > \]

98. () `thm:nondecreasing-iff-nonneg-derivative` — **Nondecreasing Iff Nonnegative Derivative**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nondecreasing on $I$ if and only if
   > \[
   > f'(x) \geq 0 \qquad \text{for all } x \in I.
   > \]

99. () `thm:nonincreasing-iff-nonpos-derivative` — **Nonincreasing Iff Nonpositive Derivative**
   > **Statement.** Let $I \subseteq \mathbb{R}$ be an interval, and let $f : I \to \mathbb{R}$ be differentiable on $I$. Then $f$ is nonincreasing on $I$ if and only if
   > \[
   > f'(x) \leq 0 \qquad \text{for all } x \in I.
   > \]

100. () `thm:first-derivative-test-maximum` — **First Derivative Test: Relative Maximum**
   > **Statement.** Let $I := [a,b] \subseteq \mathbb{R}$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$. Suppose $f$ is differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ such that $(c-\delta,c+\delta) \subseteq I$ and
   > \[
   > f'(x) \geq 0 \quad \text{for all } x \in (c-\delta,c),
   > \qquad
   > f'(x) \leq 0 \quad \text{for all } x \in (c,c+\delta),
   > \]
   > then $f$ has a relative maximum at $c$.

101. () `thm:first-derivative-test-minimum` — **First Derivative Test: Relative Minimum**
   > **Statement.** Let $I := [a,b] \subseteq \mathbb{R}$, let $f : I \to \mathbb{R}$ be continuous on $I$, and let $c \in (a,b)$. Suppose $f$ is differentiable on $(a,c)$ and $(c,b)$. If there exists $\delta > 0$ such that $(c-\delta,c+\delta) \subseteq I$ and
   > \[
   > f'(x) \leq 0 \quad \text{for all } x \in (c-\delta,c),
   > \qquad
   > f'(x) \geq 0 \quad \text{for all } x \in (c,c+\delta),
   > \]
   > then $f$ has a relative minimum at $c$.

102. () `thm:zero-derivative-implies-constant` — **Zero Derivative Implies Constant**
   > **Statement.** Let $I := [a,b] \subseteq \mathbb{R}$ be a closed interval, and let $f : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If
   > \[
   > f'(x) = 0 \qquad \text{for all } x \in (a,b),
   > \]
   > then $f$ is constant on $I$.

103. () `cor:equal-derivatives-constant-difference` — **Equal Derivatives Imply Difference Is Constant**
   > **Statement.** Let $I := [a,b] \subseteq \mathbb{R}$, and let $f, g : I \to \mathbb{R}$ be continuous on $I$ and differentiable on $(a,b)$. If
   > \[
   > f'(x) = g'(x) \qquad \text{for all } x \in (a,b),
   > \]
   > then there exists $C \in \mathbb{R}$ such that $f(x) = g(x) + C$ for all $x \in I$.

104. () `cor:taylor-expansion-peano-remainder` — **Taylor Expansion with Peano Remainder**
   > **Statement.** Let $I\subseteq\mathbb{R}$ be an interval, let $a\in I$, let
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

105. () `thm:taylor-theorem-lagrange-remainder` — **Taylor's Theorem with Lagrange Remainder**
   > **Statement.** Let $a,b\in\mathbb{R}$ with $a<b$, let $n\in\mathbb{N}$, and let
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

106. () `prop:hyperbolic-addition` — **Addition Formulas for Hyperbolic Functions**
   > **Statement.** For all $x, y \in \mathbb{R}$:
   > \[
   >  \sinh(x+y) = \sinh x \cosh y + \cosh x \sinh y,
   >  \qquad
   >  \cosh(x+y) = \cosh x \cosh y + \sinh x \sinh y.
   > \]

107. () `prop:hyperbolic-pythagorean` — **Hyperbolic Pythagorean Identity**
   > **Statement.** For all $x \in \mathbb{R}$:
   > \[
   >  \cosh^2 x - \sinh^2 x = 1.
   > \]

108. () `prop:tanh-limits` — **Limits of $ $**
   > **Statement.** \[
   >  \lim_{x \to +\infty} \tanh x = 1,
   >  \qquad
   >  \lim_{x \to -\infty} \tanh x = -1.
   > \]

109. () `prop:limit-logarithm-fundamental` — **Fundamental Logarithmic Limit**
   > **Statement.** \[
   >  \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1.
   > \]

110. () `prop:exponential-dominates-power` — **Exponential Dominates Every Power**
   > **Statement.** For every $r > 0$:
   > \[
   >  \lim_{x \to \infty} \frac{x^r}{e^x} = 0.
   > \]

111. () `prop:power-dominates-log` — **Every Power Dominates the Logarithm**
   > **Statement.** For every $r > 0$:
   > \[
   >  \lim_{x \to \infty} \frac{\ln x}{x^r} = 0
   >  \qquad\text{and}\qquad
   >  \lim_{x \to 0^+} x^r \ln x = 0.
   > \]

112. () `prop:limit-compound-interest` — **Compound Interest Limit**
   > **Statement.** \[
   >  \lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x = e.
   > \]

113. () `prop:limit-exponential-fundamental` — **Fundamental Exponential Limit**
   > **Statement.** \[
   >  \lim_{x \to 0} \frac{e^x - 1}{x} = 1.
   > \]

114. () `thm:fundamental-trig-limit` — **Fundamental Trigonometric Limit**
   > **Statement.** \[
   >  \lim_{x \to 0} \frac{\sin x}{x} = 1.
   > \]

115. () `prop:pythagorean-identity` — **Pythagorean Identity**
   > **Statement.** For all $x \in \mathbb{R}$:
   > \[
   >  \sin^2 x + \cos^2 x = 1.
   > \]

116. () `prop:trig-addition-formulas` — **Addition Formulas**
   > **Statement.** For all $x, y \in \mathbb{R}$:
   > \[
   >  \sin(x+y) = \sin x \cos y + \cos x \sin y,
   >  \qquad
   >  \cos(x+y) = \cos x \cos y - \sin x \sin y.
   > \]

117. () `prop:limit-one-minus-cos` — **Second Fundamental Trigonometric Limit**
   > **Statement.** \[
   >  \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}.
   > \]

118. () `cor:composition-bijective` — **Composition of Bijections Is Bijective**
   > **Statement.** Let $f:A\to B$ and let $g:B\to C$. If $f$ is bijective and $g$ is
   > bijective, then $g\circ f:A\to C$ is bijective.

119. () `prop:composition-injective` — **Composition of Injections Is Injective**
   > **Statement.** Let $f:A\to B$ and let $g:B\to C$. If $f$ is injective and $g$ is
   > injective, then $g\circ f:A\to C$ is injective.

120. () `prop:composition-surjective` — **Composition of Surjections Is Surjective**
   > **Statement.** $\operatorname{Surjective}(f)\wedge\operatorname{Surjective}(g)
   > \Rightarrow\operatorname{Surjective}(g\circ f)$.

121. () `prop:inverse-bijection` — **Inverse of a Bijection Is a Bijection**
   > **Statement.** $\operatorname{Bijective}(f)\Rightarrow\operatorname{Bijective}(f^{-1})$.

122. () `prop:preimage-union-intersection` — **Preimage Distributes over Union and Intersection**
   > **Statement.** Let $f:A\to B$, $S,T\subseteq B$. Then:
   > - [label=(\roman*)]
   > - $f^{-1}(S\cup T)=f^{-1}(S)\cup f^{-1}(T)$.
   > - $f^{-1}(S\cap T)=f^{-1}(S)\cap f^{-1}(T)$.
   > - $f^{-1}(S^c)=(f^{-1}(S))^c$.

123. () `thm:bounded-limits` — **Bounded Limits**
   > **Statement.** Let $f : A \to \mathbb{R}$, let $c$ be a cluster point of $A$, and
   > let $a, b \in \mathbb{R}$. If $a \leq f(x) \leq b$ for all $x \in A$
   > with $x \neq c$, and $\lim_{x\to c}f(x)=L$, then
   > $a \leq L \leq b$.

124. () `prop:cauchy-criterion-limits` — **Cauchy Criterion for Function Limits**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
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

125. () `thm:composition-of-limits` — **Composition of Limits**
   > **Statement.** Let $f : A \to B$, let $g : B \to \mathbb{R}$, let $c_1$ be a
   > cluster point of $A$, and let $c_2 \in \mathbb{R}$ be a cluster
   > point of $B$. Suppose $\lim_{x\to c_1}f(x)=c_2$ and
   > $\lim_{y\to c_2}g(y)=L$. If $c_2 \in B$, assume also that
   > $g(c_2) = L$. Then $\lim_{x\to c_1}g(f(x))=L$.

126. () `prop:limit-absolute-value` — **Limit of Absolute Value**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$, then
   > $\lim_{x\to c}|f(x)|=|L|$.

127. () `thm:limit-difference` — **Difference Rule for Function Limits**
   > **Statement.** Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(f-g)(x)=L-M.
   > \]

128. () `thm:limit-implies-local-bounding` — **Limit Implies Local Boundedness**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > If $\lim_{x\to c}f(x)=L$ for some $L \in \mathbb{R}$,
   > then there exist $\delta, M > 0$ such that $|f(x)| \leq M$ for all
   > $x \in A$ with $0<|x-c|<\delta$.

129. () `prop:limit-neighbourhood-equiv` — **Neighbourhood Form of the Limit**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every
   > $\varepsilon$-neighbourhood $V_\varepsilon(L)$ there exists a
   > $\delta$-neighbourhood $V_\delta(c)$ such that
   > $x\in V_\delta^*(c)\cap A$ implies $f(x)\in V_\varepsilon(L)$.

130. () `thm:limit-product` — **Product Rule for Function Limits**
   > **Statement.** Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(fg)(x)=LM.
   > \]

131. () `thm:limit-quotient` — **Quotient Rule for Function Limits**
   > **Statement.** Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$, $\lim_{x\to c}g(x)=M$, and $M\neq 0$, then
   > there exists $\delta_0>0$ such that $g(x)\neq 0$ whenever $x\in A$ and
   > $0<|x-c|<\delta_0$, and
   > \[
   >  \lim_{x\to c}\frac{f(x)}{g(x)}=\frac{L}{M}.
   > \]

132. () `thm:limit-scalar-multiple` — **Scalar Multiple Rule for Function Limits**
   > **Statement.** Let $f:A\to\mathbb{R}$, let $c$ be a cluster point of $A$, and let
   > $\alpha\in\mathbb{R}$. If $\lim_{x\to c}f(x)=L$, then
   > \[
   >  \lim_{x\to c}(\alpha f)(x)=\alpha L.
   > \]

133. () `thm:limit-sum` — **Sum Rule for Function Limits**
   > **Statement.** Let $f,g:A\to\mathbb{R}$ and let $c$ be a cluster point of $A$. If
   > $\lim_{x\to c}f(x)=L$ and $\lim_{x\to c}g(x)=M$, then
   > \[
   >  \lim_{x\to c}(f+g)(x)=L+M.
   > \]

134. () `thm:limit-unique` — **Uniqueness of Limits of Functions**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $f$ has at most one limit at $c$.

135. () `thm:limits-are-local` — **Limits Are Local**
   > **Statement.** Let $E \subseteq X \subseteq \mathbb{R}$, let $x_0$ be a cluster
   > point of $E$, let $f : X \to \mathbb{R}$, and let $\delta > 0$.
   > Then
   > \[
   >  \lim_{x\to x_0;\,x\in E}f(x)=L
   >  \;\iff\;
   >  \lim_{x\to x_0;\,x\in E\cap(x_0-\delta,x_0+\delta)}f(x)=L.
   > \]

136. () `thm:monotone-limit-theorem` — **Monotone Limit Theorem**
   > **Statement.** Let $a < b$ and let $f : (a,b) \to \mathbb{R}$ be monotone and
   > bounded. Then both one-sided limits exist at every interior point.
   > For increasing $f$ and every $x_0 \in (a,b)$:
   > \[
   >  f(x_0^-) = \sup\{\,f(x) : a < x < x_0\,\},
   >  \qquad
   >  f(x_0^+) = \inf\{\,f(x) : x_0 < x < b\,\}.
   > \]

137. () `cor:sequential-criterion-left-hand-limit` — **Sequential Criterion for Left-Hand Limits**
   > **Statement.** Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(-\infty,c)$. Then $\lim_{x\to c^-}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(-\infty,c)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.

138. () `prop:sequential-criterion-limits` — **Sequential Criterion for Function Limits**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > Then $\lim_{x\to c}f(x)=L$ if and only if for every sequence
   > $(x_n)\subseteq A\setminus\{c\}$ with $x_n\to c$, one has
   > $f(x_n)\to L$.

139. () `cor:limit-three-equiv` — **Three Equivalent Forms of the Function Limit**
   > **Statement.** Let $f : A \to \mathbb{R}$ and let $c$ be a cluster point of $A$.
   > The $\varepsilon$-$\delta$ form of $\lim_{x\to c}f(x)=L$, the
   > neighbourhood form, and the sequential form are equivalent descriptions
   > of the same limit condition.

140. () `thm:sequential-criterion-right-hand-limit` — **Sequential Criterion for Right-Hand Limits**
   > **Statement.** Let $A\subseteq\mathbb{R}$, let $f:A\to\mathbb{R}$, and suppose $c$ is a
   > cluster point of $A\cap(c,\infty)$. Then $\lim_{x\to c^+}f(x)=L$ if and
   > only if for every sequence $(x_n)\subseteq A\cap(c,\infty)$ with
   > $x_n\to c$, one has $f(x_n)\to L$.

141. () `thm:squeeze-function-limits` — **Squeeze Theorem for Function Limits**
   > **Statement.** Let $f, g, h : A \to \mathbb{R}$ and let $c$ be a cluster point of
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

142. () `thm:two-sided-limit-iff-matching-one-sided-limits` — **Two-Sided Limit via One-Sided Limits**
   > **Statement.** Let $A\subseteq\mathbb{R}$ and let $f:A\to\mathbb{R}$. If $c$ is a
   > cluster point of both $A\cap(c,\infty)$ and $A\cap(-\infty,c)$, then
   > $\lim_{x\to c}f(x)=L$ if and only if both $\lim_{x\to c^+}f(x)=L$ and
   > $\lim_{x\to c^-}f(x)=L$.

143. () `lem:closure-elementary` — **Elementary Properties of Closures**
   > **Statement.** Let $X, Y \subseteq \mathbb{R}$. Then: (i) $X \subseteq \overline{X}$;
   > (ii) $\overline{X \cup Y} = \overline{X} \cup \overline{Y}$;
   > (iii) $\overline{X \cap Y} \subseteq \overline{X} \cap \overline{Y}$;
   > (iv) $X \subseteq Y \Rightarrow \overline{X} \subseteq \overline{Y}$.

144. () `thm:cluster-point-sequential` — **Sequential Characterization of Cluster Points**
   > **Statement.** $c\text{ is a cluster point of }A$ if and only if there exists
   > $(a_n) \subseteq A \setminus \{c\}$ with $a_n \to c$.

145. () `cor:closed-iff-seq-limits` — **Closed iff Sequentially Closed**
   > **Statement.** $X\text{ is closed} \iff \forall (a_n)\subseteq X,\;
   > a_n \to x \Rightarrow x \in X$.

146. () `thm:heine-borel-subsets-real-line` — **Heine--Borel Theorem for $ $**
   > **Statement.** $X\text{ is closed} \wedge X\text{ is bounded}$
   > $\iff$ every $(a_n)\subseteq X$ has a subsequence converging to
   > a limit in $X$.

147. () `cor:interval-all-limit-points` — **Every Point of an Interval Is a Cluster Point**
   > **Statement.** If $I$ is an interval, then every $x\in I$ is a cluster point of $I$.

148. () `thm:absolute-value-cauchy-sequence` — **Absolute Values of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ be a Cauchy real sequence. Then $(|x_n|)$ is Cauchy.

149. () `thm:cauchy-criterion-via-tails` — **Cauchy Criterion via Tails**
   > **Statement.** Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > for every $\varepsilon>0$ there exists $N\in\mathbb{N}$ such that the
   > $N$-tail has pairwise term distances less than $\varepsilon$.

150. () `thm:cauchy-sequence-with-convergent-subsequence` — **Cauchy Sequence with a Convergent Subsequence**
   > **Statement.** Let $(x_n)$ be a Cauchy real sequence. If a subsequence of $(x_n)$
   > converges to $L\in\mathbb{R}$, then $(x_n)$ converges to $L$.

151. () `thm:cauchy-sequences-are-bounded` — **Cauchy Sequences Are Bounded**
   > **Statement.** Every Cauchy real sequence is bounded.

152. () `thm:cauchy-successive-differences-vanish` — **Cauchy Sequences Have Vanishing Successive Differences**
   > **Statement.** If $(x_n)$ is a Cauchy real sequence, then
   > \[
   >  |x_{n+1}-x_n|\to 0.
   > \]

153. () `thm:cauchy-tail-diameter-criterion` — **Cauchy Tail Diameter Criterion**
   > **Statement.** Let $(x_n)$ be a real sequence. Then $(x_n)$ is Cauchy if and only if
   > every sufficiently late tail has arbitrarily small pairwise diameter.

154. () `thm:convergent-sequences-are-cauchy` — **Convergent Sequences Are Cauchy**
   > **Statement.** Let $(x_n)$ be a real sequence. If $(x_n)$ converges, then $(x_n)$ is
   > Cauchy.

155. () `thm:product-cauchy-sequences` — **Products of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_ny_n)$ is
   > Cauchy.

156. () `thm:reciprocal-cauchy-sequence` — **Reciprocals of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ be a Cauchy real sequence. If there exist $c>0$ and
   > $N_0\in\mathbb{N}$ such that $|x_n|\ge c$ for every $n\ge N_0$, then
   > $(1/x_n)$ is Cauchy.

157. () `thm:quotient-cauchy-sequences` — **Quotients of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. If there exist $c>0$
   > and $N_0\in\mathbb{N}$ such that $|y_n|\ge c$ for every $n\ge N_0$,
   > then $(x_n/y_n)$ is Cauchy.

158. () `thm:scalar-multiple-cauchy-sequence` — **Scalar Multiples of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ be a Cauchy real sequence, and let $\alpha\in\mathbb{R}$.
   > Then $(\alpha x_n)$ is Cauchy.

159. () `thm:sum-cauchy-sequences` — **Sums of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n+y_n)$ is
   > Cauchy.

160. () `thm:difference-cauchy-sequences` — **Differences of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be Cauchy real sequences. Then $(x_n-y_n)$ is
   > Cauchy.

161. () `thm:linear-combination-cauchy-sequences` — **Linear Combinations of Cauchy Sequences**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be Cauchy real sequences, and let
   > $\alpha,\beta\in\mathbb{R}$. Then $(\alpha x_n+\beta y_n)$ is Cauchy.

162. () `thm:constant-squeeze-theorem` — **Constant Squeeze Theorem**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If there
   > exists $N_0\in\mathbb{N}$ such that $L\le x_n\le L$ for every
   > $n\ge N_0$, then $x_n\to L$.

163. () `thm:equivalence-of-convergence-formulations` — **Equivalence of Convergence Formulations**
   > **Statement.** Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. The following
   > statements are equivalent.
   > - [label=\textup{(\alph*)}]
   > - $x_n \to L$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(|x_n - L| < \varepsilon\bigr)$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(L - \varepsilon < x_n < L + \varepsilon\bigr)$.
   > - $\forall \varepsilon > 0 \;\exists K \in \mathbb{N} \;\forall n \ge K
   >  \;\bigl(x_n \in V_\varepsilon(L)\bigr)$.

164. () `thm:limit-of-a-product` — **Limit of a Product**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_ny_n\to LM$.

165. () `thm:limit-of-a-square-root` — **Limit of a Square Root**
   > **Statement.** Let $(x_n)$ be a real sequence such that $0\le x_n$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$. If $x_n\to L$, then
   > $0\le L$ and $\sqrt{x_n}\to\sqrt{L}$.

166. () `thm:limit-of-a-square` — **Limit of a Square**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $x_n^2\to L^2$.

167. () `thm:limit-of-a-sum` — **Limit of a Sum**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n+y_n\to L+M$.

168. () `thm:limit-of-an-absolute-value` — **Limit of an Absolute Value**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $|x_n|\to |L|$.

169. () `thm:limit-of-scalar-multiple` — **Limit of a Scalar Multiple**
   > **Statement.** Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $\alpha\in\mathbb{R}$. If $x_n\to L$, then $\alpha x_n\to \alpha L$.

170. () `thm:limit-of-a-negation` — **Limit of a Negation**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $-x_n\to -L$.

171. () `thm:limit-of-a-difference` — **Limit of a Difference**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > If $x_n\to L$ and $y_n\to M$, then $x_n-y_n\to L-M$.

172. () `thm:nonzero-limit-eventually-nonzero` — **Nonzero Limit is Eventually Nonzero**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$ with $L\neq 0$.
   > If $x_n\to L$, then there exists $N\in\mathbb{N}$ such that $x_n\neq 0$
   > for every $n\ge N$.

173. () `thm:limit-of-a-reciprocal` — **Limit of a Reciprocal**
   > **Statement.** Let $(x_n)$ be a real sequence such that $x_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L\in\mathbb{R}$ with $L\neq 0$. If $x_n\to L$,
   > then $1/x_n\to 1/L$.

174. () `thm:limit-of-a-quotient` — **Limit of a Quotient**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences such that $y_n\neq 0$ for every
   > $n\in\mathbb{N}$, and let $L,M\in\mathbb{R}$ with $M\neq 0$. If
   > $x_n\to L$ and $y_n\to M$, then $x_n/y_n\to L/M$.

175. () `thm:polynomial-sequence-limit` — **Polynomial Sequence Limit**
   > **Statement.** Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p\in\mathbb{R}[t]$ be a polynomial. If $x_n\to L$, then
   > $p(x_n)\to p(L)$.

176. () `thm:positive-limit-eventually-positive` — **Positive Limit is Eventually Positive**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L>0$. If $x_n\to L$, then there
   > exists $N\in\mathbb{N}$ such that $0<x_n$ for every $n\ge N$.

177. () `thm:rational-sequence-limit` — **Rational Sequence Limit**
   > **Statement.** Let $(x_n)$ be a real sequence, let $L\in\mathbb{R}$, and let
   > $p,q\in\mathbb{R}[t]$ be polynomials. Suppose $q(L)\neq 0$ and
   > $q(x_n)\neq 0$ for every $n\in\mathbb{N}$. If $x_n\to L$, then
   > \[
   > \frac{p(x_n)}{q(x_n)}\to \frac{p(L)}{q(L)}.
   > \]

178. () `thm:uniqueness-of-limits` — **Uniqueness of Limits**
   > **Statement.** Let $(x_n) \subseteq \mathbb{R}$. If $x_n \to L$ and $x_n \to K$, then
   > $L = K$.

179. () `thm:limit-preserves-eventual-order` — **Limit Preserves Eventual Order**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $L,M\in\mathbb{R}$.
   > Suppose that $x_n\to L$ and $y_n\to M$. If there exists
   > $N_0\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N_0$, then
   > $L\le M$.

180. () `thm:eventual-strict-comparison-preserves-weak-limit-order` — **Eventual Strict Comparison Preserves Weak Limit Order**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$.
   > - [label=(\alph*)]
   > - If there exists $N\in\mathbb{N}$ such that $x_n<y_n$ for every
   >  $n\ge N$, then $A\le B$.
   > - If there exists $N\in\mathbb{N}$ such that $x_n>y_n$ for every
   >  $n\ge N$, then $A\ge B$.

181. () `thm:constant-comparison-for-sequence-limits` — **Constant Comparison for Sequence Limits**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $A,B\in\mathbb{R}$. Suppose
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

182. () `thm:sequence-squeeze-theorem` — **Sequence Squeeze Theorem**
   > **Statement.** Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences, and let
   > $L\in\mathbb{R}$. Suppose that $a_n\to L$ and $b_n\to L$. If there
   > exists $N_0\in\mathbb{N}$ such that $a_n\le x_n\le b_n$ for every
   > $n\ge N_0$, then $x_n\to L$.

183. () `thm:compound-interest-approximation-e` — **Compound-Interest Approximation of $e$**
   > **Statement.** Let $(c_n)$ be the compound-interest sequence. Then
   > \[
   >  \lim_{n\to\infty}c_n=e.
   > \]

184. () `thm:decimal-truncations-converge` — **Decimal Truncations Converge**
   > **Statement.** Let $\alpha\in\mathbb{R}$, and let $(d_n)$ be the decimal truncation
   > sequence of $\alpha$. Then
   > \[
   >  \lim_{n\to\infty}d_n=\alpha.
   > \]

185. () `thm:absolute-value-squeeze-theorem` — **Absolute-Value Squeeze Theorem**
   > **Statement.** Let $(x_n)$ and $(u_n)$ be real sequences, and let $L\in\mathbb{R}$.
   > Suppose that $u_n\to 0$. If there exists $N_0\in\mathbb{N}$ such that
   > $|x_n-L|\le u_n$ for every $n\ge N_0$, then $x_n\to L$.

186. () `thm:strict-limit-separation-gives-eventual-order` — **Strict Limit Separation Gives Eventual Order**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences, and let $A,B\in\mathbb{R}$.
   > Suppose that $x_n\to A$ and $y_n\to B$. If $A<B$, then there exists
   > $N\in\mathbb{N}$ such that $x_n<y_n$ for every $n\ge N$.

187. () `thm:absolute-bound-gives-upper-and-lower-bounds` — **Absolute Bound Gives Upper and Lower Bounds**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $K > 0$. If $|x_n| \le K$ for every
   > $n \in \mathbb{N}$, then $-K \le x_n \le K$ for every
   > $n \in \mathbb{N}$.

188. () `thm:bounded-sequence-iff-bounded-above-and-below` — **Bounded Sequence If and Only If Bounded Above and Below**
   > **Statement.** Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if it is both bounded above and bounded below.

189. () `thm:constant-implies-ultimately-constant` — **Constant Implies Ultimately Constant**
   > **Statement.** Every constant real sequence is ultimately constant.

190. () `thm:constant-null-sequence` — **Constant Null Sequence**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ is a null sequence if and only if
   > $c = 0$.

191. () `thm:constant-sequence-convergence` — **Constant Sequence Convergence**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $c \in \mathbb{R}$. If $x_n = c$
   > for every $n \in \mathbb{N}$, then $(x_n)$ converges to $c$.

192. () `thm:difference-from-limit-is-null` — **Difference from the Limit is Null**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L \in \mathbb{R}$. The sequence
   > $(x_n)$ converges to $L$ if and only if the sequence $(x_n - L)$ is a null
   > sequence.

193. () `thm:eventually-bounded-above-tail-formulation` — **Eventually Bounded Above Tail Formulation**
   > **Statement.** Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded above if and
   > only if there exist $N_0 \in \mathbb{N}$ and $M \in \mathbb{R}$ such that
   > $x_n \le M$ for every $n \ge N_0$.

194. () `thm:eventually-bounded-below-tail-formulation` — **Eventually Bounded Below Tail Formulation**
   > **Statement.** Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded below if and
   > only if there exist $N_0 \in \mathbb{N}$ and $m \in \mathbb{R}$ such that
   > $m \le x_n$ for every $n \ge N_0$.

195. () `thm:eventually-bounded-tail-formulation` — **Eventually Bounded Tail Formulation**
   > **Statement.** Let $(x_n)$ be a real sequence. The sequence $(x_n)$ is bounded if and only
   > if there exist $N_0 \in \mathbb{N}$ and $M > 0$ such that $|x_n| \le M$ for
   > every $n \ge N_0$.

196. () `thm:tail-equality-preserves-convergence` — **Tail Equality Preserves Convergence**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be real sequences. If there exists
   > $N_0 \in \mathbb{N}$ such that $x_n = y_n$ for every $n \ge N_0$, then
   > for every $L \in \mathbb{R}$, $(x_n)$ converges to $L$ if and only if
   > $(y_n)$ converges to $L$.

197. () `thm:ultimately-constant-null-sequence` — **Ultimately Constant Null Sequence**
   > **Statement.** Let $(x_n)$ be a real sequence. Suppose there exist $N_0 \in \mathbb{N}$
   > and $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$. Then
   > $(x_n)$ is a null sequence if and only if $c = 0$.

198. () `thm:ultimately-constant-sequence-convergence` — **Ultimately Constant Sequence Convergence**
   > **Statement.** Let $(x_n)$ be a real sequence. If there exist $N_0 \in \mathbb{N}$ and
   > $c \in \mathbb{R}$ such that $x_n = c$ for every $n \ge N_0$, then
   > $(x_n)$ converges to $c$.

199. () `thm:ultimately-zero-sequence-is-null` — **Ultimately Zero Sequence is Null**
   > **Statement.** Let $(x_n)$ be a real sequence. If there exists $N_0 \in \mathbb{N}$ such
   > that $x_n = 0$ for every $n \ge N_0$, then $(x_n)$ is a null sequence.

200. () `thm:upper-and-lower-bounds-give-absolute-bound` — **Upper and Lower Bounds Give an Absolute Bound**
   > **Statement.** Let $(x_n)$ be a real sequence. If there exist $m,M \in \mathbb{R}$ such
   > that $m \le x_n \le M$ for every $n \in \mathbb{N}$, then there exists
   > $K > 0$ such that $|x_n| \le K$ for every $n \in \mathbb{N}$.

201. () `thm:zero-sequence-is-null` — **Zero Sequence is Null**
   > **Statement.** Let $(x_n)$ be a real sequence. If $x_n = 0$ for every $n \in \mathbb{N}$,
   > then $(x_n)$ is a null sequence.

202. () `thm:divergence-to-infinity-implies-real-divergence` — **Divergence to Infinity Implies Real Divergence**
   > **Statement.** Let $(x_n)$ be a real sequence. If $x_n\to+\infty$ or $x_n\to-\infty$,
   > then $(x_n)$ is divergent.

203. () `thm:unbounded-above-has-positive-infinity-subsequence` — **Unbounded Above Sequence Has a Positive-Infinity Subsequence**
   > **Statement.** Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded above, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to+\infty$.

204. () `thm:unbounded-below-has-negative-infinity-subsequence` — **Unbounded Below Sequence Has a Negative-Infinity Subsequence**
   > **Statement.** Let $(x_n)$ be a real sequence. If $(x_n)$ is not bounded below, then
   > there exists a subsequence $(x_{\sigma(k)})$ such that
   > $x_{\sigma(k)}\to-\infty$.

205. () `thm:convergence-iff-liminf-equals-limsup` — **Convergence iff Liminf Equals Limsup**
   > **Statement.** Let $(x_n)$ be a bounded real sequence, and let $L\in\mathbb{R}$. Then
   > $x_n\to L$ if and only if
   > \[
   >  \liminf_{n\to\infty}x_n
   >  =
   >  \limsup_{n\to\infty}x_n
   >  =
   >  L.
   > \]

206. () `thm:liminf-below-limsup` — **Liminf Is Below Limsup**
   > **Statement.** Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >  \liminf_{n\to\infty}x_n\le \limsup_{n\to\infty}x_n.
   > \]

207. () `thm:liminf-comparison-under-eventual-order` — **Liminf Comparison Under Eventual Order**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >  \liminf_{n\to\infty}x_n
   >  \le
   >  \liminf_{n\to\infty}y_n.
   > \]

208. () `thm:liminf-squeeze-under-eventual-order` — **Liminf Squeeze Under Eventual Order**
   > **Statement.** Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
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

209. () `thm:limsup-comparison-under-eventual-order` — **Limsup Comparison Under Eventual Order**
   > **Statement.** Let $(x_n)$ and $(y_n)$ be bounded real sequences. If there exists
   > $N\in\mathbb{N}$ such that $x_n\le y_n$ for every $n\ge N$, then
   > \[
   >  \limsup_{n\to\infty}x_n
   >  \le
   >  \limsup_{n\to\infty}y_n.
   > \]

210. () `thm:limsup-squeeze-under-eventual-order` — **Limsup Squeeze Under Eventual Order**
   > **Statement.** Let $(a_n)$, $(x_n)$, and $(b_n)$ be bounded real sequences. If there
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

211. () `thm:tail-infima-are-increasing` — **Tail Infima Are Increasing**
   > **Statement.** Let $(x_n)$ be a bounded real sequence, and let $(i_n)$ be its tail
   > infimum sequence. Then $(i_n)$ is increasing.

212. () `thm:tail-suprema-are-decreasing` — **Tail Suprema Are Decreasing**
   > **Statement.** Let $(x_n)$ be a bounded real sequence, and let $(s_n)$ be its tail
   > supremum sequence. Then $(s_n)$ is decreasing.

213. () `thm:algebraic-transformations-preserve-monotonicity` — **Algebraic Transformations Preserve Monotonicity**
   > **Statement.** Let $(x_n)$ be a real sequence and let $c,\alpha\in\mathbb{R}$.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing, then $(x_n+c)$ is increasing.
   > - If $(x_n)$ is decreasing, then $(x_n+c)$ is decreasing.
   > - If $(x_n)$ is increasing and $\alpha>0$, then $(\alpha x_n)$ is increasing.
   > - If $(x_n)$ is increasing and $\alpha<0$, then $(\alpha x_n)$ is decreasing.
   > - If $(x_n)$ is increasing, then $(-x_n)$ is decreasing.
   > - If $(x_n)$ is decreasing, then $(-x_n)$ is increasing.

214. () `thm:monotone-convergence-theorem` — **Monotone Convergence Theorem**
   > **Statement.** Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing and bounded above, then $(x_n)$ converges and
   >  \[
   >  \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   >  \]
   > - If $(x_n)$ is decreasing and bounded below, then $(x_n)$ converges and
   >  \[
   >  \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   >  \]

215. () `thm:newton-approximation-sqrt-two` — **Newton Approximation of $ $**
   > **Statement.** Let $(x_n)$ be the Newton sequence for $\sqrt{2}$. Then $(x_n)$ converges
   > and
   > \[
   >  \lim_{n\to\infty}x_n=\sqrt{2}.
   > \]

216. () `thm:bounded-monotone-sequence-equivalences` — **Bounded Monotone Sequence Equivalences**
   > **Statement.** Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded above.
   > - If $(x_n)$ is decreasing, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded below.
   > - If $(x_n)$ is monotone, then $(x_n)$ converges if and only if
   >  $(x_n)$ is bounded.

217. () `thm:strict-monotonicity-implies-monotonicity` — **Strict Monotonicity Implies Monotonicity**
   > **Statement.** Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is strictly increasing, then $(x_n)$ is increasing.
   > - If $(x_n)$ is strictly decreasing, then $(x_n)$ is decreasing.

218. () `thm:unbounded-monotone-divergence` — **Unbounded Monotone Divergence**
   > **Statement.** Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is increasing and is not bounded above, then
   >  $x_n\to+\infty$.
   > - If $(x_n)$ is decreasing and is not bounded below, then
   >  $x_n\to-\infty$.

219. () `thm:decreasing-sequence-limit-as-infimum` — **Decreasing Sequence Limit as Infimum**
   > **Statement.** Let $(x_n)$ be a decreasing real sequence that is bounded below. Then
   > \[
   >  \lim_{n\to\infty}x_n=\inf\{x_n:n\in\mathbb{N}\}.
   > \]

220. () `thm:increasing-sequence-limit-as-supremum` — **Increasing Sequence Limit as Supremum**
   > **Statement.** Let $(x_n)$ be an increasing real sequence that is bounded above. Then
   > \[
   >  \lim_{n\to\infty}x_n=\sup\{x_n:n\in\mathbb{N}\}.
   > \]

221. () `thm:tail-suprema-and-infima-converge` — **Tail Suprema and Infima Converge**
   > **Statement.** Let $(x_n)$ be a bounded real sequence. Define
   > \[
   >  s_n=\sup\{x_k:k\ge n\},
   >  \qquad
   >  i_n=\inf\{x_k:k\ge n\}.
   > \]
   > Then $(s_n)$ and $(i_n)$ converge.

222. () `thm:bounded-sequence-has-limsup-and-liminf` — **Bounded Sequence Has Limsup and Liminf**
   > **Statement.** Every bounded real sequence has a limit superior and a limit inferior.

223. () `thm:boundedness-passes-to-subsequences` — **Boundedness Passes to Subsequences**
   > **Statement.** Every subsequence of a bounded real sequence is bounded.

224. () `thm:frequent-properties-yield-subsequences` — **Frequent Properties Yield Subsequences**
   > **Statement.** Let $P(n)$ be a property of indices. If for every $N\in\mathbb{N}$ there
   > exists $n\ge N$ such that $P(n)$ holds, then there exists a strictly
   > increasing index map $\sigma:\mathbb{N}\to\mathbb{N}$ such that
   > $P(\sigma(k))$ holds for every $k\in\mathbb{N}$.

225. () `thm:cluster-values-are-subsequential-limits` — **Cluster Values Are Subsequential Limits**
   > **Statement.** Let $(x_n)$ be a real sequence, and let $L\in\mathbb{R}$. Then $L$ is a
   > cluster value of $(x_n)$ if and only if $L$ is a subsequential limit of
   > $(x_n)$.

226. () `thm:monotone-subsequence-theorem` — **Monotone Subsequence Theorem**
   > **Statement.** Every real sequence has a monotone subsequence.

227. () `thm:bolzano-weierstrass-sequences` — **Bolzano-Weierstrass Theorem for Sequences**
   > **Statement.** Every bounded real sequence has a convergent subsequence.

228. () `thm:cauchy-criterion-real-sequences` — **Cauchy Criterion for Real Sequences**
   > **Statement.** Let $(x_n)$ be a real sequence. Then $(x_n)$ converges if and only if
   > $(x_n)$ is Cauchy.

229. () `thm:factorial-partial-sums-approximate-e` — **Factorial Partial Sums Approximate $e$**
   > **Statement.** Let $(s_n)$ be the factorial partial-sum sequence. Then $(s_n)$ converges
   > to the Euler number $e$:
   > \[
   >  \lim_{n\to\infty}s_n=e.
   > \]

230. () `thm:bounded-sequences-have-cluster-values` — **Bounded Sequences Have Cluster Values**
   > **Statement.** Every bounded real sequence has at least one cluster value.

231. () `thm:liminf-smallest-subsequential-limit` — **Liminf Is the Smallest Subsequential Limit**
   > **Statement.** Let $(x_n)$ be a bounded real sequence, and let
   > $I=\liminf_{n\to\infty}x_n$. Then $I$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is greater than or
   > equal to $I$.

232. () `thm:limsup-largest-subsequential-limit` — **Limsup Is the Largest Subsequential Limit**
   > **Statement.** Let $(x_n)$ be a bounded real sequence, and let
   > $S=\limsup_{n\to\infty}x_n$. Then $S$ is a subsequential limit of
   > $(x_n)$, and every subsequential limit of $(x_n)$ is less than or equal
   > to $S$.

233. () `thm:limsup-liminf-extremal-cluster-values` — **Limsup and Liminf Are Extremal Cluster Values**
   > **Statement.** Let $(x_n)$ be a bounded real sequence. Then
   > $\limsup_{n\to\infty}x_n$ is the largest cluster value of $(x_n)$, and
   > $\liminf_{n\to\infty}x_n$ is the smallest cluster value of $(x_n)$.

234. () `thm:monotonicity-passes-to-subsequences` — **Monotonicity Passes to Subsequences**
   > **Statement.** Every subsequence of an increasing real sequence is increasing, and every
   > subsequence of a decreasing real sequence is decreasing.

235. () `thm:subsequence-indices-dominate-identity` — **Subsequence Indices Dominate the Identity**
   > **Statement.** Let $\sigma:\mathbb{N}\to\mathbb{N}$ be a strictly increasing index map.
   > Then
   > \[
   >  k\le \sigma(k)
   >  \qquad
   >  \text{for every } k\in\mathbb{N}.
   > \]

236. () `thm:eventual-properties-pass-to-subsequences` — **Eventual Properties Pass to Subsequences**
   > **Statement.** Let $P(n)$ be a property of indices. If there exists $N\in\mathbb{N}$ such
   > that $P(n)$ holds for every $n\ge N$, then for every strictly increasing
   > index map $\sigma$ there exists $K\in\mathbb{N}$ such that $P(\sigma(k))$
   > holds for every $k\ge K$.

237. () `thm:squeeze-passes-to-subsequences` — **Squeeze Passes to Subsequences**
   > **Statement.** Let $(a_n)$, $(x_n)$, and $(b_n)$ be real sequences. If
   > $a_n\le x_n\le b_n$ eventually, then for every subsequence
   > $(x_{\sigma(k)})$ there exists $K\in\mathbb{N}$ such that
   > \[
   >  a_{\sigma(k)}\le x_{\sigma(k)}\le b_{\sigma(k)}
   >  \qquad
   >  \text{for every } k\ge K.
   > \]

238. () `thm:subsequence-of-subsequence` — **Subsequence of a Subsequence**
   > **Statement.** Every subsequence of a subsequence of $(x_n)$ is a subsequence of $(x_n)$.

239. () `thm:subsequences-preserve-limits` — **Subsequences Preserve Limits**
   > **Statement.** Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then every subsequence of $(x_n)$ converges to $L$.

240. () `thm:bounded-divergence-produces-two-subsequential-limits` — **Bounded Divergence Produces Two Subsequential Limits**
   > **Statement.** Let $(x_n)$ be a bounded real sequence. If $(x_n)$ is divergent, then
   > there exist $L,K\in\mathbb{R}$ with $L\ne K$ such that $L$ and $K$ are
   > subsequential limits of $(x_n)$.

241. () `thm:subsequential-limit-of-convergent-sequence` — **Subsequential Limit of a Convergent Sequence**
   > **Statement.** Let $(x_n)$ be a real sequence and let $L\in\mathbb{R}$. If $x_n\to L$,
   > then $L$ is the only possible subsequential limit of $(x_n)$.

242. () `thm:divergence-by-two-subsequential-limits` — **Divergence by Two Subsequential Limits**
   > **Statement.** Let $(x_n)$ be a real sequence. If $(x_n)$ has two distinct subsequential
   > limits, then $(x_n)$ does not converge.

243. () `thm:two-subsequential-limits-force-divergence` — **Two Subsequential Limits Force Divergence**
   > **Statement.** Let $(x_n)$ be a real sequence. If $(x_n)$ has two subsequential limits
   > $L,K\in\mathbb{R}$ with $L\ne K$, then $(x_n)$ is divergent.

244. () `thm:oscillation-criterion-via-liminf-limsup` — **Oscillation Criterion via Liminf and Limsup**
   > **Statement.** Let $(x_n)$ be a bounded real sequence. Then
   > \[
   >  \liminf_{n\to\infty}x_n
   >  <
   >  \limsup_{n\to\infty}x_n
   > \]
   > if and only if $(x_n)$ has two distinct subsequential limits.

245. () `thm:subsequential-limits-respect-bounds` — **Subsequential Limits Respect Bounds**
   > **Statement.** Let $(x_n)$ be a real sequence and let $L$ be a subsequential limit of
   > $(x_n)$. If $m\le x_n\le M$ for every $n\in\mathbb{N}$, then
   > $m\le L\le M$.

246. () `thm:sequential-compactness-closed-bounded-interval` — **Sequential Compactness of Closed Bounded Intervals**
   > **Statement.** Let $a,b\in\mathbb{R}$ with $a\le b$. Every sequence in $[a,b]$ has a
   > convergent subsequence whose limit belongs to $[a,b]$.

247. () `thm:convergence-by-domination` — **Convergence by Domination**
   > **Statement.** Let $(x_n) \subseteq \mathbb{R}$ and let $L \in \mathbb{R}$. Let
   > $(a_n)$ be a sequence of positive real numbers with
   > $\displaystyle\lim_{n \to \infty} a_n = 0$. If there exist a constant
   > $c > 0$ and an index $m \in \mathbb{N}$ such that
   > \[
   >  |x_n - L| \;\le\; c\, a_n \qquad \forall n \ge m,
   > \]
   > then $\displaystyle\lim_{n \to \infty} x_n = L$.

248. () `thm:convergence-of-tail` — **Convergence of a Tail**
   > **Statement.** Let $(x_n) \subseteq \mathbb{R}$ and let $m \in \mathbb{N}$. The
   > $m$-tail $(x_{m+n})_{n \in \mathbb{N}}$ converges if and only if
   > $(x_n)$ converges. Moreover, in this case,
   > \[
   >  \lim_{n \to \infty} x_{m+n} \;=\; \lim_{n \to \infty} x_n.
   > \]

249. () `thm:eventually-monotone-convergence-theorem` — **Eventually Monotone Convergence Theorem**
   > **Statement.** Let $(x_n)$ be a real sequence.
   > - [label=(\alph*)]
   > - If $(x_n)$ is eventually increasing and bounded above, then
   >  $(x_n)$ converges.
   > - If $(x_n)$ is eventually decreasing and bounded below, then
   >  $(x_n)$ converges.
   > - If $(x_n)$ is eventually monotone and bounded, then $(x_n)$ converges.

250. () `thm:ratio-limit-less-than-one-implies-null` — **Ratio Limit Less Than One Implies Null**
   > **Statement.** Let $(x_n)$ be a sequence of positive real numbers. Suppose that the
   > limit
   > \[
   >  L := \lim_{n\to\infty}\frac{x_{n+1}}{x_n}
   > \]
   > exists. If $L<1$, then $(x_n)$ converges and
   > \[
   >  \lim_{n\to\infty} x_n = 0.
   > \]

251. () `prop:higher-diff-formula` — **Higher difference formula**
   > **Statement.** For any function \(f\),
   > \[
   > \Delta^n f(x)
   > =
   > \sum_{k=0}^{n} (-1)^{\,n-k}
   > \binom{n}{k}
   > f(x+k).
   > \]
