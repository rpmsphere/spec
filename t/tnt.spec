Name: tnt
Version: 126
Release: 2.1
Summary: Template Numerical Toolkit
License: Public domain
Group: Sciences/Mathematics
URL: https://math.nist.gov/tnt/
Source: https://math.nist.gov/tnt/tnt126.zip
#Source1: https://math.nist.gov/tnt/tnt120doc.zip

%description
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

%package devel
Summary: Development files of the Template Numerical Toolkit (TNT)
Group: Development/C++
BuildArch: noarch
Requires: gcc-c++

%description devel
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

This package contains development files of TNT.

%package doc
Summary: Documentation for the Template Numerical Toolkit (TNT)
Group: Development/Documentation
BuildArch: noarch

%description doc
The Template Numerical Toolkit (TNT) is a collection of interfaces and
reference implementations of numerical objects useful for scientific
computing in C++. The toolkit defines interfaces for basic data
structures, such as multidimensional arrays and sparse matrices,
commonly used in numerical applications. The goal of this package is to
provide reusable software components that address many of the
portability and maintennace problems with C++ codes.

TNT provides a distinction between interfaces and implementations of TNT
components. For example, there is a TNT interface for two-dimensional
arrays which describes how individual elements are accessed and how
certain information, such as the array dimensions, can be used in
algorithms; however, there can be several implementations of such an
interface: one that uses expression templates, or one that uses BLAS
kernels, or another that is instrumented to provide debugging
information. By specifying only the interface, applications codes may
utilize such algorithms, while giving library developers the greatest
flexibility in employing optimization or portability strategies.

This package contains development documentation for TNT.

%prep
%setup -q

%install
install -d %buildroot%_includedir
install -p -m644 *.h %buildroot%_includedir

%files devel
%_includedir/*

%files doc
%doc html/*

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 126
- Rebuilt for Fedora
* Fri Sep 17 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 126-alt1
- Initial build for Sisyphus
