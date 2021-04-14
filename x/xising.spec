Summary: Simulation of Ising Model
Name: xising
Version: 1.0
Release: 3.1
License: GPLv2
Group: Amusements/Graphics
URL: http://www.seehuhn.de/pages/xising
Source: http://m.seehuhn.de/programs/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel

%description
The Ising model is a simple model from statistical mechanics, which describes
a system of coupled spins. The spins are modelled as cells which can be in
either of two states. In the pictures below each pixel corresponds to one cell,
and the states are represented by the colors black and white.

The program implements two iterative methods to simulate states of the Ising model:
the Gibbs sampler and the Metropolis algorithm.

%prep
%setup -q
sed -i 's|x_res, y_res)|100, 100)|' main.c

%build
%configure
make

%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*

%changelog
* Fri Aug 24 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
