%undefine _debugsource_packages
%define V_lua 5.1

Name:         lua-cjson
Summary:      Lua Extension: JSON Encoding/Decoding
URL:          https://www.kyne.com.au/~mark/software/lua-cjson.php
Group:        Language
License:      MIT
Version:      2.1.0
Release:      6.1
Source0:      https://www.kyne.com.au/~mark/software/download/lua-cjson-%{version}.tar.gz
BuildRequires: lua-devel

%description
This is the Lua extension package for JSON encoding/decoding.

%prep
%setup -q

%build
%{__make} %{_smp_mflags} \
    CC="%{__cc}" \
    PREFIX="%{_prefix}" \
    LUA_INCLUDE_DIR=%{_includedir}

%install
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_libdir}/lua/%{V_lua} \
    $RPM_BUILD_ROOT%{_datadir}/lua/%{V_lua}/cjson
install -c -m 755 \
    cjson.so $RPM_BUILD_ROOT%{_libdir}/lua/%{V_lua}/
install -c -m 644 \
    lua/cjson/util.lua $RPM_BUILD_ROOT%{_datadir}/lua/%{V_lua}/cjson/

%files
%{_libdir}/lua/%{V_lua}/cjson.so
%{_datadir}/lua/%{V_lua}/cjson/util.lua

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
