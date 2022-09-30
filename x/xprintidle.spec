%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages

Name:           xprintidle
Version:        0.2.4
Release:        2
Summary:        Utility to print user's idle time in X
License:        GPL-2.0
Group:          System/X11/Utilities
URL:            http://freecode.com/projects/xprintidle
Source:         http://httpredir.debian.org/debian/pool/main/x/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)

%description
An utility that queries the X server for the user's idle time and
prints it to stdout (in milliseconds).

%prep
%setup -q

%build
gcc -g -O2 -o %{name} %{name}.c -lXss -lX11 -lXext

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING README.md AUTHORS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Aug 14 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuilt for Fedora
* Thu Jul  7 2016 sor.alexei@meowr.ru
- Initial package
