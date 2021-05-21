Summary: 	Commercial Handwriting Recognition Models for Tegaki
Name: 		tegaki-model-fineart
Version: 	0.4
Release: 	1
License: 	Commercial
Group: 		System/Internationalization
Source: 	%{name}.zip
BuildArch:	noarch
Requires:	tegaki, python-fineart
Provides:	tegaki-model

%description
Commercial Handwriting Recognition Models for Tegaki.
Including Fineart.

%prep
%setup -q -c

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitelib}/tegaki/engines
cp tegakifineart.py %{buildroot}%{python_sitelib}/tegaki/engines
mkdir -p %{buildroot}%{_datadir}/tegaki/models/fineart
cp handwriting-fineart-zh_TW.meta %{buildroot}%{_datadir}/tegaki/models/fineart

%clean
rm -rf %{buildroot}

%files
%{python_sitelib}/tegaki/engines/*
%{_datadir}/tegaki/models/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
* Thu Sep 01 2011 Kylix Lo <kylix.lo@ossii.com.tw> 0.4-1.ossii
- Rebuild tegaki-models-fineart as standalone source rpm
* Wed Mar 31 2010 Wei-Lun Chao <bluebat@member.fsf.org> 0.3-1.ossii
- Rebuild tegaki-models-commercial as standalone source rpm
* Tue Feb 09 2010 Feather Mountain <john@ossii.com.tw> 0.2-3.git20090918.ossii
- Fix tegaki requires tegaki-models
* Tue Nov 17 2009 Feather Mountain <john@ossii.com.tw> 0.2-2.git20090918.ossii
- Add patch for support Fineart model
- Add meta for Fineart model zh_TW
* Fri Sep 25 2009 Feather Mountain <john@ossii.com.tw> 0.2-1.git20090918.ossii
- Update to 20090918
* Mon Apr 20 2009 Feather Mountain <john@ossii.com.tw> 0.1-2.git20090421.ossii
- Rebuild for OSSII
- Add patch for support Penpower model
- Add meta for Penpower model zh_TW
- Update to 20090421
* Tue Mar 24 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0.1-1.git20090324.ossii
- Rebuild for OSSII
* Sun Feb 15 2009 Funda Wang <fundawang@mandriva.org> 0.1-1mdv2009.1
+ Revision: 340630
- BR python
- import tegaki
