%global debug_package %{nil}
Summary: 	Chinese and Japanese Handwriting Recognition
Name: 		tegaki
Version: 	0.3.1
Release: 	1
License: 	GPLv2+
Group: 		System/Internationalization
Source0: 	http://www.tegaki.org/releases/0.3.1/tegaki-python-0.3.1.tar.gz
Source1: 	http://www.tegaki.org/releases/0.3.1/tegaki-pygtk-0.3.1.tar.gz
##Source2: 	http://www.tegaki.org/releases/0.3.1/tegaki-recognize-0.3.1.tar.gz
URL: 		http://www.tegaki.org/
BuildArch:	noarch
Requires:	%{name}-models
Requires:	zinnia-python
Obsoletes:	python-zinnia

%description
Tegaki is an ongoing project which aims to develop a free and open-source
modern implementation of handwriting recognition software, that is suitable for
both the desktop and mobile devices, and that is designed from the ground up to
work well with Chinese and Japanese.

%package pygtk
Summary:        PyGTK interface for %name
Group:          Development/Library
Requires:       %{name}

%description pygtk
This package contains PyGTK interface for %name.

%prep
%setup -q -c -a 1

%build
cd tegaki-python-0.3.1 ; python2 setup.py build ; cd ..
cd tegaki-pygtk-0.3.1 ; python2 setup.py build ; cd ..

%install
rm -rf %{buildroot}
cd tegaki-python-0.3.1 ; python2 setup.py install --root=%{buildroot} ; cd ..
cd tegaki-pygtk-0.3.1 ; python2 setup.py install --root=%{buildroot} ; cd ..

%clean
rm -rf %{buildroot}

%files
%{python2_sitelib}/tegaki
%{python2_sitelib}/tegaki_python-*.egg-info

%files pygtk
%{_datadir}/tegaki/icons
%{python2_sitelib}/tegakigtk
%{python2_sitelib}/tegaki_pygtk-*.egg-info

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuild for Fedora
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
