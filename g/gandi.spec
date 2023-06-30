%undefine _debugsource_packages
Name: gandi
Version: 0.18
Release: 4.1
Summary: Gandi CLI as a service
Group: System Management
License: unknown
URL: https://github.com/gandi/
Source0: gandi.cli-%{version}.tar.gz
Provides: gandicli
BuildRequires: python-docutils, python2-devel, python-setuptools
Requires: python >= 2.7, python-click, python-yaml, python-requests
BuildArch: noarch

%description
Administrate and deploy your gandi resources.

%prep
%setup -n gandi.cli-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
rst2man --no-generator gandicli.man.rst > gandi.1
install -d -m 0755 %{buildroot}/usr/share/man/man1
install -m 0644 gandi.1 %{buildroot}/usr/share/man/man1

%clean
rm -r %{buildroot}

%files
%{_bindir}/gandi
%{_mandir}/man1/gandi.1.*
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/*-nspkg.pth
%{python2_sitelib}/gandi

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18
- Rebuilt for Fedora
* Fri Jul 18 2014 Gandi <feedback@gandi.net> 0.1
- first rpm structure
