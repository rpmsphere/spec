%define __python /usr/bin/python3

Name: qutip
Summary: Quantum Toolbox in Python
Version: 2.2.0
Release: 7.1
Group: Development/Libraries
License: GPLv3
URL: https://qutip.org/
Source0: https://qutip.org/downloads/%{version}/QuTiP-%{version}.tar.gz
BuildRequires: python3-devel numpy Cython atlas

%description
QuTiP is open-source software for simulating the dynamics of open quantum
systems. The QuTiP library depends on the excellent Numpy and Scipy numerical
packages. In addition, graphical output is provided by Matplotlib. QuTiP aims
to provide user-friendly and efficient numerical simulations of a wide variety
of Hamiltonians, including those with arbitrary time-dependence, commonly found
in a wide range of physics applications such as quantum optics, trapped ions,
superconducting circuits, and quantum nanomechanical resonators.

%prep
%setup -q
sed -i 's|-w -ffast-math -O3|-ffast-math|' qutip/cyQ/setup.py

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot}

%files
%doc *.txt
%{python3_sitearch}/*

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
