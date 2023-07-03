%undefine _debugsource_packages

Name: yforth
Summary: Small freeware Forth environment in ANSI C
Version: 0.2.1
Release: 3.1
License: GPLv3+
Group: interpreters
URL: https://git.gag.com/?p=debian/yforth
Source0: %{name}-%{version}.tar.gz

%description
yForth? is an interestingly small implementation of Forth for Linux.  It
suffers several deficiencies.  For general Forth programming or learning
under Linux, yForth? is not the best choice.

%prep
%setup -q

%build
make

%install
install -d %{buildroot}%{_bindir}
install -m755 %{name} div %{buildroot}%{_bindir}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc LICENSE README yforthlogo.gif
%{_bindir}/*
%{_mandir}/man1/%{name}.1*

%changelog
* Fri Sep 08 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.1
- Rebuilt for Fedora
