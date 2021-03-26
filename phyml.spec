%global debug_package %{nil}

Summary: A simple, fast, and accurate algorithm to estimate large phylogenies by maximum likelihood
Name: phyml
Version: 20120412
Release: 5.1
License: GPL
Group: Applications/Bioinformatics
URL: http://atgc.lirmm.fr/phyml/
Source0: http://www.lirmm.fr/~guindon/%{name}-%{version}.tar.gz

%description
Authors: Stéphane Guindon (Auckland University, New Zealand) and Olivier Gascuel (LIRMM, Montpellier, France)

PHYML is a software implementing a new method for building phylogenies
from DNA and protein sequences using maximum likelihood. Data sets can
be analysed under several models of evolution (JC69, K80, F81, F84,
HKY85, TN93 and GTR for nucleotides and Dayhoff, JTT, mtREV, WAG and
DCMut for amino acids). A discrete-gamma model (Yang, 1994) is
implemented to accommodate rate variation among sites. Invariable
sites can also be taken into account. PHYML has been compared to
several other softwares using extensive simulations. The results
indicate that its topological accuracy is at least as high as that of
fastDNAml, while being much faster.

%prep
%setup -q

%build
autoreconf -ifv
%configure
%ifarch aarch64
sed -i 's|-msse||' Makefile */Makefile
%endif
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README doc/phyml-manual-20120306.pdf
%{_bindir}/phyml

%changelog
* Thu Jun 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20120412
- Rebuild for Fedora
* Mon Feb 21 2005 Cymon Cox <cymon@duke.edu>
- Rebuild for version 2.4.4
* Tue Dec 14 2004 Cymon Cox <cymon@duke.edu>
- Initial packaging
