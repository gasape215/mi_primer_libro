<!-- Convertido automáticamente desde PDF. Revisar y corregir formato si es necesario. -->

# **Transverse expansion of the metric at null infinity** 

Marc Mars[∗] and Gabriel S´anchez-P´erez[†] Departamento de F´ısica Fundamental, Universidad de Salamanca Plaza de la Merced s/n, 37008 Salamanca, Spain 

February 6, 2026 

## **Abstract** 

In this paper we analyze the conformal Einstein equations to all orders at null infinity without imposing any restriction on the spacetime dimension, the topology of _I_ , or fall-off conditions for the Weyl tensor. In particular, we study how the equations constrain the geometry of null infinity when it is assumed to be foliated by cross-sections, not necessarily spheres. Our approach is coordinate-free and treats the conformal factor Ωas a dynamical variable. After identifying the free data at _I_ , we show that any two asymptotically flat spacetimes sharing the same free data at null infinity are necessarily isometric to infinite order. In addition, we provide a detached definition of null infinity and prove an existence theorem for asymptotically flat spacetimes solving the field equations to infinite order at _I_ realizing the prescribed initial data. 

## **1 Introduction** 

The study of gravitational radiation is one of the central problems in mathematical relativity. It is also technically difficult because the metric that defines fall-off at infinity is itself a dynamical variable on which boundary conditions must be imposed. This difficulty is most naturally addressed within Penrose’s conformal framework [53, 54], where asymptotic flatness and radiation are encoded in the geometry of a null boundary _I_ attached to an unphysical spacetime ( _M, g,_ Ω), allowing infinity to be treated as a genuine geometric object. Within this setting, several notions of asymptotic flatness have been proposed (see e.g. [55, 24]), typically requiring the fulfillment of Einstein field equations in a neighbourhood of _I_ , as well as some global assumptions such as (weak) asymptotic simplicity [55]. In four spacetime dimensions, this forces null infinity to have topology R _×_ S[2] [50], which in turn implies the vanishing of the Weyl tensor at _I_ [63, 15]. As a consequence, most standard definitions of asymptotic flatness and radiation, as well as the associated notions of news [23, 23, 14], are inherently tied to spherical topology and four dimensions, and rely on the assumption that the rescaled Weyl tensor vanishes at null infinity. However, smooth solutions of the Einstein equations with non-spherical _I_ are known to exist, already in four dimensions, and the Weyl tensor need not vanish there [59]. 

While given an already compactified spacetime it is relatively straightforward to analyze its geometry induced at null infinity, the converse problem, namely constructing an asymptotically flat spacetime from prescribed data at _I_ , is far more delicate and relies on a regular conformal formulation of the field equations [17, 18]. Current existence results for the asymptotic characteristic problem [56, 33, 28] are restricted to four dimensions and assume spherical topology and vanishing Weyl tensor at _I_ . For the asymptotic hyperboloidal problem [19, 20, 2], where spherical topology is likewise imposed, generic initial data lead to a non-vanishing Weyl tensor at null infinity, which is in turn associated with the appearance of logarithmic terms in the asymptotic expansion that spoil the smoothness of _I_ [1]. This behavior is consistent with other works on non-smooth null infinity [65, 7, 61, 62, 34]. 

> ∗marc@usal.es 

> †gasape21@usal.es 

1 

Motivated by the fact that comparatively fewer results are available in higher dimensions and non-spherical topologies, the aim of this paper is to analyze conformal null infinity in full generality, without assuming any restriction on the spacetime dimension, the topology of _I_ beyond admitting a foliation by cross-sections, or the vanishing of the Weyl tensor at infinity. More precisely, given a conformal manifold admitting a null infinity, we study how the geometry of _I_ is constrained by the requirement of asymptotic flatness, understood here as the validity of the conformal Einstein equations order by order at infinity. Analyzing these equations allows us to identify the free data at _I_ , regardless of its dimension and the topology of its cross-sections. Our approach is entirely coordinate-free and treats the conformal factor Ωas a dynamical variable rather than as a fixed background quantity. Once the free data have been isolated, we prove that any two asymptotically flat spacetimes sharing the same free data at _I_ are necessarily isometric to infinite order. We also provide a detached definition of null infinity and prove that, given such free data, there exists an asymptotically flat spacetime in which the prescribed null hypersurface arises as its null infinity. 

In order to study detached null hypersurfaces, it is convenient to employ the hypersurface data formalism developed in [48, 38, 39]. The basic building block of this formalism is the notion of _metric hypersurface data {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ , where _**γ**_ is a symmetric tensor with one degenerate direction, _**ℓ**_ is a one-form, and _ℓ_[(2)] is a scalar function on _H_ . When _H_ is embedded in an ambient manifold, the collection _{_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ encodes respectively the fully tangent, tangenttransverse, and fully transverse components of the ambient metric _g_ at _H_ . Metric hypersurface _◦_ data uniquely determine contravariant data _{P, n}_ , together with a torsion-free connection _∇_ on _H_ . The vector field _n_ spans the kernel of _**γ**_ , i.e. _**γ**_ ( _n, ·_ ) = 0. 

While metric hypersurface data capture only zeroth-order information of the ambient metric, it is natural to consider higher-order derivatives at _H_ . Let 2 **Y**[(] _[k]_[)] denote the _k_ -th Lie derivative of _g_ along an arbitrary transverse vector field _ξ_ . We refer to the collection _{_ **Y**[(] _[k]_[)] _}k≥_ 1 as the _transverse_ or _asymptotic expansion_ . Informally, this expansion allows one to reconstruct the ambient metric order by order in the transverse direction. In a previous work [47], we made this statement precise by proving that, given null metric hypersurface data _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ and a prescribed collection of tensors _{_ Y[(] _[k]_[)] _}k≥_ 1 on _H_ , there exists an ambient manifold ( _M, g_ ) such that **Y**[(] _[k]_[)] = Y[(] _[k]_[)] for all _k ≥_ 1. A priori, the resulting spacetime need not satisfy any field equations. In order to characterize those collections _{_ Y[(] _[k]_[)] _}k≥_ 1 for which ( _M, g_ ) satisfies prescribed equations, such as the Einstein equations, we derived in [46] a system of identities relating the transverse derivatives of the ambient Ricci tensor at _H_ to the tensors _{_ **Y**[(] _[k]_[)] _}k≥_ 1. 

The identities obtained in [46, 47] are well adapted to the Einstein equations in the bulk, but not to the study of null infinity. The reason is that the Einstein equations are naturally expressed in terms of the Ricci tensor, whereas the conformal Einstein equations involve additional structures. Consequently, the first step of the present analysis is to rewrite these identities in a form suitable for the conformal field equations. The resulting identities depend not only on the tensors _{_ **Y**[(] _[k]_[)] _}k≥_ 1, but also on the transverse derivatives of the conformal factor Ωat _I_ , which we denote by _{σ_[(] _[k]_[)] _}k≥_ 1. 

Once these identities have been established, we consider a conformal manifold ( _M, g,_ Ω) and fix[1] the conformal gauge by imposing _|∇_ Ω _|_[2] = 0, which we refer to as a _conformal geodesic gauge_ . As shown in [44], this gauge is uniquely determined once the value of Ωis prescribed on a hypersurface transverse to _I_ . Analyzing the conformal Einstein equations order by order in this gauge leads to the following conclusions: 

1. At each order, the scalars _P[ab]_ Y[(] _ab[k]_[)][,] **[Y]**[(] _[k]_[+1)][(] _[n, n]_[),][and] _[σ]_[(] _[k]_[+1)][satisfy][a][system][of][equations] 

> 1In order to compute the transverse expansion at _I_ , it is necessary to work with a specific representative of the conformal class, and hence to fix a conformal gauge. 

2 

on _I_ which, except for one value of _k_ , can be solved to determine these quantities in terms of lower-order data and the value of _σ_[(] _[k]_[+1)] on a chosen cross-section Σ _→ I_ . This initial condition codifies the residual conformal freedom within the conformal geodesic gauge. For a very specific value of _k_ = _m_ 1, however, the system fails to be invertible, and instead we use another conformal equation, the so-called higher order Raychaudhuri equation, that allows us to determine _P[ab]_ Y[(] _ab[m]_[1][)] , **Y**[(] _[m]_[1][+1)] ( _n, n_ ), and _σ_[(] _[m]_[1][+1)] provided an additional free function m on Σ is prescribed. As pointed out recently in [8], the null Raychaudhuri constraint gives rise to the Bondi mass-loss formula in four dimensions. Our result suggests that a similar conclusion holds in higher dimensions. 

2. Once _P[ab]_ Y[(] _[k]_[)] **[Y]**[(] _[k]_[+1)][(] _[n, n]_[),][and] _[σ]_[(] _[k]_[+1)][have][been][fixed,][the][one-form] **[Y]**[(] _[k]_[)][(] _[n,][ ·]_[)][is][com-] _ab_[,] 

pletely determined by the conformal equations, except for a specific value of _k_ = _m_ 2 that we discuss later, at which an additional one-form _**β**_ on Σ must be prescribed as free data in order to determine **Y**[(] _[m]_[2][)] ( _n, ·_ ). 

3. Finally, after determining _P[ab]_ Y[(] _ab[k]_[)][,] **[Y]**[(] _[k]_[+1)][(] _[n, n]_[),] _[σ]_[(] _[k]_[+1)][,][and] **[Y]**[(] _[k]_[)][(] _[n,][ ·]_[),][the][remaining] components of **Y**[(] _[k]_[)] generically satisfy a transport equation along _n_ , which can be integrated starting from an initial symmetric trace-free tensor _Y_[(] _[k]_[)] on Σ. For even-dimensional spacetimes and for a specific value of _k_ = _m_ 3, however, **Y**[(] _[m]_[3][)] satisfies no transport equation at all, and the components of **Y**[(] _[m]_[3][)] not encoded in _P[ab]_ Y[(] _ab[m]_[3][)] or **Y**[(] _[m]_[3][)] ( _n, ·_ ) must be prescribed as additional free data. 

The number of degrees of freedom in the geometric and detached approach that we present agrees with the analysis in Bondi coordinates in dimension four [58, 10] and also in higher even dimensions [6, 57]. Furthermore, the fact that the tensor **Y**[(] _[m]_[)] is only freely specifiable in even dimensions enforces the idea already pointed out in [31] that there are not smooth radiating odd dimensional spacetimes. This is why most of the definitions of asymptotic flatness in higher dimensions restrict to even dimensional spacetimes [29, 60]. 

The exceptional cases appearing in the second and third items give rise to two potential obstructions, analogous in spirit to the Fefferman–Graham obstruction tensor. These obstructions have already appeared in the literature in specific situations with other names (see e.g. [57] where they are denoted as the “Coulombian” and “radiative” anomalies). Let us see in more detail why these obstructions appear. The equation determining the one-form **r**[(] _[k]_[)] := **Y**[(] _[k]_[)] ( _n, ·_ ) at each order takes the schematic form 

**==> picture [303 x 14] intentionally omitted <==**

The initial condition for this transport equation is obtained from another conformal equation, which reads 

**==> picture [319 x 14] intentionally omitted <==**

where n denotes the dimension of _I_ . For _k_ = n, equation (2) uniquely determines **r**[(] _[k]_[)] _|_ Σ, which can then be used as initial data to integrate (1). For _k_ = n, however, an initial condition for **r**[(][n][)] must be prescribed, which motivates the introduction of the free one-form _**β**_ . Moreover, if the lower-order terms in (2) do not vanish identically, the resulting spacetime cannot be smooth beyond this order. In this sense, equation (2) defines an obstruction tensor, which we refer to as the _Coulombian obstruction tensor_ and denote by _O_[Σ] . In Section 6 we derive a necessary and sufficient condition for the vanishing of this obstruction in four spacetime dimensions and relate it to the vanishing of the Weyl tensor at _I_ . 

Concerning item 3, the recursive determination of **Y**[(] _[k]_[)] is governed by another transport equation of the form 

**==> picture [338 x 27] intentionally omitted <==**

3 

For _k_ =[n] _[−]_[1][the][tensor] **[Y]**[(] _[k]_[)][can][be][determined][from][an][initial][condition] _[Y]_[(] _[k]_[)][on][Σ.][When] 2[,] _k_ =[n] _[−]_ 2[1] (which occurs only when n is odd), **Y**[(] _[k]_[)] satisfies no transport equation at all, and the components of **Y**[(] _[k]_[)] not encoded in _P[ab]_ Y[(] _ab[k]_[)][or] **[Y]**[(] _[k]_[)][(] _[n,][ ·]_[)][must][be][prescribed][as][free][data.] Furthermore, the remainder term in (3) defines another obstruction tensor, which we call the _radiative obstruction tensor_ and denote by _O[I]_ . If this tensor is not identically zero, the conformal equations cannot be satisfied beyond this order. In Section 6 we show that this obstruction vanishes identically in four spacetime dimensions and that, in six dimensions, it is closely related to the Fefferman–Graham obstruction tensor. We also conjecture that this behaviour also emerges in higher dimensions (Conjecture 6.3). 

Once the free data _D_ have been identified, we prove a uniqueness theorem (Theorem 5.2), showing that any two asymptotically flat spacetimes sharing the same free data at _I_ are necessarily isometric to infinite order at their respective _I_ . Our notion of asymptotic flatness is less restrictive than others commonly adopted in the literature such as the ones described above, as it only requires the conformal field equations to be satisfied to infinite order at _I_ . An informal version of the uniqueness result is as follows. 

**Theorem 1.1** (Informal version, see Theorem 5.2) **.** _Let_ ( _M, g,_ Ω) _and_ ( _M[′] , g[′] ,_ Ω _[′]_ ) _be two asymptotically flat spacetimes both written in a conformal geodesic gauge. Suppose that their respective null infinities have the same free data D. Then_ ( _M, g,_ Ω) _and_ ( _M[′] , g[′] ,_ Ω _[′]_ ) _are isometric to infinite order at I ._ 

Having established that the free data fully characterize the geometry at null infinity, we prove the converse statement: given such free data on an abstract null hypersurface, together with the zeroth-order data that we call _I_ - _structure data_ (see Definition 3.3), there exists an asymptotically flat conformal spacetime realizing them (Theorem 5.5). An informal formulation of this existence theorem is the following. 

**Theorem 1.2** (Informal version, see Theorem 5.5) **.** _Given I -structure data and free data D such that the radiative and Coulombian obstruction tensors vanish, there exists an asymptotically flat spacetime realizing these data._ 

The construction of the ambient spacetime is technically involved, since the higher order conformal field equations are highly coupled order by order and, moreover, there are more equations than variables to be determined. A key part of the proof consists in showing that the redundant equations are automatically satisfied once the remaining ones are solved. At the core of this redundancy is the contracted Bianchi identity. While this redundancy is irrelevant when the ambient spacetime is already given, it becomes a central issue when the spacetime is to be constructed order by order, as it is the case in our existence theorem. 

The structure of this manuscript is as follows. Sections 2 and 3 provide an overview of the aspects of hypersurface data and conformal geometry needed in this work. In Section 4 we review the identities derived in [46] relating the transverse expansion to derivatives of the ambient Ricci tensor at a null hypersurface, and we derive new identities adapted to the conformal field equations. We also analyze the redundancy of the equations order by order and identify the free data. In Section 5 we prove that these data completely characterize the geometry at null infinity and that any such data set can be realized by an asymptotically flat spacetime. Finally, in Section 6 we study in detail the radiative and Coulombian obstruction tensors in the lowest spacetime dimensions in which they appear. The paper contains four appendices. Appendix A collects several identities used throughout the paper. Appendix B presents auxiliary calculations that are not included in the main body for the sake of clarity. Appendix C presents the conformal field equations in full generality. Finally, Appendix D is devoted to the derivation of the higherorder Raychaudhuri equation. 

4 

## **Notation and conventions** 

Throughout this paper ( _M, g_ ) denotes an arbitrary smooth _d_ -dimensional semi-Riemannian manifold of any signature ( _p, q_ ) with both _p_ and _q_ different from zero. We employ both index-free and abstract index notation at our convenience. Ambient indices are denoted with Greek letters, abstract indices on a hypersurface are written in lowercase Latin letters, and abstract indices at cross-sections of a hypersurface are expressed in uppercase Latin letters. As usual, square brackets enclosing indices denote antisymmetrization and parenthesis are for symmetrization. The symmetrized tensor product is denoted with _⊗s_ . By _F_ ( _M_ ), X( _M_ ) and X _[⋆]_ ( _M_ ) we denote respectively the set of smooth functions, vector fields and one-forms on _M_ . The subset _F[⋆]_ ( _M_ ) _⊂ F_ ( _M_ ) consists of the nowhere vanishing functions on _M_ . The pullback of a function _f_ via a diffeomorphism Φ will be denoted by Φ _[⋆] f_ or simply by _f_ depending on the context. A ( _p, q_ )- tensor refers to a tensor field _p_ times contravariant and _q_ times covariant. Given any pair of (2 _,_ 0) and (0 _,_ 2) tensors _A[ab]_ and _Bcd_ we denote tr _A_ _**B**_ := _A[ab] Bab_ . We employ the symbol _∇_ for the Levi-Civita connection of _g_ , and our convention for the Riemann tensor is 

**==> picture [171 x 13] intentionally omitted <==**

We use the notation _£_[(] _[m]_[)][to][denote][the] _[m]_[-th][Lie][derivative][of][the][tensor] _[T]_[along] _[X]_[,][and] _X[T] X_[(] _[m]_[)] ( _f_ ) for the _m_ -th directional derivative of the function _f_ along _X_ . When _m_ = 1 we also write _£X T_ and _X_ ( _f_ ), respectively, and when _m_ = 0 they are just the identity operators. All manifolds are assumed to be connected and smooth. Embedded hypersurfaces are assumed to be two-sided unless otherwise indicated. 

## **2 Review of hypersurface data formalism** 

In this section we review the notions of the _hypersurface data formalism_ needed in this paper. Details can be found in [38, 39] (see also [48, 36]). We restrict from the beginning to the null case. **Null metric hypersurface data** is a set _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ consisting of an n-dimensional manifold _H_ , a symmetric, degenerate (0 _,_ 2)-tensor field _**γ**_ with just one degenerate direction at each point, a one-form _**ℓ**_ , and a scalar function _ℓ_[(2)] on _H_ , provided that the 2-covariant, symmetric tensor _**A** |p_ on _TpH ×_ R defined by 

**==> picture [298 x 15] intentionally omitted <==**

is non-degenerate at every _p ∈H_ . A five-tuple _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _,_ **Y** _}_ , where **Y** is a (0 _,_ 2) symmetric tensor field on _H_ , is called **null hypersurface data** . The non-degeneracy of _**A**_ allows one to define a 2-contravariant, symmetric tensor field _P_ and a vector _n_ on _H_ by means of 

**==> picture [368 x 30] intentionally omitted <==**

Given null hypersurface data we define the tensor fields 

**==> picture [373 x 23] intentionally omitted <==**

as well as the contractions **s** := **F** ( _n, ·_ ), **r** := **Y** ( _n, ·_ ) and _κn_ := _−_ **Y** ( _n, n_ ). Note that **s** ( _n_ ) = 0 because **F** is a two-form. It is also useful to introduce a (1 _,_ 1)-tensor _V_ defined by 

**==> picture [313 x 24] intentionally omitted <==**

and write out its contraction with _n[a]_ , namely 

**==> picture [310 x 23] intentionally omitted <==**

5 

Note that these definitions are fully detached from any ambient space. To connect with the standard concept of hypersurface we say that null metric hypersurface data _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ is (Φ _, ξ_ )-embedded in a semi-Riemannian manifold ( _M, g_ ) if there exists an embedding Φ : _H →M_ and a vector field _ξ_ along Φ( _H_ ) everywhere transversal to Φ( _H_ ), called rigging, such that 

**==> picture [349 x 14] intentionally omitted <==**

Furthermore, null hypersurface data _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _,_ **Y** _}_ is embedded provided that, in addition, 

**==> picture [265 x 23] intentionally omitted <==**

For embedded data, **U** coincides with the second fundamental form of Φ( _H_ ) w.r.t. the unique normal one-form _**ν**_ satisfying _**ν**_ ( _ξ_ ) = 1. Moreover, introducing a (local) basis _{ea}_ of _H_ , the inverse metric _g[αβ]_ at Φ( _H_ ) can be then written in the basis _{ξ,_  _ea_ := Φ _⋆ea}_ as 

**==> picture [311 x 17] intentionally omitted <==**

In the embedded picture the notion of rigging vector is non-unique, since given a rigging _ξ_ any other vector of the form _ξ[′]_ = _z_ ( _ξ_ +Φ _⋆V_ ) with ( _z, V_ ) _∈F[⋆]_ ( _H_ ) _×_ X( _H_ ) is also transverse to Φ( _H_ ). Translating this into the abstract setting, one defines the gauge transformed data by 

**==> picture [441 x 42] intentionally omitted <==**

These transformations induce the following gauge behaviour for _P_ and _n_ [38], 

**==> picture [406 x 15] intentionally omitted <==**

Given null metric hypersurface data _{H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ it is possible to define a torsion-free connection _◦ ∇_ on _H_ by means of [39] 

**==> picture [403 x 16] intentionally omitted <==**

which in the embedded case can be related with the Levi-Civita connection _∇_ of _g_ by 

**==> picture [385 x 15] intentionally omitted <==**

_◦_ The action of _∇_ on the contravariant data _{P, n}_ turns out to be [39] 

**==> picture [339 x 35] intentionally omitted <==**

In the embedded case, the _∇_ -derivative of _ξ_ along tangent directions to _H_ is [38] 

**==> picture [298 x 17] intentionally omitted <==**

and as a consequence (cf. (14)) 

**==> picture [371 x 16] intentionally omitted <==**

A direct consequence of (24) is that for any one-form _**ω**_ [36], 

**==> picture [362 x 17] intentionally omitted <==**

6 

while (25) implies that for every (0 _,_ 2) tensor T _ab_ the _P_ -trace of its Lie derivative along _n_ is 

tr _P £n_ **T** := _P[ab] £n_ T _ab_ = _£n_ (tr _P_ **T** ) + 4 _P[ab]_ T _ac_ s _bn[c]_ + 2 _P[ac] P[bd]_ U _cdTab_ + _n_ ( _ℓ_[(2)] ) **T** ( _n, n_ ) _._ (29) Finally, we will frequently use that every (0 _,_ 2) tensor T _ab_ can be uniquely decomposed by [40] 

**==> picture [376 x 26] intentionally omitted <==**

where T[] _ab_ is a tensor lying on the kernel of so-called the energy-momentum map, i.e. a tensor satisfying _P[ab]_ T[] _ab_ = 0 and T[] _abn[a]_ = 0. We will often call T[] _ab_ the transverse part of T _ab_ , or when T _ab_ = T[] _ab_ we will say that T _ab_ is a transverse tensor. Similarly, for a one-form _**ω**_ we define 

**==> picture [265 x 12] intentionally omitted <==**

  and call _**ω**_ the transverse part of _**ω**_ , that satisfies _**ω**_ ( _n_ ) = 0. 

## **3 Quasi-Einstein manifolds** 

In this section we review the basic aspects of conformal completions of manifolds. The results are well-known. However, our presentation puts the emphasis on the notion of “quasi-Einstein” manifold. This follows e.g. [11, 41]. We start by recalling the definition of the Schouten tensor for a ( _d ≥_ 3)-dimensional metric _g_ in terms of the Ricci, 

**==> picture [311 x 27] intentionally omitted <==**

We will employ the symbols _Lαβ_ and _L_ for the Schouten in abstract index notation and for its trace, respectively. The Schouten and Ricci scalars are related by _L_ = 2( _dR−_ 1)[.][From][the][second] Bianchi identity it follows that 

**==> picture [412 x 13] intentionally omitted <==**

_C[µ] ναβ_ being the Weyl tensor. The Weyl, Schouten and Ricci tensors transform as follows under  a conformal rescaling _g_ = _ω_[2] _g_ [64], 

**==> picture [349 x 100] intentionally omitted <==**

Let ( _M,_ [ _g_ ]) be a _d_ -dimensional conformal structure of arbitrary semi-Riemannian signature. For each _g ∈_ [ _g_ ] we construct the differential operator 

**==> picture [338 x 14] intentionally omitted <==**

“ ” where _tf_ denotes the trace free part w.r.t. _g_ . One can easily check that _Aω_ 2 _g_ ( _ωf_ ) = _ωAg_ ( _f_ ), and therefore 

Ω _[−]_[2] _g ∈_ [ _g_ ] is Einstein _⇐⇒_ (Hess _g_ Ω+ ΩSch _g_ ) _[tf]_ = 0 _._ This condition can be rewritten in an equivalent way in terms of the scalar 

**==> picture [265 x 24] intentionally omitted <==**

as Hess _g_ Ω+ ΩSch _g −qg_ = 0. This discussion motivates the following definition. 

7 

**Definition 3.1.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold of dimension d ≥_ 3 _,_ Ω _∈F_ ( _M_ ) _a non-identically zero function and T a trace-free, two-covariant tensor field. We say that the four-tuple_ ( _M, g,_ Ω _, T_ ) _is a quasi-Einstein manifold provided that_ 

**==> picture [292 x 13] intentionally omitted <==**

_A quasi-Einstein manifold is called vacuum when T_ = 0 _. Note that if_ ( _M, g,_ Ω _, T_ ) _is a quasi-Einstein manifold, then_ ( _M, ω_[2] _g, ω_ Ω _, ωT_ ) _is also a quasi-Einstein manifold for every ω ∈F[⋆]_ ( _M_ ) _._ 

From the transformation Ω=[] _ω_ Ωand using (37) and (38), the behaviour of _q_ under conformal rescalings is 

**==> picture [321 x 34] intentionally omitted <==**

A direct consequence of (41) and (34) is that for any quasi-Einstein manifold ( _M, g,_ Ω _, T_ ), 

**==> picture [338 x 23] intentionally omitted <==**

**==> picture [371 x 24] intentionally omitted <==**

Moreover, for any quasi-Einstein manifold satisfying Ω _∇βT[αβ] −_ ( _d −_ 1) _T[αβ] ∇β_ Ω= 0 (this holds in particular for any vacuum quasi-Einstein manifold) one can define a conformally invariant constant 

**==> picture [271 x 16] intentionally omitted <==**

Its geometric interpretation is as follows. Consider a vacuum quasi-Einstein manifold ( _M, g,_ Ω) and define the metric _g_  := Ω _[−]_[2] _g_ on the subset _{_ Ω = 0 _}_ . Plugging _ω_ = Ω _[−]_[1] into (36) and using the quasi-Einstein equation (41), 

**==> picture [301 x 26] intentionally omitted <==**

So, up to a numerical factor, _λ_ is the cosmological constant associated to the Einstein representative of ( _M,_ [ _g_ ]). Thus, it makes sense to talk about _λ_ -vacuum quasi-Einstein manifolds. 

At the points where Ω = 0 one can define the rescaled Weyl tensor D _[α] βµν_ := Ω[3] _[−][d] C[α] βµν_ . From (44), 

**==> picture [366 x 27] intentionally omitted <==**

It then follows that for _λ_ -vacuum quasi-Einstein manifolds, the rescaled Weyl tensor satisfies a regular PDE on the closure of _{_ Ω = 0 _}_ . As we show now, _{_ Ω = 0 _}_ is dense on _M_ , so D _[α] βµν_ satisfies a regular PDE everywhere on _M_ . This does not mean, however, that D _[α] βµν_ extends regularly to _{_ Ω= 0 _}_ . The first part of the lemma is well-known, see e.g. [35]. The second is probably known to experts but we could not find an explicit proof in the literature. 

**Lemma 3.2.** _Let_ ( _M, g,_ Ω) _a λ-vacuum quasi-Einstein manifold with constant λ and assume {_ Ω= 0 _} ̸_ = _∅. Then,_ 

> _1. If λ_ = 0 _, {_ Ω= 0 _} is an embedded hypersurface with non-zero normal given by ∇_ Ω _. Furthermore, it is spacelike when λ >_ 0 _, and timelike when λ <_ 0 _._ 

> _2. If λ_ = 0 _, then except for a (possibly empty) collection of isolated points {pi}, {_ Ω= 0 _} is an embedded null hypersurface with nowhere zero normal ∇_ Ω _._ 

8 

_Proof._ A point _p ∈M_ is called singular provided that Ω _|p_ = 0 and _∇_ Ω _|p_ = 0. Then, from equation (45) the set _{_ Ω= 0 _}_ cannot admit any singular point in the case _λ ̸_ = 0, and therefore it is a smooth embedded hypersurface. The vector field _∇_ Ωis normal to _{_ Ω= 0 _}_ and again by equation (45) we see that _{_ Ω= 0 _}_ is spacelike when _λ >_ 0 and timelike when _λ <_ 0. 

For item 2. we first prove that singular points are necessarily isolated. Let _p ∈{_ Ω= 0 _}_ be a ˆ singular point and define _qp_ := _q_ ( _p_ ). By (42) the transformation of _qp_ is _qp_ = _ω_ ( _p_ ) _[−]_[1] _qp_ , so being zero/non-zero is a conformally invariant statement. Let us prove that _qp_ = 0. Let _{ea}_ be an orthonormal basis of _TpM_ , _I ⊆_ R an interval, and let _γ_ ( _v_ ), _v ∈I_ , be an affinely parametrized geodesic starting at _p_ . Let _{ea_ ( _v_ ) _}_ the basis at _Tγ_ ( _v_ ) _M_ obtained by parallel transport of _{ea}_ along _γ_ ( _v_ ). Define the following quantities 

**==> picture [326 x 16] intentionally omitted <==**

If _ηab_ := _g_ ( _ea, eb_ ) then _g_ ( _ea_ ( _v_ ) _, eb_ ( _v_ )) = _ηab_ for all _v ∈I_ . Observe that 

**==> picture [287 x 15] intentionally omitted <==**

where _η[ab]_ := _ηab_ . Let us establish the following equations, 

**==> picture [388 x 82] intentionally omitted <==**

where the first one follows from (47), the second from (41) and the last one from (43). We also compute for later use 

**==> picture [368 x 26] intentionally omitted <==**

Equations (48) constitute a linear first order system of homogeneous ODE for _{_ Ω[˜] _,_ Ω[˜] _a,_ ˜ _q}_ . Since ˜ _p_ is a singular point we have Ω(0)[˜] = Ω[˜] _a_ (0) = 0. If, moreover, _qp_ = 0, then also _q_ (0) = 0 and thus by uniqueness of the solution, all the points on _γ_ ( _v_ ) would be singular with _q_ = 0. Since _γ_ is arbitrary it follows that the set of singular points with _q_ = 0 is open (and obviously also closed). Since _M_ is connected, this set is the whole of _M_ , which contradicts the fact that Ωis not identically zero. Then, _qp_ = 0 at any singular point. Next we prove that singular points are isolated. Since _qp_ = 0 it follows from (41) that Hess _g_ Ω _|p_ = 0 and thus _p_ is a non-degenerate critical point of Ω. By Morse lemma [5] there exists a neighbourhood _U_ of _p_ and coordinates _{x[α] }[d] α_ =1[with] _[ x][α]_[(] _[p]_[) = 0 such that Ω=] _[ −]_[(] _[x]_[1][)][2] _[ −· · ·−]_[(] _[x][σ]_[)][2][ +(] _[x][σ]_[+1][)][2][ +] _[· · ·]_[+(] _[x][d]_[)][2][, the number] _[ σ]_ being the Morse index (i.e. the signature of the Hessian). Clearly the differential _d_ Ωon _U_ only vanishes at _p_ , so _p_ is isolated and _∇_ Ωis a non-zero normal to ( _{_ Ω= 0 _} \ {p}_ ) _∪U_ , and thus by (45) this set is a smooth null hypersurface (it may be empty, e.g. when _g_ is Riemannian). 

We then define _I_ as the set of points where Ω= 0 and _∇_ Ω = 0. Equations (41), (43) and (46) are known as conformal field equations [21, 22]. Their key property is that they are regular at _I_ . 

Let ( _M, g,_ Ω) be a _d_ = n+1 dimensional (vacuum) quasi-Einstein manifold with _λ_ = 0. Consider an embedding Φ : _I →M_ and rigging _ξ_ , and let _{I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ be the corresponding embedded null metric hypersurface data. Since _∇_ Ωis non-vanishing, null and tangent to _I_ , there must exist a non-vanishing function _σ_ such that _∇_ Ω= _σν_ (and hence _£ξ_ Ω= _σ_ ) on _I_ . Moreover, by pull-backing (41) to _{_ Ω= 0 _}_ and noting that _e[α] a[e][β] b[∇][α][∇][β]_[Ω=][1] 2 _[e] a[α][e][β] b_  _£∇_ Ω _g_  _αβ_[=] _[ σ]_[U] _[ab]_[, it follows] 

9 

that **U** = _qσ[−]_[1] _**γ**_ , so _I_ is totally umbilical. Furthermore, the conformal freedom _g[′]_ = _ω_[2] _g_ leaves a remnant conformal freedom on _I_ of the form 

**==> picture [355 x 13] intentionally omitted <==**

Since _∇[′]_ Ω _[′]_ = _ω[−]_[1] _∇_ Ω= _ω[−]_[1] _σν_ = _ωσν[′]_ on _I_ , it follows that the function _σ_ scales by _σ[′]_ = _ωσ_ and _q|I_ by (cf. (42)) _q[′]_ = _[I] ω[−]_[1] _q_ + _ω[−]_[2] _σ£nω_ . The functions _q_ and _ω_ are obviously independent of the rigging, so _q|I_ and _ω|I_ are gauge invariant quantities. One the other hand _σ_ = _£ξ_ Ω _|I_ has gauge behavior 

**==> picture [259 x 14] intentionally omitted <==**

Observe also that _q|I_ and _σ|I_ are not independent because from (45), 

**==> picture [182 x 23] intentionally omitted <==**

so _q|I_ is the surface gravity of _∇_ Ω= _σν_ at _I_ . Given that _∇νν_ = _κnν_ (cf. (23)) we also have 

**==> picture [133 x 12] intentionally omitted <==**

and hence _q_ = _[I] £nσ_ + _σκn_ . With this relation at hand, it is easy to check using (138) in Appendix A that the pullback of (40) to Ω= 0 is automatically fulfilled. This motivates the following definition of “universal structure”. This notion is commonly used in the literature, see e.g. [23, 3, 9, 27]. Here we are just adapting it to the context of metric hypersurface data. 

**Definition 3.3.** _We say {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q _} is I -_ _**structure data** provided {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} is null metric hypersurface data, σ ∈F[⋆]_ ( _I_ ) _,_ q _∈F_ ( _I_ ) _and_ **U** = q _σ[−]_[1] _**γ** . Moreover, the gauge transformations of σ and_ q _are G_ ( _z,V_ ) _σ_ := _zσ and G_ ( _z,V_ )q := q _. Furthermore, we define the conformal transformation Cω of {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q _}, where ω ∈F[⋆]_ ( _I_ ) _is a gauge-invariant function (called conformal factor), by_ 

**==> picture [445 x 14] intentionally omitted <==**

_It is straightforward to check that Cω ◦G_ ( _z,V_ ) = _G_ ( _z,V_ ) _◦Cω._ 

Note that given _I_ -structure data and _X ∈_ X( _I_ ), the _∇_ -derivative of _∇_ Ωalong _X_ at _I_ is, by (23) and (24), 

**==> picture [439 x 15] intentionally omitted <==**

Next we define the embedded version of the data to guarantee that _σ_ agrees with the proportionality function between _ν_ and _∇_ Ωat _I_ , and also that q is the pullback of the scalar _q_ defined in (40). 

**Definition 3.4.** _We say that {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q _} is_ (Φ _, ξ_ ) _-embedded in_ ( _M, g,_ Ω) _provided that {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} is_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _,_ Ω= 0 _in_ Φ( _I_ ) _, and in addition ∇_ Ω = _[I] σν and_ q = _σκn_ + _£nσ._ 

From the conformal transformation of q in Def. 3.3 it follows that whenever _I_ admits crosssections one can always find a conformal factor _ω_ that satisfies _ω_[2] q + _σ£nω_ = 0 and, as a consequence, _Cω_ q = 0. The remaining conformal freedom is the function _ω_ at any cross-section. In any of such conformal gauges _I_ is totally geodesic, **U** = 0. 

10 

## **4 Transverse expansion of the metric** 

In previous works [46, 47] we computed the _m_ -th transverse derivative of the ambient Ricci tensor in terms of transverse derivatives of the ambient metric _g_ at a general null hypersurface _H_ . In this section we quote the results that shall be needed in the rest of the paper. In order to simplify the notation one introduces the tensors 

**==> picture [418 x 23] intentionally omitted <==**

as well as 

**==> picture [424 x 18] intentionally omitted <==**

for _m ≥_ 1. We also denote _K_[(0)] := _g_ . Note that **Y**[(1)] _,_ **r**[(1)] _, κ_[(1)] coincide with **Y** _,_ **r** _, κn_ , respectively. In what follows we refer to the tensors _{_ **Y**[(1)] _,_ **Y**[(2)] _, ...}_ as the _transverse_ (or _asymptotic) expansion_ . The remaining derivatives of the metric, namely the tensors _K_[(] _[m]_[)] ( _ξ, ·_ ) at _H_ , are given by 

**==> picture [448 x 36] intentionally omitted <==**

under the assumption _∇ξξ_ = 0 [46]. Note that (52) together with (14) imply 

**==> picture [443 x 63] intentionally omitted <==**

and 

In particular, 

**==> picture [333 x 27] intentionally omitted <==**

Recall also that for any two objects _S_ and _T_ , any product of them _S_ ⊛ _T_ (including tensor contraction) and any derivative operator _D_ , 

**==> picture [339 x 32] intentionally omitted <==**

In general, we employ the notation _A_[(] _[m]_[)] := _£_[(] _ξ[m][−]_[1)] _A_ , _m ≥_ 1, for any tensor _A_ . As shown in [46], the commutator [ _£_[(] _ξ[m]_[)] _, ∇_ ] acting on _A_ is given by 

**==> picture [407 x 77] intentionally omitted <==**

where Σ _[α] µν_ = 2[1] _[g][αβ]_[ (] _[∇][µ][K][νβ]_[+] _[ ∇][ν][K][µβ][−∇][β][K][µν]_[)][and][Σ][(] _[m]_[)][:=] _[£]_[(] _ξ[m][−]_[1)] Σ. We also define the tensor Σ[] _αµν_ := _gαβ_ Σ _[β] µν_ and Σ[][(] _[m]_[)] := _£_[(] _ξ[m][−]_[1)] Σ, and note that Σ[(] _αµν[m]_[)][=] _[g] αβ_[Σ][(] _[m]_[)] _[β] µν_[.][Applying] (57) to _A_ = _df_ one arrives at the following. 

11 

**Proposition 4.1.** _Let ξ ∈_ X( _M_ ) _and m ≥_ 1 _an integer. Then, given any function f the following identity holds_ 

**==> picture [463 x 103] intentionally omitted <==**

_Proof._ Using (57) with _A_ = _df_ as well as _£ξd_ = _d£ξ_ , so that _A_[(] _[k]_[)] = _d_ ( _£_[(] _ξ[k][−]_[1)] ( _f_ )), (58) follows. Identity (59) follows at once from (56) after inserting (58), i.e. 

**==> picture [218 x 31] intentionally omitted <==**

One of the main results in [46, 47] is the computation of _R_[(] _ab[m]_[)][,] _[R]_[˙][(] _a[m]_[)] and _R_[¨][(] _[m]_[)] to the leading order, namely _R_[˙][(] _a[m]_[)] and _R_[¨][(] _[m]_[)] up to order _m_ + 1 and _R_[(] _ab[m]_[)] up to order _m_ . In this paper we also need _R_[˙][(] _a[m]_[)] up to order _m_ . In order not to overload the body of the paper we postpone the computation to Appendix B. The result is as follows. 

**Proposition 4.2** ([46] and Prop. B.2) **.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} be null metric hypersurface data_ (Φ _, ξ_ ) _-embedded on_ ( _M, g_ ) _and extend ξ off_ Φ( _H_ ) _by ∇ξξ_ = 0 _. Let m ≥_ 2 _be an integer. Then,_ 

**==> picture [427 x 102] intentionally omitted <==**

_where O_[(] _[m]_[)] _, Oa_[(] _[m]_[)] _and Oab_[(] _[m]_[)] _are, respectively, a scalar, a one-form and a (0,2) symmetric tensor depending only on metric data {_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} and {_ **Y** _, ...,_ **Y**[(] _[m]_[)] _}. Moreover,_ 

**==> picture [441 x 104] intentionally omitted <==**

The corresponding expressions in the case _m_ = 1, i.e. for _R_[(1)] _ab_[,] _[R]_[˙][(1)] _a_ and _R_[¨][(1)] , are as follows [37, 46] 

**==> picture [434 x 82] intentionally omitted <==**

12 

_◦ ◦_ where _Rab_ is the Ricci tensor of _∇_ , while _A_ is given by 

**==> picture [269 x 16] intentionally omitted <==**

and satisfies (the third equality is a result established in [37]) 

**==> picture [449 x 101] intentionally omitted <==**

Therefore, the contraction of (68) with _n[c]_ is 

**==> picture [429 x 58] intentionally omitted <==**

The contractions of _R_[(1)] _[P]_[and] _[n]_[are][[][37][]] _ab_[with] 

**==> picture [460 x 73] intentionally omitted <==**

Expressions (72) and (69) are all one needs to compute the ambient scalar curvature at _H_ . Indeed, using (14), _R_[(1)] = _R_ = tr _[H] P R_ + 2 _R_[˙] _an[a]_ , and inserting (72) and (69) one concludes 

**==> picture [444 x 35] intentionally omitted <==**

Before computing the higher order derivatives of the scalar curvature _R_[(] _[m]_[)] , _m ≥_ 2, we recall the following notation from [46, 47]. 

**Notation 4.3.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold and H a hypersurface. Given two_ [ _m_ ] _ambient tensors T and S, the notation T_ = _S means that T − S does not depend on derivatives_ ( _m_ ) _of g of order m or higher. When T and S are tensors on H, we use T_ = _S to denote that T − S does not depend on_ _**transverse** derivatives of g at H of order m or higher. Clearly, for_ [ _m_ ] ( _m_ ) _two ambient tensors T and S satisfying T_ = _S, their pullbacks to H satisfy_ Φ _[⋆] T_ = Φ _[⋆] S._ 

Applying _£_[(] _ξ[m][−]_[1)] to _g[αβ] Rαβ_ for _m ≥_ 2 and using identity (56) and _£ξg[αβ]_ = _−g[αµ] g[βν] Kµν_ one obtains 

_R_[(] _[m]_[)][[] = _[m]_[]] _g[αβ] Rαβ_[(] _[m]_[)] _[−]_[(] _[m][−]_[1)] _[g][αµ][g][βν][K][µν][R] αβ_[(] _[m][−]_[1)] [= _m_ ] _P[ab] R_[(] _ab[m]_[)][+2] _[R]_[˙][(] _a[m]_[)] _n[a] −_ ( _m−_ 1) _g[αµ] g[βν] KµνRαβ_[(] _[m][−]_[1)] _,_ 

where in the second equality we inserted (14). The first two terms are (64) and (65). Concerning the third one, we note that (62) implies that terms of the form **Y**[(] _[m]_[)] and **Y**[(] _[m]_[+1)] can only appear 

13 

when the tensor _Rαβ_[(] _[m][−]_[1)] is contracted with _ξ_ at least once, i.e. (cf. (14)) 

**==> picture [357 x 63] intentionally omitted <==**

where in the second line we used _Kab_ = 2Y _ab_ and _Kµνξ[µ] e[ν] a_[=] 2[1] _∇◦ aℓ_ (2) (see (52)), and in the third line (61), (65) and (60). Finally, inserting this, (64) and (65) into the expression of _R_[(] _[m]_[)] , we arrive at 

**==> picture [441 x 37] intentionally omitted <==**

An immediate consequence is 

**==> picture [279 x 17] intentionally omitted <==**

**Remark 4.4.** _With the notation introduced in 4.3 it is clear from_ (60) _,_ (61) _,_ (62) _and_ (74) _that R_[(] _ab[m]_[)] ( _m_ =+1) 0 _, R_[˙][(] _a[m]_[)] ( _m_ =+2) 0 _, R_[¨][(] _[m]_[)][(] _[m]_ =[+2)] 0 _and R_[(] _[m]_[)][(] _[m]_ =[+2)] 0 _._ 

Next we recall the general existence and uniqueness results of [46, 47] that will be needed below. Proposition 4.5 quotes the result in [46] where we constructed a diffeomorphism between neighbourhoods of two diffeomorphic hypersurfaces. Proposition 4.6 quotes a result in [46] where this diffeomorphism was used to derive a set of sufficient conditions on two diffeomorphic hypersurfaces such that there exists an isometry between two neighbourhood of them. Finally, in Theorem 4.7 we recall a result from [47] where an ambient spacetime was constructed from the would-be expansion at a null hypersurface. 

**Proposition 4.5.** _Let_ Φ : _H →M and_ Φ _[′]_ : _H[′] →M[′] be two embedded hypersurfaces in ambient manifolds_ ( _M, g_ ) _and_ ( _M[′] , g[′]_ ) _and let ξ, ξ[′] be respectively riggings of_ Φ( _H_ ) _,_ Φ _[′]_ ( _H[′]_ ) _extended geodesically. Assume that there exists a diffeomorphism χ_ : _H −→H[′] . Then, there exist open neighbourhoods U ⊂M and U[′] ⊂M[′] of_ Φ( _H_ ) _and_ Φ _[′]_ ( _H[′]_ ) _and a unique diffeomorphism_ Ψ : _U −→U[′] satisfying_ Ψ _⋆ξ_ = _ξ[′] and_ Φ _[′] ◦ χ_ = Ψ _◦_ Φ _._ 

**Proposition 4.6.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} (respectively {H[′] ,_ _**γ**[′] ,_ _**ℓ**[′] , ℓ_[(2)] _[′] }) be null metric hypersurface data_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _(resp._ (Φ _[′] , ξ[′]_ ) _-embedded in_ ( _M[′] , g[′]_ ) _) with ξ and ξ[′] extended geodesically. Assume that there exists a diffeomorphism χ_ : _H −→H[′] such that_ 

**==> picture [301 x 14] intentionally omitted <==**

_and χ[⋆]_ **Y**[(] _[k]_[)] _[′]_ = **Y**[(] _[k]_[)] _for every k ≥_ 1 _. Then, there exist neighbourhoods U ⊂M and U[′] ⊂M[′] of_ Φ( _H_ ) _and_ Φ _[′]_ ( _H[′]_ ) _and a diffeomorphism_ Ψ : _U −→U[′] satisfying_ Ψ _⋆ξ_ = _ξ[′] and_ Φ _[′] ◦ χ_ = Ψ _◦_ Φ _(as in Proposition 4.5) such that_ 

**==> picture [267 x 18] intentionally omitted <==**

_for every i ∈_ N _∪{_ 0 _}._ 

**Theorem 4.7.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} be null metric hypersurface data and {_ Y[(] _[k]_[)] _}k≥_ 1 _a sequence of_ (0 _,_ 2) _symmetric tensor fields on H. Then there exists a semi-Riemannian manifold_ ( _M, g_ ) _, an embedding_ Φ : _H →M and a rigging vector ξ satisfying ∇ξξ_ = 0 _on M such that (i) {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} is null metric hypersurface data_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and (ii) {_ Y[(] _[k]_[)] _}k≥_ 1 _is the transverse expansion of g at_ Φ( _H_ ) _, i.e._ Y[(] _[k]_[)] = **Y**[(] _[k]_[)] := 2[1][Φ] _[⋆]_[] _£_[(] _ξ[k]_[)] _[g]_  _for every k ≥_ 1 _._ 

14 

We emphasize that the ambient spacetime ( _M, g_ ) in this theorem need not to be analytic (i.e. the series need not to converge). An important ingredient in the proof of this theorem is Borel’s Lemma [26], which we shall also need later in the following specific form. 

**Lemma 4.8** (Borel) **.** _Let M be a smooth manifold, H →M a embedded smooth hypersurface with rigging ξ and {σ_[(] _[k]_[)] _}k≥_ 0 _a collection of functions on H. Then, there exists a function_ Ω _in a neighbourhood of H in M such that £_[(] _ξ[k]_[)][Ω] _[|][H]_[=] _[ σ]_[(] _[k]_[)] _[for][every][k][≥]_[0] _[.]_ 

The main idea of the present paper is to analyze how the quasi-Einstein equations fix the geometry at null infinity, i.e. how the transverse expansion of the metric is constrained when the conformal Einstein equations are imposed at _I_ to infinite order. To analyse this problem it is convenient to introduce the following tensors 

**==> picture [402 x 54] intentionally omitted <==**

and the function _f_ := _|∇_ Ω _|_[2] . These tensors are obviously related by 

**==> picture [300 x 23] intentionally omitted <==**

Less immediate is the identity 

**==> picture [295 x 14] intentionally omitted <==**

which follows from the Bianchi identity (43) after replacing _q_ =[tr] n[2] _[g] −[ Q]_ 1[and][(][n] _[ −]_[1)] _[T]_[=] _[ Q −]_ n[tr] +1 _[ Q][g]_[.] In accordance of the general notation of this paper, we introduce the tensors 

**==> picture [312 x 18] intentionally omitted <==**

and 

**==> picture [414 x 36] intentionally omitted <==**

We also denote the transverse derivatives of Ωat _I_ by _σ_[(] _[k]_[)] := _£_[(] _ξ[k]_[)][Ω] _[|][I]_[ .][Note][that] _[σ]_[(1)][agrees] with the function _σ_ introduced before, so we shall use both symbols indistinctly. As already mentioned this function cannot vanish anywhere on _I_ . 

The idea now is to impose the conformal equations to infinite order at _I_ to see how _{_ **Y**[(] _[k]_[)] _}k≥_ 1 and _{σ_[(] _[k]_[)] _}k≥_ 1 are constrained. Clearly, this depends on how the conformal factor Ωhas been fixed. One sensible choice commonly used in the literature is to require the transformed Ricci scalar to vanish, which amounts solving a wave equation of the form □ _g_ Ω= Ω _F_ for some function _F_ , see [21]. Another interesting possibility is to fix Ωby solving _|∇_ Ω _|_[2] = 0. We next quote a result from [44] where we showed that this conformal gauge always exists locally near _I_ and depends on a free function on a hypersurface transverse to _I_ . 

**Lemma 4.9.** _Let_ ( _M, g,_ Ω) _be a conformal manifold with λ_ = 0 _and H a hypersurface transverse_  _to I . Let ω_ 0 _be a non-vanishing function on H. Then, there exists a unique_ ( _g_ = _ω_[2] _g,_ Ω=[] _ω_ Ω) _in a neighbourhood of I ∩H such that |∇_[] Ω[] _|_[2] _g_ [= 0] _[and]_[Ω][][=] _[H][ ω]_[0][Ω] _[.]_ 

In either of the two choices mentioned above, one can verify that _I_ is totally geodesic, which, in terms of hypersurface data means **U** = 0. However, in a generic conformal gauge, _I_ is only totally umbilical. In this paper we shall be mostly concerned with the choice _|∇_ Ω _|_[2] = 0, so in 

15 

Proposition 4.11 below we write down the tensors _Q_[(] _ab[m]_[)][,] _[Q]_[˙][(] _a[m]_[)] , _Q_[¨][(] _[m]_[)] , _L_[(] _a[m]_[)] , _L_[˙] ( _m_ ), and _f_ ( _m_ ) under the assumption **U** = 0. Each computation is performed up to the order that it will be needed. Given that other conformal choices are possible, in Appendix C we compute the expressions in full generality, i.e. without the assumption **U** = 0. The formulae in Prop. 4.11 are simply their ( _m_ ) particularization to **U** = 0. We also extend the meaning of = in Notation 4.3 as follows. 

**Notation 4.10.** _Let_ ( _M, g,_ Ω) _be a conformal manifold with null infinity I and T , S two tensors on I . We use T_ (= _m_ ) _S to denote that T − S does not depend on transverse derivatives of g and_ Ω _at I of order m or higher._ 

**Proposition 4.11.** _Let I_ = _{_ Ω= 0 _} be_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and extend ξ off_ Φ( _I_ ) _geodesically. Assume_ **U** = 0 _. Then, for every m ≥_ 2 _,_ 

**==> picture [448 x 218] intentionally omitted <==**

 ˙ _where Rab_[(] _[m]_[)] _[,] RL_[(] _[m]_[)] _are tensors that depend on_ **r**[(] _[m]_[)] _, σ_[(] _[m]_[)] _and lower order terms and we do not write for simplicity (they can be easily read out by performing all the calculations in their respective proofs)._ 

_Proof._ The first three expressions are the particularization to the case **U** = 0 of Proposition C.3, the next two of Proposition C.2 and the last one of Proposition C.4. 

The tensors _L_[(1)] _µ_[,] _[Q]_[(1)] _αβ_[,] _[Q]_[(2)] _αβ_[and] _[f]_[(2)][are][not][covered][by][this][proposition.][Again][under][the] assumption **U** = 0 they are given by (see (206)-(209), (193)-(194) and (211) in Appendix C) 

**==> picture [369 x 16] intentionally omitted <==**

**==> picture [447 x 143] intentionally omitted <==**

16 

**==> picture [427 x 88] intentionally omitted <==**

where _R_ is explicitly given by (73). In addition (cf. (211)) 

**==> picture [282 x 14] intentionally omitted <==**

Although _f_[(3)] is covered in Proposition 4.11, we will need shortly its explicit expression (cf. (212)) 

**==> picture [404 x 34] intentionally omitted <==**

One˙ immediate consequence of (206) is that, for every embedded _I_ -structure data satisfying _Qa_ = q _ℓa_ , the _∇X_ derivative of _∇_ Ωat _I_ is given by (see (51)) 

**==> picture [76 x 16] intentionally omitted <==**

and therefore every _I_ -structure data written in a conformal gauge in which q = 0 is in particular a weakly isolated horizon (see [4]). 

In the conformal gauge in which _|∇_ Ω _|_[2] = 0, the “higher order conformal equations” that we must solve are _Q_[(] _ab[m]_[)] = 0, _Q_ ˙[(] _a[m]_[)] = 0, _Q_[¨][(] _[m]_[)] = 0, _L_[(] _a[m]_[)] = 0, _L_[˙] ( _m_ ) = 0 and _f_ ( _m_ ) = 0 for every _m ≥_ 1. Observe that, for each _m_ , there are 2(n + 1) equations more than components of the metric to be fixed ( **Y**[(] _[m]_[)] and _σ_[(] _[m]_[)] ). This overdeterminacy is related to the identities (79) and (80). Taking _m_ transverse derivatives in (79) and applying (57) we arrive at 

**==> picture [455 x 48] intentionally omitted <==**

and applying _£_[(] _ξ[m][−]_[1)] to (80) gives 

**==> picture [431 x 72] intentionally omitted <==**

In the next two lemmas we prove some direct consequences of these identities. They will be essential in Section 5 to show, order by order, that the set of 2(n + 1) redundant equations is automatically satisfied provided the remaining equations hold. This is analogous (though considerably more involved) to Proposition 4.5 in [47]. Each lemma comes with its own general hypothesis, namely the validity of the quasi-Einstein equations up to a certain order, and is divided into several items with additional conditions. Although some items follow directly from others, each will be used separately in Section 5. For the sake of clarity, we therefore present them individually. 

**Lemma 4.12.** _Fix m ≥_ 1 _and assume Q_[(] _αβ[k]_[)][= 0] _[and][L]_[(] _αβ[k]_[)][= 0] _[for][every][k]_[= 1] _[, ..., m][−]_[1] _[whenever] m ≥_ 2 _._ 

17 

**==> picture [442 x 206] intentionally omitted <==**

_Proof._ Directly from (97), 

**==> picture [427 x 109] intentionally omitted <==**

which after inserting _∇[β]_ Ω = _[I] σ_[(1)] _ν[β]_ , (55) and (14) becomes 

The contraction of this identity with _ν[α]_ gives (99) at once after using that _Q_[(] _ab[m]_[)] _[n][b]_[=][0.][To] prove (100) one contracts (103) with _e[α] a_[and][uses][the][hypothesis] _[Q]_[(] _ab[m]_[)] = 0. Identity (102) is an immediate consequence of (100). Finally, to show (101) we contract (103) with _ξ[α]_ and use _Q_[(] _ab[m]_[)] = 0 and _Q_[˙][(] _a[m]_[)] = 0. 

**Lemma 4.13.** _Fix m ≥_ 1 _and assume Q_[(] _αβ[k]_[)][= 0] _[for][every][k]_[= 1] _[, ..., m][ −]_[1] _[whenever][m][ ≥]_[2] _[.] 1. If Q_[(] _ab[m]_[)] _[n][b]_[= 0] _[,][then]_ 

**==> picture [418 x 42] intentionally omitted <==**

**==> picture [98 x 16] intentionally omitted <==**

**==> picture [376 x 16] intentionally omitted <==**

**==> picture [442 x 39] intentionally omitted <==**

**==> picture [138 x 17] intentionally omitted <==**

_and_ 

**==> picture [300 x 49] intentionally omitted <==**

18 

_Proof._ Relations (107) and (108) are particularizations respectively of (106) and (105), so it suffices to prove (104)-(106). Our strategy is to write down (98) at _I_ and then compute its contractions first with _e[µ] c_[and then with] _[ ξ][µ]_[.][The former will show][(][104][)-(][105][),][and the later will] establish (106). With the assumption _Q_[(] _αβ[k]_[)][= 0][for] _[k]_[= 1] _[, ..., m][ −]_[1,][identity][(][98][)][reads] 

**==> picture [390 x 42] intentionally omitted <==**

where in the second line we used _Q_[(] _αβ[m][−]_[1)] = 0 _I_ and _£ξgαβ_ = _−Kαβ_ . 

**==> picture [455 x 63] intentionally omitted <==**

because the tangential derivatives of _Q_[(] _αβ[m][−]_[1)] vanish at _I_ . Only the first term requires further analysis. In Appendix A we recall several general identities for pullbacks onto a null hypersurface _H_ . Applying Proposition A.2 to _H_ = _I_ and using _Q_[(] _ab[m]_[)] _[n][b]_[= 0][we][get] 

**==> picture [435 x 56] intentionally omitted <==**

where we used (cf. (24)) _£nQ_[˙][(] _a[m]_[)] = _n[b] ∇[◦] bQ_[˙][(] _a[m]_[)] + _P[bc]_ U _baQ_[˙][(] _c[m]_[)] + s _aQ_[˙][(] _b[m]_[)] _n[b]_ . Since _Q_[(] _ab[m]_[)] = tr _P Q_[(] _[m]_[)] n _−_ 1 _γab_ + _Q_[][(] _ab[m]_[)][,][the][second][and][fifth][terms][can][be][elaborated][further][by][means][of] 

**==> picture [437 x 55] intentionally omitted <==**

and 

**==> picture [209 x 26] intentionally omitted <==**

Consequently, 

**==> picture [473 x 43] intentionally omitted <==**

Inserting this into (110) and simplifying gives 

**==> picture [465 x 71] intentionally omitted <==**

A contraction with _n[a]_ gives (104) after noting _Q_[][(] _ab[m]_[)] _[n][a]_[= 0][and] _[n][a][∇][◦][b]_[ ] _[Q]_[(] _ac[m]_[)] = _−P[ad]_ U _dbQ_[][(] _ac[m]_[)] (cf. (24)), while (105) is just this expression after setting tr _P Q_[(] _[m]_[)] = 0 and _Q_[][(] _ab[m]_[)] = 0. 

19 

To show (106) we now contract (109) with _ξ[µ]_ and use 

**==> picture [387 x 18] intentionally omitted <==**

**==> picture [259 x 18] intentionally omitted <==**

**==> picture [345 x 18] intentionally omitted <==**

˙ The first term is given by Prop. A.2, which under the assumption _Q_[(] _a[m]_[)] = 0 is _∇ρQ_[˙][(] _[m]_[)] _[ρ]_ = _Q_ ˙[(] _a[m]_[+1)] _n[a]_ + _£nQ_[¨][(] _[m]_[)] + 2 _κn_ + tr _P_ **U**  _Q_ ¨( _m_ ). The second term is computed from (27) after noting that, after the assumptions of item 3., namely _Q_[(] _ab[m]_[)] = 0 and _Q_[˙][(] _a[m]_[)] = 0, only the term with two riggings survives, _Q_[(] _[m]_[)] _[ρ] µ∇ρξ[µ]_ = _−κnQ_[¨][(] _[m]_[)] . The third term is simply _g[αβ] Q_[(] _αβ[m]_[+1)] (=14)[tr] _[P][Q]_[(] _[m]_[+1)][+] 

2 _Q_[˙][(] _a[m]_[+1)] _n[a]_ , and for the fourth term we use again that the only piece that does not vanish is the contraction with _ξ_ twice, obtaining 

**==> picture [363 x 23] intentionally omitted <==**

Adding up the four terms and n _L_[˙][(] _[m]_[)] , (106) is established. 

Combining (100) and (105) one has the following corollary. 

**Corollary 4.14.** _Let m ≥_ 1 _and assume Q_[(] _αβ[k]_[)][=][0] _[and][L]_[(] _µ[k]_[)] = 0 _for every k_ = 1 _, ..., m −_ 1 _, as well as f_[(] _[m]_[+1)] = 0 _, Q_[˙][(] _a[m]_[)] _n[a]_ = 0 _, Q_[(] _ab[m]_[)] _[n][a]_[=][0] _[and]_[tr] _[P][Q]_[(] _[m]_[)][=][0] _[.][If][m]_[=][n] _[,][then][Q]_[(][n][+1)][(] _[n, n]_[)][=] n _L_[(] _a_[n][)] _[n][a][;][and][if][m][ ̸]_[=][ n] _[,][then][Q]_[(] _[m]_[+1)][(] _[n, n]_[) =] _[ L]_[(] _a[m]_[)] _n[a]_ = 0 _._ 

_Proof._ From (99) one has _Q_[(] _[m]_[+1)] ( _n, n_ ) = _mL_[(] _a[m]_[)] _n[a]_ , and from _Qab_ = 0 we have U _ab_ = 0 (see (206)), so (104) gives _Q_[(] _[m]_[+1)] ( _n, n_ ) = n _L_[(] _a[m]_[)] _n[a]_ . When n = _m_ , then _Q_[(] _[m]_[+1)] ( _n, n_ ) = n _L_[(] _a[m]_[)] _n[a]_ ; and when n _̸_ = _m_ , _Q_[(] _[m]_[+1)] ( _n, n_ ) = _L_[(] _a[m]_[)] _n[a]_ = 0. 

As we will see in detail below, these results show that, for generic values of _m_ , determining the transverse expansion at _I_ reduces to analyzing, order by order, the equations _Q_[¨][(] _[m]_[)] = 0, _f_[(] _[m]_[)] = 0, _L_[˙][(] _[m]_[)] = 0 as well as _L_[][(] _a[m]_[)] := _L_[(] _a[m]_[)] _−_ ( _L_[(] _b[m]_[)] _n[b]_ ) _ℓa_ = 0 (cf. (31)) and (cf. (30)) 

**==> picture [385 x 26] intentionally omitted <==**

The remaining equations will turn out to be automatically satisfied as a consequence of Lemmas 4.12 and 4.13, together with Corollary 4.14. 

**Proposition 4.15.** _Let_ ( _M, g,_ Ω) _be an_ (n+1) _-dimensional conformal manifold with null infinity I and assume I admits a cross-section_ Σ _. Fix an integer ℓ ≥_ 1 _and assume that equations L_[(] _µ[k]_[)] = 0 _, Q_[(] _µν[k]_[)][= 0] _[hold][for][every][k][≤][ℓ][,][f]_[(] _[k]_[)][= 0] _[for][every][k][≤][ℓ]_[+ 2] _[,][and][also][L]_[(] _a_[n][)] _[n][a]_[= 0] _[when] ℓ_ = n _−_ 1 _and f_[(][n][+1)] _|_ Σ = 0 _when ℓ_ = n _−_ 2 _. Then,_ ˙ _1. Q_[(] _a[ℓ]_[+1)] _n[a]_ = 0 _, Q_[(] _ab[ℓ]_[+1)] _n[b]_ = 0 _, P[ab] Q_[(] _ab[ℓ]_[+1)] = 0 _and Q_[(] _ab[ℓ]_[+2)] _n[a] n[b]_ = _L_[(] _a[ℓ]_[+1)] _n[a]_ = 0 _._ 

_Assume in addition that L_[][(] _a[ℓ]_[+1)] = 0 _, Q_[][˙][(] _a[ℓ]_[+1)] _|_ Σ = 0 _and Q_[][(] _ab[ℓ]_[+1)] = 0 _. Then,_ 

˙ _2. Q_[(] _a[ℓ]_[+1)] = 0 _and Q_[(] _ab[ℓ]_[+2)] _n[b]_ = 0 _._ 

_If, moreover, we suppose Q_[¨][(] _[ℓ]_[+1)] = _L_[˙][(] _[ℓ]_[+1)] = 0 _and, provided ℓ_ = n _−_ 2 _, that f_[(] _[ℓ]_[+3)] = 0 _. Then_ 

20 

_3. P[ab] Q_[(] _ab[ℓ]_[+2)] = 0 _, Q_[˙][(] _a[ℓ]_[+2)] _n[a]_ = 0 _, and if ℓ_ = n _−_ 2 _also f_[(][n][+1)] = 0 _and Q_[(] _ab_[n][+1)] _n[a] n[b]_ = 0 _._ 

_Proof._ In order to prove items 1., 2. and 3. we make use of the identities in Lemmas 4.12 and 4.13 particularized to **U** = 0 (because _Qab_ = 0, see (206)). First we prove that the equations ˙ _Q_[(] _a[ℓ]_[+1)] _n[a]_ = 0, _Q_[(] _ab[ℓ]_[+1)] _n[b]_ = 0 and _P[ab] Q_[(] _ab[ℓ]_[+1)] = 0 hold under the assumptions _L_[(] _µ[k]_[)] = 0, _Q_[(] _µν[k]_[)][=][0] for _k ≤ ℓ_ , and _f_[(] _[k]_[)] = 0 for _k ≤ ℓ_ + 2. Under the present hypothesis all the conditions of item 3. in Lemma 4.12 with _m_ = _ℓ_ are verified and equation (102) simplifies to _Q_[(] _ab[ℓ]_[+1)] _n[b]_ = 0. Similarly, _P[ab] Q_[(] _ab[ℓ]_[+1)] = 0 is a consequence of (107) also for _m_ = _ℓ_ . The remaining two claims in this item are now immediate by Corollary 4.14 for _m_ = _ℓ_ + 1 (note that when _ℓ_ + 1 = n, _L_[(] _a[ℓ]_[+1)] _n[a]_ = _L_[(] _a_[n][)] _[n][a]_[= 0][holds][by][hypothesis).] 

Now we prove item 2. We first note that the result _L_[(] _a[ℓ]_[+1)] _n[a]_ = 0 combined with the hypothesis  _L_[(] _a[ℓ]_[+1)] = 0 gives _L_[(] _a[ℓ]_[+1)] = 0, and the results in item 1. combined with the hypothesis _Q_[][(] _ab[ℓ]_[+1)] = 0 gives _Q_[(] _ab[ℓ]_[+1)] = 0. Since by item 1. we also have _Q_[˙][(] _a[ℓ]_[+1)] _n[a]_ = 0, identities (100) and (105) for _m_ = _ℓ_ + 1 simplify to 

**==> picture [249 x 36] intentionally omitted <==**

Solving for _Q_[(] _ab[ℓ]_[+2)] _n[b]_ in the second and inserting it into the first gives 

**==> picture [257 x 15] intentionally omitted <==**

This is a homogeneous transport equation for _Q_[˙][(] _a[ℓ]_[+1)] , and since _Q_[˙][(] _a[ℓ]_[+1)] = 0Σ (because _Q_ ˙ ( _aℓ_ +1) = 0Σ ˙ ˙ and _Q_[(] _a[ℓ]_[+1)] _n[a]_ = 0 everywhere, and in particular at Σ), one concludes that _Q_[(] _a[ℓ]_[+1)] = 0, and consequently _Q_[(] _ab[ℓ]_[+2)] _n[b]_ = 0. 

It only remains to prove item 3. which has the additional hypotheses _Q_[¨][(] _[ℓ]_[+1)] = _L_[˙][(] _[ℓ]_[+1)] = 0 (which imply _Q_[(] _αβ[ℓ]_[+1)] = 0 and _L_[(] _µ[ℓ]_[+1)] = 0) and, provided _ℓ_ = n _−_ 2, that _f_[(] _[ℓ]_[+3)] = 0. Then, by (101) for _m_ = _ℓ_ + 1 one has _Q_[˙][(] _a[ℓ]_[+2)] _n[a]_ = 0, and since _Q_[(] _αβ[ℓ]_[+1)] = 0, from item 4. in Lemma 4.13 for _m_ = _ℓ_ + 1 we get tr _P Q_[(] _[ℓ]_[+2)] = 0, which proves the item for _ℓ_ = n _−_ 2. For the case _ℓ_ = n _−_ 2 we cannot use (101) to prove _Q_[˙][(] _a_[n][)] _[n][a]_[= 0][because][we][do][not][know][yet][that] _[f]_[(][n][+1)][= 0.][Instead,][the] strategy is to consider the identities (101) and (107) for _m_ = n _−_ 1 and the identities (99) and (104) for _m_ = n (recall that _Q_[(] _αβ_[n] _[−]_[1)] = 0, _L_[(] _µ_[n] _[−]_[1)] = 0, _L_[(] _a_[n][)] _[n][a]_[= 0][and,][by][item][2.,] _[Q]_[(] _ab_[n][)] _[n][a]_[= 0),] 

**==> picture [319 x 87] intentionally omitted <==**

Combining the second and the fourth yields _Q_[(] _ab_[n][+1)] _n[a] n[b]_ + 2 _κnQ_[˙][(] _a_[n][)] _[n][a]_[=][0,][which][after][inserted] in the third and taking into account the first gives 

**==> picture [256 x 16] intentionally omitted <==**

Since _f_[(][n][+1)] _|_ Σ = 0 we conclude _f_[(][n][+1)] = 0, and as a consequence, _Q_[˙][(] _a_[n][)] _[n][a]_[= 0,][tr] _P[Q]_[(][n][)][= 0][and] _Q_[(] _ab_[n][+1)] _n[a] n[b]_ = 0 also hold. 

21 

˙ _Q_ This˙ ( _ak_ ) _[|]_ Σproposition[= 0 and] _[Q]_[][(] _ab_ shows _[k]_[)][= 0 at all orders, as well as] that it suffices to analyse _[ f]_[(] _[k]_[)][= 0 (except for] equations _L_[][(] _a[k]_[)] _[ k]_ =[=] 0,[ n][+1),] _Q_[¨][(] _[k]_[)] _[ f]_ =[(][n][+1)] 0, _[|] L_[Σ][(][= 0 and] _[k]_[)] = 0, _L_[(] _a_[n][)] _[n][a]_[=][0,][since][the][rest][of][the][conformal][equations][follow][from][them.][Note][that][the][number] of equations agrees with the degrees of freedom to be fixed at each order (i.e. a symmetric tensor **Y**[(] _[k]_[)] and a scalar function _σ_[(] _[k]_[)] ). Indeed, the reduced set of equations _L_[][(] _a[k]_[)] = 0, _Q_[¨][(] _[k]_[)] = 0, ˙  _L_[(] _[k]_[)] = 0, _f_[(] _[k]_[)] = 0 and _Q_[(] _ab[k]_[)][= 0][constitute][exactly][(][n] _[ −]_[1) + 1 + 1 + 1 +][(][n][+][1][)(] 2[n] _[−]_[2][)] =[n][(][n] 2[+][1][)] + 1 equations, the same as the number of degrees of freedom of **Y**[(] _[k]_[)] and _σ_[(] _[k]_[)] . An immediate corollary of this proposition that will be useful in Theorem 5.5 is the following. 

**Corollary 4.16.** _Let_ ( _M, g,_ Ω) _be an_ (n + 1) _-dimensional conformal manifold with null infinity I and assume I admits a cross-section_ Σ _. Fix an integer ℓ ≥_ 1 _and assume that equations L_[(] _µ[k]_[)] = 0 _, Q_[(] _µν[k]_[)][= 0] _[hold][for][every][k][≤][ℓ][,][f]_[(] _[k]_[)][= 0] _[for][every][k][≤][ℓ]_[+ 2] _[,][and][also][L]_[(] _a_[n][)] _[n][a]_[= 0] _[when] ℓ_ = n _−_ 1 _and f_[(][n][+1)] _|_ Σ = 0 _when ℓ_ = n _−_ 2 _. Then,_ 

_1. L_[(] _a[ℓ]_[+1)] _n[a]_ = 0 _._ 

_Assume in addition that L_[(] _a[ℓ]_[+1)] = 0 _, Q_[][˙][(] _a[ℓ]_[+1)] _|_ Σ = 0 _and Q_[(] _ab[ℓ]_[+1)] = 0 _. Then,_ 

**==> picture [155 x 17] intentionally omitted <==**

_If, moreover, we suppose Q_[¨][(] _[ℓ]_[+1)] = _L_[˙][(] _[ℓ]_[+1)] = 0 _and, provided ℓ_ = n _−_ 2 _, that f_[(] _[ℓ]_[+3)] = 0 _. Then_ 

_3. P[ab] Q_[(] _ab[ℓ]_[+2)] = 0 _._ 

Actually, one could have proven Corollary 4.16 directly with much less effort. However, presented in this way it would not have allowed us to count the number of degrees of freedom to be fixed, and ultimately which equations need to be imposed and which ones are automatically fulfilled form the others. 

In the following remark we motivate how the reduced set of equations mentioned below Proposition 4.15 constrain the asymptotic expansion at null infinity. Later, in Section 5 we will use this motivated free data to characterize the full asymptotic expansion at null infinity. 

**Remark 4.17.** _Consider a conformal manifold_ ( _M, g,_ Ω) _with null infinity I (assumed to admit a cross-section ι_ : Σ _→ I ) and denote as usual the embedded metric hypersurface data by {_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}, the asymptotic expansion by {_ **Y**[(] _[k]_[)] _}, and the transverse derivatives of_ Ω _at I by {σ_[(] _[k]_[)] _}. The idea is to see how the reduced set of conformal equations described above Corollary 4.16 constrain {_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}, {_ **Y**[(] _[k]_[)] _}k≥_ 1 _and {σ_[(] _[k]_[)] _}k≥_ 2 _order by order (the quantity σ_[(1)] _is part of the data, see Definitions 3.3 and 3.4). Of course, the first restriction is_ **U** =[1] 2 _[£][n]_ _**[γ]**_[= 0] _[.][Equations] Q_[(1)] _αβ_[= 0] _[ (see]_[(][89][)] _[) impose the following two extra restrictions on the data:][(i)]_ **[ r]**[ =] **[ s]**[+] _[d]_[(log] _[ |][σ]_[(1)] _[|]_[)] _and (ii) σ_[(2)] = 0 _, so the full one-form_ **r** _is determined in terms of metric data and σ. In particular, this means that the surface gravity of ∇_ Ω _vanishes, κ_ := _σ_[(1)] _κn_ + _£nσ_[(1)] = 0 _, so f_[(2)] = 0 _and L_[(1)] _a_ = 0 _follow automatically (by_ (95) _and_ (94) _). Moreover, equations L_[˙][(1)] = 0 (93) _and f_[(3)] = 0 (96) _constrain the pair {κ_[(2)] _, £n_ (tr _P_ **Y** ) _} such that, given a function χ at_ Σ _, there is a unique pair {κ_[(2)] _,_ tr _P_ **Y** _} satisfying L_[˙][(1)] = _f_[(3)] = 0 _and_ tr _P_ **Y** _|_ Σ = _χ. For_ n _̸_ = 3 _, the remaining part of the tensor_ **Y** _that is not yet fixed, namely_ **Y**[] _, becomes completely constrained by equation_  _Q_[(2)] _ab_[=][0] _[(which][is][equivalent][to]_[(][90][)] _[,][because][by][item][1.][in][Prop.][4.15][for][ℓ]_[=][1] _[,][Q]_[(2)] _ab[n][b]_[=][0] _and P[ab] Q_[(2)] _ab_[=][0] _[)][in][terms][of]_ **[Y]**[] _[|]_[Σ] _[.][Showing][this][statement][rigorously][requires][analyzing][the] compatibility between the equations, something we will accomplish in Theorem 5.5._ 

_When_ n = 3 _, the equation Q_[][(2)] _ab_[=][0] _[does][not][constrain]_ **[Y]**[] _[because][the][coefficients][in][front][of] £n_ **Y** _and_ **Y** _in_ (90) _both vanish. In principle, this could mean that Q_[][(2)] _ab_[= 0] _[is][a][new][restriction] on the data {_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, χ}. However, the tensor Q_[(2)] _ab[in][dimension]_[n][=][3] _[identically][vanishes,]_ 

22 

_so it imposes no new restrictions on the data. To see this it suffices to prove it in a gauge in which σ_[(1)] = 1 _and ℓ_[(2)] = 0 _(by the transformations laws_ (50) _and_ (17) _it is easy to see that this gauge can always be achieved), because Q_[(2)] _ab[being][(or][not)][zero][is][a][gauge][invariant][property] provided Q_[(1)] _αβ_[= 0] _[(this][is][a][particular][case][of][Lemma][6.2][below).][So,][in][this][gauge][we][also][have]_ **r** = **s** _and κn_ = 0 _. Under these assumptions, the values of κ_[(2)] _and £n_ (tr _P_ **Y** ) _that are obtained ◦ from L_[˙][(1)] = _f_[(3)] = 0 _are κ_[(2)] = _−_ 4 _P_ ( **s** _,_ **s** ) _and £n_ (tr _P_ **Y** ) = _−_[1] 2  tr _P R −_ 5 div **s** + 9 _P_ ( **s** _,_ **s** ) _, ◦ and therefore the scalar curvature at I is given by R_ = 3(tr _P R_ + _P_ ( **s** _,_ **s** ) _−_ div **s** ) _(see_ (73) _). Inserting this into_ (90) _for_ n = 3 _gives_ 

**==> picture [294 x 23] intentionally omitted <==**

_This tensor is manifestly traceless and its contraction with n[a] vanishes because γabn[a]_ = 0 _and ◦ ◦_  _R_ ( _ab_ ) + s _a_ s _b − ∇_ ( _a_ s _b_ ) _n[a]_ = 0 _(see [37]). Moreover, its pullback to a cross section is [37] Q_[(2)] _AB_[=] _[R] AB[h][−][R]_ 2 _[h][h][AB][,][which][is][identically][zero][in][dimension][two.][So][we][conclude][that][the] equation Q_[(2)] _ab_[= 0] _[is][fulfilled][when][I][is][three-dimensional.]_ 

_For the higher order derivatives the idea is similar but with some important differences. Let us assume that we already know how {_ **Y**[(] _[k]_[)] _, σ_[(] _[k]_[+1)] _, κ_[(] _[k]_[+1)] _} are fixed for every k_ = 1 _, ..., m −_ 1 _. Then, equations L_[(] _a[m]_[)] = 0 (86) _and Q_[˙][(] _a[m]_[)] _|_ Σ = 0 (84) _constrain the remaining part of the one-form_ **r**[(] _[m]_[)] _provided m_ = n _, while equations Q_[¨][(] _[m]_[)] = 0 _, L_[˙][(] _[m]_[)] = 0 _and f_[(] _[m]_[+2)] = 0 _(cf._ (85) _,_ (87) _and_ (88) _) read_ 

**==> picture [419 x 56] intentionally omitted <==**

_where L[m] Q_ ¨ _[,][L][m] L_ ˙ _[and][ L][m] f_[+2] _gather the lower order terms that we already know how are constrained, and Fm_ := (2 _m_ (n _−_ 1) _−_ n) _σ_[(1)] _κn_ + ( _m −_ 1)n _£nσ_[(1)][] _. Given σ_[(] _[m]_[+1)] _|_ Σ _(this is a completely free function associated to the remaining conformal freedom present in Lemma 4.9), this system admits a unique solution for {σ_[(] _[m]_[+1)] _, κ_[(] _[m]_[+1)] _,_ tr _P_ **Y**[(] _[m]_[)] _} provided m ̸_ = n _−_ 1 _. Indeed, taking the Lie derivative of the first one along n and combining it with the three equations in_ (111) _gives (the precise combination can be read off from the RHS)_ 

**==> picture [402 x 36] intentionally omitted <==**

_where Gm_ := _m_ (n _− m −_ 1) _σκn_ + ( _m −_ 1)(n _− m −_ 2) _κ_ = _m_ (n _− m −_ 1) _σκn (recall that the surface gravity κ_ = _σκn_ + _£nσ has already been shown to be zero). This admits a unique solution for_ tr _P_ **Y**[(] _[m]_[)] _with “initial” data determined by the first equation in_ (111) _, namely_ tr _P_ **Y**[(] _[m]_[)] _|_ Σ = ( _m−_ 1)1 _σ_[(1)] (n _−_ 1) _σ_[(] _[m]_[+1)] _|_ Σ _− L[m] Q_ ¨ _[|]_[Σ]  _except when m_ = n _−_ 1 _, because then the coefficient in front of £n_  tr _P_ **Y**[(] _[m]_[)][] _vanishes and G_ n _−_ 1 = 0 _. Finally, equation Q_[][(] _ab[m]_[+1)] = 0 _, which is equivalent to_ (83) _because Q_[(] _ab[m]_[+1)] _n[b]_ = 0 _and P[ab] Q_[(] _ab[m]_[+1)] = 0 _by item 1. in Prop. 4.15_  ( _m_ )  ( _m_ ) _for ℓ_ = _m, constrains the remaining part of_ **Y**[(] _[m]_[)] _, i.e._ **Y** _, in terms of free data_ **Y** _|_ Σ _provided_ 2 _m_ = n _−_ 1 _. As before, this statement requires checking the compatibility with the rest of the equations, see Theorem 5.5 below. Let us now analyse the “special” cases m_ =[n] _[−]_ 2[1] _[,] m_ = n _−_ 1 _and m_ = n _._ 

23 

_Case m_ =[n] _[−]_ 2[1] _(_ n _even)_ 

_In this case, the coefficients multiplying £n_ **Y**[(] _[m]_[)] _and_ **Y**[(] _[m]_[)] _in Q_[(] _ab[m]_[+1)] _(cf._ (83) _) vanish (recall that κ_ = 0 _), and therefore the equation Q_[][(] _ab[m]_[+1)] = 0 _does not constrain_ **Y**[] ( _m_ ) _in terms of_ **Y**  ( _m_ ) _|_ Σ _. Instead, it becomes a potential constraint on the remaining free data, i.e. the metric hypersurface_ ( _k_ ) _data {_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}, the functions_ tr _P_ **Y** _|_ Σ _, {σ_[(] _[k]_[)] _|_ Σ _}k≤m and the tensors {_ **Y**[] _|_ Σ _}k<m. We denote the resulting tensor by Oab[I][and][refer][to][it][as][the][“radiative][obstruction][tensor”.][It][is][symmetric] (since Q is), and by item 1. in Prop. 4.15 it is also transverse, i.e. P[ab] Oab[I]_[= 0] _[and][O] ab[I][n][a]_[= 0] _[.] A more detailed analysis of Oab[I][is][presented][in][Section][6][.]_ 

## _Case m_ = n _−_ 1 

_As already discussed, when m_ = n _−_ 1 _the system_ (111) _no longer determines the set of tensors {σ_[(][n][)] _, κ_[(][n][)] _,_ tr _P_ **Y**[(][n] _[−]_[1)] _} in terms of σ_[(][n][)] _|_ Σ _, as it does for the remaining values of m. Instead, these quantities become fully determined in terms of σ_[(][n][)] _|_ Σ _and κ_[(][n][)] _|_ Σ _through the equations_ ¨ ˙ _Q_[(][n] _[−]_[1)] = 0 _, L_[(][n] _[−]_[1)] = 0 _, L_[(] _a_[n][)] _[n][a]_[=][0] _[and][f]_[(][n][+1)] _[|]_ Σ[=][0] _[(that][is,][we][replace][the][third][equation] f_[(][n][+1)] = 0 _in the system_ (111) _by f_[(][n][+1)] _|_ Σ = 0 _and L_[(] _a_[n][)] _[n][a]_[=][0] _[),][as][we][discuss][next.][First,][the] equations Q_[¨][(][n] _[−]_[1)] = 0 _and L_[˙][(][n] _[−]_[1)] = 0 _(see_ (85) _and_ (87) _) take the form_ 

**==> picture [274 x 18] intentionally omitted <==**

**==> picture [389 x 17] intentionally omitted <==**

_Substituting the expression for κ_[(][n][)] _obtained from_ (114) _into the equation L_[(] _a_[n][)] _[n][a]_[= 0] _[(see]_[(][216][)] _[)] yields_[2] _a second-order transport equation for_ tr _P_ **Y**[(][n] _[−]_[1)] _of the form_ 

**==> picture [421 x 15] intentionally omitted <==**

_for some functions H_[] _i, i_ = 1 _,_ 2 _. Thus, given σ_[(][n][)] _|_ Σ _and κ_[(][n][)] _|_ Σ _, one can then uniquely determine_ tr _P_ **Y**[(][n] _[−]_[1)] _|_ Σ _and £nσ_[(][n][)] _|_ Σ _from Q_[¨][(][n] _[−]_[1)] _|_ Σ = 0 _and f_[(][n][+1)] _|_ Σ = 0 _(see the third equation in_ (112) _which recall is just a rewriting of_ (88) _), namely_ 

**==> picture [319 x 38] intentionally omitted <==**

_and from £nσ_[(][n][)] _|_ Σ _one gets £n_  **Y**[(][n] _[−]_[1)][] _|_ Σ _using_ (113) _. Integrating_ (115) _with this initial data_ tr _P_ **Y**[(][n] _[−]_[1)] _|_ Σ _and £n_  **Y**[(][n] _[−]_[1)][] _|_ Σ _gives_ tr _P_ **Y**[(][n] _[−]_[1)] _everywhere. Once_ tr _P_ **Y**[(][n] _[−]_[1)] _is known, equations_ (113) _and_ (114) _determine σ_[(][n][)] _and κ_[(][n][)] _uniquely. Moreover, since the initial condition £n_  **Y**[(][n] _[−]_[1)][] _|_ Σ _has been fitted so that f_[(][n][+1)] _|_ Σ = 0 _, Proposition 4.15 ensures f_[(][n][+1)] = 0 _every-_ ˙ _where. In summary, we have shown that the equations Q_[¨][(][n] _[−]_[1)] = 0 _, L_[(][n] _[−]_[1)] = 0 _, L_[(] _a_[n][)] _[n][a]_[=][0] _and f_[(][n][+1)] = 0 _form a compatible system which determines uniquely {σ_[(][n][)] _, κ_[(][n][)] _,_ tr _P_ **Y**[(][n] _[−]_[1)] _} in terms of {σ_[(][n][)] _|_ Σ _, κ_[(][n][)] _|_ Σ _}. In particular the system_ (111) _for m_ = n _−_ 2 _is compatible and hence equation_ (112) _is satisfied. Since the LHS of this equations is identically zero when m_ = n _−_ 1 _, it follows that the RHS is also identically zero, which means that there is no obstruction in this case._ 

## _Case m_ = n 

_For this value of m, the coefficient multiplying_ **r**[(] _[m]_[+1)] _in_ (84) _vanishes, and as a consequence thethe equationtensor Q_ ˙ _Q_[(][˙][n][(][)][n] _|_[)] Σ _|_ Σ _only_ = 0 _doesdependsnot imposeon σ_[(][n][)] _,anyκ_[(][n] _new_[)] _andconstraintlower orderon theterms,one-formthat_ **r** _have_[(][n][)] _onalready_ Σ _. Instead,been_ 

> 2Equation (216) is written in a particular gauge, and therefore it will change under another choice of rigging _ξ_ . Nevertheless, its second-order character is gauge invariant. 

24 

˙ _determined, so Q_[(][n][)] _|_ Σ = 0 _becomes a potential constraint on the free data. We denote the resulting tensor by Oa_[Σ] _[and][refer][to][it][as][the][“Coulombic][obstruction”.][Note][that][by][item][1.][of] Proposition 4.15 it satisfies Oa[I][n][a]_[=][0] _[.][A][more][detailed][analysis][of][this][obstruction][tensor][is] undertaken in Section 6._ 

In summary, when n is even, the data that can be freely prescribed at _I_ consist of: 

1. Metric hypersurface data _{_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _}_ satisfying **U** = 0, 

2. The collection of functions _{σ, σ_[(2)] = 0 _, σ_[(3)] _, ...}_ on Σ ( _σ_ is pure metric hypersurface gauge, cf. (50)), 

3. The scalar tr _P_ **Y** on Σ, 

**==> picture [244 x 17] intentionally omitted <==**

5. The full one-form **r**[(][n][)] on Σ. 

> [n] _[−]_[1] When n is odd, one must additionally prescribe the tensor **Y**[][(] 2[)] on _I_ . This extra data must 

> [n] _[−]_[1] of course be compatible with the **Y**[][(] 2[)] _|_ Σ already prescribed in point 4. One way of ensuring 

> [n] _[−]_[1][n] _[−]_[1] this is to just prescribe _£n_ **Y**[][(] 2[)] and solve for **Y**[][(] 2[)] with the already given data at Σ. 

## **5 Existence and uniqueness results** 

In this section we prove that the free data described in Remark 4.17 fully characterizes the geometric structure at null infinity (Theorem 5.2), and reciprocally, that given such free data there exists a conformal spacetime realizing it (Theorem 5.5). It is convenient first to set up the following notions of asymptotic flatness of finite and infinite order. 

**Definition 5.1.** _Let_ ( _M, g,_ Ω) _be a conformal manifold with null infinity I . We say_ ( _M, g,_ Ω) _I is k-asymptotically flat provided it satisfies the quasi-Einstein equation_ (41) _with Tαβ_[(] _[ℓ]_[)] = 0 _for every ℓ ≤ k. When k_ = _∞ we simply say that_ ( _M, g,_ Ω) _is asymptotically flat._ 

This definition is less restrictive that others usually made in the literature (see e.g. the reviews [16, 3] or the classic references [54, 23]), but it is well-adapted to the asymptotic expansion analysis we perform in this paper. We are ready to establish our uniqueness theorem. 

**Theorem 5.2.** _Let_ ( _M, g,_ Ω) _,_ ( _M[′] , g[′] ,_ Ω _[′]_ ) _be two asymptotically flat manifolds with respective null infinities_ Φ : _I →M,_ Φ _[′]_ : _I[′] →M[′] . Choose any conformal gauge on_ ( _M, g,_ Ω) _and_ ( _M[′] , g[′] ,_ Ω _[′]_ ) _such that |∇_ Ω _|_[2] _g_[=][0] _[and][|∇][′]_[Ω] _[′][|]_[2] _g[′]_[=][0] _[,][and][let][ξ][,][ξ][′][be][respective][riggings][of]_[Φ(] _[I]_[ )] _[,]_ Φ _[′]_ ( _I[′]_ ) _extended geodesically. Suppose that I admits a cross section ι_ : Σ _→ I and that there_ 

_ι[′] exists a diffeomorphism χ_ : _I −→ I[′] . Let ι[′]_ := _χ ◦ ι so that_ Σ _[′]_ := _χ_ (Σ) _→ I[′] and let_ Ψ _be the diffeomorphism of Prop. 4.5 constructed between neighbourhoods U ⊂M, U ⊂M[′] of_ Φ(Σ) _,_ Φ _[′]_ (Σ _[′]_ ) _. Define the function ω_ := Ω _[−]_[1] Ψ _[⋆]_ Ω _[′] , which is smooth and nowhere zero on U, and let_ ( _k_ ) _⋆_ ( _k_ ) **Y** := Φ _£ξ_[(] _[ω]_[2] _[g]_[)] _[and][ϖ]_[:= Φ] _[⋆][ω][.][Finally,][assume]_ 

_1. χ[⋆] {_ _**γ**[′] ,_ _**ℓ**[′] , ℓ_[(2)] _[′] }_ = _{ϖ_[2] _**γ** , ϖ_[2] _**ℓ** , ϖ_[2] _ℓ_[(2)] _},_ 

**==> picture [341 x 17] intentionally omitted <==**

**==> picture [100 x 14] intentionally omitted <==**

**==> picture [181 x 16] intentionally omitted <==**

**==> picture [281 x 30] intentionally omitted <==**

25 

_Proof._ Let _g_ := _ω_[2] _g_ and Ω:= _ω_ Ω. Since Φ _⋆ξ_ = _ξ[′]_ we have Ψ _[⋆] σ_[(] _[k]_[)] _[′]_ = _σ_ ~~[(]~~ _[k]_[)] for every _k ≥_ 0, and given that _χ[⋆] {_ _**γ**[′] ,_ _**ℓ**[′] , ℓ_[(2)] _[′] }_ = _{ϖ_[2] _**γ** , ϖ_[2] _**ℓ** , ϖ_[2] _ℓ_[(2)] _}_ , by Proposition 4.6 it suffices to show that _χ[⋆]_ **Y** _[′]_[(] _[k]_[)] = **Y**[(] _[k]_[)] for all _k ≥_ 1. This follows after noting that, except at the exceptional orders, the equations that constrain **Y** _[′]_[(] _[k]_[)] and **Y**[(] _[k]_[)] at each order (see Remark 4.17) are identical and share the same initial conditions (by item 2.), which necessarily forces **Y** _[′]_[(] _[k]_[)] = **Y**[(] _[k]_[)] order by order. The first exception is related to the one-form **r**[(][n][)] , which is constrained by the conformal equations only up to its value at one cross-section, but since by item 3. one has that _χ[⋆]_ **r** _[′]_[(][n][)] = **r** ~~[(]~~[n][)] at Σ, then _χ[⋆]_ **r** _[′]_[(][n][)] = **r** ~~[(]~~[n][)] everywhere. Additionally, when n is even there is another exceptional[n] _[−]_[1] case regarding **Y**[][(] 2[)] because the conformal equations do not constrain it at all. This is taken care by item 4., which imposes _χ[⋆]_ **Y**[] _′_ ( n _−_ 2 1[)] = **Y**[][(][n] _[−]_ 2[1][)] . Hence the conformal equations along with the agreement on the “free data” in items 1.-4. completely constrain the transverse expansion, and then a direct application of Proposition 4.6 yields the result. **Remark 5.3.** _Note that the statement of the theorem already rules out all possible obstructions discussed in Remark 4.17, because_ ( _M, g,_ Ω) _and_ ( _M[′] , g[′] ,_ Ω _[′]_ ) _are assumed to be asymptotically flat (as in Def. 5.1). With comparable effort one can prove that_ Ψ _is an asymptotic isometry_ n _−_ 3 _up to order_[n] _[−]_ 2[3] _for asymptotically flat metrics with differentiability C_ 2 _and non-vanishing obstruction tensors; or an isometry to order_[n] _[−]_ 2[1] _for smooth metrics that are_[n] _[−]_ 2[1] _[-asymptotically] flat._ 

**Remark 5.4.** _It is worth connecting the uniqueness result in Theorem 5.2 with our previous work [44], where we considered conformal manifolds_ ( _M, g,_ Ω) _arising from Fefferman-Graham ambient metrics, which as we proved there are in one-to-one correspondence with manifolds_ ( _M, g,_ Ω) _admitting an integrable conformal Killing vector £ηg_ = 2 _ψg with I as one of the horizons and satisfying £η_ (Ω) = ( _ψ −_ 1)Ω _. As proven in [44], for such manifolds it is always possible to choose the conformal gauge such that ψ_ = 0 _, and thus η is Killing. We now connect this with the fact that, under the assumption that η is a Killing vector and η_ = _[I] αν for some function α, each element of the transverse expansion {_ **Y**[(] _[k]_[)] _} satisfies a constraint given by [46, 47]_ 

**==> picture [455 x 43] intentionally omitted <==**

**==> picture [387 x 31] intentionally omitted <==**

_◦ and Xη[a]_[=] 2[1] _[αn]_[(] _[ℓ]_[(2)][)] _[n][a]_[+] _[ P][ ab]_[] 2 _α_ s _b_ + _∇bα_  _. As proven in [46], when η is non-degenerate, i.e. its surface gravity is nowhere zero, one can always choose ξ|I and extend it geodesically so that P_[(1)] = _**ℓ** ⊗s d_  _£nα_  _and P_[(] _[m]_[)] = 0 _for every m ≥_ 2 _. Contracting_ (116) _for m ≥_ 2 _with n once and twice in this gauge gives_ 

**==> picture [363 x 14] intentionally omitted <==**

_Taking_ Σ _to be the bifurcation surface, where α_ = 0 _and £nα ̸_ = 0 _, one concludes that the free data of item 2. in Theorem 5.2 must be trivial. Note that this statement is gauge invariant because the leading order of_ **Y** _[′]_[(] _[k]_[)] _under a gauge transformation is z[k]_ **Y**[(] _[k]_[)] _. Moreover, condition η_ (Ω) = _−_ Ω _at all orders implies that the free functions {σ_[(] _[k]_[)] _}k≥_ 1 _at_ Σ _are also zero. In conclusion, the only remaining freedom is a traceless tensor_ Ψ _AB_ = Y[] ( _AB_[n] _[−]_ 2[1][)] _|_ Σ _for_ n _odd, from where the full_ **Y**[(][n] _[−]_ 2[1][)] _is constrained by equation_ (116) _. This freedom agrees with the one we obtained by a different argument in [44], which related this tensor to the free data that appears in the Fefferman-Graham construction of the ambient metric._ 

26 

We now prove one of the main results of this paper, namely that given _I_ -structure data (as in Definition 3.3) together with the free data described in Theorem 5.2, it is possible to construct a smooth asymptotically flat[3] spacetime ( _M, g,_ Ω) provided the obstruction tensors vanish. 

**Theorem 5.5.** _Let {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q = 0 _} be an_ n _-dimensional I -structure data admitting a cross-section ι_ : Σ _→ I with induced metric h_ := _ι[⋆]_ _**γ** . Let_ 

- _a. χ be a scalar function on_ Σ _,_ 

- _b. {σ_ Σ[(] _[k]_[)] _[}][k][≥]_[3] _[a][collection][of][scalar][functions][on]_[Σ] _[,]_ 

- _c. {YAB_[(] _[k]_[)] _[}][k][≥]_[1] _[a][set][of][symmetric][tensors][on]_[Σ] _[traceless][w.r.t.][h][,]_ 

- _d._ _**β** and_ m _a one-form and a function on_ Σ _, and_ 

_e. for_ n _odd, let_ Y[] ( _ab_[n] _[−]_ 2[1][)] _be a symmetric transverse tensor on I satisfying ι[⋆]_ Y[][(][n] _[−]_ 2[1][)] = _Y_[(][n] _[−]_ 2[1][)] _._ 

_Assume the obstruction tensors Oa_[Σ] _[and][O] ab[I][constructed][from][this][data][as][described][in][Remark] 4.17 both vanish. Then, there exists a smooth conformal manifold_ ( _M, g,_ Ω) _, an embedding_ Φ : _I →M and a geodesic vector ξ such that (i)_ ( _M, g,_ Ω) _satisfies |∇_ Ω _|_[2] _g_[=][0] _[and][the][quasi-] Einstein equations to infinite order at I_ = _{_ Ω= 0 _}, (ii) {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q _} is_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _in the sense of Def. 3.4, and (iii)_ tr _P_ **Y** _|_ Σ = _χ, £_[(2)] _ξ_[Ω] _[|]_[Σ][=][0] _[and][£]_[(] _ξ[k]_[)][Ω] _[|]_[Σ][=] _[σ]_ Σ[(] _[k]_[)] _for every k ≥_ 3 _,_ ( _ι[⋆]_ **Y**[(] _[k]_[)] ) _[tf]_ = _Y_[(] _[k]_[)] _for every k ≥_ 1 _, ι[⋆]_ **r**[(][n][)] = _**β** and κ_[(][n][)] _|_ Σ = m _. For_ n _odd one has, in addition, that_ Y[] _ab_ ([n] _[−]_ 2[1][)] = Y[] _ab_ ([n] _[−]_ 2[1][)] _._ 

_**Remark:** Note that there is not loss of generality in assuming_ q = 0 _from the beginning because by the comment right after Def. 3.4 a conformal gauge in which_ q = 0 _can always be achieved. Proof._ The strategy of the proof is similar to the one we followed in Theorem 4.7 of [47] with some important differences. The idea is to construct a spacetime ( _M, g_ ) and a function Ωusing Theorem 4.7 and Lemma 4.8 from a collection of “abstract” tensors _{_ Y[(] _[k]_[)] _}k≥_ 1 and functions _{σ_[(] _[k]_[)] _}k≥_ 1 on _I_ so that ( _M, g,_ Ω) satisfies the quasi-Einstein equations to infinite order at _I_ . To do that, we will construct each Y[(] _[k]_[)] and _σ_[(] _[k]_[)] from the equations derived in Section 4 obtained after setting _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[)] = 0 for all _k_ and replacing each **Y**[(] _[k]_[)] by Y[(] _[k]_[)] . To follow a consistent notation we introduce r[(] _[k]_[)] := Y[(] _[k]_[)] ( _n, ·_ ) and k[(] _[k]_[)] := _−_ Y[(] _[k]_[)] ( _n, n_ ) to denote the would-be tensors **r**[(] _[k]_[)] and _κ_[(] _[k]_[)] , respectively. 

## 1. The strategy 

To construct the abstract expansion _{_ Y[(] _[k]_[)] _}_ there arises the following difficulty. Let’s say that we want to use the equation _Q_[(] _ab[k]_[+1)] = 0 to construct Y[(] _[k]_[)] from some initial condition on Σ. By looking at the right hand side of (83) (recall that the tensor _O_[] _ab_[(] _[k]_[)][collects][additional][terms] depending on r[(] _[k]_[)] and _σ_[(] _[k]_[)] ) one immediately realizes that this is not a transport equation, but a partial differential system due to the presence of _∇◦_ -derivatives of r( _k_ ) in _O_  _ab_ ( _k_ )[and][of][tr] _[P]_[Y][(] _[k]_[)][.] This is a complicated system and to the best of our knowledge there is no existence theorem available. In addition, there appears the scalar _κ_[(] _[k]_[+1)] , which is one order higher. Thus, our strategy is to first construct a suitable one-form _**c**_[(] _[k]_[)] and three scalar functions _t_[(] _[k]_[)] , c[(] _[k]_[)] and c[(] _[k]_[+1)] , and then rewrite the equation _Q_[(] _ab[k]_[+1)] = 0 but replacing k[(] _[k]_[)] by c[(] _[k]_[)] , r[(] _[k]_[)] by _**c**_[(] _[k]_[)] , tr _P_ Y[(] _[k]_[)] by _t_[(] _[k]_[)] , and _κ_[(] _[k]_[+1)] by c[(] _[k]_[+1)] . The resulting equation is now an actual transport equation for Y[(] _[k]_[)] , from which we can build Y[(] _[k]_[)] given an initial condition at Σ. Later, we will need to close 

> 3In the sense of Def. 5.1, which as already noted is weaker than other notions in the literature. Stronger conclusions such as e.g. that Ω _[−]_[2] _g_ is vacuum in a full neighbourhood of _I_ clearly cannot be proven with data given only at _I_ . 

27 

the argument by showing that _**c**_[(] _[k]_[)] ( _n_ ) = _−_ c[(] _[k]_[)] , Y[(] _[k]_[)] ( _n, ·_ ) := r[(] _[k]_[)] = _**c**_[(] _[k]_[)] , tr _P_ Y[(] _[k]_[)] = _t_[(] _[k]_[)] and Y[(] _[k]_[+1)] ( _n, n_ ) = _−_ c[(] _[k]_[+1)] for every _k ≥_ 1. 

Now we provide the summary of the argument step by step: Suppose that for a given value[4] of _m ≥_ 1 we have already constructed the collection _{_ Y[(] _[k]_[)] _, σ_[(] _[k]_[)] _}k≤m_ and also _σ_[(] _[m]_[+1)] and c[(] _[m]_[+1)] such that the equations _Q_[(] _αβ[k]_[)][= 0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[+2)] = 0 for all _k ≤ m_ , and _Q_[(] _ab[m]_[+1)] = 0 are all satisfied with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] . Then we construct Y[(] _[m]_[+1)] , _σ_[(] _[m]_[+2)] and c[(] _[m]_[+2)] by following these steps: 

1. We define _**c**_[(] _[m]_[+1)] _|_ Σ as the unique one-form that satisfies (i) _**c**_[(] _[m]_[+1)] ( _n_ ) _|_ Σ = _−_ c[(] _[m]_[+1)] _|_ Σ and (ii) the equation _ι[⋆] Q_[˙][(] _a[m]_[+1)] = 0 (see (84)) with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] . 

2. Given _**c**_[(] _[m]_[+1)] _|_ Σ, we integrate the one-form _**c**_[(] _[m]_[+1)] by solving the equation _L_[(] _a[m]_[+1)] = 0 (86) with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] . We emphasize that our working hypothesis is the function c[(] _[m]_[+1)] has already been fixed at this stage. 

3. Having determined _**c**_[(] _[m]_[+1)] , we build three˙ functions¨ _σ_[(] _[m]_[+2)] , _t_[(] _[m]_[+1)] and c[(] _[m]_[+2)] by solving the system of equations _f_[(] _[m]_[+3)] = _L_[(] _[m]_[+1)] = _Q_[(] _[m]_[+1)] = 0 with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] , _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , tr _P_ **Y**[(] _[m]_[+1)] _→ t_[(] _[m]_[+1)] and _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] , from an initial condition _σ_[(] _[m]_[+2)] _|_ Σ = _σ_ Σ[(] _[m]_[+2)] (see (111) and the subsequent discussion on existence of solutions). The free function _σ_ Σ[(] _[m]_[+2)] simply encodes the residual conformal freedom, as described in Lemma 4.9. 

4. Finally, with the tensors _**c**_[(] _[m]_[+1)] , _σ_[(] _[m]_[+2)] , _t_[(] _[m]_[+1)] and c[(] _[m]_[+2)] just determined, we construct Y[(] _[m]_[+1)] by integrating the equation _Q_[(] _ab[m]_[+2)] = 0 with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] , _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , tr _P_ **Y**[(] _[m]_[+1)] _→ t_[(] _[m]_[+1)] , _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] and **Y**[(] _[m]_[+1)] _→_ Y[(] _[m]_[+1)] , with the initial condition tr _P_ Y[(] _[m]_[+1)] _|_ Σ = _t_[(] _[m]_[+1)] _|_ Σ, Y[(] _[m]_[+1)] ( _n, ·_ ) _|_ Σ = _**c**_[(] _[m]_[+1)] _|_ Σ and (Y[(] _AB[m]_[+1)] ) _[tf] |_ Σ = _YAB_[(] _[m]_[+1)] . 

To close the argument we need to show that the collection _{_ Y[(] _[k]_[)] _, σ_[(] _[k]_[)] _}k≤m_ +1 and also the functions _σ_[(] _[m]_[+2)] and c[(] _[m]_[+2)] satisfy the equations _Q_[(] _αβ[k]_[)][= 0,] _[ L] µ_[(] _[k]_[)] = 0 and _f_[(] _[k]_[+2)] = 0 for all _k ≤ m_ +1, and also _Q_[(] _ab[m]_[+2)] = 0 (each one with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ + 1, and _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] ). This is equivalent to proving three things: (1) That the scalars _**c**_[(] _[m]_[+1)] ( _n_ ) and _−_ c[(] _[m]_[+1)] are the same; (2) That r[(] _[m]_[+1)] := Y[(] _[m]_[+1)] ( _n, ·_ ) agrees with _**c**_[(] _[m]_[+1)] ; And (3) that tr _P_ Y[(] _[m]_[+1)] is the same as _t_[(] _[m]_[+1)] . Finally, we will construct the conformal manifold ( _M, g,_ Ω) from the collection _{_ Y[(] _[k]_[)] _, σ_[(] _[k]_[)] _}k≥_ 1 using Theorem 4.7 and Lemma 4.8, and given that these tensors satisfy _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[)] = 0 (with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] ) for every _k ≥_ 1, it is clear that ( _M, g,_ Ω) will also satisfy _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[)] = 0 to all orders because **Y**[(] _[k]_[)] = Y[(] _[k]_[)] and _£_[(] _ξ[k]_[)][Ω] _[|][I]_[=] _[ σ]_[(] _[k]_[)][for][every] _[k][≥]_[1.] 

## 2. The frst order 

The first order is special because, as already noted several times, the conformal equations have a different structural form at their lowest orders. This fact reflects itself in the way how the one-form _**c**_ and the scalars c, _t_ and _σ_[(2)] will be built. Let us start by defining _**c**_ := **s** + _d_ log _|σ|_ (cf. (89)), and the scalars[5] c := _−£n_ (log _|σ|_ ), _σ_[(2)] = 0 (see (89)) and c[(2)] := c _n_ ( _ℓ_[(2)] ) _−_ 4 _P_ ( _**c** ,_ **s** ) _−_ 

> 4 n _−_ 1 Assume for the sake of the argument that _m_ + 1 is not one of the exceptional values n, n _−_ 1 or 2[.][These] will be dealt with separately. 

> 5Observe that by construction c = _−_ _**c**_ ( _n_ ) so we do not need to worry about proving this at this order, in contrast with the rest of orders. 

28 

_◦ ◦_ 2 _P_ ( _∇_ log _|σ|, ∇_ log _|σ|_ ) (which is obtained after equating (96) to zero with the replacements _κ_[(2)] _→_ c[(2)] , _σ_[(2)] _→_ 0, **r** _→_ _**c**_ and _κn →_ c). We can now construct the function _t_ by integrating the ODE _L_[˙][(1)] = 0 (see (93)) with the replacements **r** by _**c**_ , _κn_ by c, _κ_[(2)] by c[(2)] and tr _P_ **Y** by _t_ , and with the initial condition _t|_ Σ = _χ_ . Next, if n _>_ 3 we construct the tensor Y _ab_ by integrating the transport equation _Q_[(2)] _ab_[=][0][(cf.][(][90][))][obtained][after][replacing] **[r]**[by] _**[c]**_[,] _[κ][n]_[by][c][,] _[κ]_[(2)][by][c][(2)] and tr _P_ **Y** by _t_ , with the initial conditions Y _[tf] AB[|]_[Σ][=] _[ Y][AB]_[,][tr] _[P]_[Y] _[|]_[Σ][=] _[ t][|]_[Σ][and][r] _[|]_[Σ][=] _**[ c]**[|]_[Σ][,][namely] 

**==> picture [393 x 44] intentionally omitted <==**

where R is given by (73) with the corresponding replacements (tr _P_ **Y** _→ t_ , _κ_[(2)] _→_ c[(2)] , **r** _→_ _**c**_ , _κn →_ c). If n = 3 we simply define the symmetric tensor Y _ab_ by means of the decomposition (30) with the values Y _abn[b]_ = _ca_ , tr _P_ Y = _t_ and its transverse part given by the data Y[] _ab_ prescribed in item (e) of the theorem. Recall that for n = 3 the equation _Q_[(2)] _ab_[= 0][holds][automatically.] 

We now prove that in the case n _>_ 3, r = _**c**_ and tr _P_ Y = _t_ everywhere (for n = 3 it holds by construction). Firstly, we contract equation (118) with _n_ and use identity (28) twice (with _ωa_ = _ca_ and _ωa_ = s _a_ ) and _R◦_ ( _ab_ ) _nb_ = 12 _[£][n]_[s] _[a]_[[][37][]][to][get] 

**==> picture [424 x 31] intentionally omitted <==**

Contracting it again with _n_ and recalling the notation k _n_ := _−_ r( _n_ ) = _−_ Y( _n, n_ ), 

> _[◦] ◦_ 2 0 = _−_ (n _−_ 3) _σ£n_ k _n −_ (n _−_ 3) _σ_ c k _n_ + (n _−_ 1) _n[a] n[b] ∇a∇bσ_ + 2 _σ_ (n _−_ 2) _£n_ c _−_ 2 _σ_ c _._ (120) Additionally, the contraction of (118) with _P[ab]_ gives, after using (29), 

0 = (n _−_ 3) _σ£n_ (tr _P_ Y) + 4 _σ_ (n _−_ 3) _P_ (r _,_ **s** ) _− σ_ (n _−_ 3) _n_ ( _ℓ_[(2)] )k _n_ + (n _−_ 3) _σ_ c tr _P_ Y + (n _−_ 1)□ _P σ ◦ −_ 2 _σ_ (n _−_ 2) div _P_ _**c**_ + _σ_  div _P_ **s** _−_ 2 _P_ ( _**c** ,_ _**c**_ ) + 4 _P_ ( _**c** ,_ _**s**_ ) _− P_ ( _**s** ,_ _**s**_ ) + tr _P R_  _−_[n] _[ −]_[1][(121)] 2n _[σ]_[R] _[.]_ 

Next, we construct an auxiliary spacetime ( _M_ 1 _, g_ 1) using Theorem 4.7 from the sequence _{_ T[(] _ab[k]_[)] _[}][k][≥]_[1][defined][by][(cf.][(][30][))] 

**==> picture [307 x 26] intentionally omitted <==**

and T[(] _ab[k]_[)][= 0][for][every] _[k][≥]_[3.][It][is][immediate][to][check][that] _[P][ ab]_[T][(1)] _ab_[=] _[ t]_[,][T][(1)] _ab[n][a]_[=][ ] _[c][b][ −]_[c] _[ℓ][b]_[=] _[ c][b]_ and T[(2)] _ab[n][a][n][b]_[=] _[ −]_[c][(2)][.][We also construct a function Ω][1][on] _[ M]_[1][using Borel’s Lemma][ 4.8][ from the] sequence _{_ 0˙ _, σ,_ 0 _,_ 0 _, ..._ ¨ _}_ . Since ( _M_ 1 _, g_ 1 _,_ Ω1) satisfies _L_[(1)] _µ_ = 0, _Q_[(1)] _αβ_[= 0 and] _[ f]_[(1)][=] _[ f]_[(2)][=] _[ f]_[(3)][= 0] ( _L_[˙] = 0, _Qa_ = 0, _Q_ = 0 and _f_[(3)] = 0 hold by construction, and _Qab_ = 0, _La_ = 0 and _f_[(1)] = _f_[(2)] = 0 are automatically true, see (89), (94), (95)), the first item in Proposition 4.15 (with _ℓ_ = 1) ensures that it also satisfies _Q_[(2)] _ab[n][a]_[= 0 and] _[ P][ ab][Q]_[(2)] _ab_[= 0, which imply the following:] 

1. The scalar c = _−_ **T**[(1)] ( _n, n_ ) satisfies the same equation as k _n_ (cf. (120)) with the replacement k _n →_ c, namely 

**==> picture [332 x 15] intentionally omitted <==**

Subtracting both equations one then arrives at 

**==> picture [210 x 12] intentionally omitted <==**

This is a linear homogeneous ODE for k _n −_ c, and since k _n_ and c agree on Σ (because of the initial data we have imposed when solving (118)) we conclude k _n_ = c everywhere. 

29 

2. Once k _n_ = c is known to be true, the one-form _**c**_ = **T**[(1)] ( _n, ·_ ) satisfies the same equation than r (119) with the replacement r _→_ _**c**_ , namely 

      - _[◦] ◦ ◦_ 

      - 0 = (n _−_ 3) _σ£nca_ + (n _−_ 3) _σ_ c _ca_ + (n _−_ 1) _n[b] ∇a∇bσ − σ_ (n _−_ 2)( _£nca − ∇a_ c + 2cs _a_ ) + _σ£n_ s _a_ + 2 _σ_ c( _ca −_ s _a_ ) _,_ 

   - so subtracting it from (119) and using that r _|_ Σ = _**c** |_ Σ, it follows that _**c**_ = r everywhere. 

3. Finally, once we have shown that _**c**_ = r, the scalar _t_ = _P[ab]_ T[(1)] _ab_[satisfies][the][same][equation] than tr _P_ Y (121) with the replacement tr _P_ Y _→ t_ , namely 

   - 0 = (n _−_ 3) _σ£nt_ + 4 _σ_ (n _−_ 3) _P_ (r _,_ **s** ) _− σ_ (n _−_ 3) _n_ ( _ℓ_[(2)] )k _n_ + (n _−_ 3) _σ_ c _t_ + (n _−_ 1)□ _P σ_ 

**==> picture [397 x 23] intentionally omitted <==**

Subtracting them and using that they coincide at Σ we also conclude that _t_ = tr _P_ Y everywhere. 

Note that at this point we have already constructed _σ_[(2)] , c[(2)] and the full tensor Y _ab_ . The construction guarantees that the equations _Q_[¨][(1)] = 0, _f_[(3)] = 0, _Q_[˙][(1)] _a_ = 0, _L_[˙][(1)] = 0 and _Q_[(2)] _ab_[= 0] are fulfilled. Recall also that _Q_[(1)] _ab_[= 0][and] _[L]_[(1)] _a_ = 0 hold automatically. 

## 3. Higher order terms 

For the higher order terms we apply a similar strategy. Fix _m ≥_ 1 (suppose that _m_ + 1 is not one of the exceptional values, i.e. that _m_ + 1 =[n] _[−]_ 2[1][,] _[m]_[ + 1][=][n][and] _[m]_[ + 1][=][n] _[ −]_[1)][and][that] we have already constructed _{_ Y[(] _[k]_[)] _, σ_[(] _[k]_[)] _}_ for all _k ≤ m_ and also _σ_[(] _[m]_[+1)] and c[(] _[m]_[+1)] , and that the equations _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0, _f_[(] _[k]_[+2)] = 0 (with the replacements _{_ **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] _}k≤m_ and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] ) hold for every _k ≤ m_ , and also _Q_[(] _ab[m]_[+1)] = 0. Note that this is what we achieved in the first order. We now follow the steps 1.-4. that we explained in the strategy of the proof. 

1. We construct uniquely _**c**_[(] _[m]_[+1)] _|_ Σ from conditions (i) _**c**_[(] _[m]_[+1)] ( _n_ ) _|_ Σ = _−_ c[(] _[m]_[+1)] _|_ Σ and such that (ii) the equation _ι[⋆] Q_[˙][(] _a[m]_[+1)] = 0 with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] is fulfilled. 

2. Given _**c**_[(] _[m]_[+1)] _|_ Σ, we integrate the one-form _**c**_[(] _[m]_[+1)] by solving the equation _L_[(] _a[m]_[+1)] = 0 (86) with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] and _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , namely 

**==> picture [413 x 21] intentionally omitted <==**

**==> picture [409 x 14] intentionally omitted <==**

**==> picture [423 x 33] intentionally omitted <==**

3. With the _**c**_[(] _[m]_[+1)] constructed in 2., we build the three˙ functions¨ _σ_[(] _[m]_[+2)] , _t_[(] _[m]_[+1)] and c[(] _[m]_[+2)] by solving the system of equations _f_[(] _[m]_[+3)] = _L_[(] _[m]_[+1)] = _Q_[(] _[m]_[+1)] = 0 (see (111)) with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] , tr _P_ **Y**[(] _[m]_[+1)] _→ t_[(] _[m]_[+1)] and _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] ) from the initial condition _σ_[(] _[m]_[+2)] _|_ Σ = _σ_ Σ[(] _[m]_[+2)] . 

4. Finally, we construct Y[(] _ab[m]_[+1)] by integrating the equation _Q_[(] _ab[m]_[+2)] = 0 with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] , _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , tr _P_ **Y**[(] _[m]_[+1)] _→ t_[(] _[m]_[+1)] , _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] and **Y**[(] _[m]_[+1)] _→_ Y[(] _[m]_[+1)] with the initial conditions tr _P_ Y[(] _[m]_[+1)] _|_ Σ = _t_[(] _[m]_[+1)] _|_ Σ, Y[(] _[m]_[+1)] ( _n, ·_ ) _|_ Σ = _**c**_[(] _[m]_[+1)] _|_ Σ and (Y[(] _AB[m]_[+1)] ) _[tf] |_ Σ = _YAB_[(] _[m]_[+1)] . 

30 

Once the tensors _{_ Y[(] _[k]_[)] _, σ_[(] _[k]_[)] _}k≤m_ +1 and the functions _σ_[(] _[m]_[+2)] and c[(] _[m]_[+2)] are built, we need to check that the equations _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[+2)] = 0 hold for all _k ≤ m_ + 1, and also _Q_[(] _ab[m]_[+2)] = 0 (each one with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ + 1, and _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] ). To do that it suffices to prove that (1) _**c**_[(] _[m]_[+1)] ( _n_ ) = _−_ c[(] _[m]_[+1)] , (2) Y[(] _[m]_[+1)] ( _n, ·_ ) = _**c**_[(] _[m]_[+1)] , and (3) tr _P_ Y[(] _[m]_[+1)] = _t_[(] _[m]_[+1)] . 

To prove the three claims we shall construct an auxiliary spacetime ( _Mm, gm_ ) using Theorem 4.7 from the sequence _{_ **T**[(] _[k]_[)] _}k≥_ 1, with **T**[(] _[k]_[)] = Y[(] _[k]_[)] for all _k ≤ m_ , 

**==> picture [455 x 26] intentionally omitted <==**

and T[(] _ab[k]_[)][= 0][for][every] _[k][≥][m]_[ + 3.][We][also][construct][a][function][Ω] _[m]_[on] _[M][m]_[from][the][sequence] _{_ 0 _, σ,_ 0 _, ..., σ_[(] _[m]_[+2)] _,_ 0 _, ...}_ using Borel’s Lemma 4.8. Note that _P[ab]_ T[(] _ab[m]_[+1)] = _t_[(] _[m]_[+1)] , T[(] _ab[m]_[+1)] _n[b]_ =  _c_[(] _[m]_[+1)] _−_ c[(] _[m]_[+1)] _ℓa_ , T[(] _ab[m]_[+1)] _n[a] n[b]_ = _−_ c[(] _[m]_[+1)] and T[(] _ab[m]_[+2)] _n[a] n[b]_ = _−_ c[(] _[m]_[+2)] , but we do not yet know that _**c**_[(] _[m]_[+1)] ( _n_ ) = _−_ c[(] _[m]_[+1)] . To establish this we note that by construction this spacetime satisfies the equations _Q_[(] _αβ[k]_[)][= 0,] _[L]_[(] _µ[k]_[)] = 0 for _k ≤ m_ and _f_[(] _[k]_[)] = 0 for _k ≤ m_ + 2. So, item 1. of Corollary 4.16 for _ℓ_ = _m_ yields firstly _L_[(] _a[m]_[+1)] _n[a]_ = 0, which by (86) takes the form 

**==> picture [375 x 21] intentionally omitted <==**

The key point is that the lower order terms in this equation are, by construction, the same ones as in (123). Thus, subtracting both equations we get a homogeneous first order ODE for _c_[(] _a[m]_[+1)] _n[a]_ + c[(] _[m]_[+1)] , and since _**c**_[(] _[m]_[+1)] ( _n_ ) _|_ Σ = _−_ c[(] _[m]_[+1)] _|_ Σ we conclude _**c**_[(] _[m]_[+1)] ( _n_ ) = _−_ c[(] _[m]_[+1)] everywhere. 

Once we have shown _**c**_[(] _[m]_[+1)] ( _n_ ) = _−_ c[(] _[m]_[+1)] we also have T[(] _ab[m]_[+1)] _n[b]_ =  _c_[(] _[m]_[+1)] _−_ c[(] _[m]_[+1)] _ℓa_ = _c_[(] _a[m]_[+1)] and we are ready to prove the other two claims, namely that Y[(] _[m]_[+1)] ( _n, ·_ ) = _**c**_[(] _[m]_[+1)] and tr¨ _P_ Y[(] _[m]_[+1)] =˙ _t_[(] _[m]_[+1)] . First of all note that ( _Mm, gm,_ Ω _m_ ) satisfies _L_[(] _a[m]_[+1)] = 0, _ι[⋆] Q_[˙][(] _a[m]_[+1)] = 0, _Q_[(] _[m]_[+1)] = _L_[(] _[m]_[+1)] = _f_[(] _[m]_[+3)] = 0 (because these were the equations we used to obtain _**c**_[(] _[m]_[+1)] , _σ_[(] _[m]_[+2)] , _t_[(] _[m]_[+1)] and c[(] _[m]_[+2)] ) and _Q_[(] _ab[m]_[+1)] = 0 (by assumption). Then, items 2. and 3. in Corollary 4.16 (with _ℓ_ = _m_ ) imply that ( _Mm, gm,_ Ω _m_ ) satisfies also _Q_[(] _ab[m]_[+2)] _n[a] n[b]_ = 0, _Q_[(] _ab[m]_[+2)] _n[a]_ = 0 and _P[ab] Q_[(] _ab[m]_[+2)] = 0. From (83) with **Y**[(] _[m]_[+1)] _→_ **T**[(] _[m]_[+1)] we get (for the third one we use (29), and define for shortness _Nm_[n][:=][ n] _[ −]_[3] _[ −]_[2] _[m][ ̸]_[= 0)] 

**==> picture [425 x 101] intentionally omitted <==**

But the tensor Y[(] _[m]_[+1)] is the solution of the equation _Q_[(] _ab[m]_[+2)] = 0 with the replacements **Y**[(] _[k]_[)] _→_ Y[(] _[k]_[)] for every _k ≤ m_ , **r**[(] _[m]_[+1)] _→_ _**c**_[(] _[m]_[+1)] , _κ_[(] _[m]_[+1)] _→_ c[(] _[m]_[+1)] , tr _P_ **Y**[(] _[m]_[+1)] _→ t_[(] _[m]_[+1)] , _κ_[(] _[m]_[+2)] _→_ c[(] _[m]_[+2)] and **Y**[(] _[m]_[+1)] _→_ Y[(] _[m]_[+1)] . This means that the equations _Q_[(] _ab[m]_[+2)] _n[a] n[b]_ = 0, _Q_[(] _ab[m]_[+2)] _n[a]_ = 0 and 

31 

_P[ab] Q_[(] _ab[m]_[+2)] = 0 (with the corresponding replacements) are also satisfied. Explicitly, 

**==> picture [428 x 101] intentionally omitted <==**

By subtracting both systems and recalling that _Nm_[n][= 0 (because we have assumed] _[ m]_[+1] _[ ̸]_[=][n] _[−]_ 2[1][)] and that the lower order terms agree (by construction), one arrives at a homogeneous hierarchical system of ODEs for c[(] _[m]_[+1)] _−_ k[(] _[m]_[+1)] , _**c**_[(] _[m]_[+1)] _−_ r[(] _[m]_[+1)] and _t_[(] _[m]_[+1)] _−_ tr _P_ Y[(] _[m]_[+1)] . Since these quantities vanish at Σ (because of the initial conditions employed to build Y[(] _ab[m]_[+1)] ) one concludes that they vanish everywhere. 

Summarizing, the tensors Y[(] _[m]_[+1)] , _σ_[(] _[m]_[+2)] and c[(] _[m]_[+2)] we have just constructed satisfy the equa˙ ¨  tions _Q_[(] _ab[m]_[+2)] = 0, _L_[(] _a[m]_[+1)] = 0, _L_[(] _[m]_[+1)] = _Q_[(] _[m]_[+1)] = _f_[(] _[m]_[+3)] = 0 and _Q_[˙][(] _a[m]_[+1)] _|_ Σ = 0. An application of item 2. in Corollary 4.16 (with _ℓ_ = _m_ ) for ( _Mm, gm,_ Ω _m_ ) shows that Y[(] _[m]_[+1)] also satisfies _Q_[˙][(] _a[m]_[+1)] = 0 because Y[(] _ab[m]_[+1)] = T[(] _ab[m]_[+1)] . Then, the equations _Q_[(] _αβ[k]_[)][=][0,] _[L]_[(] _µ[k]_[)] = 0 and _f_[(] _[k]_[+2)] = 0 hold for all _k ≤ m_ + 1, and also _Q_[(] _ab[m]_[+2)] = 0. This closes the induction argument. To conclude the proof we only need to analyze the three exceptional cases. 

- In the case _m_ + 1 =[n] _[−]_ 2[1] (when n is odd) the only thing that changes is that the equation _Q_ ( _ab_[n][+1] 2[)] = 0 cannot be employed to build Y[(][n] _[−]_ 2[1][)] . Instead, we construct it using decompo[n] _[−]_[1][n] _[−]_[1][n] _[−]_[1][n] _[−]_[1] 

- sition (30) with r[(] 2[)] := _**c**_[(] 2[)] , tr _P_ Y[(] 2[)] := _t_[(] 2[)] and the transverse part given by the free data Y[][(][n] _[−]_ 2[1][)] . Note that equation _Q_ ( _ab_[n][+1] 2[)] = 0 still holds by hypothesis because we have assumed _Oab[I]_[= 0.][Here][obviously][we][do][not][need][to][prove][that][Y][(] _[m]_[+1)][(] _[n,][ ·]_[) =] _**[ c]**_[(] _[m]_[+1)][and] tr _P_ Y[(] _[m]_[+1)] = _t_[(] _[m]_[+1)] . The rest of the argument remains unchanged. 

- When _m_ +1 = n _−_ 1, the problem is that the system (111) does not determine the quantities _{σ_[(][n][)] _,_ c[(][n][)] _, t_[(][n] _[−]_[1)] _}_ , so instead we integrate the second-order transport equation (115) with the replacement tr _P_ **Y**[(][n] _[−]_[1)] _→ t_[(][n] _[−]_[1)] with the initial conditions _t_[(][n] _[−]_[1)] _|_ Σ and _£nt_[(][n] _[−]_[1)] _|_ Σ determined from _σ_ Σ[(][n][)] and c[(][n][)] _|_ Σ := m using the equations _Q_[¨][(][n] _[−]_[1)] _|_ Σ = 0 and _f_[(][n][+1)] _|_ Σ = 0, exactly as explained in Remark 4.17. The remainder of the argument proceeds identically. 

- Finally, for _m_ + 1 = n the issue is that the equation _Q_[][˙][(] _a_[n][)] _[|]_ Σ[=][0][cannot][be][imposed][to] obtain the value of the one-form _**c**_[(][n][)] at Σ, and instead we establish _ι[⋆]_ _**c**_[(][n][)] = _**β**_[(][n][)] and _**c**_[(][n][)] ( _n_ ) _|_ Σ = _−_ c[(][n][)] _|_ Σ as initial condition. Note again that the equation _Q_[][˙][(] _a_[n][)] _[|]_ Σ[=][0][holds] by hypothesis because we have assumed _Oa_[Σ][=][0.][The][argument][continues][in][the][same] manner. 

Once the full collections _{σ_[(] _[k]_[)] _}k≥_ 0 and _{_ Y[(] _[k]_[)] _}k≥_ 1 have been constructed, we use Borel’s Lemma 4.8 and Theorem 4.7 to build a function Ωand a spacetime ( _M, g_ ) that satisfies _f_[(] _[k]_[)] = 0, _Q_[(] _αβ[k]_[)][=][0][and] _[L]_[(] _α[k]_[)] = 0 for all _k ≥_ 1. Therefore, ( _M, g,_ Ω) solves the conformal Einstein equations to infinite order at _I_ and realizes the initial data. 

## **6 Obstruction tensors at** _I_ **. Four and six dimensional cases** 

The purpose of this section is to study the obstruction tensors at their lowest non-trivial orders, namely the Coulombian obstruction tensor _Oa_[Σ][in][spacetime][dimension][four][(][n][=][3)][and][the] 

32 

radiative obstruction tensor _Oab[I]_[in][spacetime][dimension][six][(][n][ = 5),][because][recall][that] _[Q]_[(2)] _ab_[is] identically zero in spacetime dimension four. First of all we put forward the precise definition of the obstruction tensors. 

**Definition 6.1.** _Let_ ( _M, g,_ Ω) _be an_ (n + 1) _-dimensional conformal manifold with null infinity_ Φ : _I →M written in a conformal gauge satisfying |∇_ Ω _|_[2] = 0 _. Let ξ be a rigging extended off_ Φ( _I_ ) _geodesically, ι_ : Σ _→ I a cross-section and Q_ := (n _−_ 1) Hess Ω+ ΩSch _g_  _. We define the radiative obstruction tensor O[I] (for_ n _odd) and the Coulombian obstruction tensor O_[Σ] _(for any_ n _) by means of_ 

**==> picture [253 x 21] intentionally omitted <==**

A definition of the obstruction tensors can also be given in an arbitrary conformal gauge, but this is beyond the scope of this paper. 

## **6.1 Coulombian obstruction in four dimensions** 

As already indicated in the previous section, the factor (n _− m_ ) multiplying **r**[(] _[m]_[)] in equation ˙ _Q_[(] _a[m]_[)] _|_ Σ = 0 leads to two important consequences when _m_ = n. The first one is that the equation does not constrain the value of the one-form  **r**[(][n][)] _|_ Σ (which therefore becomes free data), and the second one is that if the reminder of the equation does not vanish, either the conformal spacetime is not smooth or does not satisfy the Einstein equations beyond order _m −_ 1. This reminder defines the Coulombian obstruction tensor _Oa_[Σ][.][In][spacetime][dimension][four,] _[O] a[I]_[=] _[Q]_[˙][(3)] _a_[,][and] hence it depends on the _I_ -structure data, **Y** , **Y**[(2)] , _σ_[(3)] and _κ_[(3)] . These tensors are uniquely given in terms of the free data _{χ, σ_ Σ[(3)] _[,]_[ m] _[,][ Y] AB_[(1)] _[}]_[ on Σ and the radiation field][ ][Y] _[ab]_[on] _[ I]_[after solv-] ing the equations _Q_[(1)] _αβ_[=] _[Q]_[(2)] _αβ_[=][0,] _[L][µ]_[=] _[L]_[(2)] _µ_ = 0, _f_[(2)] = _f_[(3)] = 0, _L_[(3)] _a[n][a]_[=][0][and] _[f]_[(4)] _[|]_ Σ[=][0.] Note also that by Prop. 4.15 the equations _Q_[˙][(3)] _a[n][a]_[=][0,] _[Q]_[(3)] _ab[n][a]_[=][0,] _[P][ ab][Q]_[(3)] _ab_[=][0][and] _[f]_[(4)][=][0] follow automatically, so in particular the obstruction tensor satisfies _Oa_[Σ] _[n][a]_[= 0.] 

In order to find a necessary and sufficient condition for _Oa_[Σ][to][vanish,][let][us][note][that][since] _Qαβ_ vanishes up to an including order 2, it suffices to study the tensor _Q_ ˙[(3)] _a_ in any gauge, since its vanishing is a gauge-invariant statement. This is a consequence of the following simple observation. 

**Lemma 6.2.** _Assume Q_[(] _αβ[k]_[)][=][0] _[for][all][k]_[=][1] _[, ..., m][.][Let][ξ][′]_[=] _[z]_[(] _[ξ]_[ +] _[ V]_[ )] _[,][with][z][and][V][extended] ′ arbitrarily off I . Then, Q_[(] _ab[m]_[+1)] := ( _£_[(] _ξ[m][′]_[)] _[Q]_[)] _[ab]_[=] _[ z][m][Q]_[(] _ab[m]_[+1)] _._ 

_Proof._ The result is obtained at once by inserting _ξ[′]_ = _z_ ( _ξ_ + _V_ ) into _£_[(] _ξ[m][′]_[)] _[Q][αβ]_[and using] _[ Q]_[(] _αβ[k]_[)][= 0] for all _k_ = 1 _, ..., m_ . 

Hence, it is sufficient to analyze _Oa_[Σ][in][a][gauge][in][which] _[σ]_[(1)][=][1,] _[ℓ]_[(2)][=][0][and][the][pullback] of _**ℓ**_ to the cross-sections of _I_ vanishes, _**ℓ** ∥_ = 0. This immediately implies **s** = 0 [43, 42] and hence **r** = **s** + _dσ_[(1)] = 0. Moreover, the tensor _P_ at Σ decomposes as _P[ab]_ = _h[AB] e[a] A[e][b] B_[,] where _h[AB]_ is the inverse metric of _hAB_ and _{eA}_ is a basis in Σ with dual _{_ _**θ**[A] }_ , and therefore _δρ[α]_[=] _[ e][α] B[θ] ρ[B]_[+] _[ ξ][α][ν][ρ]_[+] _[ ν][α][ξ][ρ]_[.][Since][the][tensor] _[Q]_[involves][up][to][third][derivatives][of][the][metric][and] the quasi-Einstein equations to second order are imposed, it is to be expected that _Q_ may have some relation to derivatives of the Weyl tensor. We pursue this idea by applying a transverse derivative to the identity (44) and evaluating the result at _I_ . Since _Q_ vanishes up to order two, we may perform the substitution _Tαβ_ = n _−_ 1 1 _[Q][αβ]_[=] 2(nΩ _−_[2] 1) _[P][αβ]_[for][some][tensor] _[P][αβ]_[satisfying] 

33 

_Q_[(3)] = _P_[(1)] at _I_ . Rewriting identity (44) (recall _d_ = n + 1) in terms of _Pαβ_ gives 

**==> picture [343 x 53] intentionally omitted <==**

Applying _∇ξ_ (here it turns out to be more useful to take a covariant derivative along _ξ_ rather than a Lie derivative) and evaluating the result at Ω= 0 gives (we use that _ξ_ (Ω) = _[I] σ_[(1)] = 1 and _[I] I_ hence _νµ_ = _∇µ_ Ω) 

**==> picture [431 x 26] intentionally omitted <==**

The second term in the left-hand side vanishes because _ξ[ρ] ∇ρ∇α_ Ω = _[I]_ n _−_ 1 1 _[Q] ρα_[(1)] _[ξ][ρ][ −]_[Ω] _[ξ][ρ][L] ρα_ = _I_ 0, so we arrive at 

**==> picture [398 x 25] intentionally omitted <==**

We now contract this equation with _ξ[β] e[µ] A[ξ][ν]_[to][make][the][tensor][E] _[αβ]_[:=] _[ ξ][µ][ξ][ν][C][αµβν]_[appear.][The] contraction of (124) with _ξ[β] e[µ] A[ξ][ν]_[then][gives,][after][using] _[e][µ] A[ν][µ]_[=] _[ e][µ] A[ξ][µ]_[=] _[ ξ][µ][ξ][µ]_[= 0,] _[ν][α][ξ][α]_[= 1][and] _∇ξξ_ = 0, 

**==> picture [333 x 24] intentionally omitted <==**

We still need to elaborate the second term in the left-hand side. Note that due to **r** = **s** = 0 and _ℓ_[(2)] = 0 we have from (27), (10) and (11) that _∇[α] ξ[β]_ = _P[ac] V[b] ce[α] a[e][β] b_[=] _[ P][ ac][P][ bd]_[(Y] _[cd]_[ + F] _[cd]_[)] _[e] a[α][e][β] b_[=] _h[AC] h[BD]_ (Y _CD_ + F _CD_ ) _e[α] A[e][β] B_[,][and][hence] 

**==> picture [325 x 37] intentionally omitted <==**

where we recall the notation in Appendix A for[(2)] _Cαβµ_ := _ξ[ν] Cανβµ_ . We finally use _δρ[α]_[=] _e[α] B[θ] ρ[B]_[+] _[ ξ][α][ν][ρ]_[+] _[ ν][α][ξ][ρ]_[in][the][first][term][of][the][right-hand][side][to][get] 

**==> picture [289 x 38] intentionally omitted <==**

where in the first term we used _e[µ] A[e] B[α][θ] ρ[B][∇][α]_[E] _[ρµ]_[=] _[∇][h] B_[E] _[BA]_[(because][E][is][orthogonal][both][to] _[ξ]_ and _ν_ ), and the third term vanishes because _ν[α] ∇αξ[ρ]_ = _[I]_ 0 (by (26) and (11)) and E( _ξ, ·_ ) = 0. Therefore, we conclude 

**==> picture [439 x 23] intentionally omitted <==**

In four spacetime dimensions (n = 3) the first term vanishes and the tensor[(2)] _CABC_ is zero, because the identity (44) entails _Cαβµνν[α]_ = _[I]_ 0, so _Cαβµν_ has Petrov type _N_ at _I_ , and all its non-vanishing components at _I_ are encoded in E _αβ_ (see [51, 15]). Since _Q_[˙][(3)] _A_ = _OA_[Σ][,][then][a] necessary and sufficient condition for the Coulombian obstruction tensor to vanish is E _AB_ being divergence-free. When the cuts of _I_ are 2-spheres (e.g. for asymptotically simple spacetimes [50]), the fact that there are no TT tensors on S[2] [63] imply that _Oa_[Σ][= 0 if and only if][ E] _[AB]_[= 0,] 

34 

and hence the full Weyl tensor vanishes at _I_ . For other topologies of _I_ , such as R _× T_[2] (see [59]), E _AB_ being divergence-free does not imply E _AB_ = 0. One can then construct four dimensional, smooth, asymptotically flat spacetimes (in the sense of Def. 5.1) as a particular case of Theorem 5.5 with _I ̸≃_ R _×_ S[2] whose Weyl tensor does not vanish at _I_ . Establishing existence in the stronger sense that the spacetime Ω _[−]_[2] _g_ is Ricci flat in a neighborhood of _I_ is an interesting and open problem. To the best of our knowledge, the asymptotic characteristic problem has only been solved under the assumption that the Weyl tensor vanishes at _I_ [33, 28] (and in dimension 4). 

Equation (125) is interesting also in higher dimensions, because if one is interested in using the Weyl as a variable to be determined iteratively from an expansion, (125) can be used to compute the second order term _ναe[µ] A[ξ][ρ][∇][ρ]_[E] _[αµ]_[in][terms][of][E][,][(2)] _[C][ABC]_[and] _[Q]_[˙][(3)][provided][n][=][3][(recall] that in higher dimension the tensor[(2)] _CABC_ need not to vanish, see [51]). When n = 3 the Coulombian obstruction would manifest itself also in this approach. 

## **6.2 Radiative obstruction in six dimensions** 

As already mentioned, for n odd the equation _Q_ ( _ab_[n][+1] 2[)] = 0 does not fix the full tensor **Y**[(][n] _[−]_ 2[1][)] . ([n][+1] 2[)] Furthermore, after having assumed that the previous orders are satisfied, the tensor _Qab_ turns out to only depend on null metric hypersurface data, _χ_ , _{σ_ Σ[(] _[k]_[)] _[}] k≤_[n][+1] 2 and _{YAB_[(] _[k]_[)] _[}] k≤_[n] _[−]_ 2[3][.][This] defines the radiative obstruction tensor _Oab[I]_[whose][vanishing][determines][whether] _[Q]_ ( _ab_[n][+1] 2[)] = 0 can be satisfied. This behaviour is reminiscent of the Fefferman-Graham obstruction tensor _O[FG]_ in the context of ambient metrics [12, 13]. Recall that for n = 3 the tensor _Oab[I]_[automat-] ically vanishes, just like _O[FG]_ , and that they appear at the same order. This suggests a strong connection between _Oab[I]_[and][the][FG][obstruction][tensor][at][the][cross-sections][of] _[I]_[ .][Establish-] ing this connection would require understanding in detail all the lower order terms arising in (83). This task is challenging and well beyond the scope of this paper, so in this section we just analyze the first non-trivial case, namely n = 5 (i.e. spacetime dimension six), where _Oab[I]_[=] _[ Q]_[(3)] _ab_[.] 

Assume ( _M, g,_ Ω) is a six-dimensional conformal manifold with _λ_ = 0 satisfying _Q_[(1)] _αβ_[=] _[ Q]_[(2)] _αβ_[= 0,] _L_[(1)] _µ_ = _L_[(2)] _µ_ = 0 and _f_[(1)] = _f_[(2)] = _f_[(3)] = _f_[(4)] = 0. By item 1. in Prop. 4.15 we know that the tensor _Q_[(3)] _ab_[satisfies] _[P][ ab][Q]_[(3)] _ab_[=][0][and] _[Q]_[(3)] _ab[n][b]_[=][0.][In][Lemma][6.2][we][have][established][that] under any change of rigging _ξ[′]_ = _z_ ( _ξ_ + _V_ ) (with _z_ and _V_ extended arbitrarily off _I_ ) one has _Q_[(3)] _ab ′_ = _z_ 2 _Q_[(3)] _ab_[.][So, in order to analyze the obstruction tensor at] _[ I]_[it suffices to compute] _[ Q]_[(3)] _ab_[in] a simple gauge. We choose, as in the previous subsection, the gauge in which _σ_[(1)] = 1, _ℓ_[(2)] = 0 and the pullback of _**ℓ**_ to the cross-sections of _I_ vanishes, _**ℓ** ∥_ = 0. More specifically, we shall work in Gaussian null coordinates _{t, u, x[A] }_ in which the metric in a neighbourhood of _I_ = _{t_ = 0 _}_ takes the form _g_ = 2 _dudt_ + _ϕdu_[2] + 2 _βAdx[A] du_ + _µABdx[A] dx[B] ,_ where _ϕ_ and _**β**_ vanish at _t_ = 0 and the rigging is _ξ_ = _∂t_ . Following the same notation as in Appendix D, we have _γab_ = _δa[A][δ] b[B][h][AB]_[,][where] _[h][AB]_[:=] _[µ][AB][|][t]_[=0][,] _[κ]_[(] _[m]_[)][=] _[−]_ 2[1] _[ϕ]_[˙][(] _[m]_[)][,][r][(] _A[m]_[)] =[1] 2 _**[β]**_[˙][(] _[m]_[)][,] Y[(] _AB[m]_[)][=][1] 2 _[µ]_[˙] _AB_[(] _[m]_[)][,] _[P][ ab]_[=] _[ µ][AB][δ] A[a][δ] B[b]_[and] _[n][a]_[=] _[ δ] u[a]_[.][In][particular,][we][use][a][prime][to][denote][derivative] w.r.t. _u_ and a dot for derivative w.r.t. _t_ . 

Computing the quasi-Einstein equation (including all terms) by hand becomes intractable very quickly. Therefore, and since we need the full expression of the quasi-Einstein equation up to order _Q_[(3)] _ab_[,][we][have][performed][the][computation][with][the][aid][of][the] `[xAct]`[package][[][66][]][in] `Mathematica` . The outcome of the computation has the following consequences. Firstly, equations _Q_[(1)] _AB_[=][0,] _[Q]_[˙][(1)] _A_ = 0, _Q_[˙][(1)] _u_ = 0 and _Q_[¨][(1)] = 0 at _I_ imply _h[′] AB_[=][0,][r] _[A]_[=][0,] _[κ][n]_[=][0][and] _σ_[(2)] = 0, while _Q_[(1)] _Au_[=] _[Q]_[(1)] _uu_[=] _[L]_[(1)] _A_ = _L_[(1)] _u_ = 0 hold automatically. Next, equation _f_[(3)] = 0 

35 

fixes _κ_[(2)] = 0, which inserted into _L_[˙][(1)] = 0 gives _£n_  _P[AB]_ Y _AB_  = _−[R]_ 4 _[h]_[.][One][then][checks][that] _µ[AB] Q_[(2)] _AB_[=] _[ Q]_[(2)] _uA_[=] _[ Q] uu_[(2)][= 0][hold][automatically,][and][from] _[Q]_[(2)] _AB_[= 0][one][obtains] 

**==> picture [269 x 14] intentionally omitted <==**

˙ where _L[h] AB_[is][the][Schouten][tensor][of] _[h][AB]_[.] One can also check that _Q_[(2)] _u_ = _L_[(2)] _u_ = 0 hold automatically. Equation _Q_[˙] _A_ = 0 then gives r[(2)] _A_[=] 3[1]  _DB_ Y _[B] A − DA_ Y _[B] B_ , where _D_ is the LeviCivita _Q_ ¨[(2)] = 0,derivative _f_[(4)] = 0ofand _h_ , and _L_ ˙[(2)] _L_ = 0[(2)] _A_ read,[=] _[Q]_[(3)] _Au_ respectively,[=] _[Q]_[(3)] _uu_[=][0][are][automatically][satisfied.][Next,][equations] 

**==> picture [249 x 52] intentionally omitted <==**

Taking a derivative of the first equation w.r.t. _u_ and solving the system one obtains _£nσ_[(3)] = _ϕ_[(3)] = 0 and _£n_ (tr _P_ **Y**[(2)] ) = _−_ 2 _h[AB] h[CD] L[h] AC_[Y] _[BD]_[.][One][can][now][check][that] _[P][ ab][Q]_[(3)] _ab_[=][0][is] automatically verified. Substituting all these expressions into the tensor _Q_[(3)] _AB_[yields] 

**==> picture [434 x 46] intentionally omitted <==**

where _WACBD[h]_[denotes][the][Weyl][tensor][of] _[h][AB]_[.][Observe][that][the][right-hand][side][is][manifestly] traceless. In accordance with the general results in the previous sections, equation _Q_[(3)] _AB_[=][0] does not determine the tensor Y[(2)][a][transport][equation.][Instead,][the][right-hand][side][of] _AB_[via] (127) defines a symmetric, traceless tensor 

**==> picture [435 x 47] intentionally omitted <==**

constructed solely from _hAB_ and Y _AB_ . Taking the derivative of _OAB[I]_[along] _[ ∂][u]_[ and using] _[ ∂][u][h][AB]_[=] 0, (126), and the identity _D_ ( _AD[C] L[h] B_ ) _C_[=] _[h][CD][D][A][D][B][L][h] CD_[(which][follows][at][once][form][the] contracted Bianchi identity, see (33)), one finds 

**==> picture [257 x 21] intentionally omitted <==**

The term between round brackets in the right-hand side is precisely the Bach tensor of _hAB_ (see e.g. [13]), which we denote by _BAB[h]_[.][Summarizing,][we][have][obtained] _[∂][u][Q]_[(3)] _AB_[=][2] _[B] AB[h]_[.][The] Bach tensor is precisely the Fefferman and Graham obstruction tensor in the case of conformal metrics of dimension four. This provides strong support for our expectation that _O[I]_ is closely related to the FG obstruction tensor _O[FG]_ of the corresponding dimension. 

We now give a different argument to show that _∂uQ_[(3)] _AB_[must][be][proportional][to][the][FG][ob-] struction tensor. In the recent work [44] we proved that the Fefferman–Graham ambient metric associated to the conformal class [ _h_ ] admits a null infinity whose _I_ -structure is given precisely by _h_ . Furthermore, we showed that the derivative of _Q_[(3)] _AB_[along] _[∂][u]_[at] _[I]_[is][proportional][to][the] Fefferman–Graham obstruction tensor of [ _h_ ]. Since the derivative _∂uQ_[(3)] _AB_[of][(][127][)][only][depends] on _hAB_ , it must be the same for all spacetimes sharing the same _hAB_ at _I_ . Thus, the only possibility is _∂uQ_[(3)] _AB_[being][proportional][to][the][FG][obstruction][tensor][in][dimension][four,][i.e.][the] 

36 

Bach tensor. 

In summary, the vanishing of the Bach tensor of _hAB_ , together with the condition _OAB[I]_[= 0][on] a cross-section Σ (which by (127) may be interpreted as a restriction on the free data Y _AB|_ Σ), guarantees that the full obstruction tensor _O[I]_ vanishes everywhere on _I_ . Thus, the hypothesis _Oab[I]_[= 0 in Theorem][ 5.5][ for][ n][ = 5 can be relaxed to] _[ B] AB[h]_[= 0 and] _[ O] AB[I][|]_[Σ][= 0.][Note that the FG] obstruction tensor is conformally covariant, and hence the condition _BAB[h]_[= 0][does][not][depend] on the conformal representative of the _I_ -structure. 

Our recent results in [44] concerning a geometric characterization of conformal infinity for the Fefferman–Graham ambient metric, together with preliminary analysis of the general case, suggest that a similar picture emerges in higher dimensions, namely that the FG obstruction tensor arises after taking a sufficient number of derivatives along _n_ on the radiative obstruction tensor. We therefore expect the following conjecture to be true. 

**Conjecture 6.3.** _Let {I ,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _, σ,_ q _} be I -structure data of odd dimension_ n _≥_ 7 _admitting a cross-section ι_ : Σ _→ I with induced metric h_ := _ι[⋆]_ _**γ** and let Oab[I][be][the][radiative][obstruction] tensor. Denote by O[FG] the Fefferman-Graham obstruction tensor of_ [ _h_ ] _. Then,_ 

**==> picture [119 x 19] intentionally omitted <==**

_where c_ n _is a constant depending only on_ n _._ 

Note that the Fefferman-Graham obstruction tensor vanishes e.g. when _h_ is Einstein or conformally flat, among others [13]. Establishing this conjecture would require a detailed analysis of the lower order terms appearing in (83). We intend to analyze this problem in future work. 

## **7 Conclusions and future work** 

In this paper we have analyzed how the conformal Einstein equations constrain the geometry at null infinity without imposing any restriction on the spacetime dimension, fall-off conditions for the Weyl tensor or the topology of _I_ beyond admitting a cross-section. Our analysis leads to the identification of a collection of free tensors on _I_ that completely characterize asymptotically flat spacetimes within this framework. Moreover, we proved that, provided the obstruction tensors vanish, any such choice of free data gives rise to a smooth asymptotically flat spacetime. 

There are several natural directions for future research. First, it would be important to clarify the physical interpretation of the free tensors m and _**β**_ appearing in Theorem 5.5, and to relate them to the notions of Bondi mass and angular momentum in higher dimensions as developed in [29, 32, 60, 25, 30]. Addressing this question within our framework will require an appropriate conformally covariant definition of these quantities, as well as suitable higher-dimensional generalizations of the news tensor and Geroch’s _ρ_ -tensor. Second, we plan to investigate further the radiative obstruction tensor in arbitrary dimension and conformal gauge and its relation to the Fefferman–Graham obstruction tensor, as conjectured in Conjecture 6.3. In this context, it would be particularly interesting to connect our results with those of [57] and similar references, where logarithmic terms in the asymptotic expansions at infinity are allowed. 

Further open problems include extending the notion of double null data introduced in [43, 42] to the asymptotic characteristic problem, incorporating the new free data identified in this work. It would be interesting to determine whether this detached object suffices to construct a conformal spacetime satisfying Einstein’s equations in a neighbourhood of _I_ , once suitable existence theorems for the conformal equations are available, either in higher dimensions or in four dimensions with non-spherical topology. Finally, another promising direction is the inclusion of Killing and homothetic initial data, making use of the general identities developed in [45], and the study of the corresponding asymptotic KID problem in this setting (see [52]). 

37 

## **Acknowledgements** 

This work has been supported by Grant PID2024-158938NB-I00 funded by MICIU/AEI/10.13039/ 501100011033 and by “ERDF A way of making Europe”. M. Mars acknowledges financial support under projects SA097P24 (JCyL) and RED2022-134301-T funded by MCIN/AEI/10.13039/ 501100011033. G. S´anchez-P´erez also acknowledges support of the PhD. grant FPU20/03751 from Spanish Ministerio de Universidades. 

## **A Some pullbacks into a null hypersurface** 

In this appendix we particularize several results from [46, 47, 45] to the null case and we prove additional pullback identities concerning the Hessian of a function (Prop. A.4). Given a (0 _, p_ ) tensor field _Tα_ 1 _···αp_ on _M_ , we use the notation _Ta_ 1 _···ap_ to denote its pullback to _H_ , and[(] _[i,j]_[)] _Tα_ 1 _···αp−_ 1 for its contraction first in the _j_ -th slot and then in the _i_ -th slot, i.e.[(] _[i,j]_[)] _T_ =[(] _[i]_[)][][(] _[j]_[)] _T_  (note that the order ( _i, j_ ) is relevant). Similarly,[(] _[i]_[)] _Ta_ 1 _···ap−_ 1 denotes the pullback of[(] _[i]_[)] _Tα_ 1 _···αp−_ 1 to _H_ . The rest of the quantities are defined in Section 2. 

**Proposition A.1.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold and_ Φ : _H →M a smooth embedded null hypersurface with rigging ξ. Let T be a_ (0 _, p_ ) _-tensor on M and f ∈F_ ( _M_ ) _. Then, for any j ≥_ 1 

**==> picture [456 x 192] intentionally omitted <==**

**Proposition A.2.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold and_ Φ : _H →M a smooth null hypersurface with rigging ξ. Let T be a_ (0 _, p_ + 1) _-tensor on M and denote by_ div _T the p-covariant tensor defined by_ (div _T_ ) _α_ 1 _···αp_ := _g[µν] ∇µTνα_ 1 _···αp. Then,_ 

**==> picture [460 x 147] intentionally omitted <==**

38 

**Proposition A.3.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold,_ Φ : _H →M a smooth embedded null hypersurface with geodesic rigging ξ and let T be a_ (0 _, p_ ) _-tensor on M. Then,_ 

**==> picture [428 x 150] intentionally omitted <==**

**Proposition A.4.** _Let_ ( _M, g_ ) _be a semi-Riemannian manifold and_ Φ : _H →M a smooth null hypersurface with geodesic rigging ξ. Let f be function on M. Then,_ 

**==> picture [362 x 57] intentionally omitted <==**

_As a consequence,_ 

_◦_ □ _gf_ = _[H]_ □ _P f_ +  tr _P_ **Y** _− n_ ( _ℓ_[(2)] ) _£nf_ +(tr _P_ **U** + 2 _κn_ ) _£ξf_ +2 _£n_  _£ξf_  _−_ 2 _P[ab]_ (r+s) _a∇bf,_ (138) _[◦] ◦ where_ □ _P_ := _P[ab] ∇a∇b._ 

_Proof._ Identity (135) was already proven in [45]. To prove the second one we contract _∇α∇βf_ with _e[α] a[ξ][β]_[and][use][(][26][),] 

**==> picture [388 x 15] intentionally omitted <==**

Expression (137) is immediate because _ξ[α] ξ[β] ∇α∇βf_ = _∇ξ∇ξf −∇∇ξξf_ = _£_[(2)] _ξ[f][−][£][a] ξ[f]_[.][Fi-] nally, identity (138) follows from (see (14)) _g[αβ] ∇α∇βf_ = _P[ab] e[α] a[e][β] b[∇][α][∇][β][f]_[+ 2] _[ξ][α][ν][β][∇][α][∇][β][f]_[after] inserting (135)-(136) and using (11). 

## **B Auxiliary computations and proof of** (61) 

In this appendix we compute several contractions of the tensors Σ[][(] _[m]_[)] and Σ[(] _[m]_[)] that will be used both to prove (61) and in Appendix C below. Let us begin by recalling the following expressions computed in [46, Prop. 4.21], 

**==> picture [438 x 49] intentionally omitted <==**

The next expressions also proved in [46] (formulas (65), (67) and (68)) and valid for _m ≥_ 1 will be also needed 

39 

**==> picture [442 x 48] intentionally omitted <==**

Note that these three identities become exact for _m_ = 1. Later in this appendix we will also need several contractions of _ξ[β]_[ ] Σ[(] _µαβ[m]_[)][that][we][compute][next.][First][observe][that][the][contraction] of (144) with _ξ[β]_ can be written as 

**==> picture [372 x 23] intentionally omitted <==**

We now use the two identities (53) and get (the notation introduced in Appendix A also applies here) 

**==> picture [445 x 161] intentionally omitted <==**

Taking trace in (142) in the indices _µ, α_ and using (144) one gets 

**==> picture [339 x 23] intentionally omitted <==**

Finally, the _m −_ 1 Lie derivative of the Ricci tensor is [46, Eq. (63)], for _m ≥_ 2, 

**==> picture [336 x 19] intentionally omitted <==**

**Proposition B.1.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} be null metric hypersurface data_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and extend ξ off_ Φ( _H_ ) _by ∇ξξ_ = 0 _. Then, for any m ≥_ 2 _,_ 

**==> picture [426 x 109] intentionally omitted <==**

_As a consequence,_ 

**==> picture [389 x 72] intentionally omitted <==**

40 

_Proof._ Identity (150) will be a consequence of (139) and (142). The pullback of the second is, ( _m_ ) after taking into account (53), (140) and Σ[][(] _cab[m][−]_[1)] = 0 (by (139)), 

**==> picture [156 x 18] intentionally omitted <==**

Replacing here Σ[][(] _cab[m]_[)][from][(][139][)][yields][(][150][).][The][contraction][of][(][150][)][with] _[n][c]_[gives][(][155][)][after] using 

**==> picture [267 x 19] intentionally omitted <==**

To show (151) we simply contract (148) with _e[β] a_[and use (][54][) (recall that a tangential derivative] of _K_[(] _[m][−]_[1)] is at most of transverse order _m −_ 1). 

The remaining identities will rely on (145)-(147). Before applying them we need to determine the terms of the form ([(] _[i]_[)] _∇K_[(] _[m]_[)] ) _ab_ and ([(] _[i,j]_[)] _∇K_[(] _[m]_[)] ) _a_ for various values of _i, j_ . For the former we use (130)-(131), and for the latter (132)-(134). Taking also into account (52) the result is 

**==> picture [397 x 43] intentionally omitted <==**

Note that these expressions immediately imply 

**==> picture [353 x 43] intentionally omitted <==**

With all these expressions at hand, identities (146) and (147) become, respectively, 

**==> picture [213 x 18] intentionally omitted <==**

**==> picture [432 x 77] intentionally omitted <==**

which is (153). A contraction with _n[c]_ gives (156). Now, identity (154) is a consequence of replacing (152), (153) and (53) into (142), namely 

**==> picture [457 x 75] intentionally omitted <==**

Finally, (157) is its contraction with _n[c]_ . 

We already have all the necessary ingredients to compute _R_[˙][(] _a[m]_[)] up to order _m_ . 

**Proposition B.2.** _Let H be a null hypersurface_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and extend ξ off_ Φ( _H_ ) _by ∇ξξ_ = 0 _. Then for any m ≥_ 2 _,_ 

**==> picture [442 x 42] intentionally omitted <==**

41 

_and consequently_ 

**==> picture [437 x 48] intentionally omitted <==**

_Proof._ From (149), 

**==> picture [442 x 42] intentionally omitted <==**

We evaluate each term separately. For the first we apply Prop. A.2 to _T_ =[(3)] Σ[(] _[m][−]_[1)] and take into account (3)Σ( _m−_ 1) _ab_ (= _m_ ) Y[(] _ab[m]_[)] (by (140) and (143)) and[(2] _[,]_[3)] Σ[(] _[m][−]_[1)][(] = _[m]_[)] (1 _,_ 3)Σ( _m−_ 1)[(] = _[m]_[)] 0 (by (152) and (143)). Thus, 

**==> picture [434 x 36] intentionally omitted <==**

Only the first term needs further analysis. Note that 

**==> picture [452 x 24] intentionally omitted <==**

so 

**==> picture [390 x 20] intentionally omitted <==**

The first term in the right hand side is directly given by (156), and for the second one we use 

**==> picture [385 x 56] intentionally omitted <==**

where in the second line we also used (152). Replacing this and (156) into (164) gives 

**==> picture [410 x 23] intentionally omitted <==**

and hence (163) takes the form 

**==> picture [443 x 49] intentionally omitted <==**

( _m_ ) For the second term of (162) we insert (27) and use that _e[α] a[ξ][µ][ξ][β]_[Σ][(] _µαβ[m][−]_[1)] = 0 (by (152)) and ( _m_ ) _e[µ] c[e][α] a[e][β] b_[Σ][(] _µαβ[m][−]_[1)] = 0 (by (139)), obtaining 

**==> picture [399 x 48] intentionally omitted <==**

42 

where in the second equality we also inserted (11). Finally, the last term in (162) is 

**==> picture [379 x 56] intentionally omitted <==**

where in the last step we used (26) for _e[α] a[∇][α][ξ][β]_[and][recalled][(][151][)][and][(][141][).][Equation][(][160][)][is] now obtained by simply inserting (165)-(167) into (162). To prove (161) it suffices to contract (160) with _n[a]_ and use (24) and (11). 

We conclude the appendix with the explicit expressions for Σ _cab_ , ([(3)] Σ) _ca_ and ([(2] _[,]_[3)] Σ) _c_ . Although they are a particular case of more general identities derived in [45], we re-derive them for completeness and to avoid the need of introducing additional notation to connect with the results in [46]. We emphasize that this result is not contained in Proposition B.1 because, as usual, the lowest values of _m_ require a different treatment. 

**Proposition B.3.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} be null metric hypersurface data_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and extend ξ off_ Φ( _H_ ) _by ∇ξξ_ = 0 _. Then,_ 

**==> picture [352 x 49] intentionally omitted <==**

**==> picture [354 x 14] intentionally omitted <==**

_As a consequence,_ 

**==> picture [363 x 66] intentionally omitted <==**

_Proof._ From (144) for _m_ = 1 (recall that the equality is exact) 

**==> picture [177 x 23] intentionally omitted <==**

Pulling this back onto _H_ and using (129) with _T_ = _K_ , 

**==> picture [248 x 24] intentionally omitted <==**

Identity (168) follows after inserting _Kab_ = 2Y _ab_ and ([(1)] _K_ ) _c_ =[1] _∇◦ cℓ_ (2) (see (52)). The contrac2 tion with _n[c]_ given in (171) is obtained from this after using _n[c] ∇[◦] c_ Y _ab_ = _£n_ Y _ab −_ 2Y _c_ ( _a∇◦ b_ ) _nc_ and (24). To prove the second and third identities we repeat the same strategy as in Prop. B.1. First we compute the terms of the form[(] _[i]_[)] _∇K_ and[(] _[i,j]_[)] _∇K_ that appear in (145)-(146) for _m_ = 1 (which recall are exact in this case). To do this we use (130)-(132), (134) and recall _Kab_[(] _[m]_[)] = 2Y[(] _ab[m]_[)] as well as (52), 

**==> picture [460 x 49] intentionally omitted <==**

Expressions (169) and (170) are obtained by replacing this into (145)-(146) respectively, and noting that _∇K_[(0)] = _∇g_ = 0. Finally, (172) and (173) are the contraction of (169)-(170) with _n[c]_ . 

43 

## **C Quasi-Einstein equations at null infinity** 

In this appendix we write down explicitly the tensors (81)-(82) for every _m ≥_ 1 making the leading order terms explicit. The definition (32) of the Schouten tensor in terms of the Ricci yields, after recalling (56), 

**==> picture [374 x 33] intentionally omitted <==**

From Remark 4.4 one has 

**==> picture [453 x 119] intentionally omitted <==**

and 

In the following proposition we compute the contractions of _L_[(] _αβ[m]_[)][that will be needed below.][No-] tice that some contractions are computed up to order _m_ , and some others just to order _m_ + 1, depending on our needs for the rest of the appendix. 

**Proposition C.1.** _Let {H,_ _**γ** ,_ _**ℓ** , ℓ_[(2)] _} be null metric hypersurface data_ (Φ _, ξ_ ) _-embedded in_ ( _M, g_ ) _and extend ξ off_ Φ( _H_ ) _by ∇ξξ_ = 0 _. Let Lαβ be the Schouten tensor, L_[(] _αβ[m]_[)][=] _[£]_[(] _ξ[m][−]_[1)] _Lαβ and m ≥_ 2 _. Then,_ 

**==> picture [448 x 245] intentionally omitted <==**

44 

_In particular,_ 

**==> picture [451 x 206] intentionally omitted <==**

_and_ 

_Proof._ The contraction of (176) with _e[α] a[e][β] b_[gives][(][179][)][after][replacing][(][62][),][(][74][)][and][(][75][)][and] recalling that _Kab_ = 2Y _ab_ . Similarly, (180) is obtained by contracting (176) with _e[α] a[ξ][β]_[and using] (61), (74)-(75) and ([(1)] _K_ ) _a_ =[1] 2 _∇◦ aℓ_ (2) (cf. (52)). To prove (181) we simply contract (177) with _ξ_ twice and insert (60) and (74). Relations (182) and (183) are respectively the contractions of (179) and (180) with _n_ . They are obtained after using _γabn[b]_ = U _abn[b]_ = 0, s _bn[b]_ = 0 and _ℓan[a]_ = 1 together with the definitions of _κn_ , r _a_ , _κ_[(] _[m]_[)] and r[(] _a[m]_[)] . In addition, (182) uses identity (28) applied to _ωa_ = r _a_ , and (183) employs (24) and (11). Finally, relations (184)-(187) are immediate from the previous ones by simply keeping the quantities of order _m_ + 1. 

The tensors _L_[(1)] _ab_[,] _[L]_[˙][(1)] _a_ and _L_[¨][(1)] require a separate analysis. The starting point is (174) with _m_ = 1 (this is an exact relation), which we contract with _e[α] a[e][β] b_[,] _[e][α] a[ξ][β]_[and] _[ξ][α][ξ][β]_[.][Taking][into] account (66), (67) and (68) (we do not replace _R_ from (73) since this will not be needed) and recalling _gαβe[α] a[e][β] b_[=] _[ γ][ab]_[,] _[g][αβ][e][α] a[ξ][β]_[=] _[ ℓ][a]_[and] _[g][αβ][ξ][α][ξ][β]_[=] _[ ℓ]_[(2)][,][the][result][is] 

**==> picture [449 x 158] intentionally omitted <==**

Using these identities we can now compute _L_[(] _a[m]_[+1)] and _L_[˙][(] _[m]_[+1)] up to order _m_ + 1. Taking _m_ transverse derivatives of _Lα_ := (n _−_ 1) _Lαβ∇[β]_ Ωand using (56), 

**==> picture [392 x 72] intentionally omitted <==**

45 

[ _k_ +2] so (recall _L_[(] _αβ[k]_[)] = 0, by (178)) 

**==> picture [368 x 22] intentionally omitted <==**

Now we note that _g[βµ] ∇µ_ Ω = _[I] σ_[(1)] _ν[β]_ (by (14)) and 

**==> picture [406 x 93] intentionally omitted <==**

Hence, 

**==> picture [438 x 71] intentionally omitted <==**

**Proposition C.2.** _Let L_[(] _a[m]_[+1)] _and L_[˙][(] _[m]_[+1)] _be defined as in_ (82) _. Then,_ 

**==> picture [454 x 124] intentionally omitted <==**

_and for every m ≥_ 1 _,_ 

**==> picture [454 x 86] intentionally omitted <==**

˙ _where RL_[(] _[m]_[)] _is an explicit tensor that depends linearly on_ **r**[(] _[m]_[+1)] _as well as on lower order transverse derivatives and that we do not write for simplicity (it can be easily read out by making explicit all the calculations in the proof)._ 

**==> picture [357 x 55] intentionally omitted <==**

46 

The contraction with _ξ[α]_ yields (193) after replacing (69) and (73), and that with _e[α] a_[gives,][after] inserting (70), (194). To obtain (195) we contract (192) with _e[α] a_[and][use] _[L]_[(] _ab[m]_[)] _[n][b]_[(] _[m]_ =[+1)] 0 (by (184)), 

**==> picture [438 x 24] intentionally omitted <==**

This becomes (195) after inserting (182), (185) and (187). In order to prove (196) we contract (192) with _ξ[α]_ , 

**==> picture [435 x 54] intentionally omitted <==**

Inserting (183), (181), (185) and (186) and using _P[bc] ℓb_ = _−ℓ_[(2)] _n[c]_ , (196) is established. 

Next we compute the tensors _Q_[(] _ab[m]_[)][,] _[Q]_[˙][(] _a[m]_[)] and _Q_[¨][(] _[m]_[)] to the leading order. To do that, we apply _£_[(] _ξ[m]_[)] to (77) and use Proposition 4.1, 

**==> picture [456 x 46] intentionally omitted <==**

To perform the calculation it is convenient to introduce the following symmetric tensors (recall that Σ _[σ] βα_ is symmetric in _α, β_ , so the same holds for Σ[(] _[k]_[)] _[σ] βα_ ) 

**==> picture [363 x 33] intentionally omitted <==**

**==> picture [184 x 32] intentionally omitted <==**

Given that Σ[(] _[k]_[)] involves at most _m_ + 1 derivatives of _g_ and that Ω= 0, _∇µ_ Ω = _[I] σ_[(1)] _νµ_ at _I_ , we can write 

**==> picture [442 x 49] intentionally omitted <==**

Similarly, _L_[(] _[m]_[)] involves at most _m_ + 1 derivatives of _g_ , so 

**==> picture [376 x 29] intentionally omitted <==**

**==> picture [376 x 20] intentionally omitted <==**

Using this and the formulas in Propositions A.4, B.1 and C.1, the computation of _Q_[(] _ab[m]_[)][,] _[Q]_[˙][(] _a[m]_[)] and _Q_[¨][(] _[m]_[)] will be straightforward. Observe again that _Q_[¨][(] _[m]_[)] is computed to one order less, since this is all that will be needed. 

47 

**==> picture [455 x 233] intentionally omitted <==**

_where O_[] _ab_[(] _[m]_[)] _and O_[] _a_[(] _[m]_[)] _are tensors that depend on_ **r**[(] _[m]_[)] _, σ_[(] _[m]_[)] _and lower order terms and we do not write for simplicity (they can be easily read out by performing all the calculations in the proof explicitly)._ 

_Proof._ To prove each identity in (202)-(204) we contract the three pieces I[(] _αβ[m]_[+1)] , II[(] _αβ[m]_[+1)] and III[(] _αβ[m]_[+1)] with _e[α] a[e][β] b_[,] _[ e] a[α][ξ][β]_[and] _[ ξ][α][ξ][β]_[.][The contraction of I][(] _αβ[m]_[+1)] with _e[α] a[e][β] b_[gives, after using identity] (135), 

**==> picture [233 x 16] intentionally omitted <==**

( _m_ ) Contracting (198) with _e[α] a[e][β] b_[,][inserting][(][14][)][and][recalling][Σ][(] _cab[m][−]_[1)] = 0 (by (139)) gives 

**==> picture [405 x 65] intentionally omitted <==**

Inserting (155), (140) and taking into account (143), 

Finally, the contraction of (200) with _e[α] a[e][β] b_[is][(recall][Ω][= 0)] _[I]_ 

**==> picture [455 x 65] intentionally omitted <==**

To prove (203) we repeat the same steps. Firstly, we contract I[(] _αβ[m]_[+1)] with _e[α] a[ξ][β]_[and][use][(][136][)] to get 

**==> picture [359 x 17] intentionally omitted <==**

**==> picture [455 x 99] intentionally omitted <==**

48 

where in the second line we used (154) and (157). To compute _e[α] a[ξ][β]_[III][(] _αβ[m]_[+1)] we contract (200) with _e[α] a[ξ][β]_[,] 

**==> picture [247 x 26] intentionally omitted <==**

The explicit forms of _L_[˙][(] _a[m]_[)] and _L_[˙][(] _a[m][−]_[1)] are given in (180) and (185). Using as before _Q_[˙][(] _a[m]_[)] = (n _−_ 1) _e[α] a[ξ][β]_[] I[(] _αβ[m]_[)][+ II][(] _αβ[m]_[)][+ III][(] _αβ[m]_[)]  we find (203) after adding the three terms and simplifying. The proof of (204) is analogous. Contracting I[(] _αβ[m]_[+1)] with _ξ[α] ξ[β]_ and using (137) gives 

**==> picture [102 x 17] intentionally omitted <==**

The corresponding term with II[(] _αβ[m]_[+1)] vanishes because the contraction of (199) with _ξ[α] ξ[β]_ is 

**==> picture [219 x 20] intentionally omitted <==**

where in the last equality we used (143) and (152). Finally, the term with III[(] _αβ[m]_[+1)] is obtained by contracting (201) with _ξ[α] ξ[β]_ and inserting (181), which gives 

**==> picture [353 x 34] intentionally omitted <==**

The expression _Q_[¨][(] _[m]_[)] = (n _−_ 1) _ξ[α] ξ[β]_[] I[(] _αβ[m]_[)][+ II][(] _αβ[m]_[)][+ III][(] _αβ[m]_[)]  yields (204) at once. 

As in other cases, the lowest orders _Q_[(1)] and _Q_[(2)] require a specific treatment (note that they are excluded from Proposition C.3 by the condition _m ≥_ 2). To obtain the former we simply contract _Qαβ_ = ( _I_ n _−_ 1) _∇α∇β_ Ωwith _eαa[e][β] b_[,] _[e][α] a[ξ][β]_[and] _[ξ][α][ξ][β]_[and][use][(][135][)-(][137][),] 

**==> picture [384 x 16] intentionally omitted <==**

To compute the latter we evaluate the exact expression (197) with _m_ = 1 and use _∇σ_ Ω = _[I] σ_[(1)] _νσ_ to get 

**==> picture [232 x 24] intentionally omitted <==**

The contraction of this expression with _e[α] a[e][β] b_[,] _[e][α] a[ξ][β]_[and] _[ξ][α][ξ][β]_[can][be][evaluated][from][(][135][)-(][137][),] (171)-(173) and (188)-(190). The result is 

**==> picture [468 x 181] intentionally omitted <==**

49 

where _R_ is given by (73) and needs not be written out explicitly. 

We conclude this appendix by computing the scalars _f_[(] _[m]_[+1)] , obtained after applying _£_[(] _ξ[m]_[)] to _f_ = _g[αβ] ∇α_ Ω _∇β_ Ωand using (56), 

**==> picture [395 x 35] intentionally omitted <==**

Again, the lowest orders _f_[(1)] , _f_[(2)] and _f_[(3)] need a separate treatment. Obviously _f_[(1)] = 0 because _I_ is null. To compute _f_[(2)] we particularize (210) to _m_ = 1 so that 

**==> picture [201 x 15] intentionally omitted <==**

The first term is ( _£ξg[αβ]_ ) _∇α_ Ω _∇β_ Ω= 2( _σ_[(1)] )[2] _κn_ (by (214) and Ω = _[I]_ 0) and the second term is 2 _σ_[(1)] _£nσ_[(1)] because _∇[α]_ Ω = _[I] σ_[(1)] _ν[α]_ . Thus, 

**==> picture [300 x 15] intentionally omitted <==**

We now compute _f_[(3)] . The expanded form of (210) for _m_ = 2 is 

_f_[(3)] = 2 _∇[α]_ Ω _∇α_ ( _£_[(2)] _ξ_[Ω)+2] _[g][αβ][∇][α]_[(] _[£][ξ]_[Ω)] _[∇][β]_[(] _[£][ξ]_[Ω)+4(] _[£][ξ][g][αβ]_[)] _[∇][α]_[(] _[£][ξ]_[Ω)] _[∇][β]_[Ω+(] _[£]_[(2)] _ξ[g][αβ]_[)] _[∇][α]_[Ω] _[∇][β]_[Ω] _[.]_ 

Now, using _∇[α]_ Ω = _[I] σ_[(1)] _ν[α]_ , together with (214) and 

**==> picture [315 x 72] intentionally omitted <==**

it follows that 

**==> picture [404 x 35] intentionally omitted <==**

We now deal with the rest of the cases in the following proposition. 

**Proposition C.4.** _Let f_ := _g[αβ] ∇α_ Ω _∇β_ Ω _. Then, for any m ≥_ 2 _,_ 

**==> picture [386 x 18] intentionally omitted <==**

_Proof._ The case _m_ = 2 is (212), which after ignoring terms of order one and zero becomes (213). For _m ≥_ 3, the only terms in (210) that have a chance to depend on **Y**[(] _[m]_[)] or _σ_[(] _[m]_[)] are _k_ = 0 (and _j_ = 0 _,_ 1 _, m −_ 1 _, m_ ), _k_ = 1 (and _j_ = 0 _, m −_ 1) and _k_ = _m_ , namely 

**==> picture [444 x 40] intentionally omitted <==**

where we used the fact that _m ≥_ 3 because we have used that the terms with _k_ = 0 and _j_ = 0 _,_ 1 _, m −_ 1 _, m_ are all different. When _m_ = 2 we would be overcounting (but it turns out that 

50 

the extra factor compensates, so (213) is valid also for _m_ = 2). Now one uses _∇[β]_ Ω = _[I] σ_[(1)] _ν[β]_ in ( _m_ ) the first term, _∇[α]_[] _£_[(] _ξ[m][−]_[1)] Ω = _σ_[(] _[m]_[)] _ν[α]_ in the second, and in the third and fourth 

**==> picture [442 x 50] intentionally omitted <==**

After adding up the four terms one gets 

> [(] _[m]_[)] _f_[(] _[m]_[+1)] = 2 _σ_[(1)] _£nσ_[(] _[m]_[)] + 2 _m_ ( _£nσ_[(1)] ) _σ_[(] _[m]_[)] + 4 _mσ_[(1)] _κnσ_[(] _[m]_[)] + 2( _σ_[(1)] )[2] _κ_[(] _[m]_[)] _,_ which is (213) for _m ≥_ 3. 

## **D Higher order Raychaudhuri equation** 

In this appendix we compute the contraction _L_[(] _a[m]_[+1)] _n[a]_ to one order less, i.e. up to order _m_ . This computation requires knowing _R_[(] _ab[m]_[+1)] _n[a] n[b]_ up to order _m_ and turns out to be quite laborious using the general formalism of hypersurface data. To keep the computations to a reasonable length we have decided to perform the computation using a particular gauge and assuming that the hypersurface is totally geodesic and admits a foliation by cross-sections. The result presented here will be sufficient for the purposes of this paper. 

**Proposition D.1.** _Let H be a null hypersurface embedded in_ ( _M, g_ ) _and assume the existence of a foliation {Su}u∈_ R _of H by cross-sections. Let ξ be the (uniquely defined) rigging satisfying (i) g_ ( _ξ, ξ_ ) = 0 _[H] and (ii)_ Φ _[⋆]_ _**ξ**_ = _du. Suppose in addition that £n_ _**γ**_ = 0 _. Then,_ 

**==> picture [385 x 37] intentionally omitted <==**

_where OR is a scalar that depends on_ **r**[(] _[m]_[)] _and lower order terms._ 

_Proof._ We construct Gaussian null coordinates [49] _{t, u, x[A] }_ from _H_ = _{t_ = 0 _}_ in which the metric takes the form 

**==> picture [221 x 13] intentionally omitted <==**

where _ϕ_ , _**β**_ and _µ_ are, respectively, a function, a one-form and a 2-covariant, symmetric tensor satisfying _ϕ_ ( _t_ = 0) = 0, _**β**_ ( _t_ = 0) = 0 and _µAB_ ( _t_ = 0) = _γAB_ . In these coordinates, the rigging is _ξ_ = _∂t_ and _ν_ = _∂u_ . Denoting the derivative w.r.t. _t_ at _t_ = 0 with a dot, it is easy to check that, at _t_ = 0, _κn_ = _−_ 2[1] _[ϕ]_[˙][,][r] _[A]_[=] 2[1] _**[β]**_[˙][and][Y] _[AB]_[=][1] 2 _[µ]_[˙] _[AB]_[.][If][we][denote][by] _[f]_[˙][(] _[m]_[)][the] _[m]_[-th] _[t]_[-derivative] at _t_ = 0, one also cheeks easily that _κ_[(] _[m]_[)] = _−_[1] 2 _[ϕ]_[˙][(] _[m]_[)][,][r][(] _A[m]_[)] =[1] 2 _**[β]**_[˙][(] _[m]_[)][and][Y][(] _AB[m]_[)][=][1] 2 _[µ]_[˙] _AB_[(] _[m]_[)][.][We][also] note that _P[ab]_ = _µ[AB] δA[a][δ] B[b]_[and] _[n][a]_[=] _[ δ] u[a]_[.][In][these][coordinates,][the][(] _[u, u]_[)][component][of][the][Ricci] tensor is given by [49] 

**==> picture [432 x 101] intentionally omitted <==**

51 

where the prime means derivative w.r.t. _u_ and _D_ is the Levi-Civita connection of the induced metric in the codimension-two surfaces _u_ = _const._ , _t_ = _const._ . Obviously this connection depends on _u_ and _t_ (we do not reflect this dependence for notational simplicity). Note however that at _t_ = 0, the connection is independent of _u_ because _γAB_ does not depend on _u_ (because of _£nγ_ = 0). So, when an expression is evaluated at _t_ = 0 (e.g. all expressions with an ( _m_ ) on top of the equal sign), _D_ will mean the covariant derivative associated to the metric _γAB_ . The strategy now is to take˙ ˙ ˙ _m_ derivatives along _t_ and keep only the terms depending on _ϕ_[˙][(] _[m]_[+1)] , _**β**_[(] _[m]_[+1)] , _µ_[(] _[m]_[+1)] and _µ_[(] _[m]_[)] . This requires commuting _∂t_ with _D_ using a formula analogous to (57), 

**==> picture [453 x 77] intentionally omitted <==**

where Ξ _[A] BC_ = _D_ ( _B_ ˙ _µC_ ) _[A] −_[1][Then,][Ξ][(] _[k]_[)] _[ABC]_[will][depend][on] _[µ]_[˙][(] _[j]_[)][with] _[j]_[=][1] _[, ..., k]_[.] 2 _[D][A]_[ ˙] _[µ][BC]_[.] Consequently, for any tensor field _T_ satisfying _T |t_ =0 = 0, the previous identity implies 

**==> picture [231 x 18] intentionally omitted <==**

This is the case, in particular, of _DAϕ_ , _βA_ , _βA[′]_[,] _[µ][′] AB_[and] _[µ][′′] AB_[.][Using][this][rule][and][that] _[µ][′] AB_[(] _[t]_[ =] 0) = _βA_ ( _t_ = 0) = _ϕ_ ( _t_ = 0) = 0, the _m_ -th _t_ -derivative of _Ruu_ at _t_ = 0 is 

**==> picture [405 x 40] intentionally omitted <==**

˙ which is (215) after replacing _ϕ_[˙] = _−_ 2 _κn_ , _ϕ_[˙][(] _[m]_[+1)] = _−_ 2 _κ_[(] _[m]_[+1)] , _µ_[(] _AB[m]_[)][=][2Y][(] _AB[m]_[)][and][taking][into] account _γAB[′]_[= 0.] 

We now use the previous proposition to compute _L_[(] _a[m]_[+1)] _n[a]_ up to order _m_ under the same assumptions on _I_ and the rigging. 

**Proposition D.2.** _Assume I admits a foliation of cross-sections {Su}u∈_ R _and let ξ be the rigging satisfying g_ ( _ξ, ξ_ ) = 0 _[I] and_ Φ _[⋆]_ _**ξ**_ = _du. Suppose in addition that £n_ _**γ**_ = 0 _. Then,_ 

_L_[(] _a[m]_[+1)] _n[a]_[(] = _[m]_[)] _H_ 1 _κ_[(] _[m]_[+1)] _− σ_[(1)] _£_[(2)] _n_  tr _P_ **Y**[(] _[m]_[)][] + _H_ 2 _£n_  tr _P_ **Y**[(] _[m]_[)][] + _H_ 3 tr _P_ **Y**[(] _[m]_[)] + _OL,_ (216) 

_where OL is a scalar that depends on_ **r**[(] _[m]_[)] _and lower order terms and whose explicit form is not relevant for this paper, and_ 

**==> picture [347 x 54] intentionally omitted <==**

_Proof._ We begin by computing _L_[(] _α[m]_[+1)] to order [ _m_ ]. From (191) and Proposition C.1, the only terms that could depend on **Y**[(] _[m]_[)] are _i_ = _m_ , _i_ = _m −_ 1 ( _j_ = 0 _,_ 1) and _i_ = _m −_ 2 ( _j_ = 0 _,_ 1 _,_ 2), namely 

**==> picture [433 x 71] intentionally omitted <==**

52 

Contracting with _ν[α]_ , evaluating at _I_ and using as usual _∇[β]_ Ω = _[I] σ_[(1)] _ν[β]_ we get 

**==> picture [451 x 51] intentionally omitted <==**

It is easier to split the computation into three pieces, namely I = (n _−_ 1) _σ_[(1)] _L_[(] _αβ[m]_[+1)] _ν[α] ν[β]_ , II = (n _−_ 1) _mν[α] L_[(] _αβ[m]_[)]  _g[βµ] ∇µ£ξ_ Ω+ ( _£ξg[βµ]_ ) _∇µ_ Ω and 

**==> picture [402 x 24] intentionally omitted <==**

and compute each term separately. Those involving only **r**[(] _[m]_[)] or _κ_[(] _[m]_[)] are not needed in explicit form. We shall gather all of them into the tensor _OL_ in the statement of the proposition. For the calculation we shall write _· · ·_ to mean additional terms of this form. For the first term I we contract (175) (with _m_ + 1 instead of _m_ ) with _ν[α] ν[β]_ and use _Kαβν[α] ν[β]_ = _−_ 2 _κn_ and _K_[(2)][=] _[ −]_[2] _[κ]_[(2)][to][get] _αβ[ν][α][ν][β]_ 

**==> picture [320 x 28] intentionally omitted <==**

Inserting (215) as well as 

**==> picture [386 x 17] intentionally omitted <==**

we arrive at 

**==> picture [389 x 56] intentionally omitted <==**

To compute II we now use that (cf. (182)-(183)) 

**==> picture [442 x 60] intentionally omitted <==**

Inserting these into the definition of II and using (14) and (214) gives 

**==> picture [465 x 72] intentionally omitted <==**

Finally, it is clear from (217)-(218) that III = _· · ·_ . To show (216) we only need to add _L_[(] _a[m]_[+1)] _n[a]_[(] = _[m]_[)] I + II + III and simplify. 

53 

## **References** 

- [1] Andersson, L., and Chru´sciel, P. T. On “hyperboloidal” Cauchy data for vacuum Einstein equations and obstructions to smoothness of scri. Communications in Mathematical Physics **161** (1994), 533–568. 

- [2] Andersson, L., Chru´sciel, P. T., and Friedrich, H. On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einstein’s field equations. Communications in Mathematical Physics **149** (1992), 587–612. 

- [3] Ashtekar, A. Geometry and physics of null infinity. Surveys in Differential Geometry **20** (2015), 99–122. 

- [4] Ashtekar, A., and Speziale, S. Null infinity as a weakly isolated horizon. Physical Review D **110** (2024), 044048. 

- [5] Bott, R. Lectures on Morse theory, old and new. Bulletin of the American Mathematical Society **7** (1982), 331–358. 

- [6] Capone, F., Mitra, P., Poole, A., and Tomova, B. Phase space renormalization and finite BMS charges in six dimensions. Journal of High Energy Physics **2023** (2023), 1–75. 

- [7] Chru´sciel, P. T., MacCallum, M. A., and Singleton, D. B. Gravitational waves in general relativity XIV. Bondi expansions and the ‘polyhomogeneity’ of _I_ . Philosophical Transactions of the Royal Society of London. Series A: Physical and Engineering Sciences **350** (1995), 113–141. 

- [8] Ciambelli, L. Asymptotic limit of null hypersurfaces. arXiv:2501.17357 (2025). 

- [9] Ciambelli, L., Leigh, R. G., Marteau, C., and Petropoulos, P. M. Carroll structures, null geometry, and conformal isometries. Physical Review D **100** (2019), 046010. 

- [10] Comp`ere, G., Fiorucci, A., and Ruzziconi, R. The _λ_ -BMS4 group of dS4 and new boundary conditions for AdS4. Classical and Quantum Gravity **36** (2019), 195017. 

- [11] Curry, S. N., and Gover, A. R. An introduction to conformal geometry and tractor calculus, with a view to applications in general relativity. Asymptotic Analysis in General Relativity **443** (2018), 86. 

- [12] Fefferman, C., and Graham, C. R. Conformal invariants. “Elie Cartan et les Mathematiques d’Aujourd’hui”, Asterisque, hors serie **S131** (1985), 95–116. 

- [13] Fefferman, C., and Graham, C. R. The ambient metric. Princeton University Press, 2012. 

- [14] Fern´andez-Alvarez,[´] F. News tensor on null hypersurfaces. Classical and Quantum Gravity **42** (2025), 155017. 

- [15] Fernandez-Alvarez, F., and Senovilla, J. M. M. Asymptotic structure with vanishing cosmological constant. Classical and Quantum Gravity **39** (2022), 165011. 

- [16] Frauendiener, J. Conformal infinity. Living Reviews in Relativity **7** (2004). 

- [17] Friedrich, H. The asymptotic characteristic initial value problem for Einstein’s vacuum field equations as an initial value problem for a first-order quasilinear symmetric hyperbolic system. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences **378** (1981), 401–421. 

54 

- [18] Friedrich, H. On the regular and the asymptotic characteristic initial value problem for Einstein’s vacuum field equations. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences **375** (1981), 169–184. 

- [19] Friedrich, H. Cauchy problems for the conformal vacuum field equations in general relativity. Communications in Mathematical Physics **91** (1983), 445–472. 

- [20] Friedrich, H. On the existence of _n_ -geodesically complete or future complete solutions of Einstein’s field equations with smooth asymptotic structure. Communications in Mathematical Physics **107** (1986), 587–609. 

- [21] Friedrich, H. Conformal Einstein evolution. In The conformal structure of space-time: Geometry, Analysis, Numerics. Springer, 2002, pp. 1–50. 

- [22] Friedrich, H. Geometric asymptotics and beyond. In One hundred years of general relativity (Surveys in Differential Geometry, 20). International Press, 2015, pp. 37–74. 

- [23] Geroch, R. Asymptotic structure of space-time. In Asymptotic structure of space-time. Springer, 1977, pp. 1–105. 

- [24] Geroch, R., and Horowtiz, G. T. Asymptotically simple does not imply asymptotically Minkowskian. Physical Review Letters **40** (1978), 203. 

- [25] Godazgar, M., and Reall, H. S. Peeling of the Weyl tensor and gravitational radiation in higher dimensions. Physical Review D **85** (2012), 084021. 

- [26] Golubitsky, M., and Guillemin, V. Stable mappings and their singularities, vol. **14** . Springer Science & Business Media, 2012. 

- [27] Herfray, Y. Tractor geometry of asymptotically flat spacetimes. Annales Henri Poincar´e **23** (2022), 3265–3310. 

- [28] Hilditch, D., Valiente Kroon, J. A., and Zhao, P. Improved existence for the characteristic initial value problem with the conformal Einstein field equations. General Relativity and Gravitation **52** (2020), 85. 

- [29] Hollands, S., and Ishibashi, A. Asymptotic flatness and Bondi energy in higher dimensional gravity. Journal of Mathematical Physics **46** (2005). 

- [30] Hollands, S., and Thorne, A. Bondi mass cannot become negative in higher dimensions. Communications in Mathematical Physics **333** (2015), 1037–1059. 

- [31] Hollands, S., and Wald, R. M. Conformal null infinity does not exist for radiating solutions in odd spacetime dimensions. Classical and Quantum Gravity **21** (2004), 5139. 

- [32] Ishibashi, A. Higher dimensional Bondi energy with a globally specified background structure. Classical and Quantum Gravity **25** (2008), 165004. 

- [33] Kannar, J. On the existence of smooth solutions to the asymptotic characteristic initial value problem in general relativity. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences **452** (1996), 945–952. 

- [34] Kehrberger, L. M. The case against smooth null infinity I: heuristics and counterexamples. Annales Henri Poincar´e **23** (2022), 829–921. 

- [35] Krtouˇs, P., and Podolsk`y, J. Asymptotic directional structure of radiative fields in spacetimes with a cosmological constant. Classical and Quantum Gravity **21** (2004), R233. 

- [36] Manzano, M. Geometry of abstract null hypersurfaces and matching of spacetimes. PhD Thesis, University of Salamanca, 2023. 

55 

- [37] Manzano, M., and Mars, M. The constraint tensor for null hypersurfaces. Journal of Geometry and Physics **208** (2025), 105375. 

- [38] Mars, M. Constraint equations for general hypersurfaces and applications to shells. General Relativity and Gravitation **45** (2013), 2175–2221. 

- [39] Mars, M. Hypersurface data: general properties and Birkhoff theorem in spherical symmetry. Mediterranean Journal of Mathematics **17** (2020), 1–45. 

- [40] Mars, M. Abstract null geometry, energy-momentum map and applications to the constraint tensor. Beijing Journal of Pure and Applied Mathematics **1** (2024), 797–852. 

- [41] Mars, M., and Pe´on-Nieto, C. Classification of _λ_ = 0-vacuum algebraically special spacetimes with conformally flat I from weyl tensor expansion. Journal of Geometry and Physics **220** (2025), 105713. 

- [42] Mars, M., and S´anchez-P´erez, G. Covariant definition of double null data and geometric uniqueness of the characteristic initial value problem. Journal of Physics A: Mathematical and Theoretical **56** (2023), 255203. 

- [43] Mars, M., and S´anchez-P´erez, G. Double null data and the characteristic problem in general relativity. Journal of Physics A: Mathematical and Theoretical **56** (2023), 035203. 

- [44] Mars, M., and S´anchez-P´erez, G. Conformal characterization of the FeffermanGraham ambient metric. arXiv: 2510.21646 (2025). 

- [45] Mars, M., and S´anchez-P´erez, G. Killing and homothetic initial data for general hypersurfaces. Classical and Quantum Gravity **42** (2025), 125001. 

- [46] Mars, M., and S´anchez-P´erez, G. Transverse expansion of the metric at null hypersurfaces I. Uniqueness and application to Killing horizons. Journal of Geometry and Physics **209** (2025), 105416. 

- [47] Mars, M., and S´anchez-P´erez, G. Transverse expansion of the metric at null hypersurfaces II. Existence results and application to Killing horizons. Journal of Geometry and Physics **217** (2025), 105605. 

- [48] Mars, M., and Senovilla, J. M. M. Geometry of general hypersurfaces in spacetime: junction conditions. Classical and Quantum Gravity **10** (1993), 1865. 

- [49] Moncrief, V., and Isenberg, J. Symmetries of cosmological Cauchy horizons. Communications in Mathematical Physics **89** (1983), 387–413. 

- [50] Newman, R. P. The global structure of simple space-times. Communications in Mathematical Physics **123** (1989), 17–52. 

- [51] Ortaggio, M. Bel–Debever criteria for the classification of the Weyl tensor in higher dimensions. Classical and Quantum Gravity **26** (2009), 195015. 

- [52] Paetz, T.-T. KIDs prefer special cones. Classical and Quantum Gravity **31** (2014), 085007. 

- [53] Penrose, R. The light cone at infinity. In Relativistic Theories of Gravitation, L. Infeld, Ed. Pergamon Press, Oxford, U.K., 1964, pp. 369–373. 

- [54] Penrose, R. Zero rest-mass fields including gravitation: asymptotic behaviour. Proceedings of the Royal Society of London. Series A. Mathematical and Physical Sciences **284** (1965), 159–203. 

56 

- [55] Penrose, R. Structure of space-time. In Battelle Rencontres, C. M. DeWitt and J. A. Wheeler, Eds. W. A. Benjamin, Inc., New York, NY, U.S.A., 1968, pp. 121–235. 

- [56] Rendall, A. D. Reduction of the characteristic initial value problem to the Cauchy problem and its applications to the Einstein equations. Proceedings of the Royal Society of London. A. Mathematical and Physical Sciences **427** (1990), 221–239. 

- [57] Riello, A., and Freidel, L. Renormalization of conformal infinity as a stretched horizon. Classical and Quantum Gravity **41** (2024), 175013. 

- [58] Sachs, R. K. On the characteristic initial value problem in gravitational theory. Journal of Mathematical Physics **3** (1962), 908–914. 

- [59] Schmidt, B. G. Vacuum spacetimes with toroidal null infinities. Classical and Quantum Gravity **13** (1996), 2811–2816. 

- [60] Tanabe, K., Kinoshita, S., and Shiromizu, T. Asymptotic flatness at null infinity in arbitrary dimensions. Physical Review D **84** (2011), 044055. 

- [61] Valiente Kroon, J. A. Polyhomogeneous expansions close to null and spatial infinity. In The Conformal Structure of Space-Time: Geometry, Analysis, Numerics. Springer, 2002, pp. 135–159. 

- [62] Valiente Kroon, J. A. A new class of obstructions to the smoothness of null infinity. Communications in Mathematical Physics **244** (2004), 133–156. 

- [63] Valiente Kroon, J. A. Conformal methods in general relativity. Cambridge University Press, 2017. 

- [64] Wald, R. M. General Relativity. University of Chicago Press, 2010. 

- [65] Winicour, J. Logarithmic asymptotic flatness. Foundations of Physics **15** (1985), 605–616. 

- [66] xAct Development Group. xAct: Efficient tensor computer algebra for the Wolfram language. https://www.xact.es/, 2026. Version 1.3.0. 

57 

