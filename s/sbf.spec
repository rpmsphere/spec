%global debug_package %{nil}

Name: sbf
Summary: A program for brainfuck
Version: 0.9.4
Release: 16.1
Group: Development/Languages
URL: http://sourceforge.net/projects/sbfutil/
Source0: http://sourceforge.net/projects/sbfutil/files/%{name}-%{version}/%{name}-%{version}.tar.gz
License: GPL, BSD
BuildRequires: readline-devel

%description
sbf stands for "sbf brainfuck". It is a command-line-based program for using
the brainfuck programming language.

%prep
%setup -q -n %{name}
sed -i -e 's|dylib|so|' -e 's|"i386"|*86*|' -e 's|$binary|%{buildroot}%{_bindir}|' -e 's|$manpage|%{buildroot}%{_datadir}/man|' -e 's|-02|-O2|' configure

%build
%configure
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/man/man1 %{buildroot}%{_datadir}/man/man7
make install

%files
%doc README SAMPLES BSD COPYING GPL
%{_bindir}/%{name}
%{_datadir}/man/man?/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
