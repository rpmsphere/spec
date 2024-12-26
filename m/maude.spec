Name: maude
Summary: High-performance logical framework
Version: 3.4
Release: 1
Group: science
License: Free Software
URL: https://maude.cs.uiuc.edu
Source0: https://maude.cs.illinois.edu/w/images/d/d8/Maude%{version}.tar.gz
BuildRequires: buddy-devel
#BuildRequires: tecla-devel
BuildRequires: libsigsegv-devel
BuildRequires: cvc5-devel
BuildRequires: symfpu-devel
BuildRequires: gmp-devel
BuildRequires: yices-devel

%description
Maude is a high-performance reflective language and system supporting
both equational and rewriting logic specification and programming for
a wide range of applications. Maude has been influenced in important
ways by the OBJ3 language, which can be regarded as an equational
logic sublanguage. Besides supporting equational specification and
programming, Maude also supports rewriting logic computation.

%prep
%setup -q -n Maude-Maude%{version}
#sed -i 's|kind::IFF|kind::ITE|' src/Mixfix/variableGenerator.cc
cp /usr/include/yices/* src/Mixfix/

%build
%configure --without-tecla
make

%install
make install DESTDIR=%{buildroot}
install -d %{buildroot}%{_datadir}/%{name}
mv %{buildroot}%{_datadir}/*.%{name} %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS README.md COPYING NEWS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.4
- Rebuilt for Fedora
