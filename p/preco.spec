%undefine _debugsource_packages

Name: preco
Summary: Exciton Model Preequilibrium Code with Direct Reactions
Version: 2006
Release: 5.1
Group: Applications/Engineering
License: opensource
URL: http://www.nndc.bnl.gov/nndcscr/model-codes/preco-2000/
Source0: http://www.nndc.bnl.gov/nndcscr/model-codes/%{name}-%{version}/%{name}6.zip
BuildRequires: gcc-gfortran

%description
PRECO is a two-component exciton model code for the calculation of double
differential cross sections of light particle nuclear reactions. The code,
written in FORTRAN, runs on a PC and calculates the emission of particles up to
mass four, including separate subroutines for nucleon transfer reactions,
knockout and inelastic scattering involving complex particles, and collective
state excitation (both discrete and GDR). Emission of a second nucleon at either
the preequilibrium or equilibrium phase of the reaction is allowed following
neutron or proton emission. Available options include collective or ordinary
pairing corrections, isospin conservation, and shell structure effects. Output
of both the energy differential and double differential cross sections is available.
A recommended set of global parameters is provided.

%prep
%setup -q -c

%build
f95 -c *.for
f95 *.o -o %{name}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
cp preco6.pdf preco6.dat preco6.out %{buildroot}%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Mar 17 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2006
- Rebuilt for Fedora

