Summary:	Icon programming language
Summary(pl):	Język programowania Icon
Name:		icon
Version:	9.5.20i
%define	sver	%(echo %{version} | tr -d .)
Release:	1
License:	Public Domain (see README)
Group:		Development/Languages
Source0:	https://github.com/gtownsend/icon/archive/v9.5.20i.tar.gz#/%{name}-%{version}.tar.gz
URL:		http://www.cs.arizona.edu/icon/
BuildRequires:	libX11-devel, libXt-devel

%description
Icon is a very high level general-purpose programming language with
extensive features for processing strings (text) and data structures.
Icon is an imperative, procedural language with a syntax that is
reminiscent of C and Pascal, but with semantics at a much higher
level.

%description -l pl
Icon to język programowania ogólnego przeznaczenia bardzo wysokiego
poziomu z dużymi możliwościami przetwarzania łańcuchów (tekstu) i
struktur danych. Icon jest imperatywnym, proceduralnym językiem ze
składnią przypominającą C i Pascala, ale z semantyką na dużo wyższym
poziomie.

%prep
#setup -q -n %{name}-v%{sver}src
%setup -q

%build
%{__make} X-Configure name=linux

%{__make} CC="%{__cc}" \
	CFLAGS="%{optflags} -D_STDIO_USES_IOSTREAM" \
	XLIBS="-L/usr/%{_lib} -lX11"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/icon/{bin,lib}}
install -m755 bin/* $RPM_BUILD_ROOT%{_libdir}/icon/bin
install lib/* $RPM_BUILD_ROOT%{_libdir}/icon/lib
for f in icon icont iconx vib ; do
ln -sf %{_libdir}/icon/bin/$f $RPM_BUILD_ROOT%{_bindir}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README doc/*
%{_bindir}/*
%{_libdir}/icon

%changelog
* Fri Mar 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 9.5.20i
- Rebuild for Fedora
* Sat Jan 24 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.5  2004/01/24 18:33:24  undefine
- fix build on amd64, release 2
Revision 1.4  2004/01/21 22:29:08  qboosh
- new-style bcond
Revision 1.3  2003/05/28 12:59:08  malekith
- massive attack: source-md5
Revision 1.2  2003/05/25 05:48:49  misi3k
- massive attack s/pld.org.pl/pld-linux.org/
Revision 1.1  2002/12/28 16:26:08  qboosh
- new, patched to use system libXpm
