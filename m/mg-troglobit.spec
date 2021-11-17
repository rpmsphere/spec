%global _name mg

Name: mg-troglobit
Summary: Public domain Micro Emacs derivative
Version: 3.5
Release: 1
Group: Applications/Editors
License: Unlicense
URL: https://github.com/troglobit/mg/
Source0: https://github.com/troglobit/mg/releases/download/v%{version}/%{_name}-%{version}.tar.gz
BuildRequires: ncurses-devel
Conflicts: mg

%description
This program is intended to be a small, fast, and portable
editor for people who can't (or don't want to) run real
Emacs for one reason or another.  It is compatible with GNU
because there shouldn't be any reason to learn more than
one Emacs flavor.

%prep
%setup -q -n %{_name}-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_bindir}/%{_name}
%{_docdir}/%{_name}
%{_mandir}/man1/%{_name}.1.*

%changelog
* Sun Oct 24 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.5
- Rebuilt for Fedora
