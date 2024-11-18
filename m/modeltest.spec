%global __os_install_post %{nil}
%undefine _debugsource_packages

Summary: Helps choose the model of DNA substitution that best fits the data
Name: modeltest
Version: 3.6
Release: 3.1
License: GPL
Group: Applications/Bioinformatics
URL: https://darwin.uvigo.es/software/modeltest.html
#NB Broken source link; go to URL
Source0: https://darwin.uvigo.es/software/modeltest3.6.zip

%description
The use of a model of DNA substitution is routine in the analysis of DNA
sequences. Modeltest helps a user to choose the model of DNA substitution
that best fits his/her data, among 56 possible models. This is accomplished
through an implementation of hierarchical likelihood ratio tests and the AIC
criterion.

%prep
%setup -q -n Modeltest3.6\ folder

%build
cd source
sed -i -e 's|-fast|-Ofast|' -e 's|gcc -c|gcc -Wno-implicit-function-declaration -c|' Makefile
make 

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/{doc,license,paupblock,sample}
install -m 755 README.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m 755 source/modeltest%{version} $RPM_BUILD_ROOT%{_bindir}
install -m 755 doc/Modeltest3.6.pdf $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/doc
install -m 755 license/gpl.html $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/license
install -m 755 paupblock/modelblockPAUPb10 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/paupblock
install -m 755 sample/{sample.log,sample.unix.scores,sample.nex,sample.out} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/sample

%files
%{_bindir}/modeltest%{version}
%{_docdir}/%{name}-%{version}

%changelog
* Thu Jun 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.6
- Rebuilt for Fedora
* Thu Dec 30 2004 Cymon J. Cox <cymon@duke.edu>
- New version 3.6
* Thu Oct 02 2003 Hunter Matthews <thm@duke.edu>
- Initial packaging
