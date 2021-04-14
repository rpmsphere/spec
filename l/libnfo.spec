%undefine _debugsource_packages
Name:           libnfo
Version:        1.0.1
Release:        1
Summary:        An NFO file parser/writer library
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://libnfo.geexbox.org/
Source0:        http://libnfo.geexbox.org/releases/%{name}-1.0.1.tar.bz2
BuildRequires:  libxml2-devel,doxygen

%description
libnfo is a small library used to parse and write NFO files.
NFO files are used to store metadata information on many multimedia files.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
./configure --prefix=/usr --libdir=%{_libdir} --disable-doc
export CFLAGS=-fPIC
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING README
#/usr/share/doc/libnfo
%{_bindir}/libnfo-reader
%{_libdir}/libnfo.so
%{_libdir}/libnfo.so.1
%{_libdir}/libnfo.so.1.0.1
%{_libdir}/pkgconfig/libnfo.pc
%{_mandir}/man1/libnfo-reader.1.gz

%files devel
%{_includedir}/nfo.h
%{_libdir}/libnfo.a

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuilt for Fedora
* Mon Oct 04 2010 Emmanuel Seyman <emmanuel.seyman@club-internet.fr> - 2.0.0-1
- Update to 2.0.0
