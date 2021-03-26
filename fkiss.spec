Summary      : French-KISS!
Name         : fkiss
Version      : 0.35
Release      : 8.1
License      : GPL
Group        : Amusements/Graphics
Source0      : http://www.oersted.co.jp/~yav/soft/fkiss/%{name}-%{version}.tar.gz
URL          : http://www.oersted.co.jp/~yav/soft/#fkiss
BuildRequires: xorg-x11-proto-devel, libX11-devel

%description
This software fkiss - French-KISS! is a sample implementation of
KISekae Set system (KISS) for X Window System.
KISS is a software for playing Paper-doll on any computers.
"Kisekae" means "changing clothes".

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
install -Dm644 fkiss.man $RPM_BUILD_ROOT%{_mandir}/man6/fkiss.6
install -Dm644 frkismi4.lzh $RPM_BUILD_ROOT%{_datadir}/kiss/frkismi4.lzh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README*
%doc *.doc.* fkissrc.smp
%{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/kiss/*

%changelog
* Tue Mar 15 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.35
- Rebuild for Fedora
* Fri Nov 30 2001 NORIKANE Seiichiro <no_ri@kf6.so-net.ne.jp> - 0.33a-0k
- version up
* Fri Jan 05 2001 NORIKANE Seiichiro <no_ri@kf6.so-net.ne.jp> - 0.32-0k
- first build