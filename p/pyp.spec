%global debug_package %{nil}
Name: pyp
Summary: Python Power at the Prompt
Version: 2.12
Release: 1
Group: Development/Tools
License: New BSD
URL: https://code.google.com/p/pyp/
Source0: pyp-2.12.tar.gz
BuildArch: noarch
Requires: python2

%description
Pyp is a linux command line text manipulation tool similar to awk or sed,
but which uses standard python string and list methods as well as custom
functions evolved to generate fast results in an intense production
environment. Pyed Pyper was developed at Sony Pictures Imageworks to
facilitate the construction of complex image manipulation "one-liner"
commands during visual effects work on Alice in Wonderland, Green Lantern,
and the The Amazing Spiderman.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-2

%files
%{_bindir}/%{name}-2
%{python2_sitelib}/%{name}-%{version}-py2.*.egg-info

%changelog
* Tue Nov 26 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.12
- Rebuild for Fedora
