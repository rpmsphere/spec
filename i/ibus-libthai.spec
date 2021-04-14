Summary:	Thai input method engine for IBus
Summary(pl.UTF-8):	Silnik metody wprowadzania znaków tajskich dla platformy IBus
Name:		ibus-libthai
Version:	0.1.4
Release:	2.1
License:	GPL v2+
Group:		Libraries
Source0:	https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# Source0-md5:	0ac245d0f59f7cde5e1eaacb7d4faab5
URL:		https://linux.thai.net/
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk3-devel
BuildRequires:	ibus-devel
BuildRequires:	libthai-devel
%define		_libexecdir	%{_libdir}/ibus

%description
IBus-LibThai is a Thai input method engine for IBus, based on the
LibThai library.

Currently, it provides 3 keyboard layouts internally:
 - Ketmanee
 - Pattachote
 - TIS-820.2538
(Thai XKB symbols are also supported.)

%description -l pl.UTF-8
IBus-LibThai to silnik metody wprowadzania znaków tajskich dla
platformy IBus, oparty na bibliotece LibThai.

Obecnie udostępnia wewnętrznie 3 układy klawiatury:
 - Metmanee
 - Pattachote
 - TIS-820.2538
(tajskie symbole XKB są także obsługiwane).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-libthai
%attr(755,root,root) %{_libexecdir}/ibus-setup-libthai
%{_datadir}/ibus-libthai
%{_datadir}/ibus/component/libthai.xml

%changelog
* Tue Mar 14 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.4
- Rebuilt for Fedora
* Sat Jan 21 2017 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/ibus-libthai.git;a=log;h=master
* Sat Jan 21 2017 Jakub Bogusz <qboosh@pld-linux.org> 4b70dc1
- updated to 0.1.4
* Sat Apr 02 2016 Jakub Bogusz <qboosh@pld-linux.org> 77bc246
- updated to 0.1.3
* Sun Dec 28 2014 Jan Rękorajski <baggins@pld-linux.org> b00abf4
- updated gettext BR
* Thu Oct 31 2013 Jakub Bogusz <qboosh@pld-linux.org> dd45b67
- updated to 0.1.2
* Sun Jul 21 2013 Jakub Bogusz <qboosh@pld-linux.org> 52d68f9
- new
