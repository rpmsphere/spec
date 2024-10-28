%undefine _debugsource_packages
Summary:        Han character library for CJKV languages
Name:           cjklib
Version:        0.3.2
Release:        7.1
Group:          Development/Python
License:        LGPLv3+
URL:            https://code.google.com/p/cjklib/
Source0:        https://cjklib.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  python2
BuildRequires:  python2-setuptools
Requires:       python-sqlalchemy
BuildArch:      noarch

%description
Cjklib provides language routines related to Han characters (characters
based on Chinese characters named Hanzi, Kanji, Hanja and chu Han
respectively) used in writing of the Chinese, the Japanese, infrequently
the Korean and formerly the Vietnamese language(s). Functionality is
included for character pronunciations, radicals, glyph components, stroke
decomposition and variant information. Cjklib is implemented in Python.

%prep
%setup -q
sed -i '/use_setuptools/d' setup.py

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root=$RPM_BUILD_ROOT --optimize=2

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*
 
%files
%doc COPYING README TODO examples
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Fri Jan 04 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.2
- Rebuilt for Fedora
* Mon Nov 01 2010 Funda Wang <fwang@mandriva.org> 0.3-4mdv2011.0
+ Revision: 591552
- add requires
* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.3-3mdv2011.0
+ Revision: 591062
- add requires
* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 0.3-2mdv2011.0
+ Revision: 590789
- rebuild for py2.7
* Sat Oct 02 2010 Funda Wang <fwang@mandriva.org> 0.3-1mdv2011.0
+ Revision: 582464
- update to new version 0.3
* Sat Dec 12 2009 Funda Wang <fwang@mandriva.org> 0.2-1mdv2010.1
+ Revision: 477760
- import cjklib
