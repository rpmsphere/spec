%define debug_package %{nil}

Summary:	Command-line based markdown presentation tool
Name:		mdp
Version:	1.0.15
Release:	1
License:	GPLv3
Group:		Office
URL:		https://github.com/visit1985/mdp
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)

%description
A command-line based markdown presentation tool.

%prep
%setup -q

%build
make

%install
%make_install PREFIX=/usr

%files
%doc AUTHORS COPYING CREDITS
%{_bindir}/*
%{_mandir}/man1/%{name}.1.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.15
- Rebuild for Fedora
* Tue Feb 24 2015 Denis Silakov <denis.silakov@rosalab.ru> 0.93.0-1
+ Revision: fbb562e
- Fix ncurses BR
