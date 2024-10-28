Summary:        Qbasic to C conversion
Summary(pl):    Konwerter z Qbasic na C
Name:           qb2c
Version:        3.43
Release:        3.1
License:        freely distributable
Group:          Development/Languages
Source0:        https://www.sourcefiles.org/Programming/Compilers/Procedural/%{name}-%{version}.tgz
URL:            https://www.sourcefiles.org/Programming/Compilers/Procedural/qb2c-3.43.tgz.shtml
BuildRequires:  libX11-devel

%description
This package attempts to convert Microsoft QBASIC programs into
compilable C code. A 'brun' script is also provided to directly
execute a qbasic program.

%description -l pl
Ten pakiet próbuje dokonać konwersji programów pisanych w Microsoft
QBASIC w kod kompatybilny z C. Dołączony jest też skrypt brun do
bezpośredniego uruchamiania programów w qbasicu.

%prep
%setup -q -c
sed -i -e 's/bcc/qbcc/g' -e 's/bcpp/qbcpp/g' -e 's/brun/qbrun/g' *

%build
%{__cc} %{optflags} -o qbcpp bcpp.c
%{__cc} %{optflags} -o qb2c qb2c.c -lm
%{__cc} %{optflags} -o calib calib.c -lm
%{__cc} %{optflags} -c -w x11int.c rotated.c gifencode.c gifdecode.c pickpalette.c
ar -cr libqbX11.a x11int.o rotated.o gifencode.o gifdecode.o pickpalette.o
rm -f *.o
%{__cc} %{optflags} -fPIC -c -w x11int.c rotated.c gifencode.c gifdecode.c pickpalette.c
%{__cc} %{optflags} -shared -Wl,-soname,libqbX11.so.3 -o libqbX11.so.%{version} *.o -lX11 -lm

cat <<'EOF' > qbcc
#!/bin/sh
qb2c -b -C $1 $2 $3 $4 $5 $6
if test $? = 0 ; then
        gcc -o $1 $1.c -L$(pwd) -lqbX11 -lX11 -lm
fi
EOF

cat <<'EOF' > qbrun
#!/bin/sh
TEMPNAM=`mktemp /tmp/qb.XXXXXX`
rm -f $TEMPNAM
qb2c -b -C $1 $2 $3 $4 $5
if test $? = 0 ; then
        gcc -o $TEMPNAM $1.c -L$(pwd) -lqbX11 -lX11 -lm
        if test $? = 0 ; then
                $TEMPNAM $2 $3 $4 $5
        fi
fi
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}}
install qbcpp qb2c calib qbrun qbcc $RPM_BUILD_ROOT%{_bindir}
install libqbX11.* $RPM_BUILD_ROOT%{_libdir}

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc ANNOUNCEMENT IAFA-PACKAGE README manual.txt
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libqbX11.so.*
%{_libdir}/libqbX11.a

%changelog
* Sun Dec 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 3.43
- Rebuilt for Fedora
* Mon Jan 15 2007 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.13  2007/01/15 22:43:48  glen
- avoid security hole by not expanding tmpfiles at compile stage
- typo
- add TODO
- rel 4
Revision 1.12  2006/11/09 20:57:28  glen
- strict internal deps
Revision 1.11  2004/08/18 16:30:54  undefine
- fix dir on amd64
Revision 1.10  2004/08/18 16:25:00  undefine
- release 3
Revision 1.9  2003/11/17 11:08:29  qboosh
- use -fPIC for shared library objects (fixes build on alpha)
- fixed -L in scripts, moved libs to /usr/lib, separated static
- release 2
Revision 1.8  2003/05/28 13:01:31  malekith
- massive attack: source-md5
Revision 1.7  2003/05/25 06:26:04  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.6  2002/09/06 23:51:47  undefine
- changed url
- new %doc
- on site this version is 3.41 now...
- stbr
Revision 1.5  2002/02/22 23:29:39  kloczek
- removed all Group fields translations (oure rpm now can handle translating
  Group field using gettext).
Revision 1.4  2002/01/18 02:14:45  kloczek
- perl -pi -e "s/pld-list\@pld.org.pl/feedback\@pld.org.pl/"
Revision 1.3  2001/11/23 13:01:00  qboosh
- s/Copyright/License/, use %__cc instead of directly gcc
Revision 1.2  2001/07/18 08:53:24  undefine
- removed dummy error (rpm hadles $ :)
- added creating shared library
Revision 1.1  2001/07/04 13:11:50  undefine
- initial PLD version. (STB?)
