Name:		codec2
Version:	0.2.0
Release:	3.1
Summary:	An open source speech codec
Group:		Applications/Communications
License:	GPLv2+	
URL:		http://rowetel.com/codec2.html
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%package devel
Summary:  	Development files for Codec 2 
Group: 		Applications/Communications
Requires: 	codec2

%description
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This is the runtime library package.

%description devel
Codec 2 is an open source (LGPL licensed) speech codec for 2400 bit/s
and below. This package contains the development files required to 
compile programs that use codec2.

%prep

%setup -q

%build
make

%install
BINDIR=$RPM_BUILD_ROOT%{_bindir}
LIBDIR=$RPM_BUILD_ROOT%{_libdir}
INCLUDEDIR=$RPM_BUILD_ROOT%{_includedir}/%{name}
SHAREDIR=$RPM_BUILD_ROOT%{_datadir}/%{name}
DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $BINDIR
cd src
install -m 0755 c2dec $BINDIR
install -m 0755 c2demo $BINDIR
install -m 0755 c2enc $BINDIR
install -m 0755 c2sim $BINDIR
install -d -m 0755 $LIBDIR
cp --archive .libs/libcodec2.* $LIBDIR
#install -m 0755 .libs/libcodec2.a $LIBDIR
#install -m 0755 .libs/libcodec2.so $LIBDIR
#install -m 0755 .libs/libcodec2.so.0 $LIBDIR
#install -m 0755 .libs/libcodec2.so.0.0.0 $LIBDIR
install -d -m 0755 $INCLUDEDIR
cp --archive *.h $INCLUDEDIR
install -d -m 0755 $SHAREDIR
cd ..
cp --archive asterisk $SHAREDIR
cp --archive fltk $SHAREDIR
cp --archive octave $SHAREDIR
cp --archive portaudio $SHAREDIR
cp --archive raw $SHAREDIR
cp --archive script $SHAREDIR
cp --archive voicing $SHAREDIR
cp --archive wav $SHAREDIR
cp --archive win32 $SHAREDIR

%post
/usr/sbin/ldconfig

%postun  
/usr/sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/lib*

%files devel
%{_includedir}/*
%{_datadir}/%{name}
%doc AUTHORS ChangeLog COPYING INSTALL README* NEWS

%changelog
* Thu Feb 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuild for Fedora
* Sun Dec 30 2012 Mike Heitmann <mheitmann@n0so.net> 0.2.0-2
- Fixed ldconfig path error
* Sun Dec 30 2012 Mike Heitmann <mheitmann@n0so.net> 0.2.0-1
- Fixed ldconfig errors, corrected version number
* Sun Dec 23 2012 Mike Heitmann <mheitmann@n0so.net> 0.0.1-1
- Initial SPEC
- Split out from FreeDV to compile separately
