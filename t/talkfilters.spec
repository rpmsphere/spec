Name:         talkfilters
Summary:      GNU Talk Filters
URL:          https://www.hyperrealm.com/main.php?s=talkfilters
Group:        Writing
License:      GPL
Version:      2.3.8
Release:      7.1
Source0:      https://www.hyperrealm.com/talkfilters/talkfilters-%{version}.tar.gz

%description
The GNU Talk Filters are filter programs that convert ordinary
English text into text that mimics a stereotyped or otherwise
humorous dialect. These filters have been in the public domain for
many years, but now for the first time they are provided as a single
integrated package. The filters include austro, b1ff, brooklyn,
chef, cockney, drawl, dubya, fudd, funetak, jethro, jive, kraut,
pansy, pirate, postmodern, redneck, valspeak, and warez. Each
program reads from standard input and writes to standard output. The
package also provides the filters as a C library, so they can be
easily used by other programs.

%prep
%setup -q

%build
autoreconf -ifv
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --disable-shared
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install AM_MAKEFLAGS="DESTDIR=$RPM_BUILD_ROOT"
rm %{buildroot}%{_datadir}/info/dir

%files
%{_bindir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/info/*
%{_mandir}/man?/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.8
- Rebuilt for Fedora
