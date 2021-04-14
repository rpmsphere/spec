%define _name MrAIC14

Summary: Perl script for calculating AIC, AICc, BIC, and Akaike weights for nucleotide substitution models
Name: mraic
Version: 1.4
Release: 3
License: unknown
Group: Applications/Bioinformatics
URL: http://www.ebc.uu.se/systzoo/staff/nylander.html
Source0: http://www.ebc.uu.se/systzoo/staff/nylander/%{_name}.tgz
BuildArch: noarch

%description
Author: Johan A. A. Nylander

Perl script for calculating AIC, AICc, BIC, and Akaike weights for
nucleotide substitution models. Likelihood scores under different
models are estimated using PHYML (Guindon and Gascuel, 2003). A
difference between Modeltest/MrModeltest2 and MrAIC.pl is that
MrAIC.pl does not evaluate all models on the same, approximate
topology. Instead, PHYML is used to try to find the maximum of the
likelihood function under all models. This is essential for
calculating AIC, AICc, and BIC. 

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{_name}
install -m 755 mraic.pl $RPM_BUILD_ROOT%{_bindir}
install -m 755 dat $RPM_BUILD_ROOT%{_docdir}/%{_name}
install -m 755 README.html $RPM_BUILD_ROOT%{_docdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/mraic.pl
%{_docdir}/%{_name}

%changelog
* Thu Jun 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Mar 28 2005 Cymon Cox <cymon@duke.edu>
- Updated to version 1.4
* Wed Mar 16 2005 Cymon Cox <cymon@duke.edu>
- Updated to version 1.3.3
- License changed to unknown
* Tue Feb 22 2005 Cymon Cox <cymon@duke.edu>
- Rebuild for version 1.3
- Added '%%define _name' to .spec file
* Fri Dec 10 2004 Cymon Cox <cymon@duke.edu>
- Initial packaging
