Summary:	Simple port scanner
Summary(pl):	Prosty skaner portów
Name:		knocker
Version:	0.8.0
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	https://belnet.dl.sourceforge.net/sourceforge/knocker/%{name}-%{version}.tar.gz
Source1:	%{name}.png
URL:		https://knocker.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake

%description
Knocker is a simple, versatile, and easy-to-use TCP security port
scanner written in C.

%description -l pl
Knocker jest prostym, uniwersalnym i łatwym w użyciu skanerem portów.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
aclocal
autoconf
automake --add-missing
%configure
make

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog AUTHORS BUGS TO-DO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
* Sun May 26 2002 PLD Team <feedback@pld.org.pl>
Revision 1.5  2002/05/26 00:50:35  kloczek
- added png Icon to desktop file,
- simplications in %%install (use DESTDIR style install) and use more macros.
Revision 1.4  2002/05/25 14:38:12  klark
- add desktop file
- cosmetics
- release 2
- STBR
Revision 1.3  2002/05/25 11:10:53  qboosh
- pl fix
- Group changed to X11/Applications/Networking, prefix to /usr/X11R6
Revision 1.2  2002/05/25 10:55:24  kloczek
- added BuildRequires rules,
- added regenerat ac/am file (added am15 patch),
TODO: add desktop file.
Revision 1.1  2002/05/24 13:56:27  klark
- new PLD spec
