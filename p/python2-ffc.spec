%global srcname ffc

Name:           python2-%{srcname}
Version:        0.9.10
Release:        4.1
Summary:        A compiler for finite element variational forms
Group:          Applications/Engineering
License:        GPLv3+
URL:            https://www.fenicsproject.org
Source0:        https://launchpad.net/%{srcname}/trunk/%{version}/+download/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python2-ufl
Requires:       python2-fiat
Requires:       numpy

%description
FFC is a compiler for finite element variational forms. From a high
level description of the form, it generates efficient low-level C++
code that can be used to assemble the corresponding discrete operator
(tensor). In particular, a bilinear form may be assembled into a matrix
and a linear form may be assembled into a vector.

%prep
%setup -q -n %{srcname}-%{version}
find test -name '*.py' -exec chmod -x {} ';'
chmod -x test/regression/references/update.sh

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root $RPM_BUILD_ROOT

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README TODO demo/ bench/ test/
%{_mandir}/man*/*.1*
%{_bindir}/%{srcname}*
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/FFC*.egg-info

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.10
- Rebuilt for Fedora
* Sat Sep 10 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9.10-1
- Updated to new upstream version 0.9.10
* Sun Mar 27 2011 Fabian Affolter <fabian@bernewireless.net> - 0.9.9-1
- numpy is required
- Manual removed
- Updated URL
- Updated to new upstream version 0.9.9
* Sat Jul 03 2010 Fabian Affolter <fabian@bernewireless.net> - 0.9.3-1
- Initial package for Fedora
