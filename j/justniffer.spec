Name:          justniffer
Version:       0.5.15
Release:       1
Summary:       Intelligent packet sniffer geared for capturing TCP traffic
Group:         Applications/Internet 
License:       GPL2+
URL:           https://github.com/onotelli/justniffer
Source0:       https://sourceforge.net/projects/justniffer/files/justniffer/justniffer%20%{version}/%{name}_%{version}.tar.gz 
BuildRequires: libpcap-devel, boost-devel, glib2-devel, libnet-devel, python-devel
Requires:      libpcap, boost, libicu

%description
justniffer captures TCP packets, reassembles and reorders them, performs
IP packet defragmentation and displays the tcp flow in a customizable way.
It is useful for logging network traffic in a 'standard' (web server like)
or in a customized way. It can log timings (e.g. response time), useful
for tracking network services performances (e.g. web server, application server, etc.).

%prep
%setup -q
#sed -i 's|^inline ||' lib/libnids-1.21_patched/src/util.h lib/libnids-1.21_patched/src/checksum.c

%build
#aclocal --force
#autoconf --force
#autoheader --force
#automake --add-missing
#libtoolize --copy --force
#autoreconf -ifv
#sed -i 's|boost_major_version=`.*`|boost_major_version=158|' configure
cp -f /usr/share/automake-*/config.* .
./configure --with-boost-libdir=%{_libdir} --prefix=%{_prefix}
make CXXFLAGS+="-std=gnu++14"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc README NEWS COPYING ChangeLog AUTHORS
%{_bindir}/justniffer
%{_mandir}/man8/justniffer.8*

%changelog
* Fri Oct 18 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.15
- Rebuilt for Fedora
* Tue Feb 12 2013 josef radinger <cheese@nosuchhost.net> - 0.5.11-2
- fix boost on 64bit-archs
* Tue Feb 12 2013 josef radinger <cheese@nosuchhost.net> - 0.5.11-1
- bump version
* Wed Mar 11 2010 Vladimir Vuksan <vuksan-php@veus.hr> - 0.5.6
- Initial SPEC created
