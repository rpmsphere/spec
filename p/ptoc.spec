Summary:    ANSI/Turbo Pascal to C/C++ converter
Name:       ptoc
Version:    3.61
Release:    4.1
License:    Free software
Group:      Development/Languages
Source:     https://www.garret.ru/%{name}-%{version}.tar.gz
URL:        https://www.garret.ru/lang.html
BuildRequires: libX11-devel

%description
This is yet another Pascal to C/C++ converter. The primary idea of this
converter is to produce readable and supportable code which preserves style
of original code as far as possible.

%prep
%setup -q -n %{name}

%build
make

%install
install -d %{buildroot}%{_bindir}
install -m755 ptoc cganal %{buildroot}%{_bindir}
install -d %{buildroot}%{_libdir}
install -m755 libptoc.a libXbgi.a %{buildroot}%{_libdir}

%files
%doc Readme.htm
%{_libdir}/lib*.a
%{_bindir}/*

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.61
- Rebuilt for Fedora
