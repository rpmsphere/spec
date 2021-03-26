Name:           llink
Version:        2.3.2
Release:        1
Summary:        A media streamer
Group:          Applications/Multimedia
License:        freeware, no commercial
URL:            http://lundman.net/wiki/index.php/Llink
Source0:        http://www.lundman.net/ftp/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}
BuildRequires:  clinkcav-devel, libdvdnav-devel, libdvdread-devel, libdvdcss-devel

%description
Llink lets you play movies, view online trailers, browse images or play music
over a network using the http protocol. It should work with most Syabas NMT
hardware (NetworkedMediaTank middleware based players), such as the Popcorn
Hour A- and B-series, HDX, iSTAR, Egreat a whole range of others, possibly
even a couple of older ones like the LinkTheater. Some of the best reasons to
run llink is that it can run on a great many platforms, including most popular
NAS devices - even on the NMT player itself - and it can play media directly
from RAR files. llink is also a UPNP MediaServer, sometimes called DNLA/UPNP,
and is able to talk to many UPNP devices.

%package devel
Summary:        Llink media streamer
Requires:       %{name}	

%description devel
Development files for Llink media streamer.

%prep
%setup -q
sed -i '37i #include "dvdread/dvd_input.h"' undvd/undvd.c
sed -i -e 's/^SKIN|USERAGENT/#SKIN|USERAGENT/' -e 's/^ROOT/#ROOT/' -e 's,^#ROOT|path=~/,^ROOT|path=~/,' src/%{name}.conf
sed -i '/dvdread\/dvd_input.h/d' undvd/undvd.c

%build
%configure --enable-clinkc --without-openssl --enable-dvdcss
sed -i 's|-ldl|-ldl -lexpat -lpthread -luuid|' src/Makefile
%__make %{?_smp_mflags}

%install
%__rm -rf %{buildroot}
%__make install DESTDIR=%{buildroot}
install -Dm755 %{SOURCE1} %{buildroot}%{_sysconfdir}/init.d/%{name}
rm -f %{buildroot}%{_sysconfdir}/%{name}/undvd %{buildroot}%{_sysconfdir}/%{name}/unrar
mkdir -p %{buildroot}/usr/local/bin
mv %{buildroot}%{_bindir}/unrar %{buildroot}/usr/local/bin

%clean
%__rm -rf %{buildroot}

%files
%doc README* LICENSE* Example-playlist.txt *.png
%{_bindir}/*
/usr/local/bin/unrar
%{_sysconfdir}/%{name}
%{_sysconfdir}/init.d/%{name}

%files devel
%{_libdir}/lib*.a
%{_includedir}/*.h

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuild for Fedora
