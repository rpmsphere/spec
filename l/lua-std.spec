%define       V_lua    5.1

Name:         lua-std
Summary:      Lua Extension: Standard Libraries
URL:          http://luaforge.net/projects/stdlib/
Group:        Language
License:      MIT
Version:      22
Release:      4.1
Source0:      http://files.luaforge.net/releases/stdlib/stdlib/release22/stdlib-22.zip
BuildArch:    noarch

%description
This is the Lua extension package for standard library functions.

%prep
%setup -q -n stdlib

%build

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_datadir}/lua/%{V_lua}
cp -a \
    modules/* $RPM_BUILD_ROOT%{_datadir}/lua/%{V_lua}/

%files
%{_datadir}/lua/%{V_lua}/*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 22
- Rebuilt for Fedora
