Name:		sc-im
Version:	0.8.3
Release:	1
Summary:	Spreadsheet Calculator Improvised
Group:		Applications/Productivity
License:	https://github.com/andmarti1424/sc-im/blob/freeze/LICENSE
URL:		https://github.com/andmarti1424/sc-im
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	libzip-devel libxml2-devel ncurses-devel byacc git gcc gnuplot
Requires:	gnuplot

%description
SC-IM is an ncurses spreadsheet program for terminal.

%prep
%setup -q
sed -i 's|/usr/local|/usr|' src/Makefile

%build
cd src
make %{?_smp_mflags}

%install
cd src
%make_install

%files
%doc BUGS CHANGES HELP KNOWN_ISSUES LICENSE USER_REQUESTS WIKI
%{_bindir}/*
%{_mandir}/man1/sc-im.1*
%{_datadir}/sc-im

%changelog
* Sun May 21 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.3
- Rebuilt for Fedora
* Tue Aug 14 2018 Nux <rpm@li.nux.ro> - 0.7.0-1
- initial EL7 package build
