Name: libforth
Summary: A small Forth interpreter that can be used as a library written in c99
Version: 0.4
Release: 3.1
License: MIT
Group: interpreters
URL: https://github.com/howerj/libforth
Source0: https://github.com/howerj/libforth/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
A Forth interpreter built around a library, libforth, that implements a
complete Forth interpreter.

%prep
%setup -q

%build
make %{name} %{name}.md

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm755 %{name}.a %{buildroot}%{_libdir}/%{name}.a

%files
%doc LICENSE *.md
%{_bindir}/*
%{_libdir}/%{name}.a

%changelog
* Thu Oct 05 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
