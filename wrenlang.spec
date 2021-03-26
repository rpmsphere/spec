#global debug_package %{nil}
%define _name wren

Summary: Wren programming language
Name: wrenlang
Version: 0.2.0
Release: 1
License: MIT
Group: Development/Languages
Source: https://github.com/munificent/wren/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
URL: https://github.com/munificent/wren
BuildRequires: libuv-static
#BuildRequires: gyp
BuildRequires: python2

%description
Wren is a small, fast, class-based concurrent scripting language.
Think Smalltalk in a Lua-sized package with a dash of Erlang and
wrapped up in a familiar, modern syntax.

%prep
%setup -q -n %{_name}-%{version}
#sed -i 's|LIBUV_DIR :=.*|LIBUV_DIR := /usr|' util/wren.mk
#sed -i 's|LIBUV     :=.*|LIBUV     := %{_libdir}/libuv.a|' util/wren.mk
#sed -i '/libuv.py/d' util/wren.mk
#sed -i 's|-fPIC|-fPIC -Wno-error|' Makefile util/wren.mk
#sed -i 's|sprintf(message,|snprintf(message, sizeof(message),|' src/vm/wren_compiler.c

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 %{_name} %{buildroot}%{_bindir}/%{_name}

%files 
%doc *.md AUTHORS LICENSE
%{_bindir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Oct 09 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
