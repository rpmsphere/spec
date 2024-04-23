Name:           gaphor
Version:        2.17.0
Release:        1
Summary:        A UML modelling tool
License:        GPLv2
URL:            https://gaphor.sourceforge.net/index.php
Source0:        https://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  intltool
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
#BuildRequires:  python2-nose
Requires:       python3-zope-component
Requires:       python3-etk-docking
Requires:       gaphas

%description
Gaphor is a UML modelling tool, written in Python. This makes
it very easy to use (and very easy to extend -- and to write
;-) ).

%prep
%setup -q
sed -i 's|setuptools-git|setuptools|' setup.py

%build
python3 setup.py build

%install
python3 setup.py install --root $RPM_BUILD_ROOT
#sed -i 's|%{name}-48x48.png|%{python3_sitelib}/%{name}/ui/pixmaps/%{name}-48x48.png|' %{name}.desktop
#install -Dm644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/python$|/usr/bin/python3|' %{buildroot}%{_bindir}/%{name}*

%files
%doc LICENSE.txt README.md
#doc AUTHORS COPYING FAQ HACKING NEWS README
%{_bindir}/%{name}
%{_bindir}/%{name}convert
#{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/%{name}*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 2.17.0
- Rebuilt for Fedora
* Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.17.1-2
- Adds missing "Requires"
* Sat Dec 17 2011 qmp <glang@lavabit.com> - 0.17.1-1
- Initial packaging
