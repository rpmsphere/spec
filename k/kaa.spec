Name:           kaa
Version:        0.53.0
Release:        2.1
Summary:        Console text editor
License:        MIT
URL:            https://github.com/kaaedit/kaa
Source0:        %{name}-master.zip
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel

%description
Kaa is a small and easy CUI text editor for console/terminal emulator environments.

%prep
%setup -q -n %{name}-master
rm -rf %{name}.egg.info
sed -i 's|\+\+Py_REFCNT(o);|++(o->ob_refcnt);|' _gappedbuf/_gappedbuf.c
sed -i 's|--Py_REFCNT(o);|--(o->ob_refcnt);|' _gappedbuf/_gappedbuf.c

%build
%py3_build

%install
%py3_install

%files
%doc *.rst  
%{_bindir}/%{name}
%{python3_sitearch}/*

%changelog
* Tue Nov 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.53.0
- Rebuilt for Fedora
