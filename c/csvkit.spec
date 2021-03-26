Name:           csvkit
Version:        0.6.1
Release:        3.1
URL:            http://blog.apps.chicagotribune.com/
Summary:        A library of utilities for working with CSV
License:        MIT
Group:          Development/Languages/Python
Source:         http://pypi.python.org/packages/source/c/csvkit/csvkit-%{version}.tar.gz
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:	python-argparse
Requires:       python-dateutil
Requires:	python-sqlalchemy
BuildArch:      noarch

%description
csvkit is a library of utilities for working with CSV, the king of tabular file
formats. It is inspired by pdftk, gdal and the original csvcut utility by Joe
Germuska and Aaron Bycoffe.

%prep
%setup -q -n csvkit-%{version}
sed -i "1d" csvkit/{grep,convert/__init__,convert/xls,utilities/csvjson,convert/csvitself,sql,convert/fixed,__init__,exceptions,table,typeinference,cli,cleanup,sniffer,join,utilities/csvstack,convert/js}.py # Fix non-executable scripts

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc README
%{_bindir}/csv*
%{_bindir}/in2csv
%{python_sitelib}/*

%changelog
* Thu Jan 02 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1
- Rebuild for Fedora
* Fri Sep 27 2013 p.drouand@gmail.com
- Update to version 0.6.1
  + No changelog available
* Wed Jul 31 2013 hpj@urpla.net
- Update to version 0.5.0
* Fri Sep 23 2011 saschpe@suse.de
- Update to version 0.3.0
* Wed Aug 31 2011 saschpe@suse.de
- Update to version 0.2.5:
  * Use proper tarball
- Regenerated with py2pack:
  * Proper version checks around fdupes
  * Simpler Buildrequires
  * Fixed several rpmlint issues (non-excutable scripts, summary)
* Mon Aug 22 2011 hpj@urpla.net
- initial package version 0.2.4 git 3f0d6c2
