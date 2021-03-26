%undefine _missing_build_ids_terminate_build
%global debug_package %{nil}

Name:		ch
Version:	7.0.0
Release:	1.bin
Summary:	C/C++ interpreter and shell
Group:		System Environment/Shells
License:	Shareware
URL:		http://www.softintegration.com/
Source0:	http://www.softintegration.com/download/software/release/Linux/chstandard-%{version}.linux2.4.20.intel.tar.gz
Source1:	http://www.softintegration.com/download/software/release/Linux64/chstandard-%{version}.linux64-2.6.18.intel.tar.gz
AutoReqProv:    off

%description
Ch is an embeddable C/C++ interpreter for cross-platform scripting,
shell programming, 2D/3D plotting, numerical computing, and embedded
scripting.

%package demos
Summary:	Various demos
Group:		System Environment/Shells
Requires:	%{name} = %{version}-%{release}

%description demos
Various demos

%package devel
Summary:	Necessary files to extend ch
Group:		System Environment/Shells
Requires:	%{name} = %{version}-%{release}

%description devel
Necessary files to extend ch

%prep
%ifarch x86_64
%setup -q -T -b 1 -n chstandard-%{version}.linux64-2.6.18.intel
%else
%setup -q -T -b 0 -n chstandard-%{version}.linux2.4.20.intel
%endif
tar xfz ch.bin
rm -f ch.bin
echo "CHHOME=%{_libdir}/%{name}" > ch.sh
echo "export CHHOME" >> ch.sh
echo "setenv CHHOME %{_libdir}/%{name}" > ch.csh
chmod 644 docs/chguide.pdf
chmod 644 docs/chinstall.pdf
chmod 644 docs/chref.pdf
rm -f extern/README
rm -rf include/windows
rm -f include/README
chmod 644 lib/libc/ftime.chf
chmod 644 lib/libc/strtoll.chf
chmod 644 lib/libopt/_sleep.chf
rm -f lib/README
rm -f lib/libc/README
rm -f lib/libch/README
rm -f lib/libopt/README

rm -f toolkit/demos/X11/xlib/basicwin/reflect/basicwin
rm -f toolkit/demos/X11/xlib/basicwin/reflect/basicwin.o
rm -f toolkit/demos/OpenGL/book_glx/glut/libglut/libglut.a

%build

%install
# install binary executables and scripts
install -d $RPM_BUILD_ROOT/bin
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/bin
install -p -m755 bin/* $RPM_BUILD_ROOT%{_libdir}/%{name}/bin

# install config files
install -D -p -m 0644 ch.sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/ch.sh
install -D -p -m 0644 ch.csh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d/ch.csh
install -d $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/config
install -p -m644 config/.chlogin $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.chlogout $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.chrc $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.chslogin $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.chslogout $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.chsrc $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.mime.types $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/.mailcap $RPM_BUILD_ROOT%{_sysconfdir}/skel
install -p -m644 config/chlogin $RPM_BUILD_ROOT%{_libdir}/%{name}/config
install -p -m644 config/chrc $RPM_BUILD_ROOT%{_libdir}/%{name}/config
install -p -m644 config/chslogin $RPM_BUILD_ROOT%{_libdir}/%{name}/config
install -p -m644 config/chsrc $RPM_BUILD_ROOT%{_libdir}/%{name}/config

cp -ra demos $RPM_BUILD_ROOT/%{_libdir}/%{name}

# install base libraries
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/dl
install -p -m755 dl/* $RPM_BUILD_ROOT%{_libdir}/%{name}/dl

#install files, necessary to extend ch
install -D -p -m644 extern/include/ch.h $RPM_BUILD_ROOT%{_libdir}/%{name}/extern/include/ch.h
install -D -p -m644 extern/lib/libchsdk.a $RPM_BUILD_ROOT%{_libdir}/%{name}/extern/lib/libchsdk.a

cp -ra include $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -ra lib $RPM_BUILD_ROOT%{_libdir}/%{name}
cp -ra package $RPM_BUILD_ROOT%{_libdir}/%{name}
install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/sbin

# install man-pages
install -D -p -m644 docs/man/man1/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install -p -m644 docs/man/man1/createpkg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 docs/man/man1/foreach.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 docs/man/man1/installpkg.1 $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m644 docs/man/man1/pkginstall.1 $RPM_BUILD_ROOT%{_mandir}/man1

cd $RPM_BUILD_ROOT/bin
ln -s %{_libdir}/%{name}/bin/ch ch
ln -s %{_libdir}/%{name}/bin/chs chs

%post
HASCH=""
if [ ! -f /etc/shells ]; then
	> /etc/shells
fi
(while read line ; do
	if [ "$line" = "/bin/ch" ]; then
		HASCH=1
	fi
done
if [ -z "$HASCH" ]; then
	echo "/bin/ch" >> /etc/shells
fi) < /etc/shells

%postun
if [ "$1" = 0 ]; then
	/bin/grep -v '^/bin/ch$'  /etc/shells > /etc/shells.new && /bin/mv /etc/shells{.new,}
fi

%files
%doc README license.txt docs/chguide.pdf docs/chinstall.pdf docs/chref.pdf docs/chsdk.pdf
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/bin
%dir %{_libdir}/%{name}/config
%dir %{_libdir}/%{name}/dl
%dir %{_libdir}/%{name}/include
%dir %{_libdir}/%{name}/lib
%dir %{_libdir}/%{name}/package
%dir %{_libdir}/%{name}/sbin
%{_sysconfdir}/profile.d/ch.sh
%{_sysconfdir}/profile.d/ch.csh
%config(noreplace) %{_sysconfdir}/skel/.chlogin
%config(noreplace) %{_sysconfdir}/skel/.chlogout
%config(noreplace) %{_sysconfdir}/skel/.chrc
%config(noreplace) %{_sysconfdir}/skel/.chslogin
%config(noreplace) %{_sysconfdir}/skel/.chslogout
%config(noreplace) %{_sysconfdir}/skel/.chsrc
%config(noreplace) %{_sysconfdir}/skel/.mailcap
%config(noreplace) %{_sysconfdir}/skel/.mime.types
%config(noreplace) %{_libdir}/%{name}/config/chlogin
%config(noreplace) %{_libdir}/%{name}/config/chrc
%config(noreplace) %{_libdir}/%{name}/config/chslogin
%config(noreplace) %{_libdir}/%{name}/config/chsrc
/bin/ch
/bin/chs
%{_libdir}/%{name}/bin/*
%{_libdir}/%{name}/dl/*
%{_libdir}/%{name}/extern/*
%{_libdir}/%{name}/include/*
%{_libdir}/%{name}/lib/*
%{_mandir}/man1/*

%files demos
%{_libdir}/%{name}/demos
%{_libdir}/%{name}/package/sample

%files devel
%dir %{_libdir}/%{name}/extern
%dir %{_libdir}/%{name}/extern/include
%dir %{_libdir}/%{name}/extern/lib
%{_libdir}/%{name}/extern/include/ch.h
%{_libdir}/%{name}/extern/lib/libchsdk.a

%changelog
* Thu Jan 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 7.0.0
- Rebuild binary package

* Fri Nov  7 2008 Peter Lemenkov <lemenkov@gmail.com> 6.1.0.13631-2
- Added profile files for bash and csh

* Thu Oct 30 2008 Peter Lemenkov <lemenkov@gmail.com> 6.1.0.13631-1
- Initial package
