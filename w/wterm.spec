%undefine _debugsource_packages

Summary:	Terminal emulator for WindowMaker
Name:		wterm
Version:	6.2.9
License:	GPL
Group:		X11/Applications
Source0:	http://sourceforge.net/projects/wterm/files/wterm/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/wterm/
Release:       23.1
BuildRequires:  libpng-devel
BuildRequires:  giflib-devel
BuildRequires:  libX11-devel libXt-devel WINGs-devel
BuildRequires:  WindowMaker-devel 
BuildRequires:  ghostscript-core

%description
Wterm is a rxvt clone designed for WindowMaker. It has some
interesting featrues like very fast transparency or transparent NeXT
scroll bar.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
	--enable-xgetdefault \
	--enable-transparency \
	--enable-next-scroll \
	--enable-ttygid \
	--enable-xpm-background \
	--with-xpm-library=%{_libdir} \
	--enable-menubar \
	--enable-wtmp \
	--enable-utmp

%{__make}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README doc/{BUGS,FAQ,README*,TODO}
%attr(755,root,root) %{_bindir}/wterm
%{_mandir}/man1/wterm.1*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2.9
- Rebuilt for Fedora
* Fri Jan 30 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
$Log: wterm.spec,v $
Revision 1.8  2004/01/30 12:54:00  jajcus
- Release: 2
- pass Xpm library path to %configure (it won't find it on AMD64 otherwise)
Revision 1.7  2004/01/29 21:12:31  gausus
- cosmetics
- stbr for Ac
- dedicated 2 djurban's obsession ;P
Revision 1.6  2003/10/20 13:32:11  qboosh
- added files, BR: WindowMaker-devel,XFree86-devel
Revision 1.5  2003/10/14 19:10:45  gausus
- small fixes
Revision 1.4  2003/10/14 10:18:25  ankry
- better pl
Revision 1.3  2003/10/14 07:27:30  gausus
- Happy Birthday to Averne - wszystkiego naj naj naj stary :D
- Some features added
Revision 1.2  2003/10/13 18:41:01  djurban
- removed ac/am bsyste macros (this apps has a screwed buildsystem)
- create rpmbuildroot
- use %configure2_13
- fixed changelog
- removed %files stuff
- gaus please do rpmbuild -bi wterm.spec
Revision 1.1  2003/10/13 18:29:17  gausus
- Initial release of wterm
