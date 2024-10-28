Summary:        Userspace bootsplash utility
Summary(de.UTF-8):      Eine Boosplashes Utility die auf der Benutzerebene arbeitet
Summary(pl.UTF-8):      Narzędzie do bootsplasha w przestrzeni użytkownika
Name:           usplash
Version:        0.5.19
Release:        9.1
License:        GPL
Group:          Applications
Source0:        https://ftp.debian.org/debian/pool/main/u/usplash/%{name}_%{version}.orig.tar.gz
Patch0:         %{name}-includes.patch
URL:            https://wiki.ubuntu.com/USplash
BuildRequires:  gd-devel
BuildRequires:  libpng-devel

%description
Usplash is a userspace application that uses the Linux framebuffer
interface to draw a splash screen at boot. It has a companion utility
that is able to send commands to usplash, allowing information about
the bootup sequence to be displayed in a more attractive way.

%description -l de.UTF-8
Usplash ist ein Programm dass auf der Benutzerebene arbeit und den
Linux Framepuffer benutzt um ein Bild beim Booten zu zeichnen. Es hat
ein Begleitprogramm dass Befehle an Usplash sendet, die dazu dienen
die Bootvorgang Informationen atraktiver zu gestalten.

%description -l pl.UTF-8
Usplash to aplikacja działająca w przestrzeni użytkownika
wykorzystująca linuksowy interfejs framebuffera do rysowania ekranu
startowego (splash screen) podczas startu systemu. Zawiera
towarzyszące narzędzie do wysyłania poleceń do usplasha, pozwalające
wyświetlać informacje o sekwencji startowej w bardziej atrakcyjny
sposób.

%package devel
Summary:        Usplash header files
Summary(de.UTF-8):      Usplash header Dateien
Summary(pl.UTF-8):      Pliki nagłówkowe usplasha
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
Usplash header files.

%description devel -l de.UTF-8
Usplash header Dateien.

%description devel -l pl.UTF-8
Pliki nagłówkowe usplasha.

%prep
%setup -q -n usplash
%patch 0 -p0

%build
%{__make} -C bogl \
        CC="%{__cc} -Wl,--allow-multiple-definition" \
        CFLAGS="-O2 -g -pipe -Wall -Wno-error -fPIC" \
        LDFLAGS+=" -s"

%{__make} \
        CC="%{__cc} -Wl,--allow-multiple-definition" \
        CFLAGS="-O2 -g -pipe -Wall -Wno-error -fPIC" \
        LDFLAGS+=" -s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}
%{__make} install DESTDIR=$RPM_BUILD_ROOT
%ifarch x86_64 aarch64
mv %{buildroot}/lib %{buildroot}/lib64
%endif


%files
%doc README
%{_sbindir}/*
%{_bindir}/*
/sbin/*
/%{_lib}/libusplash.so.0

%files devel
%{_includedir}/*.h
/%{_lib}/libusplash.so

%changelog
* Mon Jul 11 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.19
- Rebuilt for Fedora
* Thu Aug 23 2007 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
$Log: usplash.spec,v $
Revision 1.12  2007/08/23 14:58:46  shadzik
- package .so link in -devel subpackage
- rel 4
Revision 1.11  2007/08/23 14:35:31  shadzik
- add post and postun
- rel 3
Revision 1.10  2007/08/23 14:03:15  shadzik
- -devel  subpackage
- rel 2
Revision 1.9  2007/08/23 13:49:46  shadzik
- 0.5.2
- rel 1
Revision 1.8  2007/08/23 13:27:57  shadzik
- fix build on current th
- pass LDFLAGS
Revision 1.7  2007/02/12 22:09:19  glen
- tabs in preamble
Revision 1.6  2007/02/12 01:06:35  baggins
- converted to UTF-8
Revision 1.5  2006/11/19 03:07:12  shadzik
- 0.3e
- Source0 from debian ftp
Revision 1.4  2006/05/19 03:05:54  shadzik
- de
Revision 1.3  2006/05/19 02:12:20  shadzik
- CC and CFLAGS added
Revision 1.2  2006/03/21 19:48:28  qboosh
- pl
Revision 1.1  2006/03/16 20:45:17  patrys
- taken from Ubuntu
- NFY
