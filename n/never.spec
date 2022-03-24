%undefine _debugsource_packages

Summary: A statically typed, embeddable functional programming language
Name: never
Version: 2.1.8
Release: 1
License: MIT
Group: Development/Language
URL: https://github.com/never-lang/
Source0: https://github.com/never-lang/never/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: libffi-devel

%description
Never is a simple functional programming language. Technically it may be
classified as syntactically scoped, strongly typed, call by value, functional
programming language.

In practise Never offers basic data types, assignment, control flow, arrays,
first order functions and some mathematical functions to make it useful to
calculate expressions. Also it demonstrates how functions can be compiled,
invoked and passed as parameters or results between other functions.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=/usr
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.lang %{buildroot}%{_datadir}/gtksourceview-2.0/language-specs/%{name}.lang

%clean
rm -rf %{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/%{name}
%{_datadir}/gtksourceview-2.0/language-specs/%{name}.lang

%changelog
* Sun Mar 6 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.8
- Rebuilt for Fedora
