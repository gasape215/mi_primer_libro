<!-- Convertido automáticamente desde PDF. Revisar y corregir formato si es necesario. -->

# Conformal characterization of the Fefferman-Graham ambient metric

Marc Mars[*] and Gabriel Sánchez-Pérez[]

Departamento de Física Fundamental, Universidad de Salamanca Plaza de la Merced s/n, 37008 Salamanca, Spain

February 6, 2026

## Abstract

In this paper, we study the asymptotic structure of the Fefferman-Graham ambient metric. We prove that every straight ambient metric admits a conformal completion with a well-defined null infinity, and that the asymptotic expansion of the metric at infinity can be related to that at the homothetic horizon. Furthermore, in even dimensions, we show that the Fefferman-Graham obstruction tensor naturally arises in the geometry at infinity. By identifying the fundamental properties that this particular conformal extension exhibits, and analysing their sufficiency, we arrive at the main result of the paper, namely the identification of a set of conformally covariant conditions that completely characterize the ambient metric from a conformal perspective. In particular, our result relaxes the requirement of the homothety one-form being exact. 

## **1 Introduction** 

Homothetic vector fields play a fundamental role both in general relativity and in conformal geometry. Mathematically, they generate scale transformations, providing a natural framework to study conformal invariants and related structures [9]. In mathematical relativity, homotheties often arise as self-similar limits of families of solutions to Einstein’s equations, such as in Christodoulou’s proof of cosmic censorship in spherical symmetry [5]. From the physical side, they are central to the analysis of critical phenomena in gravitational collapse, where self-similarity governs the threshold between dispersion and black hole formation [4, 14]. It is therefore natural to investigate self-similar solutions of Einstein’s equations, with particular attention to their asymptotic behaviour. 

In their seminal work [9] (later expanded into the monograph [10]), Fefferman and Graham developed a powerful formalism to study conformal invariants from a differential geometry perspective. Their construction is based on the observation that the light-cone of a point in Minkowski spacetime (which is a homothetic horizon) encodes the full conformal structure of the sphere, and seeks to extend this picture to arbitrary conformal classes. Beyond its intrinsic mathematical appeal, this formalism has become central in several physically motivated contexts such as holography (see [23] and references therein). The basic idea is to associate to each conformal structure ( _S,_ [ _h_ ]) of signature ( _p, q_ ) another ambient manifold ( _M, g_ ) of signature ( _p_ + 1 _, q_ + 1) satisfying the following properties: (i) ( _M, g_ ) admits a homothetic horizon with homothety _T_ ; (ii) the horizon encodes the conformal structure ( _S,_ [ _h_ ]), in the sense that any of its sections is conformal to ( _S, h_ ); and (iii) the ambient metric is Ricci-flat to all orders at the horizon. 

Starting from a natural ansatz for the ambient metric, Fefferman and Graham write down the derivatives of its Ricci tensor in terms of the derivatives of the metric coefficients. They 

> * marc@usal.es 

>  gasape21@usal.es 

1 

prove that, in odd dimensions, the Einstein equations uniquely determine the coefficients of the ambient metric as a formal power series to infinite order. In even dimensions, however, this recursive determination is only possible up to certain order, and an additional symmetric, traceless tensor must be specified as free data to continue the expansion. In this setting, the so-called obstruction tensor emerges, whose vanishing or not characterizes whether the ambient metric can be Ricci-flat to all orders or not. In both odd and even dimensions, the one-form _**T**_ associated to the homothety is exact (as a one-form) up to the order determined by the equations, namely to infinite order in the odd case, and up to the order of the obstruction in the even case. Moreover, in even dimensions, if the free data satisfies a particular divergence condition, _**T**_ becomes exact to infinite order as well. Ambient metrics satisfying these conditions are known as _straight_ . 

There exist natural generalizations of the ambient metric beyond the smooth class. In the even dimensional case, and when the obstruction tensor does not vanish, one can enforce the Ricci tensor to vanish to infinite order by introducing logarithmic terms into the expansion that compensate the presence of the obstruction tensor, but at the same time spoil the smoothness of the ambient metric at the horizon. In odd dimensions, one can naturally consider solutions with expansions involving half-integer powers which also have an indeterminacy at a certain order. Recall that in the even-dimensional case an indeterminacy also appears. 

The existence of ambient metrics is a intensively studied topic in the literature. For analytic data ( _h,_ Ψ), standard convergence methods can be applied to establish existence of the ambient metric when the obstruction tensor vanishes (see [3]) and also when log terms occur [18]. In the general smooth case, the results in [1, 2, 17] can be used to prove existence of odd dimensional ambient metrics beyond the analytic case. In a remarkable breakthrough, the authors of [24] study a class of metrics, called _self-similar_ , defined as metrics admitting a homothetic horizon and solving _exactly_ the Einstein equations. These metrics are obtained after defining characteristic initial data and applying a suitable scaling limit. One of the fundamental results in [24] is the existence and uniqueness of a self-similar, regular solution realizing prescribed data consisting of a Riemannian metric and a symmetric traceless (0 _,_ 2) tensor. The precise notion of regularity in this construction depends crucially on the spacetime dimension. 

In this paper, we study the Fefferman-Graham ambient metric, with particular emphasis on its asymptotic structure. We prove that every straight ambient metric admits a conformal completion with a well-defined null infinity, and that in even dimensions the Fefferman-Graham obstruction tensor naturally arises in the geometry at infinity, in the sense that the conformal Einstein equations fail to hold at infinity at a certain order of derivatives whenever the Fefferman-Graham obstruction tensor does not vanish. We further study the conformal properties of the ambient metric and identify a necessary and sufficient set of conditions that completely characterize it from a conformal perspective. Finally, we show that the requirement of the homothety one-form _**T**_ being exact can be relaxed, thereby extending the scope of the construction. 

Given a straight ambient metric _g_ in Fefferman-Graham coordinates, we construct a coordinate  transformation and a conformal metric _g_ that extends _g_ to null infinity _J_ . This extension admits a bifurcate Killing horizon with integrable Killing one-form, with one branch corresponding to _J_ and the other to the original homothetic horizon. Moreover, the transverse derivatives of the metric at infinity coincide with the Fefferman–Graham expansion at the horizon. In even dimensions, we further determine the Fefferman-Graham obstruction tensor directly at infinity. 

Having understood the basic features of this particular conformal completion, namely (i) the presence of a Killing field with bifurcate horizon, and (ii) its integrability, it is natural to ask for 

2 

a set of sufficient conditions that determine the ambient metric from a conformal viewpoint. As we shall see, there are three. The first (I) is the existence of a conformal Killing vector admitting a bifurcate horizon, which is the natural conformally-invariant replacement for condition (i). The second (II) is condition (ii), which is already conformally invariant. And finally, we need to ask for an extra condition (III) relating the conformal Killing and the conformal factor in a conformally-covariant way. Our main result (Theorem 4.8) establishes that these three conditions fully characterize the ambient metric. 

**Theorem 1.1** (Informal version) **.** _Let_ ( _M, g,_ Ω) _be a regular conformal spacetime satisfying the conformal Einstein equations with conformal Killing η fulfilling conditions (I)-(III) above. Then, and only then,_ Ω _[−]_[2] _g is a Fefferman-Graham ambient metric._ 

To achieve such result, we identify a particularly convenient subclass of conformal rescalings, that we call _geodesic Killing gauge_ , in which the gradient of the conformal factor is geodesic and the conformal Killing becomes an actual Killing vector. Once ( _M, g,_ Ω) is expressed in any such gauge, we construct a unique R´acz-Wald coordinate system, called _adapted R´acz-Wald coordinates_ , which allows us to relate the transverse expansion of the metric at the homothetic horizon to that at null infinity. Furthermore, we identify the remaining conformal freedom, consisting of arbitrary conformal transformations at the bifurcation surface. This residual freedom coincides precisely with the one in the original Fefferman-Graham construction. 

Besides providing a conformal characterization of the ambient metric, the results in this paper establish an interesting link between the Fefferman-Graham expansion of the ambient metric across the homothetic horizon and at null infinity. This connection will play a significant role in our forthcoming paper [21] where we will address general existence and uniqueness of the asymptotic conformal equations from data at null infinity. As will be shown, the gravitational degrees of freedom of a general asymptotically flat spacetime appear at the same order as the free data in the Fefferman-Graham construction. Moreover, an intrinsic obstruction to the smoothness of _J_ is found to be closely linked to the Fefferman-Graham obstruction tensor at the cuts of _J_ being non-zero. This points to a deep relationship between the ambient metric and a geometric characterization of radiation, which we intend to investigate in future works. 

This paper is organized as follows. In Section 2 we review the Fefferman-Graham construction and its connection with the self-similar metrics studied in [24]. In Section 3 we prove that the ambient metric admits a conformal extension and analyse its key properties. In Section 4 we identify a complete set of sufficient conditions that characterize the ambient metric from a conformal perspective. Finally, Appendix A contains the explicit form of the quasi-Einstein equations in R´acz-Wald coordinates. 

## **Notation and conventions** 

All manifolds in this paper are assumed to be connected and, depending on convenience, both index-free and abstract index notation are used to denote tensorial operations. Spacetime indices are denoted with Greek letters, indices on a hypersurface are written in lowercase Latin letters, and indices at cross-sections of a hypersurface are expressed in uppercase Latin letters. As usual, square brackets enclosing indices denote antisymmetrization and parenthesis are for symmetrization. By _F_ ( _M_ ), X( _M_ ) and X _[⋆]_ ( _M_ ) we denote, respectively, the set of smooth functions, vector fields and one-forms on a manifold _M_ . The subset _F[⋆]_ ( _M_ ) _⊂F_ ( _M_ ) consists of the nowhere vanishing functions on _M_ . A ( _p, q_ )-tensor refers to a tensor field _p_ times contravariant and _q_ times covariant. Given any pair of (2 _,_ 0) and (0 _,_ 2) tensors _A[ab]_ and _Bcd_ we denote tr _A_ _**B**_ := _A[ab] Bab_ . 

3 

## **2 Review of the ambient metric** 

In this section, we summarize the main aspects of the ambient metric construction developed in [10]. The strategy we present differs slightly from the original one in order to simplify the exposition. The basic idea is to associate to each conformal structure of signature ( _p, q_ ) another ambient manifold of signature ( _p_ + 1 _, q_ + 1), as we now review. 

Let ( _S,_ [ _h_ ]) be an n-dimensional smooth conformal structure of signature ( _p, q_ ). Consider the product manifold R[+] _× S_ and denote by _t_ the coordinate in its first factor. Then, after picking up a representative _h ∈_ [ _h_ ] one introduces the vector field _T_ := _t∂t_ and the degenerate bilinear form _**σ**_ := _t_[2] _π[⋆] h_ , where _π_ : R[+] _× S −→ S_ is the projection onto the second factor. Note that _LT_ _**σ**_ = 2 _**σ**_ . 

Now consider the space R _×_ R[+] _× S_ , and denote the coordinate in the first factor by _ρ_ . The idea is to extend _T_ trivially off R[+] _× S_ , and to construct a smooth metric _g_ of signature ( _p_ +1 _, q_ +1) in a neighbourhood of _ρ_ = 0, the so-called _ambient metric_ , such that (i) _T_ is a homothety of _g_ , (ii) the pullback of _g_ into R[+] _× S_ is _**σ**_ and (iii) _g_ is Ricci-flat to infinite order at _ρ_ = 0. As shown in [10], it is sufficient to consider ambient metrics written in _normal form_ , i.e. such that at each point ( _ρ_ = 0 _, t, x_ ) _∈{_ 0 _} ×_ R[+] _× S_ the metric is of the form 

**==> picture [75 x 11] intentionally omitted <==**

and the vector _∂ρ_ is geodesic. The reason is that every ambient metric can be diffeomorphically mapped into one that is written in normal form. Taking all these considerations into account, the line element in a neighbourhood of _ρ_ = 0 can be written as 

**==> picture [317 x 14] intentionally omitted <==**

where _a_ ( _ρ, x[A]_ ), _bA_ ( _ρ, x[A]_ ) and _µ_ ( _ρ, x[A]_ ) are to be determined as a series in _ρ_ by imposing Ricci flatness order by order at _ρ_ = 0. We use the notation _µ_[(] _[m]_[)] , _a_[(] _[m]_[)] , _b_[(] _[m]_[)] to denote the _m_ -th term of the expansion, i.e. _µ_[(] _[m]_[)] := _∂ρ_[(] _[m]_[)] _µ|ρ_ =0, etc. By construction, one has _a_[(0)] = 0, _b_[(0)] = 0 and _µ_[(0)] = _h_ . 

The idea to obtain the expansion _{a_[(] _[m]_[)] _, b_[(] _[m]_[)] _, µ_[(] _[m]_[)] _}m≥_ 1 is as follows. First, the ( _t, t_ ) and ( _t, A_ ) components of the ambient Ricci tensor at _ρ_ = 0 are 

**==> picture [257 x 23] intentionally omitted <==**

where _∇[h]_ is the Levi-Civita connection of _h_ . It is clear that only the choice _a_[(1)] = 1 and _ρ_ =0 _ρ_ =0 _b_[(1)] _A_ = 0 makes _Rtt_ = 0 and _RtA_ = 0. After inserting them into the ( _A, B_ ) components of the ambient Ricci tensor at _ρ_ = 0 one arrives at 

**==> picture [219 x 29] intentionally omitted <==**

where _R_[(] _[h]_[)][the][Ricci][tensor][of] _[h]_[.][Whenever][n] _[>]_[2,][one][can][uniquely][choose] _[µ]_[(1)][make] _AB_[is] _AB_[to] _ρ_ =0 _ρ_ =0 _RAB_ = 0, and when n = 2 equation _RAB_ = 0 is automatically fulfilled because in dimension two every metric satisfies _RAB_[(] _[h]_[)][=] _[R]_ 2[(] _[h]_[)] _[h][AB]_[.][Now][suppose][that] _[a]_[(] _[k]_[)][,] _[b]_[(] _[k]_[)][,] _[µ]_[(] _[k]_[)][(1] _[ ≤][k][≤][m]_[)][have] already been determined. The ( _t, t_ ) component of the ambient Ricci tensor then reads 

**==> picture [157 x 24] intentionally omitted <==**

where _L_[(] _[m]_[)] gathers lower order terms, i.e. terms depending on _a_[(] _[m]_[)] , _b_[(] _[m]_[)] , _µ_[(] _[m]_[)] and below. For every _m_ when n is odd, and for every _m <_ 2[n][when][n][is][even,][one][can][uniquely][choose] _[a]_[(] _[m]_[+1)] 

4 

_ρ_ =0 to make _∂ρ[m][R][tt]_ = 0. Substituting it into the ( _t, A_ ) components ( _L_[(] _A[m]_[)] are again lower order terms), 

**==> picture [228 x 23] intentionally omitted <==**

_ρ_ =0 allows one to determine _b_[(] _A[m]_[+1)] so that _∂ρ[m][R][tA]_ = 0. Finally, the ( _ρ, ρ_ ) and ( _A, B_ ) components read (note the difference in the order of the transverse derivative in the left hand side) 

**==> picture [309 x 23] intentionally omitted <==**

and 

**==> picture [443 x 23] intentionally omitted <==**

where _LAB_ is the Schouten tensor[1] of _h_ and as before _L_[][(] _[m]_[)] and _L_[(] _AB[m]_[)][gather][all][the][lower] order terms, i.e. the terms depending on _a_[(] _[m]_[)] , _b_[(] _[m]_[)] , _µ_[(] _[m]_[)] and below. From (2) one can always _ρ_ =0 choose _h[AB] µ_[(] _AB[m]_[+1)] so that _∂ρ[m][−]_[1] _Rρρ_ = 0 for every _m ≥_ 1. The contracted Bianchi identity _ρ_ =0 _ρ_ =0 _ρ_ =0 then implies that _h[AB] ∂ρ[m][R][AB]_ = 0, _∂ρ[m][−]_[1] _Rρt_ = 0 and _∂ρ[m][−]_[1] _RρA_ = 0 are automatically fulfilled. As a consequence, the only non-trivial equation corresponds to the trace-free part of (3) w.r.t. _h_ . Whenever _m <_ n _/_ 2 _−_ 1 (for n even) and for all _m_ (for n odd), one can uniquely _TF ρ_ =0 choose ( _µ_[(] _AB[m]_[+1)] ) _[TF]_ to make  _∂ρ[m][R][AB]_  = 0 (“TF” denotes the trace-free part w.r.t. _h_ ). So, for n odd, the Einstein equations determine the full transverse expansion of the metric, _{a_[(] _[m]_[)] _, b_[(] _[m]_[)] _, µ_[(] _[m]_[)] _}m≥_ 1, while for n even the expansion is determined up to and including order _{a_[(][n] _[/]_[2)] _, b_[(] _A_[n] _[/]_[2)] _, µAB_[(][n] _[/]_[2] _[−]_[1)] _}_ , because only the trace of the coefficient _µ_[(] _AB_[n] _[/]_[2)] can be determined from the equations. Both in the odd and even cases, _a_ = _ρ_ and _b_ = 0 up to the order they are determined, i.e. _a_[(] _[m]_[)] = _δ_ 1 _[m]_[and] _[b]_[(] _A[m]_[)] = 0 for all _m_ when n is odd, and for all _m_ = 0 _, ...,_ n _/_ 2 when n is even. In general, the metrics constructed in this way are called _ambient metrics_ . 

As already mentioned, for n even the determination of _µ_[(][n] _[/]_[2)] is obstructed due to the vanishing of the coefficient in front of _µAB_[(][n] _[/]_[2)] in (3) when _m_ = 2[n] _[−]_[1.][Therefore,][this][equation][does][not][fix] the trace-free part of the term _µ_[(] _AB_[n] _[/]_[2)][,][which][can][therefore][be][freely][specified][in][the][form][of][a] _TF ρ_ =0 (0 _,_ 2) symmetric, traceless tensor Ψ _AB_ . In addition,  _∂ρ_[n] _[/]_[2] _[−]_[1] _RAB_  = 0 holds if and only if _TF_  _L_[(] _AB_[n] _[/]_[2] _[−]_[1)]  vanishes identically. This tensor (which in general does not vanish) only depends on the initial metric _h_ and it is called _obstruction tensor OAB_ . It has the following properties (indices _A, B, ..._ are raised and lowered with the metric _h_ ): (i) it is traceless _OA[A]_ = 0, (ii) divergence-free _∇[h] B[O][AB]_[=][0,][(iii)][conformally][covariant][and][(iv)][it][vanishes][if] _[h]_[is][Einstein] (but not only). As an example let us study the first non-trivial obstruction tensor, i.e. the one appearing for n = 4[2] . Equation (3) for _m_ = 1 is 

**==> picture [255 x 21] intentionally omitted <==**

where _B_ is the Bach tensor of _h_ . For n = 4, this equation determines the coefficient _µ_[(2)] , but for n = 4 the trace-free part of _µ_[(2)] remains undetermined and the ambient metric can only be Ricci flat provided the Bach tensor of _h_ (which is the obstruction tensor in dimension 4) vanishes. Thus, for n _≥_ 4 even, it is not possible in general to have an ambient metric that is _ρ_ =0 simultaneously more than n _/_ 2 _−_ 1 times differentiable and satisfy _Rαβ_ = 0 to infinite order. 

> 1We recall the definition of this tensor in Section 3, see (6). 

> 2As already discussed, for n = 2 equation _RAB ρ_ ==0 0 holds automatically, and hence there is no obstruction tensor when n = 2. 

5 

_ρ_ =0 If one insists on forcing _Rαβ_ = 0 to infinite order (or, more strongly, in a neighbourhood of the homothetic horizon) then one must include logarithmic terms into the expansion that compensate the presence of the obstruction tensor, but at the same time spoil the smoothness of the ambient metric at the horizon _ρ_ = 0. 

When n is odd, there is no obstruction tensor, but one can naturally consider solutions with expansions involving half-integral powers of _ρ_ which also have an indeterminacy at order n _/_ 2 _ρ_ =0 and that satisfy _Rαβ_ = 0 to infinite order. These ambient metrics are, in general, of class _ρ_ =0 _C[⌊]_[n] _[/]_[2] _[⌋−]_[1] at _ρ_ = 0. To sum up, ambient metrics satisfying _Rαβ_ = 0 to infinite order present the following differentiability: for n = 2 they are smooth; when n _≥_ 4 is even they are, generically, no more than n _/_ 2 _−_ 1 times differentiable; and for n _≥_ 3 odd they are smooth provided there are no half-integer powers, or _⌊_ n _/_ 2 _⌋−_ 1 times differentiable otherwise. 

Given analytic data ( _h,_ Ψ), standard convergence techniques establish existence of the ambient metric [3], even in the presence of a non-vanishing obstruction tensor [18]. In odd dimensions, the works [1, 2, 17] show existence of ambient metrics beyond the analytic setting. In a remarkable breakthrough, the authors of [24] study a class of metrics, called _self-similar_ , defined as metrics admitting a homothetic horizon and solving _exactly_ the Einstein equations on the hyperbolic region, i.e. where the homothety is timelike[3] . They work in double null coordinates in which the metric takes the form 

**==> picture [344 x 16] intentionally omitted <==**

where Θ, _q_ and _/g_ are a function, a one-form and a Riemannian metric¯ on the¯ surfaces _Su,_ ¯ _v_ ¯, respectively. The homothetic vector in these coordinates is _K_ = _v∂v_ ¯ + _u∂u_ ¯ and the homothetic horizon is at _{u_ ¯ = 0 _}_ . Their strategy is to define characteristic initial data on ¯ ¯ _{u_ = 0 _} ∪{v_ = _−_ 1 _}_ to construct self-similar solutions after applying a suitable scaling limit. On _{u_ ¯ = 0 _}_ they specify the lapse Θ, the shift _q_ and the conformal class subject to the normalization conditions Θ _|u_ ¯=0 = 1 and _q|u_ ¯=0 = 0 (according to [24] the condition on Θ is not very relevant, but the one on _q_ is essential to guarantee the regularity of Θ). In principle, there are many ways to prescribe data on the hypersurface _{v_ ¯ = _−_ 1 _}_ , but after the limiting process used by the authors to construct self-similar solutions they show that by prescribing solely a Riemannian metric _h_ and symmetric traceless (0 _,_ 2)-tensor Ψ, there exists a unique self-similar, _regular_ solution such that (i) _/g|S_ 0 _,−_ 1 = _h_ , (ii) Ψ agrees with the trace-free part of the coefficient ¯ _v_[n] _[/]_[2] of _/g_ at _u_ = 0 and (iii) _/g_ satisfies the normalization conditions Θ _|u_ ¯=0 = 1 and _q|u_ ¯=0 = 0. 

The notion of regularity can be understood as follows. For n = 2, _g_ is regular provided it is smooth. When n _≥_ 3 is odd, _g_ is regular provided it is smooth everywhere except at _u_ ¯ = 0, n _−_ 1 and there exists smooth tensors _{gαβ_[(] _[i]_[)] _[}] i_ =02[and] _[g]_[] _[αβ]_[such][that] 

**==> picture [175 x 37] intentionally omitted <==**

Finally, when n _≥_ 4 is even, _g_ is regular if it is smooth everywhere except at _u_ ¯ = 0, and there n exists smooth tensors _{gαβ_[(] _[i]_[)] _[}] i_ 2=0[and] _[g]_[] _[αβ]_[such][that] 

**==> picture [297 x 36] intentionally omitted <==**

> 3In [15] a similar result showing existence in the elliptic region is shown, with the main difference that no free data at order n _/_ 2 needs to be prescribed in this case. We are grateful to R. Graham for pointing out this reference. 

6 

Observe that this definition of regularity is in complete agreement with the differentiability for Fefferman-Graham ambient metrics discussed above. 

One natural question is whether an _exact ambient metric_ (i.e. one solving _Rαβ_ = 0 in a neighbourhood of the horizon) is self-similar in the sense of [24] and vice-versa. There is one specific situation where exact ambient metrics and self-similar metrics are in one-to-one correspondence, namely when the ambient metric is _straight_ . 

## **2.1 Straightness** 

One says that an ambient metric is straight provided the homothety _T_ satisfies _d_ _**T**_ = 0. Proposition 3.4 of [10] shows that this is equivalent to _**T**_ being exact in a full neighbourhood of the horizon, and also equivalent to _a_ = 1 and _bA_ = 0. In fact, the metric (1) with _a_ = 1 and _bA_ = 0 satisfies _Rtt_ = _Rtρ_ = _RtA_ = 0 exactly. As we already discussed, one of the results in [10] is that every ambient metric is straight up to the order determined by the initial metric _h_ , i.e. to infinite order for n odd (and no half integers are allowed) and up to and including order n _/_ 2 when n is even. The question of whether the metric is straight to infinite order depends on the free data Ψ. When n is even, the (n _/_ 2 _−_ 1) _ρ_ -derivative of the ( _ρ, A_ ) components of the Einstein equations read 

**==> picture [337 x 23] intentionally omitted <==**

where _DA_ is a one-form that depends only on _h_ . Hence, the condition _∇[B]_ Ψ _AB_ = _DA_ is necessary for the ambient metric to be simultaneously Ricci flat and straight to infinite order. As proven in [10, Thm. 3.10], it is also sufficient. When n is odd, the ambient metric is straight to infinite order if and only if _∇B_ Ψ _[AB]_ = 0 (see [10, Thm. 3.9]). One can combine these two conditions into a single one by just writing _∇B_ Ψ _[AB]_ = _D[A]_ , letting _DA_ be identically zero when n is odd. 

In the context of self-similar metrics, Proposition B.7 of [24] shows that whenever the free data Ψ satisfies _∇B_ Ψ _[AB]_ = _D[A]_ , the metric (4) has vanishing torsion one-form _ζ_ and scalar _ω_[4] . These are given in terms of Θ and _q_ by _ω_ = _−_[1][and] _[ζ][A]_[=] _[−]_[1][Thus,][the] 2 _[∇]_[4][(log Θ)] 4[Θ] _[−]_[1] _[e]_[4][(] _[q][B]_[)] _[/g][AB]_[.] self-similar solutions that satisfy _∇[B]_ Ψ _AB_ = _DA_ also have Θ = 1 and _q_ = 0 everywhere. The change of coordinates _t_ = _v_ ¯ and _ρ_ = _u_ ¯ _v_ ¯ _[−]_[1] in (4) leads to 

**==> picture [172 x 16] intentionally omitted <==**

which after identifying _/g_ = _t_[2] _µ_ happens to be a straight, exact ambient metric. In the rest of the paper we will focus on straight metrics, so we will not make a distinction between selfsimilar metrics and exact ambient metrics. One can rephrase Theorem 1.3 of [24] in terms of straight, exact ambient metrics as follows. 

**Theorem 2.1** ([24]) **.** _Let h be a Riemannian metric and_ Ψ _a symmetric, traceless tensor field on S that satisfies ∇[B]_ Ψ _AB_ = _DA, where DA is an explicit one-form that only depends on h when_ n _is even, and identically zero for_ n _odd. Then, there exists a unique straight, exact and regular ambient metric such that g|S_ = _h and_ Ψ _agrees with the trace-free part of the coefficient u_ ¯[n] _[/]_[2] _of g at the horizon._ 

> 4 In double null coordinates, the torsion _ζ_ and the function _ω_ are defined by _ζA_ :=[1][and] _[ω]_[:=] 2 _[g]_[(] _[∇][A][e][a][, e]_[3][)] _−_[1][where] _[e]_[3][:= Θ] _[−]_[1] _[∂][v]_[¯][and] _[e]_[3][:= Θ] _[−]_[1][(] _[∂][u]_[¯][ +] _[ q][A][∂][A]_[)][are][null][vectors][satisfying] _[g]_[(] _[e]_[3] _[, e]_[4][) =] _[ −]_[2.] 4 _[g]_[(] _[∇]_[4] _[e]_[3] _[, e]_[4][),] 

7 

## **3 Conformal completion and null infinity** 

In this section we show that the ambient metric admits a conformal completion with a null conformal infinity. Before proving this we first recall the key aspects of the conformal Einstein equations. For details see [12, 11, 13]. We start by fixing some notation. Given a semiRiemannian manifold ( _M, g_ ) of dimension _d ≥_ 3 the Schouten tensor is defined by 

**==> picture [308 x 27] intentionally omitted <==**

where Ric _g_ and Scal _g_ are the Ricci tensor and scalar, respectively. Reciprocally, the expression of the Ricci tensor in terms of the Schouten is given by 

**==> picture [356 x 26] intentionally omitted <==**

where as in Section 2 we employ the symbols _Lαβ_ and _L_ for the Schouten tensor and its trace in index notation, and we used that _L_ = 2(Scal _d−g_ 1)[.][From][the][transformation][of][the][Ricci][tensor] under a conformal rescaling _g_ = _ω[m] g_ , namely 

**==> picture [451 x 89] intentionally omitted <==**

where in this case “tf” denotes the trace-free part w.r.t. _g_ (or w.r.t. _g_ , since “tf” is a conformally invariant operation). Let ( _M,_ [ _g_ ]) be a _d_ -dimensional conformal structure. For each _g ∈_ [ _g_ ] one constructs the differential operator 

**==> picture [337 x 17] intentionally omitted <==**

From the conformal transformation law of _∇_ and Sch _g_ one can check that 

**==> picture [274 x 13] intentionally omitted <==**

Recall that (in dimension _d ≥_ 3) _g_ is an Einstein metric if and only if Sch _[tf] g_[= 0.][Then, putting] _f_ = 1 in (9) and _ω_ = Ωin (9)-(10) one gets 

**==> picture [293 x 16] intentionally omitted <==**

The previous equation can be written equivalently in terms of the scalar s := _d[−]_[1][] □ _g_ Ω+ Ω _L_  as Hess _g_ Ω+ ΩSch _g −_ s _g_ = 0 _._ (11) 

A 3-tuple ( _M, g,_ Ω) is a (vacuum) quasi-Einstein manifold provided that (11) is satisfied. Property (10) guarantees that if ( _M, g,_ Ω) is quasi-Einstein and _ω ∈F[⋆]_ ( _M_ ), then ( _M, ω_[2] _g, ω_ Ω) is also quasi-Einstein. One important consequence of this definition is that the quantity 

**==> picture [266 x 15] intentionally omitted <==**

is constant (and conformally invariant). Ignoring an irrelevant numerical factor, the constant _λ_ corresponds to the cosmological constant associated to Ω _[−]_[2] _g_ , which is the Einstein representative of ( _M, g,_ Ω). 

8 

## **3.1 Conformal completion of the ambient metric** 

Let us consider a straight ambient metric 

**==> picture [284 x 14] intentionally omitted <==**

and the change of coordinates _{t, ρ} −→{t, u_ := _ρt}_ , under which (13) takes the form 

**==> picture [264 x 13] intentionally omitted <==**

where now _µ_ is a series in powers of _[u] t_[.][In][these][coordinates][the][homothetic][horizon][(] _[ρ]_[ = 0)][is] placed at _u_ = 0, and the infinity is reached when _t →∞_ . Introducing the coordinate _v_ := _t[−]_[1] the metric (14) becomes 

**==> picture [281 x 14] intentionally omitted <==**

where now _µ_ is a series in powers of _uv_ . Then, the metric 

**==> picture [280 x 13] intentionally omitted <==**

is extendible beyond _J_ := _{v_ = 0 _}_ , the (null) conformal infinity of the ambient metric. Note that if _g_ is Ricci flat, then ( _g, v_  ) satisfies (11). Following the notation of Section 2, for n odd the tensor _µ_ is given as a formal series by 

**==> picture [213 x 38] intentionally omitted <==**

while for n _≥_ 4 even _µ_ is given by 

**==> picture [362 x 36] intentionally omitted <==**

As already said, the case n = 2 is special because no obstruction tensor appears and the ambient metric is always smooth. 

Note that in these coordinates the vector _T_ is given by _T_ = _u∂u − v∂v_ . It is straightforward  to check that _T_ is a Killing vector w.r.t _g_ and that the set _{u_ = 0 _} ∪{v_ = 0 _}_ is a (nondegenerate) bifurcate Killing horizon with bifurcation surface _{u_ = _v_ = 0 _}_ . Also note that the straightness condition implies that the one-form _**T**_[] :=  _g_ ( _T, ·_ ) is integrable in the conformal manifold ( _M_[] := _M ∪ J ,_  _g,_ Ω), i.e. _**T** ∧ d_ _**T**_  = 0. Being part of a Killing horizon, it follows that _J_ is a totally geodesic null hypersurface with first fundamental form _h_ . Moreover, the transverse derivatives of _g_  at _{v_ = 0 _}_ are 

**==> picture [191 x 17] intentionally omitted <==**

while the transverse derivatives along _s_ := _uv_ at _s_ = 0 are given by[5] 

**==> picture [315 x 15] intentionally omitted <==**

This means that the free data Ψ _AB_ agrees with the trace-free part of the coefficient in _s_[n] _[/]_[2] . 

Particularizing equation (12) to _λ_ = 0 and taking into account that _|∇_[] Ω _|_[2] _g_ [=] _[|][∇]_[] _[v][|]_[2] _g_ [=][0][it][fol-] lowsbe writtenthat s = 0,as _Qαβ_ so= 0. _Qαβ_ In:=other _∇_[] _α∇_[] _β_ words,Ω+ Ω _L_[] if _αβg_ is= _Q_ exactly _[tf] αβ_[and] Ricci[thus] flat,[the] then[quasi-Einstein] _g_  satisfies[equations] _Qαβ_ = 0.[can] Let 

> 5 _A_ We use _∂s_ as the derivative w.r.t. the product _uv_ for functions that only depend on ( _uv, x_ ). 

9 

_ρ_ =0 us consider an even dimensional ambient metric constructed by solving _∂ρ_[(] _[m]_[)] _Rαβ_ = 0 up to an including order _m_ = n _/_ 2 _−_ 2. As we discussed before, the determination of the next coefficient of the expansion is (in general) obstructed, in the sense that ( _∂ρ_[(][n] _[/]_[2] _[−]_[1)] _RAB_ ) _[TF][ρ]_ =[=0] _OAB_ = 0, where _OAB_ is the obstruction tensor of _h_ = _µ_[(0)] . This obstruction can also be detected at _J_ , as we explain next. 

_ρ_ =0 _ρ_ =0 _ρ_ =0 _ρ_ =0 First observe that _∂ρ[m][R][αβ]_ = 0 _∀m ≤_ n _/_ 2 _−_ 2 implies _∂ρ[m][L][αβ]_ = 0 and _∂ρ[m][R]_ = _∂ρ[m][L]_ = 0 _∀m ≤_ n _/_ 2 _−_ 2 ( _R_ and _L_ are the Ricci and Schouten scalars of _g_ , respectively), so (cf. (6)) 

**==> picture [349 x 36] intentionally omitted <==**

and therefore 

**==> picture [139 x 16] intentionally omitted <==**

Recalling that _L[tf] αβ_[=] _[L]_[] _[tf] αβ_[+ Ω] _[−]_[1][] Hess _g_  Ω _tfαβ_[= Ω] _[−]_[1] _[Q][αβ]_[(see][(][8][))][it][follows][that] 

**==> picture [347 x 84] intentionally omitted <==**

and then (note that _∂ρ_ Ω= _∂ρt[−]_[1] = 0) 

Under the transformation _{t_ = _v[−]_[1] _, ρ_ = _uv}_ this expression becomes (note that _∂ρ_ = _v[−]_[1] _∂u_ ) 

( _∂ρ_[n] _[/]_[2] _[−]_[1] _LAB|ρ_ =0) _[TF]_ = _v[−]_[n] _[/]_[2] ( _∂u_[n] _[/]_[2] _[−]_[1] _QAB|u_ =0) _[TF]_ = _⇒ OAB_ = n _v[−]_[n] _[/]_[2] ( _∂u_[n] _[/]_[2] _[−]_[1] _QAB|u_ =0) _[TF] ._ 

We are interested in obtaining an expression relating the obstruction tensor with transverse derivatives of the tensor _Q_ at null infinity, i.e. derivatives of _Q_ w.r.t. _∂v_ at _v_ = 0. In other words, we want to “interchange” the roles of _u_ and _v_ in the formula for _OAB_ we have just obtained. In order to do that, we exploit the fact that _uv_ = 0 is a bifurcate Killing horizon. Indeed, since _Q_ = Hess _g_  _v_ + _v_ Sch _g_  and _T_ = _u∂u−v∂v_ is a Killing vector of  _g_ , one has _LT Q_ = _−Q_ and hence _T_ ( _QAB_ ) = _−QAB_ . This implies that _QAB_ is of the form _QAB_ = _vTAB_ ( _uv, x[C]_ ), and hence 

**==> picture [289 x 17] intentionally omitted <==**

where _T_[(] _[m]_[)] denotes the _m_ -th derivative w.r.t. _uv_ and we used that _TAB_ ( _uv, x[C]_ ) _|u_ =0 = _TAB_ ( _uv, x[C]_ ) _|uv_ =0. Recall that _∂u[k]_[=] _[ v][k][∂] s[k]_[and] _[∂] v[k]_[=] _[ u][k][∂] s[k]_[for][every] _[k]_[,][and][note][also][that] 

**==> picture [297 x 16] intentionally omitted <==**

where we have used that _∂u[k]_[(] _[u][k][T]_[ (] _AB[k]_[)][)] _[|][v]_[=0][=] _[k]_[!] _[T]_[ (] _AB[k]_[)] _[|][v]_[=0][.][Note][also][that][the][horizon][is][totally] geodesic and then _∂u_ and _∂v_ commute with _TF_ . Then, 

**==> picture [336 x 73] intentionally omitted <==**

This shows that the presence of a non-vanishing obstruction tensor can also be detected from the conformal infinity, as it makes the n _/_ 2-transverse derivative of the tensor _Q_ at _J_ to be different from zero. 

10 

## **4 Conformal characterization of the ambient metric** 

In this section we characterize the ambient metric from a conformal viewpoint. More specifically, we want to find a set of conformally covariant conditions on a conformal manifold ( _M, g,_ Ω) that univocally lead to the ambient metric. As we studied in the previous section, the conformal completion of the ambient metric exhibits two key properties, namely the existence of a bifurcate Killing horizon where one of the horizons is _J_ , and that the one-form _**T**_ is integrable. While the latter condition is already conformally invariant, the former is not. The obvious replacement is to ask for the existence of a bifurcate _conformal_ Killing horizon. Additionally, it is clear that one should impose some extra condition relating the conformal Killing field (that we now denote by _η_ to avoid confusion with the previous section) and the function Ω. In the conformal completion of the previous section Ω= _v_ and _T_ = _u∂u − v∂v_ , so _T_ (Ω) = _−v_ . The natural replacement for this condition is to ask that _η_ (Ω) =  _ψ −_ 1Ω, where _ψ_ is the function such that _Lηg_ = 2 _ψg_ . That this condition is conformally invariant follows because under a conformal rescaling _g[′]_ := _ω_[2] _g_ the function _ψ_ transforms by _ψ[′]_ = _ψ_ + _η_  log _|ω|_ , and hence _η_ ( _ω_ Ω) = _ωη_ (Ω) + _ω_ Ω _η_  log _|ω|_  =  _ψ[′] −_ 1) _ω_ Ω. The main result of this paper is that these three conditions fully characterize the Fefferman-Graham ambient metric (Theorem 4.8). We start by showing that the function _ψ_ necessarily vanishes at the bifurcation surface. 

**Lemma 4.1.** _Let η be a conformal Killing field and ψ the function defined by Lηg_ = 2 _ψg. Assume η admits a bifurcation surface S. Then, ψ|S_ = 0 _._ 

_Proof._ Let _V, W ∈ T S_ . Since [ _η, V_ ] = 0 _[S]_ it follows _∇V η_ = 0, _[S]_ and then 

**==> picture [149 x 17] intentionally omitted <==**

Since _V, W_ are arbitrary it follows that _ψ_ = 0. _[S]_ 

Next we show that it is possible to fix the gauge such that _|∇_ Ω _|_[2] = 0. 

**Lemma 4.2.** _Let_ ( _M, g,_ Ω) _be a conformal manifold with λ_ = 0 _and H a hypersurface trans-_  _verse to J . Let ω_ 0 _be a non-vanishing function on H. Then, there exists a unique_ ( _g_ = _ω_[2] _g,_ Ω=[] _ω_ Ω) _in a neighbourhood of J ∩H such that |∇_[] Ω[] _|_[2] _g_ [= 0] _[and]_[Ω][][=] _[H][ ω]_[0][Ω] _[.]_ 

_Proof._ Let ( _M, g,_ Ω) be a conformal manifold, _ω >_ 0 a function, and define _g_  := _ω_[2] _g_ , Ω:=[] _ω_ Ω and _F_ := _|∇_ Ω _|_[2] _g_[.][Then,] 

**==> picture [219 x 16] intentionally omitted <==**

where we defined _f_ := log _ω_ . We want to show that the equation _F_[] = 0 admits a unique solution given the function _f_ in a hypersurface transverse to _J_ . Since _F |_ Ω=0 = 0, the function Ω _[−]_[1] _F_ has a good limit at Ω= 0 and henceforth we can equivalently look for solutions to the following equation 

**==> picture [327 x 14] intentionally omitted <==**

In order to do that we use the method of characteristics (see [8]), which basically consists of rewriting the PDE as a first order system of ODEs for _f_ and its gradient _p[α]_ := _∇[α] f_ along the so-called characteristic curves, with the aim of solving it from data at a hypersurface _H_ . In our specific setup, since _∇[α]_ Ωis tangent to _J_ , it is also necessarily transverse to _H_ (at least in a neighbourhood of _H ∩ J_ ). Then, we can complete any local coordinate system _{x[a] }_ on _H_ to a local coordinate system _{x_[0] _, x[a] }_ on _M_ by extending _{x[a] }_ trivially along _∇_ Ω, and solving _∇_ Ω( _x_[0] ) = 1, _x_[0] _|H_ = 0 (then, _∇_ Ω= _∂x_ 0). Given a smooth function _f_ on _H_ , an initial condition for _p_ is called admissible provided that _pa|H_ = _dfa_ and _F_[] _[′]_ ( _f, p|H_ ) = 0. _[H]_ Note that, in general, a covector _p|H_ satisfying these conditions may not exist or may not be unique. It is only when the 

11 

problem is non-characteristic, i.e. _ξ[α] DpαF_[] _[′] |H_ = 0 for any non-vanishing vector _ξ_ transverse to _H_ , when a unique solution for _p_ exists. In our specific setup, choosing _ξ_ = _∇_ Ω= _∂x_ 0, equation (18) becomes 

**==> picture [300 x 14] intentionally omitted <==**

and then one can check that _ξ[α] DpαF_[] _[′] |H_ = _Dp_ 0 _F_[] _[′]_ = 2+ _O_ (Ω), so _Dp_ 0 _F_[] _[′]_ = 0 in a neighbourhood of _H ∩ J_ . This proves that the problem is non-characteristic and therefore the equation _|∇_ Ω _|_[2] _g_[=][0][admits][a][unique][solution][given][the][function] _[ω]_[on][a][hypersurface][transverse][to] . _J_ 

Let ( _M, g,_ Ω) be a conformal manifold admitting a bifurcate conformal Killing horizon such that one of the horizons is _J_ . Let _η_ be the conformal field and _ψ_ the function satisfying _Lηg_ = 2 _ψg_ . Assume also that _η_ (Ω) =  _ψ −_ 1Ω. Now we show that one can restrict further the gauge to set _ψ_ = 0. 

**Proposition 4.3.** _Let_ ( _M, g,_ Ω) _be a conformal manifold admitting a bifurcate conformal Killing vector η where one of the horizons is J and η_ (Ω) = ( _ψ −_ 1)Ω _. Then, there exists a conformal gauge in which simultaneously |∇_ Ω _|_[2] = 0 _and Lηg_ = 0 _in a neighbourhood of the bifurcation surface. Moreover, the remaining gauge freedom is a function ω_ ( _x[A]_ ) _._ 

_Proof._ We choose the transverse hypersurface _H_ of the previous proposition as the conformal Killing horizon transverse to _J_ , so that _η_ is tangent to _H_ and _S_ := _H ∩ J_ is the bifurcation surface of _η_ . The idea of the proof is to show that one can make _ψ_ to vanish at _H_ by choosing the free function _ω_ of the proposition to satisfy _ψ[′]_ = _ψ_ + _η_ (log _ω_ ) = 0 at _H_ , and then to prove that condition _|∇_ Ω _|_[2] = 0 implies that _ψ_ vanishes everywhere. Recall by Lemma 4.1 that _ψ_ = 0 at _H∩ J_ , so in order to prove that the equation _ψ_ + _η_ (log _ω_ ) = 0 along _H_ admits a solution we must show that _η|H_ has a zero of order one at _S_ . We choose double null coordinates _{v, u, x[A] }_ adapted to _J_ = _{v_ = 0 _}_ and _H_ = _{u_ = 0 _}_ , where the metric is given by 

**==> picture [223 x 16] intentionally omitted <==**

Note that _n_ := _∂v − q[A] ∂xA_ is a null generator of _H_ and by construction _η|H_ = _Hn_ for some function _H_ defined on _H_ . We want to show that _H_ satisfies _H|v_ =0 = 0 and _∂vH|v_ =0 = 0. 

Consider the equation _η[α] ∇α_ Ω= ( _ψ −_ 1)Ω. Applying _∇β_ to both sides it follows that 

**==> picture [231 x 12] intentionally omitted <==**

**==> picture [358 x 34] intentionally omitted <==**

which evaluated at _S_ gives _Fβ[α] ∇α_ Ω= _−∇β_ Ω. Since _d_ Ω= _fdv_ on _v_ = 0 with _f_ = 0 it _S_ follows that _Fβ[v]_ = _−δβ[v]_[,][and][hence][taking] _[β]_[=] _[v]_[and][using][that] _[g][vα]_[=] _[G][−]_[1] _[δ] u[α]_[we][get] _[F][vu]_ = _S S S ∂vηu − ∂uηv_ = 2 _∂vηu_ = _−G ̸_ = 0, where we used _∂αηβ_ + _∂βηα_ = 0. Since _**η** |H_ = _g_ ( _η, ·_ ) _|H_ = _Hdu_ we conclude _∂vH|S_ = 0, so _η|H_ has a zero of order one at _S_ and then equation _ψ_ + _η_ (log _ω_ ) = 0 admits a solution along _H_ . 

Once we have guaranteed that (part of) the remaining freedom in Prop. 4.2 can be chosen so that _ψ_ = 0 on _H_ , it remains to show that _ψ_ actually vanishes everywhere. Using that _Lη_ ( _g[αβ]_ ) = _−_ 2 _ψg[αβ]_ , 

**==> picture [258 x 50] intentionally omitted <==**

12 

Then, in a gauge in which _|∇_ Ω _|_[2] = 0 one has _∇α_ Ω _∇[α] ψ_ = 0, and since _∇α_ Ωis transverse to _H_ , the condition _ψ_ = 0 _[H]_ extends to a neighbourhood of _S_ . 

An immediate corollary of this proposition is the following. 

**Corollary 4.4.** _Let f_ 1 _and f_ 2 _be two functions satisfying |∇f_ 1 _|_[2] = _|∇f_ 2 _|_[2] = 0 _and η_ ( _f_ 1) = _−f_ 1 _, S η_ ( _f_ 2) = _−f_ 2 _. Assume f_ 1 = _f_ 2 _. Then, f_ 1 = _f_ 2 _._ 

_Proof._ In Proposition 4.3 it is shown that the solution to _|∇f |_[2] = 0 and _η_ ( _f_ ) = _−f_ is characterized by a free function _ω_ on _S_ . Since both _f_ 1 and _f_ 2 agree on _S_ the function _ω_ is identically 1, and then _f_ 1 = _f_ 2 everywhere. 

In this conformal gauge, from now on called _geodesic Killing gauge_ , the metric _g_ admits a bifurcate Killing horizon, so it can be written in R´acz-Wald coordinates as [25] 

**==> picture [321 x 15] intentionally omitted <==**

where _G_ , _**β**_ and _µ_ are a function, a one-form and a metric on the codimension-two surfaces _Su,v_ that depend only upon _{s_ := _uv, x[A] }_ . In these coordinates the Killing field is given by _η_ = _u∂u − v∂v_ . We note that in the geodesic Killing gauge, the vector field gradΩis geodesic (hence the name). This follows from 0 = _∇β_ ( _∇α_ Ω _∇[α]_ Ω) = 2 _∇[α]_ Ω _∇α∇β_ Ω= 0. 

The R´acz–Wald (RW) construction allows for the freedom to choose any cross-section Σ on _{v_ = 0 _}_ (not intersecting the bifurcation surface _S_ ). From this surface, the coordinate _u_ is uniquely defined so that _u|S_ = 0, _u|_ Σ = 1, and _∂u_ is geodesic. Given any conformal factor Ωin a geodesic Killing gauge, we fix the RW coordinate _u_ as follows. Choose the family of geodesic ˙ curves _γ_ ( _τ_ ) on _{v_ = 0 _}_ satisfying _τ |S_ = 0 and _γ|S_ = gradΩ _|S_ (note that gradΩis tangential to the hypersurface _{v_ = 0 _}_ ). We then choose Σ := _{τ_ = 1 _}_ in the construction described ˙ above. Since _u|S_ = _τ |S_ = 0, _u|_ Σ = _τ |_ Σ = 1, and both _∂u_ and _γ_ are geodesic, it follows that _u_ = _τ_ , so gradΩ _[v]_ =[=0] _∂u_ . In particular, _d_ Ω = _[S] Gdv_ . The resulting RW coordinates only admit an additional scaling freedom for the coordinate _v_ of the form _v_ = _vh_ ¯ ( _x[A]_ ). Next, we show that one can rescale the coordinate _v_ to set _**β**_ = 0 locally when _η_ is integrable. **Lemma 4.5.** _Assume that the Killing η_ = _u∂u − v∂v is integrable w.r.t the metric_ (20) _. Then_ _**β** is closed, and hence locally exact._ 

**==> picture [458 x 57] intentionally omitted <==**

where the dot denotes derivative w.r.t. _s_ and _/d_ is the exterior derivative on the codimension two surfaces _Su,v_ . Since the four terms on the RHS are linearly independent, the last term shows that _/d_ _**β**_ = 0 (note that although the computation has been done away from _u_ = 0 or _v_ = 0, by continuity the result is valid everywhere). 

**Corollary 4.6.** _Assume the Killing η_ = _u∂u − v∂v is integrable w.r.t the metric_ (20) _. Then, there exists a change of coordinates that respects the form of η and such as the metric takes the form_ (20) _with_ _**β**_ = 0 _, i.e._ 

**==> picture [265 x 12] intentionally omitted <==**

_Proof._ Since _**η**_ is integrable, by the previous lemma it is locally exact, i.e. there exists a function _f_ such that _**β**_ = _df_ . Moreover, since _**β**_[˙] = 0 it follows that _f_ = _f_ ( _x[A]_ ). Inserting this and _v_ = _vh_ ¯ ( _x[A]_ ) into (20) yields 

**==> picture [165 x 14] intentionally omitted <==**

13 

By choosing _h_ such that _dh_ + _hdf_ = 0 and redefining _G_ , the metric _g_ takes (locally) the form ¯ ¯ (21). Note that this change keeps the same form of _η_ , since _v∂v_ = _hvh[−]_[1] _∂v_ ¯ = _v∂v_ ¯. 

Note that this change of _v_ does not affect the coordinate _u_ and that the remaining freedom is scaling _v_ by a non-zero constant. In these new coordinates, we still have _d_ Ω = _[S] Gdv_ . This means that Ω= _vF_ , where _F_ satisfies _F |S_ = _G|S_ . Since _η_ (Ω) = _−_ Ωand _η_ ( _v_ ) = _−v_ it follows that _η_ ( _F_ ) = 0 and thus _F_ = _F_ ( _uv, x[A]_ ). 

 Next, we define Ω:=[] _F[−]_[1] Ωand _g_ := _F[−]_[2] _g_ (note that Ω=[] _v_ ). We write the metric as   _g_ = 2 _Gdudv_[] + _µ_ and note that _G_[] = _F[−]_[2] _G_ , and in particular _G_[] _|S_ = _F[−]_[1] _|S_ (this is the key reason for our specific choice of RW coordinates above). Using the conformal covariance of the equations, showing that ( _g,_ Ω) is quasi-Einstein is equivalent to showing that ( _g, v_  ) satisfy _Q_ := Hess _v_ + _v_ Sch _g_  _−_ s _g_ = 0 (note that a priori the conformal factor Ωneed not to satisfy _|∇_ Ω[] _|_[2] _g_ [=][0,][i.e.][we][have][momentarily][abandoned][the][geodesic][Killing][gauge][and][the][term][s] _[g]_[] appears in the conformal Killing equations). In Appendix A we have computed the components of the tensor Hess _v_ + _v_ Sch _g_  for the metric (21). In particular, we are interested in the equations    _Qvv_ = 0 and _QvA_ = 0. Since _gvv_ = _gvA_ = 0, the ( _v, v_ ) and ( _v, A_ ) equations that ( _g, v_ ) satisfy are obtained by simply replacing _G_ by _G_[] and _µ_ by _µ_ . In particular, equation _Qvv_ = 0 is 

**==> picture [193 x 31] intentionally omitted <==**

which proves _G_[][˙] = 0 (at least in a neighbourhood of _s_ = 0), and equation _QvA_ = 0 reads 

**==> picture [247 x 29] intentionally omitted <==**

which evaluated at _s_ = 0 implies _G_[] = _A ∈_ R _\ {_ 0 _}_ is constant on _s_ = 0 (we assume _S_ is connected), and hence everywhere. It follows that _F |S_ = _A[−]_[1] . Now, in the original geodesic Killing gauge we have that Ωsatisfies _|∇_ Ω _|_[2] _g_[= 0][and] _[L][η]_[Ω=] _[ −]_[Ω.][The][function] _[v]_[has][the][same] properties and satisfies Ω= _A[−]_[1] _v_ on _S_ , so by Corollary 4.4 one has Ω= _A[−]_[1] _v_ and _F_ = _A[−]_[1] everywhere. Moreover, _G_ = _GF_[][2] = _A[−]_[1] because _G_[] = _A_ . Performing a final constant rescaling of _v_ we finally arrive at 

**==> picture [288 x 12] intentionally omitted <==**

We emphasize that we have arrived at this expression starting with any Ωthat belongs to the geodesic Killing gauge. The RW coordinates _{u, v}_ in the final metric (22) are fully determined in terms of Ω. We call them _adapted R´acz-Wald coordinates_ . A conformal change within the geodesic Killing gauge has a highly non-trivial effect in the coordinates _{u, v}_ and also on _µ_ . However, at _S_ , the effect is simple. Any other Ωin[] this gauge is uniquely parametrized by a ˜ positive function _ω_ on _S_ by means of Ω[] _|S_ = _ω_ Ω _|S_ , and then _µ|S_ = _ω_[2] _µ|S_ . So our construction keeps the full conformal freedom at _S_ . This is exactly the conformal freedom that exists in the original Fefferman-Graham construction. 

 Whenever ( _g,_ Ω) is quasi-Einstein one has that _g_ = Ω _[−]_[2] _g_ = _v[−]_[2] (2 _dudv_ + _µ_ ) is Ricci flat. Defining _u_ ¯ := _u_ and _v_ ¯ := _v[−]_[1] one finds 

**==> picture [91 x 13] intentionally omitted <==**

Therefore, this metric is exactly Ricci flat, admits a homothetic horizon (¯ _u_ = 0) and it is written in a double null coordinate system with Θ = 1, _q_ = 0 and _/g_ = _v_ ¯[2] _µ_ . This proves that the class of ambient metrics of Theorem 2.1 is in one-to-one correspondence with the class of quasi-Einstein manifolds ( _M, g,_ Ω) that we have considered in this section. 

14 

**Proposition 4.7.** _There exists a one-to-one correspondence between straight, exact and regular ambient metrics and quasi-Einstein manifolds_ ( _M, g,_ Ω) _with λ_ = 0 _admitting an integrable conformal field Lηg_ = 2 _ψg satisfying Lη_ Ω= ( _ψ −_ 1)Ω _and such that η admits a bifurcate horizon where one of the horizons is J ._ 

This result relaxes the condition of _η_ being closed. As a consequence of the regularity in Theorem 2.1 and relation (17), the regularity of _g_ is as follows: For n = 2, _g_ is smooth. When n _−_ 1 nand _≥_ 3 is odd, _g_  _αβ_ such _g_ thatis smooth everywhere except at _s_ = 0, and there exists smooth tensors _{gαβ_[(] _[i]_[)] _[}] i_ =02 

**==> picture [171 x 37] intentionally omitted <==**

Finally, when n _≥_ 4 is even, _g_ is smooth everywhere except at _s_ = 0, and there exists smooth n tensors _{gαβ_[(] _[i]_[)] _[}] i_ 2=0[and] _[g]_[] _[αβ]_[such][that] 

**==> picture [297 x 37] intentionally omitted <==**

This allows us to identify the free data from the conformal picture as follows. 

**Theorem 4.8.** _Let_ ( _M, g,_ Ω) _be a regular quasi-Einstein manifold of dimension_ n + 2 _that admits an integrable conformal Killing vector Lηg_ = 2 _ψg and a bifurcate horizon where one of the horizons is J_ = _{_ Ω= 0 _} ≃S ×_ R _and such that Lη_ Ω= ( _ψ −_ 1)Ω _. Write_ ( _g,_ Ω) _in a geodesic Killing gauge and let h be the metric of the bifurcation surface S and_ Ψ _the trace-free part of the term s_[n] _[/]_[2] _in the expansion of g in adapted R´acz-Wald coordinates. Then,_ Ω _[−]_[2] _g is the exact, straight and regular ambient metric with data_ ( _S, h,_ Ψ) _._ 

Beyond its intrinsic mathematical interest, we believe that Theorem 4.8 may also be relevant to the physics community, in particular in the context of holography and AdS/CFT. One open problem in flat holography concerns the precise relation between observables in a conformal field theory (defined on the lightcone) and observables at null infinity (see e.g. [7, 22]). This question has a strong parallel with the work presented in this paper. We are grateful to an anonymous referee for drawing our attention to this connection. 

It is also instructive to see how this free data appears by analysing the conformal Einstein equations order by order at _s_ = 0. Let us consider the ( _A, B_ ) and ( _v, u_ ) components of the quasi-Einstein equations of the metric (21), that we write again here for completeness (see Appendix A) 

**==> picture [405 x 97] intentionally omitted <==**

In order to study how the equations fix the geometry order by order at _s_ = 0 we start by solving _Quv s_ ==0 0 for tr _µ µ_ ˙ , which gives tr _µ µ_ ˙ = n _−_ 1 1 _[R]_[(] _[h]_[)][.][Inserting][it][into][equation] _[Q][AB] s_ ==0 0 we obtain 

**==> picture [178 x 26] intentionally omitted <==**

15 

For n _>_ 2 this equation fixes the tensor _µ_ ˙ _AB_ at _s_ = 0 to be twice the Schouten of _hAB_ , while for n = 2 this equation do not determine _µ_ ˙ _AB_ but holds automatically because in two dimensions _R_[(] _[h]_[)][1][Let][us][now][analyse][the][equations][order][by][order.][To][do][that][the][strategy] _AB_[=] 2 _[R]_[(] _[h]_[)] _[h][AB]_[.] is to take _m_ derivatives of the equations w.r.t _s_ and keep track of the leading order terms. Dropping irrelevant global factors the result is (the symbol _∝_ means proportionality with a non-zero factor) 

**==> picture [323 x 47] intentionally omitted <==**

where _µ_[(] _[m]_[)] := _∂s_[(] _[m]_[)] _µ_ and “l.o.t” stands for lower order terms. For every 1 _≤ m <_[n] _[−]_ 2[2] it is clear that the first equation determines the trace of _µ_[(] _AB[m]_[+1)] , which inserted into the second gives the full _µ_[(] _AB[m]_[+1)] . When _m_ =[n] _[−]_ 2[2] the trace-free part of _µAB_[(][n] _[/]_[2)] cannot be determined from the equations, which makes the 2[n][-term][of][the][expansion][free.][Once][such][free][data][Ψ] _[AB]_[has] been specified, one can continue determining the rest of the expansion. 

That the free data Ψ _AB_ must satisfy a divergence condition follows from Proposition 4.7, as otherwise the ambient metric would not be straight. This can also be detected from the conformal viewpoint. Indeed, consider the ( _u, A_ ) components of the conformal equations, namely 

**==> picture [122 x 13] intentionally omitted <==**

After taking (n _/_ 2 _−_ 1) derivatives along _∂s_ one arrives to 

**==> picture [83 x 15] intentionally omitted <==**

where _D_[] is a tensor that only depends on _hAB_ . By Theorem 4.7, this condition must be equivalent to (5) (i.e. _D_[] = _D_ ). 

## **5 Conclusions and future work** 

In this paper, we have shown that any straight ambient metric admits a conformal completion with a bifurcate Killing horizon with integrable Killing one-form, where one of the branches corresponds to _J_ and the other to the original homothetic horizon. This implies that the transverse expansion of the metric at null infinity can be related to the one at the homothetic horizon. In particular, the free data in the Fefferman–Graham construction appears at the same order as the gravitational radiation at _J_ . We then established a one-to-one correspondence between exact, straight ambient metrics and solutions of the conformal Einstein equations that admit a bifurcate conformal Killing horizon with integrable Killing one-form and whose conformal factor satisfies a suitable condition. Notably, this result identifies the Fefferman–Graham ambient metric as the unique conformal spacetime with these properties. We believe this result is relevant for at least two reasons: first, because it characterizes the ambient metric from a conformal geometric perspective; and second, because it relaxes the requirement for the homothety to be exact as a one-form. 

The results of this paper open the door for our next work [21], where we will employ the general identities developed in [19, 20] to provide a fully geometric characterization of asymptotically flat spacetimes. As we will see, the gravitational degrees of freedom for a general asymptotically flat spacetime of arbitrary dimension appear at the same order as the free data in the ambient metric. This suggests a strong connection between the ambient metric and a geometric definition of radiation that we plan to analyse further in future works. Moreover, in [21] we will 

16 

show that one intrinsic obstruction for the smoothness of _J_ is strongly related to the presence of a non-vanishing “radiative obstruction tensor” at the cuts of _J_ . 

Another promising direction for future work is to analyze the conformal freedom in the FeffermanGraham construction also from the conformal perspective, that is, to determine which data ( _ω_[2] _h,_ Ψ _[′]_ ) give rise to the same ambient metric as ( _h,_ Ψ). This analysis could shed light on the general (and complicated) question of when two asymptotically flat spacetimes in arbitrary dimension with conformally related universal structures are equivalent, or in other words, how radiation behaves under conformal transformations. One possible approach to this problem is through tractor calculus [6], which is naturally adapted to conformally invariant structures and is closely related with the ambient metric construction itself. Reformulating the ideas developed in this paper, as well as those of [21], within the tractor framework could therefore provide a more intrinsic understanding of the conformal freedom in the Fefferman–Graham construction. Such a reformulation would also facilitate a direct comparison with existing tractor-based treatments of null infinity, for instance those in [16], and may help clarify how radiation data transforms under conformal rescalings. 

## **Acknowledgements** 

This work has been supported by Projects PID2024-158938NB-I00 (Spanish Ministerio de Ciencia e Innovaci´on and FEDER “A way of making Europe”). M. Mars acknowledges financial support under projects SA097P24 (JCyL) and RED2022-134301-T funded by MCIN/AEI/10.13039/ 501100011033. G. S´anchez-P´erez also acknowledges support of the PhD. grant FPU20/03751 from Spanish Ministerio de Universidades. 

## **A Quasi-Einstein equations in R´acz-Wald coordinates** 

In this appendix we write down explicitly the quasi-Einstein equations associated to the metric (21) in R´acz-Wald coordinates. More specifically we compute the components of the tensor _Q_ := Hess _v_ + _v_ Sch _g_ . The computation has been done using the `xAct` package of `Mathematica` . We introduce the variable _s_ := _uv_ and we denote a derivative w.r.t. _s_ with a dot. 

**==> picture [409 x 199] intentionally omitted <==**

17 

**==> picture [505 x 107] intentionally omitted <==**

where tr _µ_ is the trace w.r.t. _µ_ and ( ˙ _µ · µ_ ˙ ) _AB_ := _µ[CD] µ_ ˙ _AC_ ˙ _µBD_ . Particularizing the equations for _G_ = _−_ 1, 

**==> picture [403 x 75] intentionally omitted <==**

**==> picture [376 x 122] intentionally omitted <==**

## **References** 

- [1] Anderson, M. T. Existence and stability of even-dimensional asymptotically de Sitter spaces. In Annales Henri Poincar´e (2005), vol. **6** , Springer, pp. 801–820. 

- [2] Anderson, M. T., and Chru´sciel, P. T. Asymptotically simple solutions of the vacuum Einstein equations in even dimensions. Communications in mathematical physics **260** (2005), 557–577. 

- [3] Baouendi, M. S., and Goulaouic, C. Singular nonlinear Cauchy problems. Journal of Differential Equations **22** (1976), 268–291. 

- [4] Choptuik, M. W. Universality and scaling in gravitational collapse of a massless scalar field. Physical review letters **70** (1993), 9. 

- [5] Christodoulou, D. The instability of naked singularities in the gravitational collapse of a scalar field. Annals of Mathematics **149** (1999), 183–217. 

- [6] Curry, S. N., and Gover, A. R. An introduction to conformal geometry and tractor calculus, with a view to applications in general relativity. Asymptotic Analysis in General Relativity **443** (2018), 86. 

- [7] de Boer, J., and Solodukhin, S. N. A holographic reduction of Minkowski space–time. Nuclear Physics B **665** (2003), 545–593. 

18 

- [8] Evans, L. C. Partial Differential Equations, vol. **19** . American Mathematical Society, 2022. 

- [9] Fefferman, C., and Graham, C. R. Conformal invariants. “Elie Cartan et les Mathematiques d’Aujourd’hui”, Asterisque, hors serie (1985), 95–116. 

- [10] Fefferman, C., and Graham, C. R. The ambient metric. Princeton University Press, 2012. 

- [11] Frauendiener, J. Conformal infinity. Living Reviews in Relativity **7** (2004), 1. 

- [12] Friedrich, H. Conformal Einstein evolution. The conformal structure of space-time: Geometry, Analysis, Numerics (2002), 1–50. 

- [13] Friedrich, H. Geometric asymptotics and beyond. One hundred years of general relativity (Surveys in Differential Geometry) (2015), 37–74. 

- [14] Gundlach, C., and Martin-Garcia, J. M. Critical phenomena in gravitational collapse. Living Reviews in Relativity **10** (2007), 1–57. 

- [15] Gursky, M. J., and Sz´ekelyhidi, G. A local existence result for Poincar´e-Einstein metrics. Advances in Mathematics **361** (2020), 106912. 

- [16] Herfray, Y. Tractor geometry of asymptotically flat spacetimes. Annales Henri Poincar´e **23** (2022), 3265–3310. 

- [17] Kami´nski, W. Well-posedness of the ambient metric equations and stability of even dimensional asymptotically de Sitter spacetimes. Communications in Mathematical Physics **401** (2023), 2959–2998. 

- [18] Kichenassamy, S. On a conjecture of Fefferman and Graham. Advances in Mathematics **184** , 2 (2004), 268–288. 

- [19] Mars, M., and S´anchez-P´erez, G. Transverse expansion of the metric at null hypersurfaces I. Uniqueness and application to Killing horizons. Journal of Geometry and Physics **209** (2025), 105416. 

- [20] Mars, M., and S´anchez-P´erez, G. Transverse expansion of the metric at null hypersurfaces II. Existence results and application to Killing horizons. Journal of Geometry and Physics **217** (2025), 105605. 

- [21] Mars, M., and S´anchez-P´erez, G. Transverse expansion of the metric at null infinity. arXiv:2602.05061 (2026). 

- [22] Nguyen, K. Lectures on Carrollian Holography. arXiv:2511.10162 (2025). 

- [23] Parisini, E., Skenderis, K., and Withers, B. The ambient space formalism. Journal of High Energy Physics **2024** (2024), 1–76. 

- [24] Rodnianski, I., and Shlapentokh-Rothman, Y. The asymptotically self-similar regime for the Einstein vacuum equations. Geometric and Functional Analysis **28** (2018), 755–878. 

- [25] R´acz, I., and Wald, R. M. Extensions of spacetimes with Killing horizons. Classical and Quantum Gravity **9** (1992), 2643. 

19 

