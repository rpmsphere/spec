Name:           4store
Version:        1.1.6
Release:        1
Group:          Productivity/Networking/Servers
License:        GPL v3+
URL:            https://github.com/4store/4store
Summary:        4store RDF server
Source:         %{name}-%{version}.tar.gz
BuildRequires:  automake, gmp-devel, glib2-devel, libxml2-devel, raptor2-devel, rasqal-devel, pcre-devel, avahi-glib-devel, readline-devel

%package        devel
Summary:        Development package for 4store
Group:          Development

%description
4store was designed by Steve Harris and developed at Garlik to underpin their
Semantic Web applications. It has been providing the base platform for around
3 years. At times holding and running queries over databases of 15GT,
supporting a Web application used by thousands of people.

%description    devel
Development package for 4store

%prep
%setup -q -n %{name}-%{version}
sed -i 's|#define _XOPEN_SOURCE|#define _XOPEN_SOURCE 700|' src/frontend/filter-datatypes.c

%build
#autoreconf -ifv
export LDFLAGS=-Wl,--allow-multiple-definition
echo %{version} > .version && ./autogen.sh
./configure --prefix=/usr --disable-static
#configure CFLAGS="-lz -fPIC -lraptor2"
#sed -i 's|-O2|-O2 -fPIC -lz -lraptor2|' src/*/Makefile*
%{__make}

%install
%{__rm} -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
%make_install
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/%{_libdir}
# hack
rm -f $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.*a

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README
%{_bindir}/4s-*
%{_libdir}/lib%{name}.so.*
%{_mandir}/man?/*

%files  devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}-0.pc
%{_includedir}/%{name}/*

%changelog
* Wed Sep 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.6
- Rebuilt for Fedora
* Fri Jan 13 2012 TI_Eugene <ti.eugene@gmail.com> - 1.1.4
- Initial build in OBS
