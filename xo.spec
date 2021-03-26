Name:           xo
Version:        0.1.14
Release:        4.1
Summary:        Exofrills Text Editor 
License:        WTFPL
Group:          Editor
URL:            https://github.com/scopatz/xo
Source0:        https://github.com/scopatz/xo/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-pegments
Requires:       python3-urwid
Requires:       python3-lazyasd

%description
The text editor without frills.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install -O1 --root=%{buildroot} --prefix=/usr
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}/usr/license %{buildroot}/usr/readme.rst %{buildroot}%{_docdir}/%{name}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{python3_sitelib}/*

%changelog
* Thu Oct 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.14
- Rebuild for Fedora
