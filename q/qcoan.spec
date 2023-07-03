Name:           qcoan
Version:        2.0
Release:        2
Summary:        Automaton and Turing Machine Simulator 
License:        C-FSL-v1.1
Group:          Development/Tools/Other
URL:            https://www.elstel.org/coan/index.html.en
Source0:        https://www.elstel.org/coan/coan-v%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Svg)

%description
qCoAn allows you to edit automata and turing machines in their graphical
representation. qCoAn can simulate finite automata, pushdown automata,
Turing machines and machine schemata for both types of automata: deterministic
and non-deterministic. The machines are abbreviated as follows:
FA, NFA, DFA, PDA, NPDA, TM, NDTM, MS.

%prep
%setup -qT -b 0 -n coan-%{version}

%build
%if ! %{defined mageia}
qmake-qt5 qcoan.pro
%else
qmake qcoan.pro
%endif
make %{_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install --mode=0755 build-qt/qcoan %{buildroot}%{_bindir}/qcoan
install --mode=0644 qcoan.desktop %{buildroot}%{_datadir}/applications/qcoan.desktop
install --mode=0644 images/coan-ico.png %{buildroot}%{_datadir}/pixmaps/coan-ico.png
mkdir -p %{buildroot}%{_docdir}/%{name}/examples
install --mode=0644 Test2.atm %{buildroot}%{_docdir}/%{name}/examples/Test2.atm

%files
%doc html/QuickHelp.html
%docdir %{_docdir}/%{name}/examples
%{_docdir}/%{name}/examples/
%{_docdir}/%{name}/examples/Test2.atm
%license C-FSL-v1.1.txt
%{_bindir}/qcoan
%{_datadir}/applications/qcoan.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuilt for Fedora
* Mon Jan  1 2018 estellnb@elstel.org
- fixed building for Debian packages and Mageia
* Mon Jan  1 2018 estellnb@elstel.org
- checked in initial version of coan-v2.0
