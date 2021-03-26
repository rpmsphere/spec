Name: szl
Summary: A lightweight, embeddable scripting language
Version: 0.0.1
Release: 3.1
License: MIT
Group: Development/Languages
URL: https://github.com/dimkr/szl
Source0: %{name}-master.zip
BuildRequires: meson
BuildRequires: ninja-build

%description
szl is a tiny, embeddable scripting engine inspired by Tcl and shell. It's a
balanced mix of their key features: szl combines the simplicity of shell
scripting with the power of a dynamic, Tcl-like type system, minimalistic
syntax and programming language features missing in the shell, like exceptions
and OOP.

%prep
%setup -q -n %{name}-master

%build
meson --prefix=/usr build
%ninja_build -C build

%install
%ninja_install -C build

%files
%doc COPYING README AUTHORS
%{_bindir}/*
%{_mandir}/man1/%{name}*.1*
%{_includedir}/%{name}.h
%{_docdir}/%{name}
%{_libdir}/%{name}
%{_libdir}/lib%{name}.so

%changelog
* Fri Nov 09 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuild for Fedora
