Name:           psftools
License:        GPL v2 or later
Group:          Development/Tools/Other
Summary:        Conversion tools for .PSF fonts
URL:            http://www.seasip.demon.co.uk/Unix/PSF/
Version:        1.0.7
Release:        3.1
Source:         psftools-1.0.7.tar.bz2
Patch1:         psftools-1.0.7-Makefile.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The PSFTOOLS are designed to manipulate fixed-width bitmap fonts, such
as DOS or Linux console fonts. Both the PSF1 (8 pixels wide) and PSF2
(any width) formats are supported; the default output format is PSF2.

Note that these programs share no code with the Linux console utilities
(kbd).

%prep
%setup -q
#patch1

%build
%configure --disable-static
make %{?jobs:-j %jobs}

%install
make install DESTDIR=$RPM_BUILD_ROOT
# no devel package for now
# also, let's not split off a library package, as the library is only
# used by the tools
rm -r $RPM_BUILD_ROOT/usr/include
rm $RPM_BUILD_ROOT%_libdir/libpsf.{so,la}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%_bindir/*
%_libdir/libpsf.so.*
%_mandir/man1/*

%changelog
* Wed Jul 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuilt for Fedora

* Wed Oct  1 2008 mmarek@suse.cz
- packaged psftools version 1.0.7
