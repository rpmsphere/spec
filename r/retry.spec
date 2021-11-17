Name:      retry
Version:   1.0.4
Release:   1
Summary:   Repeat a command until success
License:   ASL 2.0
Group:     Applications/System
Source:    https://github.com/minfrin/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
URL:       https://github.com/minfrin/%{name}
BuildRequires: gcc, autoconf, automake, libtool
%define    __libtoolize /bin/true

%description
Repeat a command until the command succeeds.

%prep
%setup -q
rm -rf %{_builddir}/%{name}-%{version}/debian
%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/retry
%{_mandir}/man1/retry.1*
%doc AUTHORS ChangeLog README
%license COPYING

%changelog
* Sun Oct 31 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
* Sun Jan 05 2020 Graham Leggett <minfrin@sharp.fm> - 1.0.0-1
- Initial version of the package
