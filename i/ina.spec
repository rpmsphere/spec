Name: ina
Version: 0.4.3
Release: 1
Summary: Intrinsic Noise Analyzer
License: GPLv2
Group: Applications/Engineering
URL: http://www.ina.bio.ed.ac.uk/
Source0: http://intrinsic-noise-analyzer.googlecode.com/files/intrinsic-noise-analyzer-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: qt-devel
BuildRequires: eigen3-devel
BuildRequires: ginac-devel
BuildRequires: libsbml-devel
BuildRequires: llvm34-devel

%description
iNA is an analytic tool for quantifying fluctuations in biochemical networks.
In living cells such fluctuations are known as intrinsic noise arising from
low numbers of molecules. The software computes the Linear Noise Approximation
and more accurate approximations obtained from the system size expansion
automatically from a SBML file. As a result statistical measures such as
coefficients of variations and Fano factors as well as means and standard
deviations of concentrations are obtained. Analyses are performed in steady
state, in time-course or as a parameter scan and can be compared directly to
the stochastic simulation algorithm.

%prep
%setup -q -n intrinsic-noise-analyzer-%{version}

%build
%cmake
sed -i 's|-lLLVM[0-9A-Za-z]*|-lLLVM-3.4|g' app/CMakeFiles/ina.dir/link.txt lib/CMakeFiles/libina.dir/link.txt
make

%install
%make_install

%files
%{_bindir}/%{name}
%{_includedir}/libina
%{_libdir}/libina.so*
%{_datadir}/applications/IntrinsicNoiseAnalyzer.desktop
%{_datadir}/icons/IntrinsicNoiseAnalyzer.png

%changelog
* Mon Jan 12 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.3
- Rebuild for Fedora
