%undefine _debugsource_packages

Summary: X based gopher client
Name: xgopher
Version: 1.3.3
Release: 16.1
License: distributable
Group: X11/Applications/Networking
Source0: ftp.x.org:/contrib/applications/xgopher.1.3.3.tar.Z
Patch0: xgopher.1.3.dif
BuildRequires: imake
BuildRequires: libXt-devel, xorg-x11-xbitmaps, libXaw-devel, libXmu-devel, libXext-devel
Summary(de): X-orientierter Gopher-Client
Summary(fr): Client gopher sous X
Summary(tr): X tabanlý gopher istemcisi

%description
Gopher, a method of accessing information on the Internet, is made easy
with this X-Windows gopher client. Although gopher is less up-to-date than
the WWW, Xgopher can still open up a portal to the vast storehouse of
information available on the Internet.

%description -l de
Gopher, ein Verfahren des Informationszugriffs im Internet, wird mit
diesem Gopher-Client für X-Windows zum Kinderspiel. Obwohl Gopher
nicht so aktuell wie das WWW ist, stellt Xgopher trotzdem ein Tor 
zu den im Internet gespeicherten Informationen dar.

%description -l tr
gopher, Ýnternet üzerindeki bilgilere ulaţmanýn en eski yöntemlerinden
biridir. xgopher yardýmýyla son derece geniţ bilgi bankalarýna grafik
arabirimi yardýmýyla rahatlýkla bađlanabileceksiniz.

%prep
%setup -q -n xgopher.1.3
%patch0 -p0
sed -i '/extern.*errno;/i #include <errno.h>' sc_*.c

%build
xmkmf
sed -i 's|-lX11|-lX11 -Wl,--allow-multiple-definition|' Makefile
make

%install
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
make DESTDIR=$RPM_BUILD_ROOT install install.man
cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/xgopher <<EOF
xgopher name "xgopher"
xgopher description "Gopher Client"
xgopher group Networking
xgopher exec "xgopher &"
EOF

%files
%{_bindir}/xgopher
/usr/lib/X11/app-defaults
/usr/lib/X11/xgopher/xgopher.help
%if %{fedora}<21
%config /etc/X11/app-defaults/Xgopher
%config /etc/X11/app-defaults/Xgopher-color
%else
%config %{_datadir}/X11/app-defaults/Xgopher
%config %{_datadir}/X11/app-defaults/Xgopher-color
%endif
%{_mandir}/man1/xgopher.1x.*
%config /etc/X11/wmconfig/xgopher

%changelog
* Tue Jan 28 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.3
- Rebuilt for Fedora
* Wed Aug 12 1998 Jeff Johnson <jbj@redhat.com>
- build root
* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr
* Fri Oct 24 1997 Marc Ewing <marc@redhat.com>
- wmconfig
* Mon Jul 21 1997 Erik Troan <ewt@redhat.com>
- built against glibc
