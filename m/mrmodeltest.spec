%undefine _debugsource_packages

Summary: A simplified version of David Posada's Modeltest
Name: mrmodeltest
Version: 2.1
Release: 4.1
License: GPL
Group: Applications/Bioinformatics
URL: https://www.ebc.uu.se/systzoo/staff/nylander.html
Source0: https://www.ebc.uu.se/systzoo/staff/nylander/MrMod21.tgz

%description
Author: Johan A. A. Nylander

MrModeltest is a simplified version of David Posada's "Modeltest 3.06" (see
Modeltest homepage https://bioag.byu.edu/zoology/crandall_lab/modeltest.htm).

"Simplified version" means that it was rewritten to perform the HLRT on 24
instead of 56 model of nucleotide substitutions (basically a Modeltest
version 1.0). It also means that it cannot perform all things that Modeltest
3.06 can such as calculations in "calculator mode" etc.

%prep
%setup -q -n MrModeltest%{version}
sed -i 's|-fast|-Ofast|' Makefile

%build
make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
cd %{_builddir}/MrModeltest%{version}
install -m 755 mrmodeltest2 $RPM_BUILD_ROOT%{_bindir}
install -m 644 doc/gpl.html $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
install -m 644 doc/hLRT1.jpg $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
install -m 644 doc/hLRT2.jpg $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
install -m 644 doc/hLRT3.jpg $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
install -m 644 doc/hLRT4.jpg $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}
install -m 644 README.html $RPM_BUILD_ROOT%{_docdir}/MrModeltest%{version}

%files
%{_bindir}/mrmodeltest2
%{_docdir}/MrModeltest%{version}

%changelog
* Fri Jun 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
* Tue Feb 22 2005 Cymon Cox <cymon@duke.edu>
- Updated to version 2.2
* Fri Dec 10 2004 Cymon Cox <cymon@duke.edu>
- Updated to version 2.1
* Thu Oct 02 2003 Hunter Matthews <thm@duke.edu>
- Initial packaging
